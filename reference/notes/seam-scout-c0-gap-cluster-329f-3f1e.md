# Seam Scout: Audit Gap Cluster `C0:329F`, `C0:3C25..3F1E` (2026-04-24)

This is a focused seam-scout write-up for the audit-led `C0` gap cluster:

- `C0:329F`
- `C0:3C25`, `C0:3C4B`
- `C0:3DAA`
- `C0:3E25`, `C0:3E5A`, `C0:3E9D`, `C0:3EC3`
- `C0:3F1E`

It is intended to be **byte-evidence + call-graph + reference corroboration** you can hand to a decompiler without re-doing discovery.

Existing context notes (useful background, not duplicated here):

- `notes/character-affliction-clear-c0329f.md`
- `notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md`

## Executive seam recommendation

If you only pick *one* seam to decompile next from this cluster, pick:

- `C0:3EC3` (and its tight helper chain `C0:3E9D -> C0:3E5A`, plus `C0:3E25` for the “previous registry entry” lookup).

Reasons:

- Has multiple **direct `JSL` callers** across `C0` and `EF` (easy to validate).
- Has a **self-contained predicate**: compares a measured “order delta” against a target and flips a single bit (`#$1000`) in a per-slot word table rooted at `$7E:1002`.
- Its return value is immediately stored into object field `+$3D` in multiple call sites.

## Corroboration anchors (refs/)

`ebsrc-main` corroborates that each address is a distinct exported seam (still `UNKNOWN_...`), and that:

- `C0:3DAA` and `C0:3F1E` are used as `EVENT_CALLROUTINE` targets:
  - `refs/ebsrc-main/.../src/data/events/scripts/002.asm` uses `EVENT_UNKNOWN_C03DAA`
  - `refs/ebsrc-main/.../src/data/events/scripts/068.asm`, `069.asm`, `070.asm` use `EVENT_UNKNOWN_C03F1E`
- `earthbound-disasm-legacy` contains labeled bodies for `C0:3C25`, `C0:3DAA`, `C0:3E5A`, `C0:3E9D`, `C0:3EC3` (but notably not `C0:3C4B` / `C0:3E25` / `C0:3F1E`).

WRAM naming corroboration:

- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/RAM_Map_EB.asm` defines:
  - `$7E:9877` = `Player_XPosLo`
  - `$7E:987B` = `Player_YPosLo`
  - `$7E:987F` = `Player_FacingDirection`

## `C0:329F` — clear 7-byte status group in a `$005F`-stride record

Suggested cautious name:

- `Clear_CharacterAfflictionBytes` (see the dedicated note for rationale)

Byte evidence (prologue + stride multiply + 7-byte clear loop):

- Entry at `C0:329F`: `C2 31 0B 48 7B 69 EE FF 5B 68` (REP/DP-frame pattern)
- Stride-multiply call: `A0 5F 00 22 F7 8F C0` (sets `Y=#005F`, `JSL C0:8FF7`)
- Clear byte 0: `E2 20 9E DC 99` (8-bit A; `STZ $99DC,X`)
- Loop clear: computes `X = ($99DC + (A*#$005F) + i)` then `A9 00 9D 00 00`

Direct callers:

- none found via direct `JSL/JSR` scan

Indirect reference evidence:

- `find_xrefs` finds **raw 16-bit word** hits for `#$329F` (likely bank-implied pointer tables), no `JSL` hits.

Remaining uncertainty:

- The *calling convention* for the “record selector” input (what domain the input `A` ranges over) is still inferred from surrounding registry code, not proven by a direct `JSL` caller.

## `C0:3C25` — guarded refresh using current player position

Suggested cautious name:

- `Refresh_DestinationContextIfPositionChanged`

Byte evidence (entire body is short; key calls and predicate):

- Entry at `C0:3C25`: `C2 31 A9 01 00 8D DA 5D` (sets `$5DDA=1`)
- Uses player position: `AE 7B 98` / `AD 77 98` (loads `$987B` and `$9877`)
- Calls position-based helper: `22 F4 68 C0` (`JSL C0:68F4`)
- Compares `$5DD6` vs `$5DD4`, and on change calls:
  - `22 56 87 C0` (`JSL C0:8756`)
  - `22 AF 69 C0` (`JSL C0:69AF`)
- Exit: `9C DA 5D 60` (clears `$5DDA`, `RTS`)

Direct caller(s):

- `C0:5279` (`JSR C0:3C25`)

Corroboration:

- The direct caller at `C0:5279` only calls this after detecting a cached packed-position mismatch at `$5D5C/$5D5E` (decode at `C0:526C..527C`), reinforcing the “guarded refresh” model.

Remaining uncertainty:

- Meaning of `$5DD4/$5DD6/$5DDA` (context latch? “destination”/music/zone id?) is still open; the call shape suggests “zone change” but that needs a label pass on `C0:68F4`, `C0:8756`, `C0:69AF`.

## `C0:3C4B` — current-position probe returning only high collision/terrain bits

