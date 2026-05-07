# Audio Nonzero Control Probe Runner Contract

Status: ignored command/reader-PC job files can be generated for the future non-0x00 control probe harness.

## Summary

- jobs: `7`
- source candidates: `56`
- unique source tracks: `10`
- command jobs: `{'0xEF': 3, '0xFD': 1, '0xFE': 2, '0xFF': 1}`
- reader PC jobs: `{'0x0847': 2, '0x0957': 3, '0x0B8A': 1, '0x0D12': 1}`
- affected kind jobs: `{'return_stack_context': 3, 'static_walk_blocker': 1, 'timing_toggle_context': 3}`
- required capture fields: `21`
- sequence promotion allowed: `False`

## Runner

- job root: `build/audio/nonzero-control-probe-jobs`
- job index: `build/audio/nonzero-control-probe-jobs/nonzero-control-probe-jobs.json`
- command template: `['<nonzero-control-probe-harness>', '--job', '{job}', '--result', '{result}']`
- result validator: `python tools/validate_audio_nonzero_control_probe_result.py {result}`
- result collector: `python tools/collect_audio_nonzero_control_probe_results.py`

## Jobs

| Job | Command | Reader PC | Reads | Affected kind | Source candidates | Job path |
| --- | --- | --- | ---: | --- | ---: | --- |
| `nonzero-probe-ff-pc-0957` | `0xFF` | `0x0957` | 10 | `static_walk_blocker` | 8 | `build/audio/nonzero-control-probe-jobs/nonzero-probe-ff-pc-0957/job.json` |
| `nonzero-probe-ef-pc-0957` | `0xEF` | `0x0957` | 23 | `return_stack_context` | 8 | `build/audio/nonzero-control-probe-jobs/nonzero-probe-ef-pc-0957/job.json` |
| `nonzero-probe-fe-pc-0957` | `0xFE` | `0x0957` | 4 | `timing_toggle_context` | 8 | `build/audio/nonzero-control-probe-jobs/nonzero-probe-fe-pc-0957/job.json` |
| `nonzero-probe-ef-pc-0b8a` | `0xEF` | `0x0B8A` | 95 | `return_stack_context` | 8 | `build/audio/nonzero-control-probe-jobs/nonzero-probe-ef-pc-0b8a/job.json` |
| `nonzero-probe-ef-pc-0d12` | `0xEF` | `0x0D12` | 1 | `return_stack_context` | 8 | `build/audio/nonzero-control-probe-jobs/nonzero-probe-ef-pc-0d12/job.json` |
| `nonzero-probe-fd-pc-0847` | `0xFD` | `0x0847` | 1 | `timing_toggle_context` | 8 | `build/audio/nonzero-control-probe-jobs/nonzero-probe-fd-pc-0847/job.json` |
| `nonzero-probe-fe-pc-0847` | `0xFE` | `0x0847` | 1 | `timing_toggle_context` | 8 | `build/audio/nonzero-control-probe-jobs/nonzero-probe-fe-pc-0847/job.json` |

## Runner Policy

- Generated job files stay under ignored build/audio paths and may reference local ROM-derived SPC/WAV evidence.
- Each job targets one command and reader PC, then offers multiple source candidates for harness reachability.
- The harness must write one result JSON per job using earthbound-decomp.audio-nonzero-control-probe-result.v1.
- The runner contract cannot directly promote public exact-duration exports.
- Validated command effects must still be fed through audio-sequence-command-semantics before changing exact-duration policy.
