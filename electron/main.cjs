const { app, BrowserWindow, dialog, ipcMain, shell } = require("electron");
const crypto = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");
const zlib = require("node:zlib");

const EXPECTED_HEADERLESS_SIZE = 3145728;
const EXPECTED_HEADERED_SIZE = EXPECTED_HEADERLESS_SIZE + 512;
const EXPECTED_HEADERLESS_SHA1 = "d67a8ef36ef616bc39306aa1b486e1bd3047815a";
const BANK_SIZE = 0x10000;
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

function writeSnes4bppPreview(filePath, data, options = {}) {
  const tilesPerRow = options.tilesPerRow || 16;
  const scale = options.scale || 2;
  const palette = options.palette || snesPaletteFromBytes(Buffer.alloc(0));
  const tileCount = Math.floor(data.length / 32);
  const tileRows = Math.max(1, Math.ceil(tileCount / tilesPerRow));
  const width = tilesPerRow * 8 * scale;
  const height = tileRows * 8 * scale;
  const rgba = Buffer.alloc(width * height * 4);
  for (let index = 0; index < rgba.length; index += 4) {
    rgba[index] = 15;
    rgba[index + 1] = 15;
    rgba[index + 2] = 14;
    rgba[index + 3] = 255;
  }
  for (let tileIndex = 0; tileIndex < tileCount; tileIndex += 1) {
    const tile = decodeSnes4bppTile(data.subarray(tileIndex * 32, tileIndex * 32 + 32));
    const tileLeft = (tileIndex % tilesPerRow) * 8 * scale;
    const tileTop = Math.floor(tileIndex / tilesPerRow) * 8 * scale;
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
  writePngRgba(filePath, width, height, rgba);
  return { width, height, tileCount };
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
      const relativePath = `overworld-sprites/${bank}/${spriteId}_palette_00_preview.png`;
      const filePath = path.join(outputDir, relativePath);
      const image = writeSnes4bppPreview(filePath, payload.subarray(range.startOffset, range.endOffset), {
        tilesPerRow: 8,
        scale: 3,
        palette
      });
      previewEntries.push({
        id: asset.id,
        title: asset.title,
        bank: bank.toUpperCase(),
        sourceRange: source.range,
        bytes: range.length,
        path: relativePath,
        palette: "C3:0000..C3:0020",
        width: image.width,
        height: image.height,
        tileCount: image.tileCount
      });
    }
  }
  writeJson(path.join(spriteDir, "index.json"), {
    schema: "earthbound-decomp.generated-overworld-sprite-previews.v1",
    generatedAt: new Date().toISOString(),
    palette: "C3:0000..C3:0020",
    previewCount: previewEntries.length,
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
    status: "rendered-preview",
    decoderStatus: "Generated palette-applied overworld sprite tile previews from D1-D5 sprite payload ranges. Battle graphics and composed/object-aware previews remain later renderer stages.",
    assetBankRange: "0xCA..0xEE",
    banks: assetBanks,
    generatedPreviews: {
      overworldSpritePalette00Png: overworldSpritePreviews.length
    },
    previewIndex: "overworld-sprites/index.json"
  });
  writeText(path.join(outputDir, "README.md"), [
    "# Generated Graphics And Sprite Previews",
    "",
    "This local workspace contains palette-applied overworld sprite tile preview PNGs generated from the verified ROM.",
    "The current built-in renderer uses the source-safe D1-D5 sprite payload ranges and the ROM-backed palette-00 source at C3:0000..C3:0020.",
    "",
    "These are tile previews, not final object-aware composed animation sheets. Battle graphics and richer composed sprite views remain separate renderer stages."
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
  writeJson(path.join(outputDir, "bundled-audio-backend.json"), {
    schema: "earthbound-decomp.encyclopedia-bundled-audio-backend.v1",
    generatedAt: new Date().toISOString(),
    backend: backendStatus,
    generationBoundary: {
      audioPacks: "generated directly from the verified ROM by the Encyclopedia app",
      wavExports: "requires C0:AB06 fusion SPC snapshots plus bundled libgme render jobs",
      currentPackagedState: backendStatus.libgmeHarness.present && backendStatus.c0ab06Harness.present
        ? "native_harnesses_bundled_snapshot_orchestration_not_yet_ported_to_node"
        : "native_harnesses_missing"
    },
    docs: [
      "audio-backend/manifests/audio-backend-contract.json",
      "audio-backend/manifests/audio-export-plan.json",
      "audio-backend/notes/audio-backend-contract.md",
      "audio-backend/notes/audio-spc-state-frontier.md"
    ]
  });
  writeJson(path.join(outputDir, "audio-playback-export-manifest.json"), {
    ...makeFamilyBaseManifest(manifest, family, payload),
    status: "packs-extracted",
    backendStatus: {
      audioPackExtraction: "ready",
      aresSnapshotCore: backendStatus.aresHarness.present ? "ares-audio-harness-packaged" : "not-packaged",
      playbackCore: backendStatus.libgmeHarness.present ? "libgme-harness-packaged" : "not-packaged",
      c0ab06SnapshotCore: backendStatus.c0ab06Harness.present ? "ares-c0ab06-loader-harness-packaged" : "not-packaged",
      spcExport: "requires-c0ab06-fusion-snapshot-generation",
      wavExport: "native-renderer-packaged-orchestration-pending",
      validationCorpus: "20/20 CHANGE_MUSIC load-apply render corpus validated in the reference workspace"
    },
    knownEntryPoints: [
      { label: "Change music loader", address: "C0:AB06" },
      { label: "Send APU port 0 command byte", address: "C0:ABBD" },
      { label: "Stop music and latch no track", address: "C0:ABC6" }
    ],
    generatedPacks: audioPacks.length,
    packIndex: "audio-pack-index.json",
    bundledBackend: "bundled-audio-backend.json",
    exportFamilies: ["ebm", "json", "manifest", "wav-after-snapshot-orchestration"]
  });
  writeText(path.join(outputDir, "README.md"), [
    "# Generated Music And Audio Workspace",
    "",
    "This local workspace extracts EarthBound audio pack payloads (`.ebm`) from the verified ROM.",
    "These packs are real ROM-derived audio assets, but they are not directly playable WAV files.",
    "",
    "The packaged app now includes the native C0:AB06 snapshot harness, libgme WAV renderer harness, audio backend contracts, export plan, notes, and orchestration scripts.",
    "The remaining gap is wiring C0:AB06 fusion snapshot generation into Electron/Node so the bundled renderer can produce WAVs from the selected ROM without an external decomp checkout."
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
  if (stat.size > 8 * 1024 * 1024) {
    throw new Error("Generated media is too large for inline preview. Open the family folder instead.");
  }
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
  return {
    path: cleanRelativePath,
    size: stat.size,
    modifiedAt: stat.mtime.toISOString(),
    mimeType,
    dataUrl: `data:${mimeType};base64,${fs.readFileSync(filePath).toString("base64")}`
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
