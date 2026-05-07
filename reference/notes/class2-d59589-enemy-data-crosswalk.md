# Class2 D59589 Enemy Data Crosswalk

This note captures the strongest current crosswalk between our local `D5:9589` record family and the `ebsrc` enemy configuration data.

See also [class2-005e-record-domain.md](notes/class2-005e-record-domain.md).
See also [class2-reflected-hit-side-token-consumers.md](notes/class2-reflected-hit-side-token-consumers.md).

## Main result

`D5:9589` is now very likely the base of EarthBound's enemy configuration table.

The case rests on three independent matches:

- local code uses `C0:8FF7` with selector `#$005E`, so the records have stride `0x5E`
- the `ebsrc` reference defines `.STRUCT enemy_data` with size `0x5E`
- local text extraction from `D5:9589 + 1` decodes directly to enemy names

That is much stronger than a loose naming similarity.

## Local name check

Using [extract_ebtext.py](tools/extract_ebtext.py) on the local ROM:

- `D5:958A` -> `null`
- `D5:95E8` -> `Insane Cultist`
- `D5:9646` -> `Dept. Store Spook`
- `D5:96A4` -> `Armored Frog`
- `D5:9702` -> `Bad Buffalo`

Those addresses are exactly `D5:9589 + 1 + n * 0x5E`.

## Reference struct shape

From `refs/ebsrc-main/ebsrc-main/include/structs.asm`:

- `enemy_data::the_flag` is byte `0`
- `enemy_data::name` is bytes `1..25`
- `enemy_data::encounter_text_ptr` is at `0x2D`
- `enemy_data::death_text_ptr` is at `0x31`
- `enemy_data::music` is at `0x37`
- `enemy_data::final_action` is at `0x4E`
- `enemy_data::final_action_arg` is at `0x54`
- `enemy_data::boss` is at `0x56`
- `enemy_data::row` is at `0x5B`
- `enemy_data::max_called` is at `0x5C`
- `enemy_data::mirror_success` is at `0x5D`

The reference data file is `refs/ebsrc-main/ebsrc-main/src/data/battle/enemies.asm`, where the table is explicitly labeled `ENEMY_CONFIGURATION_TABLE`.

## Best local-to-reference field matches

These are the most convincing behavioral matches so far:

- local `+0x00` article gate -> `enemy_data::the_flag`
- local `+0x2D` text pointer consumer -> `enemy_data::encounter_text_ptr`
- local `+0x31` late text or presentation pointer consumer -> `enemy_data::death_text_ptr`
- local `+0x37` audio cue consumer -> `enemy_data::music`
- local `+0x44` threshold-like byte -> `enemy_data::miss_rate`
- local `+0x4E` late action selector -> `enemy_data::final_action`
- local `+0x54` paired action parameter -> `enemy_data::final_action_arg`
- local `+0x5B` row-sensitive formatter linkage -> `enemy_data::row`
- local `+0x5C` helper behavior compatible with call-for-help style limits -> `enemy_data::max_called`
- local `+0x5D` threshold-like byte -> `enemy_data::mirror_success`

## Why this helps the reflected-hit text work

This crosswalk is especially useful for the battle text notes.

In the late side-token path, `C3:E773` and `C3:E78F`:

- resolve the current id through `#$005E`
- check record byte `+0x00`
- then choose between `"The "` and `"the "`

With the enemy-data match in hand, record byte `+0x00` is no longer just a nameless gating byte. It is very likely `enemy_data::the_flag`, which is exactly the kind of field that would control article insertion for enemy names.

The row-sensitive text cluster also gets stronger, because the same record family carries `enemy_data::row` at `+0x5B`.

## Current safest takeaway

The safest takeaway is:

- `9F8C` behaves like an upstream list of enemy ids
- `D5:9589` behaves like the enemy configuration table those ids index into
- the local battle-side text and action code is consuming real enemy configuration fields, not anonymous battle descriptors

That gives us a much better base for the next round of naming.

## Update: enemy text pointer roles are now sharper

A later cross-check narrowed the two main text-pointer fields considerably.

- `+0x2D` is now best read as `enemy_data::encounter_text_ptr`, i.e. the enemy's battle-start or appearance text pointer
- `+0x31` is now best read as `enemy_data::death_text_ptr`, i.e. the enemy's KO or death text pointer

That change is not just from field names in the reference. The `ebsrc` battle flow uses those exact fields in the expected places:

- `main_battle_routine.asm` fixes attacker name first, then displays `encounter_text_ptr`
- `ko_target.asm` displays `death_text_ptr` in the enemy KO path before clearing consciousness

This strengthens the idea that the local `C1`/`C2`/`C3` name, article, and row-formatting work is part of the same enemy battle text pipeline rather than a separate formatting subsystem.

See also [class2-enemy-text-pointer-consumers.md](notes/class2-enemy-text-pointer-consumers.md).