Suggested cautious name:

- `Probe_CurrentPositionHighCollisionBits`

Byte evidence (entire body):

- `C2 31` (`REP #$31`)
- `A0 0C 00` (`LDY #$000C`)
- `AE 7B 98` / `AD 77 98` (player Y/X)
- `22 8B 5D C0` (`JSL C0:5D8B`)
- `29 C0 00` (`AND #$00C0`)
- `6B` (`RTL`)

Direct caller(s):

- `C1:B182` (`JSL C0:3C4B`)

Remaining uncertainty:

- The semantic of the `Y=#000C` argument to `C0:5D8B`, and what `#$00C0` represents (terrain class? collision layer? special trigger?), is not yet anchored to a named table.

## `C0:3DAA` — event-callable slot↔record sync + random seed

Suggested cautious name:

- `Sync_CurrentSlotToPartyCharacterRecord`

Entry byte evidence:

- Prologue: `C2 31 0B 7B 69 F0 FF 5B` (alloc DP frame)
- Slot index: `AD 42 1A` (reads `$1A42`)
- Seeds `$0F12[...]`: `A9 08 00 ... 9D 00 00` where `X = $0F12 + 2*slot` (via `ADC #$0F12`)
- Random low nibble: `22 9A 8E C0 29 0F 00 99 D6 0E` (calls `C0:8E9A`, stores at `$0ED6[slot]`)
- Stride map: `B9 9A 0E ... A0 5F 00 22 F7 8F C0 ... 69 CE 99` (maps `$0E9A[slot]` to `$99CE + slot*#$005F`)

Direct callers:

- none found as `JSL/JSR`

Event-pointer evidence (hard proof it’s an `EVENT_CALLROUTINE` target):

- `find_rom_bytes --ptr24 C0:3DAA` yields exactly one hit at file `0x03A067` (`C3:A067`).
- Nearby ROM bytes show the event opcode followed by the pointer bytes: `42 AA 3D C0` (interpreted as event “call routine C0:3DAA”).

Corroboration:

- `refs/ebsrc-main/.../src/data/events/scripts/002.asm` includes `EVENT_UNKNOWN_C03DAA` in `EVENT_2`, right after animation/callback setup.

Remaining uncertainty:

- `$3456[...]`, `$0E9A[...]`, `$0E5E[...]`, `$0ED6[...]`, `$0F12[...]`, and the record fields at `+$35/+$39/+$3B/+$5C` are not yet labeled; behavior is solid, but field names should remain conservative.

## `C0:3E25` — predecessor lookup in `$988B` registry

Suggested cautious name:

- `Get_PreviousRegistryTypeCode`

Byte evidence (core loop):

- Compares `($988B,X & $FF)` against `(A+1)` and increments `X` until match:
  - `BD 8B 98 29 FF 00 C5 02 D0 EF`
- Returns `#$FFFF` if index is 0:
  - `E0 00 00 D0 05 A9 FF FF`
- Otherwise `DEX` then returns `($988B,X & $FF)`:
  - `CA BD 8B 98 29 FF 00`
- Exit: `2B 60` (`PLD; RTS`)

Direct callers:

- none found as direct `JSR` (likely reached via indirect call shapes / tables)

Remaining uncertainty:

- What exactly `$7E:988B` represents (it behaves like a compact ordered registry of 8-bit type codes).

## `C0:3E5A` / `C0:3E9D` / `C0:3EC3` — registry/object ordering and gap flagging

Suggested cautious names:

- `C0:3E5A` = `Get_PreviousRegistryObjectOrderByte`
- `C0:3E9D` = `Measure_PreviousRegistryOrderDelta`
- `C0:3EC3` = `Advance_RegistryOrderAndUpdateGapFlag`

### `C0:3E5A` (direct helper)

Direct caller(s):

- `C0:3EA7` (`JSR C0:3E5A`) from inside `C0:3E9D`

Byte evidence (mapping chain to object field `+$3D`):

- Find predecessor in `$988B` (same loop structure as `C0:3E25`)
- Map predecessor index through `$9897` -> `$0E9A` -> `$4DC8`:
  - `BD 97 98` (loads `$9897[...]`)
  - `BD 9A 0E` (loads `$0E9A[...]`)
  - `BD C8 4D` (loads pointer from `$4DC8[...]`)
- Read `+$3D` field: `BD 3D 00`

Remaining uncertainty:

- Exact meanings of `$9897` and `$4DC8` domains (they behave like slot→object-pointer tables).

### `C0:3E9D` (delta computation; has cross-bank call)

Direct caller(s):

- `C0:3ED7` (inside `C0:3EC3`)
- `EF:02EA` (battle-side logic)

Byte evidence (wrapped subtraction):

- Calls helper: `20 5A 3E` (`JSR C0:3E5A`)
- Gets current object order byte: `AE C6 4D BD 3D 00` (uses pointer at `$4DC6`)
- Wrap if previous < current: `B0 04 18 69 00 01`
- Subtract: `38 E5 02`
- Exit: `2B 6B` (`PLD; RTL`)

