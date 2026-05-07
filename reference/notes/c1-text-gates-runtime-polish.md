# C1 Text Gates Runtime Polish

Status: first C1 text/menu-core polish slice after the battle-facing passes.

This note records byte-neutral source comments added after
`notes/c1-battle-psi-runtime-polish.md`. The slice focuses on the early C1
text-entry wrappers, wait-frame pump, window drain/focus helpers, prompt gates,
halt-control worker, text-state wait, and active text context resolver.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c1/c1_0004_process_textbox_data_from_caller_pointer.asm` | Restages caller-local text pointer `$20/$22` into the C1:86B1 text pointer ABI, brackets the run with C0 coordinate/state save/restore, and waits for `$B4A8 == FFFF`. |
| `src/c1/c1_004e_pump_text_wait_frame.asm` | Shared text wait-frame pump with queued window work, ordinary renderer/entity/input service, and battle text display mode routing through C4:3568. |
| `src/c1/c1_008e_close_and_drain_all_windows.asm` | Drains queued/current windows from `$88E2` under guard `$5E70`, then refreshes text/window state and clears drain side effects. |
| `src/c1/c1_00d6_wait_text_ticks.asm` | Counted wait helper that refreshes text state and pumps C1:2E42 until the incoming tick count expires. |
| `src/c1/c1_00fe_wait_for_text_prompt_or_input_gate.asm` | Shared prompt/input gate using `$006D & A0A0`, default ticks from `$964B`, and debug unlock chord `$8010` for `$9645`. |
| `src/c1/c1_0166_run_text_halt_control_worker.asm` | Shared halt-control worker for text commands 0x13/0x14, including prompt tile alternation and EF battle-text wait/finalize hooks. |
| `src/c1/c1_02d0_wait_for_text_state_flag9641.asm` | Wait-until-`$9641` gate using C1:004E frame pumping and debug skip chord handling. |
| `src/c1/c1_0301_get_active_interaction_context_record.asm` | Resolves the active `$8650` text/interaction descriptor or fallback `$85FE`, with neighbor snapshot/restore helpers for descriptor pointer/workmem slots. |

## Evidence Inputs

- `notes/text-engine-entry-waits-window-gates-c10000-c102d0.md`
- `notes/text-command-semantics-manifest.md`
- `notes/text-commands-13-and-14-halt-control.md`
- `notes/text-commands-11-and-12-menu-and-line-control.md`
- `notes/text-command-10-parameterized-pause.md`

## Runtime Contract

The early C1 strip is the service layer underneath many text command leaves. It
owns pointer staging, wait frames, focus state, input locks, and active
descriptor lookup; individual text commands mostly delegate into these helpers.

Key shared state:

- `$8958`: active window focus
- `$88E2`: queued/current window index for drain-all handling
- `$88E4`: focus-to-descriptor index table
- `$8650`: active text/interaction descriptor table
- `$9641`: text-state wait flag
- `$9645`: text input lock
- `$964B`: default prompt wait tick count
- `$964D`: blinking prompt or battle-text display state, depending on local lane
- `$B4A8`: text completion sentinel checked by the far text-entry wrapper

## Promotion Boundary

This slice promotes comments and local runtime wording only. It does not decode
the full C1:0A1D/C1:86B1 text executor, rename every `$8650` descriptor field,
or close all text command families. The important gain is that future opcode
notes can point to this shared machinery instead of restating low-level wait and
prompt behavior.

Open followups:

- polish `$89D4` text-entry record constructors and active-entry chain helpers
- carry this ABI wording into the text command family notes where command leaves
  already call C1:00D6, C1:00FE, C1:0166, or C1:02D0
- correlate `$964D` naming across blinking-prompt and battle-text mode callers

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C1 --module all --combined --scaffold src\c1\bank_c1_helpers_asar.asm --strict
```
