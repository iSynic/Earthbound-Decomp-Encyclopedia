# E4 build-candidate byte ranges

This manifest records source slices promoted into the reusable source-bank scaffold pipeline.

## Summary

- ranges: `6`
- total bytes: `65536`
- source bytes: `0`
- data gap bytes: `65536`

## Ranges

| Level | Source Path | Range | Span Bytes | Source Bytes | Data Gap Bytes | SHA-1 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `build-candidate` | `src/e4/asset_audio_pack_64.asm` | `E4:0000..E4:514A` | 20810 | 0 | 20810 | `6a286fabc724986769acb5acbdde8f566f3c861f` |
| `build-candidate` | `src/e4/asset_audio_pack_42.asm` | `E4:514A..E4:A232` | 20712 | 0 | 20712 | `eefacc2d2464ef7864085b51574a451ba1b06acb` |
| `build-candidate` | `src/e4/asset_audio_pack_126.asm` | `E4:A232..E4:EED0` | 19614 | 0 | 19614 | `828a859f29a4d36a0a75db7a22c850184b58941a` |
| `build-candidate` | `src/e4/asset_audio_pack_125.asm` | `E4:EED0..E4:FD92` | 3778 | 0 | 3778 | `2addf288d357da0e39aced77a4b602c4bae77eaf` |
| `build-candidate` | `src/e4/asset_audio_pack_155.asm` | `E4:FD92..E4:FFF9` | 615 | 0 | 615 | `15dcaca2f48785c4fcf34b6b40cbea76358840bc` |
| `build-candidate` | `src/e4/asset_bank_e4_gap_1_tailpadding.asm` | `E4:FFF9..E4:10000` | 7 | 0 | 7 | `77ce0377defbd11b77b1f4ad54ca40ea5ef28490` |

## Source Segments

### `src/e4/asset_audio_pack_64.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E4:0000..E4:514A` (`20810` bytes, SHA-1 `6a286fabc724986769acb5acbdde8f566f3c861f`) `AssetAudioPack64`

Labels:

- `E4:0000 AssetAudioPack64`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank24.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e4.json`
- `notes/bank-e4-asset-data-map.md`

### `src/e4/asset_audio_pack_42.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E4:514A..E4:A232` (`20712` bytes, SHA-1 `eefacc2d2464ef7864085b51574a451ba1b06acb`) `AssetAudioPack42`

Labels:

- `E4:514A AssetAudioPack42`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank24.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e4.json`
- `notes/bank-e4-asset-data-map.md`

### `src/e4/asset_audio_pack_126.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E4:A232..E4:EED0` (`19614` bytes, SHA-1 `828a859f29a4d36a0a75db7a22c850184b58941a`) `AssetAudioPack126`

Labels:

- `E4:A232 AssetAudioPack126`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank24.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e4.json`
- `notes/bank-e4-asset-data-map.md`

### `src/e4/asset_audio_pack_125.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E4:EED0..E4:FD92` (`3778` bytes, SHA-1 `2addf288d357da0e39aced77a4b602c4bae77eaf`) `AssetAudioPack125`

Labels:

- `E4:EED0 AssetAudioPack125`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank24.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e4.json`
- `notes/bank-e4-asset-data-map.md`

### `src/e4/asset_audio_pack_155.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E4:FD92..E4:FFF9` (`615` bytes, SHA-1 `15dcaca2f48785c4fcf34b6b40cbea76358840bc`) `AssetAudioPack155`

Labels:

- `E4:FD92 AssetAudioPack155`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank24.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e4.json`
- `notes/bank-e4-asset-data-map.md`

### `src/e4/asset_bank_e4_gap_1_tailpadding.asm`

| Range | Size | Name | SHA-1 |
| --- | ---: | --- | --- |
| n/a | 0 | `data-only protected span` | n/a |

Data gaps inside protected span:

- `E4:FFF9..E4:10000` (`7` bytes, SHA-1 `77ce0377defbd11b77b1f4ad54ca40ea5ef28490`) `AssetBankE4Gap1TailPadding`

Labels:

- `E4:FFF9 AssetBankE4Gap1TailPadding`

Evidence:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank24.asm`
- `refs/ebsrc-main/ebsrc-main/earthbound.yml`
- `build/asset-bank-e4.json`
- `notes/bank-e4-asset-data-map.md`

## Notes

The scaffold preserves intentional source-adjacent data gaps from the manifest and validates each protected span against the original ROM bytes.
