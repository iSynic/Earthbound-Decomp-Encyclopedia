# Class2 005E Record Domain

This note captures the current ROM-first model for the structure family reached when bank `C2` maps `9F8C` entries through `C0:8FF7` with selector `#$005E`.

See also `notes/class2-d59589-enemy-data-crosswalk.md`.
See also `notes/class2-record-consumer-families.md`.
See also [class2-battle-start-extra-message-state-4dbc-aa10.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battle-start-extra-message-state-4dbc-aa10.md).

## Current strongest claim

The old "anonymous descriptor" label is now too weak.

The best current reading is:

- `C0:8FF7` is a generic hardware-multiplier scaled-index helper
- selector `#$005E` is the stride for a real fixed-size record family
- the `D5:9589` root is now very likely the enemy configuration table
- the records reached there line up unusually well with the `ebsrc` `enemy_data` struct and `ENEMY_CONFIGURATION_TABLE`

This is no longer just a size match. Multiple offsets that we previously inferred from local behavior now line up exactly with named enemy fields.

## Why the enemy-data interpretation is strong

Three independent anchors now agree:

- local ROM code repeatedly maps ids through `#$005E` and then reads fields from `D5:9589 + offset`
- the `ebsrc` reference defines `.STRUCT enemy_data` with `.SIZEOF(enemy_data) = 0x5E`
- local text extraction from `D5:9589 + 1` decodes padded enemy names exactly as expected

The local name extraction check is especially useful because it comes straight from our own ROM bytes:

- `D5:958A` decodes to `null`
- `D5:95E8` decodes to `Insane Cultist`
- `D5:9646` decodes to `Dept. Store Spook`
- `D5:96A4` decodes to `Armored Frog`
- `D5:9702` decodes to `Bad Buffalo`

That makes the `D5:9589` root feel much more like a real enemy table than a generic battle descriptor bank.

## `C0:8FF7` is still a generic scaled-index helper

The local bytes at `C0:8FF7` show a small helper that uses SNES hardware multiplier registers at `$4202` and `$4216`.

The important structural point is unchanged:

- it is not specific to the class-`2` family
- it combines the caller's `A` value with the caller's `Y` value to produce a scaled offset
- selector `#$005E` therefore behaves like a record stride rather than a semantic mode by itself

## Representative local consumers

Representative local `C2` paths still include:

- `C2:4A4B` / `C2:4CD5` reading `D5:9589 + 0x37`
- `C2:4D7D..4E3C` reading `D5:9589 + 0x57` and `+0x58`
- `C2:4F0D` reading `D5:9589 + 0x2D`
- `C2:7680+` reading `D5:9589 + 0x31`
- `C2:78B8+` reading `D5:9589 + 0x4E` and `+0x54`
- `C2:F0E6` reading `D5:9589 + 0x1C`
- `C3:E773` / `C3:E78F` checking `D5:9589 + 0x00`

Those caller groups are exactly the kind of scattered field accesses we would expect if `9F8C` holds enemy ids and bank `C2` is consuming enemy configuration data indirectly.

## Confirmed or strongly matched field offsets

The most useful crosswalk so far is:

- `+0x00` -> `enemy_data::the_flag`
- `+0x1C` -> `enemy_data::battle_sprite`
- `+0x20` -> `enemy_data::run_flag`
- `+0x21` -> `enemy_data::hp`
- `+0x25` -> `enemy_data::exp`
- `+0x29` -> `enemy_data::money`
- `+0x2D` -> `enemy_data::encounter_text_ptr`
- `+0x31` -> `enemy_data::death_text_ptr`
- `+0x37` -> `enemy_data::music`
- `+0x3A` -> `enemy_data::defense`
- `+0x3C` -> `enemy_data::speed`
- `+0x44` -> `enemy_data::miss_rate`
- `+0x4E` -> `enemy_data::final_action`
- `+0x54` -> `enemy_data::final_action_arg`
- `+0x56` -> `enemy_data::boss`
- `+0x57/+0x58` -> still tentative locally despite the strong overall enemy-data match
- `+0x5A` -> `enemy_data::death_type`
- `+0x5B` -> `enemy_data::row`
- `+0x5C` -> `enemy_data::max_called`
- `+0x5D` -> `enemy_data::mirror_success`

Some of those are now exact matches to behaviors we had already inferred locally:

- `+0x2D` acting like a text pointer now matches `encounter_text_ptr`
- `+0x31` acting like a second text or presentation pointer now matches `death_text_ptr`
- `+0x37` acting like an audio cue id now matches `music`
- `+0x4E` acting like a late battle-action selector now matches `final_action`
- `+0x54` acting like its paired parameter now matches `final_action_arg`
- `+0x44` acting like a threshold-like byte now matches `miss_rate`
- `+0x5D` acting like a count or threshold byte now matches `mirror_success`

## Where our earlier guesses were off

A few of the older field guesses were directionally useful but semantically wrong:

- `+0x25` is not a generic accumulated size field; it matches the 32-bit EXP field
- `+0x29` is not a generic contribution byte; it matches the money reward field
- `+0x56..+0x5D` are not a completely abstract control tail; most of them line up with real enemy properties
- `+0x5C` is not just a scaling selector; it matches `max_called`, which also fits the local summon-style behavior much better

The main remaining caution is the `+0x57/+0x58` pair.

A newer local read at `C2:4D7D..4E3C` shows those two bytes participating directly in a battle-start extra-message or selector path. That does not fit cleanly with the borrowed reference names we had been using there, so those two field names should remain tentative until we verify them more directly.

## Why this matters for the battle-text path

This crosswalk sharpens the reflected-hit and late formatting work too.

A particularly good anchor is the side-token path in bank `C3`:

- `C3:E773` / `C3:E78F` resolve the current id through `#$005E`
- they check record byte `+0x00`
- the reference enemy struct names byte `+0x00` as `the_flag`

That means the article-insertion gate we were already tracing now sits directly on top of a field explicitly meant to control `The`-style article behavior for enemy names.

The row-text side gets sharper as well, because `enemy_data::row` is at `+0x5B`, right where our local battle-row phrase work was already pointing.

## Current safest interpretation

The safest interpretation is now:

- bank `C0` builds an upstream id list in `9F8C`
- bank `C2` maps those ids into the enemy configuration table at `D5:9589`
- bank `C2` and bank `C3` consume enemy fields for battle text, audio, late action dispatch, row-sensitive formatting, and battle-start message control

So the subsystem is no longer best described as "class-2 candidate records that happen to look battle-like." It now looks like a battle-side pipeline consuming enemy configuration records through an indirect id list.

## Best next target

The best next move is to keep tightening how `enemy_data::the_flag` and `enemy_data::row` feed the late text path, or to trace the battle-start consumer for `enemy_data + 0x57/+0x58` far enough to decide what those two tail bytes really represent locally.
