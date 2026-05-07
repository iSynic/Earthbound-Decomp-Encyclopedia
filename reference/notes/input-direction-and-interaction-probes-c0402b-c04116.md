# Input Direction and Interaction Probe Helpers `C0:402B..4116`

This note covers the next small C0 audit cluster after the bicycle/registry pass.

## Reference Status

- `C0:402B` is `UNKNOWN_C0402B`.
- `C0:4049` is `UNKNOWN_C04049`.
- `C0:404F` is the reference-named `MAP_INPUT_TO_DIRECTION`.
- `C0:4116` is `UNKNOWN_C04116`.
- `C0:41E3` and the surrounding interaction flow already have local names in `bank-c0-first-pass.md` and `front-interaction-flow.md`.

Direct caller anchors:

- `C0:402B`: `C4:8EC8`
- `C0:4049`: no direct control-flow caller found by the current xref helper
- `C0:4116`: internal calls from `C0:41F8`, `C0:4219`, `C0:423C`, and `C0:425D`

## Working Names

- `C0:402B` = `Install_AnimationScriptFromCallerPointer`
- `C0:4049` = `Clear_AnimationScriptCountdown`
- `C0:404F` = `MapInputToDirection`
- `C0:4116` = `Probe_InteractableInFacingDirection`
- `C3:E12C` = `InputDirectionPermissionMaskTable`
- `C3:E148` = `InteractionProbeDirectionXOffsetTable`
- `C3:E158` = `InteractionProbeDirectionYOffsetTable`

## `C0:402B`

Suggested local name:

- `Install_AnimationScriptFromCallerPointer`

This routine copies a long pointer from the caller's DP frame:

```text
source pointer = [$20/$22]
local pointer  = [$0E/$10]
call C0:83E3
```

`C0:83E3` reads a small record from `[$0E]`, installs the record's byte count into `$0081`, copies the record pointer to `$007D/$007F`, copies its payload word to `$0077/$0079`, and sets bit `#$4000` in `$007B`.

The only direct caller seen in this pass, `C4:8EC8`, first builds a pointer into a `$9E58`-rooted buffer and then calls `C0:402B`. So `C0:402B` is a wrapper for installing or starting that small record-driven animation/script stream, not the stream interpreter itself.

## `C0:4049`

Suggested local name:

- `Clear_AnimationScriptCountdown`

This body is only:

```text
REP #$31
STZ $0081
RTL
```

Since `$0081` is the countdown byte set by `C0:83E3`, the safest local read is that this clears the active countdown for the same small `$007B/$007D/$007F/$0081/$0083` stream family.

No direct control-flow caller was found, so keep the name cautious until a caller is pinned.

## `MAP_INPUT_TO_DIRECTION` / `C0:404F`

Reference name:

- `MAP_INPUT_TO_DIRECTION`

Input:

- `A` = table index into `C3:E12C`

Output:

- `A = 0..7` when the active input nibble matches an enabled direction bit
- `A = #$FFFF` when no enabled direction matches, or when `$5D9A != 0`

The routine:

1. Rejects immediately with `#$FFFF` if `$5D9A` is nonzero.
2. Loads a direction-permission bitmask from `C3:E12C[A]`.
3. Reads `($0065 & #$0F00)` as the active input nibble.
4. Maps selected input nibble values to direction indices when the corresponding bit is enabled.

Observed mapping:

| `$0065 & #$0F00` | required bit | return |
|---|---:|---:|
| `#$0800` | `#$0001` | `0` |
| `#$0900` | `#$0002` | `1` |
| `#$0100` | `#$0004` | `2` |
| `#$0500` | `#$0008` | `3` |
| `#$0400` | `#$0010` | `4` |
| `#$0600` | `#$0020` | `5` |
| `#$0200` | `#$0040` | `6` |
| `#$0A00` | `#$0080` | `7` |

This lines up with the earlier `overworld-camera-step-accumulator-c017ea-c018f2.md` finding that `$0065` carries movement/direction flags.

## `C0:4116`

Suggested local name:

- `Probe_InteractableInFacingDirection`

Input:

- `A` = facing/direction index

Behavior:

1. Use direction-offset tables at `C3:E148` and `C3:E158`.
2. Add those offsets to `$9877/$987B` to form a probe point.
3. Temporarily force `$5D58 = 1`.
4. Call `C0:5FF6` at the probe point, using the live slot base from `$9889`.
5. If `C0:5FF6` returns a live slot (`< #$8000`), copy `$2C9A[slot]` to `$5D62` and the slot id to `$5D64`.
6. Otherwise, call `C0:5CD7` and test for tile flag pattern `#$0082`.
7. If that pattern is present, advance the probe point by `8` pixels in the direction's nonzero axis and retry.
8. Restore `$5D58`.
9. If `$5D62` is `0` or `#$FFFF`, call `C4:334A` with the original direction.
10. Return `$5D62`.

This is the lower-level directional probe used by `C0:41E3`. `C0:41E3` tries the current facing and then rotated alternatives, while `C0:4116` performs one actual point-and-tile probe for a single direction.

## Relation to Existing Interaction Notes

This pass tightens the split in `front-interaction-flow.md`:

- `C0:4116` = one facing-direction probe
- `C0:41E3` = rotate through candidate facings and pick one that yields a usable result
- `C0:4279` = public resolver that initializes `$5D62/$5D64`, invokes the rotation pass, and updates `$2AF6`/`$987F`
- `C0:42EF` = sibling/front-facing probe path used by `C0:43BC` and `C0:4452`

So the `4116` gap is not a new interaction system. It is the missing lowest-level helper under the already-documented front-interaction pipeline.
