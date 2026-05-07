# Audio 0x00 Runtime Probe Results Summary

Status: no public export behavior changes; probe outputs are collected only when local ignored result files exist.

## Summary

- probe jobs: `19`
- result files found: `0`
- valid results: `0`
- statuses: `{'pending': 19}`
- validation: `{'invalid_or_pending': 19}`
- classifications: `{'pending': 19}`
- remaining blockers: `{'active_preview_classification': 7, 'ef_return_stack_model': 15, 'finite_transition_review': 10, 'loop_point_metadata': 2, 'zero_runtime_effect_proof': 19}`
- proven zero-effect tracks: `[]`
- sequence promotion allowed: `False`

## Acceptance Policy

- A result can resolve zero_runtime_effect_proof only when it validates and classifies 0x00 as true_end, ef_return, or loop_or_hold_continues.
- A result can resolve ef_return_stack_model only when it validates, includes EF stack observations, and has a resolved 0x00 classification.
- Loop-point metadata, finite/transition review, and active-preview classification remain separate post-proof blockers.
- This summary cannot directly promote public exact-duration exports.

## Results

| Track | Name | Status | Valid | 0x00 classification | Remaining blockers | Result path |
| ---: | --- | --- | --- | --- | --- | --- |
| `001` | `GAS_STATION` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'active_preview_classification']` | `build/audio/zero-runtime-probe/zero-probe-track-001-gas_station/zero-runtime-proof-result.json` |
| `174` | `GAS_STATION_2` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | `build/audio/zero-runtime-probe/zero-probe-track-174-gas_station_2/zero-runtime-proof-result.json` |
| `025` | `CHAOS_THEATRE` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'active_preview_classification']` | `build/audio/zero-runtime-probe/zero-probe-track-025-chaos_theatre/zero-runtime-proof-result.json` |
| `032` | `GIANT_STEP` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | `build/audio/zero-runtime-probe/zero-probe-track-032-giant_step/zero-runtime-proof-result.json` |
| `033` | `LILLIPUT_STEPS` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | `build/audio/zero-runtime-probe/zero-probe-track-033-lilliput_steps/zero-runtime-proof-result.json` |
| `034` | `MILKY_WELL` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | `build/audio/zero-runtime-probe/zero-probe-track-034-milky_well/zero-runtime-proof-result.json` |
| `035` | `RAINY_CIRCLE` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | `build/audio/zero-runtime-probe/zero-probe-track-035-rainy_circle/zero-runtime-proof-result.json` |
| `036` | `MAGNET_HILL` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | `build/audio/zero-runtime-probe/zero-probe-track-036-magnet_hill/zero-runtime-proof-result.json` |
| `037` | `PINK_CLOUD` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | `build/audio/zero-runtime-probe/zero-probe-track-037-pink_cloud/zero-runtime-proof-result.json` |
| `038` | `LUMINE_HALL` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | `build/audio/zero-runtime-probe/zero-probe-track-038-lumine_hall/zero-runtime-proof-result.json` |
| `039` | `FIRE_SPRING` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | `build/audio/zero-runtime-probe/zero-probe-track-039-fire_spring/zero-runtime-proof-result.json` |
| `085` | `BULLDOZER` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'active_preview_classification']` | `build/audio/zero-runtime-probe/zero-probe-track-085-bulldozer/zero-runtime-proof-result.json` |
| `094` | `GOOD_FRIENDS_BAD_FRIENDS` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'active_preview_classification']` | `build/audio/zero-runtime-probe/zero-probe-track-094-good_friends_bad_friends/zero-runtime-proof-result.json` |
| `120` | `HOTEL_OF_THE_LIVING_DEAD` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'active_preview_classification']` | `build/audio/zero-runtime-probe/zero-probe-track-120-hotel_of_the_living_dead/zero-runtime-proof-result.json` |
| `173` | `GOOD_MORNING_MOONSIDE` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'loop_point_metadata']` | `build/audio/zero-runtime-probe/zero-probe-track-173-good_morning_moonside/zero-runtime-proof-result.json` |
| `143` | `LEAVING_MAGICANT` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'active_preview_classification']` | `build/audio/zero-runtime-probe/zero-probe-track-143-leaving_magicant/zero-runtime-proof-result.json` |
| `157` | `ATTRACT_MODE` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'active_preview_classification']` | `build/audio/zero-runtime-probe/zero-probe-track-157-attract_mode/zero-runtime-proof-result.json` |
| `171` | `WINTERS_INTRO` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'loop_point_metadata']` | `build/audio/zero-runtime-probe/zero-probe-track-171-winters_intro/zero-runtime-proof-result.json` |
| `175` | `TITLE_SCREEN` | `pending` | `False` | `pending` | `['zero_runtime_effect_proof', 'ef_return_stack_model', 'finite_transition_review']` | `build/audio/zero-runtime-probe/zero-probe-track-175-title_screen/zero-runtime-proof-result.json` |

## Next Work

- run the zero probe jobs after the ares harness emits the widened trace contract
- review invalid or unresolved probe outputs before changing duration policy
- feed only validated true_end/ef_return/loop_or_hold_continues classifications back into triage
