# Interaction Context And Event Flags

This note collects the current ROM-first picture around the interaction-context structure selected by `C1:0301` and the event-flag plumbing tied to class `2` interaction results.

See also `notes/class2-c2-handlers.md`, `notes/class2-dispatch-family.md`, and `notes/class2-state-machine-99xx.md` for the current bridge into the C2-side flag handlers, target refresh path, and surrounding per-slot state family.

## Current structure base model

`C1:0301` resolves a base pointer for the active interaction context.

Current best reading:

- if `$88E0 != #$FFFF`, it uses the active slot index in `$8958`
- it reads a per-slot base from `$88E4`
- it runs that value through `C0:8FF7` with selector `#$0052`
- it adds `#$8650`
- the result is the base address for the current interaction context structure

That makes `8650+` the current best candidate for the live talk/check interaction record for the active slot.

## Helper cluster around `C1:0301`

The helper family immediately after `C1:0301` now looks structured rather than miscellaneous.

Working model:

- `C1:0326` snapshots context fields `+$17`, `+$1B`, and `+$1F` into `+$21`, `+$25`, and `+$29`
- `C1:0380` restores `+$21`, `+$25`, and `+$29` back into `+$17`, `+$1B`, and `+$1F`
- `C1:03DC` loads the pointer pair at `+$1B` into `$14/$16`
- `C1:0410` loads the pointer pair at `+$17` into `$14/$16`
- `C1:0450` stores a small value from `Y` into `+$1F`
- `C1:045D` stores `$1C/$1E` into `+$17`
- `C1:0489` stores `$1C/$1E` into `+$1B`
- `C1:04B5` returns the current slot field at `+$0E` relative to the `8650` base
- `C1:04D8` returns the current slot field at `+$10` relative to the `8650` base

The strongest current interpretation is that `+$17` and `+$1B` are two context pointer slots, `+$1F` is a small mode/index field, and `+$21/+25/+29` are saved copies used for temporary overrides.

## `$9C88` is an event-flag id

The class-`2` interaction selector stores record word `+6` from `CF:8985` into `$9C88`.

That field is no longer mysterious:

- `C2:21628` tests a bit in the event-flag bitfield rooted at `$9C08`
- `C2:2165E` sets or clears a bit in that same bitfield
- both helpers use the mask table `C4:562F`, which is just `01 02 04 08 10 20 40 80`

This is the same helper pair used by the textbox commands identified in the legacy reference as:

- `EB_TextboxCommand04_Main` -> turn event flag on
- `EB_TextboxCommand05_TurnOffEventFlag_Main` -> turn event flag off

So `$9C88` is best understood as an event-flag index associated with the active interaction result.

## Why this matters for class `2`

This sharpens the class-`2` model considerably.

Current best reading:

- class `2` writes one or two context pointers into the active interaction record
- it installs an event-flag id into `$9C88`
- later bank `C2` code can test or modify that flag through the standard event-flag helpers
- after a flag change, bank `C2` refreshes the raw target in `$5D64` through `C0:C30C`, which toggles `$2AF6,target` between `0` and `4` before calling `C0:A48F`
- `C0:A48F` and `C0:A780` show that `$2AF6` feeds an 8-state redraw selector, so class `2` is choosing between two target-local visual variants rather than mutating an abstract state word in isolation

That means class `2` is very likely an event-flag-aware two-state interaction class rather than just a generic "secondary structured output" case.

## Remaining unknowns

The important unresolved pieces are now narrower:

- what exact semantics the context pointers at `+$17` and `+$1B` have
- what `+$1F` means in gameplay/UI terms
- what exact meaning selector values `1` and `2` have in the surrounding `99DC` per-slot timed-state family
- whether class `3` bypasses event-flag logic entirely or just uses a different context path

## Best next target

- Trace the current-slot field family used by the `99xx` controller, or follow the `JSL C2:7550` branch from that same controller, so selector values `1/2` in `99DC+` can be named from concrete behavior.
