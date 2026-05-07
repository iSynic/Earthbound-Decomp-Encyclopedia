# Audio Finite Ending Tail Metrics

Status: finite-ending tail metrics are frame-normalized; current export behavior remains unchanged.

## Summary

- records: `5`
- tail classifications: `{'active_through_render_boundary': 3, 'post_candidate_tail_nonzero': 2}`
- diagnostic focus counts: `{'active_through_preview_or_loop_candidate': 2, 'finite_tail_or_transition_end': 2, 'general_playback_equivalence': 1}`
- nonzero after candidate end: `5`
- active through render boundary: `3`
- public exact finite export ready: `False`

## Unit Policy

- candidate end frame: `pcm_frame_32000hz`
- last nonzero frame: `interleaved source sample index divided by stereo channel count`
- render-boundary active tolerance: `4` frames

## Records

| Track | Name | Tail classification | Candidate end frame | Last nonzero frame | Tail frames | Tail seconds | Silent frames at render end |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 008 | `BATTLE_SWIRL1` | `post_candidate_tail_nonzero` | 129158 | 140984 | 11826 | 0.369563 | 819015 |
| 009 | `BATTLE_SWIRL2` | `active_through_render_boundary` | 131027 | 959997 | 828970 | 25.905313 | 2 |
| 011 | `NEW_FRIEND` | `active_through_render_boundary` | 253126 | 959999 | 706873 | 22.089781 | 0 |
| 123 | `SOMEONE_JOINS` | `post_candidate_tail_nonzero` | 83972 | 113116 | 29144 | 0.91075 | 846883 |
| 176 | `BATTLE_SWIRL4` | `active_through_render_boundary` | 170468 | 959999 | 789531 | 24.672844 | 0 |

## Decision Policy

- This report normalizes source-render sample indexes to 32 kHz PCM frames before comparing them to finite-end samples.
- Post-candidate PCM activity is diagnostic evidence only; it does not change export trimming or playback behavior.
- Tracks active through the render boundary need runtime/oracle state evidence before a true finite ending can be claimed.
- Tracks with shorter post-candidate tails still need transition/stinger versus true-release classification.

## Remaining Uncertainty

- `BATTLE_SWIRL2`, `NEW_FRIEND`, and `BATTLE_SWIRL4` are active through the diagnostic render boundary.
- `BATTLE_SWIRL1` and `SOMEONE_JOINS` have shorter nonzero post-candidate tails and still need true-release versus transition classification.
- No public exact finite duration can be promoted from this report alone.
