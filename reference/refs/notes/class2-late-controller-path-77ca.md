# Class2 Late Controller Path 77CA

This note captures the first ROM-first pass over the alternate late branch reached from `C2:7550` when the selected row's phase byte `+0x0E` is nonzero.

See also `notes/class2-post-selection-controller-phases.md`.
See also `notes/class2-second-stage-selector-a970.md`.
See also `notes/class2-005e-record-domain.md`.

## Why this path matters

The early `7550` pass established that row byte `+0x0E` acts like a major controller-phase selector.

This branch matters because it shows what happens after the selected row is no longer in the simple `+0x0E == 0` startup path. The code here is too large and too structured to be a mere failure case.

## Entry conditions at `C2:77CA`

Current safest reading:

- `C2:7550` jumps here immediately when selected-row byte `+0x0E != 0`
- the branch special-cases selected-row id values `0xDA`, `0xDB`, `0xDD`, and `0xE5` and returns immediately for those ids
- otherwise it calls `C2:BAC5` with requested row-state value `1`
- only when that count returns `1` does it continue into the heavier late path

That makes the path look like a controlled single-active-row late phase rather than a generic catch-all.

## Early scan over the six upstream source entries

## `9FC9` and `9FCA` now need to stay split

The newer local reads make it important not to blur these neighboring metadata bytes together.

Safest current split:

- `9FC9` = candidate class byte used by several late or row-selection helpers
  - `C2:77CA` excludes class `1` during its six-entry late claim pass
  - `C2:41B8` treats classes `1` and `2` as the permissive side of another broad helper
  - `C2:BB8D` also treats class `1` as the excluded side before one promotion branch
- `9FCA` = separate neighboring metadata byte
  - `C2:7550` requires `9FCA == 2` in its startup-side six-entry scan

So the startup and late paths are not checking the same metadata byte, and the late branch should no longer be described as though it selects `9FC9 == 1`.


The first half of the path scans the six-entry upstream source family.

Current safest reading:

- it iterates source indices `0..5` through the `0x4E`-stride candidate helper
- it requires candidate enable byte `9FB8 != 0`
- it requires candidate metadata byte `9FBA == 0`
- it excludes entries whose candidate class byte `9FC9` is `1`
- it requires marker byte `9FBB == 0`
- for each surviving source entry, it maps the linked value from `9FBC[index]` through selector `#$005F`
- if the linked `9A13` marker is still clear, it sets source byte `9FBF = 1`, marks linked table `9A15`, and sets linked table `9A13 = 1`

This is the strongest local evidence so far that the late phase performs a fresh source-entry claim or activation pass instead of only working on the already-selected row. It also corrects one older overreach in the note set: the late path is not selecting `9FC9 == 1` entries. It is selecting the complementary non-`1` candidate class side.

## Selected-row state save, replacement, and controller dispatch

After the six-entry scan, the path moves into a save-and-run pattern.

Current safest reading:

- it adds row-local contributions from `+0x3F/+0x41` into the running totals at `$A974/$A976`
- it adds row byte `+0x3D` into `$A978`
- it checks record field `+0x4E` in the selected row's `D5:9589` descriptor and returns early if that field is zero
- when `+0x4E` is nonzero, it treats that field as a selector into the paired-pointer table documented in `notes/class2-descriptor-field-4e-and-d57b68.md`
- it sets `$AA90 = 1`
- it saves the previous active-row anchors from `$A970/$A972` and the working pair `$A96C/$A96E`
- it temporarily makes the current row the active row in `$A970`
- it copies descriptor-backed fields into row words `+0x04` and `+0x08`
- it then runs the same action-builder and dispatcher pair we saw earlier: `C2:4477` followed by `C2:4703`
- it also runs additional controller helpers at `C2:3BCF`, `C2:3E32`, and later `C2:40A4`
- after the temporary active-row work, it clears `$AA90`, restores `$A970/$A972` and `$A96C/$A96E`, then runs `C2:3BCF` and `C2:3D05` again in the restored state

That makes this branch look like a nested late-phase controller pass that temporarily swaps the active row, performs action selection and dispatch, then restores the outer controller state.

## Descriptor-backed pointer dispatches in the late path

The late branch includes multiple explicit descriptor-backed pointer loads.

Current safest reading:

- one dispatch path uses the selected row's `D5:9589` record plus offset `+0x4E` as a selector into `D5:7B68`, then dispatches the first fetched pointer through `C1:DC1C`
- a second dispatch path uses the companion pointer from the same `D5:7B68` table entry and dispatches it through `C2:40A4`
- another later dispatch uses the selected row's `D5:9589` record plus offset `+0x31` and calls `C1:DC1C`

The important local conclusion is that the late phase is not just mutating state. It keeps reaching back into descriptor ROM data and emitting pointer-driven scripted or presentation work.

## `+0x4B` looks like a per-row active marker

This branch sharpens row byte `+0x4B` substantially.

Current safest reading:

- the code explicitly clears `+0x4B` across all 32 candidate rows
- it then marks the current selected row with `+0x4B = 1`
- later in the same branch, another pass can mark `+0x4B = 1` on all rows whose `+0x0C` occupancy byte is nonzero

That makes `+0x4B` look much more like a row-selection or active-membership marker than a generic unknown byte.

## `+0x0E`, `+0x0F`, and `+0x10` are getting clearer

Current safest reading:

- `+0x0E` is a major row-phase byte. `BAC5` counts rows by this value, and `7550` selects its startup path versus this late branch using it.
- `+0x0F` is a subtype or route selector inside the controller. In the startup path it decides between hardcoded script `EF:6C6B` and descriptor pointer `+0x31`. In the late branch it also decides whether the path clears or rebuilds related source-entry metadata.
- `+0x10` behaves like a linked subtype or object id. It participates in the `9A13/9A15` table updates and in the startup path can be cleared across matching rows after subtype comparison.

These are still provisional names, but they are stronger than the earlier abstract "mystery bytes" model.

## Relation to the earlier controller-phase note

This branch fits cleanly with the earlier phase model:

- `7397` installs or resets the selected row
- `7550` handles the simple startup route when `+0x0E == 0`
- `77CA` handles a later nonzero-`+0x0E` phase with nested active-row dispatch, source-entry claiming, row-marker resets, and descriptor-backed pointer work

That turns `+0x0E` into a real controller-phase discriminator instead of just another tested byte.

## What is still unresolved

Still open:

- the exact meaning of the row ids `0xDA`, `0xDB`, `0xDD`, and `0xE5` that bypass the late path
- the precise semantic meaning of descriptor field `+0x4E` beyond the now-solid selector role
- what the helper pair `C2:3BCF` / `C2:3D05` contributes relative to the already-known `4477` / `4703` action dispatch pair
- how to name the first `D5:7B68` pointer more precisely, even though the second pointer now has a good reference-backed battle-action clue through `C2:40A4`

## Current safest takeaway

The safest current takeaway is:

- `77CA` is a real late controller phase, not a failure stub
- row byte `+0x0E` is now strongly supported as a major controller-phase byte
- row byte `+0x4B` is best read as an active-membership or selected-row marker
- the late phase continues to use descriptor-backed pointers and source-entry bookkeeping after the initial selection work

That gives us a much stronger foundation for naming the selected-row controller end to end.

## Best next target

- See `notes/class2-descriptor-field-4e-and-d57b68.md` for the new selector-table pass. The best next move is to trace the second-pointer consumer at `C2:40A4`, or inspect concrete `D5:7B68` second-pointer targets like `C2:9039`, `C2:9556`, and `C2:A821`, so the paired table can be named from behavior instead of just from structure.
