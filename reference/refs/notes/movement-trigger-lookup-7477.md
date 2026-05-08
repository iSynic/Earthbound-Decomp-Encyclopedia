# Movement Trigger Lookup at `C0:7477`

This note captures the current ROM-first interpretation of `Lookup_MovementTriggerType` at `C0:7477` and `Dispatch_MovementHelperFromLookup` at `C0:7526`.

## High-level picture

This pair sits above the `75xx` helper family and below several gameplay-facing callers.

- `C0:7477` looks up a small trigger or movement code from data in bank `D0`.
- `C0:7526` dispatches that code into one of several movement-side helper routines.

The strongest current reading is that this is a map- or trigger-lookup layer for movement interactions rather than a generic scheduler routine.

## `C0:7477` `Lookup_MovementTriggerType`

What the ROM clearly shows:

- The routine builds a long pointer whose bank byte is `D0`.
- It derives a coarse index from the incoming coordinates by combining one coordinate shifted right by 5 with the other masked to a 32-pixel boundary.
- It uses that coarse index to read a bucket pointer from bank `D0`.
- If the bucket is empty, it returns `#$FF` in 8-bit `A`.
- Otherwise it treats the bucket as a variable-length list with a count at the head.
- It then scans 5-byte records, comparing two per-record coordinate bytes against the low 5-bit fragments of the incoming coordinates.
- On match, it stores a word-like side value into `$5DBC`, stores a second byte-like value into `$5DBE`, and returns the same byte-like value in 8-bit `A`.
- On miss, it advances by 5 bytes and continues until the record count reaches zero, then returns `#$FF`.

A useful working record model is:

- byte 0: low 5-bit coordinate fragment A
- byte 1: low 5-bit coordinate fragment B
- byte 2: trigger or helper type returned in `A` and copied to `$5DBE`
- bytes 3-4: trigger parameter copied into `$5DBC`

That record layout is still an inference, but it matches the byte-level behavior well.

## `C0:7526` `Dispatch_MovementHelperFromLookup`

This wrapper calls `Lookup_MovementTriggerType`, then branches on the returned 8-bit code.

Verified dispatch map from the ROM:

- type `0` -> `JSR $6A1B`
- type `1` -> `JSR $6A91`
- type `2` -> `JSR $6ACA`
- type `3` -> `JSR $6E6E`
- type `4` -> `JSR $70CB`
- types `5` and `7` -> `JSR $6A8B`
- type `6` -> `JSR $6A8E`
- anything else -> falls through without a helper call

The wrapper passes `$5DBC` into most of these helper calls, and for types `3` and `4` it also restores the original coordinate inputs in `Y` and `X` before calling the helper.

The routine returns a small success-like value through `$0E`, which the direct callers then test.

## Direct callers

Confirmed direct callers of `C0:7526` so far:

- `C0:3C1F`
- `C0:46B9`
- `C0:484C`

Those callers use the returned value as a boolean-like gate for follow-up movement or position work, which supports the interpretation that this lookup-and-dispatch layer is part of gameplay movement interaction handling.

## Targeted cross-checks

A narrow compare against the legacy reference reinforces two useful points:

- the same dispatch map appears there around `C0:7526`
- some direct consumers of lookup types `5` and `6` use `EB_DoorDestinationTable`, which makes door-related semantics a strong candidate for at least part of this type space

That door interpretation is still a targeted inference rather than fully proven from our ROM-local analysis alone.

## Current best model

The best current model is:

- bank `D0` holds per-cell trigger buckets
- `C0:7477` resolves a movement-trigger record at sub-tile precision
- the returned type chooses one of several specialized movement or interaction helpers
- types `0` and `2` now look door-destination-oriented because both feed the bank `CF` table family used by `C0:6A1B` and `C0:6ACA`
- type `1` is a small movement-state switcher that writes `#$0007` or `#$0008` into `$9883`
- type `3` feeds a timed offset-step helper at `C0:6E6E`
- type `4` is the branch that reaches the staged-movement wrapper at `C0:70CB`
- types `5` and `7` still need broader-context tracing because the local `C0` dispatcher body is a stub
- type `6` is now much clearer: the front-interaction helper at `C0:65C2` treats it as a sentinel for a cached door-like fallback result, storing a pointer in `$5DDE/$5DE0` and marking `$5D62 = #$FFFE`

The focused helper-body write-up now lives in `notes/movement-trigger-helper-bodies.md`, the type-`6` probe write-up lives in `notes/type6-door-candidate-probe-65c2.md`, and the surrounding interaction pipeline is summarized in `notes/front-interaction-flow.md` and `notes/interaction-result-consumers.md`.

## Best next target

- Trace the higher-level C2 state family around `99DC`, and pair that with object-refresh helpers that consume `$2AF6`, so selector values `1/2` and target states `0/4` can be named from behavior instead of control flow.
