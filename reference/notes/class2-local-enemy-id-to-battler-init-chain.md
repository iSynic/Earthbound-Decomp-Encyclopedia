# Class2 Local Enemy Id To Battler Init Chain

This note captures the first explicit local chain tying `9F8C`, the `D5:9589` enemy-data table, and the `9FAC + 0x4E * n` battler region together.

See also [class2-battlers-table-layout-9f8a-9fac.md](notes/class2-battlers-table-layout-9f8a-9fac.md).
See also [class2-9f8c-upstream-verification.md](notes/class2-9f8c-upstream-verification.md).
See also [class2-d59589-enemy-data-crosswalk.md](notes/class2-d59589-enemy-data-crosswalk.md).
See also [class2-b6eb-caller-family-4dxx.md](notes/class2-b6eb-caller-family-4dxx.md).
See also [class2-b6eb-caller-family-760c.md](notes/class2-b6eb-caller-family-760c.md).

## Working Names

- `C2:B6EB` = `InitializeEnemyBattlerStatsFromEnemyId`

## Main result

We now have a real local initializer body plus real local callers that tie the model together.

Current safest local chain:

1. bank `C0` builds `9F8A` and `9F8C`
2. bank `C2` computes battler bases in `9FAC + 0x4E * n`
3. bank `C2` calls local `C2:B6EB`
4. `C2:B6EB` maps an enemy id through the `D5:9589` table with stride `0x5E`
5. `C2:B6EB` clears and fills a `0x4E` battler-sized struct at the supplied base

That is the direct local bridge we were missing.

## Local `C2:B6EB` matches `BATTLE_INIT_ENEMY_STATS`

The body at `C2:B6EB` is a very close local match for the reference `BATTLE_INIT_ENEMY_STATS` routine.

Important local byte shape:

- prologue begins at `C2:B6EB`
- stores incoming target base in `$02`
- stores incoming enemy id in `Y` and local `$0F`
- builds `D5:9589 + enemy_id * 0x5E`
- clears a `0x4E` struct at the supplied base through `C0:8EFC`
- reads enemy-data fields and stores them into battler offsets

Strong local field writes include:

- `+0x00` <- enemy id
- `+0x4C` <- enemy id copy
- `+0x02` <- sprite
- `+0x0B` <- result of `C2:B66A` -> matches `the_flag`
- `+0x0C` <- `1` -> matches `consciousness`
- `+0x0E` <- `1` -> matches enemy-side `ally_or_enemy`
- `+0x0F` <- `0` -> matches `npc_id`
- `+0x10` <- enemy-data `row`
- `+0x11/+0x13/+0x15` <- enemy-data HP copied into `hp / hp_target / hp_max`
- `+0x17/+0x19/+0x1B` <- enemy-data PP copied into `pp / pp_target / pp_max`

That is much too close to the reference initializer to treat as coincidence.

Source follow-up (2026-05-06): the initializer now calls `C2:B66A` by the
`ReadBattlerNameVariantFlag` contract used by the C2 battle-text context
builders.

Second source follow-up (2026-05-06): the initializer and the player snapshot
exporter now share the C1-backed `C2:B608` /
`ConvertElementalResistanceByte` and `C2:B639` /
`ConvertStatusResistanceByte` names. The transform lane is no longer just
"compact stat" plumbing: enemy-data bytes `+0x3F/+0x40` and party bytes
`+0x52/+0x53` feed the fire/freeze resistance mirrors, while enemy-data bytes
`+0x41/+0x42/+0x43` and party bytes `+0x54/+0x55/+0x56` feed the flash,
paralysis, hypnosis, and inverse brainshock resistance mirrors.

Third source follow-up (2026-05-06): the initializer now names the initial
timed-shield/substate seed path. Enemy-data byte `+0x59` dispatches through
`C2:9CDC` / `ApplyTimedSubstateOrRefreshShieldCounter` for values `1..4`,
installing the same row `+0x23/+0x25` shield-family state used by the selected
row timed-substate action leaves.

## Direct local callers of `C2:B6EB`

The direct caller scan now finds 12 direct call sites to `C2:B6EB`.

Important bank-`C2` callers include:

- `C2:49B1`
- `C2:4A24`
- `C2:4B07`
- `C2:4D01`
- `C2:4D54`
- `C2:760C`
- `C2:7C76`
- `C2:8C45`
- `C2:C0BF`
- `C2:C17D`
- `C2:C359`

There is also one bank-`C1` caller at `C1:E457`.

So this is clearly a live shared initializer, not a one-off analog.

## One explicit local enemy-id -> battler-base call path

The clearest compact local chain is at `C2:4A18+`.

Current safest read:

- `A4 31 / 98 0A / AA / BD 8C 9F` loads one entry from `9F8C`
- `A6 1F` supplies a previously computed battler base in `X`
- `22 EB B6 C2` calls `C2:B6EB`

The matching base computation is visible in the nearby setup logic:

- `A0 4E 00 / 22 F7 8F C0 / 18 69 AC 9F / AA`
- that is exactly `index * 0x4E + 0x9FAC`

So this local path is doing the same high-level work as the reference battle setup loops:

- choose a battler slot
- compute `9FAC + 0x4E * slot`
- load enemy id from `9F8C`
- initialize that battler from enemy data

## Caller-family split now looks meaningful

The caller families no longer all look the same.

Current safest split:

- the `4Dxx -> 4Fxx` family now looks best as a battle-start enemy-group initialization path that later displays encounter text and enemy start-of-battle status lines
- the `760C` caller family is now source-backed as a separate selected-battler collapse/companion rebuild case that uses scratch battler base `$A180` and special enemy id `0xD5`

See [class2-b6eb-caller-family-4dxx.md](notes/class2-b6eb-caller-family-4dxx.md) for the corrected `4Dxx` read.
See [class2-b6eb-caller-family-760c.md](notes/class2-b6eb-caller-family-760c.md) for the corrected `760C` read.

## Why this upgrades the earlier RAM-layout note

Before this step, the `9F8A / 9F8C / 9FAC` interpretation was already strong because of the exact RAM layout match.

Now the local control flow itself supports the same model:

- `9F8C` is not just near the battler table, it is actually used as the enemy-id input to the battler initializer
- `9FAC + 0x4E * n` is not just the right shape, it is actually used as the initializer target base
- `C2:B6EB` is the missing local bridge from enemy ids into battler entries

That moves the model from "exactly matching layout and fields" to "explicit local initialization chain."

## Current safest takeaway

The safest takeaway is:

- `9F8C` is very likely `ENEMIES_IN_BATTLE_IDS`
- `9FAC` is very likely `BATTLERS_TABLE`
- local `C2:B6EB` is very likely `BATTLE_INIT_ENEMY_STATS`
- at least one local caller path already shows the full chain `9F8C enemy id -> C2:B6EB -> 9FAC + 0x4E * n battler`
- the `4Dxx` caller family now reads more like battle-start enemy-group setup than like a call-for-help helper
- the `760C` caller is a separate selected-row companion rebuild route, not part of the battle-start family

That is the strongest local confirmation yet for the battle RAM model.

## Best next target

The best next move is to trace the setup that feeds `$4DBC` and `$1D` in the `4Dxx -> 4Fxx` family, or refine the exact gameplay identity of the `0xD5` companion rebuilt by the `760C` selected-row route.
