# Class2 C2 Handlers

This note captures the current ROM-first model for the bank `C2` handlers that bridge class-`2` interaction results into concrete event-flag-aware behavior.

See also `notes/class2-dispatch-family.md` for the broader per-slot selector/state family around `99DC`, and `notes/class2-state-machine-99xx.md` for the newly mapped timed transition cluster.

## `C2:26EB` -> test current interaction event flag

This routine is now very direct:

- load the current class-`2` flag id from `$9C88`
- call `C2:21628`
- return the boolean-like result

`C2:21628` is the standard event-flag test helper over the bitfield rooted at `$9C08`.

Working name:

- `Test_CurrentInteractionEventFlag`

## `C2:26D0` -> set/clear current interaction event flag and refresh target

This routine takes a small on/off-style input in `A`, moves it into `X`, and then:

- loads the current interaction flag id from `$9C88`
- calls `C2:2165E` to set or clear that event flag
- saves the returned byte-like flag state
- loads raw interaction target id `$5D64`
- calls `C0:C30C`
- returns the saved flag-state byte

`C2:2165E` is the standard event-flag set/clear helper used by the textbox commands for turning event flags on and off.

Working name:

- `SetCurrentInteractionEventFlagAndRefreshTarget`

## What `C0:C30C` does with `$5D64`

`C0:C30C` turned out to be the key bridge.

Current best reading:

- treat input `A` as the raw actor/object target id
- map it through `$2C9A` to recover the interaction-result index
- use that result index to look up record field `+6` in `CF:8985`
- test that event flag through `C2:21628`
- if the flag is set, write `0` to `$2AF6,target`
- otherwise write `4` to `$2AF6,target`
- call `C0:A48F` to refresh the target state/appearance

`C0:A48F` and its sibling refresh helper `C0:A780` make this more concrete than before: `$2AF6` is an 8-state pose or variant selector that feeds the redraw tables at `C0:A60B` and `C0:A623`.

That means the class-`2` handler does not just toggle a global event flag. It immediately re-derives a target-local visual or behavior variant from that flag and refreshes the interactable object or actor represented by `$5D64`.

## Current best interpretation

This is the clearest concrete class-`2` behavior we have so far:

- class `2` installs an event-flag id in `$9C88`
- the C2-side handlers can test or modify that flag
- after a flag change, the target identified by `$5D64` is refreshed into one of two local visual variants via `$2AF6 = 0` or `$2AF6 = 4`

Working interpretation:

- class `2` likely represents an event-controlled two-state interactable object class
- the class does not flip an arbitrary state word; it chooses between two entries in the target-refresh pose or variant space
- examples could still be open/closed, active/inactive, or revealed/hidden, but the exact gameplay label for the `0` and `4` variants is still unproven

## Remaining unknowns

- what exact meaning selector values `1` and `2` have in the surrounding `99DC` per-slot state family
- what exact gameplay label the `0` and `4` visual variants correspond to for these targets
- whether class `3` is a read-only companion path to the same object family or a separate interaction family
