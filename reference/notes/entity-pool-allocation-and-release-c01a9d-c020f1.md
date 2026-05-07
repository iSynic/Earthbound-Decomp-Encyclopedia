# Entity Pool Allocation and Release `C0:1A9D..20F1`

This note follows the next seam after `early-entity-map-reset-family-c019e2-c01a86.md`: the byte pool and slot-reservation helpers used by `C0:1E49` and the entity release paths.

Reference status:

- `ebsrc-main` gives `C0:1A9D` the useful symbol `FIND_FREE_7E4682`.
- `ebsrc-main` gives `C0:1C11` the useful symbol `ALLOC_SPRITE_MEM`.
- `C0:1B15`, `C0:1B96`, `C0:1C52`, and `C0:20F1` are still `UNKNOWN_...` in `ebsrc-main`.
- The legacy Asar tree confirms the same control flow and table names like `DATA_C40BE8`, `DATA_C42B0D`, `DATA_C42F8C`, and `DATA_C4303C`, but not higher-level semantics.

## Working Model

There are two cooperating allocation layers:

- `$467E..49FD` is a byte-backed visual/entity record pool. Records are written in 5-byte chunks, and pointer-like owners store `7E:467E + offset`.
- `$4A00..4A57` is a compact slot-ownership bitmap or reservation map. Each byte is either `0`, a low slot id, or a slot id with bit 7 set.

The main allocation path is:

1. `C0:1DED` reads the `EF:133F` pose descriptor and seeds `$467A/$467C`.
2. `C0:1C52` reserves enough `$4A00` space for the visual span and uploads missing `0x4000/0x4100` VRAM chunks from `C4:0BE8`, using offsets from `C4:2F8C`.
3. `C0:1A9D` finds a free run in `$467E..49FD` for the 5-byte visual records.
4. `C0:1D38` writes those 5-byte records into `$467E..`.
5. `C0:1E49` stores the allocated byte-pool pointer into `$112E,Y` and bank `#$007E` into `$116A,Y`.
6. `C0:1B15` and `C0:1C11` are the matching release-side helpers.

## `C0:1A9D` / `FIND_FREE_7E4682`

Input:

- `A` = requested byte count

Output:

- `A` = offset into `$467E` on success
- `A = #$FF01` if no candidate free byte is found before `0x380`
- `A = #$FF02` if the candidate run would overflow the pool

The routine scans `$4682 + X` in steps of 5. Since `$4682` is `4` bytes after the pool base `$467E`, the probe byte is the last byte of each 5-byte record. A value of `#$FF` means free.

Once it finds a candidate record, it checks a contiguous byte run of caller-requested length. Any occupied probe byte inside that run forces the scan to resume at the next 5-byte boundary. That makes this a first-fit allocator over 5-byte record units, despite the requested size being a byte count.

Only direct code caller found:

- `C0:1EE9`, inside `C0:1E49`

The request size in that call is derived from the selected secondary descriptor:

```text
record_count = descriptor[0]
requested_bytes = record_count * 10
```

That matches `C0:1D38`, which writes two passes of 5-byte records.

## `C0:1B15`

Input:

- `A` = pointer into `$467E..49FE`, normally loaded from `$112E,Y`

Behavior:

- rejects pointers below `$467E`
- accepts pointers up to `$49FE`
- converts the pointer to a pool offset
- clears records to `#$FF`
- follows bit 7 of the fifth byte to decide when a record run ends
- repeats for at most two runs

The record clear writes `#$FF` to:

- `$467E + offset`
- `$467F + offset`
- `$4680 + offset`
- `$4681 + offset`
- `$4682 + offset`

The fifth byte is saved before clearing, then `saved_byte & #$80` decides whether the current run is finished. This means bit 7 of record byte `+4` is an end-of-run marker.

Direct callers:

- `C0:2105`, in `C0:20F1`
- `C0:2153`, in `C0:2140`

So `C0:1B15` is the byte-pool release helper for both script-triggered and full entity release.

## `C0:1B96`

Input:

- `A` = span length
- `X` = slot id or owner byte

Output:

- start index into `$4A00` on success
- `A = #$FF03` if no contiguous span is available

Behavior:

- scans `$4A00..4A57`
- searches for `A` consecutive zero bytes
- writes `X | #$80` into the reserved span

Direct caller:

- `C0:1C81`, inside `C0:1C52`

This looks like a companion reservation layer for VRAM/tile span ownership. It does not allocate the `$467E` record bytes directly; it reserves a compact span first, then `C0:1C52` uses that span to drive upload work.

## `C0:1C11` / `ALLOC_SPRITE_MEM`

Inputs:

- `A` = slot id, or `#$FFFF`
- `X` = replacement byte to write into matching entries

Behavior:

