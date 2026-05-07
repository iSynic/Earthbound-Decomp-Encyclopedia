# Current-Slot Position Staging (`C4:6B8D..C4:6D4B`)

This pass closes the dense position-helper strip between the direction octant helpers and the movement target/vector layer.
It also names the two immediately adjacent text/deferred-record helpers at `C4:6E46` and `C4:6E4F`, because ebsrc's event macro file gives them useful corroborating context.

See also:

- [direction-octant-normalizers-c46a5e-c46b51.md](notes/direction-octant-normalizers-c46a5e-c46b51.md)
- [entity-resolver-script-and-direction-wrappers-c460ce-c4645a.md](notes/entity-resolver-script-and-direction-wrappers-c460ce-c4645a.md)
- [movement-target-bounds-and-vector-refresh-c46ef8-c47369.md](notes/movement-target-bounds-and-vector-refresh-c46ef8-c47369.md)
- [actionscript-wrapper-strip-c0a841-c0aafd.md](notes/actionscript-wrapper-strip-c0a841-c0aafd.md)

## Main result

The strip is a compact action-script adapter layer over the same entity-slot fields used by the later movement stepper:

- `$0B8E/$0BCA[current]`: live world anchor X/Y
- `$0FC6/$1002[current]`: cached movement target X/Y
- `$0E5E/$0E9A[current]`: staged X/Y words reused by bounds/vector scripts
- `$0C42/$0C7E[current]`: cleared or set together by camera-relative placement helpers
- `$0031/$0033`: camera/screen-origin X/Y
- `$9E35`: caller-side scene/photo index set by the wandering-photographer entry path

The important practical split is:

| Target field | Helpers |
|---|---|
| cached target `$0FC6/$1002` | `C4:6B8D`, `C4:6BBB`, `C4:6BE9`, earlier `C4:6B65`, `C4:6B79` |
| staged words `$0E5E/$0E9A` | `C4:6C45`, `C4:6C5E` |
| live anchor `$0B8E/$0BCA` | `C4:6C87`, `C4:6C9B`, `C4:6CC7`, `C4:6CF5`, `C4:6D23`, `C4:6D4B` |

So the area is not a loose unknown movement blob. It is the bridge that lets action scripts choose a source position, copy it into either a target/staging pair, and then let the already-documented movement helpers consume those fields.

## Target-position setters

`C4:6B8D` and `C4:6BBB` take a word selector from the action-script wrapper, resolve another live entity slot, and copy that entity's anchor into the current slot's cached target:

- `C4:6B8D` resolves through `C4:605A`, the `$2C9A` visual-type id resolver.
- `C4:6BBB` resolves through `C4:6028`, the `$2CD6` cached-pose descriptor resolver.

Both preserve the original current slot from `$1A42` before resolving the source slot.

`C4:6BE9` is the party/registry-code sibling reached by `C0:A943`, whose ebsrc symbol order labels it as `EVENT_GET_POSITION_OF_PARTY_MEMBER`. It resolves through `C4:608C` for ordinary byte codes, but has a special `#$FE` branch that selects from the active `$9897` registry list and falls back one entry if the last selected slot has zero X. Its output is still the same: copy source `$0B8E/$0BCA` into current `$0FC6/$1002`.

## Staged-position helpers

`C4:6C45` snapshots the current slot live anchor into the staging words:

- `$0E5E[current] = $0B8E[current]`
- `$0E9A[current] = $0BCA[current]`

This is the very common setup used before scripts write action variables `V2/V3` and call the short movement helpers around `C3:AB8A`.

`C4:6C5E` is the offset sibling. The action-script wrapper reads two words and passes them as X/Y offsets; the helper stores:

- `$0E5E[current] = $0B8E[current] + x_offset`
- `$0E9A[current] = $0BCA[current] + y_offset`

## Live-anchor setters

`C4:6C87` restores the current live anchor from the cached target pair. Timed-delivery and scripted looping movement use this after computing a target position, so the entity's anchor can be snapped back to the moving target before the next vector refresh.

`C4:6C9B` and `C4:6CC7` copy another entity's live anchor directly into the current slot's live anchor:

- `C4:6C9B` resolves the source by registry code through `C4:608C`.
- `C4:6CC7` resolves the source by cached pose descriptor through `C4:6028`.

`C4:6CF5` places the current slot at a camera-relative coordinate pair supplied by script parameters:

- `$0B8E[current] = $0031 + x_offset`
- `$0BCA[current] = $0033 + y_offset`
- `$0C7E[current] = $8000`
- `$0C42[current] = $8000`

The two high-bit writes are deliberately named mechanically for now; the paired set/clear contract is byte-clear, but the exact global field meaning remains open.

`C4:6D23` is a random camera-relative placement helper. It calls the common RNG at `C0:8E9A`, then places the current slot at:

- `$0B8E[current] = $0031 + $0070 + rng`
- `$0BCA[current] = $0033`

It is used by event scripts `495` and `496` before a repeated velocity pattern, which matches a screen-edge or camera-origin spawn setup more than a general movement step.

