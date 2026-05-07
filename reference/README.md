# EarthBound Decomp Scaffold

EarthBound Decomp Scaffold is a ROM-wide reverse-engineering scaffold and
documentation corpus for the US headerless EarthBound ROM.

It is built for romhackers, preservation-minded researchers, and anyone
interested in turning EarthBound from an opaque ROM into named, validated,
editable source/data structures.

This repository does not contain a ROM, extracted copyrighted assets, generated
audio, or a finished source port. Bring your own legally obtained ROM.

## What This Release Is

This is a first public research/scaffold release.

It gives you:

- byte-equivalent source scaffolds for all configured banks from `C0` through
  `EF`
- readable-source closure for the audited source-heavy banks
- source, table, script, text, asset, and audio notes with validation evidence
- EB-M2 Listing v1 name/module crosswalks, with meaningful labels promoted only
  through reviewed byte-equivalent batches
- Python tools for ROM verification, disassembly support, table inspection,
  script/text decoding, EB-M2 symbol lookup, asset manifests, and audio backend
  research
- machine-readable manifests for major subsystem and audio contracts
- a separate Electron Encyclopedia release binary for browsing the work in a
  searchable, romhacker/porter-friendly interface

It does not give you:

- an EarthBound ROM
- redistributed game graphics, music, samples, maps, or text dumps as assets
- exact-length public audio exports
- a complete C port or portable engine
- any rights to EarthBound, Mother 2, or ROM-derived content

## Encyclopedia App

GitHub link to **EarthBound Decomp Encyclopedia** Electron app
binary: https://github.com/iSynic/Earthbound-Decomp-Encyclopedia

The app is a companion browser/intelligence layer for this repository. It is
intended to make the notes, manifests, source scaffolds, bank maps, and subsystem
contracts easier to search and understand.

The app should be treated as a convenience viewer, not as a replacement for the
repo:

- it does not include the EarthBound ROM
- it should not include generated ROM-derived assets
- any ROM-derived outputs should be generated locally from a user-supplied ROM
- the source of truth remains the checked-in `notes/`, `src/`, `tools/`, and
  `manifests/` directories

## Current Status

The project has reached ROM-wide structural closure:

- `48 / 48` configured banks from `C0` through `EF` have checked-in
  byte-equivalent source scaffolds.
- Every bank scaffold validates against the expected ROM with `0` residual
  bytes and `0` byte-equivalence mismatches.
- The audited native-source-heavy banks, `C0`, `C1`, `C2`, `C4`, and `EF`, now
  report `0` preserved source corridors in
  `notes/readable-source-bank-closure.md`.
- EB-M2 Listing v1 is now integrated as a credited naming reference through
  `manifests/eb-m2-name-crosswalk.json`,
  `manifests/symbol-aliases.json`, and
  `notes/eb-m2-module-crosswalk.md`. The reviewed source-symbol promotion pass
  has adopted every currently ready exact-address, non-`UNKNOWN_*`,
  role-compatible EB-M2 label; it preserves old address-prefixed aliases and
  validates byte-equivalent with `0` mismatches in each promoted bank.
- C3's event/actionscript bank has no unexplained raw follow-up frontier in
  `notes/c3-source-data-map.md`; remaining C3 work is semantic and source/script
  emission polish.
- The text-command VM has a generated semantics manifest at
  `notes/text-command-semantics-manifest.md`, with `29 / 32` top-level commands
  covered and `0x15..0x17` isolated as compressed-bank parser-only
  pseudo-opcodes.
- The asset/data milestone is phase-good-enough in
  `notes/phase-4-asset-data-closeout.md`: `38` manifests represent `2219`
  assets/tables/gaps, with `0` unresolved missing E0/E1 manifest-inferred
  payload metadata units.
- The audio backend has a local, user-ROM-derived playback/export path. The
  current all-track fused CHANGE_MUSIC/C0:AB06 corpus renders `190 / 190`
  snapshot-backed tracks as audible through the libgme/snes_spc harness; track
  `4` (`NONE2`) is explicitly load-ok/no-key-on.

In plain English: the ROM bytes are accounted for, and the known native-source
frontiers are closed. The remaining work is mostly semantic refinement,
reassembly-friendly editing workflows, asset/script polish, and exact audio
duration/loop work.

## What You Can Do With It

Today, this project is useful for:

- finding where ROM bytes live and what subsystem owns them
- validating that source scaffolds still reproduce the original ROM bytes
- studying native 65816 routines with local names and notes
- exploring event/actionscript and text-command semantics
- locating table, WRAM, asset, and audio contracts before editing
- building romhacking tools that use the checked-in manifests
- planning future source ports or native-engine recreations one subsystem at a
  time

Romhacks are not the limit, but a faithful port needs stronger semantic models
for battle, menus, overworld scripts, rendering, audio, text, save/state, and
asset pipelines. This repo is the foundation for that work, not the finished
portable implementation.

## Key Terms

- **Scaffold-backed**: bytes are represented by checked-in source artifacts and
  pass byte-equivalence validation.
- **Readable-source closed**: audited native 65816 source corridors have been
  promoted out of coarse byte blobs.
- **Semantically understood**: a routine, table, bytecode command, or asset has
  reliable names, evidence, consumers, and editing constraints.

This project is scaffold-backed across all configured banks. It is
readable-source closed for the audited source-heavy banks. It is not yet a full
semantic decompilation or C port.

## Quick Start

Use the US headerless EarthBound ROM:

- Size: `3145728` bytes
- SHA-1: `D67A8EF36EF616BC39306AA1B486E1BD3047815A`
- Map mode: `0x31` (`HiROM/FastROM`)

Place it at either:

