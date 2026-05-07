# Bank C9 Decompilation Progress Audit

This report cross-checks the local `notes/*.md` corpus against the quarantined `ebsrc-main` US bank include maps and symbol lists.

Treat reference names as corroboration only: a bank entry is not considered understood here just because a side reference gave it a label.

## Bank `C9` / reference bank `09`

- Reference include entries: `16`
- Reference named include entries without an address in the path: `15`
- Reference address-bearing include entries: `1`
- Address-bearing unknown include entries: `0`
- Reference symbols: `2` (`2` semantic-ish, `0` placeholder/redirect/null)
- Local notes mention `149` distinct `C9:xxxx` addresses
- Reference addresses mentioned by local notes: `1` / `1`
- Unknown include entries not directly mentioned in local notes: `0`

### Reference-Named Include Families

These are already semantically grouped by `ebsrc-main`; use them as corroborating names, not as final local proof.

- `common.asm`
- `symbols/text.inc.asm`
- `text_data/ESHOP2.ebtxt`
- `text_data/EEVENT3.ebtxt`
- `text_data/E02TWSN2.ebtxt`
- `text_data/E02TWSN1.ebtxt`
- `text_data/E19MOON.ebtxt`
- `text_data/EGOODS0.ebtxt`
- `text_data/E03HAPPY.ebtxt`
- `text_data/EEVENT5.ebtxt`
- `text_data/E12RAMA.ebtxt`
- `text_data/E15GUMI.ebtxt`
- `text_data/E14MAKYO.ebtxt`
- `text_data/EBATTLE7.ebtxt`
- `text_data/EGOODS1.ebtxt`

### Locally Corroborated Reference Addresses

- `C9:992F` -> notes/bank-c9-first-pass.md, notes/bank-c9-text-data-map.md

### Local-Only Address Mentions

These may be derived local discoveries, cross-bank targets, or address forms absent from the reference include/symbol map.

