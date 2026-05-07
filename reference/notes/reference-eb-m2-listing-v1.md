# EB-M2 Listing v1 Reference

`EB-M2-Listing-v1.zip` was provided locally on 2026-04-29 and unpacked under
the ignored reference path `refs/EB-M2-Listing-v1/`.

Archive hashes:

- SHA-1: `5BC61CFFD2027C7F204F167DAEF5491B86CFF1AC`
- SHA-256: `3C50F7DE4D36B5E6C5167D08D07AEFAA5B6B65B9D63DF54D0A5BC3025395EE5E`

## Shape

- `US/bank00.txt` through `US/bank2F.txt`
- `JP/bank00.txt` through `JP/bank2F.txt`
- roughly `42.7 MB` uncompressed
- bank indices map directly to canonical project banks:
  - `bank00` = `C0`
  - `bank01` = `C1`
  - ...
  - `bank2F` = `EF`

## Why It Matters

The listing contains address-annotated source/include traces with labels,
macros, binary includes, and emitted bytes. It is immediately useful as a
high-signal reference for:

- cross-checking our working names against established labels;
- locating original include/module boundaries;
- comparing US and JP bank structure;
- validating asset/data ownership labels;
- improving public-facing terminology so the project looks less like a raw
  byte scaffold where better names are already available.

Examples seen during import:

- `C00000` `CLEAR_ENTITY_DRAW_SORTING_TABLE`
- `C00013` `OVERWORLD_SETUP_VRAM`
- `C30100` `DISPLAY_ANTI_PIRACY_SCREEN`
- `EF0000` `ENEMY_FLASHING_OFF`

## License

The listing was reported as released under the Unlicense/public-domain
dedication:

- free and unencumbered software released into the public domain;
- permission to copy, modify, publish, use, compile, sell, or distribute;
- provided "as is" without warranty.

This permits incorporating source-label and module-boundary information into
the project. ROM-derived game assets and generated outputs remain governed by
the repository's separate no-redistribution policy.

## Usage

Look up an address:

```powershell
python tools/lookup_eb_m2_listing.py C0:0013
python tools/lookup_eb_m2_listing.py EF0000 --context 20
```

Search for a symbol:

```powershell
python tools/lookup_eb_m2_listing.py OVERWORLD_SETUP_VRAM --symbol
python tools/lookup_eb_m2_listing.py ENEMY_FLASHING_OFF --symbol --bank 2F
```

## Cautions

Treat this as a reference/cross-check source with explicit attribution. Prefer
derived indexes, crosswalks, aliases, and reviewed source-name promotions over
large unreviewed imports.

The formal integration plan is tracked in
`notes/eb-m2-listing-integration-plan.md`.

The current exact-address naming crosswalk is tracked in
`notes/eb-m2-name-crosswalk.md` and
`manifests/eb-m2-name-crosswalk.json`.
