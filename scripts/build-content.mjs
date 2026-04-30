import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(__dirname, "..");
const defaultSourceRoot = path.resolve(appRoot, "..");
const cliArgs = process.argv.slice(2);
const buildMode = resolveBuildMode();
const sourceRoot = resolveSourceRoot();
const repoRoot = sourceRoot;
const catalogSourceRoot = buildMode === "authored" ? "authored-release-baseline" : sourceRoot;
const catalogAppRoot = buildMode === "authored" ? "packaged-app" : appRoot;
const contentDir = path.join(appRoot, "content");
const generatedDir = path.join(appRoot, "public", "generated");
const entryBodyDir = path.join(generatedDir, "entry-bodies");
const sourceSnapshotPath = path.join(generatedDir, "source-snapshot.json");
const heavyBodyThreshold = 14000;
const searchTextLimit = 6000;

const notesDir = path.join(repoRoot, "notes");
const srcDir = path.join(repoRoot, "src");
const assetManifestDir = path.join(repoRoot, "asset-manifests");
const expectedRom = {
  size: 3145728,
  sha1: "D67A8EF36EF616BC39306AA1B486E1BD3047815A"
};
const romCandidates = [
  "EarthBound (USA).sfc",
  "baserom/EarthBound (USA).sfc"
];

fs.mkdirSync(generatedDir, { recursive: true });
fs.rmSync(entryBodyDir, { recursive: true, force: true });
fs.mkdirSync(entryBodyDir, { recursive: true });

function resolveSourceRoot() {
  const sourceRootIndex = cliArgs.findIndex((arg) => arg === "--source-root");
  const inlineArg = cliArgs.find((arg) => arg.startsWith("--source-root="));
  const configured = inlineArg
    ? inlineArg.slice("--source-root=".length)
    : sourceRootIndex !== -1
      ? cliArgs[sourceRootIndex + 1]
      : process.env.EB_DECOMP_SOURCE_ROOT;
  const candidate = path.resolve(configured || defaultSourceRoot);
  if (!fs.existsSync(candidate)) {
    throw new Error(`Source root does not exist: ${candidate}`);
  }
  for (const required of ["notes", "src", "tools"]) {
    if (!fs.existsSync(path.join(candidate, required))) {
      throw new Error(`Source root is missing required folder ${required}: ${candidate}`);
    }
  }
  return candidate;
}

function resolveBuildMode() {
  const modeIndex = cliArgs.findIndex((arg) => arg === "--mode");
  const inlineArg = cliArgs.find((arg) => arg.startsWith("--mode="));
  const configured = inlineArg
    ? inlineArg.slice("--mode=".length)
    : modeIndex !== -1
      ? cliArgs[modeIndex + 1]
      : process.env.EB_ENCYCLOPEDIA_BUILD_MODE;
  const mode = configured || "local";
  if (!["authored", "local"].includes(mode)) {
    throw new Error(`Unsupported build mode: ${mode}. Expected "authored" or "local".`);
  }
  return mode;
}

const entries = [];
const entryIds = new Set();
const pathEntryIds = new Map();
const noteEntries = [];

const topicConfigs = [
  {
    id: "topic-localization-authoring",
    title: "Localization And Text Authoring",
    summary: "Text command syntax, localization authoring evidence, parsed text banks, and string layout constraints.",
    aliases: ["localization", "text authoring", "text commands", "text banks", "ebtext"],
    keywords: ["localization", "authoring", "text command", "text-command", "ebtext", "ccs", "string", "glyph", "font"],
    related: ["script-and-text-vms", "text-command-vm"],
    banks: ["C1", "C5", "C6", "C7", "C8", "C9", "EF"]
  },
  {
    id: "topic-actionscript-events",
    title: "Actionscript And Event Runtime",
    summary: "C3 event/actionscript decoding, opcode semantics, movement tasks, and script callback contracts.",
    aliases: ["actionscript", "events", "event runtime", "C3 scripts"],
    keywords: ["actionscript", "opcode", "event", "movement", "task", "callback"],
    related: ["script-and-text-vms", "bank-c3"],
    banks: ["C0", "C3"]
  },
  {
    id: "topic-source-semantics",
    title: "Source Semantics And Naming",
    summary: "Readable source closure, naming proposals, symbol synthesis, comments, and source-bank handoff work.",
    aliases: ["source naming", "symbols", "working names", "readable source", "semantic naming"],
    keywords: ["working name", "symbol", "synthesis", "readable", "source scaffold", "source handoff", "closure", "semantic", "naming", "byte equivalence"],
    related: ["runtime-systems", "routine-index", "source-tree"],
    banks: ["C0", "C1", "C2", "C4", "EF"]
  },
  {
    id: "topic-asset-pipeline",
    title: "Asset Pipeline And Manifests",
    summary: "Asset manifests, graphics payloads, map tiles, sprites, palettes, compression, extraction, and render fixtures.",
    aliases: ["assets", "asset manifests", "graphics", "sprites", "palettes", "tiles"],
    keywords: ["asset", "manifest", "graphics", "sprite", "tiles", "tilemap", "palette", "render", "extract", "compression", "decompress", "battlebg"],
    related: ["asset-contracts", "asset-manifest-index"],
    banks: ["CA", "CB", "CC", "CD", "CE", "D1", "D2", "D3", "D4", "E0", "E1"]
  },
  {
    id: "topic-battle-runtime",
    title: "Battle Runtime",
    summary: "Battle action dispatch, PSI menus, target selection, statuses, enemy data, and battle text/visual contracts.",
    aliases: ["battle", "psi", "enemy", "combat"],
    keywords: ["battle", "psi", "enemy", "target", "status", "affliction", "action", "combat", "hp", "pp"],
    related: ["bank-c2", "runtime-systems"],
    banks: ["C1", "C2", "C3", "D5", "EF"]
  },
  {
    id: "topic-overworld-runtime",
    title: "Overworld Runtime",
    summary: "Overworld entities, camera, collision, movement, teleport, party presentation, and map interaction contracts.",
    aliases: ["overworld", "entities", "camera", "collision", "teleport"],
    keywords: ["overworld", "entity", "entities", "camera", "collision", "teleport", "walking", "movement", "map", "party", "door"],
    related: ["bank-c0", "runtime-systems"],
    banks: ["C0", "C3", "C4", "EF"]
  },
  {
    id: "topic-ui-rendering",
    title: "UI Rendering And Presentation",
    summary: "Menus, windows, tile staging, VWF/text rendering, file select, title/intro/credits, and presentation effects.",
    aliases: ["ui", "menus", "windows", "renderer", "presentation"],
    keywords: ["menu", "window", "tile", "vram", "renderer", "presentation", "file select", "title", "intro", "credits", "vwf", "hdma"],
    related: ["bank-c1", "bank-c4", "runtime-systems"],
    banks: ["C1", "C4", "E0", "E1"]
  },
  {
    id: "topic-debug-and-sram",
    title: "Debug, Save, And SRAM",
    summary: "Debug menu flows, save/SRAM helpers, checksum/state persistence, and late-bank support routines.",
    aliases: ["debug", "save", "sram", "state persistence"],
    keywords: ["debug", "debug menu", "save", "save slot", "sram", "checksum", "state persistence", "record playback"],
    related: ["bank-ef", "runtime-systems"],
    banks: ["EF"]
  },
  {
    id: "topic-validation-workflows",
    title: "Validation And Tooling",
    summary: "Byte-equivalence validation, extraction/generation tools, cross-check scripts, handoff commands, and workflow status.",
    aliases: ["validation", "tooling", "tools", "byte equivalence", "workflow"],
    keywords: ["validation", "validate", "byte equivalence", "tool", "workflow", "handoff", "crosscheck", "extract", "generate", "build candidate"],
    related: ["workflows", "tool-index"],
    banks: []
  },
  {
    id: "topic-audio-data",
    title: "Audio And Music Data",
    summary: "Audio-pack banks, music changes, APU transfer paths, sound menus, and sound data payloads.",
    aliases: ["audio", "music", "sound", "apu"],
    keywords: ["audio", "music", "sound", "apu", "song", "instrument"],
    related: ["asset-contracts"],
    banks: ["E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "EA", "EB", "EC", "ED", "EE", "EF"]
  }
];

function read(relativePath) {
  return fs.readFileSync(path.join(repoRoot, relativePath), "utf8");
}

function readContentJson(relativePath, fallback) {
  const absolutePath = path.join(contentDir, relativePath);
  if (!fs.existsSync(absolutePath)) {
    return fallback;
  }
  return JSON.parse(fs.readFileSync(absolutePath, "utf8"));
}

function exists(relativePath) {
  return fs.existsSync(path.join(repoRoot, relativePath));
}

const provenanceCatalog = {
  "project-authored": {
    label: "Project-authored",
    description: "Curated project prose, source-safe contracts, or checked-in documentation."
  },
  "generated-local": {
    label: "Generated locally",
    description: "Generated from the local decomp workspace or source-safe manifests."
  },
  "rom-derived-local": {
    label: "ROM-derived local",
    description: "Derived from a user-provided ROM and not intended for distribution."
  },
  "reference-imported": {
    label: "Reference/imported",
    description: "Imported or mirrored reference evidence used for comparison."
  }
};

const chapterScopeCatalog = {
  "rom-knowledge": {
    label: "ROM knowledge",
    description: "Facts about EarthBound's original data, routines, runtime behavior, or asset contracts."
  },
  "project-tooling": {
    label: "Project tooling",
    description: "Implementation details for local tools, validators, generators, harnesses, or backend adapters."
  },
  "local-generated": {
    label: "Local generated evidence",
    description: "Evidence produced locally from a user ROM or decomp workspace and kept out of distributed builds."
  },
  "release-policy": {
    label: "Release policy",
    description: "Distribution, provenance, public-status, confidence, or cleanup policy for the project."
  },
  "editor-guidance": {
    label: "Editor guidance",
    description: "Rules for safe authoring or editing built from ROM evidence and project validation."
  }
};

const localWorkspaceContract = {
  schema: "earthbound-decomp.local-workspace-contract.v1",
  expectedRom: {
    title: "EarthBound (USA), headerless",
    headerlessSize: 3145728,
    headeredSize: 3146240,
    headerlessSha1: "d67a8ef36ef616bc39306aa1b486e1bd3047815a"
  },
  artifactFamilies: [
    {
      id: "source",
      label: "Source Code",
      summary: "Generated byte-equivalent source, source snapshots, and symbol/source indexes.",
      localOnly: true,
      containsRomDerivedPayloads: true,
      exportKinds: ["source-tree", "source-snapshot", "manifest"]
    },
    {
      id: "graphics",
      label: "Graphics And Sprites",
      summary: "Decoded graphics, composed sprites, palette-applied sheets, battle visuals, UI, and font assets.",
      localOnly: true,
      containsRomDerivedPayloads: true,
      exportKinds: ["png", "json", "manifest", "zip"]
    },
    {
      id: "maps",
      label: "Maps And Tilesets",
      summary: "Map scene bundles, tilesets, arrangements, collision records, palette variants, and preview sheets.",
      localOnly: true,
      containsRomDerivedPayloads: true,
      exportKinds: ["png", "json", "manifest", "zip"]
    },
    {
      id: "audio",
      label: "Music And Audio",
      summary: "Audio pack contracts, SPC snapshots, WAV renders, render metrics, and playback/export manifests.",
      localOnly: true,
      containsRomDerivedPayloads: true,
      exportKinds: ["spc", "wav", "json", "manifest", "zip"]
    },
    {
      id: "tables",
      label: "Tables And Data Contracts",
      summary: "Generated table/data manifests, row contracts, payload-free schemas, and local extracted references.",
      localOnly: true,
      containsRomDerivedPayloads: false,
      exportKinds: ["json", "markdown", "manifest"]
    }
  ],
  policy: {
    checkedIn: "App shell, curated docs, payload-free contracts, generators, validators, and public manifests.",
    generatedLocal: "ROM-derived source, assets, audio, previews, cache files, and export bundles live in the user's local workspace.",
    neverDistributed: "ROM bytes, raw extracted copyrighted assets, generated SPC/WAV/PNG payloads, and generated byte-equivalent source."
  }
};

function inferProvenance(entry) {
  if (entry.provenance) {
    return entry.provenance;
  }
  if (buildMode === "authored" && ["bank", "text-command", "tool"].includes(entry.kind)) {
    return "project-authored";
  }
  if (entry.id === "rom-status") {
    return "rom-derived-local";
  }
  if (["chapter", "narrative", "learning-path", "topic", "workflow", "script-vm", "asset-contract", "search"].includes(entry.kind)) {
    return "project-authored";
  }
  if (entry.kind === "note") {
    return entry.sourcePath?.startsWith("refs/") ? "reference-imported" : "project-authored";
  }
  if (entry.kind === "source" || entry.kind === "source-file" || entry.kind === "routine" || entry.kind === "symbol") {
    return "generated-local";
  }
  if (entry.kind === "asset" || entry.kind === "asset-manifest") {
    return "generated-local";
  }
  return "generated-local";
}

function inferChapterScope(chapter) {
  if (chapter.scope) {
    return chapter.scope;
  }
  const id = String(chapter.id || "");
  const text = `${id} ${chapter.title || ""} ${chapter.summary || ""}`.toLowerCase();
  if (id.includes("audio-backend-adapter")) {
    return "project-tooling";
  }
  if (id.includes("audio-spc-renderer")) {
    return "local-generated";
  }
  if (text.includes("public status") || text.includes("known limits") || text.includes("validation workflow")) {
    return "release-policy";
  }
  if (text.includes("editing") || text.includes("editor")) {
    return "editor-guidance";
  }
  return "rom-knowledge";
}

function chapterScopeLabel(scope) {
  return chapterScopeCatalog[scope]?.label || scope || "Unscoped";
}

function addEntry(entry) {
  const normalized = {
    aliases: [],
    addresses: [],
    banks: [],
    sourceRefs: [],
    noteRefs: [],
    related: [],
    maturity: "curated",
    showInToc: true,
    tocPriority: 50,
    ...entry
  };
  normalized.provenance = inferProvenance(normalized);
  if (entryIds.has(normalized.id)) {
    return;
  }
  entryIds.add(normalized.id);
  entries.push(normalized);
  for (const ref of [...normalized.sourceRefs, ...normalized.noteRefs]) {
    if (ref.path && ref.entryId) {
      pathEntryIds.set(ref.path.replaceAll("\\", "/"), ref.entryId);
    }
  }
}

function noteRef(relativePath, label = relativePath) {
  return { path: relativePath, label };
}

function sourceRef(relativePath, label = relativePath) {
  return { path: relativePath, label };
}

function lines(markdown) {
  return markdown.replace(/\r\n/g, "\n").split("\n");
}

function parseMarkdownTable(markdown, requiredFirstColumn) {
  const output = [];
  for (const line of lines(markdown)) {
    const trimmed = line.trim();
    if (!trimmed.startsWith("|") || !trimmed.endsWith("|")) {
      continue;
    }
    if (trimmed.includes("---")) {
      continue;
    }
    const cells = trimmed.slice(1, -1).split("|").map((cell) => cell.trim().replace(/^`|`$/g, ""));
    if (cells[0] === requiredFirstColumn || cells[0] === "") {
      continue;
    }
    output.push(cells);
  }
  return output;
}

function stripTicks(value) {
  return String(value || "").replace(/`/g, "");
}

function slug(value) {
  return String(value).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}

function entryIdForPath(prefix, relativePath) {
  return `${prefix}-${slug(relativePath.replaceAll("\\", "/").replace(/\.[^.]+$/, ""))}`;
}

function repoRelative(filePath) {
  return path.relative(repoRoot, filePath).replaceAll("\\", "/");
}

function walkFiles(root, predicate = () => true) {
  const output = [];
  if (!fs.existsSync(root)) {
    return output;
  }
  for (const item of fs.readdirSync(root, { withFileTypes: true })) {
    const fullPath = path.join(root, item.name);
    if (item.isDirectory()) {
      output.push(...walkFiles(fullPath, predicate));
    } else if (predicate(fullPath)) {
      output.push(fullPath);
    }
  }
  return output;
}

function sourceRelative(filePath) {
  return path.relative(sourceRoot, filePath).replaceAll("\\", "/");
}

function readPreviousSourceSnapshot() {
  if (!fs.existsSync(sourceSnapshotPath)) {
    return null;
  }
  try {
    return JSON.parse(fs.readFileSync(sourceSnapshotPath, "utf8"));
  } catch {
    return null;
  }
}

function gitInfo(root) {
  const gitDir = path.join(root, ".git");
  const headPath = path.join(gitDir, "HEAD");
  if (!fs.existsSync(headPath)) {
    return { available: false };
  }

  const head = fs.readFileSync(headPath, "utf8").trim();
  if (head.startsWith("ref: ")) {
    const ref = head.slice(5);
    const refPath = path.join(gitDir, ...ref.split("/"));
    const sha = fs.existsSync(refPath) ? fs.readFileSync(refPath, "utf8").trim() : "";
    return {
      available: true,
      branch: ref.replace(/^refs\/heads\//, ""),
      sha,
      shortSha: sha ? sha.slice(0, 12) : ""
    };
  }

  return {
    available: true,
    branch: "(detached)",
    sha: head,
    shortSha: head ? head.slice(0, 12) : ""
  };
}

function collectSourceFiles() {
  const roots = [
    ["notes", (filePath) => filePath.endsWith(".md")],
    ["tools", (filePath) => filePath.endsWith(".py")],
    ...(buildMode === "local"
      ? [
          ["src", (filePath) => filePath.endsWith(".asm")],
          ["asset-manifests", (filePath) => filePath.endsWith(".json")]
        ]
      : [])
  ];
  const files = [];
  for (const [relativeRoot, predicate] of roots) {
    files.push(...walkFiles(path.join(sourceRoot, relativeRoot), predicate));
  }
  const readmePath = path.join(sourceRoot, "README.md");
  if (fs.existsSync(readmePath)) {
    files.push(readmePath);
  }
  return files.sort((a, b) => sourceRelative(a).localeCompare(sourceRelative(b)));
}

function buildSourceSnapshot() {
  const previous = readPreviousSourceSnapshot();
  const previousFiles = new Map((previous?.files || []).map((file) => [file.path, file]));
  const files = collectSourceFiles().map((filePath) => {
    const stat = fs.statSync(filePath);
    return {
      path: sourceRelative(filePath),
      size: stat.size,
      mtimeMs: Math.round(stat.mtimeMs)
    };
  });
  const currentFiles = new Map(files.map((file) => [file.path, file]));
  const added = [];
  const modified = [];
  const removed = [];

  for (const file of files) {
    const old = previousFiles.get(file.path);
    if (!old) {
      added.push(file.path);
    } else if (old.size !== file.size || old.mtimeMs !== file.mtimeMs) {
      modified.push(file.path);
    }
  }
  for (const file of previousFiles.values()) {
    if (!currentFiles.has(file.path)) {
      removed.push(file.path);
    }
  }

  const counts = files.reduce((acc, file) => {
    const top = file.path.split("/")[0];
    acc[top] = (acc[top] || 0) + 1;
    return acc;
  }, {});
  const latest = [...files]
    .sort((a, b) => b.mtimeMs - a.mtimeMs)
    .slice(0, 20)
    .map((file) => file.path);

  return {
    generatedAt: new Date().toISOString(),
    buildMode,
    sourceRoot: catalogSourceRoot,
    appRoot: catalogAppRoot,
    git: gitInfo(sourceRoot),
    counts,
    fileCount: files.length,
    changesSinceLastBuild: {
      hasPreviousSnapshot: Boolean(previous),
      added,
      modified,
      removed,
      total: added.length + modified.length + removed.length
    },
    latest,
    files
  };
}

function truncate(value, maxLength = 180) {
  const clean = String(value || "").replace(/\s+/g, " ").trim();
  if (clean.length <= maxLength) {
    return clean;
  }
  return `${clean.slice(0, maxLength - 3).trim()}...`;
}

function titleFromSlug(value) {
  return String(value)
    .replace(/\.[^.]+$/, "")
    .replace(/[_-]+/g, " ")
    .replace(/\b([a-z])/g, (match) => match.toUpperCase());
}

function markdownTitle(markdown, fallback) {
  const heading = lines(markdown).find((line) => line.startsWith("# "));
  return heading ? heading.replace(/^#\s+/, "").trim() : fallback;
}

function firstParagraph(markdown) {
  const paragraphs = [];
  let current = [];
  for (const line of lines(markdown)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#") || trimmed.startsWith("|") || trimmed.startsWith("```")) {
      if (current.length) {
        paragraphs.push(current.join(" "));
        current = [];
      }
      continue;
    }
    if (trimmed.startsWith("- ")) {
      continue;
    }
    current.push(trimmed);
    if (current.join(" ").length > 180) {
      break;
    }
  }
  if (current.length) {
    paragraphs.push(current.join(" "));
  }
  return truncate(paragraphs[0] || "Evidence note from the local decomp knowledge base.");
}

