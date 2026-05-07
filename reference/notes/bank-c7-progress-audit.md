# Bank C7 Decompilation Progress Audit

This report cross-checks the local `notes/*.md` corpus against the quarantined `ebsrc-main` US bank include maps and symbol lists.

Treat reference names as corroboration only: a bank entry is not considered understood here just because a side reference gave it a label.

## Bank `C7` / reference bank `07`

- Reference include entries: `11`
- Reference named include entries without an address in the path: `11`
- Reference address-bearing include entries: `0`
- Address-bearing unknown include entries: `0`
- Reference symbols: `2` (`2` semantic-ish, `0` placeholder/redirect/null)
- Local notes mention `104` distinct `C7:xxxx` addresses
- Reference addresses mentioned by local notes: `0` / `0`
- Unknown include entries not directly mentioned in local notes: `0`

### Reference-Named Include Families

These are already semantically grouped by `ebsrc-main`; use them as corroborating names, not as final local proof.

- `common.asm`
- `symbols/text.inc.asm`
- `text_data/EHINT.ebtxt`
- `text_data/E01ONET1.ebtxt`
- `text_data/E01ONET0.ebtxt`
- `text_data/E18MGKT.ebtxt`
- `text_data/EGOODS4.ebtxt`
- `text_data/EEVENT1.ebtxt`
- `text_data/EEVENT4.ebtxt`
- `text_data/ESYSTEM.ebtxt`
- `text_data/E08DOSEI.ebtxt`

### Local-Only Address Mentions

These may be derived local discoveries, cross-bank targets, or address forms absent from the reference include/symbol map.

