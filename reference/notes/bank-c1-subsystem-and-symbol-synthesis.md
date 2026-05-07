# Bank C1 Subsystem And Symbol Synthesis

This is the navigation layer for the local C1 notes corpus now that the bank has full audit coverage.

See also [bank-0-1-progress-audit.md](notes/bank-0-1-progress-audit.md).
See also [bank-c1-working-name-proposals.md](notes/bank-c1-working-name-proposals.md).

## Coverage State

The current audit reports:

- C1 reference addresses mentioned by local notes: `132 / 132`
- C1 unknown include entries not directly mentioned in local notes: `0`

That means C1 has enough local coverage to move from discovery to promotion: consolidate names, identify stable contracts, and decide which cross-bank dependencies need deeper proof.

## Subsystem Map

| Range | Subsystem | Local model | Primary notes |
| --- | --- | --- | --- |
| `C1:0000..2E42` | text engine core and window loop | text entry/wait gates, window focus, low-level print/render primitives, selection/cursor helpers, character select prompt, window tick | [text-engine-entry-waits-window-gates-c10000-c102d0.md](notes/text-engine-entry-waits-window-gates-c10000-c102d0.md), [text-window-rendering-primitives-c1078d-c10d7c.md](notes/text-window-rendering-primitives-c1078d-c10d7c.md), [text-entry-record-builder-neighbors-c10f40-c11887.md](notes/text-entry-record-builder-neighbors-c10f40-c11887.md), [character-selection-prompt-cluster-c11f8a-c1242e.md](notes/character-selection-prompt-cluster-c11f8a-c1242e.md) |
| `C1:339E..4070` | field menu and early text commands | open-menu prelude, debug menu hooks, timed-event callback dispatch, lower text command leaves | [open-menu-prelude-helpers-c1339e-c133b0.md](notes/open-menu-prelude-helpers-c1339e-c133b0.md), [debug-menu-window-tick-helpers-c12bf3-c12d17.md](notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md), [timed-event-callback-family-bank01.md](notes/timed-event-callback-family-bank01.md) |
| `C1:4070..81BB` | EB text command dispatcher leaves | event flags, jumps, argument/secondary/work memory, inventory/money, stat recovery, teleport, timed events, special events | [bank01-text-command-map-00-1f.md](notes/bank01-text-command-map-00-1f.md), [lower-bank01-text-control-strip-00-17.md](notes/lower-bank01-text-control-strip-00-17.md), [text-command-family-18-windows-and-selection.md](notes/text-command-family-18-windows-and-selection.md), [text-command-family-1d-inventory-money.md](notes/text-command-family-1d-inventory-money.md), [text-command-family-1e-stat-recovery.md](notes/text-command-family-1e-stat-recovery.md), [text-command-family-1f-deferred-callbacks.md](notes/text-command-family-1f-deferred-callbacks.md) |
| `C1:866D..9F29` | inventory, item names, equipment display | item give/take wrappers, inventory slot insertion/removal, HP/PP adjust helpers, item naming and category classification, equipment preview | [inventory-slot-insertion-helper-c18bc6.md](notes/inventory-slot-insertion-helper-c18bc6.md), [inventory-slot-removal-helper-c18c27.md](notes/inventory-slot-removal-helper-c18c27.md), [inventory-slot-search-removal-helper-c18e5b-c18ead.md](notes/inventory-slot-search-removal-helper-c18e5b-c18ead.md), [item-psi-name-display-and-target-prompt-c19216-c19437.md](notes/item-psi-name-display-and-target-prompt-c19216-c19437.md), [equipment-menu-display-fringe-c19a11-c19f29.md](notes/equipment-menu-display-fringe-c19a11-c19f29.md) |
| `C1:A1D8..AAFA` | equipment menu controller | selected-character equipment refresh, party-facing equipment menu, derived equipment caches | [equipment-menu-top-level-flow-c1a778-c1aa5d.md](notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md), [equipment-preview-and-derived-state-cluster.md](notes/equipment-preview-and-derived-state-cluster.md), [equipped-item-derived-cache-family-c21857-c21e03.md](notes/equipped-item-derived-cache-family-c21857-c21e03.md) |
| `C1:AAFA..BEFC` | battle/field choice text, targetting, teleport | battle text context buffers, targetting resolver, field PSI/teleport destination picker, special event dispatch | [battle-text-context-buffer-family-c1ac4a-ad42.md](notes/battle-text-context-buffer-family-c1ac4a-ad42.md), [battle-targetting-resolver-c1adb4-af50.md](notes/battle-targetting-resolver-c1adb4-af50.md), [battle-psi-user-selection-front-end-c1b5b6-b7c6.md](notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md), [teleport-menu-wrapper-c1bb71-bcab.md](notes/teleport-menu-wrapper-c1bb71-bcab.md), [text-command-1f41-special-event-dispatch-c1befc.md](notes/text-command-1f41-special-event-dispatch-c1befc.md) |
| `C1:C046..D08A` | battle PSI, item selection, and Jeff repair bridge | PSI menu metadata, PSI row builders, PSI category/selection loops, battle item action resolver, broken-item to repaired-item mapper | [battle-psi-menu-table-helpers-c1c046-c1c165.md](notes/battle-psi-menu-table-helpers-c1c046-c1c165.md), [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md), [battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md](notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md), [battle-psi-menu-controller-c1cc39-ce73.md](notes/battle-psi-menu-controller-c1cc39-ce73.md), [battle-item-action-selection-c1ce85-c1cfc6.md](notes/battle-item-action-selection-c1ce85-c1cfc6.md), [c3-jeff-repair-source-contract-f1ec.md](notes/c3-jeff-repair-source-contract-f1ec.md) |
| `C1:D08B..D76D` | level-up and stat text | growth helper, level-up application, stat gain message leaves | [level-up-stat-growth-helper-c1d08b.md](notes/level-up-stat-growth-helper-c1d08b.md), [level-up-stat-gain-text-family-c1d15b-d76d.md](notes/level-up-stat-gain-text-family-c1d15b-d76d.md) |
| `C1:DC1C..DD9F` | battle text display | battle text display wrappers, context buffer rebuild leaves, battle HP/PP window redirects | [battle-text-entry-family-c1dc1c-dd7c.md](notes/battle-text-entry-family-c1dc1c-dd7c.md), [battle-text-entry-tail-dd82-dd9f.md](notes/battle-text-entry-tail-dd82-dd9f.md), [class2-battle-text-cluster-overview.md](notes/class2-battle-text-cluster-overview.md) |
| `C1:E1A2..EC8F` | enemy select, text input, naming | null callback, enemy-select mode, text-input dialog option helpers, name-buffer commit, window-flavour preview | [bank-c1-null-hook-c1e1a2.md](notes/bank-c1-null-hook-c1e1a2.md), [text-input-dialog-option-helpers-c1e48d-c1e4be.md](notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md), [naming-buffer-commit-family-c1ead6-c4d065.md](notes/naming-buffer-commit-family-c1ead6-c4d065.md), [file-select-window-flavour-refresh-c1ec8f-ecd1.md](notes/file-select-window-flavour-refresh-c1ec8f-ecd1.md) |
| `C1:ECDC..FFFF` | save corruption, file select, setup, tail glue | save corruption check, file-select main loop, copy/delete/setup menu bodies, text-speed/sound/flavour options, file-select entry wrapper, text layout callback, SRAM checksum | [file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md](notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md), [file-select-setup-option-menus-c1f497-c1f616.md](notes/file-select-setup-option-menus-c1f497-c1f616.md), [file-select-tail-helpers-c1ff2c-ff6b-ff99.md](notes/file-select-tail-helpers-c1ff2c-ff6b-ff99.md) |

