# Transition Landing Mode Family `$9F3F / $9F41` (`C0:DD53` / `C0:EA99`)

This note captures the current best local model for the small staged state family reached from the `0x19 26` snapshot path through `$98B8`.

See also [respawn-warp-target-snapshot-helper-c230f3.md](notes/respawn-warp-target-snapshot-helper-c230f3.md).
See also [saved-coordinate-reload-path-c4c718-c0b967.md](notes/saved-coordinate-reload-path-c4c718-c0b967.md).
See also [landing-destination-table-d57880.md](notes/landing-destination-table-d57880.md).
See also [landing-profile-cache-436e-4474.md](notes/landing-profile-cache-436e-4474.md).
See also [landing-profile-bundles-ef121b-43dc.md](notes/landing-profile-bundles-ef121b-43dc.md).

## Main result

The strongest current local split is now:

- `C2:30F3` snapshots saved landing coordinates plus companion byte `$98B8`
- `C2:ABFB -> C0:DD53` stages that companion byte into a smaller transition block at `$9F3F / $9F41`
- `C0:EA99` is the larger landing / arrival controller that interprets `$9F41` as a mode selector and uses `$9F3F` only on the success-side completion branch

So the safest current system-level read is:

- `$9F3F` is a small destination selector, very likely a teleport-destination-style index
- `$9F41` is a landing or arrival mode selector
- the whole family is broader than a single "respawn" path and better described as a transition-landing family

## Local staging helper: `C0:DD53`

`C0:DD53` is the first good local bridge out of `$98B8`.

Its body is tiny:

- incoming low byte `A -> $9F3F`
- caller direct-page byte `$1D -> $9F41`

That matters because it tightens the interpretation of the saved snapshot companion byte:

- `$98B8` is not just some generic pending flag
- it is used as the direct source of `$9F3F`
- and it is paired with a second one-byte mode value coming from caller state into `$9F41`

So the strongest current local wording is:

- `$9F3F` = staged destination selector
- `$9F41` = staged landing-mode selector

## Strongest evidence for `$9F3F`

### `C0:DD79`

The most useful local consumer of `$9F3F` is `C0:DD79`.

That helper:

- reads `$9F3F`
- first clears ids `1..10` in the shared `$9C08` flag bitfield through `C2:165E`
- indexes through `C08FF7`
- walks the `D5:7880` table family
- loads record words `+0x1B / +0x1D` into `$438A / $438C`
- converts those words into scaled direct-page coordinates
- invalidates cached world-side selectors `$436E / $4370` and staged destination `$5DD4` with `#$FFFF`
- then hands the scaled coordinates to `C019B2` with `Y = #$0006`

That is stronger than a plain name lookup. `D5:7880` is already locally and reference-backed consistent as the teleport-destination / town-name table family used by the text side, and `C0:DD79` is clearly using the selected record to force a fresh landing-region or landing-profile recomputation from the chosen destination.

So `$9F3F` is no longer best read as a generic transition flag. The safest current local read is a destination index in the same broad family as the teleport destination table.

### `$438A / $438C` as destination override words

The destination words loaded by `C0:DD79` are now a useful extra anchor.

Local evidence:

- `C0:DD79` is the writer that installs `$438A / $438C` from the destination table
- `C0:3A94` reads `$438A / $438C` if nonzero and uses them instead of live `$9877 / $987B` when computing context class `$9887`
- `C0:08CF` also reads `$438A / $438C`, normalizes them, and routes through larger table-driven world-side logic
- if `$438A / $438C` are both zero, these readers fall back to live current coordinates instead

So the safest current local wording is:

- `$438A / $438C` = optional destination-coordinate override words loaded from the selected destination record
- `C0:DD79` is therefore not just loading a display label payload; it is installing destination-specific coordinate state for the success-side landing path

### lifecycle reads and clears

`$9F3F` is also:

- zeroed in broad transition init at `C0:B6D2`
- checked at `C0:B76F` and `C0:B923`
- cleared again on landing completion at `C0:EBDB`

That lifecycle fits a staged destination selector much better than a passive menu field.

## Strongest evidence for `$9F41`

`$9F41` is read repeatedly across the landing controller family:

- `C0:DDEC`
- `C0:DE56`
- `C0:E455`
- `C0:E55E`
- `C0:E5F9`
- `C0:E642`
- `C0:E81D`
- `C0:E89F`
- `C0:EAC8`
- `C0:EB43`
- `C0:EB85`

These reads are not simple flag checks. They choose among multiple movement / landing profiles and completion branches.

The strongest local examples are:

- `C0:DE56` switches setup values based on whether `$9F41 == 2`
- `C0:E455` suppresses coordinate nudges when `$9F41 == 4`
- `C0:E642` uses different threshold words depending on whether `$9F41 == 2`
- `C0:E81D / E89F / EAC8 / EB43 / EB85` all branch on explicit values `1..5`

So `$9F41` is much better described as a landing-mode selector than as a simple yes/no flag.

## `C0:EA99` as the broader arrival controller

`C0:EA99` is the best current local center of gravity for the staged family.

The rough structure is:

