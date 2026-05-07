# Overworld Companion Family Priority (`C0:1CA8`, `C0:A4C4`, `C0:A794`, `C0:A6E3`)

This note is a focused follow-up on the companion visual/entity family behind the observed `40xx/41xx/42xx` VRAM destinations during overworld walking.

See also [overworld-walking-stutter-producer-split-c01558-c01ca8.md](notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md).
See also [rom-patch-overworld-stutter-plan.md](notes/rom-patch-overworld-stutter-plan.md).
See also [overworld-timing-scroll-commit-slice-c08b20-c08284.md](notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md).

## Working Names

- `C0:1CA8` = `Upload_CompanionVisualTiles4000Band`
- `C0:A4C4` = `RefreshSlotVisualProfileShared`
- `C0:A56E` = `Generate_RenderDmaStripDescriptors`
- `C0:A6E3` = `WatchAndRefreshCompanionVisualPhase`
- `C0:A6F7` = `RefreshCompanionVisualOnSignatureChange`
- `C0:A750` = `RefreshCompanionVisualOnWatcherRerun`
- `C0:A78F` = `RefreshCompanionVisualDirectWrapper`
- `C0:A794` = `RefreshCompanionVisualProfile_PhaseBiased`
- `C0:AAA8` = `ScriptRefreshCompanionVisualProfile_PhaseBiased`
- `C0:AAB1` = `ScriptRefreshCompanionVisualProfile_CurrentSlot`

## Main result

The companion `40xx/41xx/42xx` family is still a real contributor, but the best current patch target inside it is narrower than "all of `A4C4/A794`" and broader than the already-failed timer-only gate.

The healthiest current ranking is:

1. `C0:A794` movement-time reruns, especially through `C0:A6E3..A753`
2. `C0:A4C4` as the simpler sibling producer
3. `C0:1CA8..1D37` as the narrow direct uploader

The biggest practical refinement from this pass is:

- `A794` has only five direct local callers
- two of those (`A6F7` and `A750`) are the already-proved watcher or cadence path at `A6E3..A753`
- the timer-only sub-branch inside `A6E3` was safe to gate but did not help visibly
- that makes the broader `A6E3` watcher path, not just its timer-expiry leg, the strongest remaining companion-side patch seam

So the safest current read is no longer "the timer-only `A794` rerun is the fix." It is:

- the companion lane still matters
- `A794` is still its most promising patch seam
- but the dominant residual cost likely comes from ordinary movement-time `A794` reruns plus the strip family together, not from the timer-only branch alone

## Locally proved

### `C0:1CA8..1D37` is a narrow direct uploader into the companion VRAM band

`C0:1CA8` computes a bounded chunk size and uses:

- source base `C4:0BE8`
- tile-base table `C4:2F8C`

Then it issues two `TRANSFER_TO_VRAM` calls:

- first with `+ $4000`
- second with `+ $4100`

The second add decodes awkwardly in mixed-width mode, but the structure is still clear from the paired `JSL C08616` sites at `1CFC` and `1D15`.

This makes `1CA8` a clean direct source for at least the `4040/41xx` part of the observed family.

### `C0:A4C4` is the simpler descriptor producer

`A4C4` consumes the already-seeded per-entry descriptor state:

- `$2ABA` -> transfer count
- `$2A7E` -> transfer size
- `$298E` -> VRAM base
- `$2A06/$29CA` -> descriptor stream
- `$2AF6` -> variant selector through `DATA_C0A60B`
- optional extra bias through `$2892`
- optional auxiliary prepasses through `$2BAA`

Then it caches the raw descriptor header into `$341A,Y` and emits descriptors through `A56E -> 8643`.

Direct callers are only:

- `C0:A4A2`
- `C0:AA8B`

That remains a good safety property, but this path now looks more static and less likely to be the main residual walking-time amplifier.

### `C0:A794` is the stronger movement-time amplifier

`A794` consumes the same core seeded state, but differs in the dynamic selector side:

- active entry comes from `$2896`
- variant source is `DATA_C0A623[$2AF6]`
- descriptor pointer is further biased by `$10F2,Y`

Then it caches the raw descriptor header into `$341A,Y`, seeds the main source bank from `$2A42,Y`, and emits descriptors through `A56E`.

Direct local callers are only:

- `C0:A6F7`
- `C0:A750`
- `C0:A78F`
- `C0:AAA8`
- `C0:AAB1`

That is a narrow and promising caller set.

### `C0:A6E3..A753` is the main movement-time watcher path into `A794`

`A6E3` does several things in sequence:

