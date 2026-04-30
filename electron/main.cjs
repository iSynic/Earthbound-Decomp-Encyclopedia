const { app, BrowserWindow, dialog, ipcMain, shell } = require("electron");
const { spawnSync } = require("node:child_process");
const crypto = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const zlib = require("node:zlib");

const EXPECTED_HEADERLESS_SIZE = 3145728;
const EXPECTED_HEADERED_SIZE = EXPECTED_HEADERLESS_SIZE + 512;
const EXPECTED_HEADERLESS_SHA1 = "d67a8ef36ef616bc39306aa1b486e1bd3047815a";
const BANK_SIZE = 0x10000;
const C0AB06_LOADER_OFFSET = 0x00ab06;
const C0AB06_LOADER_LENGTH = 162;
const SPC_SIGNATURE = Buffer.from("SNES-SPC700 Sound File Data v0.30", "ascii");
const AUDIO_BOOTSTRAP_PACK_ID = 1;
const FAMILY_DEFINITIONS = [
  {
    id: "source",
    label: "Source Code",
    directoryKey: "source",
    summary: "Generated local source scaffolds, ROM bank index, and byte-equivalence assembly entry points.",
    exportKinds: ["asm", "json", "markdown", "zip"]
  },
  {
    id: "graphics",
    label: "Graphics And Sprites",
    directoryKey: "graphics",
    summary: "ROM bank graphics index and renderer handoff manifest for local sprite/tile preview generation.",
    exportKinds: ["json", "markdown", "zip"]
  },
  {
    id: "maps",
    label: "Maps And Tilesets",
    directoryKey: "maps",
    summary: "Map and tileset extraction handoff manifest for local scene, FTS, palette, and collision previews.",
    exportKinds: ["json", "markdown", "zip"]
  },
  {
    id: "audio",
    label: "Music And Audio",
    directoryKey: "audio",
    summary: "Playback/export manifest for local SPC/WAV renderer stages and audio contract validation.",
    exportKinds: ["json", "spc", "wav", "zip"]
  },
  {
    id: "tables",
    label: "Tables And Data Contracts",
    directoryKey: "manifests",
    summary: "ROM header, vector, bank, and source-safe data-contract manifests.",
    exportKinds: ["json", "markdown", "zip"]
  }
];
const FAMILY_BY_ID = new Map(FAMILY_DEFINITIONS.map((family) => [family.id, family]));
const CRC_TABLE = new Uint32Array(256);
for (let n = 0; n < CRC_TABLE.length; n += 1) {
  let c = n;
  for (let k = 0; k < 8; k += 1) {
    c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
  }
  CRC_TABLE[n] = c >>> 0;
}

function createWindow() {
  const win = new BrowserWindow({
    width: 1320,
    height: 900,
    minWidth: 980,
    minHeight: 640,
    backgroundColor: "#111110",
    title: "EarthBound Decomp Encyclopedia",
    webPreferences: {
      preload: path.join(__dirname, "preload.cjs"),
      contextIsolation: true,
      nodeIntegration: false
    }
  });

  win.loadFile(path.join(__dirname, "..", "public", "index.html"));
}

function workspaceRootForSha1(sha1) {
  return path.join(app.getPath("userData"), "local-workspaces", sha1);
}

function ensureDir(targetPath) {
  fs.mkdirSync(targetPath, { recursive: true });
}

function writeJson(filePath, value) {
  ensureDir(path.dirname(filePath));
  fs.writeFileSync(filePath, JSON.stringify(value, null, 2) + "\n", "utf8");
}

function writeText(filePath, value) {
  ensureDir(path.dirname(filePath));
  fs.writeFileSync(filePath, value, "utf8");
}

function sha1Buffer(buffer) {
  return crypto.createHash("sha1").update(buffer).digest("hex");
}

function readU16Le(buffer, offset) {
  return buffer[offset] | (buffer[offset + 1] << 8);
}

function payloadForRomBuffer(data) {
  return data.length === EXPECTED_HEADERED_SIZE ? data.subarray(512) : data;
}

function verifyRom(filePath) {
  const data = fs.readFileSync(filePath);
  const size = data.length;
  const headered = size === EXPECTED_HEADERED_SIZE;
  const headerless = size === EXPECTED_HEADERLESS_SIZE;
  const payload = payloadForRomBuffer(data);
  const payloadSha1 = sha1Buffer(payload);
  const fileSha1 = sha1Buffer(data);
  const sha1Ok = payloadSha1 === EXPECTED_HEADERLESS_SHA1;
  return {
    path: filePath,
    fileName: path.basename(filePath),
    size,
    headered,
    headerless,
    sizeOk: headered || headerless,
    fileSha1,
    headerlessSha1: payloadSha1,
    sha1Ok,
    expectedHeaderlessSha1: EXPECTED_HEADERLESS_SHA1,
    expectedHeaderlessSize: EXPECTED_HEADERLESS_SIZE,
    expectedHeaderedSize: EXPECTED_HEADERED_SIZE,
    header: readRomHeader(payload),
    verifiedAt: new Date().toISOString()
  };
}

function readRomHeader(payload) {
  if (payload.length < 0x10000) {
    return null;
  }
  return {
    title: payload.subarray(0xffc0, 0xffd5).toString("ascii").replace(/\0/g, "").trim(),
    mapMode: hexByte(payload[0xffd5]),
    cartType: hexByte(payload[0xffd6]),
    romSizeCode: hexByte(payload[0xffd7]),
    sramSizeCode: hexByte(payload[0xffd8]),
    countryCode: hexByte(payload[0xffd9]),
    licenseCode: hexByte(payload[0xffda]),
    version: hexByte(payload[0xffdb]),
    complementCheck: hexWord(readU16Le(payload, 0xffdc)),
    checksum: hexWord(readU16Le(payload, 0xffde)),
    checksumXorOk: (readU16Le(payload, 0xffdc) ^ readU16Le(payload, 0xffde)) === 0xffff
  };
}

function hexByte(value) {
  return `0x${Number(value || 0).toString(16).toUpperCase().padStart(2, "0")}`;
}

function hexWord(value) {
  return `0x${Number(value || 0).toString(16).toUpperCase().padStart(4, "0")}`;
}

function hexLong(value) {
  return `0x${Number(value || 0).toString(16).toUpperCase().padStart(6, "0")}`;
}

function pngChunk(kind, data) {
  const length = Buffer.alloc(4);
  length.writeUInt32BE(data.length, 0);
  const crc = Buffer.alloc(4);
  crc.writeUInt32BE(crc32(Buffer.concat([kind, data])), 0);
  return Buffer.concat([length, kind, data, crc]);
}

function writePngRgba(filePath, width, height, rgba) {
  const header = Buffer.from("\x89PNG\r\n\x1a\n", "binary");
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(width, 0);
  ihdr.writeUInt32BE(height, 4);
  ihdr[8] = 8;
  ihdr[9] = 6;
  ihdr[10] = 0;
  ihdr[11] = 0;
  ihdr[12] = 0;
  const stride = width * 4;
  const raw = Buffer.alloc((stride + 1) * height);
  for (let y = 0; y < height; y += 1) {
    raw[y * (stride + 1)] = 0;
    rgba.copy(raw, y * (stride + 1) + 1, y * stride, (y + 1) * stride);
  }
  ensureDir(path.dirname(filePath));
  fs.writeFileSync(filePath, Buffer.concat([
    header,
    pngChunk(Buffer.from("IHDR"), ihdr),
    pngChunk(Buffer.from("IDAT"), zlib.deflateSync(raw)),
    pngChunk(Buffer.from("IEND"), Buffer.alloc(0))
  ]));
}

function snesPaletteFromBytes(data) {
  const colors = [];
  for (let offset = 0; offset + 1 < data.length && colors.length < 16; offset += 2) {
    const word = data[offset] | (data[offset + 1] << 8);
    const r = (word & 0x1f) << 3;
    const g = ((word >> 5) & 0x1f) << 3;
    const b = ((word >> 10) & 0x1f) << 3;
    colors.push([r | (r >> 5), g | (g >> 5), b | (b >> 5), colors.length === 0 ? 0 : 255]);
  }
  while (colors.length < 16) {
    const value = Math.round((colors.length / 15) * 255);
    colors.push([value, value, value, colors.length === 0 ? 0 : 255]);
  }
  return colors;
}

function decodeSnes4bppTile(tile) {
  const rows = [];
  for (let y = 0; y < 8; y += 1) {
    const p0 = tile[y * 2];
    const p1 = tile[y * 2 + 1];
    const p2 = tile[16 + y * 2];
    const p3 = tile[16 + y * 2 + 1];
    const row = [];
    for (let bit = 7; bit >= 0; bit -= 1) {
      row.push(((p0 >> bit) & 1) | (((p1 >> bit) & 1) << 1) | (((p2 >> bit) & 1) << 2) | (((p3 >> bit) & 1) << 3));
    }
    rows.push(row);
  }
  return rows;
}

function fillRgba(rgba, color) {
  for (let index = 0; index < rgba.length; index += 4) {
    rgba[index] = color[0];
    rgba[index + 1] = color[1];
    rgba[index + 2] = color[2];
    rgba[index + 3] = color[3];
  }
}

function drawSnes4bppTile(rgba, width, tile, tileLeft, tileTop, scale, palette) {
  for (let y = 0; y < 8; y += 1) {
    for (let x = 0; x < 8; x += 1) {
      const color = palette[tile[y][x]] || [0, 0, 0, 255];
      for (let sy = 0; sy < scale; sy += 1) {
        for (let sx = 0; sx < scale; sx += 1) {
          const outX = tileLeft + x * scale + sx;
          const outY = tileTop + y * scale + sy;
          const offset = (outY * width + outX) * 4;
          rgba[offset] = color[0];
          rgba[offset + 1] = color[1];
          rgba[offset + 2] = color[2];
          rgba[offset + 3] = color[3];
        }
      }
    }
  }
}

