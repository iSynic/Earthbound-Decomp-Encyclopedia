# Entity Resolver Script And Direction Wrappers (`C4:60CE..C4:645A`)

This note closes the helper band that sits between the resolver routines documented in [visual-frame-selector-update-family-c4-62ff.md](notes/visual-frame-selector-update-family-c4-62ff.md) and the later entity initializer paths. The important local result is that this range is not a loose set of one-off helpers: it is a small adapter layer over three entity-slot lookup keys.

## Main result

The band reuses the same resolver split already established for `C4:6028`, `C4:605A`, and `C4:608C`:

| resolver | lookup key | current role |
|---|---|---|
| `C4:605A` | `$2C9A` | caller-assigned visual-type/effect id |
| `C4:6028` | `$2CD6` | cached pose descriptor id |
| `C4:608C` | `$988B/$9897` registry | overworld type-registry code |

Around that split, the newly covered helpers do three jobs:

1. run small entity scripts against a resolved slot
2. compute rounded direction-octants between two resolved entity slots
3. set or clear bit `$8000` on `$0A6A` for one registry entity or the whole live registry group

## Script runners

### `C4:60CE` - visual-type slot runner with cached pose state

This path resolves a slot with `C4:605A`. If the visual-type id is found, it caches the slot's current world position from `$0B8E/$0BCA` into `$9E2D/$9E2F`, caches the current frame selector from `$2AF6` into `$9E31`, then calls `C0:93F9`.

The script pointer passed to `C0:93F9` depends on the caller's `Y` value:

- `Y != #$0006` selects `C3:A209`
- `Y == #$0006` selects `C3:A204`

The exact script VM contract for `C0:93F9` remains open, but the local adapter contract is clear: resolve by `$2C9A`, preserve the resolved slot's pose/world state in the `$9E2D..$9E31` scratch block, then run one of two fixed script entries against that slot.

### `C4:6125` - pose-descriptor slot runner with cached pose state

This is the same adapter shape as `C4:60CE`, but it resolves with `C4:6028` instead of `C4:605A`.

That makes it the pose-descriptor keyed sibling: resolve by `$2CD6`, preserve the same `$0B8E/$0BCA/$2AF6` state into `$9E2D/$9E2F/$9E31`, then run the fixed script entry selected by the caller's `Y`.

### `C4:617C` and `C4:61CC` - table-record script runners

These two helpers resolve a slot and then select a three-byte record from `C4:C4D4` using the caller's `Y` value.

- `C4:617C` resolves with `C4:605A`
- `C4:61CC` resolves with `C4:6028`

For a found slot, the first two bytes of the selected record become the script pointer passed in `A`, and the third byte becomes the `Y` argument for `C0:93F9`; `X` remains the resolved entity slot.

So this pair is the table-driven sibling of the fixed-entry runners above: one visual-type keyed, one pose-descriptor keyed, both dispatching `C0:93F9` through records at `C4:C4D4`.

## Direction-octant wrappers

### `C4:621C` - selector-mode resolver

`C4:621C` is the local mode switch used by the direction helpers. It dispatches to one of the three resolver families:

| mode | resolver |
|---:|---|
| `0` | `C4:608C` registry lookup |
| `1` | `C4:605A` visual-type lookup |
| `2` | `C4:6028` pose-descriptor lookup |

The helper returns the resolved entity slot id to its caller.

### `C4:6257` - rounded octant between resolved entities

`C4:6257` resolves two entity slots through `C4:621C`, reads their `$0B8E/$0BCA` positions, and computes the direction between them with `C4:1EFF`. It then rounds the angle into an octant by adding `$1000` and dividing by `$2000` through `C0:915B`.

The local contract is byte-clear even though the event-facing parameter order still deserves caution: it computes a rounded direction octant between two entities selected by resolver mode.

### Thin wrappers

The three short wrappers seed the resolver mode and then tail into `C4:6257`:

- `C4:62AE` selects mode `1`, the visual-type keyed path.
- `C4:62C9` selects mode `2`, the pose-descriptor keyed path.
- `C4:62E4` selects mode `0`, the registry keyed path.

These wrappers line up with C1 event opcode callers that print the result as a one-based direction value after incrementing the returned octant.

## Registry flag toggles

### `C4:63F4` - set `$8000` on `$0A6A`

This helper calls `C0:7C5B`, clears `$5D58`, then sets bit `$8000` on `$0A6A[slot]`.

The input supports two modes:

- ordinary values resolve one registry slot through `C4:608C`
- `#$00FF` iterates every live registry slot listed in `$9897[0..$98A3)`

The exact semantic name of `$0A6A` bit `$8000` remains open, so the safest current name keeps the operation explicit.

### `C4:645A` - clear `$8000` on `$0A6A`

This is the clearing sibling of `C4:63F4`. It uses the same single-registry-code versus `#$00FF` whole-registry iteration pattern, but clears the high bit with `AND #$7FFF`.

The following wrapper band is covered separately in
`notes/c4-entity-visual-flag-current-slot-wrappers-c4645a-c46a5e.md`, including
the prepared-entity consumers of `$9E2D/$9E2F/$9E31`, `$10B6/$116A` flag-word
families, visual-type movement pointer queueing, and current-slot facing
helpers.

2026-05-06 source polish follow-up:
`src/c4/entity_slot_resolver_frame_selector_helpers.asm` now names the resolver
tables for `$2CD6`, `$2C9A`, and `$988B/$9897`, the missing-slot sentinel and
slot-scan bounds, the staged new-entity scratch words filled by the fixed
script runners, the `C4:C4D4` three-byte dispatch records, selector-mode ids,
octant rounding constants, frame-selector update table, registry broadcast
cutoff, and the `$116A/$8000` marker path. C0 script, refresh, and renderer
internals remain external callees.

## Working Names

- `C4:60CE` = `RunVisualTypeEntityScriptWithCachedPose`
- `C4:6125` = `RunPoseDescriptorEntityScriptWithCachedPose`
- `C4:617C` = `RunVisualTypeEntityScriptFromRecordC4c4d4`
- `C4:61CC` = `RunPoseDescriptorEntityScriptFromRecordC4c4d4`
- `C4:621C` = `ResolveEntitySlotBySelectorMode`
- `C4:6257` = `ComputeRoundedOctantBetweenResolvedEntities`
- `C4:62AE` = `ComputeVisualTypeEntityFacingOctantToTarget`
- `C4:62C9` = `ComputePoseDescriptorEntityFacingOctantToTarget`
- `C4:62E4` = `ComputeRegistryEntityFacingOctantToTarget`
- `C4:63F4` = `MarkRegistryEntitySlotsFlag8000`
- `C4:645A` = `ClearRegistryEntitySlotsFlag8000`

## Still open

- the exact script VM contract of `C0:93F9`
- the record format/name for the three-byte table at `C4:C4D4`
- the user-facing meaning of `$0A6A` bit `$8000`
- the exact C1 event opcode parameter names for the two-entity octant helpers