`C4:6D4B` places the current slot from a scene/photo record selected by `$9E35`. The record base is `E1:2F8A`, indexed with stride `#$003E`; record words at offsets `+$0A` and `+$0C` are shifted left three times and written as live X/Y. It then clears `$0C7E/$0C42`. This lines up with the wandering-photographer setup path at `C4:66C1`, which stores `caller A - 1` into `$9E35` before dispatching the photo event script.

## Adjacent text queue helpers

`C4:6E46` is the direct target of ebsrc's `EVENT_YIELD_TO_TEXT` macro. The body is the tiny latch write:

- `$9641 = 1`

The local name keeps the latch address because the downstream text-yield contract still needs a broader pass, but the macro identity makes the user-facing role much stronger than "unknown".

`C4:6E4F` is reached from `C0:A88D`, and ebsrc's event macro file maps that wrapper to `EVENT_QUEUE_TEXT`. The helper copies the caller pointer pieces into direct-page `$06/$08` and `$0E/$10`, then calls `C0:64E3` with `A = #$0008`. Existing queue notes name `C0:64E3` as `Enqueue_MovementRecord`, but the type-8 users are better described as deferred pointer records: `C4:681A` queues a current visual-type script pointer, while this helper queues a text pointer supplied by the action-script stream.

2026-05-06 source polish follow-up: `src/c4/photo_and_new_entity_preparation_helpers.asm`
now names the local photographer record table/stride, photo-scene X/Y cell
offsets, staged new-entity argument words `$9E2D/$9E2F/$9E31`, D5 teleport
destination row fields, text-yield latch value, deferred text-pointer record
type, and the proximity-check staged X/Y plus threshold tables. The comments
keep the C4-owned staging and comparison roles separate from C0 queue/entity
creation behavior.

The adjacent consumer pass in
`notes/c4-entity-visual-flag-current-slot-wrappers-c4645a-c46a5e.md` now names
where `$9E2D/$9E2F/$9E31` are consumed by the C4 prepared-entity wrappers and
where `$9E35` is seeded by the wandering-photographer entry path.

2026-05-06 anchor/target source follow-up: the upstream
`src/c4/direction_octant_target_helpers.asm` and
`src/c4/current_slot_anchor_staging_helpers.asm` now share local names for the
current-slot live anchor, cached target, staged-position, camera-origin, player
position, staged new-entity position, and registry slot-list fields. The
camera-relative `$0C42/$0C7E` flag writes remain helper-local because their
broader field meaning is still open.

## Event-script corroboration

Reference scripts make the split visible:

- `EVENT_UNKNOWN_C46C45` appears in scripts `038`, `053`, `077`, `103`, `250`, `591`, `666`, `669`, `672`, `673`, `674`, `804`, and others immediately before short movement/bounds setup.
- `EVENT_UNKNOWN_C46C87` appears in the timed-delivery common script and in script `804` inside loops that continuously refresh a target/vector path.
- `EVENT_UNKNOWN_C46D23` appears in scripts `495` and `496` before velocity-loop motion.
- `EVENT_UNKNOWN_C46D4B` appears in scripts `448` and `449`, the same family reached by the wandering-photographer photo-index setup.
- ebsrc defines `EVENT_YIELD_TO_TEXT` as a direct call to `C4:6E46`.
- ebsrc defines `EVENT_QUEUE_TEXT` as a call through `C0:A88D`, whose wrapper feeds `C4:6E4F`.

## Working Names

- `C4:6B8D` = `SetCurrentSlotTargetToVisualTypeSlotPosition`
- `C4:6BBB` = `SetCurrentSlotTargetToPoseDescriptorSlotPosition`
- `C4:6BE9` = `SetCurrentSlotTargetToPartyRegistryPosition`
- `C4:6C45` = `SnapshotCurrentSlotAnchorToStagedPosition`
- `C4:6C5E` = `SetStagedPositionOffsetFromCurrentAnchor`
- `C4:6C87` = `RestoreCurrentSlotAnchorFromCachedTarget`
- `C4:6C9B` = `CopyRegistrySlotAnchorToCurrentSlot`
- `C4:6CC7` = `CopyPoseDescriptorSlotAnchorToCurrentSlot`
- `C4:6CF5` = `SetCurrentSlotCameraRelativeAnchorWithFlags`
- `C4:6D23` = `PlaceCurrentSlotAtRandomCameraXPlus70Y`
- `C4:6D4B` = `PlaceCurrentSlotFromPhotoSceneRecord`
- `C4:6E46` = `SetYieldToTextLatch9641`
- `C4:6E4F` = `QueueEventTextPointerRecord8`

## Confidence boundaries

### Byte-clear

- which source resolver each copy helper uses
- which destination fields each helper writes
- the camera-origin and record-table arithmetic in `C4:6CF5`, `C4:6D23`, and `C4:6D4B`
- the event-script contexts listed above
- `C4:6E46`'s `EVENT_YIELD_TO_TEXT` macro identity
- `C4:6E4F`'s `EVENT_QUEUE_TEXT` wrapper identity and type-8 queue enqueue

### Still open

- exact global semantic names for `$0C42/$0C7E`
- exact broader meaning of `$9641` outside the yield-to-text macro
- final user-facing name for the `E1:2F8A` record family beyond the photo-scene evidence
- why `C4:6BE9`'s `#$FE` case falls back when the selected registry slot has zero X
