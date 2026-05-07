# Entity Visual Flag And Current-Slot Wrappers (`C4:6534..C4:69F1`)

This note covers the high-density frontier cluster immediately after the visual frame-selector updater family.

See also [visual-frame-selector-update-family-c4-62ff.md](notes/visual-frame-selector-update-family-c4-62ff.md), [overworld-entity-type-registry-9887-98a4.md](notes/overworld-entity-type-registry-9887-98a4.md), and [direction-octant-normalizers-c46a5e-c46b51.md](notes/direction-octant-normalizers-c46a5e-c46b51.md).

## Main result

This cluster is mostly mechanical glue around already-known entity resolver and visual-refresh state:

- `$2AF6[slot]` = frame/facing selector that feeds `C0:A48F`
- `$2C9A[slot]` = caller-assigned visual type id
- `$2CD6[slot]` = cached pose descriptor id
- `$988B/$9897/$98A3` = small overworld type registry to live slot mapping
- `$0B8E/$0BCA` = per-slot anchor X/Y
- `$10B6[slot]` and `$116A[slot]` = visual/control flag words manipulated with high bits `#$C000` / `#$8000`

The useful strategic result is that the large `C4:6534..69F1` frontier is no longer a mystery block. It is a set of small front-end wrappers around the resolver family from `C4:6028`, `C4:605A`, and `C4:608C`.

## Position and script helpers

### `C4:6534`

This spawns or initializes an entity using the current task/slot anchor position:

- reads current slot index from `$1A42`
- loads anchor coordinates from `$0B8E/$0BCA`
- forwards caller `A` and `X` plus `Y = FFFF` to `C0:1E49`

This is the compact current-slot-position sibling of the broader world-positioned entity initializers documented at `C4:64B5` and `C4:6507`.

### `C4:66F0`

This is a tiny nested-text/script pointer bridge. It copies caller `A/X` into `$0E/$10` and dispatches through `C1:86B1`, locally named `ExecuteNestedTextPointer`.

### `C4:66C1`

This is the local wandering-photographer entry wrapper reached from the bank-`01` deferred callback path at `C1:7304`.

It:

- calls `C0:7C5B`
- clears `$5D58`
- stores caller `A - 1` in `$9E35`
- dispatches the fixed text/event script pointer `C7:AB3F` through `C1:86B1`
- calls `C4:343E` with the original caller value

The script at `C7:AB3F` decodes as the photographer event script: it gates on event flag `01FE`, generates active sprites, opens a window, and starts the text beginning with `@Pictu...`. This matches the existing bank-`01` deferred-callback note that identifies the `D2 -> C1:8602 -> C1:7304` branch as the wandering-photographer summon path.

### `C4:681A`

This reads the current slot's `$2C9A` visual type id. If the id is valid, it indexes the `CF:8985` record family with a `0x11`-byte stride, reads the pointer at record offset `+9`, and enqueues that pointer through `C0:64E3` as movement record type `8`.

So this is not an arbitrary event jump. It queues a movement/script pointer from the current visual-type record.

### `C4:6881`

This combines two operations:

- calls `C4:6594(FF)` to apply the registry-wide `$10B6 |= C000` flag path
- enqueues the caller pointer from `$20/$22` through `C0:64E3` as movement record type `8`

It is a convenience wrapper used by C0/C1 entry paths that need to mark the visible registry entries and then queue a caller-supplied movement/script record.

## Flag setters and clearers

The first subfamily sets or clears high bits on visual flag words for slots found through the same resolver split as `C4:62FF..6397`.

Single-target `$10B6 |= C000` setters:

- `C4:655E` resolves by visual type id through `C4:605A`
- `C4:6579` resolves by pose descriptor id through `C4:6028`

Registry/all `$10B6 |= C000` setter:

- `C4:6594` resolves a specific registry code through `C4:608C`
- if caller `A == FF`, it also marks fixed slot word `$10E4` and every live slot in `$9897[0..$98A3)`

The clearing siblings apply `$10B6 &= 3FFF` through the same resolver split:

- `C4:65FB` clears by visual type id
- `C4:6616` clears by pose descriptor id
- `C4:6631` clears by registry code, or clears fixed slot `$10E4` plus every live registry slot when caller `A == FF`

The registry companion-flag pair at `C4:6712` and `C4:675C` uses both flag families:

- `C4:6712` sets `$10B6 |= C000` for the first `$9897` slot, then sets `$116A |= 8000` for the remaining live registry slots
- `C4:675C` clears `$10B6 &= 3FFF` for the first `$9897` slot, then clears `$116A &= 7FFF` for later live registry slots except entries whose `$988B` code is `9`

That last skip keeps the exact type-code meaning open, but the bit mechanics are now pinned down.

