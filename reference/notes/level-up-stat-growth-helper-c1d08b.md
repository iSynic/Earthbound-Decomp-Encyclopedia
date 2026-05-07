# Level-Up Stat Growth Helper `C1:D08B`

This note covers the unknown include at `C1:D08B`, immediately before the named `misc/level_up_char.asm` body.

See also [equipped-item-derived-cache-family-c21857-c21e03.md](notes/equipped-item-derived-cache-family-c21857-c21e03.md).
See also [battle-action-stat-change-family-c2b2e0-b5d7.md](notes/battle-action-stat-change-family-c2b2e0-b5d7.md).

## Main Result

`C1:D08B` is the reusable stat-growth delta helper used by the level-up routine at `C1:D109`.

This helper and its caller corridor are now source-backed:

- `src/c1/c1_d08b_compute_level_up_stat_growth_delta.asm` covers `C1:D08B..D109`.
- `src/c1/c1_d109_level_up_character_and_refresh_derived_stats.asm` covers `C1:D109..DC1C`.
- Strict C1 byte-equivalence validation remains `OK`.

## Working Names

- `C1:D08B` = `ComputeLevelUpStatGrowthDelta`
- `C1:D109` = `LevelUpCharacterAndRefreshDerivedStats`

Direct callers are seven repeated call sites inside `C1:D109`, one for each level-up stat lane:

- `C1:D1C0`
- `C1:D248`
- `C1:D2D0`
- `C1:D361`
- `C1:D43C`
- `C1:D524`
- `C1:D5BB`

The surrounding `C1:D109` routine increments the character's level byte at `$99D3 + character_offset`, then applies this helper across the base stat bytes rooted at `$99EA..$99F0`.

## Growth Table

The legacy reference labels the table at `D5:EA5B` as:

- `EB_StatisticGrowthTable`

The table is 28 bytes:

```text
12 05 04 07 05 05 06
0C 03 08 05 02 07 05
0A 06 05 05 03 09 04
15 12 07 03 04 04 03
```

`C1:D109` indexes this table with a per-character, per-stat pattern:

- character index is folded into groups of seven bytes
- the stat lane chooses one byte within that group
- the current base stat byte and that growth-table byte are passed into `C1:D08B`

CoilSnake cross-check: `stats-growth-ness-offense-probe` changed
`stats_growth_vars.yml` row 0 `Offense` from `18` to `19` and produced a single
rebuilt-ROM byte change at `D5:EA5B`. That lands exactly on row 0 offset
`+0x00`, so the editor-facing `Offense` field now joins directly to the local
level-up stat-growth lane reader.

## `C1:D08B` Shape

`C1:D08B` combines:

- the current stat byte from `$21/$22`-adjacent direct-page state
- a growth-table parameter byte
- the current level-related value passed in `A`
- `C0:9032`
- `C4:5F7B(3)`
- `C0:91F4`
- `C3:F2B1`
- `C0:915B`

It computes a signed delta and clamps negative results to `0`.

The important local result is not the exact probability formula yet, but the role is clear: it is the per-stat random/growth-curve increment calculator used during level-up.

## How `C1:D109` Uses It

After each positive delta from `C1:D08B`, `C1:D109`:

- adds the delta into the corresponding base stat byte
- calls the matching derived-stat refresh helper in bank `C2`
- optionally prints a level-up message through `C1:86B1`

The visible refresh calls line up with the already-documented derived cache family:

- `C2:1857`
- `C2:192B`
- `C2:1AEB`
- `C2:1BA4`
- `C2:1D65`
- and sibling stat refresh paths later in the same routine

So `C1:D08B` is best named as a level-up stat growth delta helper, with the exact RNG/curve math still a softer edge.

## Source Polish Follow-Up

2026-05-06: `src/c1/c1_d109_level_up_character_and_refresh_derived_stats.asm`
now names its remaining helper-call surface. The pass covers the signed
fixed-point divide helper at `C0:90E6`, the IQ/Luck derived-stat recalculators
at `C2:1D7D/C2:1C5D`, the C4 bounded-random helper used by max HP/PP growth,
the battle-text display-mode/focus/name-buffer helpers, and the final
Sound Stone melody display tick tail. The `C1:D109..DC1C` source unit now has
no raw helper-call edges.

2026-05-06 follow-up: the same source unit now names its shared `D8C7` cleanup
tail as `ClearBattleTextDisplayModeAndReturn`, replacing the last raw local
branch targets in the level-up source without touching the surrounding mixed
byte-preserved region.
