import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(scriptDir, "..");
const contentPath = path.join(appRoot, "content", "narrative-chapters.json");

const args = process.argv.slice(2);
const strict = args.includes("--strict");
const json = args.includes("--json");

const patterns = [
  {
    id: "page-self-reference",
    severity: "high",
    pattern: /\b(this chapter|this page|the chapter|the page|the encyclopedia)\s+should\b/i,
    message: "Rewrite page-planning language as direct content."
  },
  {
    id: "future-editor",
    severity: "medium",
    pattern: /\bfuture (editor|tool|page|chapter)\b/i,
    message: "Prefer direct editing constraints or current scope labels over future-facing prose."
  },
  {
    id: "unscoped-should",
    severity: "low",
    pattern: /\bshould\b/i,
    message: "Check whether this is a real constraint or soft meta-commentary."
  },
  {
    id: "planned-tooling",
    severity: "medium",
    pattern: /\bplanned\b/i,
    message: "Clarify whether the item is ROM knowledge, project tooling, or not implemented."
  },
  {
    id: "frontier-word",
    severity: "low",
    pattern: /\bfrontier\b/i,
    message: "Use frontier only for unresolved boundaries; prefer contract for stable facts."
  }
];

function sentenceFragments(value) {
  if (typeof value !== "string") return [];
  return value
    .split(/(?<=[.!?])\s+/)
    .map((fragment) => fragment.trim())
    .filter(Boolean);
}

function collectChapterProse(chapter) {
  const items = [
    { trail: ["title"], value: chapter.title },
    { trail: ["summary"], value: chapter.summary }
  ];
  for (const [sectionIndex, section] of (chapter.sections || []).entries()) {
    items.push({ trail: ["sections", sectionIndex, "title"], value: section.title });
    for (const [paragraphIndex, paragraph] of (section.paragraphs || []).entries()) {
      items.push({ trail: ["sections", sectionIndex, "paragraphs", paragraphIndex], value: paragraph });
    }
    for (const [bulletIndex, bullet] of (section.bullets || []).entries()) {
      items.push({ trail: ["sections", sectionIndex, "bullets", bulletIndex], value: bullet });
    }
  }
  return items.filter((item) => typeof item.value === "string" && item.value.trim());
}

const data = JSON.parse(fs.readFileSync(contentPath, "utf8"));
const findings = [];

for (const chapter of data.chapters || []) {
  for (const item of collectChapterProse(chapter)) {
    for (const fragment of sentenceFragments(item.value)) {
      for (const rule of patterns) {
        if (rule.pattern.test(fragment)) {
          findings.push({
            chapter_id: chapter.id,
            chapter_title: chapter.title,
            path: item.trail.join("."),
            rule: rule.id,
            severity: rule.severity,
            message: rule.message,
            text: fragment
          });
        }
      }
    }
  }
}

const severityRank = { high: 0, medium: 1, low: 2 };
findings.sort((a, b) => {
  return (
    severityRank[a.severity] - severityRank[b.severity] ||
    a.chapter_id.localeCompare(b.chapter_id) ||
    a.rule.localeCompare(b.rule) ||
    a.text.localeCompare(b.text)
  );
});

const counts = findings.reduce((acc, finding) => {
  acc[finding.severity] = (acc[finding.severity] || 0) + 1;
  acc.total = (acc.total || 0) + 1;
  return acc;
}, {});

if (json) {
  console.log(JSON.stringify({ schema: "earthbound-decomp.editorial-tone-audit.v1", counts, findings }, null, 2));
} else {
  console.log("Editorial tone audit:");
  console.log(`- Total findings: ${counts.total || 0}`);
  console.log(`- High: ${counts.high || 0}`);
  console.log(`- Medium: ${counts.medium || 0}`);
  console.log(`- Low: ${counts.low || 0}`);
  for (const finding of findings.slice(0, 80)) {
    console.log("");
    console.log(`## ${finding.severity.toUpperCase()} ${finding.rule} - ${finding.chapter_id}`);
    console.log(`Path: ${finding.path}`);
    console.log(finding.message);
    console.log(`> ${finding.text}`);
  }
  if (findings.length > 80) {
    console.log("");
    console.log(`... ${findings.length - 80} additional findings omitted. Use --json for the full report.`);
  }
}

if (strict && findings.some((finding) => finding.severity === "high")) {
  process.exit(1);
}
