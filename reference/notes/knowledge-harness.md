# Knowledge Harness

This workspace keeps a local index of the EarthBound decomp corpus at:

`F:\Earthbound Decomp - Codex`

The index lives under `.kb/` and is intentionally ignored by git.

## Refresh

```powershell
python scripts/eb_kb.py index
```

Run this after new notes, manifests, or source files are added to the decomp
workspace.

Check whether the cache is stale:

```powershell
python scripts/eb_kb.py stale
```

The default profile indexes the high-value documentation layer: `notes/`,
`manifests/`, `asset-manifests/`, and `tools/`, excluding very large generated
JSON files. For source-heavy ASM browsing, build a separate cache:

```powershell
python scripts/eb_kb.py --config kb.source.config.json --cache .kb-source index
python scripts/eb_kb.py --cache .kb-source search "c0_1558 strip upload"
python scripts/eb_kb.py --config kb.source.config.json --cache .kb-source stale
```

## Search

```powershell
python scripts/eb_kb.py search "overworld stutter vertical defer"
python scripts/eb_kb.py search "C0:1558 strip upload" --kind notes -n 12
python scripts/eb_kb.py files "text command 1f deferred callbacks"
```

`search` ranks line-window snippets. `files` ranks whole files by path, title,
headings, bank tags, and address tags.

## Context Packs

```powershell
python scripts/eb_kb.py pack "audio exact duration loop oracle" -n 8
```

Use `pack` when a future question needs a compact briefing before deeper
inspection. It emits cited snippets with file paths and line ranges.

## Answer Style

When a readable decompiler/DSL representation exists for a script or routine,
include it alongside the lower-level assembly or byte-oriented evidence. The
preferred shape is:

- readable form first, when it makes the intent obvious
- assembly/ROM-address form second, when it proves the mapping
- note any encoding or pretty-printer differences, such as EBText glyphs that
  appear differently across tools

## Show Source Context

```powershell
python scripts/eb_kb.py show "notes/overworld_stutter_mesen_test_results_2026-04-30.md:120"
```

`show` reads from the decomp workspace and prints nearby lines from an indexed
file. It does not write to the decomp workspace.

## Current Scope

The first layer is lexical and metadata-based:

- Markdown notes
- JSON manifests
- ASM/ASAR source scaffolds
- Python tooling
- selected text/config files

It extracts headings, banks, addresses, file kinds, line windows, and token
postings. This is not a replacement for reading primary notes; it is a fast
triage layer that tells us which notes and source files deserve attention.
