# Context Class `3` and Traversal Mode `#$000A`

This note captures the strongest current local read for the special `$9887 == 3` branch.

See also [position-derived-visual-context-class-9887.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/position-derived-visual-context-class-9887.md).
See also [visual-selector-family-c0780f-c3f2b5.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/visual-selector-family-c0780f-c3f2b5.md).

## Main result

A useful gameplay-facing interpretation finally surfaced.

The strongest current local read is:

- context class `3` is very likely a doorway or transition-cell class
- that class seeds traversal mode `$9883 = #$000A`
- the resulting branch immediately consults `EB_DoorDestinationTable` through `C068F4`
- and uses the resolved destination-side music/context values during the special traversal path

That is materially better than the older wording that only called class `3` an alternate bucket family.

## Why class `3` now looks doorway-related

The cleanest local chain is:

1. `C03A94` derives `$9887` from the position-based `C00AA1` lookup.
2. If `$9887 == 3`, it sets `$9883 = #$000A`.
3. Later, the class-`3` special path runs through `C03CFD`.
4. `C03CFD` calls `C06A07` when `$5D9A` is clear.
5. `C06A07` immediately calls `C068F4` with the live player position.
6. `C068F4` explicitly uses `EB_DoorDestinationTable` and resolves destination-side data into `$5DD6` and nearby fields.

That is very hard to reconcile with an ordinary terrain-only surface.

It fits naturally with a doorway or transition-cell interpretation.

## The strongest door-table clue

Inside `C068F4`:

- the code installs `EB_DoorDestinationTable` as the active table base
- it uses position-derived indexing through `DATA_DCD637` and `DATA_CF58EF`
- then it stores the resolved result into fields like `$5DD6`

The legacy disassembly already names that table `EB_DoorDestinationTable`, and the local control flow matches that naming well enough to treat it as a strong reference-backed clue rather than a blind borrowed label.

## Why `$9883 = #$000A` now looks like a doorway-transition mode

The class-`3` branch is not just setting a cosmetic value.

`C03CFD` does all of this when `$9883 == 3` in that local branch family:

- calls `C4FD45` with `#1`
- optionally calls `C06A07`, which resolves door-destination context/music
- clears `$9887`, `$9883`, `$9A0B`, and `$987D`
- rebuilds visual/setup state through `C01E49`
- updates entity/state bits around `7E:1032` and sometimes `7E:10E6`
- refreshes the player-side visual family again with `C0A780`

That looks like a real transition-mode handoff, not a tiny movement tweak.

So the safest current statement is:

- traversal mode `#$000A` is very likely the doorway-transition mode used when the player is in context class `3`

## Why music/context refresh matters

A particularly nice clue is the `ebsrc` include naming around this same region.

The newer split project includes this area under names like:

- `unknown/C0/C068F4.asm`
- `overworld/change_music_5DD6.asm`
- `unknown/C0/C06A07.asm`

Even without relying on that source as ground truth, the naming lines up well with the local ROM behavior:

- `C06A07` calls `C068F4`
- then loads `$5DD6`
- then dispatches it through the music/audio helper family

So the current read that this branch is doorway-transition-related is stronger than a pure visual guess.

## How this updates the class model

The current best local class wording is now:

- class `3` = doorway / transition-cell context
- class `4` and class `6` remain smaller special context classes with direct pose overrides, still unnamed

I am still keeping the exact player-visible wording slightly cautious because the same class may cover more than one kind of door-like transition tile, such as map-entry cells, doorway thresholds, or closely related transfer tiles.

## Best next target

The best next move is to tighten class `4` and class `6` the same way, or to follow the exact `EB_DoorDestinationTable` fields that `C068F4` reads into `$5DD6`, `$5DD8`, and nearby state. That should tell us whether class `3` is specifically doors, a wider transition family, or a door-plus-stairs grouping.