function writeSnes4bppPreview(filePath, data, options = {}) {
  const tilesPerRow = options.tilesPerRow || 16;
  const scale = options.scale || 2;
  const palette = options.palette || snesPaletteFromBytes(Buffer.alloc(0));
  const tileCount = Math.floor(data.length / 32);
  const tileRows = Math.max(1, Math.ceil(tileCount / tilesPerRow));
  const width = tilesPerRow * 8 * scale;
  const height = tileRows * 8 * scale;
  const rgba = Buffer.alloc(width * height * 4);
  fillRgba(rgba, [15, 15, 14, 255]);
  for (let tileIndex = 0; tileIndex < tileCount; tileIndex += 1) {
    const tile = decodeSnes4bppTile(data.subarray(tileIndex * 32, tileIndex * 32 + 32));
    const tileLeft = (tileIndex % tilesPerRow) * 8 * scale;
    const tileTop = Math.floor(tileIndex / tilesPerRow) * 8 * scale;
    drawSnes4bppTile(rgba, width, tile, tileLeft, tileTop, scale, palette);
  }
  writePngRgba(filePath, width, height, rgba);
  return { width, height, tileCount };
}

function writeSnes4bppFrameSheet(filePath, data, options = {}) {
  const frameTileColumns = options.frameTileColumns || 2;
  const frameTileRows = options.frameTileRows || 3;
  const framesPerRow = options.framesPerRow || 2;
  const scale = options.scale || 4;
  const palette = options.palette || snesPaletteFromBytes(Buffer.alloc(0));
  const tileCount = Math.floor(data.length / 32);
  const tilesPerFrame = frameTileColumns * frameTileRows;
  const frameCount = Math.max(1, Math.floor(tileCount / tilesPerFrame));
  const frameRows = Math.max(1, Math.ceil(frameCount / framesPerRow));
  const frameWidth = frameTileColumns * 8 * scale;
  const frameHeight = frameTileRows * 8 * scale;
  const gutter = options.gutter ?? 4;
  const width = framesPerRow * frameWidth + (framesPerRow - 1) * gutter;
  const height = frameRows * frameHeight + (frameRows - 1) * gutter;
  const rgba = Buffer.alloc(width * height * 4);
  fillRgba(rgba, [15, 15, 14, 255]);
  for (let frameIndex = 0; frameIndex < frameCount; frameIndex += 1) {
    const frameLeft = (frameIndex % framesPerRow) * (frameWidth + gutter);
    const frameTop = Math.floor(frameIndex / framesPerRow) * (frameHeight + gutter);
    for (let frameTileIndex = 0; frameTileIndex < tilesPerFrame; frameTileIndex += 1) {
      const tileIndex = frameIndex * tilesPerFrame + frameTileIndex;
      if (tileIndex >= tileCount) {
        continue;
      }
      const tile = decodeSnes4bppTile(data.subarray(tileIndex * 32, tileIndex * 32 + 32));
      const tileLeft = frameLeft + (frameTileIndex % frameTileColumns) * 8 * scale;
      const tileTop = frameTop + Math.floor(frameTileIndex / frameTileColumns) * 8 * scale;
      drawSnes4bppTile(rgba, width, tile, tileLeft, tileTop, scale, palette);
    }
  }
  writePngRgba(filePath, width, height, rgba);
  return {
    width,
    height,
    tileCount,
    frameCount,
    frameTileColumns,
    frameTileRows,
    framesPerRow,
    layout: "candidate_2x3_tiles_per_frame_row_major"
  };
}

function spriteFrameLayout(data, options = {}) {
  const frameTileColumns = options.frameTileColumns || 2;
  const frameTileRows = options.frameTileRows || 3;
  const tileCount = Math.floor(data.length / 32);
  const tilesPerFrame = frameTileColumns * frameTileRows;
  return {
    tileCount,
    tilesPerFrame,
    frameTileColumns,
    frameTileRows,
    frameWidth: frameTileColumns * 8,
    frameHeight: frameTileRows * 8,
    frameCount: Math.max(1, Math.floor(tileCount / tilesPerFrame))
  };
}

function drawSnes4bppSpriteFrame(rgba, width, data, frameIndex, left, top, options = {}) {
  const scale = options.scale || 1;
  const palette = options.palette || snesPaletteFromBytes(Buffer.alloc(0));
  const layout = spriteFrameLayout(data, options);
  for (let frameTileIndex = 0; frameTileIndex < layout.tilesPerFrame; frameTileIndex += 1) {
    const tileIndex = frameIndex * layout.tilesPerFrame + frameTileIndex;
    if (tileIndex >= layout.tileCount) {
      continue;
    }
    const tile = decodeSnes4bppTile(data.subarray(tileIndex * 32, tileIndex * 32 + 32));
    const tileLeft = left + (frameTileIndex % layout.frameTileColumns) * 8 * scale;
    const tileTop = top + Math.floor(frameTileIndex / layout.frameTileColumns) * 8 * scale;
    drawSnes4bppTile(rgba, width, tile, tileLeft, tileTop, scale, palette);
  }
}

function writeSnes4bppSpriteSheet(filePath, data, options = {}) {
  const layout = spriteFrameLayout(data, options);
  const scale = options.scale || 1;
  const palette = options.palette || snesPaletteFromBytes(Buffer.alloc(0));
  const framesPerRow = options.framesPerRow || layout.frameCount;
  const gutter = options.gutter ?? 0;
  const frameWidth = layout.frameWidth * scale;
  const frameHeight = layout.frameHeight * scale;
  const frameRows = Math.max(1, Math.ceil(layout.frameCount / framesPerRow));
  const width = framesPerRow * frameWidth + Math.max(0, framesPerRow - 1) * gutter;
  const height = frameRows * frameHeight + Math.max(0, frameRows - 1) * gutter;
  const rgba = Buffer.alloc(width * height * 4);
  fillRgba(rgba, options.background || [0, 0, 0, 0]);
  for (let frameIndex = 0; frameIndex < layout.frameCount; frameIndex += 1) {
    const frameLeft = (frameIndex % framesPerRow) * (frameWidth + gutter);
    const frameTop = Math.floor(frameIndex / framesPerRow) * (frameHeight + gutter);
    drawSnes4bppSpriteFrame(rgba, width, data, frameIndex, frameLeft, frameTop, {
      ...options,
      scale,
      palette
    });
  }
  writePngRgba(filePath, width, height, rgba);
  return {
    width,
    height,
    tileCount: layout.tileCount,
    frameCount: layout.frameCount,
    frameWidth: layout.frameWidth,
    frameHeight: layout.frameHeight,
    frameTileColumns: layout.frameTileColumns,
    frameTileRows: layout.frameTileRows,
    framesPerRow,
    scale,
    layout: "overworld_sprite_2x3_frames_row_major"
  };
}

function decodedSpriteFrameRows(data, options = {}) {
  const layout = spriteFrameLayout(data, options);
  const frames = [];
  for (let frameIndex = 0; frameIndex < layout.frameCount; frameIndex += 1) {
    const rows = Array.from({ length: layout.frameHeight }, () => Array.from({ length: layout.frameWidth }, () => 0));
    for (let frameTileIndex = 0; frameTileIndex < layout.tilesPerFrame; frameTileIndex += 1) {
      const tileIndex = frameIndex * layout.tilesPerFrame + frameTileIndex;
      if (tileIndex >= layout.tileCount) {
        continue;
      }
      const tile = decodeSnes4bppTile(data.subarray(tileIndex * 32, tileIndex * 32 + 32));
      const tileLeft = (frameTileIndex % layout.frameTileColumns) * 8;
      const tileTop = Math.floor(frameTileIndex / layout.frameTileColumns) * 8;
      for (let y = 0; y < 8; y += 1) {
        for (let x = 0; x < 8; x += 1) {
          rows[tileTop + y][tileLeft + x] = tile[y][x];
        }
      }
    }
    frames.push({
      index: frameIndex,
      width: layout.frameWidth,
      height: layout.frameHeight,
      paletteIndexRows: rows.map((row) => row.map((value) => value.toString(16).toUpperCase()).join(""))
    });
  }
  return frames;
}

function writeSpriteContactSheet(filePath, sprites, options = {}) {
  const scale = options.scale || 2;
  const palette = options.palette || snesPaletteFromBytes(Buffer.alloc(0));
  const columns = options.columns || 8;
  const framesPerSpriteRow = options.framesPerSpriteRow || 2;
  const maxFrameRows = options.maxFrameRows || 2;
  const frameWidth = 16 * scale;
  const frameHeight = 24 * scale;
  const frameGutter = options.frameGutter ?? 2;
  const cellPadding = options.cellPadding ?? 4;
  const cellWidth = cellPadding * 2 + framesPerSpriteRow * frameWidth + (framesPerSpriteRow - 1) * frameGutter;
  const cellHeight = cellPadding * 2 + maxFrameRows * frameHeight + (maxFrameRows - 1) * frameGutter;
  const rows = Math.max(1, Math.ceil(sprites.length / columns));
  const width = columns * cellWidth;
  const height = rows * cellHeight;
  const rgba = Buffer.alloc(width * height * 4);
  fillRgba(rgba, options.background || [13, 13, 12, 255]);
  for (const [spriteIndex, sprite] of sprites.entries()) {
    const cellLeft = (spriteIndex % columns) * cellWidth + cellPadding;
    const cellTop = Math.floor(spriteIndex / columns) * cellHeight + cellPadding;
    const layout = spriteFrameLayout(sprite.bytes);
    const visibleFrames = Math.min(layout.frameCount, framesPerSpriteRow * maxFrameRows);
    for (let frameIndex = 0; frameIndex < visibleFrames; frameIndex += 1) {
      const frameLeft = cellLeft + (frameIndex % framesPerSpriteRow) * (frameWidth + frameGutter);
      const frameTop = cellTop + Math.floor(frameIndex / framesPerSpriteRow) * (frameHeight + frameGutter);
      drawSnes4bppSpriteFrame(rgba, width, sprite.bytes, frameIndex, frameLeft, frameTop, { scale, palette });
    }
  }
  writePngRgba(filePath, width, height, rgba);
  return {
    width,
    height,
    spriteCount: sprites.length,
    columns,
    scale,
    cellWidth,
    cellHeight,
    layout: "bank_contact_sheet_first_four_2x3_frames"
  };
}

