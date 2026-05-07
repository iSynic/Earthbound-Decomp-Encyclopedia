# Nested Text Pointer + Callback Invoker Source Promotion (`C1:86B1..8B2C`)

This note records the promotion of two adjacent working-name byte corridors into decoded source modules:

- `C1:86B1..C1:87CC` `ExecuteNestedTextPointer`
- `C1:87CC..C1:8B2C` `InvokeTextEngineCallbackLowWord`

Both routines are already described semantically in earlier working-name notes:

- `C1:86B1` is the shared nested text-execution helper used by text command `0x08` (`CALL_TEXT`).
- `C1:87CC` is the bank-`01` callback step that invokes same-bank low-word handlers via an RTS-as-JSR stack trick.

See:

- [text-command-08-call-text.md](notes/text-command-08-call-text.md)
- [timed-event-callback-invoker-c187cc.md](notes/timed-event-callback-invoker-c187cc.md)

## Source modules

- `src/c1/c1_86b1_execute_nested_text_pointer.asm`
- `src/c1/c1_87cc_invoke_text_engine_callback_low_word.asm`

## Source polish follow-up

2026-05-06: both source modules now name their main execution edges directly.

- `C1:86B1` names the caller-side letter-box pointer advance helper, managed
  text-event slot front initializer at `C1:866D`, active-window parser preflight
  helper at `C4:45E1`, and the shared done target at `C1:8B2A`.
- `C1:87CC` names the line/scroll, line-state, halt-control, selection-menu,
  working-memory, active-line clear, glyph print, managed-slot apply, and
  name-entry pointer retreat helpers.
- The same source now names the compressed-bank pointer tables used by
  pseudo-opcodes `0x15..17` and the top-level callback roots for the low
  control strip plus structured families `0x18..1F`.

## Manifest intent

These two intervals are now treated as full `source` segments in the C1 build-candidate manifest so the scaffold emits assembled instructions instead of preserving the bytes as `db` data gaps.
