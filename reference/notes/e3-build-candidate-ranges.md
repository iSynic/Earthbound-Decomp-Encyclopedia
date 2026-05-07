# E3 build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `5`
- total bytes: `65536`
- source bytes: `0`
- data gap bytes: `65536`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/e3/asset_audio_pack_3.asm` | `E3:0000..E3:5F64` | 24420 | 0 | 24420 | `894bec23386da9fa815f4659a67f67ca003a8583` |
| `build-candidate` | `src/e3/asset_audio_pack_70.asm` | `E3:5F64..E3:B0FA` | 20886 | 0 | 20886 | `a287acb2674cd8d32a7d3a2058dcee3da1ac2b7f` |
| `build-candidate` | `src/e3/asset_audio_pack_37.asm` | `E3:B0FA..E3:FDCC` | 19666 | 0 | 19666 | `443878d19185009e8d3de6637e12b39c13a544b3` |
| `build-candidate` | `src/e3/asset_audio_pack_32.asm` | `E3:FDCC..E3:FFF2` | 550 | 0 | 550 | `b31185c6a29d3b0309f4fc65054bd91b7ac75122` |
| `build-candidate` | `src/e3/asset_bank_e3_gap_1_tailpadding.asm` | `E3:FFF2..E3:10000` | 14 | 0 | 14 | `4595c5b7ac9f265cdf89acec0069630697680f96` |

## Source Segments

### `src/e3/asset_audio_pack_3.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E3:0000..E3:5F64` (`24420` bytes, SHA-1 `894bec23386da9fa815f4659a67f67ca003a8583`) `AssetAudioPack3`

Labels:

- `E3:0000 AssetAudioPack3`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank23.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e3.json`
- `notes/bank-e3-asset-data-map.md`

### `src/e3/asset_audio_pack_70.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E3:5F64..E3:B0FA` (`20886` bytes, SHA-1 `a287acb2674cd8d32a7d3a2058dcee3da1ac2b7f`) `AssetAudioPack70`

Labels:

- `E3:5F64 AssetAudioPack70`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank23.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e3.json`
- `notes/bank-e3-asset-data-map.md`

### `src/e3/asset_audio_pack_37.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E3:B0FA..E3:FDCC` (`19666` bytes, SHA-1 `443878d19185009e8d3de6637e12b39c13a544b3`) `AssetAudioPack37`

Labels:

- `E3:B0FA AssetAudioPack37`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank23.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e3.json`
- `notes/bank-e3-asset-data-map.md`

### `src/e3/asset_audio_pack_32.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E3:FDCC..E3:FFF2` (`550` bytes, SHA-1 `b31185c6a29d3b0309f4fc65054bd91b7ac75122`) `AssetAudioPack32`

Labels:

- `E3:FDCC AssetAudioPack32`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank23.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e3.json`
- `notes/bank-e3-asset-data-map.md`

### `src/e3/asset_bank_e3_gap_1_tailpadding.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E3:FFF2..E3:10000` (`14` bytes, SHA-1 `4595c5b7ac9f265cdf89acec0069630697680f96`) `AssetBankE3Gap1TailPadding`

Labels:

- `E3:FFF2 AssetBankE3Gap1TailPadding`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank23.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e3.json`
- `notes/bank-e3-asset-data-map.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
