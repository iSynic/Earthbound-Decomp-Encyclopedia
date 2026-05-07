# Battle Targetting Resolver `C1:ADB4 .. AF50`

This note captures the current best local model for the battle-side helper rooted at `C1:ADB4`.

See also [battle-psi-menu-controller-c1cc39-ce73.md](notes/battle-psi-menu-controller-c1cc39-ce73.md).
See also [battle-choice-text-family-c1b2ec-b997.md](notes/battle-choice-text-family-c1b2ec-b997.md).
See also [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md).

## Main result

The strongest current local-plus-reference-backed read is:

- `C1:ADB4 .. AF50` is the shared battle targetting resolver
- it takes a `D5:7B68` battle action id in `A`
- it takes the current acting battler or character slot in `X`
- it reads the associated `D5:7B68` row's direction and target bytes
- and it returns one packed targetting-result word containing both a target-class bitfield and a selected-target byte

That is now strong enough to promote this helper as the best current match for reference `DETERMINE_TARGETTING`.

`C1:ADB4..B5B6` is now promoted into byte-equivalent source at `src/c1/c1_adb4_determine_battle_targetting.asm`. The promoted interval contains the resolver itself, the adjacent use-item bridge, and the first action-row battle-choice text lane.

The resolver needed explicit source-emitter CPU-state anchors at the single-target branches because early return paths temporarily switch index width before jumping to the shared return block. The checked-in source validates byte-for-byte after those state anchors.

The follow-up source polish now names the major tables and state lanes used by
the adjacent `AF73..B5B6` strip: `D5:5000` item config rows, `D5:7B68` action
rows, fixed C7 item-use failure text pointers, CF:8985 NPC-config fallback text,
the `$9FFA` battle selection snapshot block, and the `$9FAC` handoff row used
before `C2:B930`.

Source polish follow-up (2026-05-06): `src/c1/c1_adb4_determine_battle_targetting.asm`
now names the resolver's remaining target-selection helper edges:
`C2BAC5_CountFilteredSecondStageRows`, `C45F7B_GetRandomLessThanA`, and
`C127EF_RunCharacterSelectionPromptWithCallback`. The module now has no raw
helper-call edges.

## Direct caller family

Pinned direct callers are now:

- `C1:B2A3 -> C1:ADB4`
- `C1:B79A -> C1:ADB4`
- `C1:CDBF -> C1:ADB4`
- `C1:CF23 -> C1:ADB4`
- `C1:CF88 -> C1:ADB4`

That is a healthy caller mix:

- ordinary battle-choice text and export lanes
- the ordinary battle PSI menu controller
- deeper PSI-menu-side helpers in the same family

So this is clearly not a one-off PSI-only worker.

## Input model

The input side is locally clean.

`ADB4`:

- treats input `A` as a battle action id
- multiplies that id by the 12-byte `D5:7B68` row stride
- reads the row's leading direction byte
- then reads the row's target byte at `+1`

The reference `determine_targetting.asm` matches this unusually closely, including the same direction-first split and the same target-type ladder.

## Direction split

The direction split is now strong enough to summarize directly.

When the action direction byte is:

- `0` = enemy-targetting PSI-style lane
- `1` = ally-targetting PSI-style lane
- anything else = immediate return side through `AF50`

Within those two live lanes, the target byte then selects the targetting subtype.

## Target byte ladder

The local byte ladder matches the reference targetting helper closely enough that the safest current mapping is:

- `0` = single-target default or none-style lane
- `1` = single target
- `2` = random single target
- `3` = row or grouped lane on the enemy side, all-target fold-in on the ally side
- `4` = all target

The exact branch shapes differ slightly between enemy and ally handling, but the broad target-type mapping is now very healthy.

## Output model

The return shape is the most useful local result.

At the end of `AF50 .. AF73`, the helper:

- keeps one byte in local `$01` as the selected target id
- keeps one byte in local `$16` as the targetting-class selector
- converts the targetting-class selector through `C0:923E`
- ORs that result with the selected-target byte
- and returns the packed word in `A`

So the safest current read is:

- low byte = selected target id
- upper bits = targetting-class flags or targetted-group bitfield

That fits the reference return path exactly enough for the helper identity to be considered stable even though the exact bit names still rest partly on the reference constants.

## Why this matters for the PSI menu notes

This helper is the bridge that keeps the PSI menu notes honest.

In `C1:CC39 .. CE73`, the ordinary battle PSI controller:

- reads associated battle action id `D5:8A50 + 4`
- passes that action id into `C1:ADB4`
- and then splits the returned packed targetting result into final selection-struct fields

So the PSI controller is not deriving final targetting directly from PSI-table byte `+3`. It relies on the associated battle action row through this shared resolver.

## Safest current interpretation

The safest current summary is:

- `ADB4 .. AF50` is the shared battle targetting resolver
- it is the strongest current local match for reference `DETERMINE_TARGETTING`
- it operates over `D5:7B68` action rows, not directly over `D5:8A50`
- it is shared by ordinary battle choice text, PSI-menu-side helpers, and the main battle PSI menu controller

The remaining soft edge is mostly the exact symbolic names of the returned targetting flag bits, not what the helper fundamentally does.

## Adjacent Use-Item Bridge Boundary

The `C1:AF73` tail is still physically in the same source module, but its
runtime role is clearer now.

Current safest source-backed read:

- resolve the selected item id through `C3:E977`
- index `D5:5000` with stride `0x27`
- use item config byte `+0x19` to choose the use lane
- use item config byte `+0x1C` for per-character usability checks
- use item config word `+0x1D` as the associated `D5:7B68` action id
- choose either an action-row text pointer, a fixed C7 failure text pointer, or
  a CF:8985-derived fallback pointer
- when targetting succeeds, flow into the `B2EC/B450` battle-choice text and
  `$9FFA` snapshot export family

This keeps `AF73` connected to `ADB4`, but it no longer needs to be described
as an anonymous tail after the targetting resolver.

## Working Names

- `C1:ADB4` = `DetermineBattleTargetting`
- `C1:AF73` = `UseItemBattleOrFieldBridge`
