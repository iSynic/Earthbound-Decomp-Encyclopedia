# Class2 Battle Text Cluster Overview

This note gives a higher-level map of the currently best-understood `class2` battle-text cluster.

See also:
- [class2-battle-text-dispatch-stack.md](notes/class2-battle-text-dispatch-stack.md)
- [battle-text-entry-family-c1dc1c-dd7c.md](notes/battle-text-entry-family-c1dc1c-dd7c.md)
- [battle-text-entry-tail-dd82-dd9f.md](notes/battle-text-entry-tail-dd82-dd9f.md)
- [class2-concrete-battle-text-call-paths.md](notes/class2-concrete-battle-text-call-paths.md)
- [class2-enemy-text-pointer-consumers.md](notes/class2-enemy-text-pointer-consumers.md)
- [class2-dispatch-family.md](notes/class2-dispatch-family.md)
- [battle-action-stat-change-family-c2b2e0-b5d7.md](notes/battle-action-stat-change-family-c2b2e0-b5d7.md)
- [battle-affliction-recovery-family-c29aea-a39d.md](notes/battle-affliction-recovery-family-c29aea-a39d.md)
- [battle-text-context-buffer-family-c1ac4a-ad42.md](notes/battle-text-context-buffer-family-c1ac4a-ad42.md)
- [battle-choice-text-family-c1b2ec-b997.md](notes/battle-choice-text-family-c1b2ec-b997.md)
- [battle-psi-user-selection-front-end-c1b5b6-b7c6.md](notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md)
- [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md)
- [battle-psi-ability-table-d58a50.md](notes/battle-psi-ability-table-d58a50.md)
- [battle-psi-category-list-family-c1caf5-c1cb7f.md](notes/battle-psi-category-list-family-c1caf5-c1cb7f.md)
- [battle-psi-menu-controller-c1cc39-ce73.md](notes/battle-psi-menu-controller-c1cc39-ce73.md)
- [battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md](notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md)
- [battle-targetting-resolver-c1adb4-af50.md](notes/battle-targetting-resolver-c1adb4-af50.md)
- [battle-selection-snapshot-export-c2b930.md](notes/battle-selection-snapshot-export-c2b930.md)

## Main result

The local `class2` battle-text cluster now reads less like one anonymous message sink and more like a small layered family:

- pointer-source selection in bank `C2`
- context refresh around attacker and target naming
- one-pointer and two-pointer display wrappers in bank `C1`
- nearby wait, sync, and party-state setup helpers

That is enough to describe a useful local runtime pipeline even though some symbolic identities still remain open.

## Current safest layered model

The strongest current split is:

1. source-side pointer selection in `class2`
- enemy record pointers like `encounter_text_ptr` and `death_text_ptr`
- hardcoded `EF:` battle status messages
- table-driven `D5:7B68` battle message pointers

2. battle-text context refresh helpers
- `C1:DD70 -> C1:AC4A`
- `C1:DD76 -> C1:ACA1`
- `C1:DD7C -> C1:ACF8`

3. display-entry wrappers
- `C1:DC1C` = strongest local fit for the main one-pointer battle-text display wrapper
- `C1:DC66` = companion wrapper best named locally as `DISPLAY_IN_BATTLE_TEXT_WITH_SUBSTITUTION_PAYLOAD`, now promoted as the best final match for reference `DISPLAY_TEXT_WAIT`, staging a secondary substitution payload through `C1:AD0A` before displaying the primary text, with the strongest current bridge pointing to amount-like payloads later read through `0x1C 0F`
- `C1:DD9F` = narrower wrapper best named locally as `DISPLAY_CURRENT_ACTION_TABLE_TEXT_MODE1`, now promoted as the best final match for reference `DISPLAY_IN_BATTLE_TEXT_NO_PROMPT`, used on the table-selected current-action text path and forcing explicit temporary mode `1`

4. adjacent support helpers
- `C1:DD82` = context-only pointer setter through `C1:AD0A`
- `C1:DD5F` = `BATTLE_DISPLAY_CLOSE_AND_SYNC_WAIT`, a battle-display close/reset/sync wrapper around battle or display-state transitions
- `C1:DCCB` = `INITIALIZE_PARTY_BATTLE_START_STATE`, the party-side battle-start initializer, including export of a reused `$99DC` selector/state byte rooted in the broader per-slot family already described in [class2-dispatch-family.md](notes/class2-dispatch-family.md)

