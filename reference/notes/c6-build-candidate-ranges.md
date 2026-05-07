# C6 build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `9`
- total bytes: `65536`
- source bytes: `0`
- data gap bytes: `65536`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/c6/text_e09dsrt.asm` | `C6:0000..C6:2D30` | 11568 | 0 | 11568 | `1326c7a4134476506a832df7d5feac6883db9426` |
| `build-candidate` | `src/c6/text_eshop3.asm` | `C6:2D30..C6:59C9` | 11417 | 0 | 11417 | `07f91c389c84c7225ebc67f493737492685ebbfa` |
| `build-candidate` | `src/c6/text_e01onet2.asm` | `C6:59C9..C6:7EEC` | 9507 | 0 | 9507 | `03f057edde7612974e45492e24d36a31ee717a1b` |
| `build-candidate` | `src/c6/text_bank_c6_gap_1_alignmentgap.asm` | `C6:7EEC..C6:8000` | 276 | 0 | 276 | `6b01519b9a995c5bb1ecb39f80980be2a335f10d` |
| `build-candidate` | `src/c6/text_eglobal.asm` | `C6:8000..C6:A9F9` | 10745 | 0 | 10745 | `fb955803fb5494b3f8df703d5e8fb50ebdc4fc3f` |
| `build-candidate` | `src/c6/text_e06wins.asm` | `C6:A9F9..C6:D19C` | 10147 | 0 | 10147 | `243ee64fd2899acb116df651cd172ac1e18b43b6` |
| `build-candidate` | `src/c6/text_e10four0.asm` | `C6:D19C..C6:F8D9` | 10045 | 0 | 10045 | `f7bb11d0a9089bf3c224c75ffd0bbb57fe4ccd31` |
| `build-candidate` | `src/c6/text_egoods3.asm` | `C6:F8D9..C6:FFE3` | 1802 | 0 | 1802 | `86f489a00eda61a5f640408faadd17c976721f18` |
| `build-candidate` | `src/c6/text_bank_c6_gap_2_tailpadding.asm` | `C6:FFE3..C6:10000` | 29 | 0 | 29 | `1da89865c5192465f8f4fe62d454c2175aff4441` |

## Source Segments

### `src/c6/text_e09dsrt.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C6:0000..C6:2D30` (`11568` bytes, SHA-1 `1326c7a4134476506a832df7d5feac6883db9426`) `TextSegmentE09dsrt`

Labels:

- `C6:0000 TextSegmentE09dsrt`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank06.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c6.json`
- `notes/bank-c6-text-data-map.md`

### `src/c6/text_eshop3.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C6:2D30..C6:59C9` (`11417` bytes, SHA-1 `07f91c389c84c7225ebc67f493737492685ebbfa`) `TextSegmentEshop3`

Labels:

- `C6:2D30 TextSegmentEshop3`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank06.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c6.json`
- `notes/bank-c6-text-data-map.md`

### `src/c6/text_e01onet2.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C6:59C9..C6:7EEC` (`9507` bytes, SHA-1 `03f057edde7612974e45492e24d36a31ee717a1b`) `TextSegmentE01onet2`

Labels:

- `C6:59C9 TextSegmentE01onet2`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank06.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c6.json`
- `notes/bank-c6-text-data-map.md`

### `src/c6/text_bank_c6_gap_1_alignmentgap.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C6:7EEC..C6:8000` (`276` bytes, SHA-1 `6b01519b9a995c5bb1ecb39f80980be2a335f10d`) `TextBankC6Gap1AlignmentGap`

Labels:

- `C6:7EEC TextBankC6Gap1AlignmentGap`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank06.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c6.json`
- `notes/bank-c6-text-data-map.md`

### `src/c6/text_eglobal.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C6:8000..C6:A9F9` (`10745` bytes, SHA-1 `fb955803fb5494b3f8df703d5e8fb50ebdc4fc3f`) `TextSegmentEglobal`

Labels:

- `C6:8000 TextSegmentEglobal`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank06.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c6.json`
- `notes/bank-c6-text-data-map.md`

### `src/c6/text_e06wins.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C6:A9F9..C6:D19C` (`10147` bytes, SHA-1 `243ee64fd2899acb116df651cd172ac1e18b43b6`) `TextSegmentE06wins`

Labels:

- `C6:A9F9 TextSegmentE06wins`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank06.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c6.json`
- `notes/bank-c6-text-data-map.md`

### `src/c6/text_e10four0.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C6:D19C..C6:F8D9` (`10045` bytes, SHA-1 `f7bb11d0a9089bf3c224c75ffd0bbb57fe4ccd31`) `TextSegmentE10four0`

Labels:

- `C6:D19C TextSegmentE10four0`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank06.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c6.json`
- `notes/bank-c6-text-data-map.md`

### `src/c6/text_egoods3.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C6:F8D9..C6:FFE3` (`1802` bytes, SHA-1 `86f489a00eda61a5f640408faadd17c976721f18`) `TextSegmentEgoods3`

Labels:

- `C6:F8D9 TextSegmentEgoods3`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank06.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c6.json`
- `notes/bank-c6-text-data-map.md`

### `src/c6/text_bank_c6_gap_2_tailpadding.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C6:FFE3..C6:10000` (`29` bytes, SHA-1 `1da89865c5192465f8f4fe62d454c2175aff4441`) `TextBankC6Gap2TailPadding`

Labels:

- `C6:FFE3 TextBankC6Gap2TailPadding`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank06.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c6.json`
- `notes/bank-c6-text-data-map.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