- stores the active entry index into `$2896`
- builds a composite signature from `$2C22` high byte plus `$2AF6`
- compares it against `$3456`
- reruns `A794` immediately on signature change
- otherwise follows several side branches:
  - sign-bit clearing on `$1002`
  - `$10F2` clearing when `$1002 & $2000` is set
  - cadence countdown on `$0ED6`
  - reload from `$0F12`
  - `EOR #$0002` on `$10F2`
  - optional `ABE0` side effect under the `$2898/$289A/$289C` checks
- then calls `A794` again at `A750`

So the important structural fact is:

- `A6E3` is not only a timer path
- it is the broader watcher path that decides when movement or cadence state should rerun `A794`

### The timer-only branch is real, but insufficient by itself

The existing patch experiment on the timer-only branch at `A723..A750` was stable and safe, but the user reported no meaningful microstutter improvement.

That gives a strong negative result:

- timer-only reruns are not the dominant visual hitch source on their own

But that does not clear `A794` as a whole. It only clears one narrow leg of the broader watcher path.

### `A56E` page splitting is a real amplifier, but still a poor first patch seam

`A56E` can turn one logical companion update into:

- one descriptor when no page crossing occurs
- two descriptors when the VRAM destination crosses a `0x0100` page boundary

That is a plausible multiplier on companion-side pressure.

But it is still a shared helper under both `A4C4` and `A794`, so it remains a worse first patch seam than the producer-side watcher path.

## Ref-backed and locally consistent

### Why `A794` still looks more promising than `A4C4`

The current local and ref-backed reasons are:

- it has more dynamic selector state than `A4C4`
- it is tied directly to the cadence watcher at `A6E3`
- it can rerun even when the base descriptor-source fields are unchanged enough to keep the scene looking similar
- it is already using the existing header cache field `$341A`

So even after the failed timer-only gate, `A794` is still the best current companion-side patch candidate.

### Why `1CA8` is still secondary

`1CA8` is attractive because it is narrow and directly in the `0x4000+` family, but it now looks more like a direct uploader sibling than the main recurring movement-time amplifier.

The stronger current read is:

- `1CA8` proves the family is real
- `A794` is likelier to explain the residual repeated work under ordinary walking

## Still uncertain

### Which `A794` caller mix dominates during ordinary diagonal walking

The current strongest structural statement is:

- `A6E3` is the key movement-time watcher path
- `AAA8/AAB1` and `A78F` look narrower and more wrapper-like

But I have not yet externally sampled `8677` by immediate caller in a way that cleanly separates:

- `A6E3/A750`-driven reruns
- `A78F` direct wrapper calls
- script-side `AAA8/AAB1` uses

### Whether a broader `A6E3` gate would help enough to matter

The timer-only gate did not matter by itself.

What remains uncertain is whether a broader compare over the `A6E3`-driven rerun cases would materially reduce visible hitch without under-updating the companion visual layer.

## Practical patch implications

### Best next companion-side experiment

The next companion-side experiment should probably be:

- not another timer-only gate
- not a shared-helper patch at `A56E/8643`
- but a broader `A6E3` watcher-side gate over `A794` reruns

The healthiest first compare tuple still looks like a derived-output signature, not a single field:

- `$341A` raw descriptor header
- `$298E` VRAM base
- `$2A7E` transfer size
- `$2ABA` transfer count
- `$2A42` source bank
- effective selector derived from `$29CA + 4*DATA_C0A623[$2AF6] + $10F2`
- optional auxiliary-prepass enable from raw-header bit `1` plus `$2BAA` bits `3/2`

That would be a real `A794`-side identity check, not the weaker timer-only shortcut.

### Why not jump to that patch immediately

The broader timing work in [overworld-timing-scroll-commit-slice-c08b20-c08284.md](notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md) weakened both the missed-movement-update and missed-publish theories.

So the companion family still looks real, but the remaining hitch now looks more like aggregate presentation workload than one obviously redundant rerun.

That means a broader `A6E3/A794` gate is still plausible, but it no longer looks certain enough to write before another round of caller-family attribution.

## Bottom line

The companion family still matters, but the latest narrowing changes how to think about it:

- `1CA8` proves the family reaches the `0x4000+` VRAM band directly
- `A4C4` is the simpler descriptor producer
- `A794` is still the strongest movement-time amplifier
- `A6E3` is the real watcher path to care about
- the timer-only `A6E3` branch was safe but not impactful enough

So if we return to a companion-side patch, the best current seam is a broader `A6E3 -> A794` rerun gate, not another timer-only experiment and not a shared queue-helper patch.