- `C9:0000` -> notes/bank-c9-text-data-map.md, notes/text-command-08-call-text.md
- `C9:0008` -> notes/bank-c9-text-data-map.md
- `C9:0010` -> notes/bank-c9-text-data-map.md
- `C9:0025` -> notes/bank-c9-text-data-map.md
- `C9:002B` -> notes/bank-c9-text-data-map.md
- `C9:0033` -> notes/bank-c9-text-data-map.md
- `C9:0067` -> notes/bank-c9-text-data-map.md
- `C9:006F` -> notes/bank-c9-text-data-map.md
- `C9:1870` -> notes/jeff-repair-item-name-bridge.md
- `C9:1905` -> notes/text-command-0a-24bit-jump.md
- `C9:1A91` -> notes/class2-c1-display-text-substitution-handler-7af3.md, notes/class2-cc19-1f-cross-segment-reuse.md, notes/class2-cc19-20-eshop2-single-use.md, +1 more
- `C9:1A93` -> notes/class2-cc19-20-eshop2-single-use.md
- `C9:1A95` -> notes/class2-cc19-20-eshop2-single-use.md
- `C9:1C39` -> notes/bank-c9-text-data-map.md
- `C9:1C3A` -> notes/bank-c9-text-data-map.md
- `C9:1CC1` -> notes/bank-c9-text-data-map.md
- `C9:1F9C` -> notes/bank-c9-text-data-map.md
- `C9:1FBA` -> notes/bank-c9-text-data-map.md
- `C9:1FD9` -> notes/bank-c9-text-data-map.md
- `C9:1FDB` -> notes/bank-c9-text-data-map.md
- `C9:1FFA` -> notes/bank-c9-text-data-map.md
- `C9:1FFD` -> notes/bank-c9-text-data-map.md
- `C9:3852` -> notes/bank-c9-text-data-map.md
- `C9:3853` -> notes/bank-c9-text-data-map.md
- `C9:3891` -> notes/bank-c9-text-data-map.md
- `C9:38A6` -> notes/bank-c9-text-data-map.md
- `C9:39B9` -> notes/bank-c9-text-data-map.md
- `C9:3A00` -> notes/bank-c9-text-data-map.md
- `C9:3A2E` -> notes/bank-c9-text-data-map.md
- `C9:3A82` -> notes/bank-c9-text-data-map.md
- `C9:3AC1` -> notes/bank-c9-text-data-map.md
- `C9:53BE` -> notes/bank-c9-text-data-map.md
- `C9:53BF` -> notes/bank-c9-text-data-map.md
- `C9:53F7` -> notes/bank-c9-text-data-map.md
- `C9:54B3` -> notes/bank-c9-text-data-map.md
- `C9:54E1` -> notes/bank-c9-text-data-map.md
- `C9:5532` -> notes/bank-c9-text-data-map.md
- `C9:560B` -> notes/bank-c9-text-data-map.md
- `C9:564F` -> notes/bank-c9-text-data-map.md
- `C9:5673` -> notes/bank-c9-text-data-map.md
- `C9:6D0F` -> notes/bank-c9-text-data-map.md
- `C9:6D10` -> notes/bank-c9-text-data-map.md
- `C9:6D4F` -> notes/bank-c9-text-data-map.md
- `C9:6D6A` -> notes/bank-c9-text-data-map.md
- `C9:6D8A` -> notes/bank-c9-text-data-map.md
- `C9:6DB2` -> notes/bank-c9-text-data-map.md
- `C9:6DEC` -> notes/bank-c9-text-data-map.md
- `C9:6E07` -> notes/bank-c9-text-data-map.md
- `C9:6E22` -> notes/bank-c9-text-data-map.md
- `C9:7B6A` -> notes/bank-c9-text-data-map.md
- `C9:7B6B` -> notes/bank-c9-text-data-map.md, notes/class2-cc19-1f-cross-segment-reuse.md, notes/class2-healing-amount-family-c29ab8-c29ae1.md
- `C9:7BAB` -> notes/bank-c9-text-data-map.md
- `C9:7BC4` -> notes/bank-c9-text-data-map.md
- `C9:7C06` -> notes/bank-c9-text-data-map.md
- `C9:7C30` -> notes/bank-c9-text-data-map.md
- `C9:7C5F` -> notes/bank-c9-text-data-map.md
- `C9:7C7B` -> notes/bank-c9-text-data-map.md
- `C9:7C9D` -> notes/bank-c9-text-data-map.md
- `C9:7E9E` -> notes/class2-bomb-common-family-c2a658-c2a821.md
- `C9:7EB7` -> notes/class2-bomb-common-family-c2a658-c2a821.md
- `C9:7F56` -> notes/class2-solidification-item-action-c2a5ec-a630.md
- `C9:7FB2` -> notes/bank-c9-text-data-map.md
- `C9:7FB3` -> notes/bank-c9-first-pass.md, notes/bank-c9-text-data-map.md
- `C9:7FFF` -> notes/bank-c9-first-pass.md, notes/bank-c9-text-data-map.md
- `C9:8000` -> notes/bank-c9-text-data-map.md
- `C9:8024` -> notes/bank-c9-text-data-map.md
- `C9:80C1` -> notes/bank-c9-text-data-map.md
- `C9:8148` -> notes/bank-c9-text-data-map.md
- `C9:817A` -> notes/bank-c9-text-data-map.md
- `C9:81C6` -> notes/bank-c9-text-data-map.md
- `C9:827C` -> notes/bank-c9-text-data-map.md
- `C9:82B3` -> notes/bank-c9-text-data-map.md
- `C9:8571` -> notes/text-command-06-jump-if-flag-set.md
- `C9:992E` -> notes/bank-c9-text-data-map.md
- `C9:9930` -> notes/bank-c9-first-pass.md, notes/bank-c9-text-data-map.md
- `C9:9945` -> notes/bank-c9-text-data-map.md
- `C9:995D` -> notes/bank-c9-first-pass.md, notes/bank-c9-text-data-map.md
- `C9:9981` -> notes/bank-c9-text-data-map.md
- `C9:9991` -> notes/bank-c9-text-data-map.md
- `C9:99A1` -> notes/bank-c9-first-pass.md, notes/bank-c9-text-data-map.md
- ... 68 more

## Suggested Workflow

1. Pick an unmentioned `unknown/...` chunk from this report.
2. Run `tools/decode_snippet.py` or a targeted helper around the address.
3. Cross-check `refs/ebsrc-main` symbols, `refs/earthbound-disasm-legacy`, and any data table in `refs/eb-decompile-4ef92` that the routine touches.
4. Write a focused note that states byte-level evidence, borrowed reference names, remaining uncertainty, and direct callers/xrefs.
5. Rerun this audit and promote the next gap.

