# Collision and Surface Probes `C0:52D4-C0:5E3A`

This pass maps the next C0 audit seam:

- `C0:52D4`
- `C0:546B`
- `C0:54C9`
- `C0:5503`
- `C0:559C`
- `C0:5639`
- `C0:56D0`
- `C0:5769`
- `C0:57E8`
- `C0:583C`
- `C0:5890`
- `C0:59EF`
- `C0:5B4E`
- `C0:5B7B`
- `C0:5CD7`
- `C0:5D8B`
- `C0:5DE7`

The safest current read is:

- `C0:52D4` initializes the `$5156` trail/snapshot ring and places party followers on trailing records.
- `C0:546B` computes a sum over active party character levels.
- `C0:54C9-C0:5E3A` is the collision/surface probe layer over a 64x64 byte page at `$E000`.

This connects the snapshot work from `C0:3F1E` and `C0:4C45` to the tile-collision and surface-class helpers that movement uses every frame.

## Decoder Tooling Note

This pass added two more opcodes to `tools/decode_snippet.py`:

- `SBC long,X` / opcode `FF`
- `AND dp` / opcode `25`

Those are needed for clean local listings of `C0:5CD7`, `C0:5D8B`, and `C0:5DE7`.

## `C0:52D4`: Seed Party Trail Snapshots

Direct caller:

- `C1:BD8B`

The caller context is useful. `C1:BD7B` first calls `C0:3FA9`, then if the script byte has bit `#$0080` set, it calls `C0:52D4` with the value in `$02`.

`C0:52D4`:

1. Writes `$987D = #$00FF`.
2. Saves current player/world words:
   - `$9877`
   - `$987B`
   - `$9881`
   - `$9883`
3. Converts the caller direction with `(A + 4) & 7`, which is the opposite-facing direction.
4. Uses `C0:2D8F` and `C0:3017` to derive two per-step deltas from `$9875/$9877` and `$9879/$987B`.
5. Fills the `$5156` snapshot records backwards from index `#$00FF` toward zero.
6. Each 12-byte record receives:
   - `+0/+2`: coordinate pair
   - `+4`: `$9881`
   - `+6`: `$9883`
   - `+8`: original caller direction
   - `+A`: zero
7. Walks active party entries and assigns follower objects to trailing records.

The follower assignment is especially strong:

- `$26` starts at `#$00FF`.
- `$1C` starts at `$5156 + #$00FF * 12`.
- For each active party entry, object field `+$3D` is set to `$26`.
- Then `$26 -= #$0010` and the snapshot pointer moves back by `#$00C0`, which is exactly 16 records times 12 bytes.

So this is best understood as a party trail initializer: after a transition/position setup, it pre-populates the historical movement ring and places followers at regular intervals behind the leader.

## `C0:546B`: Active Party Level Sum

Direct caller:

- `C0:C586`

`C0:546B` loops `$98A3` party entries. For each entry:

- reads `$988B + entry`
- only accepts entries whose byte value is less than `4`
- reads `$9891 + entry` as the character selector
- maps that selector through `C0:8FF7` with stride `#$005F`
- reads byte `$99D3 + mapped_offset`
- adds it to a running total

The local layout makes `$99D3` a strong candidate for character level: it is `+$05` inside the `$99CE` party-character record, and `C0:C586` compares the returned sum against a threshold derived from `D5:9589`.

Working name:

- `C0:546B` -> `Sum_ActivePartyLevels`

## Collision Byte Addressing

The core collision byte read is:

```text
index = ((y >> 3) & #$003F) * 64 + ((x >> 3) & #$003F)
byte  = $E000[index] & #$00FF
```

That pattern is used by:

- `C0:54C9`
- `C0:5503`
- `C0:559C`
- `C0:5639`
- `C0:56D0`
- `C0:5769`
- `C0:5890`
- `C0:59EF`

So `$E000` is acting as the active 64x64 tile-collision byte page in this layer. The helpers operate on pixel coordinates, then shift by three to convert to 8-pixel tile coordinates.

## `C0:54C9`: Single Collision Tile Read

