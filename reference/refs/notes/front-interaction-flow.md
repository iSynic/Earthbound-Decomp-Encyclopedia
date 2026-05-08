# Front Interaction Flow Around `C0:42EF`

This note captures the current ROM-first model of the front-of-player interaction path and how the cached type-`6` door candidate fits into it.

## High-level picture

The interaction flow now looks like a layered probe pipeline:

- `Resolve_FrontInteractionTarget` at `C0:4452` is the main entry used by a caller in bank `C1`.
- `Resolve_InteractableAlongFacingTarget` at `C0:4279` is the sibling entry used by a second consumer in bank `C1`.
- Both feed the same result-state family around `$5D62/$5D64`.
- `C0:4452` calls `Resolve_InteractionFacingRotation` at `C0:43BC`.
- That helper tries `Probe_FrontInteractionFacing` at `C0:42EF` across several facing candidates.
- If the ordinary probe leaves no usable result, `Probe_FrontType6DoorCandidate` at `C0:65C2` can cache a special fallback pointer for the type-`6` case.

So the type-`6` path is not a separate system. It is a fallback branch inside the ordinary front-interaction resolver.

## `C0:4452` `Resolve_FrontInteractionTarget`

What the ROM clearly shows:

- Initializes `$5D62` and `$5D64` to `#$FFFF`.
- Calls `C0:43BC` and gets back a facing-like value in `A`.
- If that facing result is not `#$FFFF`, it compares it against a per-party cached facing value in `$2AF6 + 2 * [7E:9889]`.
- When the facing changed, it writes the new facing to `$987F`, updates that per-party cache entry, and calls `JSL $C0A780`.
- Returns `$5D62` in `A`.

Working interpretation:

- this is the main front-interaction target resolver
- `$5D62` is the important output code or sentinel
- `$5D64` is an auxiliary value produced by the ordinary object/tile probe path

## `C0:43BC` `Resolve_InteractionFacingRotation`

What the ROM clearly shows:

- Saves the original facing from `$987F & #$FFFE`.
- Calls `C0:42EF` with the current facing.
- If the probe returns neither `0` nor `#$FFFF`, it returns that facing immediately.
- Otherwise it rotates facing and retries up to three more times.
- The tested sequence is current facing, then `+2`, then `+4`, then `-2` modulo 8.
- If all attempts fail, it restores the original facing and returns `#$FFFF`.

Working interpretation:

- this helper searches for an interactable target by trying multiple facing candidates around the player rather than only the currently displayed facing
- the return value is the facing that produced a usable result, not the target itself

## `C0:42EF` `Probe_FrontInteractionFacing`

What the ROM clearly shows:

- Takes a facing value in `A`.
- Uses direction-offset tables at `C3:E148` and `C3:E158` to derive an initial point in front of the player from `$9877/$987B`.
- Temporarily saves `$5D58`, forces `$5D58 = #$0001`, and restores it before returning.
- Calls `JSL $C05FF6` on the probe point.
- If that result is below `#$8000`, it maps the result through `$2C9A`, stores the mapped value in `$5D62`, stores the raw probe result in `$5D64`, restores `$5D58`, and returns.
- Otherwise it calls `JSL $C05CD7`, checks for flag pattern `#$0082`, and, if allowed, advances the probe point along the direction offsets to continue searching.
- After the ordinary probe path, if `$5D62` is `0` or `#$FFFF`, it calls `C0:65C2` with the original facing.
- Finally it returns `$5D62`.

Working interpretation:

- this is the core "look in front of the player for an interactable thing" routine
- the normal success path is object or tile driven through `C05FF6` and the table at `$2C9A`
- the type-`6` branch is only a fallback after that ordinary path fails to produce a usable result

## Where type `6` fits

The role of `C0:65C2` is now easier to state precisely:

- `C0:42EF` first tries to resolve a normal interaction result
- only when that leaves `$5D62` as `0` or `#$FFFF` does it call `C0:65C2`
- `C0:65C2` probes nearby trigger cells through `C0:7477`
- if the trigger type is `6`, it caches a bank `CF` destination-table pointer in `$5DDE/$5DE0`, copies the side byte to `$5DDC`, and sets `$5D62 = #$FFFE`

That means:

- `0` means no interaction result
- `#$FFFF` means invalid or blocked result
- `#$FFFE` means use the cached fallback pointer from the type-`6` path
- any other value in `$5D62` is a normal table-driven interaction result

## Current best model

- `4452` is the public front-interaction resolver
- `43BC` is the facing-rotation chooser
- `42EF` is the core front-of-player probe
- `65C2` is a fallback probe for door-like type-`6` trigger cells
- the type-`6` path is now best understood as interaction fallback state, not as a missing movement helper body

## Best next target

- Trace the higher-level C2 state family around `99DC`, and pair that with object-refresh helpers that consume `$2AF6`, so selector values `1/2` and target states `0/4` can be named from behavior instead of control flow.
