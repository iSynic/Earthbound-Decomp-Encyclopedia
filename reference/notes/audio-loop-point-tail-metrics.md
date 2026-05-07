# Audio Loop Point Tail Metrics

Status: loop/held diagnostic tail metrics are frame-normalized; current loop-count/fade preview behavior remains unchanged.

## Summary

- records: `5`
- tail classifications: `{'active_through_diagnostic_render_boundary': 5}`
- diagnostic focus counts: `{'active_through_preview_or_loop_candidate': 4, 'general_playback_equivalence': 1}`
- primary sample packs: `{'5': 5}`
- active through diagnostic render boundary: `5`
- missing exact loop fields: `20`
- public exact loop export ready: `False`

## Unit Policy

- source nonzero index: `interleaved_pcm_sample_index`
- normalized nonzero index: `pcm_frame_32000hz`
- diagnostic render seconds: `30.0`
- public preview duration seconds: `120.0`

## Records

| Track | Name | Tail classification | Render seconds | Last nonzero frame | Silent frames at render end | Missing loop fields |
| ---: | --- | --- | ---: | ---: | ---: | --- |
| 005 | `YOU_WON1` | `active_through_diagnostic_render_boundary` | 30.0 | 959999 | 0 | `['intro_samples', 'loop_start_sample', 'loop_end_sample', 'measured_by']` |
| 006 | `LEVEL_UP` | `active_through_diagnostic_render_boundary` | 30.0 | 959999 | 0 | `['intro_samples', 'loop_start_sample', 'loop_end_sample', 'measured_by']` |
| 115 | `PHONE_CALL` | `active_through_diagnostic_render_boundary` | 30.0 | 959998 | 1 | `['intro_samples', 'loop_start_sample', 'loop_end_sample', 'measured_by']` |
| 183 | `SUDDEN_VICTORY` | `active_through_diagnostic_render_boundary` | 30.0 | 959999 | 0 | `['intro_samples', 'loop_start_sample', 'loop_end_sample', 'measured_by']` |
| 184 | `YOU_WON3` | `active_through_diagnostic_render_boundary` | 30.0 | 959999 | 0 | `['intro_samples', 'loop_start_sample', 'loop_end_sample', 'measured_by']` |

## Decision Policy

- This report measures diagnostic render tails only; it does not derive sample-accurate intro/start/end loop points.
- All source-render nonzero indexes are normalized from interleaved stereo sample indexes to 32 kHz PCM frames.
- Activity through the diagnostic render boundary supports loop/held prioritization but does not prove exact loop points.
- Public loop export remains loop-count-plus-fade preview until exact loop points or a held-policy classification are validated.

## Remaining Uncertainty

- All five loop/held candidates are active through the diagnostic render boundary.
- Exact loop metadata is still placeholder-only: intro, loop start, loop end, and measured_by remain missing for every track.
- The next runtime evidence needs to decide exact loop points versus held-policy/no-exact-loop classification.