- scans all `$4A00..4A57` entries
- if `A != #$8000`, it compares each entry against `(A & #$00FF) | #$0080`
- matching entries are replaced with low byte of `X`
- if `A == #$8000`, it writes low byte of `X` over every entry

This is better described as a `$4A00` reservation rewrite/free helper than as allocation in the modern sense. The reference name `ALLOC_SPRITE_MEM` is still useful as a clue that this table is sprite/entity visual memory ownership, but locally the behavior is "rewrite reservations for owner".

Direct callers:

- `C0:1F68`, from the special `C0:1E49` path
- `C0:210E`, from `C0:20F1`
- `C0:215C`, from `C0:2140`
- `C0:B547` and `C0:B695`, broad scene initialization paths
- `C4:D9A3` and `EF:E1A8`, still pending caller-context reads

## `C0:1C52`

Inputs from `C0:1E49`:

- `A = $467A`, derived from high nibble of pose descriptor byte `+1`
- `X = $467C`, derived from pose descriptor byte `+0`
- `Y = caller-supplied slot/owner value`

Behavior:

- rounds width-like inputs up to even values
- calls `C0:9032`, then divides by 4 to get a span length
- calls `C0:1B96` to reserve a `$4A00` span
- if the reservation succeeds and the rounded inputs differ from original inputs, uploads chunks from `C4:0BE8`
- uses `C4:2F8C` offsets plus `#$4000` and `#$4100` as VRAM destinations
- returns the `$4A00` reservation start index, or an error code propagated from `C0:1B96`

This strengthens the previous walking-stutter finding: `C0:1CA8..1D37` is not an incidental uploader, it is the tile-memory fill path paired with the `$4A00` reservation map.

## `C0:1D38`

This helper writes the actual 5-byte records into the `$467E` pool.

For each source record:

- byte `+0` copies from the secondary descriptor stream
- byte `+1` comes from `C4:303C`
- byte `+2` combines:
  - high byte of `C4:303C`
  - caller `Y` low bit or flag
  - descriptor byte `+2` with bit 0 cleared
- bytes `+3/+4` copy from descriptor bytes `+3/+4`

It loops in two passes, matching the release helper's "up to two runs" behavior.

## `C0:20F1`

`C0:20F1` is now worth separating from `C0:2140`.

Behavior:

- reads current slot id from `$1A42`
- releases the slot's `$467E` byte-pool pointer through `C0:1B15`
- rewrites/frees the slot's `$4A00` reservations through `C0:1C11`
- decrements `$4A5C` if `$2C9A,Y & #$F000 == #$8000`
- clears `$4A60` if `$2D12,X == #$00E1`
- writes `#$FFFF` to `$2CD6,X` and `$2C9A,X`
- returns without calling `C0:9C35`

By contrast, `C0:2140` performs the same local release steps and then calls `C0:9C35`, which performs the broader task-slot/entity cleanup. So `C0:20F1` looks like a script-facing partial release for the current entity slot, while `C0:2140` is the full release path.

Reference corroboration:

- `ebsrc-main/include/eventmacros.asm` defines `EVENT_UNKNOWN_C020F1` as a script call to `UNKNOWN_C020F1`.
- Several `refs/ebsrc-main/src/data/events/...` scripts use that macro.
- `find_xrefs.py C020F1` reports raw 24-bit script pointer hits in `C3`, `C4`, and several later event banks rather than ordinary JSL callers.

## Working Names

Suggested local names from this pass:

- `C0:1A86` = `Reset_EntityBytePool467E`
- `C0:1A9D` = `Find_FreeEntityBytePoolRun467E`
- `C0:1B15` = `Release_EntityBytePoolRun467E`
- `C0:1B96` = `Reserve_VisualMemorySpan4A00`
- `C0:1C11` = `Rewrite_VisualMemoryReservations4A00`
- `C0:1C52` = `ReserveAndUpload_EntityVisualTiles`
- `C0:1D38` = `Build_EntityVisualRecords467E`
- `C0:1DED` = `Read_SpritePoseVisualDescriptor`
- `C0:20F1` = `ScriptRelease_CurrentEntityVisualState`
- `C0:2140` = `Release_EntitySlotAndVisualState`

These names are intentionally a little verbose until the exact gameplay term for the `$4A00` reservation map is proven.

## Remaining Checks

- Decode the `C4:D9A3` and `EF:E1A8` callers of `C0:1C11`.
- Decode the script contexts that invoke `EVENT_UNKNOWN_C020F1`; this should reveal whether `C0:20F1` is tied to temporary event NPC cleanup, floating sprites, or a broader "delete current actor visuals" operation.
- Tighten the field names for the 5-byte `$467E` record by pairing `C0:1D38` writers with the later consumers of `$112E/$116A`.
- Decide whether the borrowed name `ALLOC_SPRITE_MEM` should be preserved as an alias for `C0:1C11`, or replaced locally by the observed reservation-rewrite behavior.