## Best concrete caller bridges

The clearest currently pinned local bridges are:

- `C2:3BCF -> C1:DD70 -> C1:DC1C`
  - used with `enemy_data::encounter_text_ptr`
- `C2:3D05 -> C1:DD76 -> C1:DC1C`
  - used with the hardcoded battle-start status messages at `EF:843F`, `EF:8444`, and `EF:8445`
- `C2:7680+ -> C1:DC1C`
  - used with `enemy_data::death_text_ptr`
- `C2:5C66 -> C1:DD9F`
  - used with a `D5:7B68`-rooted table-selected current-action message pointer in the main battle-action flow
- `C2:B2E0 -> C1:DC66`
  - used by the battle stat-change consequence family for HP/PP recovery text and direct IQ/guts/speed/vitality/luck increase messages
- `C2:9AEA / 9B7A / 9C2C / 9CB8 -> C1:DC1C/DC66`
  - used by the battle affliction-recovery ladder for curative battle messages over the live affliction bytes

These are the strongest reasons the current cluster note is now useful rather than speculative.

There is also a now-separated ordinary battle-side caller family at [battle-choice-text-family-c1b2ec-b997.md](notes/battle-choice-text-family-c1b2ec-b997.md): it reuses `AC4A/ACA1/ACF8` outside the `DCxx/DDxx` wrappers, selects text from `D5:7B68` or from the `D5:8A50` battle PSI ability table, seeds the larger `$9FFA`-rooted battle selection snapshot block through `C2:B930`, and then exports row byte `+0x1D` back into the live `$99DC` slot-state family.

The PSI-menu-side notes now give the strongest bridge for that second lane:

- [battle-psi-user-selection-front-end-c1b5b6-b7c6.md](notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md) now covers the outer PSI-user-selection stage
- [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md) places `C1:C8BC` directly on the battle PSI menu path
- [battle-psi-ability-table-d58a50.md](notes/battle-psi-ability-table-d58a50.md) pins `D5:8A50` as the battle PSI ability table
- [battle-psi-menu-controller-c1cc39-ce73.md](notes/battle-psi-menu-controller-c1cc39-ce73.md) now gives the lower ordinary controller above the category and PSI-entry stages
- [battle-targetting-resolver-c1adb4-af50.md](notes/battle-targetting-resolver-c1adb4-af50.md) now gives the shared targetting resolver underneath both the battle-choice and PSI-menu lanes
- [battle-selection-snapshot-export-c2b930.md](notes/battle-selection-snapshot-export-c2b930.md) now gives the larger `$9FFA`-rooted battle selection snapshot block used by the outer PSI-user-selection and battle-choice lanes
- [battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md](notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md) now separates the two naming lanes under that same menu family

## Safest current interpretation

The safest current summary is:

- `C1:86B1` is still the generic textbox-data processor at the bottom of the cluster
- `C1:DC1C` is still the strongest local fit for the main battle-text display entry
- the surrounding `DDxx` helpers are no longer a blur: they now separate reasonably into context refresh, support, and adjacent setup work
- `C1:DC66` now has a stronger local bridge to the bank-`01` amount-printing side through `C1:AD0A / AD26` and `0x1C 0F`, so it is best treated locally as `DISPLAY_IN_BATTLE_TEXT_WITH_SUBSTITUTION_PAYLOAD` rather than just a second pointer sink
- the PSI-menu-side naming and selection layer is now cleaner too: `B5B6 .. B7C6` is the outer PSI-user-selection front end, `C1:CA06` is the direct PSI-id-plus-rank path, `C1:C8BC` is the second-stage entry-row builder with an explicit Thunder bypass, `C1:CC39 .. CE73` is the lower category-plus-entry controller, and `C1:ADB4 .. AF50` is the shared battle targetting resolver beneath that selection flow
- the remaining uncertainty is mostly symbolic naming and exact mode semantics, not whether the cluster exists

## What is still open

- the exact user-facing meaning of the reused `$99DC` selector/state values, especially `1` versus `2`
- whether the final export-driven names should eventually replace the current local helper-style names in the top summaries
- the exact user-facing meaning of temporary display modes `1` and `2` through `$964D`
- a real caller family for `C1:DD82`



