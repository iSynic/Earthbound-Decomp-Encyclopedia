# Bank C8 Decompilation Progress Audit

This report cross-checks the local `notes/*.md` corpus against the quarantined `ebsrc-main` US bank include maps and symbol lists.

Treat reference names as corroboration only: a bank entry is not considered understood here just because a side reference gave it a label.

## Bank `C8` / reference bank `08`

- Reference include entries: `12`
- Reference named include entries without an address in the path: `12`
- Reference address-bearing include entries: `0`
- Address-bearing unknown include entries: `0`
- Reference symbols: `2` (`2` semantic-ish, `0` placeholder/redirect/null)
- Local notes mention `93` distinct `C8:xxxx` addresses
- Reference addresses mentioned by local notes: `0` / `0`
- Unknown include entries not directly mentioned in local notes: `0`

### Reference-Named Include Families

These are already semantically grouped by `ebsrc-main`; use them as corroborating names, not as final local proof.

- `common.asm`
- `symbols/text.inc.asm`
- `text_data/E02TWSN0.ebtxt`
- `text_data/E10FOUR1.ebtxt`
- `text_data/ENEWS.ebtxt`
- `text_data/EBGMESS.ebtxt`
- `text_data/EEVENT2.ebtxt`
- `text_data/E11SUMS.ebtxt`
- `data/text/compressed_text_data.asm`
- `data/text/compressed_text_pointers.asm`
- `text_data/E05THRK.ebtxt`
- `text_data/EBATTLE6.ebtxt`

### Local-Only Address Mentions

These may be derived local discoveries, cross-bank targets, or address forms absent from the reference include/symbol map.

