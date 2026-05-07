# Class2 Descriptor Field 4E And D5 7B68

This note captures the first ROM-first interpretation of descriptor field `+0x4E` and the secondary ROM table rooted at `D5:7B68`.

See also `notes/class2-late-controller-path-77ca.md`.
See also `notes/class2-005e-record-domain.md`.
See also `notes/class2-d57b68-battle-action-table-match.md`.

## Why this field matters

The late selected-row controller at `C2:77CA+` repeatedly reaches into descriptor field `+0x4E`.

That field is important because it is the clearest bridge yet from the `D5:9589` descriptor records into a second structured ROM table that carries two distinct pointer payloads.

## `+0x4E` behaves like a selector, not a direct pointer

Current safest reading from the `C2:78B8+` path:

- bank `C2` maps the selected row's descriptor id through stride `#$005E`
- it reads descriptor field `+0x4E` as a 16-bit value
- if that value is zero, the late path returns early
- otherwise bank `C2` treats the value as a selector into another ROM table rooted at `D5:7B68`

The important behavioral point is that `+0x4E` is not consumed like the direct pointer fields `+0x2D` or `+0x31`. It drives a second table lookup.

## `D5:7B68` behaves like a 12-byte action-descriptor table

The strongest local evidence is the arithmetic in the late path:

- after loading field `+0x4E`, the code computes `selector * 12 + 4`
- it uses that offset relative to `D5:7B68` to load one 32-bit pointer
- it also computes `selector * 12 + 8`
- it uses that offset relative to `D5:7B68` to load a second 32-bit pointer

That is strong local evidence that `D5:7B68` is a 12-byte record table. The newer cross-check in `notes/class2-d57b68-battle-action-table-match.md` tightens the front half of the layout further:

- `+0x00`: action direction byte
- `+0x01`: action target byte
- `+0x02`: action type byte
- `+0x03`: cost byte
- `+0x04`: first 32-bit pointer
- `+0x08`: second 32-bit pointer

That byte-level interpretation is still marked as an inference supported by the `ebsrc` reference tree, but it now fits the local ROM entries unusually well.

## The two pointers go to two different dispatcher families

Current safest reading from `C2:7950+` and `C2:79A0+`:

- the first pointer from `D5:7B68 + selector * 12 + 4` is copied into `$0E/$10` and dispatched through `C1:DC1C`
- the second pointer from `D5:7B68 + selector * 12 + 8` is copied into `$0E/$10` and dispatched through `C2:40A4`

That means the `D5:7B68` records carry a paired payload, not just a single script target.

The safest interpretation is that the first pointer is a script or presentation pointer, while the second pointer is a companion action or behavior payload used by a different consumer family. The newer local read on `C2:40A4` sharpens that second half: it now looks like a fixed payload pointer applied once per bit-selected target after `C2:3D05` installs target context. A useful reference-backed clue strengthens the same read: in the `ebsrc` side project, `C2:40A4` is called from battle paths like `ko_target.asm` and `pray.asm`, and `pray.asm` passes it a named `BTLACT_DEFENSE_DOWN_A` pointer. That does not prove the exact naming in our ROM-first notes, but it is strong evidence that the second pointer behaves like battle-action payload data rather than like passive data. See `notes/class2-second-pointer-consumer-40a4.md` for the focused consumer analysis.

## Sample table shape at `D5:7B68`

Representative entries from the table look like this:

- index `0x0000`: bytes `(1, 0, 0, 0)`, first pointer `C7:7EFF`, second pointer `C2:9039`
- index `0x0004`: bytes `(0, 1, 1, 0)`, first pointer `EF:848C`, second pointer `C2:859F`
- index `0x000A`: bytes `(0, 4, 3, 10)`, first pointer `EF:8543`, second pointer `C2:9556`
- index `0x0012`: bytes `(0, 1, 3, 4)`, first pointer `EF:8543`, second pointer `C2:9647`

Those byte patterns now line up cleanly with the battle action enums in the `ebsrc` reference tree: `direction`, `target`, `type`, and `cost`. The repeating `EF:8543` first pointer across many PSI-shaped entries, combined with varying second pointers in bank `C2`, is especially strong because the reference battle action table likewise reuses a common PSI message pointer while varying the action handler.

A few concrete second-pointer targets strengthen that reading from local bytes alone:

- `C2:9556`, `955F`, `9568`, and `9571` are the early all-target PSI wrapper quartet, converging on `C2:9516`
- `C2:95AB`, `95B4`, `95BD`, and `95C6` are the early row-target PSI wrapper quartet, converging on `C2:957A`
- `C2:9647`, `9650`, `9659`, and `9662` are the early one-target PSI wrapper quartet, converging on `C2:95CF`
- `C2:9871`, `987D`, `9889`, and `9895` are the early Thunder wrapper quartet, converging on the larger two-parameter helper `C2:966B`
- `C2:A821` is likewise a compact wrapper over a nearby shared helper with a fixed constant

Those targets read much more like parameterized action-entry routines than like static data pointers, and the early quartets now line up strongly with the canonical Rockin, Fire, Freeze, and Thunder PSI families in the reference action-table order.

## Relation to descriptor records at `D5:9589`

The `D5:9589` scan now suggests a useful split between three pointer-like layers:

- `+0x2D`: direct textbox or script-data pointer
- `+0x31`: direct script or presentation pointer used in the startup selected-row path
- `+0x4E`: selector into the paired-pointer table at `D5:7B68` used in the late selected-row path

That makes `+0x4E` the first strong sign that some descriptor behavior is mediated through a second-level action-set table rather than through direct per-record pointers alone.

## What `+0x54` appears to be doing nearby

The same late path also reads descriptor byte `+0x54` and copies it into selected-row byte `+0x08` before running the `4477` and `4703` action-builder and dispatcher pair.

Current safest reading:

- `+0x54` is not part of the `D5:7B68` selector itself
- it looks more like a local late-phase parameter paired with the `+0x4E` action-set selection

That is still provisional, but it is a better fit than treating `+0x54` like another raw pointer.

## Caveat about outliers

Most descriptor records have `+0x4E = 0`, and the records that clearly use the late path have small selector values that fit the `selector * 12` interpretation cleanly.

There are also a few outlier `+0x4E` values later in the scanned record region that do not fit the table cleanly. The safest current explanation is either:

- not every stride-`0x5E` slot in the larger region belongs to the same actively used descriptor family, or
- some tail entries use an alternate encoding that we have not verified yet

So the selector interpretation is strongest for the descriptor records we have actually traced through the late controller path.

## Current safest takeaway

The safest current takeaway is:

- descriptor field `+0x4E` is a late-phase selector into `D5:7B68`
- `D5:7B68` is best read as a 12-byte paired-pointer table
- the table supplies one pointer to `C1:DC1C` and a second pointer to `C2:40A4`
- the best current cross-checked guess is now stronger: the first pointer behaves like a battle message or presentation pointer, while the second behaves like a battle action handler pointer
- descriptor byte `+0x54` looks like a companion late-phase parameter rather than another direct pointer

That is enough to move this subsystem from "late phase loads some extra data" to "late phase selects a structured action-set entry with two coordinated payload pointers."

## Best next target

- trace the second-pointer consumer at `C2:40A4` more directly, or tighten what the shared helper families behind targets like `C2:9556` and `C2:A821` are parameterizing, because that should tell us exactly what kind of battle-action-like payload the paired table is driving.