- clear/setup shared landing state
- choose a mode branch from `$9F41`
- run one of several callback-driven or direct landing profiles
- loop until `$9F43` changes from `0`
- on completion, choose the success or failure finalizer path

The strongest current mode split is:

- mode `1` and mode `5`
  - install callback profile rooted at `C0:E28F`
- mode `2` and mode `4`
  - install callback profile rooted at `C0:E516`
- mode `3`
  - takes a shorter direct-completion path by setting `$9F43 = 1`

I am still keeping the exact gameplay names of the five modes open, but the local evidence is now good enough to say they are distinct landing/arrival modes, not just anonymous constants.

## `$9F43` as the landing result / phase byte

The controller around `C0:EA99` also tightens `$9F43`.

Best current local read:

- `$9F43 = 0` means the arrival profile is still running
- `$9F43 = 1` is the success-side completion state
- `$9F43 = 2` is the alternate failure / obstruction / fallback completion state

Why:

- `C0:EB67` loops while `$9F43 == 0`
- `$9F43 == 1` branches to `E815 -> DD79 -> E897`
- `$9F43 == 2` branches to `E9BA -> DD2C(0x000A)`

The exact wording of the failure-side state is still a little cautious, but the success-vs-alternate split is now real locally.

## Success-side branch boundary

The success path is now useful structurally even though its exact player-facing name is still open.

The strongest current local split is:

- `C0:E815`
  - landing-profile prep for the success path
- `C0:DD79`
  - destination-selector consumer, destination-coordinate override installer, and landing-region/profile reset step
- `C0:E897`
  - broader success-side landing finalizer

That ordering matters. It suggests `$9F3F` is not the variable that drives the whole movement profile. Instead, it is consumed at one specific success-side handoff point before the broader generic finalizer continues.

`C0:E897` strengthens that reading:

- mode `3` gets a shorter direct-commit path
- other modes clear/rebuild broader registry or overlay-side state
- the routine then runs a callback-driven finalizer until `$9F47 == 0`
- and only after that commits the final world coordinates through `C0400E`

So the safest current wording is:

- `$9F3F` shapes the destination-specific success-side branch
- and `C0:DD79` installs destination-specific override state from the selected destination record
- but `C0:E897` is the broader landing finalizer that is not specific to one destination label or town-name lookup

## Staged coordinate side

The same family also gives a stronger read on `$9F67 / $9F69`.

Local evidence:

- `C0:DE6F` seeds `$9F67 / $9F69` from live `$9877 / $987B`
- `C0:E455` applies one-tile directional nudges to `$9F67 / $9F69`
- `C0:E53D..E559` combines callback deltas into `$9F53 / $9F57`
- `C0:E5B5..E5BE` commits `$9F53 / $9F57 -> $9877 / $987B` when the path succeeds

So the safest current local wording is:

- `$9F67 / $9F69` = staged landing target coordinates
- `$9F53 / $9F57` = evolving candidate coordinates during the active landing profile

## How this changes the old `0x19 26` wording

The old community phrasing "set respawn coordinates" was useful but too narrow for the local helper itself.

The stronger layered model is now:

- `0x19 26 -> C2:30F3`
  - snapshot saved landing coordinates plus companion byte `$98B8`
- later `C2:ABFB -> C0:DD53`
  - turn that companion byte and a caller-side mode byte into `$9F3F / $9F41`
- `C0:EA99`
  - run the actual landing / arrival controller
- `C4:C718`
  - reload the saved coordinates as world landing position

So the safest current system-level wording is no longer just respawn point setter. It is closer to:

- transition landing target snapshot
- with one saved destination selector and one staged landing mode

## Confidence boundaries

### Locally proved

- `C2:ABFB` reads `$98B8` and passes it to `C0:DD53`
- `C0:DD53` stages low byte `A -> $9F3F` and caller byte `$1D -> $9F41`
- `$9F41` selects multiple landing profiles in `C0:EA99`
- `$9F43` is the controller result / phase byte with at least `0`, `1`, and `2`
- `$9F67 / $9F69` are staged landing coordinates
- `$9F3F` is consumed by `C0:DD79`, which indexes the `D5:7880` table family
- `C0:DD79` also installs destination-specific override words into `$438A / $438C`
- `C0:DD79` clears ids `1..10` in `$9C08` and invalidates `$436E / $4370 / $5DD4` before recomputing landing state from the selected destination
- `C0:E897` is a broader success-side landing finalizer beyond the narrow `$9F3F` lookup

### Reference-backed and locally consistent

- `D5:7880` as the teleport-destination / town-name table family
- the higher-level interpretation that this family is used by post-death respawn, scripted warp, and teleport-style landing flows

### Still open

- the exact gameplay names of landing modes `1..5`
- the exact human-facing difference between mode `1` and mode `5`, and between mode `2` and mode `4`
- whether `$9F3F` should be named simply destination id or more narrowly teleport destination id

## Best next target

The cleanest next move is to keep following the success-side branch:

- `C0:EB7B -> C0:DD79 -> C0:E897`

The key remaining question there is whether `C0:DD79` is specifically setting up named-destination arrival state, or whether it is only one narrow bookkeeping step inside a more generic landing-success path.





