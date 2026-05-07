# Class2 9F8C Upstream Verification

This note captures the current ROM-first verification status of the `9F8A` / `9F8C` list feeding the battle-side class-`2` family.

See also [class2-source-families-986f-9f8a.md](notes/class2-source-families-986f-9f8a.md).
See also [class2-battlers-table-layout-9f8a-9fac.md](notes/class2-battlers-table-layout-9f8a-9fac.md).
See also [class2-local-enemy-id-to-battler-init-chain.md](notes/class2-local-enemy-id-to-battler-init-chain.md).
See also [class2-005e-record-domain.md](notes/class2-005e-record-domain.md).

## Working Names

- `C0:D323` = `BuildCurrentEnemyBattleIdList`

## Verified locally: `C0:D323` fills `9F8A` and `9F8C`

The local ROM bytes in bank `C0` still confirm the broad structure of the upstream clue.

Current best reading of `C0:D323` through `C0:D4D6`:

- `STZ $9F8A`
- build a pointer through a table rooted in bank `D0`
- iterate entries from that pointer family
- for each accepted entry, write a value into `9F8C + 2 * count`
- increment `9F8A`

That remains solid local evidence that bank `C0` builds a count plus word-list in `9F8A` / `9F8C`.

## The new WRAM-layout match sharpens the names

The new exact WRAM layout match now gives that list a stronger identity.

Local WRAM shape:

- `9F8A` is 2 bytes
- `9F8C` spans the next 32 bytes
- `9FAC` begins the `0x4E`-stride battler region

Reference RAM order:

- `ENEMIES_IN_BATTLE`
- `ENEMIES_IN_BATTLE_IDS` as `16` words
- `BATTLERS_TABLE`

Because the sizes and order match exactly, the best current names are now:

- `9F8A` -> `ENEMIES_IN_BATTLE`
- `9F8C` -> `ENEMIES_IN_BATTLE_IDS`

## Verified locally: bank `C2` reads `9F8C` as an upstream enemy-id list

Bank `C2` still reads `9F8C` as an upstream list of values rather than as battler-local metadata.

Important local reads include:

- `C2:4A1F` -> `LDA $9F8C,X`
- `C2:4CD5` -> `LDA $9F8C`
- `C2:4F0D` -> `LDA $9F8C`
- `C2:F0E6` -> `LDA $9F8C,X`

Several of these paths immediately map the loaded value through `C0:8FF7` with selector `#$005E` and land in the `D5:9589` enemy-data table.

That is a very good fit for `ENEMIES_IN_BATTLE_IDS`.

## New direct local bridge into battler init

The new strongest result is the direct local bridge documented in [class2-local-enemy-id-to-battler-init-chain.md](notes/class2-local-enemy-id-to-battler-init-chain.md).

The short version is:

- local `C2:B6EB` behaves like `BATTLE_INIT_ENEMY_STATS`
- direct callers include `C2:4A24`, `C2:4B07`, `C2:4D01`, `C2:760C`, and several others
- a nearby caller path computes `9FAC + 0x4E * slot` as the target battler base
- that same path loads an enemy id from `9F8C`
- then it calls `C2:B6EB` to fill the battler entry from `D5:9589`

So `9F8C` is no longer just an upstream list near the battler table. It is part of an explicit local enemy-id -> battler initialization chain.

## What this proves and what it does not

What is now solid from local evidence plus the exact WRAM-layout match:

- `9F8A` is a count built by bank `C0`
- `9F8C` is a word-list built by bank `C0`
- bank `C2` consumes that list as upstream ids
- those ids map into the `D5:9589` enemy-data table with stride `0x005E`
- `9FAC` begins the battler-sized `0x4E`-stride row family immediately after the list
- local `C2:B6EB` behaves like the battle enemy-stat initializer
- the best current names are `ENEMIES_IN_BATTLE`, `ENEMIES_IN_BATTLE_IDS`, `BATTLERS_TABLE`, and likely `BATTLE_INIT_ENEMY_STATS`

What is still not fully proven:

- the exact bank-`D0` pointer-family label used by `C0:D323`
- whether every `9F8C` consumer in bank `C2` is best understood as enemy-selection logic versus a more general battle-entry path

## Current safest interpretation

The best current interpretation is:

- bank `C0` builds the current enemy-count and enemy-id list in `9F8A` / `9F8C`
- bank `C2` consumes those ids to reach `D5:9589` enemy-data records
- local `C2:B6EB` uses those ids to initialize battler entries in `9FAC + 0x4E * n`

That is materially stronger than the older wording that treated `9F8C` as only a generic upstream structured source list.

## Best next target

The best next move is to trace one of the `C2:B6EB` caller families like `C2:4D01` or `C2:760C`, because that should tell us what gameplay situations are causing battlers to be initialized or reinitialized after the enemy-id list already exists.