## High-Confidence Working Names

These are name proposals that look stable enough to promote first. They are intentionally conservative: they name behavior observed locally rather than borrowing every reference label.

- `C1:13D1` = `InstallTextEntryRecord`
- `C1:AC4A` = `BuildBattleAttackerNameBuffer`
- `C1:ACA1` = `BuildBattleTargetNameBuffer`
- `C1:ACF8` = `StageBattleTextSubstitutionByte`
- `C1:AD42` = `GetFrontInteractionResultClass`
- `C1:ADB4` = `DetermineBattleTargetting`
- `C1:B5B6` = `OpenBattlePsiUserSelection`
- `C1:BB71` = `OpenFieldPsiDestinationMenu`
- `C1:BCAB` = `ExecuteTeleportDestination`
- `C1:C046` = `RefreshPsiMenuCursorCategory`
- `C1:C165` = `CurrentCharacterKnowsPsi`
- `C1:C8BC` = `FormatBattlePsiMenuEntryRow`
- `C1:CA06` = `BuildPsiRankName`
- `C1:CA72` = `RefreshBattlePsiSelection`
- `C1:CAF5` = `BuildBattlePsiCategoryEntryList`
- `C1:CB7F` = `HasBattlePsiCategoryEntries`
- `C1:CE85` = `ResolveSelectedBattleItemAction`
- `C1:CFC6` = `OpenBattleItemSelectionLoop`
- `C1:D038` = `MapBrokenItemToRepairedItem`
- `C1:D08B` = `ComputeLevelUpStatGrowthDelta`
- `C1:DC1C` = `DisplayBattleTextFromPointer`
- `C1:DC66` = `DisplayBattleTextWithSubstitutionPayload`
- `C1:DCCB` = `InitializePartyBattleStartState`
- `C1:E1A2` = `NullFarCallback`
- `C1:E48D` = `RenderSingleTextInputOptionRowScoped`
- `C1:E4BE` = `BuildTextInputOptionStrip`
- `C1:EAD6` = `RunNamingBufferCommitFlow`
- `C1:EC04` = `CommitNamingBufferFieldWithPreview`
- `C1:EC8F` = `PreviewWindowFlavourAndRedraw`
- `C1:ECD1` = `PreviewPackedHighByteWindowFlavour`
- `C1:F07E` = `OpenFileSelectActionMenu`
- `C1:F14F` = `OpenCopyDestinationMenu`
- `C1:F2A8` = `OpenDeleteFileConfirmationMenu`
- `C1:F3C2` = `OpenTextSpeedMenu`
- `C1:F497` = `OpenOrRefreshTextSpeedSelection`
- `C1:F568` = `OpenSoundSettingMenu`
- `C1:F616` = `OpenOrRefreshSoundSettingSelection`
- `C1:FF2C` = `UpdateLeadEntityTypeRedrawFlag`
- `C1:FF6B` = `RunFileSelectSession`
- `C1:FF99` = `ComputeCenteredTextLayoutMetric`
- `C1:FFD3` = `ComputeBankC1ChecksumTail`

