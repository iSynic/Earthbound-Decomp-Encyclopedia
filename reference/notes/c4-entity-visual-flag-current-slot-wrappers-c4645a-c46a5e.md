# C4 Entity Visual Flag And Current-Slot Wrappers `C4:645A..C4:6A5E`

## Scope

This note covers `src/c4/entity_visual_flag_current_slot_wrappers.asm`, the
wrapper band immediately after the resolver/script/direction helpers. The
helpers bridge C4's entity-slot resolver families, staged new-entity argument
words, registry flag toggles, movement-script queue records, and small
current-slot presentation tests.

The resolver/script side of the same contract is covered in
`notes/entity-resolver-script-and-direction-wrappers-c460ce-c4645a.md`; that
source now names the producer-side `$9E2D/$9E2F/$9E31` fills, resolver tables,
frame-selector updates, and `$116A/$8000` marker path used here.

## Main Result

`C4:645A..C4:6698` now carries local names for the two flag-word families that
this wrapper band mutates:

- `$116A + slot*2` with mask `$8000`
- `$10B6 + slot*2` with mask `$C000`

The source deliberately names these as C4-local flag families, not global
meaning. The registry-code helpers keep the original split: ordinary inputs
resolve one slot through `C4:608C`, while `#$00FF` fans out across the live
registry slots in `$9897[0..$98A3)`.

`C4:64B5` and `C4:6507` consume the staged new-entity argument words
`$9E2D/$9E2F/$9E31`. The first variant derives a create descriptor from a
`CF:8985` visual-type row, then writes the spawned slot's frame selector and
visual-type cache. The second variant passes the caller's descriptor argument
directly while still applying the staged position/facing words. Entity
allocation remains the external `C0:1E49` contract.

`C4:6534` stages the current slot's live anchor `$0B8E/$0BCA` as create-entity
X/Y arguments before calling the same external creator.

`C4:66C1` stores the one-based wandering-photographer photo index as a
zero-based `$9E35` scene index, runs the fixed nested text pointer at `C7:AB3F`,
and hands the caller photo index to the local post-photographer cleanup helper.
This lines up with the photo-scene record placement contract in
`notes/current-slot-position-staging-c46b8d-c46d4b.md`.

`C4:681A` reads the current slot's visual-type row, walks to the optional
movement-script long pointer at row offset `+$09`, and queues it as record type
`8` only when the pointer is nonzero. `C4:6881` combines the all-registry
`$C000` flag fanout with queueing an already-staged caller movement pointer.
The C0 queue storage/dispatch behavior remains external.

`C4:6957..C4:6A5E` updates a slot's frame selector only when the new value
differs, and the two facing helpers resolve either a visual-type id or cached
pose descriptor id before computing the rounded octant from that slot toward
the current slot. C4 owns the source/target coordinate selection and the
`$2AF6` write; C0 owns the visual-profile refresh helper.

## Working Names

- `C4:645A` = `ClearRegistryEntitySlotsFlag8000`
- `C4:64B5` = `InitWorldPositionedEntityWithVisualTypeId`
- `C4:6507` = `InitForcedSlotWorldPositionedEntityWithVisualTypeId`
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
- `C4:68B5` = `TestValueLeftOfCurrentAnchorX`
- `C4:68DC` = `TestValueAboveCurrentAnchorY`
- `C4:6903` = `TestValueBelowPlayerY`
- `C4:6914` = `GetCurrentVisualTypeRecordByte03`
- `C4:6957` = `UpdateCurrentSlotFrameSelector`
- `C4:6984` = `FaceVisualTypeSlotTowardCurrentSlot`
- `C4:69F1` = `FacePoseDescriptorSlotTowardCurrentSlot`

## Boundaries

- Keep `$10B6` and `$116A` local to this wrapper family until another pass
  proves their global presentation role.
- Keep `CF:8985` row fields local: this pass names only the create-descriptor
  byte, optional movement-script pointer, and byte `+3` reader.
- C0 entity allocation, queue dispatch, and visual-profile refresh internals
  are caller joins only here.
