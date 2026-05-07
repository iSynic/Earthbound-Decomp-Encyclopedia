# Bank C5 Decompilation Progress Audit

This report cross-checks the local `notes/*.md` corpus against the quarantined `ebsrc-main` US bank include maps and symbol lists.

Treat reference names as corroboration only: a bank entry is not considered understood here just because a side reference gave it a label.

## Bank `C5` / reference bank `05`

- Reference include entries: `9`
- Reference named include entries without an address in the path: `9`
- Reference address-bearing include entries: `0`
- Address-bearing unknown include entries: `0`
- Reference symbols: `2` (`2` semantic-ish, `0` placeholder/redirect/null)
- Local notes mention `68` distinct `C5:xxxx` addresses
- Reference addresses mentioned by local notes: `0` / `0`
- Unknown include entries not directly mentioned in local notes: `0`

### Reference-Named Include Families

These are already semantically grouped by `ebsrc-main`; use them as corroborating names, not as final local proof.

- `common.asm`
- `symbols/text.inc.asm`
- `text_data/ESHOP0.ebtxt`
- `text_data/EEXPLGDS.ebtxt`
- `text_data/E13SKRB.ebtxt`
- `text_data/E17PAST.ebtxt`
- `text_data/EDEBUG.ebtxt`
- `text_data/ESHOP1.ebtxt`
- `text_data/EEVENT0.ebtxt`

### Local-Only Address Mentions

These may be derived local discoveries, cross-bank targets, or address forms absent from the reference include/symbol map.

- `C5:0000` -> notes/bank-c5-text-data-map.md
- `C5:0198` -> notes/bank-c5-text-data-map.md
- `C5:0330` -> notes/bank-c5-text-data-map.md
- `C5:04C8` -> notes/bank-c5-text-data-map.md
- `C5:0660` -> notes/bank-c5-text-data-map.md
- `C5:07F8` -> notes/bank-c5-text-data-map.md
- `C5:0990` -> notes/bank-c5-text-data-map.md
- `C5:0A72` -> notes/bank-c5-text-data-map.md
- `C5:1700` -> notes/text-command-08-call-text.md
- `C5:1B93` -> notes/jeff-repair-item-name-bridge.md
- `C5:3710` -> notes/bank-c5-text-data-map.md
- `C5:3711` -> notes/bank-c5-text-data-map.md
- `C5:3750` -> notes/bank-c5-text-data-map.md
- `C5:3761` -> notes/bank-c5-text-data-map.md
- `C5:3772` -> notes/bank-c5-text-data-map.md
- `C5:37BC` -> notes/bank-c5-text-data-map.md
- `C5:3809` -> notes/bank-c5-text-data-map.md
- `C5:382A` -> notes/bank-c5-text-data-map.md
- `C5:384D` -> notes/bank-c5-text-data-map.md
- `C5:6DF2` -> notes/bank-c5-text-data-map.md
- `C5:6DF3` -> notes/bank-c5-text-data-map.md
- `C5:6DF9` -> notes/bank-c5-text-data-map.md
- `C5:6DFF` -> notes/bank-c5-text-data-map.md
- `C5:6E2C` -> notes/bank-c5-text-data-map.md
- `C5:6E5B` -> notes/bank-c5-text-data-map.md
- `C5:6E61` -> notes/bank-c5-text-data-map.md
- `C5:6E67` -> notes/bank-c5-text-data-map.md
- `C5:6ECA` -> notes/bank-c5-text-data-map.md
- `C5:7E1B` -> notes/bank-c5-text-data-map.md
- `C5:7E1C` -> notes/bank-c5-text-data-map.md
- `C5:7FC0` -> notes/bank-c5-text-data-map.md
- `C5:8000` -> notes/bank-c5-text-data-map.md, notes/text-command-0a-24bit-jump.md
- `C5:80DA` -> notes/bank-c5-text-data-map.md
- `C5:8103` -> notes/bank-c5-text-data-map.md
- `C5:812F` -> notes/bank-c5-text-data-map.md
- `C5:8148` -> notes/bank-c5-text-data-map.md
- `C5:81E7` -> notes/bank-c5-text-data-map.md
- `C5:81EE` -> notes/bank-c5-text-data-map.md
- `C5:8214` -> notes/bank-c5-text-data-map.md
- `C5:849F` -> notes/bank-c5-text-data-map.md
- `C5:8CF0` -> notes/service-script-pointer-table-c58cf4.md
- `C5:8CF4` -> notes/selector-row-config-family-ef0ee8.md, notes/service-script-pointer-table-c58cf4.md
- `C5:8CF8` -> notes/service-script-pointer-table-c58cf4.md
- `C5:8CFC` -> notes/service-script-pointer-table-c58cf4.md
- `C5:9994` -> notes/bank-c5-text-data-map.md
- `C5:B3B9` -> notes/bank-c5-text-data-map.md
- `C5:B3BA` -> notes/bank-c5-text-data-map.md
- `C5:B3EB` -> notes/bank-c5-text-data-map.md
- `C5:B3F6` -> notes/bank-c5-text-data-map.md
- `C5:B405` -> notes/bank-c5-text-data-map.md
- `C5:B426` -> notes/bank-c5-text-data-map.md
- `C5:B42E` -> notes/bank-c5-text-data-map.md
- `C5:B43C` -> notes/bank-c5-text-data-map.md
- `C5:B447` -> notes/bank-c5-text-data-map.md
- `C5:D844` -> notes/selector-row-config-family-ef0ee8.md
- `C5:DDF1` -> notes/selector-row-config-family-ef0ee8.md
- `C5:E25B` -> notes/offensive-defensive-item-check-c17708.md
- `C5:E5BB` -> notes/bank-c5-text-data-map.md
- `C5:E5BC` -> notes/bank-c5-text-data-map.md
- `C5:E5DF` -> notes/bank-c5-text-data-map.md
- `C5:E5EB` -> notes/bank-c5-text-data-map.md
- `C5:E605` -> notes/bank-c5-text-data-map.md
- `C5:E62C` -> notes/bank-c5-text-data-map.md
- `C5:E633` -> notes/bank-c5-text-data-map.md
- `C5:E655` -> notes/bank-c5-text-data-map.md
- `C5:E675` -> notes/bank-c5-text-data-map.md
- `C5:EA35` -> notes/post-transition-deferred-script-queue-c06b21-c06bff.md
- `C5:FFEB` -> notes/bank-c5-text-data-map.md

## Suggested Workflow

1. Pick an unmentioned `unknown/...` chunk from this report.
2. Run `tools/decode_snippet.py` or a targeted helper around the address.
3. Cross-check `refs/ebsrc-main` symbols, `refs/earthbound-disasm-legacy`, and any data table in `refs/eb-decompile-4ef92` that the routine touches.
4. Write a focused note that states byte-level evidence, borrowed reference names, remaining uncertainty, and direct callers/xrefs.
5. Rerun this audit and promote the next gap.

