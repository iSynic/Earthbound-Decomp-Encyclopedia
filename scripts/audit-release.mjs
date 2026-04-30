import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(__dirname, "..");

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
  ".lzhal"
]);

const disallowedPathParts = new Set([
  "baserom",
  "roms",
  "dumps",
  "cache",
  "renderer-fixtures",
  "preview-sheets",
  "spc",
  "wav"
]);

const allowedGeneratedFiles = new Set([
  "catalog.json",
  "catalog.js",
  "source-snapshot.json"
]);

function walk(dir) {
  const results = [];
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (item.name === "node_modules" || item.name === ".git" || item.name === "dist") {
      continue;
    }
    const absolutePath = path.join(dir, item.name);
    if (item.isDirectory()) {
      results.push(...walk(absolutePath));
    } else {
      results.push(absolutePath);
    }
  }
  return results;
}

function relativeParts(filePath) {
  return path.relative(appRoot, filePath).split(path.sep).map((part) => part.toLowerCase());
}

const violations = [];

const catalogPath = path.join(appRoot, "public", "generated", "catalog.json");
if (!fs.existsSync(catalogPath)) {
  violations.push("public/generated/catalog.json is missing; run npm run build:content:authored before release audit");
} else {
  try {
    const catalogText = fs.readFileSync(catalogPath, "utf8");
    const catalog = JSON.parse(catalogText);
    if (catalog.buildMode !== "authored") {
      violations.push(`public/generated/catalog.json was built in ${JSON.stringify(catalog.buildMode)} mode; release packages must use authored mode`);
    }
    const romDerivedEntries = (catalog.entries || []).filter((entry) => entry.provenance === "rom-derived-local");
    if (romDerivedEntries.length) {
      violations.push(`catalog contains ${romDerivedEntries.length} rom-derived-local entr${romDerivedEntries.length === 1 ? "y" : "ies"}`);
    }
    const generatedLocalEntries = (catalog.entries || []).filter((entry) => entry.provenance === "generated-local");
    if (generatedLocalEntries.length) {
      violations.push(`catalog contains ${generatedLocalEntries.length} generated-local entr${generatedLocalEntries.length === 1 ? "y" : "ies"}; release catalogs must be project-authored/source-safe until a user provides a ROM`);
    }
    const localGeneratedKinds = new Set(["source", "source-file", "routine", "symbol", "asset", "asset-manifest"]);
    const localGeneratedEntries = (catalog.entries || []).filter((entry) => localGeneratedKinds.has(entry.kind));
    if (localGeneratedEntries.length) {
      violations.push(`catalog contains ${localGeneratedEntries.length} generated source/asset entr${localGeneratedEntries.length === 1 ? "y" : "ies"} that belong in local workspace mode`);
    }
    for (const field of ["repoRoot", "sourceRoot"]) {
      const value = String(catalog[field] || "");
      if (/^[A-Za-z]:[\\/]/.test(value)) {
        violations.push(`catalog field ${field} contains an absolute local path`);
      }
    }
    const absolutePathPatterns = [
      { label: "Windows absolute path", pattern: /[A-Za-z]:\\\\/ },
      { label: "file-style drive path", pattern: /\/[A-Za-z]:\// },
      { label: "encoded local drive path", pattern: /%3A%5C|%3A\//i }
    ];
    for (const { label, pattern } of absolutePathPatterns) {
      if (pattern.test(catalogText)) {
        violations.push(`catalog text contains ${label}`);
      }
    }
  } catch (error) {
    violations.push(`public/generated/catalog.json could not be parsed: ${error.message}`);
  }
}

for (const filePath of walk(appRoot)) {
  const relativePath = path.relative(appRoot, filePath).replaceAll("\\", "/");
  const ext = path.extname(filePath).toLowerCase();
  const parts = relativeParts(filePath);

  if (disallowedExtensions.has(ext)) {
    violations.push(`${relativePath} uses disallowed release extension ${ext}`);
    continue;
  }

  const disallowedPart = parts.find((part) => disallowedPathParts.has(part));
  if (disallowedPart && !allowedGeneratedFiles.has(path.basename(filePath))) {
    violations.push(`${relativePath} lives under release-disallowed path segment ${disallowedPart}`);
  }
}

if (violations.length) {
  console.error("Release audit failed. The app package contains files that should stay user-local:");
  for (const violation of violations) {
    console.error(`- ${violation}`);
  }
  process.exit(1);
}

console.log("Release audit OK: no ROMs, raw extracted payloads, or generated binary media found in the app package.");
