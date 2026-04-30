# Audio Oracle Verification Report

Status: representative near-oracle passed; independent external-emulator and all-track gates remain open.

- scope: `representative_tracks`
- jobs: `20`
- statuses: `{'audio_equivalent_state_delta': 20}`
- oracle ids: `{'ares_full_change_music_load_apply_reference': 20}`
- oracle kinds: `{'backend_result_summary_import': 20}`

## Gates

- representative oracle gate passed: `True`
- independent emulator gate passed: `False`
- all-track oracle gate passed: `False`
- release-quality playback claim ready: `False`

## Audio Equivalence

- byte-exact WAV matches: `20 / 20`
- header register matches: `20 / 20`
- DSP register matches: `20 / 20`
- full APU RAM matches: `0 / 20`
- minimum normalized PCM correlation: `1.0`
- maximum alignment offset samples: `0`

## APU Region Matches

| Region | Matches |
| --- | ---: |
| `brr_sample_payloads` | 20 / 20 |
| `driver_and_overlay` | 0 / 20 |
| `full_apu_ram` | 0 / 20 |
| `runtime_tables_and_sequences` | 20 / 20 |

## Interpretation

- What this proves: The representative corpus has reference captures at the planned paths and every compared job meets the accepted oracle status set. Current ares-managed references produce byte-identical PCM with matching header/DSP state.
- Why not final: The current imported references are ares-managed near-oracle/backend-summary captures, not independent bsnes/Mesen/Mednafen captures, and the comparison scope is still representative tracks rather than every rendered track.
- Next step: Add an independent external-emulator capture path or promote the ares runner to all-track comparison, then rerun collect/validate/report.

## Tracks

| Track | Name | Status | Oracle | WAV Exact | Offset | Correlation | DSP Match | Full RAM Match |
| ---: | --- | --- | --- | --- | ---: | ---: | --- | --- |
| `001` | `GAS_STATION` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `002` | `NAMING_SCREEN` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `046` | `ONETT` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `056` | `SUMMERS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `072` | `GIYGAS_AWAKENS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `076` | `RUNAWAY5_CONCERT_1` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `082` | `BICYCLE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `083` | `SKY_RUNNER` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `092` | `COFFEE_BREAK` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `095` | `SMILES_AND_TEARS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `096` | `VS_CRANKY_LADY` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `100` | `VS_NEW_AGE_RETRO_HIPPIE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `105` | `POKEY_MEANS_BUSINESS` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `109` | `EXPLOSION` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `121` | `ONETT_INTRO` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `133` | `HIDDEN_SONG` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `157` | `ATTRACT_MODE` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `175` | `TITLE_SCREEN` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `185` | `GIYGAS_PHASE3` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
| `190` | `GIYGAS_DEATH` | `audio_equivalent_state_delta` | `ares_full_change_music_load_apply_reference` | yes | 0 | 1.0 | yes | no |