## Stable Cross-Bank Contracts

C1 is mostly a coordinator bank. Its most important outbound dependencies are:

- C0 display/window helpers: `C0:8FF7`, `C0:90xx`, and lower window/render math are used throughout text and file-select rendering.
- C2 battle runtime: targetting, battle text, battle action resolution, and status/display updates repeatedly cross into C2.
- C3 window/update scope helpers: `C3:E4D4`, `C3:E4CA`, `C3:E521`, and related calls are the shared frame/window lifecycle layer.
- C4 renderer/data helpers: `C4:38A5`, `C4:3BB9`, `C4:3E31`, `C4:7F87`, and item/name formatting routines are central to C1's visible output.
- EF save/menu data routines: file select calls `EF:0A4D`, `EF:0A68`, `EF:0BFA`, and `EF:0C15`.

This is why the best next bank for confidence is C2. C1's battle-facing routines are locally mapped, but their deepest behavioral proof depends on C2's action rows, status mutation, and battle text result flow.

## Remaining Soft Edges

The bank is covered, but several terms should stay provisional until their consumers are documented further:

- `$B4A1`, `$B49D`, `$B4A2`, and `$B4B6` are well localized to file-select/session state, but the exact full struct layout remains a soft edge.
- C4 renderer helpers are behaviorally clear from C1 call sites, but not yet named from C4-local documentation.
- EF save-file routines have strong call-site meaning from file select, but their internals are outside the current C0/C1 bank boundary.
- Some text command families have good dispatcher coverage but still need table-level promotion if we want a source-quality CCS runtime map.

## Recommended Next Pass

The next practical run should be C2 battle-runtime synthesis:

- start from C1 callers into C2 and EF battle text helpers
- build a table of battle action/status helpers that already have class2 notes
- close the targetting/result-text loop from `C1:ADB4`, `C1:CE85`, `C1:CFC6`, and `C1:DC1C` into C2
- promote C1/C2 shared battle names together, rather than naming one side in isolation
