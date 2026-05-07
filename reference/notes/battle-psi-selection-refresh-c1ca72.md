# Battle PSI Selection Refresh `C1:CA72`

This note covers the unknown include at `C1:CA72`.

See also [battle-psi-user-selection-front-end-c1b5b6-b7c6.md](notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md).
See also [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md).
See also [battle-psi-ability-table-d58a50.md](notes/battle-psi-ability-table-d58a50.md).

## Main Result

`C1:CA72` is a battle PSI selection refresh helper used by the outer PSI-user-selection front end.

Direct callers:

- `C1:B657 -> C1:CA72`
- `C1:B691 -> C1:CA72`

Both callers sit inside the `C1:B5B6..B7C6` PSI front end, after a current PSI row has been chosen and while the menu is updating display state for that choice.

## Local Shape

`C1:CA72` takes a PSI-table row id in `A` and another display/control value in `X`.

It:

- opens a text/window update scope through `C3:E4D4`
- resolves the active window record from `$8958`, `$88E4`, and a `0x52`-byte stride
- temporarily saves the active window word at window offset `+0x10`
- calls `EF:0115` with the current focus id from `$8958`
- refreshes text/window state through `C3:E4E0`
- calls `C1:C853` with `$9D16`, the currently chosen PSI user
- calls `C1:163C`
- restores the saved active-window word
- repositions the cursor/text location through `C1:04D8` and `C4:38A5`
- prints/controls the extra value passed in `X` through `C1:0FEA`
- resolves the selected `D5:8A50` row with the 15-byte PSI ability stride
- reads the row's PSI id byte `+0`
- prints the PSI family name through `C1:C403`
- clears the temporary printed value through `C1:0FEA(0)`
- refreshes through `C3:E4CA`

The healthiest current name is "PSI selection refresh" rather than a generic row printer, because the helper recomputes both the active user-side metadata (`C1:C853`) and the selected PSI family name (`D5:8A50 + 0 -> C1:C403`).

Source polish follow-up (2026-05-06): `src/c1/c1_ca72_refresh_battle_psi_selection.asm`
now names all helper-call edges: `EF0115_ClearBattleSpriteRowEffects`,
`C3E4E0_TickWindowWithoutInstantPrinting`,
`C1C853_ResolveBattlePsiTargetingMetadata`, `C1163C_FinalizeSelectionMenu`,
`C104D8_GetCurrentTextContextRowState`, `C438A5_SetActiveWindowDescriptorCursorFields`,
`C10FEA_SetActiveWindowTileAttributes`, and `C1C403_PrintPsiFamilyName`.

## Fit With The Existing PSI Menu Model

This fills a small gap between the already-documented pieces:

- `C1:B5B6..B7C6` chooses the user and PSI row
- `C1:C853` refreshes user/metadata state
- `C1:C8BC` formats second-stage PSI rows
- `C1:CA72` refreshes display state for the current selected row
- `C1:C403` prints the PSI family name

So `C1:CA72` belongs to the battle PSI front-end display path, not to the lower category controller at `C1:CC39..CE73`.
