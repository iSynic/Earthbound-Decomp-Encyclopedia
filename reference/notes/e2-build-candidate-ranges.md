# E2 build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `5`
- total bytes: `65536`
- source bytes: `0`
- data gap bytes: `65536`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/e2/asset_audio_pack_108.asm` | `E2:0000..E2:77F0` | 30704 | 0 | 30704 | `73b5a1523a19ecdb75c148afcae9de7850a6fcbf` |
| `build-candidate` | `src/e2/asset_audio_pack_0.asm` | `E2:77F0..E2:ED2C` | 30012 | 0 | 30012 | `a25d0da30c9feb370c3e5d14e9087d89d7d4a004` |
| `build-candidate` | `src/e2/asset_audio_pack_36.asm` | `E2:ED2C..E2:FC88` | 3932 | 0 | 3932 | `eaaf3d4ada282d3da02cf9ad6c664be7bb789c54` |
| `build-candidate` | `src/e2/asset_audio_pack_18.asm` | `E2:FC88..E2:FFFD` | 885 | 0 | 885 | `36c5423b54b630a919f7d59e2261cbd0e8498748` |
| `build-candidate` | `src/e2/asset_bank_e2_gap_1_tailpadding.asm` | `E2:FFFD..E2:10000` | 3 | 0 | 3 | `29e2dcfbb16f63bb0254df7585a15bb6fb5e927d` |

## Source Segments

### `src/e2/asset_audio_pack_108.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E2:0000..E2:77F0` (`30704` bytes, SHA-1 `73b5a1523a19ecdb75c148afcae9de7850a6fcbf`) `AssetAudioPack108`

Labels:

- `E2:0000 AssetAudioPack108`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank22.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e2.json`
- `notes/bank-e2-asset-data-map.md`

### `src/e2/asset_audio_pack_0.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E2:77F0..E2:ED2C` (`30012` bytes, SHA-1 `a25d0da30c9feb370c3e5d14e9087d89d7d4a004`) `AssetAudioPack0`

Labels:

- `E2:77F0 AssetAudioPack0`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank22.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e2.json`
- `notes/bank-e2-asset-data-map.md`

### `src/e2/asset_audio_pack_36.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E2:ED2C..E2:FC88` (`3932` bytes, SHA-1 `eaaf3d4ada282d3da02cf9ad6c664be7bb789c54`) `AssetAudioPack36`

Labels:

- `E2:ED2C AssetAudioPack36`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank22.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e2.json`
- `notes/bank-e2-asset-data-map.md`

### `src/e2/asset_audio_pack_18.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E2:FC88..E2:FFFD` (`885` bytes, SHA-1 `36c5423b54b630a919f7d59e2261cbd0e8498748`) `AssetAudioPack18`

Labels:

- `E2:FC88 AssetAudioPack18`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank22.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e2.json`
- `notes/bank-e2-asset-data-map.md`

### `src/e2/asset_bank_e2_gap_1_tailpadding.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E2:FFFD..E2:10000` (`3` bytes, SHA-1 `29e2dcfbb16f63bb0254df7585a15bb6fb5e927d`) `AssetBankE2Gap1TailPadding`

Labels:

- `E2:FFFD AssetBankE2Gap1TailPadding`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank22.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e2.json`
- `notes/bank-e2-asset-data-map.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
