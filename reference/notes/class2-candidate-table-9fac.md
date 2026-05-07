# Class2 Candidate Table 9FAC

This note captures the corrected current model for the 32-entry WRAM domain rooted at `9FAC`.

See also [class2-battlers-table-layout-9f8a-9fac.md](notes/class2-battlers-table-layout-9f8a-9fac.md).
See also [class2-mask-helper-family.md](notes/class2-mask-helper-family.md).

## Major correction

The older reading of `9FAC` as a generic candidate-record pool with several nearby parallel metadata arrays is no longer the best model.

The stronger current reading is:

- `9FAC` is very likely the start of `BATTLERS_TABLE`
- the domain really is 32 entries because the battle system has 32 battler slots
- the stride is exactly `0x4E`, which matches `.SIZEOF(battler)` in the `ebsrc` reference

So the mask helper family is best understood as operating over battler slots, not over an abstract candidate pool.

## Why the correction is strong

The exact local WRAM pattern we had already established was:

- `9F8A` as a 2-byte count-like value
- `9F8C` as a 32-byte upstream id list
- `9FAC + 0x4E * n` as the 32-entry row family

The reference RAM layout matches that pattern exactly:

- `ENEMIES_IN_BATTLE` is 2 bytes
- `ENEMIES_IN_BATTLE_IDS` is 32 bytes
- `BATTLERS_TABLE` begins immediately after that block
- `.SIZEOF(battler) = 0x4E`

That means the local domain is now much more naturally explained as battlers.

## What the nearby addresses now look like

Several nearby addresses that we used to describe as separate candidate arrays are better read as battler-field offsets from `9FAC`.

Examples:

- `9FB8 = 9FAC + 0x0C` -> `battler::consciousness`
- `9FBA = 9FAC + 0x0E` -> `battler::ally_or_enemy`
- `9FBB = 9FAC + 0x0F` -> `battler::npc_id`
- `9FBC = 9FAC + 0x10` -> `battler::row`
- `9FC9 = 9FAC + 0x1D` -> `battler::afflictions`

So several earlier per-address interpretations should now be read as battler-field observations rather than as truly independent arrays.

## What still survives from the older note

The higher-level behavioral observations still matter, but their framing changes.

The family still:

- operates over a 32-bit working target set using one-hot masks from `C4:A279`
- repeatedly filters entries using active-presence, state, and affliction-like fields
- exports selected results into `ADxx` working tables
- mixes mask algebra with later controller and battle-text dispatch behavior

What changes is the entity being filtered. Those are no longer best described as anonymous candidates. They are best described as battler slots or battler-backed rows.

## Current safest interpretation

The safest current interpretation is:

- the class-`2` mask helper family operates over battler slots in `BATTLERS_TABLE`
- the earlier `9FAC` candidate-domain language should now be read as battler-domain language
- many of the nearby byte tests are most naturally battler-field tests rather than free-floating candidate metadata

## Best next target

The best next move is to tighten one direct local iterator or base-computation path over `9FAC`, so the battler-table reading can be stated from local control flow as well as from the exact WRAM layout match.
