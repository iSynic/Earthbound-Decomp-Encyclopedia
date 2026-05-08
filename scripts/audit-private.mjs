import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(__dirname, "..");
const referenceRoot = path.join(appRoot, "reference");
const catalogPath = path.join(appRoot, "public", "generated", "catalog.json");
const uiFiles = [
  path.join(appRoot, "public", "app.js"),
  path.join(appRoot, "public", "index.html"),
  path.join(appRoot, "electron", "main.cjs"),
  path.join(appRoot, "electron", "preload.cjs")
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
  "baserom",
  "dumps",
  "build",
  "cache",
  ".cache",
  "renderer-fixtures",
  "preview-sheets",
  "spc",
  "wav"
]);

function walk(root) {
  const output = [];
  if (!fs.existsSync(root)) {
    return output;
  }
  for (const item of fs.readdirSync(root, { withFileTypes: true })) {
    if (item.name === "node_modules" || item.name === ".git" || item.name === "dist") {
      continue;
    }
    const itemPath = path.join(root, item.name);
    if (item.isDirectory()) {
      output.push(...walk(itemPath));
    } else if (item.isFile()) {
      output.push(itemPath);
    }
  }
  return output;
}

const violations = [];

if (!fs.existsSync(referenceRoot)) {
  violations.push("reference/ is missing; run npm run sync:reference");
}

if (!fs.existsSync(catalogPath)) {
  violations.push("public/generated/catalog.json is missing; run npm run build:content:private");
} else {
  const catalog = JSON.parse(fs.readFileSync(catalogPath, "utf8"));
  if (catalog.buildMode !== "private") {
    violations.push(`catalog buildMode is ${JSON.stringify(catalog.buildMode)}; expected "private"`);
  }
  const entries = catalog.entries || [];
  const requiredIds = ["source-browser", "reference-source-browser", "reference-library", "reference-tables", "note-index", "asset-manifest-index"];
  for (const id of requiredIds) {
    if (!entries.some((entry) => entry.id === id)) {
      violations.push(`catalog is missing required private reference entry ${id}`);
    }
  }
  const forbiddenIds = ["local-workspace", "asset-library", "rom-status"];
  for (const id of forbiddenIds) {
    if (entries.some((entry) => entry.id === id)) {
      violations.push(`catalog still contains removed workspace entry ${id}`);
    }
  }
  if (!Array.isArray(catalog.searchIndex?.documents) || !catalog.searchIndex.documents.length) {
    violations.push("catalog searchIndex.documents is missing or empty");
  }
  if (!catalog.referenceSync || !catalog.referenceSync.generatedAt) {
    violations.push("catalog referenceSync metadata is missing a generatedAt timestamp");
  }
  if (catalog.referenceSync?.sourceGit?.available && !catalog.referenceSync.sourceGit.shortSha) {
    violations.push("catalog referenceSync sourceGit is available but shortSha is missing");
  }
  if (!Array.isArray(catalog.navSections) || !catalog.navSections.some((section) => section.title === "Systems" && (section.ids || []).includes("systems-hub"))) {
    violations.push("catalog navSections is missing the Systems hub section");
  }
  if (!catalog.facets?.kindCounts || !catalog.facets?.domainCounts) {
    violations.push("catalog facets metadata is missing kind/domain counts");
  }
  if (!entries.some((entry) => entry.kind === "source-file" && entry.sourceFile?.path && Array.isArray(entry.relatedNotes))) {
    violations.push("source-file entries are missing compact sourceFile metadata or relatedNotes");
  }
  if (!entries.some((entry) => entry.kind === "reference-source" && entry.sourceFile?.path?.includes("refs/ebsrc-main/"))) {
    violations.push("catalog is missing Herringway/ebsrc reference-source entries");
  }
  if (!entries.some((entry) => entry.kind === "reference-table" && /item ids/i.test(entry.title || ""))) {
    violations.push("catalog is missing useful reference tables such as Item IDs");
  }
  const scriptEntries = entries.filter((entry) => entry.kind === "reference-script");
  if (!scriptEntries.length) {
    violations.push("catalog is missing Shift-JIS decoded reference-script entries for .MSG files");
  }
  if (!entries.some((entry) => entry.id === "script-source-index")) {
    violations.push("catalog is missing script-source-index for decoded .MSG files");
  }
}

const removedUiStrings = [
  "Import ROM",
  "Add ROM",
  "Asset Library",
  "workspace generation"
];

for (const filePath of uiFiles) {
  if (!fs.existsSync(filePath)) {
    continue;
  }
  const text = fs.readFileSync(filePath, "utf8");
  for (const removed of removedUiStrings) {
    if (text.includes(removed)) {
      violations.push(`${path.relative(appRoot, filePath).replaceAll("\\", "/")} still contains removed UI string ${JSON.stringify(removed)}`);
    }
  }
}

for (const filePath of walk(referenceRoot)) {
  const relativePath = path.relative(referenceRoot, filePath).replaceAll("\\", "/");
  const ext = path.extname(filePath).toLowerCase();
  const parts = relativePath.split("/").map((part) => part.toLowerCase());
  if (disallowedExtensions.has(ext)) {
    violations.push(`reference/${relativePath} uses disallowed private bundle extension ${ext}`);
  }
  const disallowedPart = parts.find((part) => disallowedParts.has(part));
  if (disallowedPart) {
    violations.push(`reference/${relativePath} lives under disallowed generated path segment ${disallowedPart}`);
  }
  if (relativePath.startsWith("tools/")) {
    violations.push(`reference/${relativePath} bundles a tool script; private reference builds should keep only notes about tools`);
  }
  if (ext === ".py") {
    violations.push(`reference/${relativePath} bundles a Python tool script; private reference builds should keep only notes about tools`);
  }
}

if (violations.length) {
  console.error("Private reference audit failed:");
  for (const violation of violations) {
    console.error(`- ${violation}`);
  }
  process.exit(1);
}

console.log("Private reference audit OK: bundled notes/source reference is present without ROM/media payloads.");
