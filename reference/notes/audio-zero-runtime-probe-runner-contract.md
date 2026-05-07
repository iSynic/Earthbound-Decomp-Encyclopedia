# Audio 0x00 Runtime Probe Runner Contract

Status: ignored per-track job files can be generated for the future zero-probe harness.

## Summary

- jobs: `19`
- unique tracks: `19`
- trace focus jobs: `{'prove_zero_effect_but_loop_points_remain_required': 2, 'prove_zero_effect_then_classify_active_preview': 5, 'prove_zero_end_effect_then_review_finite_candidate': 1, 'trace_zero_reader_with_ef_stack_state': 11}`
- pack context jobs: `{'needs_ef_return_stack_model': 11, 'zero_phrase_end_candidate_runtime_pending': 8}`
- reader PC targets per job: `10`
- required capture fields: `20`
- sequence promotion allowed: `False`

## Runner

- job root: `build/audio/zero-runtime-probe-jobs`
- job index: `build/audio/zero-runtime-probe-jobs/zero-runtime-probe-jobs.json`
- command template: `['<zero-probe-harness>', '--job', '{job}', '--result', '{result}']`
- result validator: `python tools/validate_audio_zero_runtime_probe_result.py {result}`
- result collector: `python tools/collect_audio_zero_runtime_probe_results.py`

## Jobs

| Track | Name | Focus | Job path | Result path |
| ---: | --- | --- | --- | --- |
| `001` | `GAS_STATION` | `trace_zero_reader_with_ef_stack_state` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-001-gas_station/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-001-gas_station/zero-runtime-proof-result.json` |
| `174` | `GAS_STATION_2` | `trace_zero_reader_with_ef_stack_state` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-174-gas_station_2/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-174-gas_station_2/zero-runtime-proof-result.json` |
| `025` | `CHAOS_THEATRE` | `prove_zero_effect_then_classify_active_preview` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-025-chaos_theatre/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-025-chaos_theatre/zero-runtime-proof-result.json` |
| `032` | `GIANT_STEP` | `trace_zero_reader_with_ef_stack_state` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-032-giant_step/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-032-giant_step/zero-runtime-proof-result.json` |
| `033` | `LILLIPUT_STEPS` | `trace_zero_reader_with_ef_stack_state` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-033-lilliput_steps/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-033-lilliput_steps/zero-runtime-proof-result.json` |
| `034` | `MILKY_WELL` | `trace_zero_reader_with_ef_stack_state` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-034-milky_well/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-034-milky_well/zero-runtime-proof-result.json` |
| `035` | `RAINY_CIRCLE` | `trace_zero_reader_with_ef_stack_state` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-035-rainy_circle/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-035-rainy_circle/zero-runtime-proof-result.json` |
| `036` | `MAGNET_HILL` | `trace_zero_reader_with_ef_stack_state` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-036-magnet_hill/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-036-magnet_hill/zero-runtime-proof-result.json` |
| `037` | `PINK_CLOUD` | `trace_zero_reader_with_ef_stack_state` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-037-pink_cloud/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-037-pink_cloud/zero-runtime-proof-result.json` |
| `038` | `LUMINE_HALL` | `trace_zero_reader_with_ef_stack_state` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-038-lumine_hall/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-038-lumine_hall/zero-runtime-proof-result.json` |
| `039` | `FIRE_SPRING` | `trace_zero_reader_with_ef_stack_state` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-039-fire_spring/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-039-fire_spring/zero-runtime-proof-result.json` |
| `085` | `BULLDOZER` | `prove_zero_effect_then_classify_active_preview` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-085-bulldozer/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-085-bulldozer/zero-runtime-proof-result.json` |
| `094` | `GOOD_FRIENDS_BAD_FRIENDS` | `prove_zero_effect_then_classify_active_preview` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-094-good_friends_bad_friends/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-094-good_friends_bad_friends/zero-runtime-proof-result.json` |
| `120` | `HOTEL_OF_THE_LIVING_DEAD` | `prove_zero_effect_but_loop_points_remain_required` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-120-hotel_of_the_living_dead/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-120-hotel_of_the_living_dead/zero-runtime-proof-result.json` |
| `173` | `GOOD_MORNING_MOONSIDE` | `prove_zero_effect_but_loop_points_remain_required` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-173-good_morning_moonside/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-173-good_morning_moonside/zero-runtime-proof-result.json` |
| `143` | `LEAVING_MAGICANT` | `prove_zero_effect_then_classify_active_preview` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-143-leaving_magicant/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-143-leaving_magicant/zero-runtime-proof-result.json` |
| `157` | `ATTRACT_MODE` | `prove_zero_effect_then_classify_active_preview` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-157-attract_mode/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-157-attract_mode/zero-runtime-proof-result.json` |
| `171` | `WINTERS_INTRO` | `trace_zero_reader_with_ef_stack_state` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-171-winters_intro/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-171-winters_intro/zero-runtime-proof-result.json` |
| `175` | `TITLE_SCREEN` | `prove_zero_end_effect_then_review_finite_candidate` | `build/audio/zero-runtime-probe-jobs/zero-probe-track-175-title_screen/job.json` | `build/audio/zero-runtime-probe/zero-probe-track-175-title_screen/zero-runtime-proof-result.json` |

## Runner Policy

- Generated job files stay under ignored build/audio paths and may reference local ROM-derived SPC/WAV evidence.
- The harness must write one result JSON per job using earthbound-decomp.audio-zero-runtime-probe-result.v1.
- The runner contract cannot directly promote public exact-duration exports.
- Run collect_audio_zero_runtime_probe_results.py after harness execution to summarize remaining uncertainty.
