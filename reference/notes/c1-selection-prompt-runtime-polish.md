# C1 Selection Prompt Runtime Polish

Status: third C1 text/menu-core polish slice.

This note records byte-neutral source comments added after
`notes/c1-text-entry-runtime-polish.md`. The slice focuses on the
selection-prompt support layer at C1:1F8A..242E and the conservative dispatch
boundary at C1:242E.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c1/c1_1f8a_clear_active_selection_prompt_scratch.asm` | Clears the active prompt descriptor scratch pointer at `$8687 + descriptor`. |
| `src/c1/c1_1fbc_read_selection_prompt_candidate_byte.asm` | Reads one candidate byte from `$AD5A` or `$AD6A` by list side and index. |
| `src/c1/c1_1fd4_is_selection_prompt_candidate_eligible.asm` | Filters candidates, with a special list/mode-1 path through D5:7B68 metadata and C2:FAD2 state. |
| `src/c1/c1_2012_find_next_selection_prompt_candidate.asm` | Scans the selected candidate list forward using `$AD56/$AD58` counts and C1:1FD4 eligibility. |
| `src/c1/c1_2070_find_previous_selection_prompt_candidate.asm` | Scans the selected candidate list backward using the same list/count/eligibility contract. |
| `src/c1/c1_20d6_refresh_selection_prompt_candidate_text.asm` | Refreshes candidate or fallback side text using `$AD7A/$AD82`, `$9FC9`, and C4 fallback labels. |
| `src/c1/c1_21b8_run_two_list_character_selection_prompt.asm` | Runs the full two-list prompt: side switching, forward/backward scan, accept, and cancellable exit. |
| `src/c1/c1_2362_run_simple_side_selection_prompt.asm` | Runs the simpler side-only prompt with C4 highlight setup/cleanup and C1:20D6 label refresh. |
| `src/c1/c1_242e_dispatch_character_selection_prompt_mode.asm` | Dispatches to simple side prompt for nonzero X or full two-list prompt for zero X; leaves C1:244C wording cautious. |

## Evidence Inputs

- `notes/character-selection-prompt-cluster-c11f8a-c1242e.md`
- `notes/character-selection-prompt-dispatch-c1242e-c12bf3.md`
- `notes/battle-targetting-resolver-c1adb4-af50.md`
- `notes/item-psi-name-display-and-target-prompt-c19216-c19437.md`

## Runtime Contract

The selection-prompt cluster owns two candidate lists:

- `$AD56`: primary candidate count
- `$AD58`: secondary candidate count
- `$AD5A+`: primary candidate bytes
- `$AD6A+`: secondary candidate bytes
- `$AD7A+`: primary battler/record ids used by display refresh
- `$AD82+`: secondary battler/record ids used by display refresh

The full prompt at C1:21B8 can switch between lists, scan forward/backward for
eligible candidates, accept with `$006D & 00A0`, or cancel with `$006D & A000`
when the incoming mode permits it. The simple prompt at C1:2362 only chooses a
side, using C4:3657/C4:35E4 to mark and clear highlighted target rows.

## Source Polish Follow-Up

2026-05-06: the first-half prompt strip now names the helper-call surface in
source. The forward/backward scanners call the `C1:1FD4` eligibility helper by
name; the candidate text refresher names `CREATE_WINDOW`, `PRINT_STRING`,
attacker-name-buffer staging, selected-target-name buffer setup, reflected-hit
article-token resolution, active cursor setup, HP/PP status tile lookup, and
glyph printing; the two-list and simple prompts name the candidate byte reader,
candidate scanners, refresh helper, enemy flashing on/off, row-highlight
setup/clear, text/input ticks, sound effects, and focus-window close helper.

## Promotion Boundary

This slice intentionally stops short of reinterpreting the deeper C1:244C core
and the exact producer-side names for `$AD5A/$AD6A/$AD7A/$AD82`. The controller
shape is now source-commented, while the final list vocabulary should come from
the routines that populate those lists.

2026-05-06 follow-up: the misleading raw absolute `JMP`/`JSR` renderings inside
the C1:244C mixed island were demoted to explicit `db` byte runs. This is still
the same byte stream, but raw edge scans no longer report false local helper
contracts for payload/control bytes that land inside unrelated instruction
streams.

2026-05-06 follow-up: caller-side prompt callback staging now uses explicit
ABI names. The C1:244C prompt core labels the `$0E/$10` display-callback
install before `C1:1F5A`, while open-menu, equipment, battle targetting, and
PSI callers stage their `C1:27EF` display and eligibility callbacks through
named `$0E/$10` and `$12/$14` pairs. This keeps the shared callback-driven
party selection helper readable from callers without overpromoting the mixed
C1:244C body.

Open followups:

- split and polish the C1:244C character-select prompt core once its mixed
  decode is easier to isolate
- correlate C4:3657/C4:35E4 highlight bytes with renderer-side consumers
- trace producers for `$AD5A/$AD6A/$AD7A/$AD82` before giving the two lists
  stronger side names

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C1 --module all --combined --scaffold src\c1\bank_c1_helpers_asar.asm --strict
```