function appAssetManifestPath(bank) {
  return path.join(__dirname, "..", "asset-manifests", `bank-${bank.toLowerCase()}-assets.json`);
}

function bundledAudioBackendRoot() {
  if (app.isPackaged) {
    return path.join(process.resourcesPath, "app.asar.unpacked", "audio-backend");
  }
  return path.join(__dirname, "..", "audio-backend");
}

function packagedSourceTemplateRoot() {
  return path.join(__dirname, "..", "source-template");
}

function copyDirectoryRecursive(sourceDir, targetDir) {
  if (!fs.existsSync(sourceDir)) {
    throw new Error(`Packaged source template is missing: ${sourceDir}`);
  }
  ensureDir(targetDir);
  for (const entry of fs.readdirSync(sourceDir, { withFileTypes: true })) {
    const sourcePath = path.join(sourceDir, entry.name);
    const targetPath = path.join(targetDir, entry.name);
    if (entry.isDirectory()) {
      copyDirectoryRecursive(sourcePath, targetPath);
    } else if (entry.isFile()) {
      ensureDir(path.dirname(targetPath));
      fs.copyFileSync(sourcePath, targetPath);
    }
  }
}

function bundledAudioBackendStatus() {
  const root = bundledAudioBackendRoot();
  const aresHarness = path.join(root, "bin", "earthbound_ares_audio_harness.exe");
  const libgmeHarness = path.join(root, "bin", "earthbound_libgme_audio_harness.exe");
  const c0ab06Harness = path.join(root, "bin", "earthbound_ares_c0ab06_loader_handshake.exe");
  const contract = path.join(root, "manifests", "audio-backend-contract.json");
  const exportPlan = path.join(root, "manifests", "audio-export-plan.json");
  const tools = [
    "build_audio_backend_jobs_from_spc_index.py",
    "run_audio_backend_batch.py",
    "build_audio_playback_export_manifest.py",
    "validate_audio_playback_export_manifest.py"
  ].map((name) => path.join(root, "tools", name));
  return {
    root,
    bundled: fs.existsSync(root),
    aresHarness: { path: aresHarness, present: fs.existsSync(aresHarness) },
    libgmeHarness: { path: libgmeHarness, present: fs.existsSync(libgmeHarness) },
    c0ab06Harness: { path: c0ab06Harness, present: fs.existsSync(c0ab06Harness) },
    contract: { path: contract, present: fs.existsSync(contract) },
    exportPlan: { path: exportPlan, present: fs.existsSync(exportPlan) },
    orchestrationTools: tools.map((toolPath) => ({ path: toolPath, present: fs.existsSync(toolPath) }))
  };
}

function loadAppAssetManifest(bank) {
  const manifestPath = appAssetManifestPath(bank);
  if (!fs.existsSync(manifestPath)) {
    throw new Error(`Packaged asset manifest is missing for bank ${bank}.`);
  }
  return JSON.parse(fs.readFileSync(manifestPath, "utf8"));
}

function fileOffsetFromSnesRange(rangeStart) {
  const match = String(rangeStart || "").match(/^([C-F][0-9A-F]):([0-9A-F]{4,5})$/i);
  if (!match) {
    throw new Error(`Unsupported SNES range address: ${rangeStart}`);
  }
  const bankOffset = Number.parseInt(match[2], 16);
  if (bankOffset < 0 || bankOffset > BANK_SIZE) {
    throw new Error(`SNES range bank offset is out of bounds: ${rangeStart}`);
  }
  return (Number.parseInt(match[1], 16) - 0xc0) * BANK_SIZE + bankOffset;
}

function parseSnesRange(range) {
  const [start, end] = String(range || "").split("..");
  if (!start || !end) {
    throw new Error(`Unsupported SNES range: ${range}`);
  }
  const startOffset = fileOffsetFromSnesRange(start);
  const endOffset = fileOffsetFromSnesRange(end);
  return { startOffset, endOffset, length: endOffset - startOffset };
}

function generateOverworldSpritePreviews(outputDir, payload) {
  const spriteDir = path.join(outputDir, "overworld-sprites");
  const palette = snesPaletteFromBytes(payload.subarray(fileOffsetFromSnesRange("C3:0000"), fileOffsetFromSnesRange("C3:0020")));
  const previewEntries = [];
  const spritesByBank = new Map();
  writeJson(path.join(spriteDir, "palette-00.json"), {
    schema: "earthbound-decomp.generated-snes-palette.v1",
    generatedAt: new Date().toISOString(),
    sourceRange: "C3:0000..C3:0020",
    colorCount: palette.length,
    colors: palette.map(([r, g, b, a], index) => ({
      index,
      rgba: [r, g, b, a],
      hex: `#${[r, g, b].map((value) => value.toString(16).padStart(2, "0")).join("").toUpperCase()}`
    }))
  });
  for (const bank of ["d1", "d2", "d3", "d4", "d5"]) {
    const assetManifest = loadAppAssetManifest(bank);
    for (const asset of assetManifest.assets || []) {
      const source = asset.source || {};
      if (asset.category !== "graphics" || source.type !== "rom-range" || !source.range || !/^SPRITE_/i.test(String(asset.title || ""))) {
        continue;
      }
      const range = parseSnesRange(source.range);
      if (range.length <= 0 || range.length % 32 !== 0) {
        continue;
      }
      const spriteId = String(asset.title || asset.id || previewEntries.length).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
      const spriteBytes = payload.subarray(range.startOffset, range.endOffset);
      const rawOutput = (asset.outputs || []).find((entry) => entry.kind === "raw" && String(entry.path || "").endsWith(".gfx"));
      const paletteOutput = (asset.outputs || []).find((entry) => entry.kind === "snes_4bpp_tiles_palette_png");
      const rawRelativePath = rawOutput?.path ? `raw/${rawOutput.path}` : `raw/${bank}/overworld_sprites/gfx/${spriteId}.gfx`;
      const tileRelativePath = paletteOutput?.path ? `tiles/${paletteOutput.path}` : `tiles/${bank}/${spriteId}_palette_00_preview.png`;
      const frameRelativePath = `overworld-sprites/frames/${bank}/${spriteId}_palette_00_frames_2x3.png`;
      const sheetRelativePath = `overworld-sprites/sheets/${bank}/${spriteId}_palette_00_sheet.png`;
      const sheetPreviewRelativePath = `overworld-sprites/sheets-preview/${bank}/${spriteId}_palette_00_sheet_preview.png`;
      const decodedRelativePath = `overworld-sprites/decoded/${bank}/${spriteId}_palette_00_sheet.json`;
      const rawPath = path.join(outputDir, rawRelativePath);
      ensureDir(path.dirname(rawPath));
      fs.writeFileSync(rawPath, spriteBytes);
      const tileImage = writeSnes4bppPreview(path.join(outputDir, tileRelativePath), spriteBytes, {
        tilesPerRow: paletteOutput?.columns || 8,
        scale: 3,
        palette
      });
      const frameImage = writeSnes4bppFrameSheet(path.join(outputDir, frameRelativePath), spriteBytes, {
        frameTileColumns: 2,
        frameTileRows: 3,
        framesPerRow: 2,
        scale: 4,
        palette
      });
      const spriteSheet = writeSnes4bppSpriteSheet(path.join(outputDir, sheetRelativePath), spriteBytes, {
        scale: 1,
        gutter: 0,
        palette
      });
      const spriteSheetPreview = writeSnes4bppSpriteSheet(path.join(outputDir, sheetPreviewRelativePath), spriteBytes, {
        scale: 4,
        gutter: 4,
        palette,
        background: [13, 13, 12, 255]
      });
      writeJson(path.join(outputDir, decodedRelativePath), {
        schema: "earthbound-decomp.generated-overworld-sprite-sheet.v1",
        generatedAt: new Date().toISOString(),
        id: asset.id,
        title: asset.title,
        bank: bank.toUpperCase(),
        sourceRange: source.range,
        rawPath: rawRelativePath,
        sheetPath: sheetRelativePath,
        previewPath: sheetPreviewRelativePath,
        palette: {
          sourceRange: "C3:0000..C3:0020",
          colors: palette.map(([r, g, b, a], index) => ({
            index,
            rgba: [r, g, b, a],
            hex: `#${[r, g, b].map((value) => value.toString(16).padStart(2, "0")).join("").toUpperCase()}`
          }))
        },
        sheet: spriteSheet,
        frames: decodedSpriteFrameRows(spriteBytes)
      });
      const spriteRecord = {
        id: asset.id,
        title: asset.title,
        bank: bank.toUpperCase(),
        sourceRange: source.range,
        bytes: range.length,
        rawPath: rawRelativePath,
        tileAtlasPath: tileRelativePath,
        frameSheetPath: frameRelativePath,
        sheetPath: sheetRelativePath,
        sheetPreviewPath: sheetPreviewRelativePath,
        decodedSheetPath: decodedRelativePath,
        path: sheetPreviewRelativePath,
        palette: "C3:0000..C3:0020",
        tileAtlas: tileImage,
        frameSheet: frameImage,
        spriteSheet,
        spriteSheetPreview,
        width: spriteSheetPreview.width,
        height: spriteSheetPreview.height,
        tileCount: spriteSheet.tileCount,
        frameCount: spriteSheet.frameCount,
        layoutConfidence: "predigested_row_major_overworld_sprite_sheet_from_asset_payload"
      };
      if (!spritesByBank.has(bank)) {
        spritesByBank.set(bank, []);
      }
      spritesByBank.get(bank).push({ ...spriteRecord, bytes: spriteBytes });
      previewEntries.push({
        ...spriteRecord,
        bytes: range.length
      });
    }
  }
  const groupSheets = [];
  for (const [bank, sprites] of spritesByBank.entries()) {
    const bankSheetRelativePath = `overworld-sprites/groups/by-bank/${bank}_palette_00_contact_sheet.png`;
    const contactSheet = writeSpriteContactSheet(path.join(outputDir, bankSheetRelativePath), sprites, {
      scale: 2,
      columns: 8,
      palette
    });
    groupSheets.push({
      id: `${bank}-palette-00-contact-sheet`,
      title: `${bank.toUpperCase()} palette 00 sprite contact sheet`,
      bank: bank.toUpperCase(),
      path: bankSheetRelativePath,
      spriteCount: sprites.length,
      sheet: contactSheet
    });
  }
  const allSprites = [...spritesByBank.values()].flat();
  const allSheetRelativePath = "overworld-sprites/groups/all-overworld-sprites_palette_00_contact_sheet.png";
  if (allSprites.length) {
    const allSheet = writeSpriteContactSheet(path.join(outputDir, allSheetRelativePath), allSprites, {
      scale: 2,
      columns: 10,
      palette
    });
    groupSheets.unshift({
      id: "all-overworld-sprites-palette-00-contact-sheet",
      title: "All overworld sprites palette 00 contact sheet",
      bank: "ALL",
      path: allSheetRelativePath,
      spriteCount: allSprites.length,
      sheet: allSheet
    });
  }
  writeJson(path.join(spriteDir, "index.json"), {
    schema: "earthbound-decomp.generated-overworld-sprite-previews.v1",
    generatedAt: new Date().toISOString(),
    palette: "C3:0000..C3:0020",
    previewCount: previewEntries.length,
    generatedFiles: {
      rawGfx: previewEntries.length,
      tileAtlases: previewEntries.length,
      candidateFrameSheets: previewEntries.length,
      spriteSheets: previewEntries.length,
      decodedSpriteSheets: previewEntries.length,
      groupContactSheets: groupSheets.length
    },
    groups: {
      byBank: [...spritesByBank.entries()].map(([bank, sprites]) => ({
        bank: bank.toUpperCase(),
        spriteCount: sprites.length,
        sheetPath: `overworld-sprites/groups/by-bank/${bank}_palette_00_contact_sheet.png`
      })),
      sheets: groupSheets
    },
    previews: previewEntries
  });
  return previewEntries;
}

