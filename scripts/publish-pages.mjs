import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(__dirname, "..");
const webRoot = path.join(appRoot, "dist-web");
const remoteName = process.env.PAGES_REMOTE || "encyclopedia";
const branchName = process.env.PAGES_BRANCH || "gh-pages";

function run(command, args, options = {}) {
  const output = execFileSync(command, args, {
    cwd: options.cwd || appRoot,
    encoding: "utf8",
    stdio: options.stdio || "pipe"
  });
  return typeof output === "string" ? output.trim() : "";
}

function copyDirectory(sourceDir, targetDir) {
  fs.mkdirSync(targetDir, { recursive: true });
  for (const entry of fs.readdirSync(sourceDir, { withFileTypes: true })) {
    const sourcePath = path.join(sourceDir, entry.name);
    const targetPath = path.join(targetDir, entry.name);
    if (entry.isDirectory()) {
      copyDirectory(sourcePath, targetPath);
    } else if (entry.isFile()) {
      fs.mkdirSync(path.dirname(targetPath), { recursive: true });
      fs.copyFileSync(sourcePath, targetPath);
    }
  }
}

if (!fs.existsSync(path.join(webRoot, "index.html"))) {
  throw new Error("dist-web/index.html is missing; run npm run web:build first.");
}

const remoteUrl = run("git", ["config", "--get", `remote.${remoteName}.url`]);
if (!remoteUrl) {
  throw new Error(`Git remote ${remoteName} is not configured.`);
}

const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), "earthbound-pages-"));
try {
  run("git", ["init"], { cwd: tempRoot });
  run("git", ["checkout", "-B", branchName], { cwd: tempRoot });
  run("git", ["remote", "add", "origin", remoteUrl], { cwd: tempRoot });
  copyDirectory(webRoot, tempRoot);
  run("git", ["add", "-A"], { cwd: tempRoot });
  run("git", ["-c", "user.name=Codex", "-c", "user.email=codex@local", "commit", "-m", "Publish encyclopedia web build"], { cwd: tempRoot });
  run("git", ["push", "--force", "origin", `${branchName}:refs/heads/${branchName}`], { cwd: tempRoot, stdio: "inherit" });
  console.log(`Published ${webRoot} to ${remoteName}/${branchName}.`);
} finally {
  fs.rmSync(tempRoot, { recursive: true, force: true });
}