Inputs:

- `A`: x-like coordinate
- `X`: y-like coordinate

Behavior:

- reads the collision byte at `(A >> 3, X >> 3)`
- returns that byte
- if bit `#$0010` is set, stores:
  - raw `A -> $5DA8`
  - raw `X -> $5DAA`

This makes `$5DA8/$5DAA` a "last tile with bit 10" coordinate pair for this probe family.

Working name:

- `C0:54C9` -> `Read_CollisionByteAndLatchBit10Coord`

## Edge OR Helpers

The four helpers at `5503/559C/5639/56D0` OR together collision bytes along one edge of an actor footprint.

They use shape/footprint tables in bank `C4`:

- `C4:2AA7`: width count in tiles
- `C4:2AC9`: height count in tiles

Observed table values are small counts like `0`, `1`, `2`, `3`, `4`, `6`, and `8`, which fits footprint tile spans.

### `C0:5503`

Uses `$5DAE` as the fixed y coordinate, caller `A` as the x coordinate, and `C4:2AA7[shape]` as the horizontal count.

Working name:

- `OR_CollisionTopOrHorizontalEdge`

### `C0:559C`

Computes the opposite y edge with:

```text
y_tile = (($5DAE + C4:2AC9[shape] * 8 - 1) >> 3)
```

Then ORs a horizontal span of `C4:2AA7[shape]` bytes.

Working name:

- `OR_CollisionBottomOrHorizontalEdge`

### `C0:5639`

Uses `$5DAC` as the fixed x coordinate, caller `A` as the y coordinate, and `C4:2AC9[shape]` as the vertical count.

Working name:

- `OR_CollisionLeftOrVerticalEdge`

### `C0:56D0`

Computes the opposite x edge with:

```text
x_tile = (($5DAC + C4:2AA7[shape] * 8 - 1) >> 3)
```

Then ORs a vertical span of `C4:2AC9[shape]` bytes.

Working name:

- `OR_CollisionRightOrVerticalEdge`

## `C0:5CD7`: Footprint Collision Probe

Direct callers include:

- `C0:417A`
- `C0:435B`
- `C0:4A11`
- `C0:5E68`
- `C0:D127`
- `C4:339B`

Inputs are still caller-dependent, but the local body is clear enough:

- it maps the input entity/slot through `$2B6E`
- it uses the mapped footprint index to load geometry offsets from:
  - `C4:2A1F`
  - `C4:2A41`
  - `C4:2AEB`
- it derives `$5DAC/$5DAE` probe coordinates
- it dispatches an edge combination based on `$22`

The `$22` dispatch table is:

```text
1 -> C0:56D0 then C0:5503
0 -> C0:5503
3 -> C0:559C then C0:56D0
2 -> C0:56D0
5 -> C0:5639 then C0:559C
4 -> C0:559C
7 -> C0:5503 then C0:5639
6 -> C0:5639
```

It returns the accumulated `$5DA4` collision byte OR.

Working name:

- `C0:5CD7` -> `Probe_FootprintCollisionEdges`

## `C0:5D8B`: Full Footprint Collision Probe

Direct caller:

- `C0:3C56`

This is the fuller variant. It derives the same footprint anchor coordinates through `C4:2A1F`, `C4:2A41`, and `C4:2AEB`, then unconditionally runs all four edge OR helpers:

- `C0:5503`
- `C0:559C`
- `C0:5639`
- `C0:56D0`

It returns `$5DA4`.

This explains why `C0:3C4B` / `C0:3C56` can probe current-position high collision bits with a single helper call.

Working name:

- `C0:5D8B` -> `Probe_FullFootprintCollision`

## `C0:5769`: Multi-Point Surface Mask Probe

`C0:5769` takes a six-bit mask in `A`. It loops six possible sample points, using offset tables:

- `C2:00B9`
- `C2:00C5`

For each enabled sample point, it offsets `$5DAC/$5DAE`, reads a collision byte through `C0:54C9`, ORs it into an accumulated byte, and tracks whether any sampled byte had high collision bits `#$00C0`.