function extractAudioPacks(outputDir, payload) {
  const packEntries = [];
  for (const bank of ["e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "ea", "eb", "ec", "ed", "ee"]) {
    const assetManifest = loadAppAssetManifest(bank);
    for (const asset of assetManifest.assets || []) {
      const source = asset.source || {};
      const rawOutput = (asset.outputs || []).find((entry) => entry.kind === "raw" && String(entry.path || "").endsWith(".ebm"));
      if (asset.category !== "audio" || source.type !== "rom-range" || !source.range || !rawOutput?.path) {
        continue;
      }
      const range = parseSnesRange(source.range);
      if (range.length <= 0) {
        continue;
      }
      const relativePath = `audio-packs/${rawOutput.path}`;
      const filePath = path.join(outputDir, relativePath);
      ensureDir(path.dirname(filePath));
      fs.writeFileSync(filePath, payload.subarray(range.startOffset, range.endOffset));
      packEntries.push({
        id: asset.id,
        title: asset.title,
        bank: bank.toUpperCase(),
        sourceRange: source.range,
        bytes: range.length,
        path: relativePath,
        sha1: sha1Buffer(payload.subarray(range.startOffset, range.endOffset))
      });
    }
  }
  writeJson(path.join(outputDir, "audio-pack-index.json"), {
    schema: "earthbound-decomp.generated-audio-packs.v1",
    generatedAt: new Date().toISOString(),
    packCount: packEntries.length,
    playableWavCount: 0,
    rendererStatus: "libgme_wav_renderer_packaged_but_snapshot_orchestration_pending",
    packs: packEntries
  });
  return packEntries;
}

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function bundledAudioBackendManifestPath(name) {
  return path.join(bundledAudioBackendRoot(), "manifests", name);
}

function safeFileStem(value) {
  return String(value || "unnamed").toLowerCase().replace(/[^a-z0-9_-]+/g, "_").replace(/^_+|_+$/g, "") || "unnamed";
}

function parseHexAddress(value) {
  return Number.parseInt(String(value || "0").replace(/^0x/i, ""), 16);
}

function audioPackPointerMap(packContract) {
  const map = new Map();
  for (const pack of packContract.audio_packs || []) {
    const pointer = pack.pointer || {};
    if (!pointer.bank || !pointer.address) {
      continue;
    }
    map.set(Number(pack.pack_id), {
      packId: Number(pack.pack_id),
      bank: parseHexAddress(pointer.bank),
      address: parseHexAddress(pointer.address),
      range: pack.range
    });
  }
  return map;
}

function runNativeTool(executable, args, options = {}) {
  const completed = spawnSync(executable, args, {
    cwd: options.cwd || path.dirname(executable),
    encoding: "utf8",
    maxBuffer: options.maxBuffer || 16 * 1024 * 1024,
    windowsHide: true
  });
  return {
    status: completed.status,
    signal: completed.signal,
    stdout: completed.stdout || "",
    stderr: completed.stderr || "",
    ok: completed.status === 0
  };
}

function parseJsonOutput(text) {
  try {
    return JSON.parse(text);
  } catch {
    const start = String(text || "").indexOf("{");
    const end = String(text || "").lastIndexOf("}");
    if (start >= 0 && end > start) {
      return JSON.parse(text.slice(start, end + 1));
    }
    throw new Error("Native tool did not emit JSON.");
  }
}

function snapshotMetadata(filePath) {
  const data = fs.readFileSync(filePath);
  const ram = data.length >= 0x10100 ? data.subarray(0x100, 0x10100) : Buffer.alloc(0);
  const dsp = data.length >= 0x10180 ? data.subarray(0x10100, 0x10180) : Buffer.alloc(0);
  return {
    path: filePath,
    bytes: data.length,
    sha1: sha1Buffer(data),
    signature_ok: data.subarray(0, SPC_SIGNATURE.length).equals(SPC_SIGNATURE),
    pc: data.length > 0x26 ? hexWord(data[0x25] | (data[0x26] << 8)) : null,
    ram_sha1: ram.length === 0x10000 ? sha1Buffer(ram) : null,
    dsp_register_sha1: dsp.length === 128 ? sha1Buffer(dsp) : null,
    dsp_nonzero_count: dsp.length === 128 ? Array.from(dsp).filter(Boolean).length : null,
    kon: data.length > 0x1014c ? hexByte(data[0x1014c]) : null
  };
}

function buildAudioLoaderFixture(outputDir, payload) {
  const loaderPath = path.join(outputDir, "fixtures", "c0-ab06-load-spc700-data-stream.bin");
  ensureDir(path.dirname(loaderPath));
  fs.writeFileSync(loaderPath, payload.subarray(C0AB06_LOADER_OFFSET, C0AB06_LOADER_OFFSET + C0AB06_LOADER_LENGTH));
  return {
    path: loaderPath,
    bytes: C0AB06_LOADER_LENGTH,
    sha1: sha1Buffer(fs.readFileSync(loaderPath)),
    source: {
      type: "verified-rom-slice",
      fileOffset: hexLong(C0AB06_LOADER_OFFSET),
      cpuAddress: "C0:AB06"
    }
  };
}

function expectedAudioOutputsForBackend() {
  return ["complete_spc_snapshot", "rendered_wav", "render_hash_json"];
}

function buildAudioBackendJob(job, outputRoot, snapshotIndexPath) {
  const outputDir = path.join(outputRoot, job.job_id);
  return {
    job_id: job.job_id,
    backend_id: "snes_spc",
    fixture_path: snapshotIndexPath,
    output_dir: outputDir,
    render_options: {
      seconds: 30,
      fade_seconds: 5,
      sample_rate: 32000,
      channels: 2,
      output_format: "wav"
    },
    expected_outputs: expectedAudioOutputsForBackend(),
    track_id: job.track_id,
    track_name: job.track_name,
    input_apu_ram_sha1: job.snapshot?.ram_sha1 || "",
    input_load_mode: "app_owned_c0ab06_fusion_snapshot",
    source_snapshot_index: snapshotIndexPath,
    source_snapshot_path: job.snapshot?.path || null,
    source_snapshot_sha1: job.snapshot?.sha1 || null,
    source_snapshot_kind: "complete_spc_snapshot",
    status: "planned_waiting_for_backend_harness",
    result_schema: "earthbound-decomp.audio-backend-result.v1",
    result_path: path.join(outputDir, "result.json"),
    job_path: path.join(outputDir, "job.json")
  };
}

function collectAudioPlaybackManifest(summaryPath, jobIndexPath, jobs, skippedRecords = []) {
  const tracks = [];
  for (const job of jobs) {
    if (!fs.existsSync(job.result_path)) {
      continue;
    }
    const result = readJson(job.result_path);
    const outputByKind = new Map((result.outputs || []).map((output) => [output.kind, output]));
    const renderHash = outputByKind.get("render_hash_json")?.path && fs.existsSync(outputByKind.get("render_hash_json").path)
      ? readJson(outputByKind.get("render_hash_json").path)
      : {};
    const peak = Number(renderHash.peak_abs_sample || 0);
    const nonzero = Number(renderHash.nonzero_sample_count || 0);
    tracks.push({
      job_id: job.job_id,
      track_id: Number(job.track_id),
      track_name: job.track_name,
      backend_id: job.backend_id,
      backend_version: result.backend_version,
      status: result.status,
      valid: result.status === "ok",
      classification: peak > 0 && nonzero > 0 ? "audible" : "silent",
      source_state: "app_owned_full_change_music_c0ab06_snapshot",
      source_spc: outputByKind.get("complete_spc_snapshot") || null,
      rendered_wav: outputByKind.get("rendered_wav") || null,
      render_hash: outputByKind.get("render_hash_json") || null,
      metrics: {
        peak_abs_sample: renderHash.peak_abs_sample ?? null,
        rms_sample: renderHash.rms_sample ?? null,
        nonzero_sample_count: renderHash.nonzero_sample_count ?? null,
        first_nonzero_sample_index: renderHash.first_nonzero_sample_index ?? null,
        last_nonzero_sample_index: renderHash.last_nonzero_sample_index ?? null,
        voice_count: renderHash.voice_count ?? null,
        rendered_samples: renderHash.rendered_samples ?? null,
        warning: renderHash.warning || ""
      }
    });
  }
  tracks.sort((a, b) => a.track_id - b.track_id);
  const statusCounts = {};
  const classificationCounts = {};
  for (const track of tracks) {
    statusCounts[track.status] = (statusCounts[track.status] || 0) + 1;
    classificationCounts[track.classification] = (classificationCounts[track.classification] || 0) + 1;
  }
  const passedCount = tracks.filter((track) => track.status === "ok" && track.valid && track.classification === "audible").length;
  return {
    schema: "earthbound-decomp.audio-playback-export-manifest.v1",
    summary_path: summaryPath,
    backend_id: "snes_spc",
    job_index: jobIndexPath,
    track_count: tracks.length,
    table_entry_count: tracks.length + skippedRecords.length,
    skipped_count: skippedRecords.length,
    skipped_records: skippedRecords,
    status_counts: statusCounts,
    classification_counts: classificationCounts,
    quality_gate: {
      required_status: "ok",
      required_validation: true,
      required_classification: "audible",
      passed_count: passedCount,
      failed_count: tracks.length - passedCount
    },
    source_policy: {
      generated_locally: true,
      contains_rom_derived_payloads: true,
      distribution: "never_distribute_generated_audio_or_spc_outputs",
      consumer: "local_app_playback_and_user_export_only"
    },
    tracks
  };
}

function generatePlayableAudio(outputDir, payload, manifest, audioPacks) {
  const backend = bundledAudioBackendStatus();
  const contractPath = bundledAudioBackendManifestPath("audio-pack-contracts.json");
  if (!backend.c0ab06Harness.present || !backend.libgmeHarness.present || !fs.existsSync(contractPath)) {
    return {
      status: "native_backend_missing",
      generatedWavs: 0,
      generatedSnapshots: 0,
      skipped: [],
      errors: ["Packaged C0:AB06 and libgme harnesses plus audio-pack-contracts.json are required."]
    };
  }
  const packContract = readJson(contractPath);
  const pointerByPack = audioPackPointerMap(packContract);
  const bootstrap = pointerByPack.get(AUDIO_BOOTSTRAP_PACK_ID);
  if (!bootstrap) {
    throw new Error("Audio pack contract does not contain bootstrap pack 1.");
  }
  const loaderFixture = buildAudioLoaderFixture(outputDir, payload);
  const snapshotDir = path.join(outputDir, "spc-snapshots");
  const renderRoot = path.join(outputDir, "render-jobs");
  ensureDir(snapshotDir);
  ensureDir(renderRoot);
  const snapshotRecords = [];
  const skippedRecords = [];
  for (const track of packContract.tracks || []) {
    const trackId = Number(track.track_id);
    const loadOrder = Array.isArray(track.load_order) ? track.load_order : [];
    if (trackId === 0) {
      continue;
    }
    if (loadOrder.length === 0) {
      skippedRecords.push({ track_id: trackId, track_name: track.name || `TRACK_${trackId}`, reason: "no_audio_or_missing_load_order" });
      continue;
    }
    const firstPackId = Number(loadOrder[0].pack_id);
    const firstPointer = pointerByPack.get(firstPackId);
    if (!firstPointer) {
      skippedRecords.push({ track_id: trackId, track_name: track.name || `TRACK_${trackId}`, reason: `missing_pointer_for_pack_${firstPackId}` });
      continue;
    }
    const trackName = track.name || `TRACK_${trackId}`;
    const jobId = `fusion-track-${trackId.toString().padStart(3, "0")}-${safeFileStem(trackName)}`;
    const snapshotPath = path.join(snapshotDir, `${jobId}-change-music-fusion-last-keyon.spc`);
    const apuRamPath = path.join(snapshotDir, `${jobId}-change-music-fusion-apu-ram.bin`);
    const run = runNativeTool(backend.c0ab06Harness.path, [
      "--receiver", "ares_smp_builtin_ipl",
      "--loader-file", loaderFixture.path,
      "--rom-file", manifest.rom.path,
      "--stream-bank", hexByte(firstPointer.bank),
      "--stream-address", hexWord(firstPointer.address),
      "--bootstrap-bank", hexByte(bootstrap.bank),
      "--bootstrap-address", hexWord(bootstrap.address),
      "--change-music-track", hexByte(trackId),
      "--apu-ram-out", apuRamPath,
      "--snapshot-out", snapshotPath,
      "--command-write-smp-burst", "0"
    ], { cwd: outputDir, maxBuffer: 64 * 1024 * 1024 });
    if (!run.ok && /receiver must be|requires --ipl-file|SFC IPL ROM/i.test(run.stderr + run.stdout)) {
      throw new Error("The bundled C0:AB06 harness does not yet support the no-external-IPL receiver required for standalone app WAV generation.");
    }
    const parsed = run.stdout.trim() ? parseJsonOutput(run.stdout) : {};
    const snapshot = fs.existsSync(snapshotPath) ? snapshotMetadata(snapshotPath) : null;
    if (!run.ok || !snapshot?.signature_ok) {
      skippedRecords.push({
        track_id: trackId,
        track_name: trackName,
        reason: run.ok ? "missing_snapshot" : "snapshot_harness_failed",
        stderr: run.stderr.trim()
      });
      continue;
    }
    snapshotRecords.push({
      job_id: jobId,
      track_id: trackId,
      track_name: trackName,
      capture_path: path.join(snapshotDir, "c0ab06-change-music-fusion-spc-snapshots.json"),
      capture_exists: true,
      snapshot,
      smoke: {
        reached_key_on_after_ack: Boolean(parsed.change_music?.reached_key_on_after_ack),
        source_frontier_status: "app_owned_c0ab06_fusion_snapshot"
      }
    });
  }
  const snapshotIndexPath = path.join(snapshotDir, "c0ab06-change-music-fusion-spc-snapshots.json");
  writeJson(snapshotIndexPath, {
    schema: "earthbound-decomp.audio-ares-smp-mailbox-spc-index.v1",
    snapshot_kind: "c0ab06_change_music_fusion_last_keyon_spc_snapshot",
    faithfulness: "app_owned_full_change_music_invokes_c0ab06_against_selected_rom",
    source_summary: "generated inside Electron local workspace",
    job_count: snapshotRecords.length + skippedRecords.length,
    snapshot_count: snapshotRecords.length,
    missing_snapshot_count: skippedRecords.length,
    invalid_signature_count: 0,
    records: snapshotRecords,
    skipped_records: skippedRecords
  });
  const jobs = snapshotRecords.map((record) => buildAudioBackendJob(record, renderRoot, snapshotIndexPath));
  const jobIndexPath = path.join(renderRoot, "snes_spc-jobs.json");
  writeJson(jobIndexPath, {
    schema: "earthbound-decomp.audio-backend-job-index.v1",
    fixture_index: snapshotIndexPath,
    snapshot_index: snapshotIndexPath,
    backend_id: "snes_spc",
    job_count: jobs.length,
    skipped_count: skippedRecords.length,
    skipped_records: skippedRecords,
    jobs,
    status: "planned_waiting_for_backend_harness",
    source_policy: {
      requires_user_supplied_rom: true,
      do_not_commit_generated_outputs: true,
      generated_audio_output_root: "local Electron workspace"
    }
  });
  const renderErrors = [];
  for (const job of jobs) {
    writeJson(job.job_path, job);
    const run = runNativeTool(backend.libgmeHarness.path, [
      "--job", job.job_path,
      "--result", job.result_path,
      "--snapshot-index", snapshotIndexPath
    ], { cwd: outputDir, maxBuffer: 64 * 1024 * 1024 });
    if (!run.ok) {
      renderErrors.push({ job_id: job.job_id, stderr: run.stderr.trim(), stdout: run.stdout.trim() });
    }
  }
  const summaryPath = path.join(renderRoot, "snes_spc-result-summary.json");
  const completedJobs = jobs.filter((job) => fs.existsSync(job.result_path));
  writeJson(summaryPath, {
    schema: "earthbound-decomp.audio-backend-result-summary.v1",
    backend_id: "snes_spc",
    job_index: jobIndexPath,
    job_count: jobs.length,
    result_count: completedJobs.length,
    failed_count: renderErrors.length,
    results: completedJobs.map((job) => {
      const result = readJson(job.result_path);
      return {
        job_id: job.job_id,
        track_id: job.track_id,
        track_name: job.track_name,
        backend_id: job.backend_id,
        status: result.status,
        valid: result.status === "ok",
        result_path: job.result_path
      };
    }),
    errors: renderErrors
  });
  const playbackManifest = collectAudioPlaybackManifest(summaryPath, jobIndexPath, jobs, skippedRecords);
  writeJson(path.join(outputDir, "audio-playback-export-manifest.json"), playbackManifest);
  writeJson(path.join(outputDir, "audio-render-summary.json"), {
    schema: "earthbound-decomp.encyclopedia-audio-render-summary.v1",
    generatedAt: new Date().toISOString(),
    loaderFixture,
    extractedPackCount: audioPacks.length,
    snapshotIndex: path.relative(outputDir, snapshotIndexPath).replaceAll("\\", "/"),
    jobIndex: path.relative(outputDir, jobIndexPath).replaceAll("\\", "/"),
    playbackManifest: "audio-playback-export-manifest.json",
    generatedSnapshots: snapshotRecords.length,
    generatedWavs: playbackManifest.tracks.filter((track) => track.rendered_wav).length,
    skippedRecords,
    renderErrors
  });
  return {
    status: renderErrors.length ? "rendered_with_errors" : "ready",
    generatedWavs: playbackManifest.tracks.filter((track) => track.rendered_wav).length,
    generatedSnapshots: snapshotRecords.length,
    skipped: skippedRecords,
    errors: renderErrors
  };
}

function buildWorkspaceManifest(rom) {
  const workspaceRoot = workspaceRootForSha1(rom.headerlessSha1);
  const directories = {
    root: workspaceRoot,
    source: path.join(workspaceRoot, "src"),
    graphics: path.join(workspaceRoot, "assets", "graphics"),
    maps: path.join(workspaceRoot, "assets", "maps"),
    audio: path.join(workspaceRoot, "audio"),
    manifests: path.join(workspaceRoot, "manifests"),
    exports: path.join(workspaceRoot, "exports"),
    cache: path.join(workspaceRoot, "cache")
  };
  for (const dir of Object.values(directories)) {
    ensureDir(dir);
  }
  const manifest = {
    schema: "earthbound-decomp.local-workspace.v1",
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    app: "earthbound-decomp-encyclopedia",
    rom,
    directories,
    artifactFamilies: FAMILY_DEFINITIONS.map((family) => familyManifestEntry(family, directories)),
    policy: {
      containsRomDerivedPayloads: true,
      distribution: "never_distribute_generated_payloads",
      exportScope: "user_local_only"
    }
  };
  writeWorkspaceManifest(manifest);
  return manifest;
}

function familyManifestEntry(family, directories) {
  return {
    id: family.id,
    label: family.label,
    summary: family.summary,
    status: "pending-generator",
    directory: directories[family.directoryKey],
    exportKinds: family.exportKinds,
    fileCount: 0,
    generatedAt: null,
    exportZip: null
  };
}

function manifestPathForRoot(workspaceRoot) {
  return path.join(workspaceRoot, "workspace-manifest.json");
}

function readWorkspaceManifest(workspaceRoot) {
  const root = validateWorkspaceRoot(workspaceRoot);
  const manifestPath = manifestPathForRoot(root);
  if (!fs.existsSync(manifestPath)) {
    throw new Error("Workspace manifest is missing. Select and verify the ROM again.");
  }
  return JSON.parse(fs.readFileSync(manifestPath, "utf8"));
}

function writeWorkspaceManifest(manifest) {
  manifest.updatedAt = new Date().toISOString();
  writeJson(manifestPathForRoot(manifest.directories.root), manifest);
}

function validateWorkspaceRoot(workspaceRoot) {
  if (!workspaceRoot || typeof workspaceRoot !== "string") {
    throw new Error("Missing workspace root.");
  }
  const resolved = path.resolve(workspaceRoot);
  const base = path.resolve(app.getPath("userData"), "local-workspaces");
  const relative = path.relative(base, resolved);
  if (relative.startsWith("..") || path.isAbsolute(relative)) {
    throw new Error("Workspace root is outside the local workspace directory.");
  }
  return resolved;
}

function validateFamilyId(familyId) {
  const family = FAMILY_BY_ID.get(String(familyId || ""));
  if (!family) {
    throw new Error(`Unknown artifact family: ${familyId || "<empty>"}`);
  }
  return family;
}

function verifiedRomPayload(manifest) {
  const romPath = manifest?.rom?.path;
  if (!romPath || !fs.existsSync(romPath)) {
    throw new Error("The verified ROM file is no longer available at its original path.");
  }
  const data = fs.readFileSync(romPath);
  const payload = payloadForRomBuffer(data);
  const headerlessSha1 = sha1Buffer(payload);
  if (headerlessSha1 !== EXPECTED_HEADERLESS_SHA1 || headerlessSha1 !== manifest.rom.headerlessSha1) {
    throw new Error("The ROM at the saved path no longer matches the verified EarthBound US SHA-1.");
  }
  return payload;
}

function bankIndex(payload) {
  const banks = [];
  for (let index = 0; index < Math.ceil(payload.length / BANK_SIZE); index += 1) {
    const start = index * BANK_SIZE;
    const bank = payload.subarray(start, Math.min(start + BANK_SIZE, payload.length));
    const snesBank = 0xc0 + index;
    banks.push({
      index,
      id: `bank-${snesBank.toString(16).toLowerCase()}`,
      snesBank: hexByte(snesBank),
      fileOffset: hexLong(start),
      size: bank.length,
      sha1: sha1Buffer(bank)
    });
  }
  return banks;
}

function vectorIndex(payload) {
  const vectors = {
    native_cop: 0xffe4,
    native_brk: 0xffe6,
    native_abort: 0xffe8,
    native_nmi: 0xffea,
    native_irq: 0xffee,
    emulation_cop: 0xfff4,
    emulation_abort: 0xfff8,
    emulation_nmi: 0xfffa,
    emulation_reset: 0xfffc,
    emulation_irqbrk: 0xfffe
  };
  return Object.entries(vectors).map(([name, headerOffset]) => ({
    name,
    headerOffset: hexWord(headerOffset),
    targetAddress: hexWord(readU16Le(payload, headerOffset))
  }));
}

function makeFamilyBaseManifest(manifest, family, payload) {
  return {
    schema: `earthbound-decomp.generated-${family.id}.v1`,
    generatedAt: new Date().toISOString(),
    generator: "electron-local-workspace",
    family: {
      id: family.id,
      label: family.label,
      summary: family.summary,
      exportKinds: family.exportKinds
    },
    rom: {
      fileName: manifest.rom.fileName,
      size: manifest.rom.size,
      headered: manifest.rom.headered,
      headerlessSha1: sha1Buffer(payload),
      expectedHeaderlessSha1: EXPECTED_HEADERLESS_SHA1
    },
    policy: {
      localOnly: true,
      neverCommitGeneratedPayloads: true,
      exportMayContainRomDerivedMaterial: true
    }
  };
}

function generateFamily(manifest, familyId) {
  const family = validateFamilyId(familyId);
  const payload = verifiedRomPayload(manifest);
  if (family.id === "source") {
    generateSourceFamily(manifest, family, payload);
  } else if (family.id === "tables") {
    generateTablesFamily(manifest, family, payload);
  } else if (family.id === "graphics") {
    generateGraphicsFamily(manifest, family, payload);
  } else if (family.id === "maps") {
    generateMapsFamily(manifest, family, payload);
  } else if (family.id === "audio") {
    generateAudioFamily(manifest, family, payload);
  }
  updateFamilyFromDisk(manifest, family.id, "ready");
  writeWorkspaceManifest(manifest);
  return manifest;
}

function generateSourceFamily(manifest, family, payload) {
  const outputDir = manifest.directories.source;
  ensureDir(outputDir);
  const fullSourceDir = path.join(outputDir, "full-source");
  copyDirectoryRecursive(packagedSourceTemplateRoot(), fullSourceDir);
  const banks = bankIndex(payload);
  writeText(path.join(outputDir, "README.md"), [
    "# Generated Source Workspace",
    "",
    "This local source workspace is generated from the packaged complete source template plus a verified user-provided ROM.",
    "",
    "- `full-source/` contains the complete checked-in decomp source tree packaged with the app.",
    "- `banks/` contains generated local `incbin` bank anchors for byte-equivalence and ROM-local assembly experiments.",
    "",
    "The packaged app does not distribute ROM bytes. Generated bank anchor files use local `incbin` directives as byte-equivalence anchors.",
    "",
    "Set `EARTHBOUND_ROM` or replace the placeholder include path before assembling outside the app."
  ].join("\n") + "\n");
  writeJson(path.join(outputDir, "bank-index.json"), {
    ...makeFamilyBaseManifest(manifest, family, payload),
    fullSource: {
      path: "full-source",
      fileCount: listFiles(fullSourceDir).length,
      source: "packaged-source-template"
    },
    bankSize: BANK_SIZE,
    banks
  });
  const banksDir = path.join(outputDir, "banks");
  ensureDir(banksDir);
  for (const bank of banks) {
    const bankNumber = bank.snesBank.slice(2).toLowerCase();
    writeText(path.join(banksDir, `bank-${bankNumber}.asm`), [
      `; Generated local scaffold for ${bank.snesBank}.`,
      `; ROM SHA-1: ${manifest.rom.headerlessSha1}`,
      `; File offset: ${bank.fileOffset}, size: ${bank.size} bytes.`,
      "; Replace %EARTHBOUND_ROM% with the verified local ROM path or configure your assembler include path.",
      "",
      "arch 65816",
      `namespace bank_${bankNumber}`,
      `  incbin "%EARTHBOUND_ROM%", ${bank.fileOffset}, ${hexLong(bank.size)}`,
      "namespace off",
      ""
    ].join("\n"));
  }
}

function generateTablesFamily(manifest, family, payload) {
  const outputDir = manifest.directories.manifests;
  ensureDir(outputDir);
  writeJson(path.join(outputDir, "rom-header.json"), {
    ...makeFamilyBaseManifest(manifest, family, payload),
    header: readRomHeader(payload),
    vectors: vectorIndex(payload)
  });
  writeJson(path.join(outputDir, "rom-bank-index.json"), {
    ...makeFamilyBaseManifest(manifest, family, payload),
    bankSize: BANK_SIZE,
    banks: bankIndex(payload)
  });
  writeText(path.join(outputDir, "README.md"), [
    "# Generated Table And Contract Manifests",
    "",
    "This folder contains source-safe JSON manifests generated from the verified local ROM.",
    "ROM bytes and extracted copyrighted payloads are not copied here."
  ].join("\n") + "\n");
}

function generateGraphicsFamily(manifest, family, payload) {
  const outputDir = manifest.directories.graphics;
  ensureDir(outputDir);
  const assetBanks = bankIndex(payload).filter((bank) => {
    const bankNumber = Number.parseInt(bank.snesBank.slice(2), 16);
    return bankNumber >= 0xca && bankNumber <= 0xee;
  });
  const overworldSpritePreviews = generateOverworldSpritePreviews(outputDir, payload);
  writeJson(path.join(outputDir, "graphics-manifest.json"), {
    ...makeFamilyBaseManifest(manifest, family, payload),
    status: "rendered-local-assets",
    decoderStatus: "Generated raw .gfx payloads, palette metadata, decoded sprite-sheet JSON, individual sprite-sheet PNGs, bank contact sheets, tile atlas PNGs, and candidate 2x3 overworld sprite frame sheets from D1-D5 sprite payload ranges.",
    assetBankRange: "0xCA..0xEE",
    banks: assetBanks,
    generatedPreviews: {
      rawGfx: overworldSpritePreviews.length,
      overworldSpritePalette00TileAtlases: overworldSpritePreviews.length,
      overworldSpriteCandidateFrameSheets: overworldSpritePreviews.length,
      overworldSpriteSheets: overworldSpritePreviews.length,
      overworldSpriteDecodedSheets: overworldSpritePreviews.length,
      overworldSpriteGroupContactSheets: "all plus per-bank"
    },
    previewIndex: "overworld-sprites/index.json"
  });
  writeText(path.join(outputDir, "README.md"), [
    "# Generated Graphics And Sprite Previews",
    "",
    "This local workspace contains raw `.gfx` payloads, palette metadata, decoded sprite-sheet JSON, individual sprite-sheet PNGs, bank contact sheets, tile atlas PNGs, and candidate 2x3 frame-sheet PNGs generated from the verified ROM.",
    "The current built-in renderer uses the source-safe D1-D5 sprite payload ranges and the ROM-backed palette-00 source at C3:0000..C3:0020.",
    "",
    "`overworld-sprites/sheets/` contains unscaled transparent PNG sheets intended for downstream tools.",
    "`overworld-sprites/sheets-preview/` and `overworld-sprites/groups/` are browseable convenience PNGs.",
    "`overworld-sprites/decoded/` stores palette-index rows for each generated frame.",
    "",
    "The frame layout is still row-major 2x3-tile overworld sprite payload digestion. Battle graphics and exact object-aware animation metadata remain later renderer stages."
  ].join("\n") + "\n");
}

function generateMapsFamily(manifest, family, payload) {
  const outputDir = manifest.directories.maps;
  ensureDir(outputDir);
  writeJson(path.join(outputDir, "map-manifest.json"), {
    ...makeFamilyBaseManifest(manifest, family, payload),
    status: "indexed",
    decoderStatus: "Scene, FTS, palette, collision, and tile-animation renderers attach to this local manifest.",
    contractFamilies: [
      "map-scene-composition",
      "map-sector-bundle",
      "map-fts-arrangement",
      "map-fts-palette-variant",
      "map-collision-runtime-bit",
      "map-tile-animation-runtime"
    ],
    sourceBanks: bankIndex(payload).filter((bank) => Number.parseInt(bank.snesBank.slice(2), 16) >= 0xd8)
  });
  writeText(path.join(outputDir, "README.md"), [
    "# Generated Map And Tileset Index",
    "",
    "This local folder is the handoff point for scene, tileset, palette, and collision previews.",
    "Rendered image payloads remain local-only."
  ].join("\n") + "\n");
}

function generateAudioFamily(manifest, family, payload) {
  const outputDir = manifest.directories.audio;
  ensureDir(outputDir);
  const audioPacks = extractAudioPacks(outputDir, payload);
  const backendStatus = bundledAudioBackendStatus();
  const playableAudio = generatePlayableAudio(outputDir, payload, manifest, audioPacks);
  const packIndexPath = path.join(outputDir, "audio-pack-index.json");
  if (fs.existsSync(packIndexPath)) {
    const packIndex = readJson(packIndexPath);
    writeJson(packIndexPath, {
      ...packIndex,
      playableWavCount: playableAudio.generatedWavs,
      generatedSnapshotCount: playableAudio.generatedSnapshots,
      rendererStatus: playableAudio.status
    });
  }
  writeJson(path.join(outputDir, "bundled-audio-backend.json"), {
    schema: "earthbound-decomp.encyclopedia-bundled-audio-backend.v1",
    generatedAt: new Date().toISOString(),
    backend: backendStatus,
    generationBoundary: {
      audioPacks: "generated directly from the verified ROM by the Encyclopedia app",
      loaderFixture: "generated directly from C0:AB06 bytes in the verified ROM",
      wavExports: "generated from app-owned C0:AB06 fusion SPC snapshots through the bundled libgme renderer",
      currentPackagedState: playableAudio.status
    },
    playableAudio,
    docs: [
      "audio-backend/manifests/audio-backend-contract.json",
      "audio-backend/manifests/audio-export-plan.json",
      "audio-backend/notes/audio-backend-contract.md",
      "audio-backend/notes/audio-spc-state-frontier.md"
    ]
  });
  const playbackManifestPath = path.join(outputDir, "audio-playback-export-manifest.json");
  if (!fs.existsSync(playbackManifestPath)) {
    writeJson(playbackManifestPath, {
    ...makeFamilyBaseManifest(manifest, family, payload),
    status: playableAudio.generatedWavs ? "wav-rendered" : "packs-extracted",
    backendStatus: {
      audioPackExtraction: "ready",
      aresSnapshotCore: backendStatus.aresHarness.present ? "ares-audio-harness-packaged" : "not-packaged",
      playbackCore: backendStatus.libgmeHarness.present ? "libgme-harness-packaged" : "not-packaged",
      c0ab06SnapshotCore: backendStatus.c0ab06Harness.present ? "ares-c0ab06-loader-harness-packaged" : "not-packaged",
      spcExport: playableAudio.generatedSnapshots ? "generated" : "not-generated",
      wavExport: playableAudio.generatedWavs ? "generated" : "not-generated",
      validationCorpus: "20/20 CHANGE_MUSIC load-apply render corpus validated in the reference workspace"
    },
    knownEntryPoints: [
      { label: "Change music loader", address: "C0:AB06" },
      { label: "Send APU port 0 command byte", address: "C0:ABBD" },
      { label: "Stop music and latch no track", address: "C0:ABC6" }
    ],
    generatedPacks: audioPacks.length,
    generatedWavs: playableAudio.generatedWavs,
    generatedSnapshots: playableAudio.generatedSnapshots,
    packIndex: "audio-pack-index.json",
    bundledBackend: "bundled-audio-backend.json",
    exportFamilies: ["ebm", "json", "manifest", "spc", "wav"]
    });
  }
  writeText(path.join(outputDir, "README.md"), [
    "# Generated Music And Audio Workspace",
    "",
    "This local workspace extracts EarthBound audio pack payloads (`.ebm`) from the verified ROM.",
    "It also generates C0:AB06 fusion SPC snapshots and playable WAV previews through the packaged native audio backend.",
    "",
    "Generated `.spc`, `.wav`, `.ebm`, and `.bin` files are ROM-derived local artifacts. Do not commit or redistribute them.",
    "",
    `Generated WAVs: ${playableAudio.generatedWavs}`,
    `Generated SPC snapshots: ${playableAudio.generatedSnapshots}`
  ].join("\n") + "\n");
}

function updateFamilyFromDisk(manifest, familyId, status) {
  const family = validateFamilyId(familyId);
  const outputDir = manifest.directories[family.directoryKey];
  const files = listFiles(outputDir);
  manifest.artifactFamilies = manifest.artifactFamilies.map((entry) => {
    if (entry.id !== familyId) {
      return entry;
    }
    return {
      ...entry,
      status,
      directory: outputDir,
      generatedAt: new Date().toISOString(),
      fileCount: files.length,
      files: files.map((filePath) => path.relative(outputDir, filePath).replaceAll("\\", "/"))
    };
  });
}

function listFiles(root) {
  if (!fs.existsSync(root)) {
    return [];
  }
  const output = [];
  for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
    const fullPath = path.join(root, entry.name);
    if (entry.isDirectory()) {
      output.push(...listFiles(fullPath));
    } else if (entry.isFile()) {
      output.push(fullPath);
    }
  }
  return output;
}

