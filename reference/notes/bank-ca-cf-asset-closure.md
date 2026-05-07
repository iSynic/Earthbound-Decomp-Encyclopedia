# Banks CA-CF Asset/Data Closure

## Status

Banks `CA` through `CF` are now mapped at the bank-layout level. This stretch is
almost entirely assets and generated data, not executable code.

| Bank | Role | Primary artifacts | Coverage boundary |
| --- | --- | --- | --- |
| `CA` | battle background graphics/arrangements plus background tables | `notes/bank-ca-first-pass.md`, `build/asset-bank-ca.json` | `1` byte gap |
| `CB` | battle background graphics/arrangements/palettes, battle-entry background table, audio packs | `notes/bank-cb-first-pass.md`, `build/asset-bank-cb.json` | `28` bytes tail slack |
| `CC` | animation payloads, PSI animation assets/tables, audio pack | `notes/bank-cc-first-pass.md`, `build/asset-bank-cc.json` | `37` bytes tail slack |
| `CD` | full-bank battle sprite graphics payload slab | `notes/bank-cd-first-pass.md`, `build/asset-bank-cd.json` | no gaps |
| `CE` | battle sprite tail, battle sprite pointer table/palettes, swirl data, Sound Stone assets, audio pack | `notes/bank-ce-first-pass.md`, `build/asset-bank-ce.json` | `86` bytes tail slack |
| `CF` | generated map data plus audio packs | `notes/bank-cf-first-pass.md`, `build/asset-bank-cf.json` | `7` bytes tail slack |

## Tooling

`tools/build_asset_bank_manifest.py` now handles the recurring bankconfig
patterns needed for this range:

- nested `bankconfig/common/...` includes from US bank configs.
- normal `BINARY`, locale-aware `LOCALEBINARY`, and `INSERT_AUDIO_PACK`.
- root-level payloads with empty `earthbound.yml` subdirs.
- simple US retail conditional assembly with `.IF .DEFINED(...)`, `.ELSE`, and
  `.ENDIF`, including `||` and `&&` expressions.
- included source-table byte counts from `.BYTE/.WORD/.DWORD`.
- inline bankconfig `.BYTE/.WORD/.DWORD` blocks.
- inferred generated-table spans when source files are referenced but absent.

## Source-Code Readiness

High confidence source-ready as opaque assets:

- `CA`, `CB`, `CC`, `CD`, and `CE` can be represented as assembly/source with
  binary payload includes plus the table includes or inline data currently
  documented.
- `CD` is especially straightforward: all `65536` bytes are battle sprite
  payloads.

Needs a later semantic contract pass:

- battle background arrangement/palette semantics in `CA` and `CB`.
- PSI arrangement/config/pointer field names in `CC`.
- battle sprite pointer table and palette semantics in `CE`.
- swirl payload format and primary table semantics in `CE`.
- generated map-data internals in `CF`.

The important distinction: these banks are largely reconstructable as source
layout now, but some table fields remain semantically named only by surrounding
runtime behavior.

## CF Boundary

`CF` is the one bank in this range where the manifest cannot split the big
pre-audio data region into exact source-table ranges. The checked-in ebsrc
bankconfig names the generated map includes, but the generated files themselves
are absent from the ref tree. The current honest boundary is:

- `CF:0000..CF:F2B4`: generated map-data region.
- `CF:F2B5..CF:FFF8`: two audio packs.
- `CF:FFF9..CF:FFFF`: tail slack.

To split CF further, derive the internal map-data contracts from engine readers
and ROM structure, not from the missing generated source files.

## Recommended Next Move

Proceed to `D0` with the same manifest-first approach. If `D0` is another
asset/data bank, close it quickly; if it exposes more generated map-data, pause
and decide whether to build a dedicated map-data splitter for `CF+`.
