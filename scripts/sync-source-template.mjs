import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(appRoot, "..");
const codexSourceRoot = "F:\\Earthbound Decomp - Codex\\src";
const defaultSourceRoot = fs.existsSync(codexSourceRoot) ? codexSourceRoot : path.join(repoRoot, "src");
const templateRoot = path.join(appRoot, "source-template");

function optionValue(name) {
  const index = process.argv.indexOf(name);
  return index === -1 ? null : process.argv[index + 1] || null;
}

function resolveSourceRoot(inputPath) {
  const resolved = path.resolve(inputPath);
  const srcChild = path.join(resolved, "src");
  return fs.existsSync(srcChild) ? srcChild : resolved;
}

const sourceRoot = resolveSourceRoot(
  optionValue("--source-root") || process.env.EARTHBOUND_DECOMP_SOURCE_ROOT || defaultSourceRoot
);

function assertInside(parent, child) {
  const relative = path.relative(parent, child);
  if (relative.startsWith("..") || path.isAbsolute(relative)) {
    throw new Error(`Refusing to write outside ${parent}: ${child}`);
  }
}

function removeExistingTemplate() {
  assertInside(appRoot, templateRoot);
  fs.rmSync(templateRoot, { recursive: true, force: true });
  fs.mkdirSync(templateRoot, { recursive: true });
}

function copyDirectory(sourceDir, targetDir) {
  fs.mkdirSync(targetDir, { recursive: true });
  for (const entry of fs.readdirSync(sourceDir, { withFileTypes: true })) {
    const sourcePath = path.join(sourceDir, entry.name);
    const targetPath = path.join(targetDir, entry.name);
    if (entry.isDirectory()) {
      copyDirectory(sourcePath, targetPath);
    } else if (entry.isFile()) {
      fs.copyFileSync(sourcePath, targetPath);
    }
  }
}

function countFiles(root) {
  let count = 0;
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

if (!fs.existsSync(sourceRoot)) {
  throw new Error(`Source root is missing: ${sourceRoot}`);
}

removeExistingTemplate();
copyDirectory(sourceRoot, templateRoot);

console.log(`Synced ${countFiles(templateRoot).toLocaleString("en-US")} source files into ${templateRoot}`);
