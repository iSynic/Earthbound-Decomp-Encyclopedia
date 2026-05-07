# C3 Actionscript Callback Contracts

This note is the human front door for the callback layer now emitted by
`tools/build_c3_actionscript_semantics_audit.py`.

## Main Result

The C3 event/actionscript bytecode layer is syntactically closed. Native
behavior enters the script VM in two different ways:

- `EVENT_CALLROUTINE` reads inline script arguments, calls a native helper, and
  returns a condition/result to the script.
- callback installers such as `EVENT_SET_TICK_CALLBACK`,
  `EVENT_SET_POSITION_CHANGE_CALLBACK`, and `EVENT_SET_PHYSICS_CALLBACK` bind
  per-frame native behavior that keeps running after the current instruction.

The audit now tracks each `EVENT_CALLROUTINE` native target with:

- preferred local name
- semantic group
- call count
- inline argument byte count
- named argument schema, where known
- current argument/behavior contract

It also tracks installed callback targets separately with preferred local names,
semantic groups, install counts, and first-pass behavior contracts. That makes
the next C3 phase a contract-polish pass instead of a blind callback hunt.

## Current Callback Groups

The regenerated audit currently buckets `86` `EVENT_CALLROUTINE` contract seeds
and `17` installed callback targets:

| Group | Meaning |
| --- | --- |
| `timed-delivery` | EF helpers for delivery row state, retry policy, queued pointers, and arrival/departure speeds |
| `visual-profile` | current-slot visual refresh, animation pulse, display phase, and release helpers |
| `current-slot-state` | helpers that read/write current-slot script fields, anchors, or staged values |
| `movement` | direction, angle, vector, and movement-timer helpers |
| `collision` | footprint, terrain, and neighbor-cache collision refresh helpers |
| `entity-spawn` | script helpers that spawn or initialize entities from current-slot context |
| `text-presentation` | text handoff, queued text pointer, and yield-to-text helpers |
| `presentation-render` | C4 render/presentation callbacks that support visual script effects |
| `neighbor-cache` | explicit `$289E[current_slot]` cache sentinel helpers |
| `world-state-restore` | transition/display state restore helpers |
| `party-facing` | party-look/attention callbacks |
| `battle-runtime` | C2 callbacks used by C3 event flow |
| `intro-integrity` | intro-only checksum/control-flow helper |

The installed callback signal is now explicit in
`notes/c3-actionscript-semantics-audit.md`. The top installed targets are the
movement/presentation callbacks scripts repeatedly bind for entity motion and
screen placement: `C0:A37A`, `C0:9FC8`, `C0:A360`, `C0:A039`, `C4:8BE1`,
`C0:9FF0`, `C4:8C2B`, and `C0:9FF1`.

## Promotion From Prior Notes

The first semantic override set intentionally imports names that were already
proved elsewhere in the repository but were not flowing into C3 decodes:

- `EF:0CA7` -> `CheckCurrentDeliveryRetryThreshold`
- `EF:0D23` -> `GetCurrentDeliveryRetryWait`
- `EF:0D8D` -> `QueueCurrentDeliveryPointer1`
- `EF:0DFA` -> `QueueCurrentDeliveryPointer2`
- `EF:0E67` -> `GetCurrentDeliveryEnterSpeed`
- `EF:0E8A` -> `GetCurrentDeliveryExitSpeed`
- `EF:0F60` -> `CheckDeliveryServiceReadyForArrival`
- `EF:0FDB` -> `BeginDeliverySuccessArrivalState`
- `EF:0FF6` -> `ResetDeliveryArrivalState`
- `C4:8B3B` -> `MakePartyLookAtActiveEntityCallback`
- `C4:800B` -> `UndrawFlyoverTextAndRestoreWorldDisplay`
- `C2:0000` -> `RunEnemySunstrokeCheck`
- `C1:FFD3` -> `ComputeBankC1ChecksumTail`
- `C0:A039` -> `ReturnFromPositionChangeCallback_NoProjection`
- `C0:9FF0` -> `ReturnFromPhysicsCallback_NoMovement`
- `C4:8BE1` -> `SimpleScreenPositionCallback`
- `C4:8C02` -> `SimpleScreenPositionCallbackOffset`
- `C4:8C2B` -> `CentreScreenOnEntityCallback`

The important point is not just nicer names. These names now appear directly in
decode excerpts, so script-family notes can quote the generated audit without
re-introducing older `UNKNOWN_*` labels.

## Source-Pilot Attention Helpers

Several callback contracts now feed the C3 source-pilot frontier even when they
do not change the current source-map audit row set:

