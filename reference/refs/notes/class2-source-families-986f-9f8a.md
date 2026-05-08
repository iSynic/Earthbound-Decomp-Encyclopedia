# Class2 Source Families 986F And 9F8A

This note captures the current ROM-first model for the source-side families feeding the battler-side class-`2` setup work.

See also [class2-candidate-table-9fac.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-candidate-table-9fac.md).
See also [class2-battlers-table-layout-9f8a-9fac.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battlers-table-layout-9f8a-9fac.md).
See also [class2-005e-record-domain.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-005e-record-domain.md).

## Main correction

The earlier wording here treated `9F8A` and `9F8C` as a generic upstream count and source list feeding a separate candidate domain.

That is no longer the best read.

The stronger current interpretation is:

- `9F8A` is very likely `ENEMIES_IN_BATTLE`
- `9F8C` is very likely `ENEMIES_IN_BATTLE_IDS`
- `9FAC` is very likely the beginning of `BATTLERS_TABLE`

The exact WRAM sizes and order match the reference RAM layout perfectly.

## `986F` still behaves like a six-entry source family for setup

The setup passes around `C2:4958` and `C2:4A80` still repeatedly read from the `986F` family.

Current best reading:

- `986F + index` is a six-entry source byte family used during battle-side setup
- the setup passes iterate source indices `0..5`
- values below `4` go through one helper path
- values `4` and `5` go through richer setup paths that seed battler-facing state

So `986F` still looks like an upstream selector family. What changes is that the destination is better described as battler slots rather than abstract candidates.

## `983C` still looks like a source-side mapping table

The setup passes also use `983C` and `D5:8F23` when seeding values that later line up with battler-field offsets.

Current best reading:

- `983C` is a source-side mapping or subtype table tied to the `986F` family
- it contributes setup-time values to the battler-side working state rather than to an abstract candidate pool

## `9F8A` and `9F8C` now have a stronger local identity

The older note correctly observed that:

- `9F8A` behaves like a count
- `9F8C` behaves like an upstream id list

The newer WRAM-layout match strengthens that substantially.

Current best reading:

- `9F8A` is the current enemy count in battle
- `9F8C` is the list of enemy ids or battle-entry ids for those enemies
- later bank-`C2` logic consumes those ids while preparing and selecting battler slots in `9FAC + 0x4E * n`

## Verified upstream note for `9F8A` and `9F8C`

See [class2-9f8c-upstream-verification.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-9f8c-upstream-verification.md) for the direct verification writeup.

The short version is:

- local bank `C0` bytes do verify that `C0:D323` builds `9F8A` and `9F8C`
- local bank `C2` bytes do verify that `9F8C` is consumed as that list during later setup and control flow
- the new exact WRAM layout match now makes `ENEMIES_IN_BATTLE` / `ENEMIES_IN_BATTLE_IDS` the best current names for those variables

## `9FF0` still behaves like a battler-local ranking byte

The ranking passes in `C2:F980+` and `C2:FA30+` repeatedly compare byte `9FF0` when choosing outputs for the `ADxx` tables.

With the corrected battler-table model, this is best read as a battler-local ranking or priority byte rather than as metadata in a separate candidate record family.

## Current safest model

Putting the source-side clues together:

- `986F` is a six-entry setup selector family
- `983C` helps map those setup entries into battle-side state
- `9F8A` is very likely `ENEMIES_IN_BATTLE`
- `9F8C` is very likely `ENEMIES_IN_BATTLE_IDS`
- the `9F8C` values map into the `D5:9589` enemy-data table with stride `0x005E`
- later class-`2` logic is layered on top of battler slots in `9FAC + 0x4E * n`

## Best next target

The best next move is to tighten one direct local path that turns a `9F8C` enemy id into a concrete battler base in `9FAC`, so the enemy-id list and battler-table model can be tied together by explicit local control flow instead of just by exact WRAM layout and repeated field matches.