If `$5DB4 == 1`, it stores the ORed collision byte into `$5DA4`.

Working name:

- `C0:5769` -> `Probe_SurfaceMaskCollisionSamples`

## Follow-up: Runtime Bit Contract

The map milestone now has a machine-readable follow-up in
`notes/map-collision-runtime-bit-contract.md`.

The important refinements are:

- `C0:5769`'s six sample points decode from `C2:00B9/C2:00C5` as `(-8,0)`,
  `(0,0)`, `(7,0)`, `(-8,7)`, `(0,7)`, and `(7,7)`.
- The returned surface-sample value is a six-bit occupancy mask: result bit
  `N` is set when selected sample point `N` had `collision_byte & #$00C0`.
- Runtime high-collision tests use mask `#$00C0`, but the verified D8/`.fts`
  collision data currently uses observed bit `0x80`; bit `0x40` is supported
  by the code but absent from the verified map collision data.
- `0x10` is now a stronger special-surface coordinate-latch bit: `C0:54C9`
  writes `$5DA8/$5DAA`, and player movement consumes that latched coordinate.
- `0x04/0x08` are stronger entity terrain-compatibility class bits through
  `C0:5DE7`; `0x01/0x02` remain low modifier bits pending more caller-side
  naming.

## Surface-Class Decoders

`C0:57E8` calls `C0:5769` with mask `#$0007`.

It maps the sample result to direction/context outputs:

```text
7 or 2 -> #$FF00
0      -> #$FFFF
1      -> #$0001
4      -> #$0007
6 with ($5DAC & 7) == 0 -> #$0007
else   -> #$FFFF
```

`C0:583C` calls `C0:5769` with mask `#$0038`.

It maps:

```text
7 or 10 -> #$FF00
0       -> #$FFFF
8       -> #$0003
20      -> #$0005
30 with ($5DAC & 7) == 0 -> #$0005
else    -> #$FFFF
```

These two wrappers are the strongest local bridge between collision bytes and the class-`4` / class-`6` surface-context note. They are not generic byte reads; they interpret sampled collision patterns as a small direction/context code or a sentinel.

## `C0:5890` and `C0:59EF`: Paired Surface Resolvers

These are sibling surface decoders selected by `C0:5B7B`:

- mode `6 -> C0:5890`
- mode `2 -> C0:59EF`

Both:

- call `C0:5769` twice with a side-specific mask
- adjust `$5DAC` by four pixels for a second try when the first result is zero
- inspect two nearby high-bit collision samples
- return a direction-like value, `#$FFFF`, or a special `#$0006` / `#$0002` fallback

The two routines are mirrored:

- `C0:5890` uses mask `#$0009` and returns values around `5/7/6`
- `C0:59EF` uses mask `#$0024` and returns values around `1/3/2`

That shape fits the stair/escalator-style surface inference from the older class-`4`/class-`6` note.

## `C0:5B7B`: Movement Collision/Surface Front Door

Direct callers:

- `C0:3C08`
- `C0:460B`
- `C0:483A`

This is the high-level helper used by normal movement and special traversal modes.

It seeds:

- `$5DB8 = 0`
- `$5DB4 = 0`
- `$5DA4 = 0`
- `$5DA6 = mode`
- `$5DA2 = mode`
- `$5DAC = input y-like coordinate`
- `$5DAE = input x-like coordinate`

Then it dispatches by mode:

```text
0 -> C0:57E8
4 -> C0:583C
6 -> C0:5890
2 -> C0:59EF
1/3/5/7 -> C0:5B4E
other -> return current accumulator
```

After the mode-specific probe:

- if `$5D9A != 0`, it clears `$5DA8` to `#$FFFF`
- if the result is `#$FFFF` or `#$FF00`, it returns `$5DA4`
- otherwise it stores whether the result differs from the original mode into `$5DB8`
- stores the selected result into `$5DA6`
- returns `$5DA4 & #$003F`

So `C0:5B7B` is a collision byte plus surface-mode resolver, not just a raw tile probe.

