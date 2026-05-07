# Landing Profile Cache `$436E / $4370 / $4372` and Sequencer `$445C..4474`

This note captures the current best local model for the cached landing-profile state that sits downstream of the destination override words `$438A / $438C`.

See also [transition-landing-mode-family-9f3f-9f41.md](notes/transition-landing-mode-family-9f3f-9f41.md).
See also [landing-destination-table-d57880.md](notes/landing-destination-table-d57880.md).
See also [landing-profile-bundles-ef121b-43dc.md](notes/landing-profile-bundles-ef121b-43dc.md).
See also [landing-profile-asset-families-ef105b-10ab-11cb-121b.md](notes/landing-profile-asset-families-ef105b-10ab-11cb-121b.md).

## Main result

The strongest current local read is:

- `$436E / $4370 / $4372` form a small cached landing-region or landing-profile selector block
- `C0:DD79` invalidates that cache after installing a destination record from `D5:7880`
- broader world-side code rebuilds the cache from the selected destination coordinates
- the rebuilt cache then seeds a tiny sequencer at `$445C / $445E / $4460 / $4474`
- that sequencer drives `C0:A1F2`, which installs one of several WRAM payload templates
- the same cached profile also selects `EF:11CB / EF:121B`, which together drive timed VRAM uploads from decompressed WRAM payload `7E:C000`

So the safest current wording is no longer just "some world-side override state." This is now a real cached landing-profile family with both WRAM-template and VRAM-upload sides.

## Cached selector trio

### `$436E`

The strongest current local read is a cached coarse landing-region class.

Local evidence:

- `C0:08CF` derives a byte from destination override words `$438A / $438C`
- it splits that byte into:
  - low `3` bits -> direct-page `$18`
  - high bits `>> 3` -> direct-page `$04`
- `C0:0A95` later commits `$04 -> $436E`
- `C0:0974` compares the freshly derived `$04` against cached `$436E`
- if equal, it skips the more expensive profile rebuild path
- `C0:DD79` invalidates `$436E` with `#$FFFF` before forcing a fresh rebuild from the selected destination

So `$436E` is best described as the cached coarse landing-region class, not a coordinate word.

### `$4370`

The strongest current local read is the cached low-bit landing-region variant or subregion code.

Local evidence:

- in the same `C0:08CF` path, the low `3` bits of the derived region byte are stored in direct-page `$18`
- `C0:0A9A` commits `$18 -> $4370`
- `C0:DD79` invalidates `$4370` together with `$436E`

So the safest current wording is:

- `$4370` = cached low-bit landing-region variant paired with `$436E`

I am still keeping the exact player-facing name open, but this no longer looks like a free-standing flag.

### `$4372`

The strongest current local read is a cached landing-profile selector.

Local evidence:

- `C0:08CF` derives a region class in direct-page `$04`
- it doubles that class and indexes `EF:101B`
- the resulting value is parked in direct-page `$16`
- `C0:097B` commits `Y -> $4372`
- later `C0:0085` reads `$4372`, doubles it, and indexes `EF:121B`

So `$4372` is no longer best read as a coordinate or miscellaneous counter. It looks like the selector that chooses the active landing-profile bundle after the region cache has been rebuilt.

## Profile rebuild path

The cleanest visible rebuild path is:

- destination record installs `$438A / $438C`
- `C0:08CF` derives a region byte from those override coordinates
- `C0:0974` compares the new coarse class against cached `$436E`
- if changed, `C0:097B+` stores the new profile selector in `$4372`
- `C0:0A95 / 0A9A` store the new cached class pair in `$436E / $4370`

So the broad current picture is:

- `$438A / $438C` choose the destination coordinates
- `$436E / $4370 / $4372` cache the world-side region/profile interpretation of that destination

## Sequencer block `$445C / $445E / $4460 / $4474`

The `44xx` side now looks like a tiny step sequencer built from the selected profile.

### `C0:023F`

`C0:023F` builds the live sequence block:

