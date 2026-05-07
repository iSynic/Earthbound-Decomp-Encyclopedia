# Movement Target Bounds And Vector Refresh `C4:6EF8..7369`

## Scope

This pass covers the high-priority C4 frontier cluster `C4:6EF8-C4:7369`. It sits immediately after the direction-octant helpers documented in `notes/direction-octant-normalizers-c46a5e-c46b51.md` and is consumed by the C0 action-script wrapper strip and C3 movement scripts.

Reference context is still mostly placeholder names (`UNKNOWN_C46EF8`, `UNKNOWN_C47044`, etc.), but `ebsrc-main` corroborates the event-call sites:

- timed-delivery presentation prep calls `C4:6EF8`
- random-wander setup calls `C4:7225`, then `C4:7269`
- event movement helpers call `C4:7044`, `C4:7143`, and `C4:72A8`
- rope/screen-shake style scripts call `C4:7333`, `C4:733C`, `C4:734C`, and `C4:7369`

The safest model is that this is a movement-control layer over current-slot position, target position, vector/facing tables, and script-local bounds. Several per-slot fields are reused by different movement families, so the routine names below describe concrete behavior rather than assigning permanent global meanings to every table.

2026-05-06 source polish: `src/c4/movement_target_bounds_and_vector_refresh_helpers.asm`
now carries local WRAM names for the current-slot world position, cached target,
arrival tolerance, vector high/low words, facing direction, area bounds, camera
origin, and landing-profile action table. These names are deliberately scoped
to this movement-presentation corridor because `$0E5E/$0E9A/$0ED6/$0F12` and
nearby per-slot fields take narrower helper-local roles elsewhere.

The adjacent direction/anchor source pass now uses the same local names for the
current-slot live anchor, cached target pair, staged-position words, rounded
octant cache, and camera-origin placement fields; see
`notes/direction-octant-normalizers-c46a5e-c46b51.md` and
`notes/current-slot-position-staging-c46b8d-c46d4b.md`.

2026-05-06 movement-vector source follow-up: the same source now names the
arrival return values, area-class return values, sign-extension masks, split
vector high/low tables, and the C0 movement-install/facing-refresh caller
joins. It also keeps separate local aliases for `$0ED6/$0F12`: in `C4:6EF8`
they are proximity thresholds, while in `C4:7225..7269` they are the Y bounds
of the current-slot area rectangle. Do not collapse those roles into a single
global field name from this evidence alone.

## `C4:6EF8`

`C4:6EF8` returns `0` immediately while `$9F3F` is nonzero. Otherwise it compares the current slot position (`$0B8E/$0BCA`) against the player position (`$9877/$987B`):

- `abs(current_x - player_x) < $0ED6[current]`
- `abs(current_y - player_y) < $0F12[current]`

It returns `1` only when both tests pass. The timed-delivery common script uses this as a one-frame wait loop while `ACTIONSCRIPT_VARS::V4` remains true, after seeding `V2/V3 = 0x16`.

## `C4:6F7C`

`C4:6F7C` tests whether the cached target position (`$0FC6/$1002`) is within the current slot's movement threshold `$0F8A` of the live position (`$0B8E/$0BCA`).

If both axes are within threshold it returns `1`. Otherwise it:

- computes a sign/delta direction to the target through `C4:6AAC`
- calls `C0:C83B` to install movement from that direction when it differs from `$2AF6[current]`
- updates `$2AF6[current]`
- maps old/new directions through `C4:6AA3`
- calls `C0:A48F(current)` when the coarse sprite-facing bucket changes
- returns `0`

This is the sign/delta sibling of the angle-based stepper at `C4:7143`.

## `C4:7044`

`C4:7044` projects an input angle/phase in `A` through the current slot's magnitude in `$2B32[current]` by calling `C4:1FFF`. It then writes the projected components into four per-slot vector words:

- `$0CF6[current]`
- `$0DAA[current]`
- `$0D32[current]`
- `$0DE6[current]`

The writes preserve signed high-byte behavior: negative components are sign-extended with `OR #$FF00` / `OR #$00FF`, while positive components mask to the appropriate byte lane. The routine returns the original input `A`.

Direct callers:

- `C0:D969`, in the NPC/path target export path, before `C4:6B0A` and `$2AF6[current]` update
- `C4:71D2`
- `C4:72C2`

## `C4:7143`

`C4:7143` is the angle-based cached-target stepper used by the C0 action-script wrappers at `C0:A8C6`, `C0:A8D1`, and `C0:A8DC`.

Input contract:

- `A` = facing postprocess mode; nonzero applies `C4:6B37` half-turn rotation before the facing compare
- `X` = refresh mode; nonzero skips the `$2AF6`/sprite-facing refresh block after installing the vector

