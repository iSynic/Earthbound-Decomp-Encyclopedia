# C5 build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `9`
- total bytes: `65536`
- source bytes: `0`
- data gap bytes: `65536`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/c5/text_eshop0.asm` | `C5:0000..C5:3711` | 14097 | 0 | 14097 | `b2060e792a0736a96dd29846ef401608bc6e48ca` |
| `build-candidate` | `src/c5/text_eexplgds.asm` | `C5:3711..C5:6DF3` | 14050 | 0 | 14050 | `1820fd810c3201ad557c99d5e8dc21c59c503f03` |
| `build-candidate` | `src/c5/text_e13skrb.asm` | `C5:6DF3..C5:7E1C` | 4137 | 0 | 4137 | `d7e7320206f8c40b1275ff579ec620acce5f9b5c` |
| `build-candidate` | `src/c5/text_e17past.asm` | `C5:7E1C..C5:7FC1` | 421 | 0 | 421 | `415e1ded772d45ebdd44df87530041243e866dec` |
| `build-candidate` | `src/c5/text_bank_c5_gap_1_alignmentgap.asm` | `C5:7FC1..C5:8000` | 63 | 0 | 63 | `0b8bf9fc37ad802cefa6733ec62b09d5f43a1b75` |
| `build-candidate` | `src/c5/text_edebug.asm` | `C5:8000..C5:B3BA` | 13242 | 0 | 13242 | `1400e0bc440054b43c712db304d0e833efedad7e` |
| `build-candidate` | `src/c5/text_eshop1.asm` | `C5:B3BA..C5:E5BC` | 12802 | 0 | 12802 | `ef8bece9d568cc346b9283dd401a49d547dc268c` |
| `build-candidate` | `src/c5/text_eevent0.asm` | `C5:E5BC..C5:FFEC` | 6704 | 0 | 6704 | `b774d293a65ed057505899768af5b90c5eadc75e` |
| `build-candidate` | `src/c5/text_bank_c5_gap_2_tailpadding.asm` | `C5:FFEC..C5:10000` | 20 | 0 | 20 | `6768033e216468247bd031a0a2d9876d79818f8f` |

## Source Segments

### `src/c5/text_eshop0.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C5:0000..C5:3711` (`14097` bytes, SHA-1 `b2060e792a0736a96dd29846ef401608bc6e48ca`) `TextSegmentEshop0`

Labels:

- `C5:0000 TextSegmentEshop0`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank05.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c5.json`
- `notes/bank-c5-text-data-map.md`

### `src/c5/text_eexplgds.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C5:3711..C5:6DF3` (`14050` bytes, SHA-1 `1820fd810c3201ad557c99d5e8dc21c59c503f03`) `TextSegmentEexplgds`

Labels:

- `C5:3711 TextSegmentEexplgds`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank05.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c5.json`
- `notes/bank-c5-text-data-map.md`

### `src/c5/text_e13skrb.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C5:6DF3..C5:7E1C` (`4137` bytes, SHA-1 `d7e7320206f8c40b1275ff579ec620acce5f9b5c`) `TextSegmentE13skrb`

Labels:

- `C5:6DF3 TextSegmentE13skrb`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank05.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c5.json`
- `notes/bank-c5-text-data-map.md`

### `src/c5/text_e17past.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C5:7E1C..C5:7FC1` (`421` bytes, SHA-1 `415e1ded772d45ebdd44df87530041243e866dec`) `TextSegmentE17past`

Labels:

- `C5:7E1C TextSegmentE17past`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank05.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c5.json`
- `notes/bank-c5-text-data-map.md`

### `src/c5/text_bank_c5_gap_1_alignmentgap.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C5:7FC1..C5:8000` (`63` bytes, SHA-1 `0b8bf9fc37ad802cefa6733ec62b09d5f43a1b75`) `TextBankC5Gap1AlignmentGap`

Labels:

- `C5:7FC1 TextBankC5Gap1AlignmentGap`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank05.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c5.json`
- `notes/bank-c5-text-data-map.md`

### `src/c5/text_edebug.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C5:8000..C5:B3BA` (`13242` bytes, SHA-1 `1400e0bc440054b43c712db304d0e833efedad7e`) `TextSegmentEdebug`

Labels:

- `C5:8000 TextSegmentEdebug`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank05.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c5.json`
- `notes/bank-c5-text-data-map.md`

### `src/c5/text_eshop1.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C5:B3BA..C5:E5BC` (`12802` bytes, SHA-1 `ef8bece9d568cc346b9283dd401a49d547dc268c`) `TextSegmentEshop1`

Labels:

- `C5:B3BA TextSegmentEshop1`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank05.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c5.json`
- `notes/bank-c5-text-data-map.md`

### `src/c5/text_eevent0.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C5:E5BC..C5:FFEC` (`6704` bytes, SHA-1 `b774d293a65ed057505899768af5b90c5eadc75e`) `TextSegmentEevent0`

Labels:

- `C5:E5BC TextSegmentEevent0`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank05.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c5.json`
- `notes/bank-c5-text-data-map.md`

### `src/c5/text_bank_c5_gap_2_tailpadding.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `C5:FFEC..C5:10000` (`20` bytes, SHA-1 `6768033e216468247bd031a0a2d9876d79818f8f`) `TextBankC5Gap2TailPadding`

Labels:

- `C5:FFEC TextBankC5Gap2TailPadding`

Evidence:

- `refs\ebsrc-main\ebsrc-main\src\bankconfig\US\bank05.asm`
- `refs\ebsrc-main\ebsrc-main\earthbound.yml`
- `build/text-bank-c5.json`
- `notes/bank-c5-text-data-map.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
