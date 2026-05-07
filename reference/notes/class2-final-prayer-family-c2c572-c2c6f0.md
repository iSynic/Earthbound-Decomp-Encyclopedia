# Class2 Final Prayer Family C2C572 C2C6F0

This note captures the strongest current local model for the late `D5:7B68` prayer-result ladder at `C2:C572..C2:C6F0`.

See also [class2-d57b68-battle-action-table-match.md](notes/class2-d57b68-battle-action-table-match.md).
See also [class2-d57b68-early-entry-name-crosswalk.md](notes/class2-d57b68-early-entry-name-crosswalk.md).
See also [class2-special-event-results-c29298-c2c14e.md](notes/class2-special-event-results-c29298-c2c14e.md).

## Working Names

- `C2:C572` = `RunFinalPrayerOpeningTransition`
- `C2:C5D1` = `RunFinalPrayerDamagePhase2`
- `C2:C5FA` = `RunFinalPrayerDamagePhase3`
- `C2:C623` = `RunFinalPrayerDamagePhase4`
- `C2:C64C` = `RunFinalPrayerDamagePhase5`
- `C2:C675` = `RunFinalPrayerDamagePhase6`
- `C2:C69E` = `RunFinalPrayerDamagePhase7`
- `C2:C6D0` = `RunFinalPrayerNarrativePhase8`
- `C2:C6F0` = `RunFinalPrayerFinale`

## Main result

The live `D5:7B68` rows `291..299` are not generic late special-event handlers.

They are a real prayer-result ladder in the Giygas endgame battle:

- entry `291` -> `C2:C572` -> strongest local fit for `FINAL_PRAYER_1` / `BTLACT_GIYGAS_PRAYER_1`
- entry `292` -> `C2:C5D1` -> strongest local fit for `FINAL_PRAYER_2` / `BTLACT_GIYGAS_PRAYER_2`
- entry `293` -> `C2:C5FA` -> strongest local fit for `FINAL_PRAYER_3` / `BTLACT_GIYGAS_PRAYER_3`
- entry `294` -> `C2:C623` -> strongest local fit for `FINAL_PRAYER_4` / `BTLACT_GIYGAS_PRAYER_4`
- entry `295` -> `C2:C64C` -> strongest local fit for `FINAL_PRAYER_5` / `BTLACT_GIYGAS_PRAYER_5`
- entry `296` -> `C2:C675` -> strongest local fit for `FINAL_PRAYER_6` / `BTLACT_GIYGAS_PRAYER_6`
- entry `297` -> `C2:C69E` -> strongest local fit for `FINAL_PRAYER_7` / `BTLACT_GIYGAS_PRAYER_7`
- entry `298` -> `C2:C6D0` -> strongest local fit for `FINAL_PRAYER_8` / `BTLACT_GIYGAS_PRAYER_8`
- entry `299` -> `C2:C6F0` -> strongest local fit for `FINAL_PRAYER_9` / `BTLACT_GIYGAS_PRAYER_9`

The local message side, row ordering, phase writes through `$A97A`, and the `ebsrc` prayer action files all line up unusually well.

## Why the family is strong locally

All nine rows share the same unusual front shape:

- direction `enemy`
- target `none`
- type `other`
- message blocks starting with `"[user] prayed ... from bottom of her heart!"`

Rows `291..298` also form a tight body ladder:

- each loads one prayer message pointer into `$0E/$10`
- each routes through a shared setup helper at `C2:C37A` or `C2:C41F`
- each writes a consecutive phase value into `$A97A`

That is already much stronger than a loose thematic match.

Source follow-up (2026-05-06): the row bodies now call the shared helpers by
their promoted contracts: `RunFinalPrayerStageTransition`,
`ApplyFinalPrayerDamageStep`, and `RunFinalPrayerNarrativeTransition`.

## `C2:C572` is the opening prayer setup

Entry `291` uses text `C9:F0B8`, which begins:

- `[user] prayed`
- `from bottom of her heart!`

Its body is richer than the later prayer damage rows:

- loads `C7:BC96` and calls `C2:C37A` with `X = 0x00B9`, `A = 0x01DE`
- waits `0x78`
- queues the `0x40` presentation cue through `C0:ABE0` /
  `QueueSoundEffectOrPlayApuPort3Cue`
- waits `0x1E`
- writes `$AD8C = 0x003C`, `$AD8E = 0x000C`
- displays `C9:F86A` through `C1:DC1C`
- writes `$A97A = 5`
- calls `C2:C32C` with `0x01E5`
- calls `C2:C21F` / `ApplyFinalPrayerBattleVisualSelector` with `X = 0`,
  `A = 0x01DF`