- `C0:C48F` -> `GateWidePlayerDistanceBucket`: a wide player-distance gate
  proved in `notes/pathfinding-consumers-direction-helpers-c0bd96-c0c7db.md`.
  C3 attention scripts use it as the wait/engage boundary before direction or
  route handoff.
- `C0:D77F` -> `MarkOtherSlotsAttentionLocked`: marks other eligible slots'
  attention/interaction flags before scripted object-interaction cleanup.
- `C0:D7B3` -> `Save_CurrentSlotAttentionPosition`: snapshots the current slot
  position into the NPC-attention saved-position fields.
- `C0:D7C7` -> `Restore_CurrentSlotAttentionPosition`: restores that saved
  NPC-attention position back to the current slot.
- `C0:D7E0` -> `Normalize_CurrentSlotAttentionState`: collapses a nonzero
  current-slot attention marker to state `1`.

The `C0:D77F/D7B3/D7C7/D7E0` contracts are imported from
`notes/npc-attention-path-coordinator-c0d19b-c0d98f.md`. They unblock the
bus-driver and compact NPC-attention pilots without promoting any C0 runtime
implementation into C3 ownership.

## Cast-Scroll Source-Pilot Wrappers

The large event-801 cast-scroll pilot now has field-shaped wrappers for its
high-volume C0 helper calls:

- `C0:A99F` -> `SpawnEntityRelative_ReadTwoWords`: reads a sprite-pose
  descriptor index and entity script id, then calls the C4 cast-scene spawn
  helper that combines staged script `var0/var1` with the live BG3 scroll.
- `C0:A9B3` -> `PrintCastNameParty_ReadThreeWords`
- `C0:A9CF` -> `PrintCastNameEntityVar0_ReadThreeWords`
- `C0:A9EB` -> `PrintCastNameCurrentThreshold_ReadThreeWords`

Those cast-name helpers render as
`cast_name_source_word, cast_name_tile_x_word, cast_name_tile_y_word`; the
entity spawner renders as `sprite_pose_descriptor_word,
entity_script_id_word`.  The spawn contract is based on the C4 spawn wrappers
(`C4:6534` and `C4:ECAD`) forwarding A/X into `C0:1E49`, where A (`$2B`)
indexes the `EF:133F` sprite-pose descriptor table and X (`$2D`) is passed to
the delayed-action state initializer as the entity script id. `C4:ED0E` names
`$0321` as `CastSceneDriverScriptId`, matching the `$0322+` values seen in the
cast-scroll spawn pilot as entity script ids. Most individual descriptor and
script id labels remain uncataloged, but the compact Event782 party recovery
set is now C3-cataloged: `$0010/$0189/$018A/$018B` are named as the four
`party_recovery_slot*_lying` sprite-pose descriptors and `$030F` as the shared
`battle_swirl_recovery_party_spawn` entity script id. Those names are scoped to
the observed spawn sequence; exact character/pose asset identity remains
local-unknown. The same operand pair applies to `C0:A98B`
`SpawnEntityAtCurrentSlotAnchor_ReadTwoWords`; only the anchor source differs.

The contracts are imported from the C0/C4 wrapper strip and
`notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`, then applied only as C3
decoder/source-pilot metadata.

## Position Wrapper Operands

- `C0:A87A` -> `Script_SetCameraRelativeAnchor_ReadTwoWords`: X/Y offset
  words added to the current camera origin before writing the current slot
  anchor and anchor flags.
- `C0:A912` -> `ActionScript_PrepareNewEntity`: explicit new-entity X/Y words
  plus a facing/selector byte staged through the C4 new-entity helper.

## Presentation Wrapper Operands

The C3 decoder now carries a few more small presentation wrapper schemas that
show up in town hall, coffee/tea, teleport, and battle-background transition
pilots:

- `C0:9FAE` -> `ActionScript_FadeInWrapper`: one `fadein_effect_word`.
- `C0:9FBB` -> `ActionScript_FadeOutWrapper`: one `fadeout_effect_word`.
- `C0:A977` -> `Movement_LoadBattleBg`: `battle_bg_layer1_id_word` plus
  `battle_bg_layer2_id_word`. The C0 wrapper reads the first word into A and
  the second into X before calling `C4:7370`; that helper fixes Y to `$0004`
  and forwards A/X/Y to `C2:D121`, whose runtime contract names A as layer 1,
  X as optional layer 2, and Y as layout flags.
- `C0:AA07` -> `ActionScript_FadeOutWithMosaic`: display fade step,
  per-step wait, and mosaic-update flag words passed to the fade-out
  transition helper.
- `C0:AA23` -> `Script_StageMosaicWh0Mask_ReadThreeWords`: left-X, Y, and
  right-X words forwarded to the C4 WH0 mosaic/window-mask starter.
