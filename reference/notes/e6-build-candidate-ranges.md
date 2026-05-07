# E6 build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `14`
- total bytes: `65536`
- source bytes: `0`
- data gap bytes: `65536`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/e6/table_000_inline_audio_pack_1.asm` | `E6:0000..E6:0002` | 2 | 0 | 2 | `34d4fc077e54157726ae9b0adda15b8bff84a418` |
| `build-candidate` | `src/e6/table_001_inline_word.asm` | `E6:0002..E6:0004` | 2 | 0 | 2 | `4428868981ef6556daaf1e0de8a79aee292d477c` |
| `build-candidate` | `src/e6/table_002_inline_audio_subpack_0_data_start.asm` | `E6:0004..E6:0022` | 30 | 0 | 30 | `fe92c6928b1b5527af8df84f9e48115e22b425d0` |
| `build-candidate` | `src/e6/table_003_inline_audio_subpack_0_data_end.asm` | `E6:0022..E6:0024` | 2 | 0 | 2 | `bff9cd3d2942e27ef1abaf545d8b0e0b86603731` |
| `build-candidate` | `src/e6/table_004_inline_word.asm` | `E6:0024..E6:0026` | 2 | 0 | 2 | `ef05a40d9e4cdc8261845e4162b8db6a391cf016` |
| `build-candidate` | `src/e6/table_005_inline_audio_subpack_1_data_start.asm` | `E6:0026..E6:003E` | 24 | 0 | 24 | `2bd5f7ba629c35162418bbecd59639d7dc549ce6` |
| `build-candidate` | `src/e6/table_006_inline_audio_subpack_1_data_end.asm` | `E6:003E..E6:0040` | 2 | 0 | 2 | `b982886bed4a4c500f57ab1a342b66c4e1078a81` |
| `build-candidate` | `src/e6/table_007_inline_word.asm` | `E6:0040..E6:0042` | 2 | 0 | 2 | `6bc896c1c613812cb90989f1ee99b46ccc697e8f` |
| `build-candidate` | `src/e6/table_008_incbin_main_spc700_bin.asm` | `E6:0042..E6:45D8` | 17814 | 0 | 17814 | `cb5bac7dd52f2b0de2bc6aa27c18f34e956c16d2` |
| `build-candidate` | `src/e6/asset_audio_pack_74.asm` | `E6:45D8..E6:8B9A` | 17858 | 0 | 17858 | `eedb066c87ee37ad34cf671e1261c6b1c50622ab` |
| `build-candidate` | `src/e6/asset_audio_pack_76.asm` | `E6:8B9A..E6:CF08` | 17262 | 0 | 17262 | `9b6c25e09d32562c7f4be03761e8b025bb60a485` |
| `build-candidate` | `src/e6/asset_audio_pack_47.asm` | `E6:CF08..E6:FF18` | 12304 | 0 | 12304 | `c75987e2afc0547ca9b3ddf5bef78635128fc649` |
| `build-candidate` | `src/e6/asset_audio_pack_73.asm` | `E6:FF18..E6:FFF5` | 221 | 0 | 221 | `4771e9c6622793bfc04f062e6363fe8f085a90ee` |
| `build-candidate` | `src/e6/asset_bank_e6_gap_1_tailpadding.asm` | `E6:FFF5..E6:10000` | 11 | 0 | 11 | `e89931b7aa0422594a6876f9bd77450cdb6353ec` |

## Source Segments

### `src/e6/table_000_inline_audio_pack_1.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:0000..E6:0002` (`2` bytes, SHA-1 `34d4fc077e54157726ae9b0adda15b8bff84a418`) `TableInlineAudioPack1`

Labels:

- `E6:0000 TableInlineAudioPack1`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/table_001_inline_word.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:0002..E6:0004` (`2` bytes, SHA-1 `4428868981ef6556daaf1e0de8a79aee292d477c`) `TableInlineWord`

Labels:

- `E6:0002 TableInlineWord`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/table_002_inline_audio_subpack_0_data_start.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:0004..E6:0022` (`30` bytes, SHA-1 `fe92c6928b1b5527af8df84f9e48115e22b425d0`) `TableInlineAudioSubpack0DataStart`

Labels:

- `E6:0004 TableInlineAudioSubpack0DataStart`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/table_003_inline_audio_subpack_0_data_end.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:0022..E6:0024` (`2` bytes, SHA-1 `bff9cd3d2942e27ef1abaf545d8b0e0b86603731`) `TableInlineAudioSubpack0DataEnd`

Labels:

- `E6:0022 TableInlineAudioSubpack0DataEnd`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/table_004_inline_word.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:0024..E6:0026` (`2` bytes, SHA-1 `ef05a40d9e4cdc8261845e4162b8db6a391cf016`) `TableInlineWord`

Labels:

- `E6:0024 TableInlineWord`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/table_005_inline_audio_subpack_1_data_start.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:0026..E6:003E` (`24` bytes, SHA-1 `2bd5f7ba629c35162418bbecd59639d7dc549ce6`) `TableInlineAudioSubpack1DataStart`

Labels:

- `E6:0026 TableInlineAudioSubpack1DataStart`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/table_006_inline_audio_subpack_1_data_end.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:003E..E6:0040` (`2` bytes, SHA-1 `b982886bed4a4c500f57ab1a342b66c4e1078a81`) `TableInlineAudioSubpack1DataEnd`

Labels:

- `E6:003E TableInlineAudioSubpack1DataEnd`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/table_007_inline_word.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:0040..E6:0042` (`2` bytes, SHA-1 `6bc896c1c613812cb90989f1ee99b46ccc697e8f`) `TableInlineWord`

Labels:

- `E6:0040 TableInlineWord`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/table_008_incbin_main_spc700_bin.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:0042..E6:45D8` (`17814` bytes, SHA-1 `cb5bac7dd52f2b0de2bc6aa27c18f34e956c16d2`) `TableIncbinMainSpc700`

Labels:

- `E6:0042 TableIncbinMainSpc700`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/asset_audio_pack_74.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:45D8..E6:8B9A` (`17858` bytes, SHA-1 `eedb066c87ee37ad34cf671e1261c6b1c50622ab`) `AssetAudioPack74`

Labels:

- `E6:45D8 AssetAudioPack74`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/asset_audio_pack_76.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:8B9A..E6:CF08` (`17262` bytes, SHA-1 `9b6c25e09d32562c7f4be03761e8b025bb60a485`) `AssetAudioPack76`

Labels:

- `E6:8B9A AssetAudioPack76`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/asset_audio_pack_47.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:CF08..E6:FF18` (`12304` bytes, SHA-1 `c75987e2afc0547ca9b3ddf5bef78635128fc649`) `AssetAudioPack47`

Labels:

- `E6:CF08 AssetAudioPack47`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/asset_audio_pack_73.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:FF18..E6:FFF5` (`221` bytes, SHA-1 `4771e9c6622793bfc04f062e6363fe8f085a90ee`) `AssetAudioPack73`

Labels:

- `E6:FF18 AssetAudioPack73`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

### `src/e6/asset_bank_e6_gap_1_tailpadding.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E6:FFF5..E6:10000` (`11` bytes, SHA-1 `e89931b7aa0422594a6876f9bd77450cdb6353ec`) `AssetBankE6Gap1TailPadding`

Labels:

- `E6:FFF5 AssetBankE6Gap1TailPadding`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank26.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e6.json`
- `notes/bank-e6-asset-data-map.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
