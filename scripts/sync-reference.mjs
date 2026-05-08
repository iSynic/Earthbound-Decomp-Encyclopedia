import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(__dirname, "..");
const defaultSourceRoot = "F:\\Earthbound Decomp - Codex";
const referenceRoot = path.join(appRoot, "reference");
const args = process.argv.slice(2);

const includeRoots = [
  "notes",
  "src",
  "manifests",
  "asset-manifests",
  "refs"
];

const includeFiles = [
  "README.md",
  "LICENSE.md",
  "THIRD_PARTY_NOTICES.md",
  ".gitattributes"
];

const disallowedExtensions = new Set([
  ".sfc",
  ".smc",
  ".fig",
  ".rom",
  ".spc",
  ".wav",
  ".brr",
  ".gfx",
  ".pal",
  ".arr",
  ".bin",
  ".lzhal",
  ".png",
  ".jpg",
  ".jpeg",
  ".gif",
  ".webp",
  ".exe",
  ".dll",
  ".bat",
  ".cmd",
  ".ps1",
  ".sh"
]);

const disallowedParts = new Set([
  ".git",
  "node_modules",
  "build",
  "baserom",
  "dumps",
  "cache",
  ".cache",
  "tmp",
  "tools",
  "preview-sheets",
  "renderer-fixtures",
  "spc",
  "wav"
]);

function optionValue(name) {
  const index = args.indexOf(name);
  return index === -1 ? null : args[index + 1] || null;
}

const sourceRoot = path.resolve(optionValue("--source-root") || process.env.EARTHBOUND_DECOMP_SOURCE_ROOT || defaultSourceRoot);

function assertInside(parent, child) {
  const relative = path.relative(parent, child);
  if (relative.startsWith("..") || path.isAbsolute(relative)) {
    throw new Error(`Refusing to write outside ${parent}: ${child}`);
  }
}

function shouldSkip(filePath, sourceBase = sourceRoot) {
  const relative = path.relative(sourceBase, filePath);
  const parts = relative.split(path.sep).map((part) => part.toLowerCase());
  if (parts.some((part) => disallowedParts.has(part))) {
    return true;
  }
  return disallowedExtensions.has(path.extname(filePath).toLowerCase());
}

function copyDirectory(sourceDir, targetDir, stats) {
  if (!fs.existsSync(sourceDir)) {
    return;
  }
  fs.mkdirSync(targetDir, { recursive: true });
  for (const entry of fs.readdirSync(sourceDir, { withFileTypes: true })) {
    const sourcePath = path.join(sourceDir, entry.name);
    const targetPath = path.join(targetDir, entry.name);
    if (shouldSkip(sourcePath, sourceRoot)) {
      stats.skipped += 1;
      continue;
    }
    if (entry.isDirectory()) {
      copyDirectory(sourcePath, targetPath, stats);
    } else if (entry.isFile()) {
      fs.mkdirSync(path.dirname(targetPath), { recursive: true });
      fs.copyFileSync(sourcePath, targetPath);
      stats.files += 1;
    }
  }
}

function countByRoot(root) {
  const counts = {};
  if (!fs.existsSync(root)) {
    return counts;
  }
  for (const item of fs.readdirSync(root, { withFileTypes: true })) {
    if (!item.isDirectory()) {
      continue;
    }
    const dir = path.join(root, item.name);
    counts[item.name] = countFiles(dir);
  }
  return counts;
}

function countFiles(root) {
  let count = 0;
  if (!fs.existsSync(root)) {
    return count;
  }
  for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
    const entryPath = path.join(root, entry.name);
    if (entry.isDirectory()) {
      count += countFiles(entryPath);
    } else if (entry.isFile()) {
      count += 1;
    }
  }
  return count;
}

function gitInfo(root) {
  try {
    const branch = execFileSync("git", ["-C", root, "rev-parse", "--abbrev-ref", "HEAD"], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim();
    const sha = execFileSync("git", ["-C", root, "rev-parse", "HEAD"], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim();
    const status = execFileSync("git", ["-C", root, "status", "--short"], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim();
    return {
      available: true,
      branch,
      sha,
      shortSha: sha.slice(0, 12),
      dirty: Boolean(status)
    };
  } catch {
    return { available: false };
  }
}

if (!fs.existsSync(sourceRoot)) {
  throw new Error(`Reference source root is missing: ${sourceRoot}`);
}

for (const required of ["notes", "src"]) {
  if (!fs.existsSync(path.join(sourceRoot, required))) {
    throw new Error(`Reference source root is missing ${required}: ${sourceRoot}`);
  }
}

assertInside(appRoot, referenceRoot);
fs.rmSync(referenceRoot, { recursive: true, force: true });
fs.mkdirSync(referenceRoot, { recursive: true });

const stats = { files: 0, skipped: 0 };
for (const rootName of includeRoots) {
  copyDirectory(path.join(sourceRoot, rootName), path.join(referenceRoot, rootName), stats);
}
for (const fileName of includeFiles) {
  const sourcePath = path.join(sourceRoot, fileName);
  if (fs.existsSync(sourcePath) && !shouldSkip(sourcePath, sourceRoot)) {
    fs.copyFileSync(sourcePath, path.join(referenceRoot, fileName));
    stats.files += 1;
  }
}

const manifest = {
  schema: "earthbound-decomp.private-reference-sync.v1",
  generatedAt: new Date().toISOString(),
  sourceRoot,
  sourceRootLabel: "F:\\Earthbound Decomp - Codex",
  sourceGit: gitInfo(sourceRoot),
  referenceRoot,
  includedRoots: includeRoots,
  excludedPolicy: "ROMs, generated binary/media payloads, preview sheets, caches, dumps, tools/, and executable tool scripts are excluded.",
  copiedFiles: stats.files,
  skippedEntries: stats.skipped,
  counts: countByRoot(referenceRoot)
};

fs.writeFileSync(path.join(referenceRoot, "reference-sync.json"), JSON.stringify(manifest, null, 2) + "\n", "utf8");
console.log(`Synced ${stats.files.toLocaleString("en-US")} private reference files into ${referenceRoot}`);
console.log(`Skipped ${stats.skipped.toLocaleString("en-US")} binary/generated entries.`);