function exportFamily(manifest, familyId) {
  const family = validateFamilyId(familyId);
  const outputDir = manifest.directories[family.directoryKey];
  const files = listFiles(outputDir);
  if (!files.length) {
    throw new Error(`No generated files exist for ${family.label}. Run Generate first.`);
  }
  ensureDir(manifest.directories.exports);
  const zipPath = path.join(manifest.directories.exports, `${family.id}-${timestampForFile()}.zip`);
  writeZip(zipPath, files.map((filePath) => ({
    filePath,
    zipPath: path.relative(outputDir, filePath).replaceAll("\\", "/")
  })));
  manifest.artifactFamilies = manifest.artifactFamilies.map((entry) => (
    entry.id === family.id
      ? { ...entry, exportZip: zipPath, exportedAt: new Date().toISOString() }
      : entry
  ));
  writeWorkspaceManifest(manifest);
  return { manifest, zipPath };
}

function exportAll(manifest) {
  const zipEntries = [];
  for (const family of FAMILY_DEFINITIONS) {
    const outputDir = manifest.directories[family.directoryKey];
    for (const filePath of listFiles(outputDir)) {
      zipEntries.push({
        filePath,
        zipPath: `${family.id}/${path.relative(outputDir, filePath).replaceAll("\\", "/")}`
      });
    }
  }
  if (!zipEntries.length) {
    throw new Error("No generated files exist. Run Generate all first.");
  }
  ensureDir(manifest.directories.exports);
  const zipPath = path.join(manifest.directories.exports, `earthbound-local-workspace-${timestampForFile()}.zip`);
  writeZip(zipPath, zipEntries);
  manifest.lastBulkExport = { zipPath, exportedAt: new Date().toISOString(), fileCount: zipEntries.length };
  writeWorkspaceManifest(manifest);
  return { manifest, zipPath };
}

