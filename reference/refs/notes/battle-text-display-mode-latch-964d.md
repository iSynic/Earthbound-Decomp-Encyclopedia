# Battle Text Display Mode Latch `$964D`

This note captures the current best local model for the tiny mode helpers at `C1:0036 / 003C / 0042` and their role in the battle-text-adjacent display wrappers.

See also [battle-text-entry-family-c1dc1c-dd7c.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-text-entry-family-c1dc1c-dd7c.md).
See also [battle-text-entry-tail-dd82-dd9f.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-text-entry-tail-dd82-dd9f.md).

## Main result

The `C1:0036 / 003C / 0042` trio is now locally straightforward:

- `C1:0036` stores `A` into `$964D`
- `C1:003C` clears `$964D`
- `C1:0042` reads `$964D`

So the safest current local name is:

- `$964D` = temporary battle-text-adjacent display-mode latch

I am intentionally keeping that name generic. The local mechanics are clear, but the exact user-facing meaning of each mode value is still not fully pinned.

## Locally proved mechanics

The helper bodies are tiny and direct:

- `C1:0036` -> `STA $964D`
- `C1:003C` -> `STZ $964D`
- `C1:0042` -> `LDA $964D`

That means the interesting question is not what the helpers do, but how callers use the latch.

## Strong local caller patterns

The currently strongest local patterns are:

- `C1:DD9F`
  - always sets mode `1` through `JSR $0036`
  - then dispatches one pointer through `C1:86B1`
  - then clears the latch through `JSR $003C`
  - in current local callers, this is the table-selected action-text path now described as `DISPLAY_CURRENT_ACTION_TABLE_TEXT_MODE1`
- `C1:DC1C`
  - conditionally sets mode `2` when `$9643 != 0`
  - then dispatches through `C1:86B1`
  - then clears the latch through `JSR $003C`
- `C1:D14F / D18B`
  - use modes `1` and `2` as two explicit stages around a battle-side item or stat message path
- `C1:CCFF`
  - also uses mode `2` before dispatching a hardcoded `EF` battle message

That makes the safest current summary:

- mode `1` and mode `2` are real transient display modes used by nearby battle-text and battle-message wrappers
- the reader side now shows they are not interchangeable
- the strongest current caller-side split is that `DD9F` callers like `C2:5C66` take over the manual `WINDOW_TICK / C2EACF` wait loop themselves after dispatch, which strengthens the promoted `DISPLAY_IN_BATTLE_TEXT_NO_PROMPT` match for `DD9F` even though the latch value itself still stops one step short of a fully proved user-facing label

## Reader-side behavioral split

The most useful local readers so far are `C1:0ADC..0B9F` and the close bank-`04` parallel at `C4:4D17..4DC8`.

In both places:

- if `$964D == 1`, execution jumps into a shorter write path (`0B8A` / `4DB8`)
- that path records only the simpler output fields and skips the fuller paired write or update sequence used by the ordinary path
- if `$964D == 2`, the same readers coerce the width-like field in `$16` to `0x20` and then continue through the ordinary path
- if `$964D == 0`, the ordinary path runs without either special case

That makes the safest current behavioral read:

- mode `1` = alternate reduced or abbreviated write path
- mode `2` = ordinary path with a forced normalized width-like value of `0x20`

## What the current evidence supports

The current local evidence supports these cautious statements:

- `C1:DD9F` is a one-pointer display wrapper that always forces display-mode `1`
- `C1:DC1C` is a one-pointer display wrapper that may force display-mode `2` under battle-state flag `$9643`
- `$964D` is not a long-lived global state block field; it behaves like a temporary per-dispatch mode latch
- the best local difference today is structural: abbreviated path for mode `1`, normalized ordinary path for mode `2`

## What is still open

- the exact user-facing presentation meaning of the abbreviated mode-`1` path
- whether mode `1` is truly promptless, less-interactive, or simply shorter-layout
- what user-facing property the forced `0x20` value represents in mode `2`