## Selection-mode latch helpers

`C4:6698` and `C4:66A8` resolve an entity slot and then enter a small mode/latch state:

- `C4:6698` resolves through visual type id (`C4:605A`)
- `C4:66A8` resolves through pose descriptor id (`C4:6028`)
- both store the resolved slot in `$9E33`
- both set `$98A5 = 2`

`C4:66B8` clears this state by zeroing `$9885` and `$98A5`.

The exact player-facing mode name behind `$98A5 == 2` is still open, but these wrappers are clearly "select/resolved slot into mode state" helpers rather than frame update routines.

## Small predicates and accessors

The cluster also includes several tiny helpers that are useful to name mechanically:

- `C4:67B4` returns `(C0:8E9A() & 1F) + 0C`, a random delay/range helper.
- `C4:67C2` returns `(C0:8E9A() & 1F) + ((0100 - $0B52[current]) / 4)`, a random delay biased by the current draw Y.
- `C4:68A9` returns `$006D`.
- `C4:68AF` returns `$0065`.
- `C4:68B5(A)` returns `1` when `A < $0B8E[current]`, otherwise `0`.
- `C4:68DC(A)` returns `1` when `A < $0BCA[current]`, otherwise `0`.
- `C4:6903(A)` returns `1` when `A > $987B`, otherwise `0`.
- `C4:6914` reads byte `+3` from the current visual-type record at `CF:8985 + $2C9A[current] * 0x11`, returning `4` if the current visual type id is invalid.

## Current-slot frame updates

`C4:6957` updates the current slot's `$2AF6` frame/facing selector and calls `C0:A48F(current)` when it changes.

`C4:6984` and `C4:69F1` face another resolved slot toward the current slot:

- `C4:6984` resolves the target slot through visual type id (`C4:605A`)
- `C4:69F1` resolves the target slot through pose descriptor id (`C4:6028`)
- both compute direction from the target slot's `$0B8E/$0BCA` anchor to the current slot's `$0B8E/$0BCA` anchor through `C4:1EFF`
- both quantize `(angle + 1000) / 2000` through `C0:915B`
- both store the result in `$2AF6[target_slot]` and refresh through `C0:A48F(target_slot)` when it changes

This is the direction-facing counterpart to the simpler frame-selector update family at `C4:62FF..6397`.

## Working Names

- `C4:6534` = `SpawnEntityAtCurrentSlotAnchor`
- `C4:655E` = `SetVisualTypeSlotFlagsC000`
- `C4:6579` = `SetPoseDescriptorSlotFlagsC000`
- `C4:6594` = `SetRegistrySlotFlagsC000`
- `C4:65FB` = `ClearVisualTypeSlotFlagsC000`
- `C4:6616` = `ClearPoseDescriptorSlotFlagsC000`
- `C4:6631` = `ClearRegistrySlotFlagsC000`
- `C4:6698` = `SelectModeSlotByVisualTypeId`
- `C4:66A8` = `SelectModeSlotByPoseDescriptorId`
- `C4:66B8` = `ClearSelectedModeSlot`
- `C4:66C1` = `RunWanderingPhotographerScriptForPhotoIndex`
- `C4:66F0` = `ExecuteNestedTextPointerFromAx`
- `C4:6712` = `SetLeadAndCompanionRegistryVisualFlags`
- `C4:675C` = `ClearLeadAndCompanionRegistryVisualFlags`
- `C4:67B4` = `RandomDelay0cTo2b`
- `C4:67C2` = `RandomDelayBiasedByCurrentDrawY`
- `C4:67E6` = `ClearFlagsForPose016fEntities`
- `C4:681A` = `QueueCurrentVisualTypeMovementScript`
- `C4:6881` = `SetAllRegistryFlagsAndQueueCallerMovement`
- `C4:68A9` = `ReadInputState006d`
- `C4:68AF` = `ReadInputState0065`
- `C4:68B5` = `TestValueLeftOfCurrentAnchorX`
- `C4:68DC` = `TestValueAboveCurrentAnchorY`
- `C4:6903` = `TestValueBelowPlayerY`
- `C4:6914` = `GetCurrentVisualTypeRecordByte03`
- `C4:6957` = `UpdateCurrentSlotFrameSelector`
- `C4:6984` = `FaceVisualTypeSlotTowardCurrentSlot`
- `C4:69F1` = `FacePoseDescriptorSlotTowardCurrentSlot`

## Still open

- exact semantic names for the high bits in `$10B6` and `$116A`
- exact player-facing mode behind `$98A5 == 2`
- exact field names for the `CF:8985` visual-type record family
- exact post-script contract between `C4:66C1` and `C4:343E`
- whether type code `9` in the `$988B` registry should be named as a companion, party, or object-class special case