function workspaceFilePath(manifest, familyId, relativePath) {
  const family = validateFamilyId(familyId);
  if (!relativePath || typeof relativePath !== "string") {
    throw new Error("Missing generated file path.");
  }
  const outputDir = path.resolve(manifest.directories[family.directoryKey]);
  const candidate = path.resolve(outputDir, relativePath);
  const relative = path.relative(outputDir, candidate);
  if (relative.startsWith("..") || path.isAbsolute(relative)) {
    throw new Error("Generated file path is outside the requested family directory.");
  }
  if (!fs.existsSync(candidate) || !fs.statSync(candidate).isFile()) {
    throw new Error("Generated file does not exist. Run the generator stage again.");
  }
  return { family, outputDir, filePath: candidate, relativePath: relative.replaceAll("\\", "/") };
}

function readGeneratedWorkspaceFile(manifest, familyId, relativePath) {
  const { filePath, relativePath: cleanRelativePath } = workspaceFilePath(manifest, familyId, relativePath);
  const stat = fs.statSync(filePath);
  if (stat.size > 1024 * 1024) {
    throw new Error("Generated file is too large for inline preview. Open the family folder instead.");
  }
  return {
    path: cleanRelativePath,
    size: stat.size,
    modifiedAt: stat.mtime.toISOString(),
    content: fs.readFileSync(filePath, "utf8")
  };
}