### `C0:3EC3` (recommended seam to decompile first)

Direct caller(s) (hard anchors):

- `C0:4EC4` (`JSL C0:3EC3`)
- `C0:E24E` (`JSL C0:3EC3`)
- `EF:0386` (`JSL C0:3EC3`)
- `EF:03BF` (`JSL C0:3EC3`)

Byte evidence (key compare + flag writes):

- Calls delta helper: `22 9D 3E C0` (`JSL C0:3E9D`)
- Equal-to-target path clears `#$1000`:
  - `... BD 00 00 29 FF EF 9D 00 00` (AND `#$EFFF`, store back)
- Greater-than-target path sets `#$1000`:
  - `... BD 00 00 09 00 10 9D 00 00` (ORA `#$1000`, store back)
- Per-slot word location: `($7E:1002 + 2*$1A42)` via `AD 42 1A 0A 69 02 10`

Additional byte evidence (other writers for the same `$1002` bit `#$1000`):

- `C0:4EDD` clears the same bit in the current slot’s `$1002` word right before storing the new object order byte:
  - `AD 42 1A 0A 69 02 10 AA BD 00 00 29 FF EF 9D 00 00` (compute `X = $1002 + 2*$1A42`, `AND #$EFFF`, store back)
  - Immediately followed by: `... AE C6 4D 9D 3D 00` (store the byte-order value into object field `+$3D`)
- `C0:7B41..7B4F` sets the same bit for an arbitrary index held in DP `$04`, gated by `$98A5 == #$0002`:
  - `A5 04 0A 69 02 10 AA BD 00 00 09 00 10 9D 00 00` (compute `X = $1002 + 2*$04`, `ORA #$1000`, store back)

Calling convention note (important for decomp):

- The helper reads `A5 1E` early, which is *not* its own local: with the `DP -= 0x10` prologue pattern, `$1E` resolves to the **caller’s `$0E`**. In observed call sites (`C0:4EBB`, `EF:037A`, `EF:03B3`), the caller sets `$0E = #$0002` immediately before calling this helper.

Remaining uncertainty:

- Whether the `$1002` bit `#$1000` represents “gap too large”, “needs catch-up”, “out-of-spacing”, or a presentation flag. The compare directions are clear; the label should remain conservative until one `$1002` consumer is named.

## `C0:3F1E` — event-callable “fanout” of the current snapshot to registry entities

Suggested cautious name:

- `Apply_TransitionSnapshotToRegistryEntities`

Direct caller(s):

- `C0:3FD4` (internal `JSL` from `C0:3FA9`)

Event-call evidence:

- `find_rom_bytes --ptr24 C0:3F1E` yields **23** hits across `C3:*` and a couple of other banks, consistent with repeated event-script usage.
- Example nearby bytes (from file `0x030E40`, CPU `C3:0E40`): contains `42 1E 3F C0` (event “call routine C0:3F1E”).

Byte evidence (initial snapshot loop; two records, stride `#$0BF4`):

- Clears `$987D`: `9C 7D 98`
- Sets base `X=#5156`, `Y=#0002`, then for each record stores:
  - `AD 77 98 9D 00 00` (XPos)
  - `AD 7B 98 9D 02 00` (YPos)
  - `AD 7F 98 9D 08 00` (Facing)
  - `AD 83 98 9D 06 00` and `AD 81 98 9D 04 00` (mode/context words)
  - `9E 0A 00` (clear word/field at `+A`)
- Advances `X` by `#$0BF4` between the two records: `69 F4 0B`

Byte evidence (registry walk uses `$9891`, `$9897`, `$98A3`):

- Loop condition: `AD A3 98 29 FF 00` -> `$02`, then `CMP $02`
- Reads registry id: `B9 91 98 29 FF 00`
- Maps through `$4DC8`, clears object fields:
  - `9E 3D 00` (clears `+$3D`)
  - `9D 41 00` / `9D 37 00` with `A=#$FFFF`
- Maps `$9897[...]` and fans out `$9877/$987B/$987F/$9881` into per-slot arrays:
  - `... 9D 8E 0B` (X position array)
  - `... 9D CA 0B` (Y position array)
  - `... 9D F6 2A` (direction array)
  - `... 9D AA 2B` (mode/context array)

Corroboration (event scripts):

- `refs/ebsrc-main/.../src/data/events/scripts/068.asm`, `069.asm`, `070.asm` call `EVENT_UNKNOWN_C03F1E` immediately before `EVENT_PREPARE_NEW_ENTITY_AT_SELF` + `EVENT_QUEUE_TEXT`, consistent with “snap/fanout party state before spawning/cutscene”.

Remaining uncertainty:

- Exact meaning of the two `$5156` snapshot records, and the “per-slot arrays” at `$0B8E/$0BCA/$2AF6/$2BAA` (the legacy RAM map comments tie these to name-entry sprites, but the event usage here suggests they are more general-purpose slot presentation buffers).
