# Audio 0x00 Runtime Probe Plan

Status: targeted diagnostic jobs are planned; the runtime harness still needs the widened trace fields.

## Summary

- probe jobs: `19`
- unique tracks: `19`
- candidate packs: `10`
- source oracle jobs joined: `19`
- runtime 0x00 reads already observed: `5931`
- reader PC targets: `10`
- trace focus jobs: `{'prove_zero_effect_but_loop_points_remain_required': 2, 'prove_zero_effect_then_classify_active_preview': 5, 'prove_zero_end_effect_then_review_finite_candidate': 1, 'trace_zero_reader_with_ef_stack_state': 11}`
- post-zero-proof actions: `{'classify_active_preview_before_exact_export': 7, 'decode_loop_points_before_exact_export': 2, 'review_observed_silence_as_finite_or_transition': 10}`
- blockers: `{'ef_return_stack_model': 15, 'zero_runtime_effect_proof': 19}`
- sequence promotion allowed: `False`

## Probe Contract

- harness target: `tools/ares_audio_harness plus tools/run_audio_backend_batch.py external mode`
- behavior change allowed: `False`
- public exact promotion allowed: `False`
- required capture fields: `['sequence_read_trace', 'track_id', 'track_name', 'reader_pc', 'sequence_address', 'command', 'instruction', 'registers.ya', 'registers.x', 'registers.s', 'registers.p', 'command_pointer_registers.dp_10_11', 'command_pointer_registers.dp_12_13', 'ef_call_depth_before_zero', 'ef_return_target_before_zero', 'ef_call_depth_after_zero', 'post_zero_branch_or_effect', 'voice_slot_state', 'zero_effect_classification', 'classification_evidence']`
- source-effect capture requirements: `['$0230+x/$0231+x and $0240+x/$0241+x for active EF context', '$0230+x/$0231+x saved return pointer', '$30+x/$31+x before the zero read and after the post-zero branch', '$80+x before and after the zero read', '$80+x call count after EF', 'EF operands and resulting $0240+x/$0241+x subroutine target', 'capture $1B when the 0x80/0x81 pattern-control path is taken', 'capture the byte following pattern-level 0x00 before classifying StopMusic or fast-forward behavior', 'distinguish voice-stream zero reads from pattern-pointer 0x00 control pairs', 'later 0x00 branch result that consumes or restores this EF state', 'whether post-zero execution branches to L_081A, L_0AC4, L_0882, or restored-return flow']`
- accepted classifications: `['true_end', 'ef_return', 'loop_or_hold_continues', 'unreachable_from_source_state', 'unresolved']`
- independent oracle scope: This probe proves sequence-control semantics only; release-quality playback still depends on the independent emulator oracle plan.

## Reader PC Targets

| Reader PC | 0x00 reads | Driver offset | Role |
| --- | ---: | --- | --- |
| `0x2DB0` | 957 | `0x28B0` | `sequence_control_byte_reader_candidate` |
| `0x2DDA` | 955 | `0x28DA` | `sequence_control_byte_reader_candidate` |
| `0x2DF8` | 955 | `0x28F8` | `sequence_control_byte_reader_candidate` |
| `0x2E3D` | 952 | `0x293D` | `sequence_control_byte_reader_candidate` |
| `0x0957` | 114 | `0x0457` | `sequence_control_byte_reader_candidate` |
| `0x0B8A` | 84 | `0x068A` | `sequence_control_byte_reader_candidate` |
| `0x0847` | 73 | `0x0347` | `sequence_control_byte_reader_candidate` |
| `0x0782` | 8 | `0x0282` | `sequence_control_byte_reader_candidate` |
| `0x07A6` | 8 | `0x02A6` | `sequence_control_byte_reader_candidate` |
| `0x0D12` | 1 | `0x0812` | `sequence_control_byte_reader_candidate` |

## Jobs

