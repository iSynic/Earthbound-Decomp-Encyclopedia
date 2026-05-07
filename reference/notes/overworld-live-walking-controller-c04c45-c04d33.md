# Overworld Live Walking Controller (`C0:4C45..4D33`)

This note captures the first clearly live high-level walking-time controller found in the same stack as the ordinary `C0:4010 -> C0:1558` camera refresh path.

See also [overworld-timing-scroll-commit-slice-c08b20-c08284.md](overworld-timing-scroll-commit-slice-c08b20-c08284.md).
See also [overworld-visible-entity-refresh-slice-c07b52-c07c5a.md](overworld-visible-entity-refresh-slice-c07b52-c07c5a.md).
See also [position-snapshot-and-movement-tick-c0449b-c05200.md](position-snapshot-and-movement-tick-c0449b-c05200.md).

## Main result

`C0:4C45..4D33` is the strongest current fit for a live ordinary walking-time controller that:

1. reads current movement and state words from the `$987x` family
2. updates per-entry slot fields including row `+0x3D`
3. selects or updates a small descriptor/state tuple rooted near `$5156`
4. computes an intermediate result through `C0:5F82`
5. then jumps into the smooth camera/update path through `JSL C0400E` at `C0:4D24`

This makes `4C45` a better current seam for ordinary walking than several earlier candidates like `7B52` or `A780`, which did not break during normal walking tests.

## Locally proved

### `4C45` is in the live `4010` call stack

Recent emulator work on the `C0:4010` breakpoint showed `C0:4C45` in the active stack during ordinary walking.

So this routine is not just a side path. It is part of the currently executing movement-time control flow.

### `4C45` conditionally runs a helper side path, then enters an entry-state refresh

The routine starts by clearing and sampling state around `$9885`, `$5D58`, `$436C`, and `$0065`.

Notable branches:

- optional `JSL C07C5B` when `$5D58 != 0`
- special-case branch to `4D76` when `$436C != 0`, movement bit `$0065 & #$0040` is set, and a low nibble from `$0002` is nonzero

Then it resolves the current active entry through:

- `$9889`
- `$0E9A`
- `4DC8`

and writes current state into row `+0x3D` of the selected entry.

### `4C45` updates entry-local state rooted near `$5156`

At `4CBE..4D13` the routine builds an entry-local pointer rooted at `$5156` and writes:

- current `$9877` through `($10)`
- current `$987B` through `($10),Y` with `Y = 2`
- an incremented selector or phase value back through `($14)`

This is one of the cleanest current local signs that `4C45` is maintaining ordinary per-walking-step entry state, not just camera state.

### `4C45` reaches the smooth camera path through `C0400E`

The key walking-time bridge is:

- `C0:4D24  JSL $C0400E`

`C0400E..402A` contains the same small wrapper that feeds the smooth `4010 -> 4026 -> 1558` camera refresh path.

That means the current stack order is now much healthier:

- `4C45` prepares high-level entry/state context
- `4D24` enters the ordinary camera/update wrapper
- `4010` provides the smooth centered camera input to `1558`

So `4010` being smooth does not clear the whole walking path. It only clears the downstream camera-input side of it.

### `C05F82` is a direct ordinary-walking dependency of `4C45`

Just before `C0400E`, `4C45` calls:

- `C0:4CF0  JSL $C05F82`

`5F82` locally:

- uses current X/Y-like inputs
- looks up data through `2B6E` and tables in `C4:2A1F / 2A41 / 2AEB`
- computes intermediates into `$5DAC / $5DAE`
- runs `JSR 5503` and `JSR 559C`
- returns a result in `$5DA4`

So `5F82` is a live ordinary walking-time producer, not an abstract side helper.

## Decomp-backed and locally consistent

### Why `4C45` matters more than the dead breakpoint candidates

Several earlier candidates did not break during ordinary walking:

- `17EA..18F2`
- `7C35 / 7C3F`
- `A780`

By contrast, `4C45` is already confirmed in the live `4010` stack. That makes it a much better anchor for the next walking-time render or state investigation.

### Why this still fits the smooth-camera result

The recent camera-side emulator work still holds:

- `4010` inputs looked orderly
- `1558` updated `$31/$33` smoothly
- publish and NMI commit looked healthy

`4C45` gives the missing upstream context: there is still substantial walking-time state and entry preparation happening before the already-smooth `4010` camera wrapper is reached.

That makes `4C45` one of the healthiest current suspects for a visible-layer or walking-state cadence issue that survives even when the camera itself is smooth.

## Still uncertain

### Exact semantic meaning of the `$5156`-rooted state tuple

Locally it behaves like per-entry movement/phase or state data, but the exact symbolic identity is still open.

### Whether the visible judder comes from `4C45` itself, from its `5F82` side computation, or from some still-later presentation path

This note proves the live walking-time bridge. It does not yet prove where the eye-visible unevenness is introduced.

## Best next emulator workflow

The best next live breakpoints are now:

- `C0:4C45`
- `C0:4CF0` / `C0:5F82`
- `C0:4D24`

These sit on one confirmed ordinary walking stack, unlike the earlier dead candidates.

## Bottom line

`4C45..4D33` is currently the healthiest live high-level walking-time controller we have found.
It sits upstream of the already-smooth `4010 -> 1558` camera path and performs ordinary movement-time entry/state preparation before that camera path runs.

So the next useful walking-time investigation should stay on this `4C45 -> 5F82 -> 400E/4010` chain rather than returning to the now-weakened dead-end candidates.
