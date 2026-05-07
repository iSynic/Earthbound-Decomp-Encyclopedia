# EF Debug Sound Menu Prefix `EF:D56F..D6D4`

## Main Result

`EF:D56F..D6D4` is now split out of the larger debug/menu corridor as decoded
source. It contains two clean routines before the next mixed code/string/data
area begins.

## Routines

- `EF:D56F` = `WriteDebugHexByteToTileBuffer`
  - Converts the high and low nibbles of the caller's value into debug tile
    codes.
  - Writes the two tile words into a C0-allocated tile buffer and queues a
    small transfer into the `7E:7C00`-based debug tile area selected by caller
    coordinates.
- `EF:D5D9` = `DrawDebugSoundMenuRows`
  - Sets up the debug sound-menu presentation mode.
  - Clears/refills the debug menu tile rows through later helpers in the same
    EF corridor.
  - Draws a fixed set of sound-menu option lines from the string block rooted
    just before this routine family.
  - Seeds per-slot row/column state in the `$0B8E/$0BCA` tables and queues the
    menu layer transfer.

## Boundary

The next reference include boundary is `EF:D6D4`. Decoding straight through
that area quickly crosses into the debug menu option string/table payloads, so
the current source module stops at `EF:D6D4` and preserves
`EF:D6D4..EF:EB5F` as the next mixed corridor.

## Evidence

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm` places
  `unknown/EF/EFD56F.asm`, `unknown/EF/EFD5D9.asm`, and
  `unknown/EF/EFD6D4.asm` at these boundaries.
- `notes/debug-menu-reachability-c0-c1-ef.md` identifies the broader late-EF
  region as debug/menu source with at least one non-debug caller seam around
  `EF:E759`.
- `notes/bank-ef-first-pass.md` classifies `EF:D56F..EF:EB5E` as mixed
  debug/menu code, strings, overlays, cursor/menu handlers, and remaining
  unknown routines.