| Track | Name | Pack | Focus | Post-proof action | Blockers | Output root |
| ---: | --- | ---: | --- | --- | --- | --- |
| `001` | `GAS_STATION` | `1` | `trace_zero_reader_with_ef_stack_state` | `classify_active_preview_before_exact_export` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-001-gas_station` |
| `174` | `GAS_STATION_2` | `1` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-174-gas_station_2` |
| `025` | `CHAOS_THEATRE` | `18` | `prove_zero_effect_then_classify_active_preview` | `classify_active_preview_before_exact_export` | `['zero_runtime_effect_proof']` | `build/audio/zero-runtime-probe/zero-probe-track-025-chaos_theatre` |
| `032` | `GIANT_STEP` | `25` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-032-giant_step` |
| `033` | `LILLIPUT_STEPS` | `25` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-033-lilliput_steps` |
| `034` | `MILKY_WELL` | `25` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-034-milky_well` |
| `035` | `RAINY_CIRCLE` | `25` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-035-rainy_circle` |
| `036` | `MAGNET_HILL` | `25` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-036-magnet_hill` |
| `037` | `PINK_CLOUD` | `25` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-037-pink_cloud` |
| `038` | `LUMINE_HALL` | `25` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-038-lumine_hall` |
| `039` | `FIRE_SPRING` | `25` | `trace_zero_reader_with_ef_stack_state` | `review_observed_silence_as_finite_or_transition` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-039-fire_spring` |
| `085` | `BULLDOZER` | `96` | `prove_zero_effect_then_classify_active_preview` | `classify_active_preview_before_exact_export` | `['zero_runtime_effect_proof']` | `build/audio/zero-runtime-probe/zero-probe-track-085-bulldozer` |
| `094` | `GOOD_FRIENDS_BAD_FRIENDS` | `107` | `prove_zero_effect_then_classify_active_preview` | `classify_active_preview_before_exact_export` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-094-good_friends_bad_friends` |
| `120` | `HOTEL_OF_THE_LIVING_DEAD` | `136` | `prove_zero_effect_but_loop_points_remain_required` | `classify_active_preview_before_exact_export` | `['zero_runtime_effect_proof']` | `build/audio/zero-runtime-probe/zero-probe-track-120-hotel_of_the_living_dead` |
| `173` | `GOOD_MORNING_MOONSIDE` | `136` | `prove_zero_effect_but_loop_points_remain_required` | `decode_loop_points_before_exact_export` | `['zero_runtime_effect_proof']` | `build/audio/zero-runtime-probe/zero-probe-track-173-good_morning_moonside` |
| `143` | `LEAVING_MAGICANT` | `148` | `prove_zero_effect_then_classify_active_preview` | `classify_active_preview_before_exact_export` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-143-leaving_magicant` |
| `157` | `ATTRACT_MODE` | `154` | `prove_zero_effect_then_classify_active_preview` | `classify_active_preview_before_exact_export` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-157-attract_mode` |
| `171` | `WINTERS_INTRO` | `160` | `trace_zero_reader_with_ef_stack_state` | `decode_loop_points_before_exact_export` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-171-winters_intro` |
| `175` | `TITLE_SCREEN` | `163` | `prove_zero_end_effect_then_review_finite_candidate` | `review_observed_silence_as_finite_or_transition` | `['zero_runtime_effect_proof', 'ef_return_stack_model']` | `build/audio/zero-runtime-probe/zero-probe-track-175-title_screen` |

## Promotion Policy

- This plan creates diagnostic jobs only and cannot promote public exact-duration exports.
- 0x00 true-end evidence must be joined with EF call/return state before finite-ending policy changes.
- Loop or held candidates still need loop-point metadata even when 0x00 behavior is understood.
- Independent emulator comparison remains a separate release gate.

## Next Work

- extend the ares audio harness trace contract to emit every required capture field
- run the 19 targeted zero-probe jobs into build/audio/zero-runtime-probe
- add a result collector/validator that feeds proven true_end or ef_return classifications back into duration triage