## `C0:5DE7`: Entity-Type Terrain Compatibility Bit

Direct callers:

- `C0:29D7`
- `C0:5EBA`
- `C0:5F20`

`C0:5DE7` maps low collision bits from `A & #$000C` into a mask:

```text
0      -> 4
4      -> 2
8 / C  -> 1
```

Then it maps an entity/type selector in `Y` through `C0:8FF7` with stride `#$005E`, reads a byte from `D5:9589 + #$20 + mapped_offset`, and checks it against the mask.

Return:

- `0` when the metadata byte permits the collision mask
- `#$0080` when it does not

Working name:

- `C0:5DE7` -> `Classify_EntityTerrainCompatibility`

## `C0:5E3B-C0:5E82`: Per-Slot Collision Cache Wrappers

`C0:5E3B` probes a specific slot:

- validates it through `C0:9EFF`
- reads its facing/context from `$2AF6[slot]`
- probes current coordinates `$2848/$284A` through `C0:5CD7`
- stores `result & #$00D0` into `$28DA[slot]`

`C0:5E76` runs that for the current slot `$1A42`.

`C0:5E82` runs `C0:5E3B`, and if the collision result is zero, ORs in the entity terrain compatibility bit from `C0:5DE7`.

This makes `$28DA[slot]` a cached collision/terrain-status word for the slot.

## Working Names

- `C0:52D4` -> `Seed_PartyTrailSnapshotRing`
- `C0:546B` -> `Sum_ActivePartyLevels`
- `C0:54C9` -> `Read_CollisionByteAndLatchBit10Coord`
- `C0:5503` -> `OR_CollisionHorizontalEdgeA`
- `C0:559C` -> `OR_CollisionHorizontalEdgeB`
- `C0:5639` -> `OR_CollisionVerticalEdgeA`
- `C0:56D0` -> `OR_CollisionVerticalEdgeB`
- `C0:5769` -> `Probe_SurfaceMaskCollisionSamples`
- `C0:57E8` -> `Resolve_SurfaceMask0007`
- `C0:583C` -> `Resolve_SurfaceMask0038`
- `C0:5890` -> `Resolve_SurfaceMask0009`
- `C0:59EF` -> `Resolve_SurfaceMask0024`
- `C0:5B4E` -> `Validate_SingleSurfaceModeAgainstMask`
- `C0:5B7B` -> `Resolve_MovementSurfaceCollision`
- `C0:5CD7` -> `Probe_FootprintCollisionEdges`
- `C0:5D8B` -> `Probe_FullFootprintCollision`
- `C0:5DE7` -> `Classify_EntityTerrainCompatibility`
- `C0:5E3B` -> `Update_SlotCollisionCache`
- `C0:5E76` -> `Update_CurrentSlotCollisionCache`
- `C0:5E82` -> `Update_CurrentSlotCollisionCache_WithTerrainCompatibility`

## Open Edges

- The exact gameplay labels for the surface-mode return values are still provisional. The local class-`4`/class-`6` stair/escalator interpretation is stronger after this pass, but the final labels should wait for more caller-side behavior.
- `$E000` is clearly the active collision byte page in this code path, but the loader/populator of that page is outside this seam.
- `D5:9589 + #$20/+36` participates in both terrain compatibility and the `C0:C586` party-level comparison. The exact record-field names remain borrowed from broader class-2/metadata work rather than proved here.

## Follow-up: Entity Neighbor Cache

The neighboring `C0:5ECE-C0:64D3` layer is now mapped separately in `notes/entity-overlap-neighbor-cache-c05ece-c064d3.md`.

The main refinement is that `C0:5F33` and `C0:5F82` are half-footprint edge probes built from the same `C4:2A1F`, `C4:2A41`, and `C4:2AEB` geometry tables, while `C0:5FF6`, `C0:613C`, and `C0:6267` use bounding-box tests to find overlapping entity slots.

That makes `$28DA[slot]` the tile/surface collision cache, `$28CC` a single overlap-query result, and `$289E[slot]` a persistent per-slot neighbor or overlap cache.
