# Audio Residual Uncertainty Coverage Report

Status: residual duration uncertainty lanes are mapped; current playback/export behavior is preserved.

## Summary

- records: `8`
- primary uncertainty counts: `{'active_preview_classification_pending': 1, 'measurement_missing': 1, 'no_duration_uncertainty_for_current_export': 1, 'pcm_trim_usable_sequence_intent_open': 5}`
- export class counts: `{'finite_trim_candidate': 5, 'skip_no_audio': 1, 'unknown_active_preview': 1, 'unmeasured_or_missing': 1}`
- policy states: `{'public_exact_blocked': 2, 'public_exact_ready': 1, 'public_exact_ready_with_sequence_intent_open': 5}`
- public exact allowed: `6`
- public exact blocked: `2`
- PCM trim sequence-intent open: `5`

## Records

| Track | Name | Primary uncertainty | Export class | Policy state | Public exact | Recommended action |
| ---: | --- | --- | --- | --- | --- | --- |
| 000 | `NONE` | `measurement_missing` | `unmeasured_or_missing` | `public_exact_blocked` | `False` | measure_or_confirm_skip_policy_before_public_export |
| 004 | `NONE2` | `no_duration_uncertainty_for_current_export` | `skip_no_audio` | `public_exact_ready` | `True` | retain_ready_skip_no_audio_policy |
| 010 | `WHAT_THE_HECK` | `active_preview_classification_pending` | `unknown_active_preview` | `public_exact_blocked` | `False` | classify_active_preview_or_find_exact_end_before_public_exact_export |
| 012 | `YOU_WON2` | `pcm_trim_usable_sequence_intent_open` | `finite_trim_candidate` | `public_exact_ready_with_sequence_intent_open` | `True` | keep_public_pcm_trim_but_collect_sequence_intent_evidence_before_semantic_promotion |
| 013 | `TELEPORT_OUT` | `pcm_trim_usable_sequence_intent_open` | `finite_trim_candidate` | `public_exact_ready_with_sequence_intent_open` | `True` | keep_public_pcm_trim_but_collect_sequence_intent_evidence_before_semantic_promotion |
| 014 | `TELEPORT_FAIL` | `pcm_trim_usable_sequence_intent_open` | `finite_trim_candidate` | `public_exact_ready_with_sequence_intent_open` | `True` | keep_public_pcm_trim_but_collect_sequence_intent_evidence_before_semantic_promotion |
| 015 | `FALLING_UNDERGROUND` | `pcm_trim_usable_sequence_intent_open` | `finite_trim_candidate` | `public_exact_ready_with_sequence_intent_open` | `True` | keep_public_pcm_trim_but_collect_sequence_intent_evidence_before_semantic_promotion |
| 135 | `TELEPORT_IN` | `pcm_trim_usable_sequence_intent_open` | `finite_trim_candidate` | `public_exact_ready_with_sequence_intent_open` | `True` | keep_public_pcm_trim_but_collect_sequence_intent_evidence_before_semantic_promotion |

## Coverage Policy

- This report covers residual duration lanes not already owned by control, loop, finite-tail, or independent-oracle coverage reports.
- Public PCM-trim readiness is distinct from semantic sequence-intent promotion.
- Measurement-missing and active-preview residual tracks remain public-exact blockers.
- The no-audio skip track is recorded as ready and should not be treated as an audio duration blocker.

## Remaining Uncertainty

- `NONE` still needs measurement or explicit skip policy before public export.
- `WHAT_THE_HECK` still needs active-preview classification before public exact export.
- Five PCM-trim tracks are public-exact ready from PCM evidence but still need sequence-intent evidence before semantic promotion.
