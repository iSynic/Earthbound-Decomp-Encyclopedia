# Audio Probe Campaign Plan

Status: unified zero/nonzero probe execution order is ready for external harness runs; no playback or export behavior changes.

## Summary

- campaign jobs: `26`
- lane jobs: `{'nonzero': 7, 'zero': 19}`
- phase jobs: `{'nonzero-0957-command-mix': 3, 'nonzero-reader-coverage': 4, 'zero-active-preview-followup': 6, 'zero-ef-return-stack': 11, 'zero-finite-transition-followup': 1, 'zero-loop-point-followup': 1}`
- command jobs: `{'0x00': 19, '0xEF': 3, '0xFD': 1, '0xFE': 2, '0xFF': 1}`
- first phase: `nonzero-0957-command-mix`
- first three jobs: `['nonzero-probe-ff-pc-0957', 'nonzero-probe-ef-pc-0957', 'nonzero-probe-fe-pc-0957']`
- accepted intake candidates: `0`
- sequence promotion allowed by campaign: `False`

## Execution Policy

- Run external harness jobs only against local user-supplied ROM-derived source artifacts.
- Generated result, trace, SPC, and WAV evidence must stay under ignored build/audio paths.
- Stub shape commands prove runner/result schemas only and never resolve semantic blockers.
- After any real harness run, validate the individual result, collect lane results, rebuild the intake plan, then rerun duration uncertainty validation.
- This campaign plan cannot directly promote sequence semantics or public exact-duration exports.

## Campaign Jobs