- `C0:AA3F` -> `Script_SetVisualSetupBytesByMode`: COLDATA red, green,
  and blue component bytes loaded into `$9E37-$9E39` before the C4
  color-math/fixed-color writer runs with the caller-supplied mode selector.
- `C0:AAB5` -> `Script_RunLandingPaletteFade_ReadWordByteByte`: a landing
  palette existing-work mask word, palette scale byte, and fade frame-count
  byte forwarded to the C4 landing/flyover palette fade driver.

`C0:AA6E` sites now name the two inline bytes without overclaiming the exact
frame art. The first byte is a `visual_state_byte`: the C0 wrapper stores it in
current-slot `$2AF6` before the `C0:A4C4`/`C0:A794` visual-profile refresh
path. The observed C3 values are `$00-$07`. The second byte is a
`countdown_byte` seed: `$00/$01` are observed, with the zero-visual path writing
the seed raw to `$10F2/$2892` and the existing-visual path doubling it into
`$10F2` before recording the current slot in `$2896`.

The C3-local battle-bg value catalog only names observed pilot values:
`$00FF` as the event-340 Winters transition layer 1, `$0000` as the disabled
layer-2 sentinel, and `$0107/$0108` as the coffee/tea layer pair. These are
byte-shape contracts plus narrow source-pilot aliases; exact visual-effect
naming can stay with the C0/C2/C4 presentation notes.

The C3-local landing palette mask catalog names the three observed first-word
values passed through `C0:AAB5`. `C4:958E` shifts this word once per 16-color
palette block; a set bit reuses the existing `$7F:0000` work block and a clear
bit reloads the source/template word. Source pilots therefore render `$FFFC`,
`$DFFC`, and `$2000` as block-pattern masks rather than opaque palette
selectors.

The same `C0:AAB5` sites now also catalog the two trailing bytes. The palette
scale byte is forwarded through X to `C4:954C`: `$32` is the full RGB555 scale,
lower observed values dim the source block, and higher observed values such as
`$5A` saturate through the C4 clamp path. The fade frame-count byte is forwarded
through A to `C4:97C0`: `$01` is the immediate-export sentinel, while `$3C`,
`$64`, and `$78` step the landing palette interpolation once per frame before
exporting and queueing the CGRAM upload.

The C3-local COLDATA component catalog names only the observed bytes passed
through `C0:AA3F`: `$00`, `$10`, and `$18`. The C0 wrapper copies those bytes
to `$9E37-$9E39`; `C4:2439` then writes them to `$2132 COLDATA` with the red,
green, and blue selector bits applied. These source-pilot aliases preserve the
component-value contract without trying to name the exact screen effect from
the script site alone.

The C3-local fade effect catalog names only the observed words passed through
`C0:9FAE/C0:9FBB`: `$0101` and `$0701`. The wrappers preserve the word in A
and move the byte-swapped copy through X before calling `C0:886C` or
`C0:887A`; those helpers seed `$0028` from the low byte and `$0029-$002A` from
the high byte. Source pilots keep these as fade effect words until the display
state machine has stronger player-facing effect names.

The C3-local mosaic WH0 mask catalog names the two observed `C0:AA23` triples:
`$1AC0/$2170/$1B40` for the Tenda-stage dance-followup path and
`$1220/$1670/$12E0` for the repeated Tenda-stage performance-corridor path.
`C4:7765` subtracts `$0031` from the left/right X words and `$0033` from the
Y word while emitting the `$7F:0BF8` WH0 HDMA stream, so the source aliases
name the callsite preset and edge role while leaving the final visual-effect
name open.

The C3-local display fade-out catalog names the observed `C0:AA07` words:
`$0001` as the fade step, `$0001/$0008` as per-step wait counts, and `$0000`
as the disabled mosaic-update flag. The C0 wrapper forwards these as A/X/Y to
`C0:8814`; that helper subtracts A from INIDISP mirror `$000D`, waits X frames
through `C0:878B`, and only calls the `C0:87AB` mosaic-nibble updater when Y is
nonzero.

## Surface-Flag Operands

- `C0:A679` -> `Script_SetCurrentSlotSurfaceFlags`: reads one byte and stores it
  to current slot field `$2BAA`. The ebsrc symbol at the C0 wrapper is
  `SET_SURFACE_FLAGS`, so C3 now treats the operand as `surface_flags_byte`
  rather than a generic display-control byte.
- The observed C3 values are `$00`, `$01`, and `$03`. Source pilots render them
  as `!ACTIONSCRIPT_SURFACE_FLAGS_NONE`,
  `!ACTIONSCRIPT_SURFACE_FLAGS_BIT0`, and
  `!ACTIONSCRIPT_SURFACE_FLAGS_BIT0_BIT1`; those names intentionally preserve
  the bitmask shape without claiming exact per-bit runtime meaning yet.

