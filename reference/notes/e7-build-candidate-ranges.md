# E7 build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `5`
- total bytes: `65536`
- source bytes: `0`
- data gap bytes: `65536`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/e7/asset_audio_pack_78.asm` | `E7:0000..E7:4314` | 17172 | 0 | 17172 | `9db727d6424576235d1ec92dadbddcd7f69b5a9f` |
| `build-candidate` | `src/e7/asset_audio_pack_82.asm` | `E7:4314..E7:849C` | 16776 | 0 | 16776 | `094174ee5b6730a3b3c653f09270d75a43c6eee6` |
| `build-candidate` | `src/e7/asset_audio_pack_8.asm` | `E7:849C..E7:C5C8` | 16684 | 0 | 16684 | `e93744fc72ce163ec66456dcbfa030a999f10620` |
| `build-candidate` | `src/e7/asset_audio_pack_24.asm` | `E7:C5C8..E7:FF64` | 14748 | 0 | 14748 | `15421eb445da2e9c476323a5b332c00f116e6dc6` |
| `build-candidate` | `src/e7/asset_bank_e7_gap_1_tailpadding.asm` | `E7:FF64..E7:10000` | 156 | 0 | 156 | `7686dac4e3d704c9cb83a73c261f94882bca141e` |

## Source Segments

### `src/e7/asset_audio_pack_78.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E7:0000..E7:4314` (`17172` bytes, SHA-1 `9db727d6424576235d1ec92dadbddcd7f69b5a9f`) `AssetAudioPack78`

Labels:

- `E7:0000 AssetAudioPack78`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank27.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e7.json`
- `notes/bank-e7-asset-data-map.md`

### `src/e7/asset_audio_pack_82.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E7:4314..E7:849C` (`16776` bytes, SHA-1 `094174ee5b6730a3b3c653f09270d75a43c6eee6`) `AssetAudioPack82`

Labels:

- `E7:4314 AssetAudioPack82`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank27.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e7.json`
- `notes/bank-e7-asset-data-map.md`

### `src/e7/asset_audio_pack_8.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E7:849C..E7:C5C8` (`16684` bytes, SHA-1 `e93744fc72ce163ec66456dcbfa030a999f10620`) `AssetAudioPack8`

Labels:

- `E7:849C AssetAudioPack8`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank27.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e7.json`
- `notes/bank-e7-asset-data-map.md`

### `src/e7/asset_audio_pack_24.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E7:C5C8..E7:FF64` (`14748` bytes, SHA-1 `15421eb445da2e9c476323a5b332c00f116e6dc6`) `AssetAudioPack24`

Labels:

- `E7:C5C8 AssetAudioPack24`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank27.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e7.json`
- `notes/bank-e7-asset-data-map.md`

### `src/e7/asset_bank_e7_gap_1_tailpadding.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E7:FF64..E7:10000` (`156` bytes, SHA-1 `7686dac4e3d704c9cb83a73c261f94882bca141e`) `AssetBankE7Gap1TailPadding`

Labels:

- `E7:FF64 AssetBankE7Gap1TailPadding`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank27.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e7.json`
- `notes/bank-e7-asset-data-map.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
