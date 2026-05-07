# Delayed-Action Timer Callers

This note tracks the direct callers we have confirmed for `Queue_DelayedActionTimer` at `C0:DBE6`.

## Summary

- Direct-caller scan report: `notes/direct-callers-c0-dbe6.md`
- `Queue_DelayedActionTimer` has 8 direct call sites, all in bank `C0`.
- `Clear_DelayedActionTimerSlot` at `C0:DC38` has no direct `JSL` or same-bank `JSR` callers in the split ROM scan.
- The call pattern is consistent: callers set a callback pointer in `$0E/$10`, put a delay value in `A`, and then `JSL $C0DBE6` to arm one of the four `7E:9E3C` timer records.
- The repeated callback bodies at `C0:6F82` and `C0:6FED` are now decoded. They are self-rearming pollers that compare live Y at `$987B` against staged Y at `$5DCE` and only commit staged coordinates when the condition is met.
- A useful borrowed clue from the legacy reference is that `$9877/$987B` are named as player X/Y low position. That is not proven by our ROM alone, but it matches the observed read/write pattern well enough to guide the current movement-oriented interpretation.

## Confirmed direct callers of `C0:DBE6`

- `C0:4F99`
  Callback target: `C0:4F47`
  Delay source: constant `#$0001`
  Working interpretation: one-frame deferred callback after a temporary screen or state change, because `C0:4F47` restores `$0200`, sets `$001A`, and calls `C0:856B`.

- `C0:6F02`
  Callback target: `C0:6E4A`
  Delay source: `Y + 1`, where `Y` comes from `$001A`
  Working interpretation: delayed commit of the secondary staged coordinate pair at `$5DD0/$5DD2`, followed by motion-state cleanup through `$5DC4/$9883/$5D56/$5DBA`.

- `C0:6F68`
  Callback target: `C0:6E2C`
  Delay source: result of `JSL $C48D58` plus 1
  Working interpretation: computed-delay commit of the secondary staged coordinate pair at `$5DD0/$5DD2`, but this branch leaves the motion state in `$9883 = #$000C` instead of clearing it.

- `C0:6FE7`
  Callback target: `C0:6F82`
  Delay source: constant `#$0001`
  Working interpretation: one-frame delayed handoff into a self-rearming Y-position poller that commits staged coordinates from `$5DCC/$5DCE` when ready.

- `C0:7059`
  Callback target: `C0:6FED`
  Delay source: constant `#$0001`
  Working interpretation: one-frame delayed handoff into the sister poller that commits staged coordinates from `$5DCC/$5DCE` and clears motion state when ready.

- `C0:7180`
  Callback target: `C0:6F82`
  Delay source: normalized value in `$14`, derived from `JSL $C48D58` and data at `C3:E200`, `C3:E220`, and `C3:E228`
  Working interpretation: variable-delay version of the `6F82` handoff that computes a staged coordinate pair before arming the poller and storing the resulting target in `$5DCC/$5DCE`.

- `C0:71D1`
  Callback target: `C0:6FED`
  Delay source: normalized value in `$14`, derived from `JSL $C48D58` and data at `C3:E208`, `C3:E220`, and `C3:E228`
  Working interpretation: variable-delay version of the `6FED` handoff with the same staged-coordinate setup but different completion behavior.

- `C0:7710`
  Callback target: `C0:769C`
  Delay source: `Y`
  Working interpretation: delayed one-shot callback into another subsystem-local state setup path; `C0:769C` does not currently look like the same movement flow as the `6Exx/6Fxx/71xx` family.

## Structural conclusions

- `Queue_DelayedActionTimer` is not being called broadly across the ROM by arbitrary banks. At least in direct-call form, this timer-arm helper is currently a bank-`C0` local mechanism.
- The repeated callbacks at `C0:6F82` and `C0:6FED` are not one-shot wrappers. They compare only `$987B` against `$5DCE`, which makes them look like Y-position convergence pollers that keep rearming until live position crosses the staged target.
- On success, those pollers copy staged X/Y from `$5DCC/$5DCE` into `$9877/$987B`, clear `$9875/$9879`, and either set `$9883 = #$000D` or clear `$9883/$5D56/$5DBA`, depending on which poller fired.
- The secondary callbacks at `C0:6E2C` and `C0:6E4A` commit a second staged X/Y pair from `$5DD0/$5DD2`, again clearing `$9875/$9879`, but with different motion-state side effects.
- That makes `$5DC4`, `$5D56`, `$5DBA`, and `$9883` look much more like movement or actor-state fields than generic scheduler metadata.
- The timer-arm helpers still sit beside, not inside, the larger active-slot allocator path. The heavier active-slot walker is `C0:94AA -> ($0A5E) -> C0:DB0F`, while `C0:DBE6` only fills the small four-entry `7E:9E3C` timed-callback table.
- Because `C0:DC38` has no direct callers, timer clearing is likely done indirectly, through callback bodies, slot-index returns from `DBE6`, or script or handler tables rather than plain direct subroutine calls.

## Best next target

- Decode the wrapper beginning at `C0:70CB` cleanly enough to turn the `C3:E200`, `C3:E208`, `C3:E220`, and `C3:E228` tables into named movement parameters.
- Tighten the role of `$5DC4`, especially the `#$0000`, `#$0100`, and `#$FFFF` cases, so we can tell whether it is direction, movement mode, or a more general actor-state word.
