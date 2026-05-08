import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(__dirname, "..");
const publicRoot = path.join(appRoot, "public");
const webRoot = path.join(appRoot, "dist-web");

const skipped = new Set([
  path.join(publicRoot, "generated", "catalog.json"),
  path.join(publicRoot, "generated", "source-snapshot.json")
]);

function shouldSkip(filePath) {
  if (skipped.has(filePath)) {
    return true;
  }
  return /\.map$/i.test(filePath);
}

function copyDirectory(sourceDir, targetDir) {
  fs.mkdirSync(targetDir, { recursive: true });
  for (const entry of fs.readdirSync(sourceDir, { withFileTypes: true })) {
    const sourcePath = path.join(sourceDir, entry.name);
    const targetPath = path.join(targetDir, entry.name);
    if (shouldSkip(sourcePath)) {
      continue;
    }
    if (entry.isDirectory()) {
      copyDirectory(sourcePath, targetPath);
    } else if (entry.isFile()) {
      fs.mkdirSync(path.dirname(targetPath), { recursive: true });
      fs.copyFileSync(sourcePath, targetPath);
    }
  }
}

function countFiles(root) {
  let count = 0;
  let bytes = 0;
  for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
    const entryPath = path.join(root, entry.name);
    if (entry.isDirectory()) {
      const child = countFiles(entryPath);
      count += child.count;
      bytes += child.bytes;
    } else if (entry.isFile()) {
      count += 1;
      bytes += fs.statSync(entryPath).size;
    }
  }
  return { count, bytes };
}

if (!fs.existsSync(path.join(publicRoot, "generated", "catalog.js"))) {
  throw new Error("public/generated/catalog.js is missing; run npm run build:content:private first.");
}

fs.rmSync(webRoot, { recursive: true, force: true });
copyDirectory(publicRoot, webRoot);
fs.writeFileSync(path.join(webRoot, ".nojekyll"), "", "utf8");

const stats = countFiles(webRoot);
console.log(`Built GitHub Pages site at ${webRoot}`);
console.log(`Copied ${stats.count.toLocaleString("en-US")} files (${(stats.bytes / 1024 / 1024).toFixed(2)} MiB).`);
console.log("Skipped generated/catalog.json; the browser app uses generated/catalog.js.");