function markdownHeadings(markdown, limit = 12) {
  return lines(markdown)
    .filter((line) => /^#{2,3}\s+/.test(line))
    .map((line) => line.replace(/^#{2,3}\s+/, "").trim())
    .slice(0, limit);
}

function classifyNote(relativePath, title, markdown) {
  return topicConfigs
    .map((topic) => {
      const score = noteTopicScore(topic, relativePath, title, markdown);
      return { topic, score };
    })
    .filter(({ score }) => score >= 2)
    .sort((a, b) => b.score - a.score || a.topic.title.localeCompare(b.topic.title))
    .slice(0, 4)
    .map(({ topic }) => topic.id);
}

function noteTopicScore(topic, relativePath, title, markdown) {
  const strongHaystack = [
    relativePath,
    title,
    markdownHeadings(markdown, 20).join(" ")
  ].join(" ").toLowerCase();
  const weakHaystack = [
    firstParagraph(markdown),
    markdown.slice(0, 9000)
  ].join(" ").toLowerCase();

  return topic.keywords.reduce((total, keyword) => {
    const normalized = keyword.toLowerCase();
    return total
      + (strongHaystack.includes(normalized) ? 2 : 0)
      + (weakHaystack.includes(normalized) ? 1 : 0);
  }, 0);
}

function markdownPreview(markdown, maxChars = 2600) {
  if (markdown.length <= maxChars) {
    return markdown.trim();
  }

  let charCount = 0;
  let inFence = false;
  const kept = [];
  for (const line of lines(markdown)) {
    if (charCount + line.length + 1 > maxChars) {
      break;
    }
    if (line.startsWith("```")) {
      inFence = !inFence;
    }
    kept.push(line);
    charCount += line.length + 1;
  }
  if (inFence) {
    kept.push("```");
  }
  return kept.join("\n").trim();
}

function stripMarkdownForSearch(markdown) {
  return String(markdown || "")
    .replace(/```[\s\S]*?```/g, (match) => match.replace(/```[a-z]*\n?/gi, "").replace(/```/g, " "))
    .replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g, "$1 $2")
    .replace(/\[\[([^\]]+)\]\]/g, "$1")
    .replace(/[`*_#|>\-[\]()]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function compactSearchText(entry, fullBody) {
  const headings = markdownHeadings(fullBody, 80).join(" ");
  const labels = [...String(fullBody || "").matchAll(/\b([A-Z][A-Z0-9_]{2,}):/g)]
    .map((match) => match[1])
    .slice(0, 240)
    .join(" ");
  const metadata = [
    entry.title,
    entry.kind,
    entry.summary,
    entry.aliases && entry.aliases.join(" "),
    entry.addresses && entry.addresses.join(" "),
    entry.banks && entry.banks.join(" "),
    entry.sourceRefs && entry.sourceRefs.map((ref) => `${ref.label || ""} ${ref.path || ""}`).join(" "),
    entry.noteRefs && entry.noteRefs.map((ref) => `${ref.label || ""} ${ref.path || ""}`).join(" "),
    headings,
    labels
  ].filter(Boolean).join(" ");

  const bodyTerms = uniqueSearchTerms(fullBody, searchTextLimit);
  return `${metadata} ${bodyTerms}`.replace(/\s+/g, " ").trim();
}

function uniqueSearchTerms(markdown, maxChars) {
  const clean = stripMarkdownForSearch(markdown).toLowerCase();
  const seen = new Set();
  const terms = [];
  let charCount = 0;

  for (const match of clean.matchAll(/[a-z0-9_$:.]{2,}/g)) {
    const term = match[0].replace(/^[._$:]+|[._$:]+$/g, "");
    if (!term || seen.has(term)) {
      continue;
    }
    seen.add(term);
    terms.push(term);
    charCount += term.length + 1;
    if (charCount >= maxChars) {
      break;
    }
  }

  return terms.join(" ");
}

function deferredBodyStub(entry, fullBody) {
  const headings = markdownHeadings(fullBody, 10);
  const preview = markdownPreview(fullBody);
  return [
    entry.summary || "Large generated entry body.",
    "",
    "## Deferred Body",
    `This entry is ${fullBody.length.toLocaleString("en-US")} markdown characters, so the app keeps a compact stub in the startup catalog and loads the full body only when requested.`,
    "",
    headings.length ? "## In This Entry" : "",
    headings.map((heading) => `- ${heading}`).join("\n"),
    "",
    "## Preview",
    preview
  ].filter(Boolean).join("\n");
}

function deferHeavyBodies() {
  const stats = {
    count: 0,
    deferredChars: 0
  };

  for (const entry of entries) {
    const fullBody = String(entry.body || "");

    if (fullBody.length <= heavyBodyThreshold) {
      continue;
    }

    const fileName = `${entry.id}.js`;
    fs.writeFileSync(
      path.join(entryBodyDir, fileName),
      [
        "window.ENCYCLOPEDIA_ENTRY_BODIES = window.ENCYCLOPEDIA_ENTRY_BODIES || {};",
        `window.ENCYCLOPEDIA_ENTRY_BODIES[${JSON.stringify(entry.id)}] = ${JSON.stringify(fullBody)};`,
        ""
      ].join("\n"),
      "utf8"
    );

    entry.searchText = compactSearchText(entry, fullBody);
    entry.body = deferredBodyStub(entry, fullBody);
    entry.bodyChunk = `generated/entry-bodies/${fileName}`;
    entry.bodySize = fullBody.length;
    entry.deferredBody = true;
    stats.count += 1;
    stats.deferredChars += fullBody.length;
  }

  return stats;
}

function buildRelationshipGraph() {
  const entryById = new Map(entries.map((entry) => [entry.id, entry]));
  const edgeMap = new Map();

  function addEdge(source, target, type, weight = 1) {
    if (!source || !target || source === target || !entryById.has(source) || !entryById.has(target)) {
      return;
    }
    const key = `${source}\u0000${target}`;
    const existing = edgeMap.get(key);
    if (existing) {
      existing.weight += weight;
      existing.types = unique([...existing.types, type]);
      return;
    }
    edgeMap.set(key, { source, target, types: [type], weight });
  }

  for (const entry of entries) {
    for (const relatedId of entry.related || []) {
      addEdge(entry.id, relatedId, "related", 8);
    }
    for (const ref of entry.noteRefs || []) {
      addEdge(entry.id, ref.entryId, "note", 6);
    }
    for (const ref of entry.sourceRefs || []) {
      addEdge(entry.id, ref.entryId, "source", 6);
    }
    for (const bank of entry.banks || []) {
      addEdge(entry.id, `bank-${bank.toLowerCase()}`, "bank", 4);
    }
  }

  const edges = [...edgeMap.values()].sort((a, b) => {
    const sourceCompare = a.source.localeCompare(b.source);
    return sourceCompare || a.target.localeCompare(b.target);
  });
  const degree = new Map(entries.map((entry) => [entry.id, 0]));
  const neighborhoods = {};

  function addNeighbor(source, target, edge, direction) {
    const list = neighborhoods[source] || [];
    const existing = list.find((neighbor) => neighbor.id === target);
    const weight = edge.weight + (direction === "out" ? 1 : 0);
    if (existing) {
      existing.weight += weight;
      existing.types = unique([...existing.types, ...edge.types]);
      existing.directions = unique([...existing.directions, direction]);
      return;
    }
    list.push({
      id: target,
      weight,
      types: edge.types,
      directions: [direction]
    });
    neighborhoods[source] = list;
  }

  for (const edge of edges) {
    degree.set(edge.source, (degree.get(edge.source) || 0) + 1);
    degree.set(edge.target, (degree.get(edge.target) || 0) + 1);
    addNeighbor(edge.source, edge.target, edge, "out");
    addNeighbor(edge.target, edge.source, edge, "in");
  }

  for (const [id, list] of Object.entries(neighborhoods)) {
    neighborhoods[id] = list
      .sort((a, b) => b.weight - a.weight || (degree.get(b.id) || 0) - (degree.get(a.id) || 0) || entryById.get(a.id).title.localeCompare(entryById.get(b.id).title))
      .slice(0, 30);
  }

  const nodes = entries.map((entry) => ({
    id: entry.id,
    title: entry.title,
    kind: entry.kind,
    banks: entry.banks || [],
    degree: degree.get(entry.id) || 0
  }));
  const topHubs = nodes
    .filter((node) => node.id !== "search-results")
    .sort((a, b) => b.degree - a.degree || a.title.localeCompare(b.title))
    .slice(0, 18)
    .map((node) => node.id);

  return {
    stats: {
      nodeCount: nodes.length,
      edgeCount: edges.length,
      linkedNodeCount: nodes.filter((node) => node.degree > 0).length
    },
    nodes,
    edges,
    neighborhoods,
    topHubs
  };
}

function inferBankFromRelativePath(relativePath) {
  const normalized = relativePath.replaceAll("\\", "/");
  const srcMatch = normalized.match(/^src\/([c-e][0-9a-f])\//i);
  if (srcMatch) {
    return srcMatch[1].toUpperCase();
  }
  const bankMatch = normalized.match(/\bbank-([c-e][0-9a-f])\b/i) || normalized.match(/\bbank_([c-e][0-9a-f])\b/i);
  return bankMatch ? bankMatch[1].toUpperCase() : "";
}

function addressFromLabel(label) {
  const match = String(label).match(/^([C-E][0-9A-F])([0-9A-F]{4})_/i);
  return match ? `${match[1].toUpperCase()}:${match[2].toUpperCase()}` : "";
}

function labelEntryId(label) {
  return `symbol-${slug(label)}`;
}

function unique(values) {
  return [...new Set(values.filter(Boolean))];
}

function asmCallTargets(text) {
  return unique([...String(text || "").matchAll(/^\s*(?:jml|jmp|jsl|jsr|bra|beq|bne|bcc|bcs|bpl|bmi|bvc|bvs)(?:\.[a-z])?\s+([A-Za-z][A-Za-z0-9_]+)/gmi)]
    .map((match) => match[1]));
}

function addressFromFileName(name) {
  const match = String(name).match(/^([c-e][0-9a-f])_([0-9a-f]{4})(?:_([0-9a-f]{4}))?/i);
  if (!match) {
    return "";
  }
  return `${match[1].toUpperCase()}:${match[2].toUpperCase()}`;
}

function fencedCode(language, value) {
  return ["```" + language, value.replace(/\s+$/g, ""), "```"].join("\n");
}

function sourceEmbed(text, maxChars = 30000) {
  if (text.length <= maxChars) {
    return {
      note: "Full checked-in source module embedded.",
      code: text
    };
  }
  const excerpt = lines(text).slice(0, 360).join("\n");
  return {
    note: `Source module is ${text.length} characters; showing the first 360 lines. Open the source file for the full body.`,
    code: excerpt
  };
}

function markdownExcerpt(markdown, maxChars = 24000) {
  const withoutTitle = lines(markdown)
    .filter((line, index) => !(index === 0 && line.startsWith("# ")))
    .join("\n")
    .trim();
  if (withoutTitle.length <= maxChars) {
    return {
      note: "Full note content embedded.",
      markdown: withoutTitle
    };
  }

  let charCount = 0;
  let inFence = false;
  const kept = [];
  for (const line of lines(withoutTitle)) {
    if (charCount + line.length + 1 > maxChars) {
      break;
    }
    if (line.startsWith("```")) {
      inFence = !inFence;
    }
    kept.push(line);
    charCount += line.length + 1;
  }
  if (inFence) {
    kept.push("```");
  }
  return {
    note: `Note is ${withoutTitle.length} characters; showing the first ${charCount} characters. Open the source note for the full body.`,
    markdown: kept.join("\n").trim()
  };
}

function detectRom() {
  for (const candidate of romCandidates) {
    const absolutePath = path.join(repoRoot, candidate);
    if (!fs.existsSync(absolutePath)) {
      continue;
    }
    const bytes = fs.readFileSync(absolutePath);
    const sha1 = crypto.createHash("sha1").update(bytes).digest("hex").toUpperCase();
    return {
      path: candidate.replaceAll("\\", "/"),
      size: bytes.length,
      sha1,
      sizeOk: bytes.length === expectedRom.size,
      sha1Ok: sha1 === expectedRom.sha1
    };
  }
  return null;
}

function section(markdown, heading) {
  const all = lines(markdown);
  const start = all.findIndex((line) => line.trim() === `## ${heading}`);
  if (start === -1) {
    return "";
  }
  const end = all.findIndex((line, index) => index > start && /^##\s+/.test(line));
  return all.slice(start + 1, end === -1 ? all.length : end).join("\n").trim();
}

function noteLinkForPath(relativePath, label = relativePath) {
  return `[[${entryIdForPath("note", relativePath)}|${label}]]`;
}

function workstreamMatches(label, keywords, limit = 10) {
  const matches = upstreamSnapshot.files
    .filter((file) => file.path === "README.md" || file.path.startsWith("notes/"))
    .map((file) => {
      const text = read(file.path);
      const title = markdownTitle(text, titleFromSlug(path.basename(file.path)));
      const haystack = `${file.path} ${title} ${text.slice(0, 8000)}`.toLowerCase();
      const score = keywords.reduce((total, keyword) => total + (haystack.includes(keyword.toLowerCase()) ? 1 : 0), 0);
      return { file, title, score };
    })
    .filter((match) => match.score > 0)
    .sort((a, b) => b.score - a.score || a.file.path.localeCompare(b.file.path))
    .slice(0, limit);

  return {
    label,
    matches
  };
}

function sourceChangeList(paths, label) {
  if (!paths.length) {
    return `- ${label}: none`;
  }
  return [
    `- ${label}: ${paths.length}`,
    ...paths.slice(0, 20).map((file) => `  - \`${file}\``),
    paths.length > 20 ? `  - ${paths.length - 20} more omitted from this compact status page.` : ""
  ].filter(Boolean).join("\n");
}

function upstreamStatusBody() {
  const changes = upstreamSnapshot.changesSinceLastBuild;
  const workstreams = [
    workstreamMatches("Public Status Truthfulness", ["public status", "truthfulness", "project status", "known limits", "status"]),
    workstreamMatches("C3 Script Semantics", ["c3", "script semantics", "actionscript", "opcode", "event"]),
    workstreamMatches("Text VM / Localization Script Semantics", ["text vm", "text command", "localization", "authoring", "ebtext"]),
    workstreamMatches("Asset/Data Contracts", ["asset", "data contract", "manifest", "extract", "render"]),
    workstreamMatches("Editing/Validation Workflow", ["editing", "validation", "workflow", "byte equivalence", "build candidate"]),
    workstreamMatches("Known Limits Page", ["known limits", "limits", "confidence", "open questions", "boundary"])
  ];

  return [
    buildMode === "authored"
      ? "This catalog is the ROM-free authored release baseline. It is generated from source-safe project evidence and does not inspect local ROM paths."
      : "The encyclopedia is generated from an upstream decomp workspace. The app code and generated encyclopedia output stay in this workspace; notes, source, tools, and manifests are read from the source root below.",
    "",
    "## Source Root",
    `\`${catalogSourceRoot}\``,
    "",
    "## Git",
    upstreamSnapshot.git.available
      ? [
          `- Branch: \`${upstreamSnapshot.git.branch || "unknown"}\``,
          `- Commit: \`${upstreamSnapshot.git.shortSha || "unknown"}\``
        ].join("\n")
      : "- No Git metadata detected.",
    "",
    "## Imported File Counts",
    Object.entries(upstreamSnapshot.counts)
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([folder, count]) => `- \`${folder}\`: ${count}`)
      .join("\n"),
    "",
    "## Changes Since Last Build",
    changes.hasPreviousSnapshot
      ? [
          `- Total changed tracked source files: ${changes.total}`,
          sourceChangeList(changes.added, "Added"),
          sourceChangeList(changes.modified, "Modified"),
          sourceChangeList(changes.removed, "Removed")
        ].join("\n")
      : "This is the first tracked source snapshot for this encyclopedia build output.",
    "",
    "## Recent Source Files",
    upstreamSnapshot.latest.map((file) => `- \`${file}\``).join("\n"),
    "",
    "## Active Workstream Detectors",
    workstreams.map((stream) => [
      `### ${stream.label}`,
      stream.matches.length
        ? stream.matches.map((match) => `- ${noteLinkForPath(match.file.path, match.title)} - \`${match.file.path}\``).join("\n")
        : "- No matching notes detected yet."
    ].join("\n")).join("\n\n")
  ].join("\n");
}

function narrativeEvidenceMatches(chapter, limit = 16) {
  const configuredRefs = (chapter.noteRefs || [])
    .filter((ref) => exists(ref))
    .map((relativePath) => {
      const text = read(relativePath);
      const title = markdownTitle(text, titleFromSlug(path.basename(relativePath)));
      return {
        path: relativePath,
        entryId: entryIdForPath("note", relativePath),
        title,
        summary: firstParagraph(text),
        headings: markdownHeadings(text, 6),
        bank: inferBankFromRelativePath(relativePath),
        topics: classifyNote(relativePath, title, text),
        length: text.length,
        configured: true,
        score: 999
      };
    });
  const configuredPaths = new Set(configuredRefs.map((ref) => ref.path));
  const keywordMatches = upstreamSnapshot.files
    .filter((file) => (file.path === "README.md" || file.path.startsWith("notes/")) && !configuredPaths.has(file.path))
    .map((file) => {
      const text = read(file.path);
      const title = markdownTitle(text, titleFromSlug(path.basename(file.path)));
      const haystack = `${file.path} ${title} ${firstParagraph(text)} ${markdownHeadings(text, 16).join(" ")} ${text.slice(0, 8000)}`.toLowerCase();
      const score = (chapter.keywords || []).reduce((total, keyword) => total + (haystack.includes(keyword.toLowerCase()) ? 1 : 0), 0);
      return {
        path: file.path,
        entryId: entryIdForPath("note", file.path),
        title,
        summary: firstParagraph(text),
        headings: markdownHeadings(text, 6),
        bank: inferBankFromRelativePath(file.path),
        topics: classifyNote(file.path, title, text),
        length: text.length,
        configured: false,
        score
      };
    })
    .filter((match) => match.score > 0)
    .sort((a, b) => b.score - a.score || a.path.localeCompare(b.path));

  return [...configuredRefs, ...keywordMatches].slice(0, limit);
}

function renderNarrativeChapterBody(chapter, evidence) {
  const configuredCount = evidence.filter((match) => match.configured).length;
  const relatedCount = evidence.length - configuredCount;
  const scope = inferChapterScope(chapter);
  return [
    "## Chapter Status",
    `- Maturity: \`${chapter.maturity || "draft-narrative"}\``,
    `- Scope: \`${chapterScopeLabel(scope)}\``,
    chapterScopeCatalog[scope]?.description ? `- Scope meaning: ${chapterScopeCatalog[scope].description}` : "",
    `- Source root: \`${catalogSourceRoot}\``,
    `- Primary evidence notes: ${configuredCount}`,
    relatedCount ? `- Additional related notes: ${relatedCount}` : "",
    "",
    ...(chapter.sections || []).flatMap((section) => [
      `## ${section.title}`,
      ...(section.paragraphs || []).flatMap((paragraph) => [paragraph, ""]),
      section.bullets?.length ? section.bullets.map((bullet) => `- ${bullet}`).join("\n") : ""
    ]),
    "",
    evidence.length ? "## Evidence Reading Order" : "",
    evidence.map((match) => {
      const marker = match.configured ? "primary" : "related";
      const tags = [
        marker,
        match.bank ? `Bank ${match.bank}` : "",
        ...(match.topics || []).slice(0, 2).map((topicId) => topicConfigs.find((topic) => topic.id === topicId)?.title || "")
      ].filter(Boolean).join("; ");
      return `- ${noteLinkForPath(match.path, match.title)} - ${tags}; ${match.summary}`;
    }).join("\n"),
    "",
    chapter.related?.length ? "## Related Encyclopedia Entries" : "",
    (chapter.related || []).map((id) => `- [[${id}]]`).join("\n")
  ].filter(Boolean).join("\n");
}

function addNarrativeChapterEntries() {
  const chapters = narrativeChapterConfig.chapters || [];
  if (!chapters.length) {
    return;
  }

  addEntry({
    id: "narrative-index",
    title: "Narrative Chapter Index",
    kind: "chapter",
    summary: "Editable educational chapters that sit above generated notes, symbols, source entries, and asset manifests.",
    aliases: ["narrative chapters", "educational chapters", "chapter index"],
    related: ["overview", "topic-index", ...chapters.map((chapter) => chapter.id)],
    showInToc: true,
    body: [
      "Narrative chapters are the human-readable layer of the encyclopedia. They are maintained in `encyclopedia/content/narrative-chapters.json` and enriched with live upstream evidence during content generation.",
      "",
      "## Chapter Scopes",
      Object.entries(chapters.reduce((counts, chapter) => {
        const scope = inferChapterScope(chapter);
        counts[scope] = (counts[scope] || 0) + 1;
        return counts;
      }, {})).map(([scope, count]) => `- \`${chapterScopeLabel(scope)}\`: ${count}`).join("\n"),
      "",
      "## Chapters",
      chapters.map((chapter) => `- [[${chapter.id}|${chapter.title}]] - ${chapterScopeLabel(inferChapterScope(chapter))}; ${chapter.summary}`).join("\n")
    ].join("\n")
  });

  for (const chapter of chapters) {
    const evidence = narrativeEvidenceMatches(chapter);
    const noteRefs = unique([...(chapter.noteRefs || []).filter((ref) => exists(ref)), ...evidence.map((match) => match.path)])
      .map((ref) => noteRef(ref, ref));
    addEntry({
      id: chapter.id,
      title: chapter.title,
      kind: "narrative",
      summary: chapter.summary,
      maturity: chapter.maturity || "draft-narrative",
      chapterScope: inferChapterScope(chapter),
      aliases: chapter.aliases || [],
      banks: chapter.banks || [],
      noteRefs,
      related: unique([
        "narrative-index",
        "source-browser",
        ...(chapter.related || []),
        ...(chapter.banks || []).map((bank) => sourceBankIndexId(bank))
      ]),
      chapterEvidence: evidence.map((match) => ({
        id: match.entryId,
        path: match.path,
        title: match.title,
        summary: match.summary,
        headings: match.headings,
        bank: match.bank,
        topics: match.topics,
        length: match.length,
        configured: match.configured,
        score: match.score
      })),
      showInToc: true,
      body: renderNarrativeChapterBody(chapter, evidence)
    });

    const citedNoteEntryIds = noteRefs.map((ref) => entryIdForPath("note", ref.path));
    for (const noteEntry of entries) {
      if (noteEntry.kind === "note" && citedNoteEntryIds.includes(noteEntry.id)) {
        noteEntry.related = unique([...(noteEntry.related || []), chapter.id]);
      }
    }
  }
}

function learningPathIdForChapter(chapter) {
  return `learning-${String(chapter.id || "").replace(/^chapter-/, "")}`;
}

function entryTitleForId(id) {
  return entries.find((entry) => entry.id === id)?.title || id;
}

function learningPathEvidenceList(evidence, configured) {
  return evidence
    .filter((match) => Boolean(match.configured) === configured)
    .slice(0, configured ? 8 : 6)
    .map((match) => {
      const tags = [
        match.bank ? `Bank ${match.bank}` : "",
        ...(match.topics || []).slice(0, 2).map((topicId) => topicConfigs.find((topic) => topic.id === topicId)?.title || "")
      ].filter(Boolean).join("; ");
      return `- ${noteLinkForPath(match.path, match.title)}${tags ? ` - ${tags}` : ""}. ${match.summary}`;
    })
    .join("\n");
}

function renderLearningPathBody(chapter, chapterEntry, evidence) {
  const relatedEntries = unique([
    ...(chapter.related || []),
    ...(chapter.banks || []).map((bank) => `bank-${bank.toLowerCase()}`),
    ...(chapter.banks || []).map((bank) => sourceBankIndexId(bank)).filter((id) => entryIds.has(id))
  ]).filter((id) => entryIds.has(id));
  const primaryEvidence = learningPathEvidenceList(evidence, true);
  const relatedEvidence = learningPathEvidenceList(evidence, false);
  const searchTerms = unique([...(chapter.aliases || []), ...(chapter.keywords || [])]).slice(0, 16);

  return [
    `This learning path is a guided route through [[${chapter.id}|${chapter.title}]]. Use it when you want the educational order before dropping into notes, source files, or generated references.`,
    "",
    "## 1. Start With The Narrative",
    `Open [[${chapter.id}|${chapter.title}]] first. It explains the mental model and names the current confidence boundary before the evidence gets noisy.`,
    "",
    (chapter.sections || []).length ? "## 2. Concepts To Track" : "",
    (chapter.sections || []).map((section) => `- ${section.title}`).join("\n"),
    "",
    primaryEvidence ? "## 3. Primary Evidence" : "",
    primaryEvidence,
    "",
    relatedEvidence ? "## 4. Related Evidence" : "",
    relatedEvidence,
    "",
    relatedEntries.length ? "## 5. Practical References" : "",
    relatedEntries.map((id) => `- [[${id}|${entryTitleForId(id)}]]`).join("\n"),
    "",
    searchTerms.length ? "## Search Terms" : "",
    searchTerms.length ? searchTerms.map((term) => `- \`${term}\``).join("\n") : "",
    "",
    "## Promotion Note",
    "Generated references are evidence, not final prose. Promote a page into a stronger chapter section only when it teaches what can be safely inferred and what remains uncertain."
  ].filter(Boolean).join("\n");
}

function learningPathEntryItem(id, meta = "") {
  const entry = entries.find((candidate) => candidate.id === id);
  if (!entry) {
    return null;
  }
  return {
    id,
    title: entry.title,
    kind: entry.kind,
    meta: meta || entry.kind,
    summary: entry.summary || "",
    tags: entry.banks?.map((bank) => `Bank ${bank}`).slice(0, 3) || []
  };
}

function learningPathEvidenceItem(match, meta) {
  const entry = entries.find((candidate) => candidate.id === (match.id || match.entryId));
  return {
    id: match.id || match.entryId,
    title: match.title,
    kind: entry?.kind || "note",
    meta,
    summary: match.summary || entry?.summary || "",
    tags: [
      match.bank ? `Bank ${match.bank}` : "",
      ...(match.topics || []).slice(0, 2).map((topicId) => topicConfigs.find((topic) => topic.id === topicId)?.title || "")
    ].filter(Boolean)
  };
}

function buildLearningPathData(chapter, chapterEntry, evidence) {
  const relatedEntries = unique([
    ...(chapter.related || []),
    ...(chapter.banks || []).map((bank) => `bank-${bank.toLowerCase()}`),
    ...(chapter.banks || []).map((bank) => sourceBankIndexId(bank)).filter((id) => entryIds.has(id))
  ]).filter((id) => entryIds.has(id));
  const concepts = (chapter.sections || []).map((section) => ({
    title: section.title,
    summary: [
      ...(section.paragraphs || []),
      ...(section.bullets || [])
    ].join(" ")
  }));
  const searchTerms = unique([...(chapter.aliases || []), ...(chapter.keywords || [])]).slice(0, 16);
  return {
    chapterId: chapter.id,
    chapterTitle: chapter.title,
    maturity: chapter.maturity || "draft-narrative",
    steps: [
      {
        title: "Start With The Narrative",
        summary: "Read the chapter first so the evidence has context and confidence boundaries.",
        items: [learningPathEntryItem(chapter.id, "Narrative chapter")].filter(Boolean)
      },
      {
        title: "Concepts To Track",
        summary: "Keep these ideas in mind while reading notes and generated references.",
        concepts
      },
      {
        title: "Primary Evidence",
        summary: "Configured source notes for this chapter. These are the strongest evidence anchors.",
        items: evidence.filter((match) => match.configured).slice(0, 8).map((match) => learningPathEvidenceItem(match, "Primary evidence note"))
      },
      {
        title: "Related Evidence",
        summary: "Additional notes matched by keywords and topic classifiers.",
        items: evidence.filter((match) => !match.configured).slice(0, 6).map((match) => learningPathEvidenceItem(match, "Related evidence note"))
      },
      {
        title: "Practical References",
        summary: "Entries you are likely to use after reading the conceptual layer.",
        items: relatedEntries.map((id) => learningPathEntryItem(id)).filter(Boolean)
      },
      {
        title: "Search Terms",
        summary: "Useful terms for global search once you want to branch out.",
        terms: searchTerms
      }
    ],
    promotionNote: "Generated references are evidence, not final prose. Promote a page into a stronger chapter section only when it teaches what can be safely inferred and what remains uncertain."
  };
}

function addLearningPathEntries() {
  const chapters = narrativeChapterConfig.chapters || [];
  if (!chapters.length) {
    return;
  }
  const pathIds = chapters.map((chapter) => learningPathIdForChapter(chapter));
  addEntry({
    id: "learning-path-index",
    title: "Learning Path Index",
    kind: "learning-path",
    summary: "Guided reading routes through narrative chapters, primary evidence notes, and practical references.",
    aliases: ["learning paths", "reading paths", "guided reading", "study routes"],
    related: unique(["overview", "narrative-index", "topic-index", ...pathIds]),
    showInToc: true,
    tocPriority: 0,
    body: [
      "Learning paths are generated route cards. They sit between polished narrative chapters and raw generated references.",
      "",
      "Use them when you want a practical sequence: chapter first, primary evidence second, source/topic/bank references third.",
      "",
      "## Paths",
      chapters.map((chapter) => `- [[${learningPathIdForChapter(chapter)}|${chapter.title} Learning Path]] - ${chapter.summary}`).join("\n")
    ].join("\n")
  });

  for (const chapter of chapters) {
    const chapterEntry = entries.find((entry) => entry.id === chapter.id);
    if (!chapterEntry) {
      continue;
    }
    const evidence = chapterEntry.chapterEvidence || narrativeEvidenceMatches(chapter);
    const pathId = learningPathIdForChapter(chapter);
    const related = unique([
      "learning-path-index",
      chapter.id,
      ...(chapter.related || []),
      ...(chapter.banks || []).map((bank) => `bank-${bank.toLowerCase()}`),
      ...(chapter.banks || []).map((bank) => sourceBankIndexId(bank)).filter((id) => entryIds.has(id)),
      ...evidence.slice(0, 10).map((match) => match.id || match.entryId).filter(Boolean)
    ]).filter((id) => entries.some((entry) => entry.id === id) || id === "learning-path-index");

    addEntry({
      id: pathId,
      title: `${chapter.title} Learning Path`,
      kind: "learning-path",
      summary: `Guided reading route for ${chapter.title}.`,
      maturity: chapter.maturity || "draft-narrative",
      aliases: unique([`${chapter.title} path`, `${chapter.title} reading path`, ...(chapter.aliases || [])]),
      banks: chapter.banks || [],
      noteRefs: (chapter.noteRefs || []).filter((ref) => exists(ref)).map((ref) => noteRef(ref, ref)),
      related,
      showInToc: true,
      tocPriority: 20,
      learningPath: buildLearningPathData(chapter, chapterEntry, evidence),
      chapterScope: inferChapterScope(chapter),
      body: renderLearningPathBody(chapter, chapterEntry, evidence)
    });

    chapterEntry.related = unique([...(chapterEntry.related || []), pathId]);
    chapterEntry.body = [
      chapterEntry.body,
      "",
      "## Learning Path",
      `Open [[${pathId}|${chapter.title} Learning Path]] for a guided route through this chapter, its primary notes, and practical references.`
    ].join("\n");
  }

  const overview = entries.find((entry) => entry.id === "overview");
  if (overview) {
    overview.related = unique([...(overview.related || []), "learning-path-index"]);
    overview.body = overview.body.replace(
      "- Start with [[narrative-index|Narrative Chapter Index]] for educational chapters organized around active decomp workstreams.",
      "- Start with [[learning-path-index|Learning Path Index]] when you want guided reading routes through chapters, evidence notes, and practical references.\n- Use [[narrative-index|Narrative Chapter Index]] for the editable educational chapters behind those routes."
    );
  }

  const narrativeIndex = entries.find((entry) => entry.id === "narrative-index");
  if (narrativeIndex) {
    narrativeIndex.related = unique([...(narrativeIndex.related || []), "learning-path-index", ...pathIds]);
    narrativeIndex.body = [
      narrativeIndex.body,
      "",
      "## Learning Paths",
      chapters.map((chapter) => `- [[${learningPathIdForChapter(chapter)}|${chapter.title} Learning Path]]`).join("\n")
    ].join("\n");
  }

  for (const topicEntry of entries.filter((entry) => entry.kind === "topic")) {
    const matchedPaths = chapters
      .filter((chapter) => (chapter.related || []).includes(topicEntry.id))
      .map((chapter) => learningPathIdForChapter(chapter))
      .filter((id) => entryIds.has(id));
    if (matchedPaths.length) {
      topicEntry.related = unique([...(topicEntry.related || []), ...matchedPaths]);
      topicEntry.body = [
        topicEntry.body,
        "",
        "## Learning Paths",
        matchedPaths.map((id) => `- [[${id}|${entryTitleForId(id)}]]`).join("\n")
      ].join("\n");
    }
  }
}

const upstreamSnapshot = buildSourceSnapshot();
const narrativeChapterConfig = readContentJson("narrative-chapters.json", { chapters: [] });
const projectStatus = read("notes/project-status.md");
const sourceStatus = read("notes/source-scaffold-status.md");
const readiness = read("notes/source-readiness-triage.md");
const readableClosure = read("notes/readable-source-bank-closure.md");
const textManifest = read("notes/text-command-semantics-manifest.md");
const romStatus = buildMode === "local" ? detectRom() : null;

addEntry({
  id: "overview",
  title: "Project Overview",
  kind: "chapter",
  summary: "A distilled orientation for the current EarthBound decomp knowledge base.",
  aliases: ["status", "baseline", "project status"],
  noteRefs: [
    noteRef("README.md", "Repository README"),
    noteRef("notes/project-status.md", "Project Status")
  ],
  related: ["bank-map", "source-browser", "relationship-graph", "narrative-index", "topic-index", "catalog-build-status", "upstream-status", "rom-status", "semantic-frontiers", "workflows"],
  tocPriority: 0,
  body: [
    "The repository is structurally closed across all configured banks from `C0` through `EF`: every bank has a checked-in byte-equivalent source scaffold, and the audited source-heavy banks have no preserved native-source corridors left.",
    "",
    "This encyclopedia should treat that as a strong foundation, not as a claim that every routine and payload is semantically finished. The useful distinction is [[terminology|terminology]]: scaffold-backed bytes, decoded source, and semantically understood systems are separate milestones.",
    "",
    "## What This App Is For",
    "- Present durable conclusions instead of raw note dumps.",
    "- Link every bank, command, routine, table, and workflow to its own entry when one exists.",
    "- Keep evidence visible through source and note references.",
    "- Make search fast enough that it becomes the default way to move around the decomp.",
    "- Label project-authored content separately from generated local or ROM-derived local artifacts.",
    "",
    "## Current Reading Path",
    "- Start with [[narrative-index|Narrative Chapter Index]] for educational chapters organized around active decomp workstreams.",
    "- Open [[source-browser|Source Browser]] when you need the actual checked-in `.asm` file behind a bank, routine, asset, or scaffold note.",
    "- Open [[relationship-graph|Relationship Graph]] when you want to move through connected chapters, notes, banks, routines, symbols, and assets.",
    "- Start with [[bank-map|ROM And Bank Map]] for the whole scaffold.",
    "- Use [[topic-index|Topic Index]] when you want distilled knowledge areas instead of raw evidence-note files.",
    "- Check [[upstream-status|Upstream Source Status]] to confirm which decomp workspace generated this encyclopedia build.",
    "- Check [[catalog-build-status|Catalog Build Status]] to see build mode, provenance counts, and release readiness signals.",
    "- Check [[rom-status|ROM And Generated Content Status]] before running ROM-backed extraction or validation.",
    "- Check [[release-artifact-policy|Release Artifact Policy]] before deciding whether a generated output belongs in a distributable build.",
    "- Use [[runtime-systems|Runtime Systems]] for C0/C1/C2/C4/EF source-heavy work.",
    "- Use [[script-and-text-vms|Script And Text VMs]] for C3 event/actionscript and text-command semantics.",
    "- Use [[asset-contracts|Assets And Data Contracts]] for graphics, map, audio, and generated table banks."
  ].join("\n")
});

addEntry({
  id: "terminology",
  title: "Terminology",
  kind: "chapter",
  summary: "The key completion terms used throughout the decomp.",
  aliases: ["scaffold-backed", "decoded source", "semantically understood"],
  noteRefs: [noteRef("notes/project-status.md", "Project Status")],
  related: ["overview", "semantic-frontiers"],
  body: [
    "## Scaffold-backed",
    "Bytes are represented in checked-in assembler artifacts and pass byte-equivalence validation.",
    "",
    "## Decoded Source",
    "Bytes have been converted into instruction-by-instruction assembly, table definitions, or typed data emitters.",
    "",
    "## Semantically Understood",
    "Decoded source has reliable names, comments, call/data evidence, side-effect contracts, and editing constraints.",
    "",
    "The project is scaffold-backed ROM-wide. The next encyclopedia job is to make the semantic layer navigable."
  ].join("\n")
});

addEntry({
  id: "relationship-graph",
  title: "Relationship Graph",
  kind: "chapter",
  summary: "Interactive map of generated encyclopedia links across chapters, topics, banks, notes, source references, routines, symbols, and assets.",
  aliases: ["graph", "knowledge graph", "link graph", "relationships", "network"],
  related: ["overview", "narrative-index", "topic-index", "bank-map", "source-browser", "routine-index", "asset-manifest-index"],
  body: [
    "The relationship graph is generated at build time from explicit `related` links, note/source evidence references, and bank membership.",
    "",
    "Use it as a navigation aid: start from a chapter or topic, inspect its neighborhood, then open linked evidence entries when you need the underlying notes, source modules, symbols, or asset manifests.",
    "",
    "The visual graph is rendered by the app from a compact generated index, so it does not need to load deferred heavy entry bodies."
  ].join("\n")
});

addEntry({
  id: "bank-map",
  title: "ROM And Bank Map",
  kind: "chapter",
  summary: "A bank-level view of scaffold status, roles, and next work.",
  aliases: ["bank map", "banks", "rom map", "source scaffold status"],
  noteRefs: [
    noteRef("notes/source-scaffold-status.md", "Source Scaffold Status"),
    noteRef("notes/source-readiness-triage.md", "Source Readiness Triage")
  ],
  related: ["runtime-systems", "asset-contracts"],
  body: [
    "Every configured bank from `C0` through `EF` is closed and byte-equivalent. Bank entries below are generated from the scaffold and readiness dashboards.",
    "",
    "## Bank Groups",
    section(projectStatus, "Bank Groups"),
    "",
    "## Generated Bank Entries",
    "Search or use the table of contents to open individual bank pages such as [[bank-c0|Bank C0]], [[bank-c3|Bank C3]], or [[bank-ef|Bank EF]]."
  ].join("\n")
});

addEntry({
  id: "runtime-systems",
  title: "Runtime Systems",
  kind: "chapter",
  summary: "The source-heavy banks where semantic naming and side-effect contracts matter most.",
  aliases: ["runtime", "source-heavy banks", "C0 C1 C2 C4 EF"],
  banks: ["C0", "C1", "C2", "C4", "EF"],
  noteRefs: [
    noteRef("notes/source-readiness-triage.md", "Source Readiness Triage"),
    noteRef("notes/readable-source-bank-closure.md", "Readable Source Bank Closure")
  ],
  related: ["bank-c0", "bank-c1", "bank-c2", "bank-c4", "bank-ef"],
  body: [
    "Readable source-bank closure is complete for the audited runtime banks. The remaining work is semantic polish: names, comments, data contracts, side-effect documentation, and validation paths.",
    "",
    "## Priority Runtime Banks",
    "- [[bank-c0|C0]]: overworld, entity, task, movement, interaction, collision, teleport, and PPU helper contracts.",
    "- [[bank-c1|C1]]: text engine, CCS leaves, menus, battle front ends, and file select.",
    "- [[bank-c2|C2]]: battle runtime, action dispatch, target selection, status/effect families, and battle visuals.",
    "- [[bank-c4|C4]]: renderer-facing text tile staging, movement presentation, window/color HDMA, file select, town map, and presentation effects.",
    "- [[bank-ef|EF]]: save/SRAM, debug/menu routines, map tables, text/help script runs, glyph masks, and late tail data."
  ].join("\n")
});

addEntry({
  id: "script-and-text-vms",
  title: "Script And Text VMs",
  kind: "script-vm",
  summary: "The C3 event/actionscript and C1/C5-C9 text-command systems.",
  aliases: ["C3 scripts", "text command VM", "localization scripts", "actionscript"],
  banks: ["C1", "C3", "C5", "C6", "C7", "C8", "C9", "EF"],
  noteRefs: [
    noteRef("notes/text-command-semantics-manifest.md", "Text Command Semantics Manifest"),
    noteRef("notes/c3-actionscript-semantics-audit.md", "C3 Actionscript Semantics Audit")
  ].filter((ref) => exists(ref.path)),
  related: ["text-command-vm", "bank-c3"],
  body: [
    "This is the highest leverage area for turning the scaffold into editable knowledge. C3 carries event/actionscript assets; C1 and the text banks carry the text-command runtime and parsed script payloads.",
    "",
    "## Text Command VM",
    "The text-command manifest currently tracks top-level commands, structured command families, parsed hits, runtime dispatchers, and recovered localization authoring syntax signals. Open [[text-command-vm|Text Command VM]] for the generated overview.",
    "",
    "## C3 Event/Actionscript",
    "C3 has no unexplained raw follow-up frontier for the current milestone. The remaining work is opcode semantics, operand names, callback argument contracts, and source/script emission polish."
  ].join("\n")
});

addEntry({
  id: "asset-contracts",
  title: "Assets And Data Contracts",
  kind: "asset-contract",
  summary: "Graphics, map, audio, text, and generated table payloads by bank family.",
  aliases: ["assets", "data contracts", "asset manifests"],
  noteRefs: [
    noteRef("notes/asset-manifest-generation-status.md", "Asset Manifest Generation Status"),
    noteRef("notes/source-readiness-triage.md", "Source Readiness Triage")
  ].filter((ref) => exists(ref.path)),
  related: ["bank-ca", "bank-cb", "bank-d1", "bank-e0", "bank-ee"],
  body: [
    "Asset and data banks are structurally mapped, but many still need typed emitters, render/decode fixtures, and stronger row-level semantics.",
    "",
    "Open [[asset-manifest-index|Asset Manifest Index]] for the generated manifest and asset inventory.",
    "",
    "## Main Families",
    "- `CA..CE`: battle backgrounds, battle sprites, animation, PSI, swirl, Sound Stone assets.",
    "- `CF..D0`, `D5`, `D7`, `D8`: generated tables and mixed map/battle data contracts.",
    "- `D1..D4`, `D6`, `D9..DF`: overworld sprites, map tiles, arrangements, palettes, collision, and audio tails.",
    "- `E0..E1`: UI, fonts, town maps, intro/title/ending/cast assets.",
    "- `E2..EE`: audio-pack payloads."
  ].join("\n")
});

addEntry({
  id: "semantic-frontiers",
  title: "Semantic Frontiers",
  kind: "workflow",
  summary: "The next work after scaffold closure: semantics, contracts, fixtures, and editable assets.",
  aliases: ["frontiers", "remaining work", "next work"],
  noteRefs: [noteRef("notes/source-readiness-triage.md", "Source Readiness Triage")],
  related: ["overview", "script-and-text-vms", "asset-contracts"],
  body: section(readiness, "Immediate Workstreams")
});

addEntry({
  id: "workflows",
  title: "Validation And Research Workflows",
  kind: "workflow",
  summary: "Common commands for validating, regenerating, and inspecting the decomp.",
  aliases: ["validation", "tools", "commands", "workflow"],
  noteRefs: [noteRef("README.md", "Repository README")],
  related: ["bank-map", "semantic-frontiers"],
  body: [
    "## Validate One Source Bank",
    "```powershell",
    "python tools/validate_source_bank_byte_equivalence.py --bank C3",
    "```",
    "",
    "## Regenerate Core Dashboards",
    "```powershell",
    "python tools/build_readable_source_bank_closure.py",
    "python tools/build_c3_source_data_map.py",
    "python tools/build_text_command_semantics_manifest.py",
    "```",
    "",
    "## Inspect References And Data",
    "```powershell",
    "python tools/find_xrefs.py C20ABC --limit 12",
    "python tools/find_direct_callers.py C2:D121",
    "python tools/decode_snippet.py C1:244C --count 20 --show-state",
    "python tools/inspect_table.py --contract ENEMY_CONFIGURATION_TABLE --index 0 --count 1",
    "```"
  ].join("\n")
});

addEntry({
  id: "rom-status",
  title: "ROM And Generated Content Status",
  kind: "workflow",
  summary: romStatus
    ? `Detected ${romStatus.path}; SHA-1 ${romStatus.sha1Ok ? "matches" : "does not match"} the expected US headerless ROM.`
    : "No ROM detected in the configured local paths.",
  aliases: ["rom", "baserom", "rom status", "generated content", "extraction"],
  related: ["workflows", "bank-map", "asset-contracts"],
  provenance: buildMode === "local" ? "rom-derived-local" : "project-authored",
  body: [
    buildMode === "local"
      ? "This page reports whether the local generator can safely run ROM-backed validation and extraction workflows."
      : "This authored-mode catalog does not inspect local ROM paths. ROM verification belongs to the future first-run/local workspace flow.",
    "",
    "## Build Mode",
    `- Mode: \`${buildMode}\``,
    buildMode === "authored"
      ? "- ROM-backed extraction and preview generation are disabled for this catalog."
      : "- ROM-backed detection is enabled for this local catalog.",
    "",
    "## Detection",
    buildMode === "authored"
      ? "- Skipped in authored mode."
      : romStatus
      ? [
          `- Path: \`${romStatus.path}\``,
          `- Size: \`${romStatus.size}\` bytes (${romStatus.sizeOk ? "matches expected size" : "unexpected size"})`,
          `- SHA-1: \`${romStatus.sha1}\` (${romStatus.sha1Ok ? "matches expected ROM" : "does not match expected ROM"})`
        ].join("\n")
      : romCandidates.map((candidate) => `- Missing: \`${candidate}\``).join("\n"),
    "",
    "## Policy",
    "- The encyclopedia should use the ROM to verify and regenerate local manifests, source maps, and metadata.",
    "- It should not commit generated copyrighted asset payloads into the repo by default.",
    "- ROM-derived outputs should live under ignored build folders unless a specific source-safe artifact is intentionally promoted.",
    "",
    "## Next Implementation Hook",
    "A future `build:from-rom` command can run validation and extraction tools when this page reports a matching ROM, then refresh the generated encyclopedia catalog."
  ].join("\n")
});

addEntry({
  id: "local-workspace",
  title: "Local Workspace",
  kind: "workflow",
  summary: "Select and verify a user-provided ROM, create a local app-data workspace, and generate ROM-derived artifacts outside the shipped app.",
  aliases: ["first run", "add rom", "rom import", "workspace", "local generated content"],
  related: ["asset-library", "rom-status", "release-artifact-policy", "catalog-build-status", "asset-contracts"],
  provenance: "project-authored",
  body: [
    "The local workspace is the app boundary between source-safe knowledge and ROM-derived generated artifacts.",
    "",
    "## First Run",
    "- Open the encyclopedia without a ROM to read project-authored notes and contracts.",
    "- Select an EarthBound ROM to verify size, header status, and SHA-1.",
    "- A verified ROM creates a hash-keyed app-data workspace for generated source, assets, audio, previews, manifests, cache files, and export bundles.",
    "",
    "## Verification Contract",
    `- Expected headerless size: \`${localWorkspaceContract.expectedRom.headerlessSize}\` bytes.`,
    `- Expected headered size: \`${localWorkspaceContract.expectedRom.headeredSize}\` bytes; the first 512 bytes are ignored for identity checks.`,
    `- Expected headerless SHA-1: \`${localWorkspaceContract.expectedRom.headerlessSha1}\`.`,
    "",
    "## Policy",
    `- Checked in: ${localWorkspaceContract.policy.checkedIn}`,
    `- Generated locally: ${localWorkspaceContract.policy.generatedLocal}`,
    `- Never distributed: ${localWorkspaceContract.policy.neverDistributed}`,
    "",
    "Use the live controls on this page in the Electron app to add or replace a ROM. The static browser build can still be used in notes-only mode."
  ].join("\n")
});

addEntry({
  id: "asset-library",
  title: "Asset Library",
  kind: "asset-contract",
  summary: "Browse local ROM-derived source, graphics, maps, tables, and audio exports by organized artifact family.",
  aliases: ["generated assets", "asset browser", "export assets", "bulk export", "music exports", "sprite exports"],
  related: ["local-workspace", "asset-contracts", "chapter-audio-pack-frontier", "chapter-audio-backend-adapter-contract", "release-artifact-policy"],
  provenance: "project-authored",
  body: [
    "The Asset Library is the browsing and export surface for locally generated artifacts.",
    "",
    "## Families",
    localWorkspaceContract.artifactFamilies.map((family) => `- **${family.label}**: ${family.summary}`).join("\n"),
    "",
    "## Export Rule",
    "Exports are user-local only. Individual files and zip bundles may include ROM-derived payloads, so they belong outside distributed builds and outside the checked-in repository.",
    "",
    "Use the live controls on this page after adding a ROM to inspect family readiness, open related contracts, and prepare local export bundles."
  ].join("\n")
});

addEntry({
  id: "release-artifact-policy",
  title: "Release Artifact Policy",
  kind: "workflow",
  summary: "What belongs in the shipped encyclopedia app, what is generated locally, and what must never be distributed.",
  aliases: ["release policy", "artifact policy", "distribution policy", "copyright-safe release"],
  related: ["overview", "catalog-build-status", "rom-status", "workflows", "asset-contracts", "upstream-status"],
  provenance: "project-authored",
  body: [
    "The release boundary is intentionally conservative. The app should publish knowledge, contracts, generators, and validators; the user's ROM should produce protected payloads locally.",
    "",
    "## Checked In",
    "- Encyclopedia shell, curated chapters, schemas, public payload-free manifests, tools, validation logic, and source-generation code.",
    "",
    "## User Provided",
    "- EarthBound ROM file and optional local decomp/source workspace paths.",
    "",
    "## Generated Locally",
    "- Byte-equivalent `src/`, local `asset-manifests/`, renderer fixtures, source snapshots, search catalogs, extracted references, preview sheets, SPC/WAV exports, and cache files.",
    "",
    "## Never Distributed",
    "- ROM bytes, raw extracted copyrighted assets, generated audio/images that contain ROM-derived content, or generated byte-equivalent source built from the user's ROM.",
    "",
    "## Release Shape",
    "- The packaged app should be usable in authored mode without a ROM.",
    "- Selecting a ROM should verify size and SHA-1, then generate local workspace artifacts under an app-data folder.",
    "- Entries should keep provenance visible: project-authored, generated locally, ROM-derived local, or reference/imported.",
    "- Run `npm run audit:release` before packaging."
  ].join("\n")
});

addEntry({
  id: "release-readiness-checklist",
  title: "Release Readiness Checklist",
  kind: "workflow",
  summary: "Current release blockers and presentation gaps before publishing the standalone Electron app.",
  aliases: ["release checklist", "known missing content", "packaging status", "github release"],
  related: ["release-artifact-policy", "local-workspace", "asset-library", "catalog-build-status", "chapter-known-limits"],
  provenance: "project-authored",
  chapterScope: "release-policy",
  showInToc: true,
  body: [
    "This checklist keeps the release target visible inside the authored app.",
    "",
    "## Package Boundary",
    "- Authored release builds must contain no ROM, source files, generated source entries, asset entries, raw extracted payloads, preview sheets, SPC/WAV exports, or cache files.",
    "- The app package contains documentation, learning paths, ROM-knowledge chapters, source-safe workflow pages, and the first-run local workspace shell.",
    "- ROM-backed source, graphics, maps, audio, table manifests, and ZIP exports are generated only under the user's app-data workspace after ROM verification.",
    "",
    "## Binary Release Work",
    "- Windows unsigned NSIS and ZIP artifacts can be produced from this workspace.",
    "- Linux ZIP artifacts can be produced from this Windows workspace.",
    "- Linux AppImage should be built on Linux/CI or on Windows with symlink privileges enabled.",
    "- A real app icon, publisher metadata, project license, and third-party notice bundle are still required before a public binary release.",
    "",
    "## Generator Work",
    "- Current Electron generator stages create local workspace manifests, source scaffolds, ROM/header/bank manifests, and family handoff manifests.",
    "- Full renderer stages still need to attach compiled sprites, palette-applied sheets, map previews, SPC exports, WAV exports, and searchable generated catalog hydration.",
    "",
    "## Content And Access Gaps",
    "- NPC AI bytes, concrete shop selector paths, encoded PSI menu row decoding, map preview/editor rules, audio runtime state capture, and asset-family editor rules remain the highest-value content polish targets.",
    "- The Asset Library is the correct home for generated content, but it needs per-family browsers once the generator outputs real rendered artifacts.",
    "- The Local Workspace and Release Artifact Policy pages should remain the clearest explanation of project-authored versus ROM-derived local material."
  ].join("\n")
});

addEntry({
  id: "upstream-status",
  title: "Upstream Source Status",
  kind: "workflow",
  summary: `Generated from ${catalogSourceRoot}.`,
  aliases: ["upstream", "source root", "import status", "decomp workspace", "codex workspace"],
  related: ["overview", "topic-index", "workflows", "rom-status"],
  body: upstreamStatusBody()
});

addEntry({
  id: "search-results",
  title: "Search Results",
  kind: "search",
  summary: "A tab-backed view of the latest search results.",
  showInToc: false,
  body: "Search from the top bar to populate this tab."
});

addNarrativeChapterEntries();

const scaffoldRows = parseMarkdownTable(sourceStatus, "Bank");
const readinessRows = parseMarkdownTable(readiness, "Bank");
const readinessByBank = new Map(readinessRows.map((row) => [stripTicks(row[0]).toUpperCase(), row]));
const readableRows = parseMarkdownTable(readableClosure, "Bank");
const readableByBank = new Map(readableRows.map((row) => [stripTicks(row[0]).toUpperCase(), row]));

for (const row of scaffoldRows) {
  const bank = stripTicks(row[0]).toUpperCase();
  if (!/^[C-E][0-9A-F]$/.test(bank)) {
    continue;
  }
  const readinessRow = readinessByBank.get(bank);
  const closureRow = readableByBank.get(bank);
  const bankLower = bank.toLowerCase();
  const scaffoldPath = `src/${bankLower}/bank_${bankLower}_helpers_asar.asm`;
  const nextAction = readinessRow ? stripTicks(readinessRow[4]) : "No generated readiness row found yet.";
  const role = readinessRow ? stripTicks(readinessRow[1]) : "bank scaffold";
  const readinessLabel = readinessRow ? stripTicks(readinessRow[2]) : "closed";
  const priority = readinessRow ? stripTicks(readinessRow[3]) : "-";
  const closureText = closureRow
    ? `Readable-source closure: decoded ASM ${stripTicks(closureRow[1])}, preserved corridors ${stripTicks(closureRow[2])}, known data/assets ${stripTicks(closureRow[3])}.`
    : "Readable-source closure is not part of the audited source-heavy bank set.";

  addEntry({
    id: `bank-${bankLower}`,
    title: `Bank ${bank}`,
    kind: "bank",
    summary: `${role}; scaffold status ${stripTicks(row[1])}, byte equivalence ${stripTicks(row[5])}.`,
    maturity: "generated-summary",
    aliases: [bank, `bank ${bank}`, `${bank} bank`, scaffoldPath],
    banks: [bank],
    sourceRefs: [sourceRef(scaffoldPath, `Bank ${bank} scaffold`)],
    noteRefs: [
      noteRef("notes/source-scaffold-status.md", "Source Scaffold Status"),
      noteRef("notes/source-readiness-triage.md", "Source Readiness Triage"),
      ...(closureRow ? [noteRef("notes/readable-source-bank-closure.md", "Readable Source Bank Closure")] : [])
    ],
    related: bank === "C3" ? ["script-and-text-vms"] : ["bank-map"],
    body: [
      `Bank \`${bank}\` is classified as **${role}** with readiness \`${readinessLabel}\` and priority \`${priority}\`.`,
      "",
      "## Scaffold Status",
      `| Status | Ranges | Protected Bytes | Residual Bytes | Byte Equivalence | Mismatches |`,
      `| --- | ---: | ---: | ---: | --- | ---: |`,
      `| \`${stripTicks(row[1])}\` | ${stripTicks(row[2])} | ${stripTicks(row[3])} | ${stripTicks(row[4])} | \`${stripTicks(row[5])}\` | ${stripTicks(row[6])} |`,
      "",
      "## Readability",
      closureText,
      "",
      "## Next Action",
      nextAction
    ].join("\n")
  });
}

const commandRows = parseMarkdownTable(section(textManifest, "Top-Level Commands"), "Opcode");

addEntry({
  id: "text-command-vm",
  title: "Text Command VM",
  kind: "script-vm",
  summary: "Generated overview of top-level text commands and structured families.",
  aliases: ["text commands", "text-command semantics", "C1 text runtime"],
  banks: ["C1", "C5", "C6", "C7", "C8", "C9", "EF"],
  noteRefs: [noteRef("notes/text-command-semantics-manifest.md", "Text Command Semantics Manifest")],
  related: ["script-and-text-vms"],
  body: [
    section(textManifest, "Summary"),
    "",
    "## Top-Level Commands",
    commandRows
      .filter((row) => /^0x[0-9A-F]{2}$/i.test(stripTicks(row[0])))
      .map((row) => `- [[text-command-${stripTicks(row[0]).slice(2).toLowerCase()}|${stripTicks(row[0])} ${stripTicks(row[1])}]] - ${stripTicks(row[2])}, parsed hits ${stripTicks(row[3])}`)
      .join("\n")
  ].join("\n")
});

for (const row of commandRows) {
  const opcode = stripTicks(row[0]);
  if (!/^0x[0-9A-F]{2}$/i.test(opcode)) {
    continue;
  }
  const commandId = `text-command-${opcode.slice(2).toLowerCase()}`;
  const name = stripTicks(row[1]);
  const status = stripTicks(row[2]);
  const hits = stripTicks(row[3]);
  const runtime = stripTicks(row[4]);
  const notes = stripTicks(row[5]);
  const noteRefs = notes
    .split(",")
    .map((value) => value.trim())
    .filter((value) => value.endsWith(".md"))
    .map((value) => noteRef(`notes/${value}`, value))
    .filter((ref) => exists(ref.path));

  addEntry({
    id: commandId,
    title: `${opcode} ${name}`,
    kind: "text-command",
    summary: `Text command ${name} is ${status} with ${hits} parsed hits.`,
    maturity: "generated-summary",
    aliases: [opcode, name, `text command ${opcode}`, `text command ${name}`],
    addresses: runtime === "-" ? [] : [runtime],
    banks: ["C1", "C5", "C6", "C7", "C8", "C9", "EF"],
    noteRefs: [
      noteRef("notes/text-command-semantics-manifest.md", "Text Command Semantics Manifest"),
      ...noteRefs
    ],
    related: ["text-command-vm", "script-and-text-vms"],
    body: [
      `\`${opcode}\` is named \`${name}\` and currently has status \`${status}\`.`,
      "",
      "## Evidence",
      `| Parsed Hits | Runtime | Notes |`,
      `| ---: | --- | --- |`,
      `| ${hits} | \`${runtime}\` | ${notes || "-"} |`,
      "",
      status === "parsed_only"
        ? "This command is parser-only in the current model and should not be treated as a live runtime dispatcher without additional evidence."
        : "This command is covered by the current text-command manifest and should be linked from text/script discussions when referenced."
    ].join("\n")
  });
}

const toolNames = fs.readdirSync(path.join(repoRoot, "tools"))
  .filter((name) => name.endsWith(".py"))
  .sort();

for (const name of toolNames) {
  const relativePath = `tools/${name}`;
  const id = entryIdForPath("tool", relativePath);
  const source = read(relativePath);
  const firstComment = lines(source)
    .map((line) => line.trim())
    .find((line) => line.startsWith("# ") && !line.startsWith("#!/"));
  pathEntryIds.set(relativePath, id);

  addEntry({
    id,
    title: name,
    kind: "tool",
    summary: firstComment ? firstComment.replace(/^#\s+/, "") : "Local Python helper from the decomp toolchain.",
    maturity: "generated-tool",
    aliases: [name, relativePath, name.replace(/\.py$/, "").replaceAll("_", " ")],
    sourceRefs: [sourceRef(relativePath, relativePath)],
    related: ["tool-index", "workflows"],
    showInToc: false,
    body: [
      "## Tool Path",
      `\`${relativePath}\``,
      "",
      "## Role",
      firstComment ? firstComment.replace(/^#\s+/, "") : "No top-level summary comment found yet.",
      "",
      "Use this page as a searchable handle for workflow documentation and future command examples."
    ].join("\n")
  });
}

addEntry({
  id: "tool-index",
  title: "Tool Index",
  kind: "workflow",
  summary: "Generated index of local Python tools available to the decomp workflow.",
  aliases: ["tools index", "python tools"],
  sourceRefs: toolNames.map((name) => sourceRef(`tools/${name}`, name)),
  related: ["workflows"],
  body: [
    "The repository includes local Python helpers for validation, manifest generation, source promotion, xref lookup, decoding, inspection, extraction, and rendering.",
    "",
    "## Tools",
    toolNames.map((name) => `- [[${entryIdForPath("tool", `tools/${name}`)}|${name}]]`).join("\n")
  ].join("\n")
});

const srcBanks = buildMode === "local" && fs.existsSync(srcDir)
  ? fs.readdirSync(srcDir, { withFileTypes: true })
    .filter((dirent) => dirent.isDirectory())
    .map((dirent) => dirent.name.toUpperCase())
    .sort()
  : [];

addEntry({
  id: "source-tree",
  title: "Source Tree",
  kind: buildMode === "local" ? "source" : "workflow",
  summary: buildMode === "local"
    ? "Generated overview of checked-in source scaffold directories."
    : "Release baseline workspace placeholder for source generated only after ROM verification.",
  aliases: ["src", "source scaffold", "source files"],
  related: ["source-browser", "routine-index", "bank-map"],
  body: [
    buildMode === "local"
      ? "Each bank directory contains checked-in source scaffold modules that reproduce original ROM bytes."
      : "The authored release baseline does not distribute generated byte-equivalent `src/` modules. Source browsing becomes available after a local workspace is generated from a user-provided ROM or decomp source root.",
    "",
    buildMode === "local"
      ? "Open [[source-browser|Source Browser]] for all checked-in `.asm` files, including data-heavy banks and scaffold files. Open [[routine-index|Routine Index]] for semantically richer source-heavy routine pages."
      : "Open [[release-artifact-policy|Release Artifact Policy]] for the distribution boundary.",
    "",
    srcBanks.length ? "## Bank Directories" : "",
    srcBanks.map((bank) => `- [[bank-${bank.toLowerCase()}|Bank ${bank}]]`).join("\n")
  ].join("\n")
});

function addEvidenceNoteEntries() {
  const noteFiles = [
    path.join(repoRoot, "README.md"),
    ...walkFiles(notesDir, (filePath) => filePath.endsWith(".md"))
  ].sort((a, b) => repoRelative(a).localeCompare(repoRelative(b)));

  for (const filePath of noteFiles) {
    const relativePath = repoRelative(filePath);
    const markdown = fs.readFileSync(filePath, "utf8");
    const id = entryIdForPath("note", relativePath);
    const title = markdownTitle(markdown, titleFromSlug(path.basename(relativePath)));
    const headings = markdownHeadings(markdown);
    const excerpt = markdownExcerpt(markdown);
    const bank = inferBankFromRelativePath(relativePath);
    const topics = classifyNote(relativePath, title, markdown);
    pathEntryIds.set(relativePath, id);

    const entry = {
      id,
      title,
      kind: "note",
      summary: firstParagraph(markdown),
      maturity: "evidence-note",
      aliases: [relativePath, path.basename(relativePath), title],
      banks: bank ? [bank] : [],
      noteRefs: [noteRef(relativePath, relativePath)],
      related: unique([...(bank ? [`bank-${bank.toLowerCase()}`] : ["overview"]), ...topics]),
      showInToc: false,
      body: [
        "This is an evidence note entry. The encyclopedia should cite it, but curated chapter pages should carry the distilled explanation.",
        "",
        "## Source Note",
        `\`${relativePath}\``,
        "",
        "## Summary",
        firstParagraph(markdown),
        "",
        topics.length ? "## Topic Links" : "",
        topics.map((topicId) => {
          const topic = topicConfigs.find((candidate) => candidate.id === topicId);
          return topic ? `- [[${topic.id}|${topic.title}]]` : "";
        }).filter(Boolean).join("\n"),
        "",
        headings.length ? "## Headings" : "",
        headings.map((heading) => `- ${heading}`).join("\n"),
        "",
        "## Note Content",
        excerpt.note,
        "",
        excerpt.markdown
      ].filter(Boolean).join("\n")
    };
    noteEntries.push({
      id,
      title,
      summary: entry.summary,
      relativePath,
      headings,
      bank,
      topics,
      topicScores: Object.fromEntries(topics.map((topicId) => {
        const topic = topicConfigs.find((candidate) => candidate.id === topicId);
        return [topicId, topic ? noteTopicScore(topic, relativePath, title, markdown) : 0];
      })),
      length: markdown.length
    });
    addEntry(entry);
  }
}

function addTopicEntries() {
  const matchedByTopic = new Map(topicConfigs.map((topic) => [topic.id, []]));
  for (const note of noteEntries) {
    for (const topicId of note.topics) {
      matchedByTopic.get(topicId)?.push(note);
    }
  }
  for (const [topicId, notes] of matchedByTopic.entries()) {
    notes.sort((a, b) => {
      const scoreDelta = (b.topicScores?.[topicId] || 0) - (a.topicScores?.[topicId] || 0);
      return scoreDelta || a.title.localeCompare(b.title);
    });
  }

  addEntry({
    id: "topic-index",
    title: "Topic Index",
    kind: "topic",
    summary: "Generated topical map that groups evidence notes into practical encyclopedia chapters.",
    aliases: ["topics", "chapters", "knowledge areas", "distilled notes"],
    related: topicConfigs.map((topic) => topic.id),
    showInToc: true,
    body: [
      "The topic index is generated from note filenames, headings, summaries, and early body text. It is meant to bridge the raw evidence-note archive and the curated chapter pages.",
      "",
      "## Topics",
      topicConfigs.map((topic) => {
        const count = matchedByTopic.get(topic.id)?.length || 0;
        return `- [[${topic.id}|${topic.title}]] - ${count} evidence notes`;
      }).join("\n")
    ].join("\n")
  });

  for (const topic of topicConfigs) {
    const notes = matchedByTopic.get(topic.id) || [];
    const bankCounts = new Map();
    for (const note of notes) {
      if (note.bank) {
        bankCounts.set(note.bank, (bankCounts.get(note.bank) || 0) + 1);
      }
    }
    const evidenceLinks = notes.slice(0, 80).map((note) => {
      const bank = note.bank ? `Bank ${note.bank}; ` : "";
      return `- [[${note.id}|${note.title}]] - ${bank}${note.summary}`;
    });

    addEntry({
      id: topic.id,
      title: topic.title,
      kind: "topic",
      summary: topic.summary,
      maturity: "generated-summary",
      aliases: topic.aliases,
      banks: topic.banks,
      noteRefs: notes.map((note) => noteRef(note.relativePath, note.title)),
      related: unique([
        "topic-index",
        "source-browser",
        ...topic.related,
        ...topic.banks.map((bank) => `bank-${bank.toLowerCase()}`),
        ...(buildMode === "local" ? topic.banks.map((bank) => sourceBankIndexId(bank)) : [])
      ]),
      showInToc: true,
      body: [
        topic.summary,
        "",
        "## Reading Use",
        "Use this page as a practical entry point when a raw note title is too narrow. The evidence list below points back to the original notes, while related links point into curated system pages, bank pages, and generated indexes.",
        "",
        topic.banks.length ? "## Primary Banks" : "",
        topic.banks.map((bank) => `- [[bank-${bank.toLowerCase()}|Bank ${bank}]]`).join("\n"),
        "",
        bankCounts.size ? "## Evidence By Bank" : "",
        [...bankCounts.entries()].sort((a, b) => a[0].localeCompare(b[0])).map(([bank, count]) => `- [[bank-${bank.toLowerCase()}|Bank ${bank}]]: ${count} notes`).join("\n"),
        "",
        "## Evidence Notes",
        evidenceLinks.join("\n") || "No notes were classified into this topic yet.",
        notes.length > evidenceLinks.length ? `- ${notes.length - evidenceLinks.length} more evidence notes omitted from this compact topic page; use search for exact titles or filenames.` : ""
      ].filter(Boolean).join("\n")
    });
  }
}

function parseSourceModule(filePath) {
  const relativePath = repoRelative(filePath);
  const text = fs.readFileSync(filePath, "utf8");
  const fileName = path.basename(filePath);
  const bank = inferBankFromRelativePath(relativePath);
  const labels = [...text.matchAll(/^([A-Za-z0-9_]+):/gm)].map((match) => match[1]);
  const primaryLabel = labels.find((label) => !/_L[0-9A-F]{4}$/i.test(label)) || labels[0] || "";
  const address = addressFromLabel(primaryLabel) || addressFromFileName(fileName);
  const sourceUnits = [...text.matchAll(/; - ([C-E][0-9A-F]:[0-9A-F]{4}\.\.[C-E][0-9A-F]:[0-9A-F]{4})\s+(.+)/g)]
    .map((match) => ({ range: match[1], name: match[2].trim() }));
  const title = sourceUnits[0]?.name || titleFromSlug(fileName.replace(/^[c-e][0-9a-f]_[0-9a-f]{4}(?:_[0-9a-f]{4})?_?/i, ""));
  const externalContracts = [...text.matchAll(/^([A-Za-z0-9_]+)\s*=\s*\$([A-F0-9]{6})/gmi)]
    .map((match) => `${match[1]} = $${match[2].toUpperCase()}`)
    .slice(0, 12);

  return {
    relativePath,
    fileName,
    bank,
    labels,
    primaryLabel,
    address,
    sourceUnits,
    title,
    externalContracts,
    callTargets: asmCallTargets(text),
    size: text.length,
    sourceEmbed: sourceEmbed(text)
  };
}

function addSourceModuleEntries() {
  const sourceHeavyBanks = new Set(["c0", "c1", "c2", "c4", "ef"]);
  const sourceFiles = walkFiles(srcDir, (filePath) => {
    if (!filePath.endsWith(".asm")) {
      return false;
    }
    const relativePath = repoRelative(filePath);
    const parts = relativePath.split("/");
    return sourceHeavyBanks.has(parts[1]) && !path.basename(filePath).startsWith("bank_");
  }).sort((a, b) => repoRelative(a).localeCompare(repoRelative(b)));

  const modules = sourceFiles.map((filePath) => {
    const module = parseSourceModule(filePath);
    module.id = entryIdForPath("source", module.relativePath);
    module.symbolId = module.primaryLabel ? labelEntryId(module.primaryLabel) : "";
    return module;
  });
  const labelToModule = new Map();
  const primarySymbols = [];

  for (const module of modules) {
    for (const label of module.labels) {
      labelToModule.set(label, module);
    }
    if (module.primaryLabel) {
      primarySymbols.push(module);
    }
  }

  const incomingByModule = new Map();
  for (const module of modules) {
    for (const target of module.callTargets) {
      const targetModule = labelToModule.get(target);
      if (!targetModule || targetModule.id === module.id) {
        continue;
      }
      incomingByModule.set(targetModule.id, unique([...(incomingByModule.get(targetModule.id) || []), module.id]));
    }
  }

  const byBank = new Map();
  for (const module of modules) {
    const id = entryIdForPath("source", module.relativePath);
    pathEntryIds.set(module.relativePath, id);
    if (module.bank) {
      byBank.set(module.bank, [...(byBank.get(module.bank) || []), module]);
    }
    const linkedTargets = module.callTargets
      .map((target) => ({ target, module: labelToModule.get(target) }))
      .filter((item) => item.module && item.module.id !== id);
    const unresolvedTargets = module.callTargets
      .filter((target) => !labelToModule.has(target))
      .slice(0, 18);
    const incoming = incomingByModule.get(id) || [];

    addEntry({
      id,
      title: module.title,
      kind: "routine",
      summary: module.address
        ? `${module.bank} source module at ${module.address}.`
        : `${module.bank || "Source"} module from the checked-in scaffold.`,
      maturity: "generated-source",
      aliases: [
        module.relativePath,
        module.fileName,
        module.primaryLabel,
        ...module.labels.slice(0, 10)
      ].filter(Boolean),
      addresses: [
        module.address,
        ...module.sourceUnits.map((unit) => unit.range)
      ].filter(Boolean),
      banks: module.bank ? [module.bank] : [],
      sourceRefs: [sourceRef(module.relativePath, module.relativePath)],
      related: unique([
        module.symbolId,
        module.bank ? `bank-${module.bank.toLowerCase()}` : "",
        module.bank ? `routine-index-${module.bank.toLowerCase()}` : "",
        "source-tree",
        ...linkedTargets.slice(0, 10).map((item) => item.module.id),
        ...incoming.slice(0, 10)
      ]),
      showInToc: false,
      body: [
        module.address ? `Primary address: \`${module.address}\`.` : "No primary address was inferred from the filename or label.",
        "",
        "## Source File",
        `\`${module.relativePath}\``,
        "",
        module.sourceUnits.length ? "## Source Units" : "",
        module.sourceUnits.map((unit) => `- \`${unit.range}\` ${unit.name}`).join("\n"),
        "",
        module.primaryLabel ? "## Primary Label" : "",
        module.primaryLabel ? `\`${module.primaryLabel}\`` : "",
        "",
        module.externalContracts.length ? "## External Contracts" : "",
        module.externalContracts.map((contract) => `- \`${contract}\``).join("\n"),
        "",
        linkedTargets.length ? "## Linked Calls And Branch Targets" : "",
        linkedTargets.slice(0, 24).map((item) => `- [[${item.module.id}|${item.target}]]`).join("\n"),
        linkedTargets.length > 24 ? `- ${linkedTargets.length - 24} more linked targets omitted from this compact list; use search for the exact label.` : "",
        "",
        unresolvedTargets.length ? "## External Or Unindexed Targets" : "",
        unresolvedTargets.map((target) => `- \`${target}\``).join("\n"),
        "",
        incoming.length ? "## Referenced By" : "",
        incoming.slice(0, 18).map((callerId) => `- [[${callerId}|${entries.find((entry) => entry.id === callerId)?.title || callerId}]]`).join("\n"),
        incoming.length > 18 ? `- ${incoming.length - 18} more incoming references omitted from this compact list.` : "",
        "",
        "## Source Code",
        module.sourceEmbed.note,
        "",
        fencedCode("asm", module.sourceEmbed.code)
      ].filter(Boolean).join("\n")
    });
  }

  const counts = [...byBank.entries()]
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([bank, modules]) => `- [[routine-index-${bank.toLowerCase()}|Bank ${bank} routines]]: ${modules.length} source-module entries`);

  for (const [bank, bankModules] of [...byBank.entries()].sort((a, b) => a[0].localeCompare(b[0]))) {
    const bankLower = bank.toLowerCase();
    addEntry({
      id: `routine-index-${bankLower}`,
      title: `Bank ${bank} Routine Index`,
      kind: "source",
      summary: `Generated index of ${bankModules.length} source-heavy routine modules in Bank ${bank}.`,
      aliases: [`bank ${bank} routines`, `${bank} source modules`, `${bank} labels`],
      banks: [bank],
      related: [`bank-${bankLower}`, "routine-index", "source-tree"],
      showInToc: false,
      body: [
        `Bank \`${bank}\` has ${bankModules.length} generated source-module entries in this index.`,
        "",
        "## Modules",
        bankModules
          .sort((a, b) => (a.address || "").localeCompare(b.address || "") || a.title.localeCompare(b.title))
          .map((module) => `- [[${module.id}|${module.address || module.fileName} ${module.title}]]${module.primaryLabel ? ` ([[${module.symbolId}|${module.primaryLabel}]])` : ""}`)
          .join("\n")
      ].join("\n")
    });
  }

  for (const module of primarySymbols) {
    addEntry({
      id: module.symbolId,
      title: module.primaryLabel,
      kind: "symbol",
      summary: module.address
        ? `${module.bank} primary source symbol at ${module.address}.`
        : `Primary source symbol for ${module.fileName}.`,
      maturity: "generated-source",
      aliases: [module.primaryLabel, module.title, module.fileName, module.relativePath],
      addresses: module.address ? [module.address] : [],
      banks: module.bank ? [module.bank] : [],
      sourceRefs: [sourceRef(module.relativePath, module.relativePath)],
      related: unique([
        module.id,
        module.bank ? `bank-${module.bank.toLowerCase()}` : "",
        module.bank ? `routine-index-${module.bank.toLowerCase()}` : "",
        "routine-index"
      ]),
      showInToc: false,
      body: [
        `\`${module.primaryLabel}\` is the primary exported label for [[${module.id}|${module.title}]].`,
        "",
        module.address ? "## Address" : "",
        module.address ? `\`${module.address}\`` : "",
        "",
        "## Source Module",
        `[[${module.id}|${module.relativePath}]]`,
        "",
        module.sourceUnits.length ? "## Source Units" : "",
        module.sourceUnits.map((unit) => `- \`${unit.range}\` ${unit.name}`).join("\n"),
        "",
        module.callTargets.length ? "## Direct Targets Mentioned" : "",
        module.callTargets.slice(0, 24).map((target) => {
          const targetModule = labelToModule.get(target);
          return targetModule ? `- [[${targetModule.id}|${target}]]` : `- \`${target}\``;
        }).join("\n")
      ].filter(Boolean).join("\n")
    });
  }

  addEntry({
    id: "routine-index",
    title: "Routine Index",
    kind: "source",
    summary: `Generated search index for ${modules.length} source-heavy routine modules and ${primarySymbols.length} primary symbols.`,
    aliases: ["routine index", "source modules", "labels", "symbol index"],
    related: ["source-tree", "runtime-systems"],
    showInToc: true,
    body: [
      "Generated routine entries cover the small source modules in the audited source-heavy banks. They are primarily search targets and evidence pages.",
      "",
      "Each indexed module also gets a primary symbol page, so named routines can be linked directly while branch-local labels remain inside their containing source entry.",
      "",
      "## Indexed Banks",
      counts.join("\n")
    ].join("\n")
  });
}

function sourceBankIndexId(bank) {
  return `source-bank-${bank.toLowerCase()}`;
}

function addAuthoredLocalWorkspacePlaceholders() {
  const placeholderBody = [
    "This release-baseline entry is a placeholder for local generated workspace content.",
    "",
    "The packaged encyclopedia does not distribute generated byte-equivalent source, raw extracted assets, preview sheets, renderer fixtures, or ROM-derived media. Those artifacts should be generated under the user's local app-data workspace after ROM verification.",
    "",
    "Open [[release-artifact-policy|Release Artifact Policy]] for the distribution boundary."
  ].join("\n");

  addEntry({
    id: "source-browser",
    title: "Generated Source Workspace",
    kind: "workflow",
    summary: "Local workspace placeholder for source generated after ROM verification.",
    aliases: ["source browser", "asm browser", "local source"],
    related: ["local-workspace", "asset-library", "release-artifact-policy"],
    provenance: "project-authored",
    body: placeholderBody
  });

  addEntry({
    id: "routine-index",
    title: "Generated Routine Index",
    kind: "workflow",
    summary: "Local workspace placeholder for routine and symbol indexes generated after ROM verification.",
    aliases: ["routine index", "symbol index", "local routines"],
    related: ["local-workspace", "asset-library", "release-artifact-policy"],
    provenance: "project-authored",
    body: placeholderBody
  });

  addEntry({
    id: "asset-manifest-index",
    title: "Asset Manifest Index",
    kind: "asset-contract",
    summary: "Local asset manifest placeholder for ROM-derived asset inventories and previews.",
    aliases: ["asset manifest index", "local asset manifests", "asset inventory"],
    related: ["asset-contracts", "release-artifact-policy"],
    provenance: "project-authored",
    body: placeholderBody
  });

  const banks = new Set([
    ...topicConfigs.flatMap((topic) => topic.banks || []),
    ...(narrativeChapterConfig.chapters || []).flatMap((chapter) => chapter.banks || [])
  ]);
  for (const bank of [...banks].filter((value) => /^[C-E][0-9A-F]$/.test(value)).sort()) {
    addEntry({
      id: sourceBankIndexId(bank),
      title: `Bank ${bank} Generated Source Workspace`,
      kind: "workflow",
      summary: `Local workspace placeholder for Bank ${bank} source generated after ROM verification.`,
      aliases: [`bank ${bank} source`, `${bank} asm files`, `${bank} source files`],
      banks: [bank],
      related: [`bank-${bank.toLowerCase()}`, "source-browser", "source-tree", "release-artifact-policy", "local-workspace"],
      showInToc: false,
      provenance: "project-authored",
      body: placeholderBody
    });
  }
}

function countEntriesBy(field) {
  return entries.reduce((counts, entry) => {
    const key = entry[field] || "unlabeled";
    counts[key] = (counts[key] || 0) + 1;
    return counts;
  }, {});
}

function countRows(counts, labelMap = {}) {
  return Object.entries(counts)
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .map(([key, count]) => `- ${labelMap[key] || key}: ${count.toLocaleString("en-US")}`)
    .join("\n");
}

function scrubReleaseString(value) {
  if (buildMode !== "authored") {
    return value;
  }
  return String(value)
    .replace(/\/[A-Za-z]:\/[^)\s"`']*\/(notes|refs|src|tools|asset-manifests)\//g, "$1/")
    .replace(/[A-Za-z]:\\[^`"\n\r]*/g, "[local workspace path]")
    .replace(/\/[A-Za-z]:\/[^)\s"`']*/g, "[local workspace path]");
}

function scrubReleaseValue(value) {
  if (typeof value === "string") {
    return scrubReleaseString(value);
  }
  if (Array.isArray(value)) {
    return value.map((item) => scrubReleaseValue(item));
  }
  if (value && typeof value === "object") {
    return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, scrubReleaseValue(item)]));
  }
  return value;
}

function scrubEntriesForAuthoredRelease() {
  if (buildMode !== "authored") {
    return;
  }
  for (let index = 0; index < entries.length; index += 1) {
    entries[index] = scrubReleaseValue(entries[index]);
  }
}

function addCatalogBuildStatusEntry() {
  const provenanceCounts = countEntriesBy("provenance");
  const kindCounts = countEntriesBy("kind");
  const generatedLocalCount = provenanceCounts["generated-local"] || 0;
  const romDerivedCount = provenanceCounts["rom-derived-local"] || 0;
  const authoredMode = buildMode === "authored";

  addEntry({
    id: "catalog-build-status",
    title: "Catalog Build Status",
    kind: "workflow",
    summary: `This catalog was built in ${buildMode} mode with ${entries.length.toLocaleString("en-US")} entries before status finalization.`,
    aliases: ["build mode", "catalog status", "provenance status", "entry counts"],
    related: ["overview", "release-artifact-policy", "rom-status", "upstream-status"],
    provenance: "project-authored",
    body: [
      "This page summarizes the generated encyclopedia catalog itself: build mode, provenance labels, and whether local workspace content is present.",
      "",
      "## Build Mode",
      `- Mode: \`${buildMode}\``,
      authoredMode
        ? "- Release baseline: source, routine, symbol, asset, and asset-manifest entries are omitted; local-workspace placeholders point to post-ROM generation."
        : "- Local workspace catalog: generated source, routine, symbol, asset, and asset-manifest entries are included.",
      "",
      "## Provenance Counts",
      countRows(provenanceCounts, Object.fromEntries(Object.entries(provenanceCatalog).map(([key, value]) => [key, value.label]))),
      "",
      "## Entry Kind Counts",
      countRows(kindCounts),
      "",
      "## Release Readiness Signals",
      authoredMode ? "- Authored mode is enabled." : "- Local mode is enabled; run `npm run prepare:release` before packaging.",
      generatedLocalCount ? `- Generated-local entries present: ${generatedLocalCount.toLocaleString("en-US")}.` : "- No generated-local entries are present.",
      romDerivedCount ? `- ROM-derived local entries present: ${romDerivedCount.toLocaleString("en-US")}.` : "- No ROM-derived local entries are present.",
      "",
      "## Related",
      "- [[release-artifact-policy|Release Artifact Policy]]",
      "- [[rom-status|ROM And Generated Content Status]]",
      "- [[upstream-status|Upstream Source Status]]"
    ].join("\n")
  });
}

function sourceFileKind(relativePath) {
  const fileName = path.basename(relativePath);
  if (fileName.startsWith("bank_")) {
    return "bank scaffold";
  }
  if (/asset|tile|sprite|palette|map|music|sound|text|data|table|pointer/i.test(relativePath)) {
    return "data/source scaffold";
  }
  return "source scaffold";
}

function parseSourceFile(filePath) {
  const relativePath = repoRelative(filePath);
  const text = fs.readFileSync(filePath, "utf8");
  const fileName = path.basename(filePath);
  const bank = inferBankFromRelativePath(relativePath);
  const labels = [...text.matchAll(/^([A-Za-z0-9_]+):/gm)].map((match) => match[1]);
  const address = addressFromLabel(labels[0] || "") || addressFromFileName(fileName);
  const sourceUnits = [...text.matchAll(/; - ([C-E][0-9A-F]:[0-9A-F]{4}\.\.[C-E][0-9A-F]:[0-9A-F]{4})\s+(.+)/g)]
    .map((match) => ({ range: match[1], name: match[2].trim() }));
  const title = sourceUnits[0]?.name || titleFromSlug(fileName.replace(/\.asm$/i, ""));
  return {
    relativePath,
    fileName,
    bank,
    labels,
    address,
    sourceUnits,
    title,
    size: text.length,
    lineCount: lines(text).length,
    kindLabel: sourceFileKind(relativePath),
    sourceEmbed: sourceEmbed(text)
  };
}

function addSourceFileEntries() {
  const sourceFiles = walkFiles(srcDir, (filePath) => filePath.endsWith(".asm"))
    .sort((a, b) => repoRelative(a).localeCompare(repoRelative(b)));
  const files = sourceFiles.map((filePath) => {
    const file = parseSourceFile(filePath);
    file.entryId = pathEntryIds.get(file.relativePath) || entryIdForPath("source-file", file.relativePath);
    file.hasRoutineEntry = pathEntryIds.has(file.relativePath);
    return file;
  });

  const byBank = new Map();
  for (const file of files) {
    if (file.bank) {
      byBank.set(file.bank, [...(byBank.get(file.bank) || []), file]);
    }
    if (file.hasRoutineEntry) {
      continue;
    }
    pathEntryIds.set(file.relativePath, file.entryId);
    addEntry({
      id: file.entryId,
      title: file.title,
      kind: "source-file",
      summary: `${file.bank || "Source"} ${file.kindLabel} file with ${file.lineCount.toLocaleString("en-US")} lines.`,
      maturity: "generated-source",
      aliases: [
        file.relativePath,
        file.fileName,
        file.title,
        ...file.labels.slice(0, 8)
      ].filter(Boolean),
      addresses: [
        file.address,
        ...file.sourceUnits.map((unit) => unit.range)
      ].filter(Boolean),
      banks: file.bank ? [file.bank] : [],
      sourceRefs: [sourceRef(file.relativePath, file.relativePath)],
      related: unique([
        file.bank ? `bank-${file.bank.toLowerCase()}` : "",
        file.bank ? sourceBankIndexId(file.bank) : "",
        "source-browser",
        "source-tree"
      ]),
      showInToc: false,
      body: [
        `Source path: \`${file.relativePath}\`.`,
        "",
        "## File Role",
        `${file.kindLabel}.`,
        "",
        file.address ? "## First Address" : "",
        file.address ? `\`${file.address}\`` : "",
        "",
        file.sourceUnits.length ? "## Source Units" : "",
        file.sourceUnits.slice(0, 24).map((unit) => `- \`${unit.range}\` ${unit.name}`).join("\n"),
        file.sourceUnits.length > 24 ? `- ${file.sourceUnits.length - 24} more source-unit comments omitted from this compact list.` : "",
        "",
        file.labels.length ? "## Labels" : "",
        file.labels.slice(0, 40).map((label) => `- \`${label}\``).join("\n"),
        file.labels.length > 40 ? `- ${file.labels.length - 40} more labels omitted from this compact list.` : "",
        "",
        "## Source Code",
        file.sourceEmbed.note,
        "",
        fencedCode("asm", file.sourceEmbed.code)
      ].filter(Boolean).join("\n")
    });
  }

  const bankRows = [...byBank.entries()]
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([bank, bankFiles]) => {
      const routineCount = bankFiles.filter((file) => file.hasRoutineEntry).length;
      const scaffoldCount = bankFiles.length - routineCount;
      return `- [[${sourceBankIndexId(bank)}|Bank ${bank} source]]: ${bankFiles.length} files (${routineCount} routine pages, ${scaffoldCount} scaffold/data files)`;
    });

  for (const [bank, bankFiles] of [...byBank.entries()].sort((a, b) => a[0].localeCompare(b[0]))) {
    const bankLower = bank.toLowerCase();
    const routineCount = bankFiles.filter((file) => file.hasRoutineEntry).length;
    const scaffoldCount = bankFiles.length - routineCount;
    const sortedFiles = bankFiles.sort((a, b) => (a.address || "").localeCompare(b.address || "") || a.relativePath.localeCompare(b.relativePath));
    addEntry({
      id: sourceBankIndexId(bank),
      title: `Bank ${bank} Source Files`,
      kind: "source",
      summary: `Generated source browser for ${bankFiles.length} checked-in Bank ${bank} .asm files.`,
      aliases: [`bank ${bank} source`, `${bank} asm files`, `${bank} source files`, `src/${bankLower}`],
      banks: [bank],
      related: unique([
        `bank-${bankLower}`,
        "source-browser",
        "source-tree",
        entryIds.has(`routine-index-${bankLower}`) ? `routine-index-${bankLower}` : "",
        "routine-index"
      ]),
      showInToc: false,
      body: [
        `Bank \`${bank}\` has ${bankFiles.length} checked-in source files in \`src/${bankLower}\`.`,
        "",
        "## Coverage",
        `- Routine/source-heavy entries: ${routineCount}`,
        `- Scaffold/data source entries: ${scaffoldCount}`,
        "",
        "## Files",
        sortedFiles.map((file) => {
          const marker = file.hasRoutineEntry ? "routine" : file.kindLabel;
          const label = [file.address, file.title].filter(Boolean).join(" ");
          return `- [[${file.entryId}|${label || file.fileName}]] - ${marker}; \`${file.relativePath}\``;
        }).join("\n")
      ].join("\n")
    });
  }

  addEntry({
    id: "source-browser",
    title: "Source Browser",
    kind: "source",
    summary: `Generated browser for all ${files.length} checked-in source .asm files across ${byBank.size} banks.`,
    aliases: ["all source", "source browser", "asm browser", "checked-in source", "source code"],
    related: ["source-tree", "routine-index", "bank-map", ...[...byBank.keys()].map((bank) => sourceBankIndexId(bank))],
    showInToc: true,
    body: [
      "This page indexes every checked-in `.asm` source file from the configured decomp source root.",
      "",
      "Routine entries remain the richer semantic source pages for audited source-heavy banks. Source-file entries cover the broader scaffold and data-heavy banks so the encyclopedia can still open actual checked-in code from any bank.",
      "",
      "## Banks",
      bankRows.join("\n")
    ].join("\n")
  });
}

function addAssetManifestEntries() {
  if (!fs.existsSync(assetManifestDir)) {
    return;
  }

  const manifestFiles = fs.readdirSync(assetManifestDir)
    .filter((name) => name.endsWith(".json"))
    .sort();
  const manifestLinks = [];
  let assetCount = 0;

  for (const manifestName of manifestFiles) {
    const relativePath = `asset-manifests/${manifestName}`;
    const manifest = JSON.parse(read(relativePath));
    const bank = inferBankFromRelativePath(relativePath) || (manifestName.match(/bank-([c-e][0-9a-f])/i)?.[1] || "").toUpperCase();
    const id = entryIdForPath("asset-manifest", relativePath);
    const assets = Array.isArray(manifest.assets) ? manifest.assets : [];
    const summary = manifest.bank_summary
      ? Object.entries(manifest.bank_summary).slice(0, 5).map(([key, value]) => `${key}: ${value}`).join(", ")
      : `${assets.length} assets`;
    pathEntryIds.set(relativePath, id);
    manifestLinks.push(`- [[${id}|${manifest.title || manifestName}]] - ${summary}`);

    addEntry({
      id,
      title: manifest.title || titleFromSlug(manifestName),
      kind: "asset-manifest",
      summary: truncate(summary, 200),
      maturity: "generated-summary",
      aliases: [manifestName, relativePath, manifest.title || ""].filter(Boolean),
      banks: bank ? [bank] : [],
      sourceRefs: [sourceRef(relativePath, relativePath)],
      noteRefs: (manifest.references || [])
        .filter((ref) => ref.startsWith("notes/") && exists(ref))
        .map((ref) => noteRef(ref, ref)),
      related: bank ? [`bank-${bank.toLowerCase()}`, "asset-contracts"] : ["asset-contracts"],
      showInToc: false,
      body: [
        `Manifest file: \`${relativePath}\`.`,
        "",
        "## Summary",
        manifest.bank_summary
          ? Object.entries(manifest.bank_summary).map(([key, value]) => `- \`${key}\`: ${value}`).join("\n")
          : `- Assets: ${assets.length}`,
        "",
        assets.length ? "## Assets" : "",
        assets.slice(0, 80).map((asset) => `- [[asset-${slug(asset.id || asset.title)}|${asset.title || asset.id}]]`).join("\n"),
        assets.length > 80 ? `- ${assets.length - 80} more assets omitted from this compact manifest page; use search for exact asset IDs.` : ""
      ].filter(Boolean).join("\n")
    });

    for (const asset of assets) {
      assetCount += 1;
      const assetId = `asset-${slug(asset.id || `${manifestName}-${asset.title}`)}`;
      const range = asset.source?.range || "";
      const assetBank = range.match(/^([C-E][0-9A-F]):/i)?.[1].toUpperCase() || bank;
      addEntry({
        id: assetId,
        title: asset.title || asset.id || "Asset",
        kind: "asset",
        summary: `${asset.category || "asset"}${range ? ` at ${range}` : ""}.`,
        maturity: "generated-asset",
        aliases: [
          asset.id,
          asset.title,
          asset.category,
          range,
          ...(asset.outputs || []).map((output) => output.path)
        ].filter(Boolean),
        addresses: range ? [range] : [],
        banks: assetBank ? [assetBank] : [],
        sourceRefs: [sourceRef(relativePath, manifestName)],
        related: [id, "asset-contracts", ...(assetBank ? [`bank-${assetBank.toLowerCase()}`] : [])],
        showInToc: false,
        body: [
          `Category: \`${asset.category || "unknown"}\`.`,
          "",
          range ? "## Source Range" : "",
          range ? `\`${range}\`, ${asset.source?.bytes ?? "unknown"} bytes.` : "",
          "",
          asset.outputs?.length ? "## Outputs" : "",
          (asset.outputs || []).map((output) => `- \`${output.kind}\`: \`${output.path}\``).join("\n"),
          "",
          asset.notes?.length ? "## Notes" : "",
          (asset.notes || []).map((note) => `- ${note}`).join("\n")
        ].filter(Boolean).join("\n")
      });
    }
  }

  addEntry({
    id: "asset-manifest-index",
    title: "Asset Manifest Index",
    kind: "asset-contract",
    summary: `Generated index of ${manifestFiles.length} asset manifests and ${assetCount} asset entries.`,
    aliases: ["asset manifest index", "asset extraction manifests"],
    related: ["asset-contracts"],
    body: [
      "Asset manifests provide the current source-backed inventory for extractable graphics, map, text, table, debug, and audio payloads.",
      "",
      "## Manifests",
      manifestLinks.join("\n")
    ].join("\n")
  });
}

addEvidenceNoteEntries();
addTopicEntries();
if (buildMode === "local") {
  addSourceModuleEntries();
  addSourceFileEntries();
  addAssetManifestEntries();
} else {
  addAuthoredLocalWorkspacePlaceholders();
}

for (const entry of entries) {
  if (entry.kind === "bank" && entry.banks?.[0]) {
    const bank = entry.banks[0];
    const routineIndexId = `routine-index-${bank.toLowerCase()}`;
    const sourceIndexId = sourceBankIndexId(bank);
    const topicIds = topicConfigs
      .filter((topic) => topic.banks.includes(bank))
      .map((topic) => topic.id);
    if (entryIds.has(sourceIndexId)) {
      entry.related = unique([...(entry.related || []), sourceIndexId, "source-browser", "source-tree"]);
      entry.body = [
        entry.body,
        "",
        "## Source Browser",
        buildMode === "local"
          ? `Open [[${sourceIndexId}|Bank ${bank} Source Files]] for every checked-in \`src/${bank.toLowerCase()}\` source file, including scaffold/data files and routine entries.`
          : `Open [[${sourceIndexId}|Bank ${bank} Source Files]] for the local-workspace placeholder. Generated source files are not distributed in the authored release baseline.`
      ].join("\n");
    }
    if (entryIds.has(routineIndexId)) {
      entry.related = unique([...(entry.related || []), routineIndexId, "routine-index"]);
      entry.body = [
        entry.body,
        "",
        "## Source Module Index",
        `Open [[${routineIndexId}|Bank ${entry.banks[0]} Routine Index]] for source-heavy routine pages and primary symbols in this bank.`
      ].join("\n");
    }
    if (topicIds.length) {
      entry.related = unique([...(entry.related || []), ...topicIds]);
      entry.body = [
        entry.body,
        "",
        "## Related Topics",
        topicIds.map((topicId) => {
          const topic = topicConfigs.find((candidate) => candidate.id === topicId);
          return topic ? `- [[${topic.id}|${topic.title}]]` : "";
        }).filter(Boolean).join("\n")
      ].join("\n");
    }
  }
}

const narrativeChapters = narrativeChapterConfig.chapters || [];
const narrativeIds = new Set(narrativeChapters.map((chapter) => chapter.id));
for (const entry of entries) {
  if (entry.kind === "topic") {
    const matchedChapters = narrativeChapters
      .filter((chapter) => (chapter.related || []).includes(entry.id))
      .map((chapter) => chapter.id);
    if (matchedChapters.length) {
      entry.related = unique([...(entry.related || []), ...matchedChapters]);
      entry.body = [
        entry.body,
        "",
        "## Narrative Chapters",
        matchedChapters.map((id) => {
          const chapter = narrativeChapters.find((candidate) => candidate.id === id);
          return chapter ? `- [[${id}|${chapter.title}]]` : "";
        }).filter(Boolean).join("\n")
      ].join("\n");
    }
  }
  if (entry.kind === "note") {
    const relatedNarratives = (entry.related || []).filter((id) => narrativeIds.has(id));
    if (relatedNarratives.length) {
      entry.body = [
        entry.body,
        "",
        "## Narrative Chapter Links",
        relatedNarratives.map((id) => {
          const chapter = narrativeChapters.find((candidate) => candidate.id === id);
          return chapter ? `- [[${id}|${chapter.title}]]` : "";
        }).filter(Boolean).join("\n")
      ].join("\n");
    }
  }
}

addLearningPathEntries();
addCatalogBuildStatusEntry();

for (const entry of entries) {
  for (const ref of [...(entry.sourceRefs || []), ...(entry.noteRefs || [])]) {
    const normalizedPath = ref.path?.replaceAll("\\", "/");
    if (normalizedPath && pathEntryIds.has(normalizedPath)) {
      ref.entryId = pathEntryIds.get(normalizedPath);
    }
  }
}

scrubEntriesForAuthoredRelease();

entries.sort((a, b) => {
  const order = {
    chapter: 0,
    "learning-path": 1,
    workflow: 2,
    narrative: 3,
    bank: 4,
    topic: 5,
    "script-vm": 6,
    "text-command": 7,
    "asset-contract": 8,
    "asset-manifest": 9,
    asset: 10,
    source: 11,
    "source-file": 12,
    symbol: 13,
    routine: 14,
    tool: 15,
    note: 16,
    search: 17
  };
  return (order[a.kind] ?? 99) - (order[b.kind] ?? 99) || a.title.localeCompare(b.title);
});

const relationshipGraph = buildRelationshipGraph();
const deferredBodyStats = deferHeavyBodies();

const catalog = {
  generatedAt: new Date().toISOString(),
  buildMode,
  provenanceCatalog,
  chapterScopeCatalog,
  localWorkspaceContract,
  artifactPolicy: {
    checkedIn: [
      "encyclopedia shell",
      "curated docs",
      "schemas and tools",
      "public payload-free manifests",
      "validation logic",
      "source-generation code"
    ],
    userProvided: ["ROM file", "optional local decomp/source workspace"],
    generatedLocally: ["src", "asset-manifests", "renderer fixtures", "source snapshots", "search catalog", "extracted references", "preview sheets", "SPC/WAV exports", "cache files"],
    neverDistributed: ["ROM bytes", "raw extracted copyrighted assets", "ROM-derived audio/images", "generated byte-equivalent source"]
  },
  repoRoot: catalogSourceRoot,
  sourceRoot: catalogSourceRoot,
  upstream: {
    sourceRoot: catalogSourceRoot,
    git: upstreamSnapshot.git,
    fileCount: upstreamSnapshot.fileCount,
    counts: upstreamSnapshot.counts,
    changesSinceLastBuild: {
      hasPreviousSnapshot: upstreamSnapshot.changesSinceLastBuild.hasPreviousSnapshot,
      total: upstreamSnapshot.changesSinceLastBuild.total,
      added: upstreamSnapshot.changesSinceLastBuild.added.length,
      modified: upstreamSnapshot.changesSinceLastBuild.modified.length,
      removed: upstreamSnapshot.changesSinceLastBuild.removed.length
    }
  },
  entryCount: entries.length,
  heavyBodyThreshold,
  deferredBodyCount: deferredBodyStats.count,
  deferredBodyChars: deferredBodyStats.deferredChars,
  relationshipGraph,
  entries
};

fs.writeFileSync(
  path.join(generatedDir, "catalog.json"),
  JSON.stringify(catalog, null, 2),
  "utf8"
);

fs.writeFileSync(
  path.join(generatedDir, "catalog.js"),
  `window.ENCYCLOPEDIA_CATALOG = ${JSON.stringify(catalog, null, 2)};\n`,
  "utf8"
);

fs.writeFileSync(
  sourceSnapshotPath,
  JSON.stringify(upstreamSnapshot, null, 2),
  "utf8"
);

console.log(`Generated ${entries.length} encyclopedia entries.`);
console.log(`Deferred ${deferredBodyStats.count} heavy bodies (${deferredBodyStats.deferredChars.toLocaleString("en-US")} markdown characters).`);
console.log(`Relationship graph: ${relationshipGraph.stats.nodeCount} nodes, ${relationshipGraph.stats.edgeCount} edges.`);
console.log(`Build mode: ${buildMode}`);
console.log(`Source root: ${sourceRoot}`);
