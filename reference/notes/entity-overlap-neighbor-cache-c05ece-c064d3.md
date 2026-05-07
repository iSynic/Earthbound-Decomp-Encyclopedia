# Entity Overlap Neighbor Cache `C0:5ECE-C0:64D3`

This pass extends the collision/surface seam past `C0:5E82` into the entity-overlap helpers:

- `C0:5ECE`
- `C0:5F33`
- `C0:5F82`
- `C0:5FD1`
- `C0:5FF6`
- `C0:613C`
- `C0:6267`
- `C0:6478`
- `C0:64A6`

The safest current read is that this layer updates two related collision caches:

- `$28DA[slot]`: tile/surface collision status for a slot
- `$289E[slot]` and `$28CC`: entity-overlap or nearby-neighbor slot ids

The routines return `#$FFFF` when no candidate is found. Several callers also treat `#$8000` in `$289E[slot]` as a disabled or sentinel state that skips recomputation.

## Reference Anchors

`ebsrc-main` still labels these as unknown routines, but exposes two important script-side hooks:

- `EVENT_UNKNOWN_C06478` calls `UNKNOWN_C06478`.
- `EVENT_UNKNOWN_C05E76 arg1, arg2` can pass `UNKNOWN_C064A6` as a callback target, as seen in `refs/ebsrc-main/ebsrc-main/src/data/events/C3A262.asm`.

The script at `refs/ebsrc-main/ebsrc-main/src/data/events/C3A401.asm` also loops:

- `EVENT_UNKNOWN_C06478`
- then either `EVENT_UNKNOWN_C05E82` or `EVENT_UNKNOWN_C05ECE`
- then `EVENT_UNKNOWN_C0D5B0`

That makes `C0:6478`, `C0:5E82`, and `C0:5ECE` part of a repeated live entity collision/physics check in at least one event-family path.

## `C0:5ECE`: Current-Slot Collision Cache, Alternate Probe

`C0:5ECE` is script-callable through `EVENT_UNKNOWN_C05ECE`.

It validates the current slot `$1A42` through `C0:9EFF`, then probes the current `$2848/$284A` coordinate pair through `C0:5F82`. It stores `result & #$00D0` into `$28DA[current_slot]`.

If that tile collision result is zero, it calls `C0:5DE7` with the current slot's `$2D12` selector and ORs the returned terrain-compatibility bit into `$28DA[current_slot]`.

This is the same high-level cache update as `C0:5E82`, but it uses `C0:5F82` instead of `C0:5CD7` as its tile probe.

Working name:

- `C0:5ECE` -> `Update_CurrentSlotCollisionCache_FromHorizontalEdges`

## `C0:5F33` and `C0:5F82`: Half-Footprint Edge Probes

Both routines map an input slot/entity selector through `$2B6E`, use the footprint geometry tables at `C4:2A1F`, `C4:2A41`, and `C4:2AEB`, and accumulate collision bytes into `$5DA4`.

`C0:5F33` derives `$5DAC/$5DAE`, then calls:

- `C0:5639`
- `C0:56D0`

So it ORs the two vertical sides of a footprint.

`C0:5F82` derives the same style of anchor, then calls:

- `C0:5503`
- `C0:559C`

So it ORs the two horizontal sides of a footprint.

Direct callers:

- `C0:5F33`: `C0:29C6`, `C0:3FC7`, `C0:C7CA`, `C0:C7FD`, `C0:C830`, `C0:DF06`, `C0:DF16`, `C0:E1E5`, `C0:E99D`
- `C0:5F82`: `C0:4CF0`, `C0:5EF1`

Working names:

- `C0:5F33` -> `Probe_FootprintVerticalEdges`
- `C0:5F82` -> `Probe_FootprintHorizontalEdges`

## `C0:5FD1`: Center-Biased Single Tile Probe

`C0:5FD1` takes a coordinate pair, shifts it to tile coordinates, and reads one collision byte through `C0:54C9`.

The y-like input in `X` is biased by four pixels before the `>> 3` conversion:

```text
y_tile = (y + 4) >> 3
x_tile = x >> 3
```

It stores the returned byte in `$5DA4` and returns it.

Direct caller:

- `C0:466E`

Working name:

- `C0:5FD1` -> `Read_CenteredCollisionTile`

## `C0:5FF6`: Find Overlapping Entity Slot

Direct callers include front-interaction and movement-step probes:

- `C0:4152`
- `C0:4333`
- `C0:44D3`
- `C0:44F3`
- `C0:468E`
- `C0:4903`
- `C0:493D`
- `C0:4A29`
- `C0:E340`
- `C0:E59E`

The routine builds a rectangle from the caller coordinate pair and the current target slot's footprint tables. It then scans slot ids `0..16` and tests each live candidate for bounding-box overlap using:

- `$0B8E[slot]` and `$0BCA[slot]` as position-like words
- `$3366/$33A2` or `$33DE/$1A4A` as footprint dimensions, selected by `$2AF6 == 2 || 6`
- `$332A[slot]` as a nonzero collision/footprint-active gate

It skips candidates whose `$0A62[slot]` is `#$FFFF`, whose `$289E[slot]` is `#$8000`, and, when `$5D58 != 0`, candidates whose `$2C9A` looks like a high persistent/special class.

On success it stores the found slot id into `$28CC` and returns it. On failure it stores and returns `#$FFFF`.

Working name:

- `C0:5FF6` -> `Find_OverlappingEntitySlot`

## `C0:613C` and `C0:6267`: Store Per-Slot Neighbor Candidate

Both routines compute the same kind of bounding-box overlap result as `C0:5FF6`, but store the found slot id into `$289E[target_slot]`.

`C0:613C`:

- direct caller: `C0:64CE`
- skips the target slot itself
- skips reserved slot `#$0017`
- scans slots `0..29`
- stores the result into `$289E[target_slot]`

`C0:6267`:

- direct caller: `C0:64A0`
- has a two-pass scan shape
- if `$5D58 == 0`, it first scans slots `#$0018..#$001D`
- then scans slots `0..16`, skipping candidates whose `$2C9A >= #$1000`
- stores the result into `$289E[target_slot]`

The split suggests two neighbor-cache policies: `C0:613C` is the broader overlap scan, while `C0:6267` gives priority to a special high slot range before falling back to ordinary slots.

Working names:

- `C0:613C` -> `Update_SlotNeighborCache_BroadScan`
- `C0:6267` -> `Update_SlotNeighborCache_PriorityScan`

## `C0:6478` and `C0:64A6`: Script-Callable Current-Slot Wrappers

Both wrappers operate on the current slot `$1A42`.

They first check `$289E[current_slot]` against `#$8000`. If it is not disabled, they call `C0:9F08(current_slot)` to derive the current position into `$2848/$284A`, then run one of the neighbor-cache scanners with:

- `A = $2848`
- `X = $284A`
- `Y = current_slot`

`C0:6478` calls `C0:6267`. `C0:64A6` calls `C0:613C`.

Reference script context makes `C0:6478` the more visible event hook: it is called by `EVENT_UNKNOWN_C06478` in repeated event loops. `C0:64A6` appears as a callback target passed through `EVENT_UNKNOWN_C05E76` in `C3A262`.

Working names:

- `C0:6478` -> `Update_CurrentSlotNeighborCache_Priority`
- `C0:64A6` -> `Update_CurrentSlotNeighborCache_Broad`

## Open Edges

- The exact final semantic split between `$28CC` and `$289E[slot]` still needs caller-side naming. Locally, `$28CC` behaves like a single query result, while `$289E[slot]` behaves like a persistent per-slot neighbor cache.
- The high slot range `#$0018..#$001D` in `C0:6267` likely corresponds to a special actor or party/follower range, but this note keeps the label structural until the slot registry evidence is tighter.
- `$332A`, `$3366`, `$33A2`, `$33DE`, and `$1A4A` are clearly footprint/extent tables in this layer, but final field names should wait for a writer-side pass.

## Working Names

- `C0:5ECE` = `Update_CurrentSlotCollisionCache_FromHorizontalEdges`
- `C0:5F33` = `Probe_FootprintVerticalEdges`
- `C0:5F82` = `Probe_FootprintHorizontalEdges`
- `C0:5FD1` = `Read_CenteredCollisionTile`
- `C0:5FF6` = `Find_OverlappingEntitySlot`
- `C0:613C` = `Update_SlotNeighborCache_BroadScan`
- `C0:6267` = `Update_SlotNeighborCache_PriorityScan`
- `C0:6478` = `Update_CurrentSlotNeighborCache_Priority`
- `C0:64A6` = `Update_CurrentSlotNeighborCache_Broad`
- `C0:9EFF` = `Resolve_ActiveSlotPositionContext`
- `C0:9F08` = `Resolve_SlotPositionContext`