- `C7:0000` -> notes/bank-c7-text-data-map.md
- `C7:00F3` -> notes/bank-c7-text-data-map.md
- `C7:00F7` -> notes/bank-c7-text-data-map.md
- `C7:00FB` -> notes/bank-c7-text-data-map.md
- `C7:00FF` -> notes/bank-c7-text-data-map.md
- `C7:0103` -> notes/bank-c7-text-data-map.md
- `C7:0107` -> notes/bank-c7-text-data-map.md
- `C7:0144` -> notes/bank-c7-text-data-map.md
- `C7:014F` -> notes/bank-c7-text-data-map.md
- `C7:015A` -> notes/bank-c7-text-data-map.md
- `C7:0165` -> notes/bank-c7-text-data-map.md
- `C7:0176` -> notes/bank-c7-text-data-map.md
- `C7:0187` -> notes/bank-c7-text-data-map.md
- `C7:0198` -> notes/bank-c7-text-data-map.md
- `C7:2708` -> notes/bank-c7-text-data-map.md
- `C7:2709` -> notes/bank-c7-text-data-map.md
- `C7:2765` -> notes/bank-c7-text-data-map.md
- `C7:27A8` -> notes/bank-c7-text-data-map.md
- `C7:27CF` -> notes/bank-c7-text-data-map.md
- `C7:2822` -> notes/bank-c7-text-data-map.md
- `C7:2910` -> notes/bank-c7-text-data-map.md
- `C7:298C` -> notes/bank-c7-text-data-map.md
- `C7:29FF` -> notes/bank-c7-text-data-map.md
- `C7:4BA8` -> notes/bank-c7-text-data-map.md
- `C7:4BA9` -> notes/bank-c7-text-data-map.md
- `C7:4C07` -> notes/bank-c7-text-data-map.md
- `C7:4C49` -> notes/bank-c7-text-data-map.md
- `C7:4C6C` -> notes/bank-c7-text-data-map.md
- `C7:4C85` -> notes/bank-c7-text-data-map.md
- `C7:4C8A` -> notes/bank-c7-text-data-map.md
- `C7:4CE8` -> notes/bank-c7-text-data-map.md
- `C7:4CF7` -> notes/bank-c7-text-data-map.md
- `C7:500D` -> notes/jeff-repair-item-name-bridge.md
- `C7:616F` -> notes/text-command-family-1d-inventory-money.md
- `C7:6357` -> notes/text-command-06-jump-if-flag-set.md
- `C7:6F1F` -> notes/bank-c7-text-data-map.md
- `C7:6F20` -> notes/bank-c7-text-data-map.md
- `C7:6F26` -> notes/bank-c7-text-data-map.md
- `C7:6F42` -> notes/bank-c7-text-data-map.md
- `C7:6F5E` -> notes/bank-c7-text-data-map.md
- `C7:6F7A` -> notes/bank-c7-text-data-map.md
- `C7:6F96` -> notes/bank-c7-text-data-map.md
- `C7:6FB2` -> notes/bank-c7-text-data-map.md
- `C7:7007` -> notes/bank-c7-text-data-map.md
- `C7:7DCD` -> notes/bank-c7-text-data-map.md
- `C7:7DCE` -> notes/bank-c7-text-data-map.md, notes/class2-d57b68-battle-action-table-match.md
- `C7:7DF0` -> notes/bank-c7-text-data-map.md
- `C7:7E11` -> notes/bank-c7-text-data-map.md
- `C7:7E33` -> notes/bank-c7-text-data-map.md
- `C7:7E85` -> notes/bank-c7-text-data-map.md
- `C7:7EB6` -> notes/bank-c7-text-data-map.md
- `C7:7EE8` -> notes/bank-c7-text-data-map.md
- `C7:7EFF` -> notes/bank-c7-text-data-map.md, notes/class2-d57b68-battle-action-table-match.md, notes/class2-descriptor-field-4e-and-d57b68.md
- `C7:8000` -> notes/bank-c7-text-data-map.md
- `C7:8033` -> notes/bank-c7-text-data-map.md
- `C7:80B2` -> notes/bank-c7-text-data-map.md
- `C7:80F7` -> notes/bank-c7-text-data-map.md
- `C7:814B` -> notes/bank-c7-text-data-map.md
- `C7:8166` -> notes/bank-c7-text-data-map.md
- `C7:81CE` -> notes/bank-c7-text-data-map.md
- `C7:8208` -> notes/bank-c7-text-data-map.md
- `C7:A2F6` -> notes/bank-c7-text-data-map.md
- `C7:A2F7` -> notes/bank-c7-text-data-map.md
- `C7:A300` -> notes/bank-c7-text-data-map.md
- `C7:A542` -> notes/bank-c7-text-data-map.md, notes/timed-delivery-special-row-02a3.md
- `C7:A63E` -> notes/bank-c7-text-data-map.md
- `C7:A6A9` -> notes/bank-c7-text-data-map.md
- `C7:A6EA` -> notes/bank-c7-text-data-map.md
- `C7:A72F` -> notes/bank-c7-text-data-map.md
- `C7:A754` -> notes/bank-c7-text-data-map.md
- `C7:A7D9` -> notes/timed-delivery-special-row-02a3.md
- `C7:AB3F` -> notes/entity-visual-flag-and-current-slot-wrappers-c46534-c469f1.md
- `C7:B9A1` -> notes/class2-final-prayer-family-c2c572-c2c6f0.md
- `C7:BA2C` -> notes/class2-final-prayer-family-c2c572-c2c6f0.md
- `C7:BAC7` -> notes/class2-final-prayer-family-c2c572-c2c6f0.md
- `C7:BB38` -> notes/class2-final-prayer-family-c2c572-c2c6f0.md
- `C7:BBF3` -> notes/class2-final-prayer-family-c2c572-c2c6f0.md
- `C7:BC56` -> notes/class2-final-prayer-family-c2c572-c2c6f0.md
- `C7:BC96` -> notes/class2-final-prayer-family-c2c572-c2c6f0.md
- `C7:C587` -> notes/bank-c7-text-data-map.md
- ... 24 more

## Suggested Workflow

1. Pick an unmentioned `unknown/...` chunk from this report.
2. Run `tools/decode_snippet.py` or a targeted helper around the address.
3. Cross-check `refs/ebsrc-main` symbols, `refs/earthbound-disasm-legacy`, and any data table in `refs/eb-decompile-4ef92` that the routine touches.
4. Write a focused note that states byte-level evidence, borrowed reference names, remaining uncertainty, and direct callers/xrefs.
5. Rerun this audit and promote the next gap.

