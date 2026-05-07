# Character Selection Prompt Dispatch + Core (`C1:242E-C1:2BF3`)

This note follows the earlier selection-prompt cluster note and captures the
next contiguous corridor after `C1:242E` through the boundary at `C1:2BF3`.

## Source Promotion Status

- Promoted to decoded assembly source:
  - `src/c1/c1_242e_dispatch_character_selection_prompt_mode.asm` (`C1:242E..C1:2BF3`)
- Intended validation:
  - `python tools\\validate_source_bank_byte_equivalence.py --bank C1 --module all --combined --scaffold src\\c1\\bank_c1_helpers_asar.asm --strict`

## Entry Points

- `C1:242E` = `DispatchCharacterSelectionPromptMode`
  - Dispatch wrapper described in `notes/character-selection-prompt-cluster-c11f8a-c1242e.md`.
- `C1:244C` = `CharacterSelectPrompt`
  - Second entry point inside the same promoted corridor; this routine is a
    direct `JSR` target elsewhere in bank `C1`.

## High-level Behavior (Current Read)

- `C1:242E` selects between the two existing controllers:
  - if incoming `X != 0`, it calls `C1:2362` (`RunSimpleSideSelectionPrompt`)
  - if incoming `X == 0`, it calls `C1:21B8` (`RunTwoListCharacterSelectionPrompt`)
- `C1:244C` allocates a local direct-page stack frame, binds the active
  interaction-context record via `C1:0301`, and then drives the next stage of
  the character selection prompt flow (window/tile staging + prompt printing).

This corridor clearly continues the selection-prompt family, but the precise
semantic names for all internal subroutines remain intentionally conservative
until the callers at `C1:4666` / `C1:46A8` and the surrounding menu control flow
are documented.

## Source Polish Follow-Up (2026-05-06)

`src/c1/c1_242e_dispatch_character_selection_prompt_mode.asm` now carries the
same named helper-call surface as the preceding `C1:2012..242E` prompt strip.
The dispatch wrapper names the two prompt controllers directly:

- `C1:2362` = `RunSimpleSideSelectionPrompt`
- `C1:21B8` = `RunTwoListCharacterSelectionPrompt`

The `C1:244C` character-select core now names its evidence-backed local and
cross-bank joins: active interaction-context lookup, temporary text-event slot
snapshot/restore, window/context binding, character-name pointer resolution,
typed text-entry creation, active-chain refresh, selection-menu loop, prompt
callback install/clear, window close, HP/PP row focus/clear helpers, text/window
ticks, sound effects, delayed-action payload dispatch, text printing, pointer
offset resolution, VRAM transfer, and text-entry chain counting.

The remaining raw local absolute jumps and local calls at `C1:2227`, `C1:0285`,
`C1:AE4C`, and `C1:764C` are intentionally left as-is. They sit inside the
mixed internal decode for this corridor and need a separate structural split
before promotion.
