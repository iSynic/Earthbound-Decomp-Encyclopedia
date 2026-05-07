# Community EarthBound Docs Reference

Imported community reference docs under `refs/community-earthbound-docs/`:

- `ROM_map.txt`
- `RAM_map.txt`
- `Text_table.txt`
- `Control_codes.txt`
- `Standard_arguments.txt`
- `Flags.txt`

## What these appear to be

These look like community-maintained EarthBound documentation rather than a code-first disassembly or decompilation project.

At a glance:

- `ROM_map.txt` is a broad bank/file-offset map with routine and data-region descriptions.
- `RAM_map.txt` is a broad WRAM/SNES-register map.
- `Text_table.txt` is a text/compression lookup table.
- `Control_codes.txt` is a narrative explanation of the text-engine control-code model, including active/storage memory terminology.
- `Standard_arguments.txt` is a command/window/common-argument reference for the text engine.
- `Flags.txt` is a large converted flag-name list attributed to the floppy/script source recovery lineage.

## How to use them

These should be treated as supplemental cross-check references, not as authoritative ground truth.

Best use cases:

- quickly sanity-checking RAM/address naming when a local note is still vague
- cross-checking text-engine concepts like working/argument/storage memory
- checking community flag naming against local script or engine behavior
- spotting likely table domains before doing a ROM-first local trace

Less safe uses:

- treating any individual map label as proved without local confirmation
- assuming broad ROM-map region labels correspond cleanly to our exact local function boundaries
- inheriting flag or text-command names without distinguishing community naming from direct ROM evidence

## Immediate value

The strongest likely payoff is on the bank-`01` text-engine side:

- `Control_codes.txt` aligns well with the active/storage memory model already established locally around the `0x1B/0x1C/0x1D/0x1F` families.
- `Flags.txt` is likely useful as another cross-check source for script-side flag names, alongside `ebsrc-main` and `eb-decompile-4ef92`.
- `Text_table.txt` and `Standard_arguments.txt` may help as quick-look aids when checking script/control-byte behavior.

## Current stance

Keep these quarantined the same way we use the other side references:

- useful for orientation and cross-checks
- valuable when they match local behavior
- not a substitute for ROM-first verification

## Known conflict to watch

One concrete mismatch is worth keeping explicit in future note work:

- the community `RAM_map.txt` labels `$9839` as `Learned PSI`
- quarantined `ebsrc-main` struct refs place `$9839` inside `game_state::favourite_thing`
- local ROM work around `C2:27C8` shows `$9839` also being reused at runtime as a temporary party-wide bitmask accumulator for current `$99DC` state values

So the community RAM map is still useful for orientation, but `$9839` is now a clear example of why we should not inherit any single label there as authoritative without checking both the ROM and the stronger struct references.
