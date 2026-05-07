# C3 battle PSI menu data contracts

This note promotes the C3 battle PSI menu data corridor `C3:EF26..F1EC` from raw named data to explicit ROM-table contracts. The corridor is byte-backed by `src/c3/data_battle_menu_tables_ef23_f1ec.asm`; these contracts describe the table shapes used by the C1 PSI menu helpers.

## Selector group tables

`C3:EF26..F016` is `BATTLE_PSI_MENU_SELECTOR_GROUP_TABLE`.

`C1:C046` takes a menu selector, subtracts `#$0010`, and indexes this table as bytes:

```text
C1:C07C  LDY $16
C1:C07E  TYA
C1:C080  SBC #$0010
C1:C083  TAX
C1:C084  LDA $C3EF26,X
C1:C088  AND #$00FF
```

A zero byte falls back to printing the raw selector. A nonzero byte is decremented into a group index, then used with `C3:F016`.

`C3:F016..F054` is `BATTLE_PSI_MENU_GROUP_SLICE_COUNT_TABLE`.

```text
C1:C0B6  TXA
C1:C0B7  DEC A
C1:C0B8  STA $14
C1:C0BA  TAX
C1:C0BB  LDA $C3F016,X
C1:C0BF  AND #$00FF
```

The selected byte becomes the count/width used while copying grouped PSI-list text from the E0:1359 table family through the C4 text-placement helpers.

`C3:F054..F0B0` remains a single proposed block contract, `BATTLE_PSI_GROUP_RENDER_METADATA_AND_LABELS`. It contains render metadata and encoded labels adjacent to the selector-group tables; the exact field split is still softer than the two directly indexed byte tables.

## Known-state gates and row text

`C3:F0B0..F112` is `BATTLE_PSI_KNOWN_STATE_GATE_TABLE`.

`C1:C165` scans seven live PSI bytes for a party member. For each nonzero byte it computes:

```text
offset = (live_psi_byte - 1) * 2 + live_psi_slot * 14
```

Then it reads a word from `C3:F0B0 + offset`:

```text
C1:C18C  DEC A
C1:C18D  ASL A
...
C1:C199  ASL A
C1:C19B  ADC $02
C1:C19D  TAX
C1:C19E  LDA $C3F0B0,X
```

That makes the table seven rows of seven word gates.

The tail of the corridor is the PSI name/menu row formatting data already named by the C3 shared-helper pass:

- `C3:F112..F11C` = `BATTLE_PSI_RANK_SUFFIX_TABLE`
- `C3:F11C..F124` = `BATTLE_PSI_MENU_ENTRY_FIXED_TAIL`
- `C3:F124..F1EC` = `BATTLE_PSI_MENU_ENTRY_ROW_TABLE`

These are consumed by the PSI name/menu row formatting family documented in `notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md`.

## Remaining softness

`BATTLE_PSI_GROUP_RENDER_METADATA_AND_LABELS` is intentionally a block contract. It closes the source/data map and byte-boundary contract for `C3:F054..F0B0`, but a future pass should split its pointer/geometry/label fields after tracing the C1/C4 display path in more detail.
