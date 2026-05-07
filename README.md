# EarthBound Decomp Encyclopedia

Private Electron reference guide for the EarthBound decomp knowledge base.

This branch bundles the current notes, commented source, source-safe manifests, and reference metadata into the app. It does not import ROMs, generate source from a ROM, browse sprites/assets, preview generated media, or export generated payloads. Executable tools stay in the decomp repository; this app keeps notes about tool and validation workflows searchable.

## Private Reference Workflow

Sync the bundled reference copy from the active decomp checkout:

```powershell
npm run sync:reference
```

By default this reads from:

```text
F:\Earthbound Decomp - Codex
```

The sync includes:

- `notes/`
- `src/`
- `manifests/`
- `asset-manifests/`
- source-safe `refs/`
- top-level project reference docs

The sync excludes ROMs, generated binaries, generated media, build/cache folders, and `tools/`.

Build the private catalog:

```powershell
npm run build:content:private
```

Run the full private prep gate:

```powershell
npm run prepare:private
```

That runs:

- `sync:reference`
- `build:content:private`
- `check:content`
- `audit:private`

## Launch

After dependencies are installed:

```powershell
npm start
```

For a fresh private reference rebuild and launch:

```powershell
npm run prepare:private
npm start
```

## What The App Contains

- Curated orientation chapters and learning paths.
- A bank-first source browser for bundled `.asm` source.
- Source-file entries with line-numbered code blocks and deferred heavy bodies.
- Evidence-note entries for bundled markdown notes.
- Topic and relationship indexes linking notes, source, banks, routines, and manifests.
- Asset manifest documentation pages, without asset viewing/export features.
- A generated weighted search index for notes, source comments, labels, addresses, filenames, banks, manifests, and workflow notes.

## What Is Intentionally Removed

- ROM import / Add ROM / first-run local workspace.
- ROM verification and app-data generation.
- Sprite and asset viewing.
- Generated media previews.
- ZIP export workflows.
- Electron IPC handlers for generation/export/preview.
- Bundled Python tool scripts.

## Private Audit

Validate that the bundled reference does not contain ROM/media/generated payloads:

```powershell
npm run audit:private
```

The audit also checks that the catalog was built in `private` mode, includes required reference entries, has a generated search index, and does not contain the removed workspace pages.