function readGeneratedWorkspaceMedia(manifest, familyId, relativePath) {
  const { filePath, relativePath: cleanRelativePath } = workspaceFilePath(manifest, familyId, relativePath);
  const stat = fs.statSync(filePath);
  const extension = path.extname(filePath).toLowerCase();
  const mimeTypes = new Map([
    [".png", "image/png"],
    [".jpg", "image/jpeg"],
    [".jpeg", "image/jpeg"],
    [".gif", "image/gif"],
    [".webp", "image/webp"],
    [".wav", "audio/wav"],
    [".mp3", "audio/mpeg"],
    [".ogg", "audio/ogg"],
    [".flac", "audio/flac"]
  ]);
  const mimeType = mimeTypes.get(extension);
  if (!mimeType) {
    throw new Error("This generated media type cannot be previewed inline yet.");
  }
  const isAudio = [".wav", ".mp3", ".ogg", ".flac"].includes(extension);
  if (!isAudio && stat.size > 8 * 1024 * 1024) {
    throw new Error("Generated image is too large for inline preview. Open the family folder instead.");
  }
  return {
    path: cleanRelativePath,
    size: stat.size,
    modifiedAt: stat.mtime.toISOString(),
    mimeType,
    dataUrl: isAudio ? null : `data:${mimeType};base64,${fs.readFileSync(filePath).toString("base64")}`,
    fileUrl: isAudio ? pathToFileURL(filePath).toString() : null
  };
}