```text
./EarthBound (USA).sfc
./baserom/EarthBound (USA).sfc
```

Verify it:

```powershell
python tools/verify_rom.py
```

Validate a source bank:

```powershell
python tools/validate_source_bank_byte_equivalence.py --bank C3
```

Regenerate core status dashboards:

```powershell
python tools/build_source_scaffold_status.py
python tools/build_readable_source_bank_closure.py
python tools/build_text_command_semantics_manifest.py
```

Inspect code, references, or data:

```powershell
python tools/find_xrefs.py C20ABC --limit 12
python tools/find_direct_callers.py C2:D121
python tools/decode_snippet.py C1:244C --count 20 --show-state
python tools/inspect_table.py --contract ENEMY_CONFIGURATION_TABLE --index 0 --count 1
python tools/lookup_eb_m2_symbol.py OVERWORLD_SETUP_VRAM --evidence
python tools/lookup_eb_m2_symbol.py C00013
```

Work with text and event/actionscript payloads:

```powershell
python tools/find_ebtext_command.py 1C 05 --limit 12
python tools/decode_event_script.py C3:0195 C3:0295 C3:AB59
python tools/build_c3_actionscript_semantics_audit.py
```

Generated output belongs under ignored paths such as `build/`, `asm/`,
`dumps/`, or `refs/`. Commit durable conclusions in `notes/`, source modules in
`src/`, manifests in `manifests/`, and reusable tooling in `tools/`.

## Repository Layout

Tracked:

- `README.md` - public orientation
- `LICENSE.md` - Mozilla Public License 2.0 for original project code and docs
- `THIRD_PARTY_NOTICES.md` - attribution and dependency posture
- `notes/` - durable research notes and generated human-readable reports
- `src/` - source scaffold modules by bank
- `tools/` - local analysis, validation, and generation tools
- `manifests/` - machine-readable contract/status manifests
- `asset-manifests/` - asset/data manifest inputs

Ignored/local-only:

- `EarthBound (USA).sfc`
- `baserom/`
- `build/`
- `asm/`
- `dumps/`
- `refs/`
- `tmp_*.asm`
- generated audio, archives, caches, and extracted binary payloads

The `refs/` directory is intentionally local-only. Reference projects are useful
accelerators, but this repository should publish only conclusions that have been
locally checked or clearly labeled in notes.

## Best Starting Points

- `notes/project-status.md` - durable project orientation
- `notes/source-scaffold-status.md` - all-bank byte-equivalent scaffold dashboard
- `notes/readable-source-bank-closure.md` - source-heavy bank closure dashboard
- `notes/public-release-known-limits.md` - what this release does not claim
- `notes/how-to-validate.md` - validation commands
- `notes/python-tool-syntax-guide.md` - common tool syntax
- `notes/reference-first-workflow.md` - how local refs are used
- `notes/eb-m2-name-crosswalk.md` - EB-M2 canonical-name and alias policy
- `notes/eb-m2-module-crosswalk.md` - EB-M2 include/module boundary comparison
- `notes/eb-m2-needs-review-triage.md` - review queue for EB-M2/local naming
  conflicts
- `notes/c3-source-data-map.md` - C3 code/data/script split map
- `notes/c3-actionscript-semantics-audit.md` - C3 script decoder baseline
- `notes/text-command-semantics-manifest.md` - text-command VM coverage
- `notes/phase-4-asset-data-closeout.md` - asset/data contract boundary
- `notes/asset-data-contract-frontier.md` - asset/data family frontier
- `notes/audio-backend-contract.md` - local audio playback/export backend shape
- `notes/audio-export-plan.md` - current per-track export policy
- `notes/audio-exact-duration-triage.md` - exact loop/end semantics queue
- `notes/audio-dependency-policy.md` - renderer dependency and distribution policy

## Credits And References

This project stands on years of EarthBound community research. Special thanks
and credit go to:

- **Starmen.net** for long-running EarthBound community documentation, script
  resources, and preservation context.
- **EarthBound Wiki** for public game, item, location, character, and
  terminology references that help keep names and descriptions intelligible.
- **Herringway / EBSRC** for source-style EarthBound documentation and
  disassembly work that helped corroborate engine and script details.
- **EB-M2 Listing v1** for credited source-label and module-boundary reference
  data used in reviewed crosswalks and cautious source-name promotion.
- **Yoshifanatic1** for EarthBound disassembly work used as a reference and
  comparison point during this project.
- **ares** for preservation-focused SNES/APU emulation research and as the
  accuracy-first reference direction for audio backend experiments.

Those projects are references and inspirations, not bundled dependencies unless
explicitly stated. Any mistakes in this repository are ours.

## Clean Clone Expectations

A fresh clone should be useful without private local material:

- status notes, manifests, source scaffolds, and static validators are present
  immediately
- ROM-validation and byte-equivalence commands need a user-supplied ROM
- reference-assisted tools may ask for local `refs/` checkouts or recovered
  source archives
- audio renderer build/probe tools may ask for local ares or libgme checkouts
- missing local-only inputs should be treated as setup requirements, not as
  repository corruption

## Legal And Attribution Notes

This is an independent research project. It does not include a ROM and should
not be used to distribute copyrighted game data outside whatever legal framework
you are operating under.

Original project code and documentation are licensed under the Mozilla Public
License 2.0. This is a file-level copyleft license: changes to MPL-covered files
must stay available under the MPL, while larger works can combine them with
other code subject to the license terms.

Third-party emulator/audio projects are external references or optional local
build dependencies, not vendored runtime code. See `THIRD_PARTY_NOTICES.md` and
`notes/audio-dependency-policy.md` before redistributing tools, binaries, or
renderer integrations.