| Order | Phase | Lane | Job | Command | Reader PC | Score | Result path |
| ---: | --- | --- | --- | --- | --- | ---: | --- |
| 1 | `nonzero-0957-command-mix` | `nonzero` | `nonzero-probe-ff-pc-0957` | `0xFF` | `0x0957` | 11010 | `build/audio/nonzero-control-probe/nonzero-probe-ff-pc-0957/nonzero-control-proof-result.json` |
| 2 | `nonzero-0957-command-mix` | `nonzero` | `nonzero-probe-ef-pc-0957` | `0xEF` | `0x0957` | 10923 | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0957/nonzero-control-proof-result.json` |
| 3 | `nonzero-0957-command-mix` | `nonzero` | `nonzero-probe-fe-pc-0957` | `0xFE` | `0x0957` | 10904 | `build/audio/nonzero-control-probe/nonzero-probe-fe-pc-0957/nonzero-control-proof-result.json` |
| 4 | `nonzero-reader-coverage` | `nonzero` | `nonzero-probe-ef-pc-0b8a` | `0xEF` | `0x0B8A` | 10795 | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0b8a/nonzero-control-proof-result.json` |
| 5 | `nonzero-reader-coverage` | `nonzero` | `nonzero-probe-ef-pc-0d12` | `0xEF` | `0x0D12` | 10701 | `build/audio/nonzero-control-probe/nonzero-probe-ef-pc-0d12/nonzero-control-proof-result.json` |
| 6 | `nonzero-reader-coverage` | `nonzero` | `nonzero-probe-fd-pc-0847` | `0xFD` | `0x0847` | 10601 | `build/audio/nonzero-control-probe/nonzero-probe-fd-pc-0847/nonzero-control-proof-result.json` |
| 7 | `nonzero-reader-coverage` | `nonzero` | `nonzero-probe-fe-pc-0847` | `0xFE` | `0x0847` | 10601 | `build/audio/nonzero-control-probe/nonzero-probe-fe-pc-0847/nonzero-control-proof-result.json` |
| 8 | `zero-ef-return-stack` | `zero` | `zero-probe-track-174-gas_station_2` | `0x00` | `multi` | 5847 | `build/audio/zero-runtime-probe/zero-probe-track-174-gas_station_2/zero-runtime-proof-result.json` |
| 9 | `zero-ef-return-stack` | `zero` | `zero-probe-track-038-lumine_hall` | `0x00` | `multi` | 5841 | `build/audio/zero-runtime-probe/zero-probe-track-038-lumine_hall/zero-runtime-proof-result.json` |
| 10 | `zero-ef-return-stack` | `zero` | `zero-probe-track-032-giant_step` | `0x00` | `multi` | 5839 | `build/audio/zero-runtime-probe/zero-probe-track-032-giant_step/zero-runtime-proof-result.json` |
| 11 | `zero-ef-return-stack` | `zero` | `zero-probe-track-033-lilliput_steps` | `0x00` | `multi` | 5839 | `build/audio/zero-runtime-probe/zero-probe-track-033-lilliput_steps/zero-runtime-proof-result.json` |
| 12 | `zero-ef-return-stack` | `zero` | `zero-probe-track-034-milky_well` | `0x00` | `multi` | 5839 | `build/audio/zero-runtime-probe/zero-probe-track-034-milky_well/zero-runtime-proof-result.json` |
| 13 | `zero-ef-return-stack` | `zero` | `zero-probe-track-035-rainy_circle` | `0x00` | `multi` | 5839 | `build/audio/zero-runtime-probe/zero-probe-track-035-rainy_circle/zero-runtime-proof-result.json` |
| 14 | `zero-ef-return-stack` | `zero` | `zero-probe-track-036-magnet_hill` | `0x00` | `multi` | 5839 | `build/audio/zero-runtime-probe/zero-probe-track-036-magnet_hill/zero-runtime-proof-result.json` |
| 15 | `zero-ef-return-stack` | `zero` | `zero-probe-track-037-pink_cloud` | `0x00` | `multi` | 5839 | `build/audio/zero-runtime-probe/zero-probe-track-037-pink_cloud/zero-runtime-proof-result.json` |
| 16 | `zero-ef-return-stack` | `zero` | `zero-probe-track-039-fire_spring` | `0x00` | `multi` | 5839 | `build/audio/zero-runtime-probe/zero-probe-track-039-fire_spring/zero-runtime-proof-result.json` |
| 17 | `zero-ef-return-stack` | `zero` | `zero-probe-track-171-winters_intro` | `0x00` | `multi` | 5790 | `build/audio/zero-runtime-probe/zero-probe-track-171-winters_intro/zero-runtime-proof-result.json` |
| 18 | `zero-ef-return-stack` | `zero` | `zero-probe-track-001-gas_station` | `0x00` | `multi` | 5750 | `build/audio/zero-runtime-probe/zero-probe-track-001-gas_station/zero-runtime-proof-result.json` |
| 19 | `zero-finite-transition-followup` | `zero` | `zero-probe-track-175-title_screen` | `0x00` | `multi` | 5767 | `build/audio/zero-runtime-probe/zero-probe-track-175-title_screen/zero-runtime-proof-result.json` |
| 20 | `zero-loop-point-followup` | `zero` | `zero-probe-track-173-good_morning_moonside` | `0x00` | `multi` | 5210 | `build/audio/zero-runtime-probe/zero-probe-track-173-good_morning_moonside/zero-runtime-proof-result.json` |
| 21 | `zero-active-preview-followup` | `zero` | `zero-probe-track-094-good_friends_bad_friends` | `0x00` | `multi` | 5670 | `build/audio/zero-runtime-probe/zero-probe-track-094-good_friends_bad_friends/zero-runtime-proof-result.json` |
| 22 | `zero-active-preview-followup` | `zero` | `zero-probe-track-143-leaving_magicant` | `0x00` | `multi` | 5670 | `build/audio/zero-runtime-probe/zero-probe-track-143-leaving_magicant/zero-runtime-proof-result.json` |
| 23 | `zero-active-preview-followup` | `zero` | `zero-probe-track-157-attract_mode` | `0x00` | `multi` | 5670 | `build/audio/zero-runtime-probe/zero-probe-track-157-attract_mode/zero-runtime-proof-result.json` |
| 24 | `zero-active-preview-followup` | `zero` | `zero-probe-track-025-chaos_theatre` | `0x00` | `multi` | 5170 | `build/audio/zero-runtime-probe/zero-probe-track-025-chaos_theatre/zero-runtime-proof-result.json` |
| 25 | `zero-active-preview-followup` | `zero` | `zero-probe-track-085-bulldozer` | `0x00` | `multi` | 5170 | `build/audio/zero-runtime-probe/zero-probe-track-085-bulldozer/zero-runtime-proof-result.json` |
| 26 | `zero-active-preview-followup` | `zero` | `zero-probe-track-120-hotel_of_the_living_dead` | `0x00` | `multi` | 5170 | `build/audio/zero-runtime-probe/zero-probe-track-120-hotel_of_the_living_dead/zero-runtime-proof-result.json` |

## Post Run Validation

- `python tools/validate_audio_zero_runtime_probe_results_summary.py`
- `python tools/validate_audio_nonzero_control_probe_results_summary.py`
- `python tools/build_audio_sequence_semantics_intake_plan.py`
- `python tools/validate_audio_sequence_semantics_intake_plan.py`
- `python tools/validate_audio_duration_uncertainty_register.py`
- `python tools/validate_audio_sequence_command_semantics.py`