function timestampForFile() {
  return new Date().toISOString().replace(/[:.]/g, "-");
}

function crc32(buffer) {
  let crc = 0xffffffff;
  for (const byte of buffer) {
    crc = CRC_TABLE[(crc ^ byte) & 0xff] ^ (crc >>> 8);
  }
  return (crc ^ 0xffffffff) >>> 0;
}

function dosDateTime(date = new Date()) {
  const year = Math.max(1980, date.getFullYear());
  const dosTime = (date.getHours() << 11) | (date.getMinutes() << 5) | Math.floor(date.getSeconds() / 2);
  const dosDate = ((year - 1980) << 9) | ((date.getMonth() + 1) << 5) | date.getDate();
  return { dosTime, dosDate };
}

function writeZip(zipPath, entries) {
  const chunks = [];
  const central = [];
  let offset = 0;
  const { dosTime, dosDate } = dosDateTime();
  for (const entry of entries) {
    const name = Buffer.from(entry.zipPath.replaceAll("\\", "/"), "utf8");
    const data = fs.readFileSync(entry.filePath);
    const compressed = zlib.deflateRawSync(data);
    const crc = crc32(data);
    const local = Buffer.alloc(30);
    local.writeUInt32LE(0x04034b50, 0);
    local.writeUInt16LE(20, 4);
    local.writeUInt16LE(0x0800, 6);
    local.writeUInt16LE(8, 8);
    local.writeUInt16LE(dosTime, 10);
    local.writeUInt16LE(dosDate, 12);
    local.writeUInt32LE(crc, 14);
    local.writeUInt32LE(compressed.length, 18);
    local.writeUInt32LE(data.length, 22);
    local.writeUInt16LE(name.length, 26);
    local.writeUInt16LE(0, 28);
    chunks.push(local, name, compressed);
    const centralHeader = Buffer.alloc(46);
    centralHeader.writeUInt32LE(0x02014b50, 0);
    centralHeader.writeUInt16LE(20, 4);
    centralHeader.writeUInt16LE(20, 6);
    centralHeader.writeUInt16LE(0x0800, 8);
    centralHeader.writeUInt16LE(8, 10);
    centralHeader.writeUInt16LE(dosTime, 12);
    centralHeader.writeUInt16LE(dosDate, 14);
    centralHeader.writeUInt32LE(crc, 16);
    centralHeader.writeUInt32LE(compressed.length, 20);
    centralHeader.writeUInt32LE(data.length, 24);
    centralHeader.writeUInt16LE(name.length, 28);
    centralHeader.writeUInt16LE(0, 30);
    centralHeader.writeUInt16LE(0, 32);
    centralHeader.writeUInt16LE(0, 34);
    centralHeader.writeUInt16LE(0, 36);
    centralHeader.writeUInt32LE(0, 38);
    centralHeader.writeUInt32LE(offset, 42);
    central.push(centralHeader, name);
    offset += local.length + name.length + compressed.length;
  }
  const centralOffset = offset;
  const centralSize = central.reduce((sum, chunk) => sum + chunk.length, 0);
  const end = Buffer.alloc(22);
  end.writeUInt32LE(0x06054b50, 0);
  end.writeUInt16LE(0, 4);
  end.writeUInt16LE(0, 6);
  end.writeUInt16LE(entries.length, 8);
  end.writeUInt16LE(entries.length, 10);
  end.writeUInt32LE(centralSize, 12);
  end.writeUInt32LE(centralOffset, 16);
  end.writeUInt16LE(0, 20);
  fs.writeFileSync(zipPath, Buffer.concat([...chunks, ...central, end]));
}

ipcMain.handle("workspace:select-rom", async () => {
  const result = await dialog.showOpenDialog({
    title: "Select EarthBound ROM",
    properties: ["openFile"],
    filters: [
      { name: "SNES ROMs", extensions: ["sfc", "smc"] },
      { name: "All Files", extensions: ["*"] }
    ]
  });
  if (result.canceled || !result.filePaths.length) {
    return { canceled: true };
  }
  const rom = verifyRom(result.filePaths[0]);
  let manifest = null;
  if (rom.sha1Ok) {
    manifest = buildWorkspaceManifest(rom);
    for (const family of FAMILY_DEFINITIONS) {
      manifest = generateFamily(manifest, family.id);
    }
  }
  return { canceled: false, rom, manifest };
});

ipcMain.handle("workspace:generate-family", async (_event, workspaceRoot, familyId) => {
  try {
    const manifest = readWorkspaceManifest(workspaceRoot);
    return { ok: true, manifest: generateFamily(manifest, familyId) };
  } catch (error) {
    return { ok: false, error: error?.message || String(error) };
  }
});

ipcMain.handle("workspace:generate-all", async (_event, workspaceRoot) => {
  try {
    let manifest = readWorkspaceManifest(workspaceRoot);
    for (const family of FAMILY_DEFINITIONS) {
      manifest = generateFamily(manifest, family.id);
    }
    return { ok: true, manifest };
  } catch (error) {
    return { ok: false, error: error?.message || String(error) };
  }
});

ipcMain.handle("workspace:export-family", async (_event, workspaceRoot, familyId) => {
  try {
    const manifest = readWorkspaceManifest(workspaceRoot);
    return { ok: true, ...exportFamily(manifest, familyId) };
  } catch (error) {
    return { ok: false, error: error?.message || String(error) };
  }
});

ipcMain.handle("workspace:export-all", async (_event, workspaceRoot) => {
  try {
    const manifest = readWorkspaceManifest(workspaceRoot);
    return { ok: true, ...exportAll(manifest) };
  } catch (error) {
    return { ok: false, error: error?.message || String(error) };
  }
});

ipcMain.handle("workspace:read-file", async (_event, workspaceRoot, familyId, relativePath) => {
  try {
    const manifest = readWorkspaceManifest(workspaceRoot);
    return { ok: true, file: readGeneratedWorkspaceFile(manifest, familyId, relativePath) };
  } catch (error) {
    return { ok: false, error: error?.message || String(error) };
  }
});

ipcMain.handle("workspace:read-media", async (_event, workspaceRoot, familyId, relativePath) => {
  try {
    const manifest = readWorkspaceManifest(workspaceRoot);
    return { ok: true, media: readGeneratedWorkspaceMedia(manifest, familyId, relativePath) };
  } catch (error) {
    return { ok: false, error: error?.message || String(error) };
  }
});

ipcMain.handle("workspace:open-folder", async (_event, folderPath) => {
  if (!folderPath || typeof folderPath !== "string") {
    return { ok: false, error: "Missing folder path." };
  }
  const resolved = path.resolve(folderPath);
  const base = path.resolve(app.getPath("userData"), "local-workspaces");
  const relative = path.relative(base, resolved);
  if (relative.startsWith("..") || path.isAbsolute(relative)) {
    return { ok: false, error: "Refusing to open a folder outside the local workspace root." };
  }
  ensureDir(resolved);
  const error = await shell.openPath(resolved);
  return error ? { ok: false, error } : { ok: true };
});

app.whenReady().then(() => {
  createWindow();

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});
