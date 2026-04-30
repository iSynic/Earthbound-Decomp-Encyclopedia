import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(__dirname, "..");
const catalogPath = path.join(appRoot, "public", "generated", "catalog.json");

if (!fs.existsSync(catalogPath)) {
  console.error("Missing generated catalog. Run `npm run build:content` first.");
  process.exit(1);
}

const catalog = JSON.parse(fs.readFileSync(catalogPath, "utf8"));
const ids = new Set();
const duplicates = [];

for (const entry of catalog.entries) {
  if (ids.has(entry.id)) {
    duplicates.push(entry.id);
  }
  ids.add(entry.id);
}

const missing = [];
for (const entry of catalog.entries) {
  for (const id of entry.related || []) {
    if (!ids.has(id)) {
      missing.push(`${entry.id} -> ${id}`);
    }
  }

  const linkPattern = /\[\[([^|\]]+)/g;
  let match;
  while ((match = linkPattern.exec(entry.body || "")) !== null) {
    if (!ids.has(match[1])) {
      missing.push(`${entry.id} -> ${match[1]}`);
    }
  }

  for (const ref of [...(entry.sourceRefs || []), ...(entry.noteRefs || [])]) {
    if (ref.entryId && !ids.has(ref.entryId)) {
      missing.push(`${entry.id} ref -> ${ref.entryId}`);
    }
  }
}

if (duplicates.length || missing.length) {
  if (duplicates.length) {
    console.error("Duplicate entry IDs:");
    for (const id of duplicates) {
      console.error(`- ${id}`);
    }
  }
  if (missing.length) {
    console.error("Broken internal links:");
    for (const link of missing) {
      console.error(`- ${link}`);
    }
  }
  process.exit(1);
}

console.log(`Catalog OK: ${catalog.entries.length} entries, no duplicate IDs, no broken internal links.`);