Behavior:

- if cached target (`$0FC6/$1002`) is already within `$0F8A` of current position, returns `1`
- otherwise computes the angle to target via `C4:6ADB`
- projects that angle into vector tables through `C4:7044`
- when `X == 0`, converts the angle through `C4:6B0A`, optionally rotates it by `C4:6B37`, stores `$2AF6[current]`, and calls `C0:A48F(current)` if the coarse facing bucket changes
- returns `0` after doing movement/facing work

This explains the C3 `WaitForActiveEntityMovementToFinish` loop: it calls the `C0:A8DC` wrapper each frame until `C4:7143` reports arrival.

## `C4:7225` and `C4:7269`

`C4:7225` consumes two word radii from `A` and `X` and writes an axis-aligned rectangle around the current slot's live position:

- `$0E5E[current] = x - radius_x`
- `$0E9A[current] = x + radius_x`
- `$0ED6[current] = y - radius_y`
- `$0F12[current] = y + radius_y`

The C0 wrapper `C0:A964` reads the two words from action-script bytecode before calling this helper. `C3:A381` uses it with `8,8` before entering the random-wander loop.

`C4:7269` classifies the current slot position against that rectangle:

- returns `3` if current X is left of `$0E5E`
- returns `7` if current X is right of `$0E9A`
- returns `5` if current Y is above `$0ED6`
- returns `1` if current Y is below `$0F12`
- returns `0` if inside

The random-wander script uses nonzero as the branch condition for choosing a fresh cardinal direction.

## `C4:72A8`

`C4:72A8` reads `$0E5E[current]` as an angle/phase-like source, projects it through `C4:7044`, converts it through `C4:6B51`, optionally rotates the result by `C4:6B37` when input `A` is nonzero, stores the result into `$2AF6[current]`, and refreshes the visual profile through `C0:A48F(current)` if the coarse sprite-facing bucket changes.

This helper is used by `C0:A8E7` and `C0:A8EF`. In event script `051`, the script increments `V0` by `0x0800`, refreshes another movement field through `C0:A864($FF)`, calls this helper, then halves `$0D32[current]` through `C4:730E`.

## Small wrappers

`C4:730E` halves `$0D32[current]` while preserving its sign bit. It is used by script loops that gradually damp one projected vector component.

`C4:7333` returns `$98A3 & 0x00FF`, the active count in the `$988B/$9891/$9897` overworld registry. Scripts `292`, `483`, and the `676/677/678` common script use the value as a tempvar loop count for repeated shake/pulse effects.

`C4:733C` reads the current landing-region/profile selector `$436E`, indexes `EF:101B`, and calls `C0:06F2` with the selected word. Existing landing-profile notes identify `EF:101B` as part of the landing display profile family, so this is a script-callable landing-profile action dispatcher.

`C4:734C` preserves caller `A`, passes `X = A` and `A = $0031 >> 3` to `C0:1A63`, then returns the original `A`. `C0:1A63` is the far wrapper for the map-strip refresh helper. In event `263`, scripts loop this helper over incrementing tempvar values after triggering the rope-switch/falling sound sequence.

`C4:7369` is a thin far wrapper around `C0:19E2`, locally named `Refresh_MapStripsAroundCamera`.

## Working Names

- `C4:6EF8` = `CheckCurrentSlotWithinPlayerProximityThreshold`
- `C4:6F7C` = `StepCurrentSlotTowardCachedTargetOrReportArrival`
- `C4:7044` = `ProjectAngleIntoCurrentSlotVectorWords`
- `C4:7143` = `StepCurrentSlotTargetVectorByAngleModes`
- `C4:7225` = `SetCurrentSlotAreaBoundsFromRadii`
- `C4:7269` = `ClassifyCurrentSlotAgainstAreaBounds`
- `C4:72A8` = `ProjectSlot0e5eAngleAndRefreshFacing`
- `C4:730E` = `HalveCurrentSlot0d32PreserveSign`
- `C4:7333` = `ReadActiveOverworldRegistryCount`
- `C4:733C` = `DispatchCurrentLandingProfileAction`
- `C4:734C` = `RefreshMapStripForIndexPreserveA`
- `C4:7369` = `RefreshMapStripsAroundCameraFarWrapper`

## Follow-ups

- `C4:6F7C` is code-complete here but still needs an event-bytecode caller sweep outside the current generated C3 manifest.
- `C4:72A8` is byte-true, but its source field `$0E5E[current]` is context-dependent; avoid renaming that field globally from this helper alone.
- The `C0:06F2` action-dispatcher target is now tied to landing profiles through `C4:733C`, but the individual `EF:101B` actions still need asset-side decoding.
