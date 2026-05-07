# C2 Late Selected-Row Runtime Polish

This note records the byte-neutral polish slice for the selected-row continuation
at `C2:7680` and the late controller at `C2:77CA`.

Primary source modules:

- `src/c2/c2_7680_display_enemy_death_text.asm`
- `src/c2/c2_77ca_run_class2_late_selected_row_controller.asm`

Related evidence notes:

- `notes/class2-post-selection-controller-phases.md`
- `notes/class2-late-controller-path-77ca.md`
- `notes/class2-descriptor-field-4e-and-d57b68.md`
- `notes/class2-concrete-battle-text-call-paths.md`
- `notes/c2-selected-row-controller-runtime-polish.md`
- `notes/class2-b6eb-caller-family-760c.md`

## Descriptor Text Continuation

`C2:7680` continues the `C2:7550` startup path with `$02` as the selected
battler row base.

Promoted runtime contract:

- selected battler row id maps through the `0x5E` descriptor domain
- `D5:9589 + 0x31` is read as a battle text pointer
- the pointer is dispatched through `C1:DC1C`
- selected battler `consciousness` byte `+0x0C` is cleared after the text emission
- row `+0x0F` values `0x10/0x11` seed a follow-up active row from the
  `983A/983C` helper tables
- other routes scan battler rows and may clear matching row `+0x10` links
- the embedded `C2:7784` tail is the hardcoded collapse text route reached from
  `C2:7550` when row `+0x0F == 0`
- all descriptor and hardcoded routes rejoin the late controller return tail at
  `C2:7C92`

This keeps the death/collapse text path tied to the enemy/battler descriptor
field instead of only to the raw EF or D5 pointer bytes.

## Late Controller Entry

`C2:77CA` is the late selected-row controller reached from `C2:7550` when
selected-row `+0x0E` is nonzero.

Promoted runtime contract:

- row ids `0xDA`, `0xDB`, `0xDD`, and `0xE5` bypass the late body
- `C2:BAC5(1)` gates the six-entry source claim scan to the single phase-1 row
  case
- the claim scan requires enabled `9FB8`, clear `9FBA`, source-entry
  affliction/status byte `9FC9 != 1`, clear `9FBB`, and clear linked `9A13`
- surviving entries set source byte `9FBF` and linked marker `9A15`
- row-local `+0x3F/+0x41/+0x3D` contributions accumulate into
  `$A974/$A976/$A978`

This documents the late path as a real controller phase, not a failure return.

## Nested Action Pass

When descriptor field `D5:9589 + 0x4E` is nonzero, the late controller runs a
nested action pass:

- set `$AA90 = 1`
- save outer `$A970/$A972` active-row anchors
- save outer `$A96C/$A96E` target mask
- make the current row the active row
- copy descriptor-backed fields into row words `+0x04` and `+0x08`
- run target selection and derived action dispatch
- rebuild the first target text context from the current target mask through
  `C2:3E32`
- emit the first pointer from the selected `D5:7B68` action entry through
  `C1:DC1C`
- apply the companion pointer through `C2:40A4`
- clear `$AA90`
- restore the outer active-row anchors and target mask

That gives the decomp a source-commented bridge from selected-row phase state to
the battle-action descriptor table and second-pointer payload path.

Source follow-up: the late controller now calls `C2:0F9A` as
`ClampHpPpRollTargetsToLiveValues` before the single phase-1 source claim scan,
and calls the newly labeled `C2:3E32` helper as
`BuildFirstTargetTextContextFromCurrentMask` in its nested action pass. The
visual-refresh follow-up now names the same presentation helpers: `C2:FAD8`
stores the color-wave duration in `$B37C`, `C2:FB35` installs per-entry
enemy-sprite color-wave comparison/delta state, and `C2:F8F9` renders and
commits the battle sprite rows after the optional descriptor `+0x5A` active-row
marking route. The same optional visual route now names its `C0:ABE0` cue
dispatch as `QueueSoundEffectOrPlayApuPort3Cue`.

The descriptor text continuation also now names its cross-module control-flow
joins: `C2:7550` jumps to `C2:7784` as
`DisplayHardcodedCollapseTextTail`, while `C2:7680` returns through `C2:7C92` as
`ReturnFromClass2LateSelectedRowController`.

## State And Marker Effects

The later part of `C2:77CA` repeats several selected-row controller motifs:

- fallback text uses `D5:9589 + 0x31`
- row marker `+0x4B` is reset across battler rows and then set on the selected
  row
- row `+0x1D = 1` is reinstalled with sibling state bytes `+0x1E..+0x23`
  cleared
- optional descriptor field `+0x5A` can mark active rows in the `A21C` domain
- `D5` subtype routes clean up or rebuild six-entry source metadata through
  `C2:B6EB`

## Companion Rebuild Join

The `C2:7550` startup body and the `C2:77CA` late body both contain the same
source-entry companion pattern:

- scan the six `0x4E`-stride source entries
- require consciousness/active state and clear npc id markers
- test neighboring affliction byte `+0x1E == 2`
- clear the existing neighbor byte or rebuild scratch battler base `$A180`
  through `C2:B6EB`
- mirror special enemy id `0xD5` through `$A18D/$A18F`

This resolves the old `C2:760C` direct `B6EB` caller as a selected-row
collapse/companion rebuild route. It should stay separate from the `4Dxx`
battle-start enemy initialization family.

## Decomp Value

This slice closes the immediate loop around `C2:7550`:

- startup text and late text now share a documented descriptor-pointer shape
- the late phase is tied to concrete source-entry markers and active-row state
- `D5:7B68` no longer appears only in action dispatch notes; its late-controller
  nested action use is now source-commented too
- the `+0x0E` major phase byte has a direct source boundary between startup and
  late behavior
- the old unresolved `760C` battler-init call now has a local selected-row
  companion rebuild contract
- the collapse/late visual pass now calls the battle-sprite color-wave duration,
  per-entry color-wave state, and render/commit helpers by source-backed names
- the selected-row startup/death-text corridor now names the embedded
  hardcoded-collapse text tail and the shared late-controller return tail

## Remaining Soft Spots

- final gameplay names for row ids `0xDA`, `0xDB`, `0xDD`, and `0xE5`
- exact names for `$A974/$A976/$A978`
- precise gameplay meaning of descriptor field `D5:9589 + 0x5A`
- exact gameplay identity of the special `0xD5` companion rebuilt through
  scratch battler base `$A180`
- whether the now-named hardcoded `C2:7784` tail should be split into its own
  source unit in a later scaffold pass
