# Public Release Known Limits

This repository is suitable for careful community review as a ROM-wide
byte-equivalent scaffold and research corpus. It is not a finished decompilation
or a source port.

## What The First Public Release Claims

- The configured US headerless EarthBound ROM banks `C0..EF` have checked-in
  byte-equivalent source scaffolds.
- The audited native-source-heavy banks have no remaining preserved source
  corridors by the current closure dashboard.
- Major script, text, asset, table, and audio frontiers are named and bounded in
  notes and machine-readable manifests.
- Local tools can validate the ROM, rebuild scaffolds, inspect tables/scripts,
  and regenerate public status dashboards.
- Audio playback/export has a local user-ROM-derived backend path: `190 / 190`
  snapshot-backed tracks render audibly through the libgme/snes_spc path, while
  track `4` (`NONE2`) is a documented load-ok/no-key-on table entry.

## What It Does Not Claim

- No ROM, copyrighted assets, generated SPC/WAV/PCM files, or local reference
  dumps are distributed.
- The project is not yet a C port or a portable engine.
- Byte-equivalent assembly scaffolds are not the same thing as fully named,
  idiomatic, high-level source.
- C3 event/actionscript and text/localization macro semantics are phase-good
  enough, but some opcode, macro-lowering, and reassembly UX polish remains.
- Audio exports are not yet exact-length OST replacements. Loop points, some
  finite endings, and independent external-emulator oracle validation are still
  tracked work.
- Asset manifests describe and validate many payloads, but not every payload has
  a polished visual editor, renderer fixture, or semantic field name.

## Distribution Boundary

End users provide their own legally obtained ROM. Tools may generate local
source, manifests, SPCs, WAVs, previews, or extracted assets from that ROM, but
generated ROM-derived outputs stay ignored and should not be committed.

Reference projects in `refs/` are local-only accelerators. Public notes should
cite conclusions and provenance without copying private/local dumps wholesale.
