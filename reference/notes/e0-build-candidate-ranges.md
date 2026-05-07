# E0 build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `16`
- total bytes: `65536`
- source bytes: `0`
- data gap bytes: `65536`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/e0/asset_text_window_gfx.asm` | `E0:0000..E0:0754` | 1876 | 0 | 1876 | `f86cf38637a73b38b39929e06f389521696a1364` |
| `build-candidate` | `src/e0/asset_flavoured_text_gfx.asm` | `E0:0754..E0:07A0` | 76 | 0 | 76 | `d3028adb1b1111b0d5c70585f7d156a4ef854b94` |
| `build-candidate` | `src/e0/asset_mother2_romaji_font.asm` | `E0:07A0..E0:09B4` | 532 | 0 | 532 | `8cab1a236be6bd4a44b2ef45b2f34b6c46e1762b` |
| `build-candidate` | `src/e0/asset_compressed_sram.asm` | `E0:09B4..E0:1359` | 2469 | 0 | 2469 | `f299c53926f4dde193574274bca00e246bf48dce` |
| `build-candidate` | `src/e0/asset_mrsaturn_font_data.asm` | `E0:1359..E0:13B9` | 96 | 0 | 96 | `9dcdb1e85f8113b44d01717367d36b028091acd1` |
| `build-candidate` | `src/e0/asset_mrsaturn_font_gfx.asm` | `E0:13B9..E0:1FB9` | 3072 | 0 | 3072 | `e8c84354970e02afb08db511261918bd0b3829c3` |
| `build-candidate` | `src/e0/table_006_data_text_window_properties_asm.asm` | `E0:1FB9..E0:21A8` | 495 | 0 | 495 | `41b830b1870d5a4351fe5787af1e07ef862b4a50` |
| `build-candidate` | `src/e0/asset_town_map_onett.asm` | `E0:21A8..E0:4920` | 10104 | 0 | 10104 | `6029152fc6edc70fda98155f8e3734d493b063cb` |
| `build-candidate` | `src/e0/asset_town_map_twoson.asm` | `E0:4920..E0:6721` | 7681 | 0 | 7681 | `56326d834b86218dff703ed6182fd7cba8a3a015` |
| `build-candidate` | `src/e0/asset_town_map_threed.asm` | `E0:6721..E0:8379` | 7256 | 0 | 7256 | `6062db302d52fe851ead3a7cd2323da50ae8b5ab` |
| `build-candidate` | `src/e0/asset_town_map_fourside.asm` | `E0:8379..E0:ADB4` | 10811 | 0 | 10811 | `b0fb80bb899b760924b283bab7a074f235940840` |
| `build-candidate` | `src/e0/asset_town_map_scaraba.asm` | `E0:ADB4..E0:C7F1` | 6717 | 0 | 6717 | `72e7c29906134b7829c9c36625fe2b230a05770e` |
| `build-candidate` | `src/e0/asset_town_map_summers.asm` | `E0:C7F1..E0:ED03` | 9490 | 0 | 9490 | `f295511ec28d62ed670d8d2b4ea4106e85970b92` |
| `build-candidate` | `src/e0/asset_audio_pack_110.asm` | `E0:ED03..E0:FCE1` | 4062 | 0 | 4062 | `bb2842a87afb341dd46d05649413f2f8a12cb725` |
| `build-candidate` | `src/e0/asset_audio_pack_6.asm` | `E0:FCE1..E0:FFB3` | 722 | 0 | 722 | `476368a2a121f94b69a9baa2e3ec52a1fa834bd1` |
| `build-candidate` | `src/e0/asset_bank_e0_gap_1_tailpadding.asm` | `E0:FFB3..E0:10000` | 77 | 0 | 77 | `9898d25a214dba04ebd7e3030ac9e2e90ea7a369` |

## Source Segments

### `src/e0/asset_text_window_gfx.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:0000..E0:0754` (`1876` bytes, SHA-1 `f86cf38637a73b38b39929e06f389521696a1364`) `AssetTextWindowGfx`

Labels:

- `E0:0000 AssetTextWindowGfx`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_flavoured_text_gfx.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:0754..E0:07A0` (`76` bytes, SHA-1 `d3028adb1b1111b0d5c70585f7d156a4ef854b94`) `AssetFlavouredTextGfx`

