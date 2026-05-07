# Bank C6 Decompilation Progress Audit

This report cross-checks the local `notes/*.md` corpus against the quarantined `ebsrc-main` US bank include maps and symbol lists.

Treat reference names as corroboration only: a bank entry is not considered understood here just because a side reference gave it a label.

## Bank `C6` / reference bank `06`

- Reference include entries: `9`
- Reference named include entries without an address in the path: `9`
- Reference address-bearing include entries: `0`
- Address-bearing unknown include entries: `0`
- Reference symbols: `2` (`2` semantic-ish, `0` placeholder/redirect/null)
- Local notes mention `75` distinct `C6:xxxx` addresses
- Reference addresses mentioned by local notes: `0` / `0`
- Unknown include entries not directly mentioned in local notes: `0`

### Reference-Named Include Families

These are already semantically grouped by `ebsrc-main`; use them as corroborating names, not as final local proof.

- `common.asm`
- `symbols/text.inc.asm`
- `text_data/E09DSRT.ebtxt`
- `text_data/ESHOP3.ebtxt`
- `text_data/E01ONET2.ebtxt`
- `text_data/EGLOBAL.ebtxt`
- `text_data/E06WINS.ebtxt`
- `text_data/E10FOUR0.ebtxt`
- `text_data/EGOODS3.ebtxt`

### Local-Only Address Mentions

These may be derived local discoveries, cross-bank targets, or address forms absent from the reference include/symbol map.

- `C6:0000` -> notes/bank-c6-text-data-map.md
- `C6:0006` -> notes/bank-c6-text-data-map.md
- `C6:002C` -> notes/bank-c6-text-data-map.md
- `C6:005F` -> notes/bank-c6-text-data-map.md
- `C6:00A4` -> notes/bank-c6-text-data-map.md
- `C6:00D5` -> notes/bank-c6-text-data-map.md
- `C6:0100` -> notes/bank-c6-text-data-map.md
- `C6:0140` -> notes/bank-c6-text-data-map.md
- `C6:2D2F` -> notes/bank-c6-text-data-map.md
- `C6:2D30` -> notes/bank-c6-text-data-map.md
- `C6:2D8A` -> notes/bank-c6-text-data-map.md
- `C6:2D91` -> notes/bank-c6-text-data-map.md
- `C6:2D93` -> notes/bank-c6-text-data-map.md
- `C6:2DF3` -> notes/bank-c6-text-data-map.md
- `C6:2E3B` -> notes/bank-c6-text-data-map.md
- `C6:2E6D` -> notes/bank-c6-text-data-map.md
- `C6:2EEF` -> notes/bank-c6-text-data-map.md
- `C6:3EB0` -> notes/selector-row-config-family-ef0ee8.md, notes/service-script-pointer-table-c58cf4.md
- `C6:42A3` -> notes/selector-row-config-family-ef0ee8.md, notes/service-script-pointer-table-c58cf4.md
- `C6:4515` -> notes/selector-row-config-family-ef0ee8.md
- `C6:4BBF` -> notes/selector-row-config-family-ef0ee8.md, notes/service-script-pointer-table-c58cf4.md
- `C6:4CF8` -> notes/selector-row-config-family-ef0ee8.md
- `C6:5243` -> notes/service-script-pointer-table-c58cf4.md
- `C6:55B1` -> notes/service-script-pointer-table-c58cf4.md
- `C6:59C8` -> notes/bank-c6-text-data-map.md
- `C6:59C9` -> notes/bank-c6-text-data-map.md
- `C6:5A18` -> notes/bank-c6-text-data-map.md
- `C6:5A38` -> notes/bank-c6-text-data-map.md
- `C6:5A4C` -> notes/bank-c6-text-data-map.md
- `C6:5A8C` -> notes/bank-c6-text-data-map.md
- `C6:5AB6` -> notes/bank-c6-text-data-map.md
- `C6:5AE9` -> notes/bank-c6-text-data-map.md
- `C6:5B66` -> notes/bank-c6-text-data-map.md
- `C6:5DA6` -> notes/text-command-family-1d-inventory-money.md
- `C6:77CC` -> notes/text-command-06-jump-if-flag-set.md
- `C6:7EEB` -> notes/bank-c6-text-data-map.md
- `C6:8000` -> notes/bank-c6-text-data-map.md
- `C6:8008` -> notes/bank-c6-text-data-map.md
- `C6:8017` -> notes/bank-c6-text-data-map.md
- `C6:803D` -> notes/bank-c6-text-data-map.md
- `C6:8077` -> notes/bank-c6-text-data-map.md
- `C6:8091` -> notes/bank-c6-text-data-map.md
- `C6:809E` -> notes/bank-c6-text-data-map.md
- `C6:80A6` -> notes/bank-c6-text-data-map.md
- `C6:8500` -> notes/text-command-08-call-text.md
- `C6:A9F8` -> notes/bank-c6-text-data-map.md
- `C6:A9F9` -> notes/bank-c6-text-data-map.md
- `C6:AA2F` -> notes/bank-c6-text-data-map.md
- `C6:ABD5` -> notes/bank-c6-text-data-map.md
- `C6:ACDA` -> notes/bank-c6-text-data-map.md
- `C6:AD29` -> notes/bank-c6-text-data-map.md
- `C6:AD68` -> notes/bank-c6-text-data-map.md
- `C6:AD6E` -> notes/bank-c6-text-data-map.md
- `C6:AE07` -> notes/bank-c6-text-data-map.md
- `C6:B99F` -> notes/text-command-06-jump-if-flag-set.md
- `C6:C61A` -> notes/selector-row-config-family-ef0ee8.md
- `C6:D19B` -> notes/bank-c6-text-data-map.md
- `C6:D19C` -> notes/bank-c6-text-data-map.md
- `C6:D2E4` -> notes/bank-c6-text-data-map.md
- `C6:D2E8` -> notes/bank-c6-text-data-map.md
- `C6:D325` -> notes/bank-c6-text-data-map.md
- `C6:D37E` -> notes/bank-c6-text-data-map.md
- `C6:D391` -> notes/bank-c6-text-data-map.md
- `C6:D4D6` -> notes/bank-c6-text-data-map.md
- `C6:D50A` -> notes/bank-c6-text-data-map.md
- `C6:F8D8` -> notes/bank-c6-text-data-map.md
- `C6:F8D9` -> notes/bank-c6-text-data-map.md
- `C6:F8E6` -> notes/bank-c6-text-data-map.md
- `C6:F913` -> notes/bank-c6-text-data-map.md
- `C6:F940` -> notes/bank-c6-text-data-map.md
- `C6:F96D` -> notes/bank-c6-text-data-map.md
- `C6:F99A` -> notes/bank-c6-text-data-map.md
- `C6:F9BB` -> notes/bank-c6-text-data-map.md
- `C6:F9DC` -> notes/bank-c6-text-data-map.md
- `C6:FFE2` -> notes/bank-c6-text-data-map.md

## Suggested Workflow

1. Pick an unmentioned `unknown/...` chunk from this report.
2. Run `tools/decode_snippet.py` or a targeted helper around the address.
3. Cross-check `refs/ebsrc-main` symbols, `refs/earthbound-disasm-legacy`, and any data table in `refs/eb-decompile-4ef92` that the routine touches.
4. Write a focused note that states byte-level evidence, borrowed reference names, remaining uncertainty, and direct callers/xrefs.
5. Rerun this audit and promote the next gap.