Source polish: `src/c4/actionscript_camera_and_screen_position_callbacks.asm`
now names the current-slot index, action-script callback flag bit, active
entity registry scan tables/count, live world/screen/offset coordinate tables,
camera origin pair, facing-direction table, and half-octant rounding constants
used by the party-look and screen-position callbacks.

## Operand Labels In Decodes

`tools/decode_event_script.py` now also prints first-pass operand field labels
for the most common event/actionscript VM operands. For example, generated
decode excerpts use `script_var=var4`, `frames=$08`, `animation_id=$01`, and
named callback arguments such as `event_flag_word=$000C` or
`neighbor_cache_callback_long=$C0:64A6 <...>`.

Pointer-shaped operands are labeled too. Short branches/calls now distinguish
`jump_target`, `call_target`, `conditional_call_target`, and
`inverted_conditional_call_target`; task launchers use `task_script`; callback
installers use `tick_callback`, `draw_callback`, `position_change_callback`,
and `physics_callback`. The audit renders this as an opcode operand catalog so
port/reassembler work can separate byte width from VM role without reading the
Python decoder first.

The decoder also applies a deliberately small value-symbol layer where the
evidence is already bank-local or cross-referenced:

- mutation operation bytes use the C0 interpreter table names:
  `$00 <AND>`, `$01 <OR>`, `$02 <ADD>`, `$03 <EOR>`
- `$5D9A` is shown as `queue_pending_or_special_state_flag`, matching the C0/EF
  queue and transient special-state notes
- velocity and relative-position words show signed decimal meaning beside the
  raw hex value
- the generated audit now has a direction callback boundary table: C3 tempvar
  writes or `C0:9F82` random-choice word lists are counted as direction values
  only when they reach `C0:A65F` and, for movement-vector cases, `C0:C83B`
  inside the same decoded source-map span
- the same audit now records `$2B32` movement magnitudes from `C0:A685` only
  when the decoded span carries them into movement-vector or timer consumers
  such as `C0:C83B`, `C0:CA4E`, `C0:A6A2`, `C0:A6AD`, or `C0:CBD3`

This is intentionally a readability layer, not a new byte format. The raw bytes
remain printed on every decoded line, and the source-pilot emitters still
revalidate against the ROM byte-for-byte.

## Sound-Effect Word Constants

`C0:A841` reads a word-shaped `sound_effect_id_word` and hands it to the sound
queue path. The source-pilot renderer names the C3-used IDs that have direct
`SFX_XX` comments in `refs/earthbound-sounddriver-byte-perfect/sfx_sequences.asm`.
Examples include `!ACTIONSCRIPT_SOUND_EFFECT_ENTER_DOOR`,
`!ACTIONSCRIPT_SOUND_EFFECT_EXIT_DOOR`, `!ACTIONSCRIPT_SOUND_EFFECT_CAMERA_SHUTTER`,
`!ACTIONSCRIPT_SOUND_EFFECT_MAGIC_BUTTERFLY`, and
`!ACTIONSCRIPT_SOUND_EFFECT_STAIRS_FAST`.

That catalog is deliberately narrow. Other words that happen to match a sound
ID numerically, such as entity visual-type operands passed to spawn helpers,
remain numeric because they are not `sound_effect_id_word` operands.

## Good-Enough Boundary

C3 is good enough for this milestone when generated reports are truthful and
useful, not when every literal has a perfect story. Animation ids, direction
classes, and per-family variable meanings should stay literal unless a local
script family or native callback proves the symbolic meaning. That keeps the
decoder from laundering guesses into source.

## Next Contract Work

The current audit has no remaining generic `argN_byte` schemas among the C3
callback seeds. The last awkward case, `C0:5E76`, is now named using the ebsrc
macro shape:

```asm
EVENT_UNKNOWN_C05E76 $F1, UNKNOWN_C064A6
```

That means the remaining C3 callback work is semantic polish rather than byte
shape discovery. The live C3 wrapper seeds have already absorbed the C4 names
for current-slot stepping, facing other resolved slots toward the current slot,
area-bounds setup, current-anchor entity spawning, screen-position callbacks,
and passive no-op callback returns.

Good next targets:

- move to the next milestone with the current C3 semantics as the baseline
- return later only for targeted, evidence-backed constants or localization
  crosswalk improvements
- continue naming unused C0 wrapper entries as broader C0 polish unless they
  appear in the C3 callback audit

Those refinements will make C3 scripts more readable to ROM hackers without
changing the already byte-equivalent source scaffold.
