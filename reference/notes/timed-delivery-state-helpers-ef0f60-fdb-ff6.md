# Timed Delivery State Helpers (`EF:0F60` / `EF:0FDB` / `EF:0FF6`)

This note records the current local read for the remaining state-side helpers in the timed-delivery controller.

See also [timed-delivery-controller-499-500-common.md](notes/timed-delivery-controller-499-500-common.md).
See also [delivery-row-helpers-ef0e67-ef0ead.md](notes/delivery-row-helpers-ef0e67-ef0ead.md).
See also [post-transition-deferred-script-queue-c06b21-c06bff.md](notes/post-transition-deferred-script-queue-c06b21-c06bff.md).
See also [timed-delivery-system-flags-754-779.md](notes/timed-delivery-system-flags-754-779.md).
See also [timed-delivery-warning-text-gates.md](notes/timed-delivery-warning-text-gates.md).

## Main result

The timed-delivery controller is now structurally clear enough to separate three roles:

- `EF:0F60` = readiness predicate for the success-versus-retry branch
- `EF:0FDB` = success-side state setup
- `EF:0FF6` = failure-side or teardown-side state reset

The exact human-friendly names of the underlying state words are still somewhat tentative, but the split between the two key WRAM flags is better now:

- `$5D98` behaves like the broader persistent controller or service latch
- `$5D9A` behaves like the transient active-arrival / special-handling flag

## `EF:0F60`: readiness predicate

`EF:0F60` returns a boolean used by `499+500_common` to decide whether to enter the success branch or the retry/failure branch.

Its logic is permissive rather than purely table-driven. It returns nonzero immediately under several conditions:

- low byte of `$0028` is nonzero
- low byte of `$000D` is not `#$000F`
- `$88E0 != #$FFFF`
- `$B4A8 != #$FFFF`
- `$5D98 != 0`
- bit `15` is set in `7E:116A[$9889]`

It also has one explicit blocking case:

- if `$10E4 & #$C000 != 0`, it forces the return value to `0`

If that blocking case does not apply, it falls back to `$5D9A`, except that certain `$9883` modes (`7`, `8`, `0C`, `0D`) force a `1` return.

So the cleanest current wording is:

- `EF:0F60` = delivery/service readiness predicate that blends local timed-delivery state with broader world, controller, and presentation busy state

## Why the `$88E0` and `$B4A8` checks look broad, not delivery-local

Two local cross-checks are especially useful.

First, the delayed-action scheduler at `C0:DC4E` refuses to run its four-entry timer table while:

- `$88E0 != #$FFFF`
- `$9643 != 0`
- `$5D60 != 0`
- `$4DBA != 0`

That puts `$88E0` in the same larger "busy / active context" family that already blocks other engine-side deferred work.

Second, the immediate pointer runner at `C1:0004` feeds a far pointer into `EB_ProcessTextboxData_Main` and then loops until `$B4A8 == #$FFFF` before returning. That makes `$B4A8` look much more like a text or presentation busy handle than a delivery-local variable.

So the readiness helper is not simply asking "is this delivery row ready." It is also checking whether the surrounding engine state can accept the arrival-side presentation branch.

## `EF:0FDB`: success-side setup

`EF:0FDB` is short but revealing:

- `5D98 = 1`
- `5D9A = 1`
- call `C09F43`
- play sound `#$0059` through `C4:FBBD`
- call `C03CFD`

This is the helper used on the success branch before the controller queues pointer `1` and enters the arrival movement path.

So the cleanest current read is:

- `EF:0FDB` = begin success-side arrival or service state

## Why `$5D9A` looks transient

The strongest local proof comes from `C03CFD`, which `EF:0FDB` calls.

When `$9883 == 3`, `C03CFD`:

- branches differently if `$5D9A != 0`
- skips some of the ordinary refresh path when `$5D9A` is set
- clears or avoids parts of the standard visual/update reset path
- leaves a visibly different update sequence than the `$5D9A == 0` case

A second useful cross-check comes from `C03BE3`, which temporarily saves `$5D9A`, clears it around `C05B7B`, and then restores it.

That makes `$5D9A` look much more like a transient active special-state flag than a long-lived global configuration bit.

## `EF:0FF6`: failure / teardown-side reset

`EF:0FF6` is the paired reset-side helper:

- `STZ $5D9A`
- test flag `#$0049` through `C21628`
- store that result to `$5D98`
- if `$9883 == 3`, play sound `#$0052`
- otherwise call `C06A07`

This is the helper used on the failure/teardown branch before the controller queues pointer `2`.

So the cleanest current read is:

- `EF:0FF6` = end the transient arrival state and restore/reset the broader controller latch

## Why `$5D98` looks more persistent than `$5D9A`

A useful cross-check comes from `C1:BCAB`, which backs up `$5D98`, forces it to `1` during a larger preset-teleport-style flow, and restores it at the end.

A second cross-check comes from `C2:0000`, which immediately branches away from one of its special controller families when `$5D98 != 0`.

There is also a tiny direct setter at `C4:3344` (`SetSpecialEventRestrictionLatch5d98`), which simply stores the incoming `A` value into `$5D98`.

A gameplay-side cross-check from the extracted text data fits that broader reading nicely too. The project now contains explicit warning strings for three service-like pending states:

- "You should wait to teleport until after the pizza arrives."
- "You should wait to teleport until after a customer has shown up."
- "You should wait to teleport until after Escargo Express arrives."

Those lines do not name `$5D98` directly, but they are exactly the kind of shared service-pending rule that would explain why the preset-teleport path preserves `$5D98` instead of treating it like throwaway local state.

That makes `$5D98` look less like a one-frame transient and more like a broader controller or availability latch that multiple systems preserve, test, and restore. The script-side flag note in [timed-delivery-system-flags-754-779.md](notes/timed-delivery-system-flags-754-779.md) now strengthens that same point from the other side: the timed-delivery scripts also participate in a broader `FLG_SYS_DISTLPT` restriction family rather than a delivery-only local toggle.

## Caution on flag `#$0049`

`EF:0FF6` rebuilds `$5D98` from `C21628(#$0049)`. In the reference flag-name tables, `#$0049` corresponds to `FLG_WIN_GIEGU`.

That name does not fit the local timed-delivery behavior cleanly, so the safest wording is still cautious:

- locally, `EF:0FF6` restores `$5D98` from a broader global flag in the same `C21628` bitfield domain
- the exact gameplay meaning of that reused flag in this controller should remain tentative until a stronger local bridge appears

## Best current controller picture

With these helpers included, the `499+500_common` family now reads like:

1. wait for `delivery_time`
2. if `EF:0F60` says ready, arm success state with `EF:0FDB`, queue the immediate success pointer, and run arrival movement
3. otherwise retry on the row-specific threshold/wait policy
4. if retries are exhausted, run `EF:0FF6`, queue the deferred failure pointer, and tear down

That is strong enough to use operationally, even though a few of the broader state-word names should stay cautious for now.