Labels:

- `E0:0754 AssetFlavouredTextGfx`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_mother2_romaji_font.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:07A0..E0:09B4` (`532` bytes, SHA-1 `8cab1a236be6bd4a44b2ef45b2f34b6c46e1762b`) `AssetMother2RomajiFont`

Labels:

- `E0:07A0 AssetMother2RomajiFont`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_compressed_sram.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:09B4..E0:1359` (`2469` bytes, SHA-1 `f299c53926f4dde193574274bca00e246bf48dce`) `AssetCompressedSram`

Labels:

- `E0:09B4 AssetCompressedSram`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_mrsaturn_font_data.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:1359..E0:13B9` (`96` bytes, SHA-1 `9dcdb1e85f8113b44d01717367d36b028091acd1`) `AssetMrsaturnFontData`

Labels:

- `E0:1359 AssetMrsaturnFontData`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_mrsaturn_font_gfx.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:13B9..E0:1FB9` (`3072` bytes, SHA-1 `e8c84354970e02afb08db511261918bd0b3829c3`) `AssetMrsaturnFontGfx`

Labels:

- `E0:13B9 AssetMrsaturnFontGfx`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/table_006_data_text_window_properties_asm.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:1FB9..E0:21A8` (`495` bytes, SHA-1 `41b830b1870d5a4351fe5787af1e07ef862b4a50`) `TableTextWindowProperties`

Labels:

- `E0:1FB9 TableTextWindowProperties`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_town_map_onett.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:21A8..E0:4920` (`10104` bytes, SHA-1 `6029152fc6edc70fda98155f8e3734d493b063cb`) `AssetTownMapOnett`

Labels:

- `E0:21A8 AssetTownMapOnett`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_town_map_twoson.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:4920..E0:6721` (`7681` bytes, SHA-1 `56326d834b86218dff703ed6182fd7cba8a3a015`) `AssetTownMapTwoson`

Labels:

- `E0:4920 AssetTownMapTwoson`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_town_map_threed.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:6721..E0:8379` (`7256` bytes, SHA-1 `6062db302d52fe851ead3a7cd2323da50ae8b5ab`) `AssetTownMapThreed`

Labels:

- `E0:6721 AssetTownMapThreed`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_town_map_fourside.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:8379..E0:ADB4` (`10811` bytes, SHA-1 `b0fb80bb899b760924b283bab7a074f235940840`) `AssetTownMapFourside`

Labels:

- `E0:8379 AssetTownMapFourside`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_town_map_scaraba.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:ADB4..E0:C7F1` (`6717` bytes, SHA-1 `72e7c29906134b7829c9c36625fe2b230a05770e`) `AssetTownMapScaraba`

Labels:

- `E0:ADB4 AssetTownMapScaraba`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_town_map_summers.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:C7F1..E0:ED03` (`9490` bytes, SHA-1 `f295511ec28d62ed670d8d2b4ea4106e85970b92`) `AssetTownMapSummers`

Labels:

- `E0:C7F1 AssetTownMapSummers`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_audio_pack_110.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:ED03..E0:FCE1` (`4062` bytes, SHA-1 `bb2842a87afb341dd46d05649413f2f8a12cb725`) `AssetAudioPack110`

Labels:

- `E0:ED03 AssetAudioPack110`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_audio_pack_6.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:FCE1..E0:FFB3` (`722` bytes, SHA-1 `476368a2a121f94b69a9baa2e3ec52a1fa834bd1`) `AssetAudioPack6`

Labels:

- `E0:FCE1 AssetAudioPack6`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

### `src/e0/asset_bank_e0_gap_1_tailpadding.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E0:FFB3..E0:10000` (`77` bytes, SHA-1 `9898d25a214dba04ebd7e3030ac9e2e90ea7a369`) `AssetBankE0Gap1TailPadding`

Labels:

- `E0:FFB3 AssetBankE0Gap1TailPadding`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank20.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e0.json`
- `notes/bank-e0-asset-data-map.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
