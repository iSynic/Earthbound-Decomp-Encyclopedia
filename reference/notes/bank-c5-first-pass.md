# Bank C5 First Pass

## Main result

Bank `C5` is a text-data bank, not a code/data frontier like `C0` through
`C4`.

Follow-up source-scaffold status:

- durable scaffold: `src/c5/bank_c5_helpers_asar.asm`
- manifest: `build/c5-build-candidate-ranges.json`
- handoff: `notes/bank-c5-source-scaffold-handoff.md`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `9`
- byte-equivalence: `OK`, `0` mismatches

The US ebsrc bank config has only support includes plus seven locale text
segments:

| Order | Segment | Bank segment | Role |
| ---: | --- | --- | --- |
| 0 | `ESHOP0` | `BANK05` | shop message block |
| 1 | `EEXPLGDS` | `BANK05` | item/goods explanation text |
| 2 | `E13SKRB` | `BANK05` | Scaraba text block |
| 3 | `E17PAST` | `BANK05` | Cave of the Past/Pokey text block |
| 4 | `EDEBUG` | `BANK05B` | debug text/script block |
| 5 | `ESHOP1` | `BANK05B` | shop message block |
| 6 | `EEVENT0` | `BANK05B` | event/message text block |

Generated map:

- `notes/bank-c5-text-data-map.md`
- `build/text-bank-c5.json`

The generated map currently reports:

- text segments: `7`
- total bytes: `65453`
- labels: `1527`
- parsed control commands: `22043`
- unknown parsed commands: `2`

The normal bank audit and frontier scorer now also handle `LOCALEINCLUDE`:

- `notes/bank-c5-progress-audit.md`
- `notes/bank-c5-cluster-map.md`

Both agree that C5 has no address-bearing unknown include frontier.

## Tooling added

### `tools/build_text_bank_manifest.py`

This is the reusable text-bank entry point for C5 and later text banks. It
combines:

- ebsrc US bank config `LOCALEINCLUDE` order
- `earthbound.yml` text-data offsets/sizes
- `earthbound.yml` `renameLabels` entries
- local ROM bytes
- the local text-command decoder

It emits both a JSON manifest and a markdown map.

Example:

```powershell
python tools\build_text_bank_manifest.py C5 --json-out build\text-bank-c5.json --markdown-out notes\bank-c5-text-data-map.md
```

I also tested it against `C6` as a preview. That means the tool is not just
hard-coded for C5.

### Text command decoder improvements

`tools/disasm_ebtext_script.py` now carries the locally documented family names
for top-level `0x18..0x1F` text-command families, plus the C5-relevant
subcommands that were already documented in the C1 text-command notes.

This initially lowered C5's unknown parsed command count from `79` to `4`. A
later C7-driven `0x1F` argument-width correction lowered it again to `2`, which
was a good sign that most of the previous noise was stale decoder vocabulary or
linear parser desync rather than new C5 behavior.

### Segment-filtered command search

`tools/find_ebtext_command.py` now accepts `--segment`, so C5 edge cases can be
checked without scanning every text segment.

Example:

```powershell
python tools\find_ebtext_command.py 1F EF --segment EEVENT0
```

### Text-bank scaffold promotion

`tools/promote_text_bank_to_source_scaffold.py` promotes a generated text-bank
manifest into the standard source-bank range manifest and data-corridor stubs.
For C5 it creates the seven locale text stubs plus the two explicit
alignment/tail gaps, then feeds the existing durable scaffold and
byte-equivalence validators.

Example:

```powershell
python tools\promote_text_bank_to_source_scaffold.py C5
python tools\build_source_bank_scaffold.py --bank C5
python tools\validate_source_bank_byte_equivalence.py --bank C5 --module all --combined --scaffold src\c5\bank_c5_helpers_asar.asm --strict
```

This promotion also exposed and fixed a reusable bank-end conversion issue in
`tools/rom_tools.py`: synthetic range ends such as `C5:10000` now map to the
next file offset by addition, rather than accidentally wrapping through a
bitwise address merge.

## Current C5 confidence boundary

Locally strong:

- C5's bank-level shape is text-only.
- The seven ebsrc text segments line up contiguously through the bank.
- The segment start/end addresses and byte sizes are pinned from `earthbound.yml`
  and the ROM.
- The label counts and first-label anchors are pinned from `renameLabels`.
- The ordinary text-command families used in C5 now line up with the C1
  command-family notes.

Still cautious:

- The two remaining unknown parsed hits should not be promoted as real command
  semantics yet. Both are in EDEBUG pointer-like spans (`C5:849F` and
  `C5:9994`), not in a player-facing script flow.
- `EDEBUG` has many private labels and dense non-player-facing flows, so it is
  a poor first target for semantic polishing.

## Recommended next move

Do not spend a long archaeology pass on C5 unless the goal is specifically text
script semantics. The bank is structurally closed as a text bank and now
byte-protected by the durable source scaffold.

The highest-value paths are:

1. Move to `C6` with the new text-bank scaffold promotion workflow.
2. Or, if staying in C5, pick one player-facing segment (`ESHOP0`, `EEXPLGDS`,
   `E13SKRB`, or `ESHOP1`) and write a focused note about how its script labels
   exercise the already-documented text-command families.