So the healthiest local read is:

- `C2:C572` is the opening final-prayer transition, not a plain damage step

## `C2:C5D1..C2:C69E` are the main prayer damage ladder

Entries `292..297` are structurally very regular:

- `C2:C5D1` loads `C7:BA2C`, calls `C2:C37A`, then `C2:C3E2(0x0032)`, then writes `$A97A = 6`
- `C2:C5FA` loads `C7:BAC7`, calls `C2:C37A`, then `C2:C3E2(0x0064)`, then writes `$A97A = 7`
- `C2:C623` loads `C7:BB38`, calls `C2:C37A`, then `C2:C3E2(0x00C8)`, then writes `$A97A = 8`
- `C2:C64C` loads `C7:BBF3`, calls `C2:C37A`, then `C2:C3E2(0x0190)`, then writes `$A97A = 9`
- `C2:C675` loads `C7:BC56`, calls `C2:C37A`, then `C2:C3E2(0x0320)`, then writes `$A97A = 10`
- `C2:C69E` loads `C7:B9A1`, calls `C2:C37A`, then `C2:C3E2(0x0640)`, then writes `$A97A = 11`

Those amounts are the strongest local fit for the doubling prayer-damage constants in `ebsrc`:

- `0x32`, `0x64`, `0x00C8`, `0x0190`, `0x0320`, `0x0640`
- `50`, `100`, `200`, `400`, `800`, `1600`

That makes the common role of `C2:C3E2` much healthier here too:

- strongest current local fit for the prayer-damage worker later named `GIYGAS_HURT_PRAYER` in `ebsrc`

## `C2:C6D0` is the text-only phase-8 prayer step

Entry `298` uses text `C9:F389`, which is the first prayer message that already reads like a late-stage narrative beat rather than another ordinary encouragement block.

Its body is much smaller than the preceding damage rows:

- loads `C9:F6DE`
- calls `C2:C41F` with `A = 0x004A`
- writes `$A97A = 12`

That matches the reference shape unusually well:

- `BTLACT_GIYGAS_PRAYER_8` is a late prayer text step that advances phase without another visible `GIYGAS_HURT_PRAYER` call

So the safest current local description is:

- `C2:C6D0` is the phase-8 narrative prayer step, not another direct damage wrapper

## `C2:C6F0` is the full final prayer finale

Entry `299` uses text `C9:F3EC`, which immediately shifts from the normal prayer introduction into the long finale sequence.

Its body is much larger than every earlier prayer row:

- calls `C2:0F9A`
- displays four late prayer text blocks through `C2:C41F`
- interleaves four `C2:C3E2` damage calls with `0x0C80`, `0x1900`, `0x3200`, `0x6400`
- calls `C1:DD59` and `C1:DD41`
- toggles `$9643`
- writes `$A97A = -1`
- plays sound `0x00BE`
- iterates the final prayer noise table rooted at `C4:A35D`
- changes music multiple times
- writes `$A97A = 0`
- writes `SPECIAL_DEFEAT = 3`

This is not just a stronger damage row. It is the end-of-battle finale controller.

Source follow-up (2026-05-06): the finale source now names the established
presentation and visual joins for the opening clamp/prep, queued cue dispatch,
sprite-row commits, and layer-1 battle-bg distortion priming instead of leaving
those source-backed edges as raw `C20F9A/C1DD41/C0ABE0/C2F8F9/C2DAE3` calls.

The reference fit is very strong:

- `BTLACT_GIYGAS_PRAYER_9`
- repeated `GIYGAS_HURT_PRAYER` calls for the last four doubling tiers
- final death/static/noise sequence
- final special-defeat write

## Current takeaway

This family is now strong enough to treat as a finished local map:

- `291..299` are the Final Prayer action ladder
- `C2:C572` is the opening prayer transition
- `C2:C5D1..C2:C69E` are the main prayer-damage ladder
- `C2:C6D0` is the phase-8 narrative prayer step
- `C2:C6F0` is the full final prayer finale
- the visible source now names the helper calls that compose those rows instead
  of leaving the common layer as raw `C37A/C3E2/C41F` calls
- the opening and finale bodies now reuse the same presentation cue, sprite,
  and battle-background helper vocabulary as the adjacent C2 visual sources

## What is still open

Still open:

- lower-level visual selector calls inside the prayer transition helpers