- clears `$4474`
- resolves a two-level pointer chain from `DF:E4E1 + 4 * ($02A0 - 1)`
- copies a bounded list of one-byte values into `$4460...`
- seeds:
  - `$445C = $4460[0]`
  - `$445E = 1`
  - `$4474 = 1`

So the safest current wording is:

- `$4460...` = per-profile step-duration or step-parameter list
- `$445C` = current countdown or current step value
- `$445E` = current step index
- `$4474` = sequencer active/loaded latch

### `C0:030F`

`C0:030F` is the live consumer:

- decrements `$445C`
- when it reaches zero, looks up the next byte from `$4460[2 * $445E]`
- reloads `$445C` from that next value
- calls `C0:A1F2` with the current step index
- increments `$445E`

That is much stronger evidence for a real sequencer than for generic scratch memory.

### `C0:5238`

`C0:5238` is a practical runtime anchor:

- if `$4474 != 0`, it `JSL`s `C0:030F`

So the sequencer is definitely part of an ordinary recurring overworld update path, not just one-shot transition setup.

## `C0:A1F2` as payload installer

`C0:A1F2` gives the clearest clue about what the sequencer is doing.

Local behavior:

- uses the incoming step index to select one of eight words from table `C0:A20C`
- those words are:
  - `0xB800`
  - `0xB8C0`
  - `0xB980`
  - `0xBA40`
  - `0xBB00`
  - `0xBBC0`
  - `0xBC80`
  - `0xBD40`
- treats the selected word as a WRAM source offset in bank `7E`
- uses `MVN $7E,$7E` to copy `0x00C0` bytes into destination buffer `7E:0240`
- then writes `#$08 -> $0030`

So the safest current wording is:

- `C0:A1F2` installs one of several prebuilt WRAM payload templates into buffer `7E:0240`
- the landing-profile sequencer chooses which template is active at each step

I am still keeping the exact identity of the `7E:0240` buffer open. Locally, the important point is that this is a real payload-installer step, not just a counter tick.

## Confidence boundaries

### Locally proved

- `C0:DD79` invalidates `$436E / $4370 / $5DD4`
- `C0:08CF` derives a split region byte from `$438A / $438C`
- `C0:0974` compares the derived coarse class against `$436E`
- `C0:097B` writes `$4372`
- `C0:0A95 / 0A9A` write `$436E / $4370`
- `C0:0085` reads `$4372` and indexes `EF:121B`
- `C0:023F` builds the `$445C / $445E / $4460 / $4474` sequencer block
- `C0:5238` runs `C0:030F` when `$4474 != 0`
- `C0:030F` advances the step sequencer and calls `C0:A1F2`
- `C0:A1F2` copies one of eight `7E:B800..BD40` templates into `7E:0240`

### Still open

- the exact human-facing meaning of the coarse region byte behind `$436E / $4370`
- the exact semantics of the pointed data tables at `EF:101B / 105B / 10AB / 11CB / 121B`
- the exact identity of the `7E:0240` destination buffer
- whether the sequencer is best described as a landing visual-profile sequencer, a landing environment-profile sequencer, or something slightly broader

## Best next target

The cleanest next move is to tighten the asset identity side of the already-pinned profile machinery:

- the decompressed `EF:11CB` payload contents at `7E:C000`
- the exact VRAM destination addresses used by the `EF:121B` upload entries
- the relationship between those VRAM uploads and the separate `C0:A1F2` WRAM-template installer

That should let us promote this from a structural "profile sequencer" model into a more specific local name for what kind of landing display profile is actually being installed.

## Working Names

- `C0:023F` = `Build_LandingProfileStepSequencer`
- `C0:030F` = `Advance_LandingProfileStepSequencer`
- `C0:08CF` = `Derive_LandingRegionProfileFromDestination`
- `C0:0974` = `Check_LandingRegionCacheAndMaybeRebuild`
- `C0:097B` = `Commit_LandingProfileSelector`
- `C0:0A95` = `Commit_LandingRegionClass`
- `C0:0A9A` = `Commit_LandingRegionVariant`
- `C0:5238` = `Tick_LandingProfileStepSequencerIfActive`
- `C0:A1F2` = `Copy_MapBufferPageToWorkBuffer`
