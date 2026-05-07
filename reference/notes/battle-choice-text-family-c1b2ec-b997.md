# Battle Choice Text Family `C1:B2EC .. B997`

This note captures the current best local model for the battle-side `C1:B2EC / B450 / B86E / B88C / B997` family that reuses the `AC4A .. AD26` context-buffer helpers.

See also [battle-text-context-buffer-family-c1ac4a-ad42.md](notes/battle-text-context-buffer-family-c1ac4a-ad42.md).
See also [class2-battle-text-cluster-overview.md](notes/class2-battle-text-cluster-overview.md).
See also [battle-psi-user-selection-front-end-c1b5b6-b7c6.md](notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md).
See also [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md).
See also [battle-psi-ability-table-d58a50.md](notes/battle-psi-ability-table-d58a50.md).
See also [battle-targetting-resolver-c1adb4-af50.md](notes/battle-targetting-resolver-c1adb4-af50.md).
See also [battle-selection-snapshot-export-c2b930.md](notes/battle-selection-snapshot-export-c2b930.md).

## Main result

These callers are not just stray battle-text wrappers.

The first `D5:7B68` action-row lane at `C1:B2EC..B5B6` is now promoted into byte-equivalent source as part of `src/c1/c1_adb4_determine_battle_targetting.asm`.
The adjacent PSI-row lane at `C1:B850..BB06` is now source-backed as part of `src/c1/c1_b5b6_open_battle_psi_user_selection.asm`.

The strongest current local read is that this strip is a battle-side choice or targeting text family that:

- refreshes live attacker and target name buffers through `C1:AC4A` and `C1:ACA1`
- stages the current one-byte substitution through `C1:ACF8`
- selects a text pointer from one of two battle-side row tables
- displays that text through the ordinary `C1:86B1` path
- exports a larger row- and battler-facing snapshot through `$A972` and the `$9FFA`-rooted block
- later projects row byte `+0x1D` from that exported block back into the live `$99DC` state bytes

So the safest current system-level description is battle choice or targeting text plus associated battle snapshot export.

## Two sibling table lanes

The family splits into two close sibling lanes.

### `B2EC / B450` use `D5:7B68`

`C1:B2D0 .. B5AA` is the cleaner of the two.

The strongest current local model is:

- `C1:B2EC` calls `C1:AC4A` to build the attacker-name buffer
- `C1:B450` calls `C1:ACA1` to build the target-name buffer
- `C1:B2F3` calls `C1:ACF8` to stage the current one-byte substitution
- the family uses row byte `+0x1D` together with the `D5:7B68` table to resolve a text pointer
- that pointer is installed into `$00BC/$00BE` and dispatched through `C0:9279`, then later through `C1:86B1`
- the same row lane also exports a larger side block into `$9FFA` through `C2:B930` and `$A972`
- the family uses `C1:ADB4` as the shared targetting resolver when it needs concrete target-selection state from the associated battle action id

Source polish now aligns this lane with the C2 action-table vocabulary:

- `D5:7B68 + 0x04` is the ordinary action-row text pointer selected by the
  item-use bridge before the choice-text family runs
- `D5:7B68 + 0x08` is the target-choice/payload pointer dispatched by
  `B450/B504`
- `$9FAC` is used as the handoff row for the first `C2:B930` export
- `$9FFA` is the later battle selection snapshot root copied back into live
  `$99DC` party state bytes

The later loops at `B4A8 .. B4E8` and `B550 .. B58E` then copy byte `+0x1D` from that exported block back into the live per-slot state area at `$99DC + slot`.

So this first lane is not only "show some battle text." It also refreshes a live slot-state mirror from the same selected row family.

### `B86E / B88C / B997` use the `D5:8A50` battle PSI ability table

The neighboring `C1:B850 .. BAF1` strip has the same overall shape, but its table source is now on much firmer footing.

The strongest current local model is:

- `C1:B86E` calls `C1:AC4A` to build the attacker-name buffer
- `C1:B88C` and `C1:B997` call `C1:ACA1` to build the target-name buffer
- `C1:B893` calls `C1:ACF8` to stage the current one-byte substitution
- this sibling lane resolves text pointers from the `D5:8A50` battle PSI ability rows rather than directly from `D5:7B68`
- it also exports a larger side block through `C2:B930` and `$A972`, rooted at the `$9FFA` battle selection snapshot block
- it later copies row byte `+0x1D` from that exported block back into `$99DC + slot`
- it shares the same `C1:ADB4` targetting resolver when the chosen PSI row must be turned into concrete battle targetting state

So the two lanes are best treated as siblings rather than unrelated helper accidents.

## `C1:B5B6` is now better understood as the PSI-user front end

The older wording in this note treated `B5B6` mainly as a broader generic battle choice-selection controller.

The healthier current split is now:

- `B5B6 .. B7C6` = outer PSI-user-selection front end
- `B2EC/B450` = `D5:7B68` text-and-export lane
- `B86E/B88C/B997` = PSI-ability text-and-export sibling lane rooted in `D5:8A50`

So this note now links outward to the dedicated front-end note instead of overloading one family note with both layers.

## Why this matters for the `AC4A .. AD26` helpers

This family gives us a concrete ordinary-runtime caller bridge for the buffer helpers that is different from both:

- the `DCxx/DDxx` battle-action display wrappers
- the `D15B .. D76D` level-up and stat-gain narration family

That makes the helper cluster look more reusable and more stable:

- `AC4A/ACA1` are truly general live battle-name buffer builders
- `ACF8` is a generic one-byte battle-text substitution slot
- these helpers are reused by multiple distinct battle text subsystems, not just one narrow display lane

## Current safest interpretation

The safest current summary is:

- `B2EC/B450` and `B86E/B88C/B997` are sibling battle-side text families, not isolated helper callers
- one lane is rooted in `D5:7B68`
- the other is rooted in `D5:8A50`
- both reuse the live attacker and target name buffers and one-byte substitution slot
- both also export row-linked data through the larger `$9FFA`-rooted battle selection snapshot block
- both later project row byte `+0x1D` back into the live `$99DC` slot-state family
- both now have a cleaner bridge into the shared battle targetting resolver at `C1:ADB4`
- the `B2EC/B450` lane now uses the same `D5:7B68 +0x04/+0x08` action-row
  pointer vocabulary as the C2 action dispatch notes

The remaining soft edge is the exact full struct layout of the exported side block and the final user-facing name of the `B2xx/B8xx` controller family. But the runtime shape of this caller cluster is now in good condition.

## Working Names

- `C1:B2EC` = `BuildBattleActionChoiceTextFromActionRow`
- `C1:B450` = `BuildBattleActionTargetChoiceText`
- `C1:B850` = `BuildPsiSelectionSnapshotAndText`
- `C1:B997` = `DisplayBattlePsiActionText`
