# Battle PSI Menu Controller `C1:CC39 .. CE73`

This note captures the current best local model for the main battle PSI menu controller rooted at `C1:CC39`.

See also [battle-psi-user-selection-front-end-c1b5b6-b7c6.md](notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md).
See also [battle-psi-category-list-family-c1caf5-c1cb7f.md](notes/battle-psi-category-list-family-c1caf5-c1cb7f.md).
See also [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md).
See also [battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md](notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md).
See also [battle-psi-ability-table-d58a50.md](notes/battle-psi-ability-table-d58a50.md).
See also [battle-targetting-resolver-c1adb4-af50.md](notes/battle-targetting-resolver-c1adb4-af50.md).
See also [battle-selection-snapshot-export-c2b930.md](notes/battle-selection-snapshot-export-c2b930.md).

## Main result

`C1:CB7F..CE85` is now source-backed at `src/c1/c1_cb7f_has_battle_psi_category_entries.asm`. The source split keeps `CB7F..CBCD` as the category availability predicate, `CBCD..CC39` as the category-selection setup stage, `CC39..CE73` as the main controller, and `CE73..CE85` as the exit tail.

The strongest current local-plus-reference-backed read is:

- `C1:CC39 .. CE73` is the ordinary battle PSI menu controller
- it first opens a category-selection stage through `C1:CB7F` and `C1:CAF5`
- it then opens a second-stage PSI-entry selection window through `C1:C8BC`
- after selection, it validates PP and targetting from the chosen `D5:8A50` row
- and finally writes the chosen PSI row, associated battle action id, resolved targetting class, and selected target into the live battle-menu selection struct

That is strong enough to promote this strip as the current best local match for reference `BATTLE_PSI_MENU`.

This controller should now be kept separate from the outer PSI-user-selection front end at `B5B6 .. B7C6`. They are adjacent lanes, not the same routine.

## Category stage

The first half of the controller is now fairly clean:

- `CBCD .. CC39` builds the three-entry category selection stage before the controller proper
- `CC39 .. CC46` installs callback pointer `C1:CAF5`
- `CC46 .. CC53` enters the ordinary menu loop through `C1:196A / 1F8A`
- the selected category is staged in local `$02`
- `CC55 -> CE73` is the clean cancel exit when category selection returns `0`
- `CC67 -> C1:CB7F` is the category-availability predicate for the current acting character
- `CC77 -> C1:CAF5` builds the second-stage PSI list for the chosen category

So the safest current split is:

- `CB7F` = can this category be opened right now?
- `CAF5` = build the second-stage PSI list for this category
- `CC39` = category-stage controller above both helpers

## Second-stage PSI entry stage

The next stage is also structurally clear:

- `CC7B .. CC88` installs callback pointer `C1:C8BC`
- `CC88 .. CC96` enters the second-stage PSI entry picker
- the selected PSI-table row index is kept in `Y` and mirrored into local `$1C`
- `CC98 -> CE03` is the second-stage cancel path

The second-stage cancel behavior is healthier now too:

- `CE03` forces local success-state `X = 1`
- `CE17 .. CE1B` immediately tests whether the staged PSI row is zero
- when it is zero, control jumps back to `CC2A`, which is the category-stage restart side

So the safest current read is that cancel from the PSI-entry stage returns to category selection rather than leaving the PSI menu entirely.

## PP guard and entry-side special message

After a PSI row is chosen, `CC9B .. CD1E` validates the acting character's current PP against the associated battle action:

- `CC9B .. CCB6` resolves the chosen `D5:8A50` row and reads associated action id `+4`
- that action id is converted into the associated `D5:7B68` row
- `CCD3 .. CCF2` compares the associated action-row PP cost byte against `char_struct::current_pp_target`

The source now names that shape directly:

- `D5:8A50 + 0x04` = associated battle action id
- `D5:7B68 + 0x03` = PP cost byte
- `$9A1B + party_offset` = current PP target word used by the guard

When current PP is too low:

- `CCF6 .. CD13` opens a small battle text window
- forces temporary display mode `2`
- displays `C8:FAAA`
- then clears the mode and closes the focus window

The reference battle PSI menu file lines up with this path closely enough that the safest current player-facing description is simply:

- this is the ordinary battle PSI “cannot use / not enough PP” guard path

## Name refresh for single-target and row-style PSI

The middle branch at `CD2C .. CD89` is now healthier too.

It only runs when the PSI-table target byte is `1` or `3`, and then:

- re-reads the selected `D5:8A50` row
- resolves its associated `D5:7B68` action row
- checks the associated action direction byte
- for ally-side actions, opens a small temporary window and calls `C1:CA06`

So the safest current read is:

- this is a target-selection-side PSI name refresh path
- it is used for the narrower single-target and row-style lanes before the final targetting handoff

## Final targetting and selection-struct writeback

The back half at `CD8F .. CE73` now has a clean output model.

It re-reads the selected PSI row and then:

- `CDBD -> C1:ADB4`
  - strongest current local match for shared battle targetting resolver `DETERMINE_TARGETTING`
  - takes the associated `D5:8A50 + 4` action id, not the raw PSI target byte
  - resolves that action id against the current acting battler and returns one packed targetting result
- `CDC5 .. CDD6`
  - re-reads associated action id `+4`
  - uses the associated `D5:7B68` direction byte to choose which window group to close
- `CDF6 .. CE01`
  - treats targetting result `0` as failure and restarts the category side
- `CE1E .. CE6B`
  - writes the final chosen values into the live battle-menu selection struct

The current best local-plus-reference-backed field map for those final writes is:

- `+1` = selected PSI-table row id
- `+2..+3` = associated `D5:8A50 + 4` battle action id
- `+4` = resolved targetting class
- `+5` = resolved selected target

The source constants now name those exact output offsets as
`BattleMenuSelectionPsiRowByte`, `BattleMenuSelectionActionWord`,
`BattleMenuSelectionTargettingByte`, and
`BattleMenuSelectionSelectedTargetByte`.

That matches the reference `battle_menu_selection` struct unusually well:

- `param1`
- `selected_action`
- `targetting`
- `selected_target`

This lower controller note should stay distinct from the outer `B5B6 .. B7C6` front end, because the outer lane also seeds a larger `$9FFA`-rooted battle selection snapshot block through `C2:B930`, while `CC39 .. CE73` is best described as the formal 6-byte menu-selection writer.

I am still keeping the local description one notch more behavioral than the reference names, but the fit is now very strong.

## Safest current interpretation

The safest current summary is:

- `CC39 .. CE73` is the ordinary battle PSI menu controller
- it owns both PSI menu stages: category selection and PSI-entry selection
- it relies on `CB7F` and `CAF5` for category validation and entry-list generation
- it relies on `C8BC` for second-stage PSI entry formatting
- it validates current PP against the associated battle action row
- it resolves targetting through `ADB4`
- and it exports the final PSI choice into the live battle-menu selection struct

The remaining soft edge is mostly symbolic polish around the exact targetting flag names and the exact user-facing wording of the insufficient-PP text path, not the controller shape itself.