- `C8:0000` -> notes/bank-c8-text-data-map.md
- `C8:0027` -> notes/bank-c8-text-data-map.md
- `C8:00C1` -> notes/bank-c8-text-data-map.md
- `C8:00F5` -> notes/bank-c8-text-data-map.md
- `C8:015A` -> notes/bank-c8-text-data-map.md
- `C8:0277` -> notes/bank-c8-text-data-map.md
- `C8:02B9` -> notes/bank-c8-text-data-map.md
- `C8:02E6` -> notes/bank-c8-text-data-map.md
- `C8:2104` -> notes/bank-c8-text-data-map.md
- `C8:2105` -> notes/bank-c8-text-data-map.md
- `C8:21B2` -> notes/bank-c8-text-data-map.md, notes/text-command-family-1d-inventory-money.md
- `C8:21FE` -> notes/bank-c8-text-data-map.md
- `C8:2250` -> notes/bank-c8-text-data-map.md
- `C8:2285` -> notes/bank-c8-text-data-map.md
- `C8:22D2` -> notes/bank-c8-text-data-map.md
- `C8:2468` -> notes/bank-c8-text-data-map.md
- `C8:2565` -> notes/bank-c8-text-data-map.md
- `C8:41DD` -> notes/bank-c8-text-data-map.md
- `C8:41DE` -> notes/bank-c8-text-data-map.md
- `C8:42A5` -> notes/bank-c8-text-data-map.md
- `C8:42A8` -> notes/bank-c8-text-data-map.md
- `C8:42AB` -> notes/bank-c8-text-data-map.md
- `C8:42AE` -> notes/bank-c8-text-data-map.md
- `C8:42B1` -> notes/bank-c8-text-data-map.md
- `C8:42B4` -> notes/bank-c8-text-data-map.md
- `C8:42B7` -> notes/bank-c8-text-data-map.md
- `C8:435D` -> notes/bank-c8-first-pass.md, notes/bank-c8-text-data-map.md
- `C8:4A59` -> notes/bank-c8-first-pass.md, notes/bank-c8-text-data-map.md
- `C8:4A61` -> notes/bank-c8-first-pass.md, notes/bank-c8-text-data-map.md
- `C8:6278` -> notes/bank-c8-text-data-map.md
- `C8:6279` -> notes/bank-c8-text-data-map.md
- `C8:62B8` -> notes/bank-c8-text-data-map.md
- `C8:62F7` -> notes/bank-c8-text-data-map.md
- `C8:62F8` -> notes/bank-c8-text-data-map.md
- `C8:6311` -> notes/bank-c8-text-data-map.md
- `C8:6320` -> notes/bank-c8-text-data-map.md
- `C8:634C` -> notes/bank-c8-text-data-map.md
- `C8:6399` -> notes/bank-c8-text-data-map.md
- `C8:7F22` -> notes/bank-c8-text-data-map.md
- `C8:7F23` -> notes/bank-c8-first-pass.md, notes/bank-c8-text-data-map.md
- `C8:7FFF` -> notes/bank-c8-first-pass.md, notes/bank-c8-text-data-map.md
- `C8:8000` -> notes/bank-c8-text-data-map.md, notes/text-command-08-call-text.md
- `C8:807D` -> notes/bank-c8-text-data-map.md
- `C8:80B9` -> notes/bank-c8-text-data-map.md
- `C8:8103` -> notes/bank-c8-text-data-map.md
- `C8:824A` -> notes/bank-c8-text-data-map.md
- `C8:82BD` -> notes/bank-c8-text-data-map.md
- `C8:82C7` -> notes/jeff-repair-item-name-bridge.md
- `C8:8332` -> notes/bank-c8-text-data-map.md
- `C8:8386` -> notes/bank-c8-text-data-map.md
- `C8:9E1A` -> notes/bank-c8-text-data-map.md
- `C8:9E1B` -> notes/bank-c8-text-data-map.md
- `C8:9EA8` -> notes/bank-c8-text-data-map.md
- `C8:9EF8` -> notes/bank-c8-text-data-map.md
- `C8:9F2D` -> notes/bank-c8-text-data-map.md
- `C8:A023` -> notes/bank-c8-text-data-map.md
- `C8:A056` -> notes/bank-c8-text-data-map.md
- `C8:A11C` -> notes/bank-c8-text-data-map.md
- `C8:A174` -> notes/bank-c8-text-data-map.md
- `C8:BC2C` -> notes/bank-c8-text-data-map.md
- `C8:BC2D` -> notes/bank-c8-first-pass.md, notes/bank-c8-text-data-map.md
- `C8:D9EC` -> notes/bank-c8-first-pass.md, notes/bank-c8-text-data-map.md
- `C8:D9ED` -> notes/bank-c8-text-data-map.md
- `C8:DA31` -> notes/bank-c8-text-data-map.md
- `C8:DA5D` -> notes/bank-c8-text-data-map.md
- `C8:DAA0` -> notes/bank-c8-text-data-map.md
- `C8:DAD5` -> notes/bank-c8-text-data-map.md
- `C8:DAEE` -> notes/bank-c8-text-data-map.md
- `C8:DB32` -> notes/bank-c8-text-data-map.md
- `C8:DB92` -> notes/bank-c8-text-data-map.md
- `C8:F77C` -> notes/bank-c8-text-data-map.md
- `C8:F77D` -> notes/bank-c8-text-data-map.md, notes/class2-late-stat-and-resource-family-c28e42-c29e38.md
- `C8:F79A` -> notes/bank-c8-text-data-map.md
- `C8:F7B8` -> notes/bank-c8-text-data-map.md, notes/battle-action-stat-change-family-c2b2e0-b5d7.md
- `C8:F7D2` -> notes/bank-c8-text-data-map.md, notes/battle-action-stat-change-family-c2b2e0-b5d7.md
- `C8:F7EE` -> notes/bank-c8-text-data-map.md, notes/class2-late-stat-and-resource-family-c28e42-c29e38.md
- `C8:F80A` -> notes/bank-c8-text-data-map.md
- `C8:F82F` -> notes/bank-c8-text-data-map.md, notes/battle-action-stat-change-family-c2b2e0-b5d7.md
- `C8:F84C` -> notes/bank-c8-text-data-map.md, notes/battle-action-stat-change-family-c2b2e0-b5d7.md
- `C8:F86B` -> notes/battle-action-stat-change-family-c2b2e0-b5d7.md
- ... 13 more

## Suggested Workflow

1. Pick an unmentioned `unknown/...` chunk from this report.
2. Run `tools/decode_snippet.py` or a targeted helper around the address.
3. Cross-check `refs/ebsrc-main` symbols, `refs/earthbound-disasm-legacy`, and any data table in `refs/eb-decompile-4ef92` that the routine touches.
4. Write a focused note that states byte-level evidence, borrowed reference names, remaining uncertainty, and direct callers/xrefs.
5. Rerun this audit and promote the next gap.

