# Class2 CC19 1F Display-Text Bridge

This note captures the now-pinned relationship between text control code `0x19 0x1F` and the one-byte substitution slot at `$9D11`.

See also [class2-c1-display-text-substitution-handler-7af3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-c1-display-text-substitution-handler-7af3.md).
See also [class2-ufo-present-message-family.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-ufo-present-message-family.md).
See also [class2-c1acf8-substitution-byte-family.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-c1acf8-substitution-byte-family.md).

## Main result

The open question about the exact display-text token is now resolved locally.

- script control code `0x19 0x1F` dispatches to `C1:7AF3`
- `C1:7AF3` reads `$9D11` through `C1:AD02`
- so `0x19 0x1F` is the concrete display-text bridge from the one-byte substitution slot into the text engine

That means the present scripts are not just "near" the `$9D11` path. They explicitly invoke it.

## Local dispatcher proof

The dispatch table in bank `C1` around `C1:79F5..7A3A` now decodes cleanly:

- `0x19` -> `C1:7AC7`
- `0x1A` -> `C1:7ACD`
- `0x1B` -> `C1:7AD3`
- `0x1C` -> `C1:7AD9`
- `0x1D` -> `C1:7ADE`
- `0x1E` -> `C1:7AE3`
- `0x1F` -> `C1:7AF3`
- `0x20` -> `C1:7B0D`
- `0x21` -> `C1:7B29`

So `0x19 0x1F` is not a loose guess from script context. It is a direct local branch target.

## Why this matters for the present scripts

Both UFO present scripts contain this sequence:

- `0x19 0x1F`
- `0x1B 0x04` -> `SWAP_WORKING_AND_ARG_MEMORY`
- some flavor text
- `0x1C 0x05 0x00` -> `PRINT_ITEM_NAME 0`

Now that `0x19 0x1F -> C1:7AF3` is pinned, the current best local read is:

1. battle code stores the selected present item in `$9D11` through `C1:DD7C -> C1:ACF8`
2. the script executes `0x19 0x1F`, which invokes the `$9D11` reader at `C1:7AF3`
3. the script swaps working and argument memory with `0x1B 0x04`
4. `PRINT_ITEM_NAME 0` prints the resulting item name from argument slot `0`

So the `$9D11 -> item name` bridge is no longer speculative.

## Sibling cases that help confirm it

The nearby siblings reinforce the pattern:

- `0x19 0x1E -> C1:7AE3`, the pointer-substitution sibling using `C1:AD26`
- `0x19 0x20 -> C1:7B0D`, another byte-source sibling from `$98A4`

So this is clearly a real family of text-source loaders, not a one-off battle special case.

## Current safest interpretation

The safest interpretation is:

- `0x19 0x1F` is the text command that loads the current `$9D11` one-byte substitution value into the display-text pipeline
- the UFO present scripts then move that loaded value into argument memory and print it through `PRINT_ITEM_NAME 0`
- therefore `$AA10 -> C1:DD7C -> $9D11 -> 0x19 0x1F -> PRINT_ITEM_NAME 0` is a real local end-to-end bridge

## Best next target

The best next move is to name `0x19 0x1F` semantically instead of numerically, or to see whether any non-battle scripts reuse it for other item-like substitution flows.

## Update: cross-segment reuse confirms the semantic name

A later local pass showed that `0x19 0x1F` is reused well beyond the UFO present family.

Representative hits now include:

- `EGOODS0` item-use battle text before `PRINT_ITEM_NAME 0`
- `EBATTLE8` present-family text before `PRINT_ITEM_NAME 0`
- `EBATTLE0`, `EBATTLE3`, and `EBATTLE5` PSI battle text before `PRINT_PSI_NAME 0`

So the safest semantic reading is now:

- `0x19 0x1F` = load the current one-byte substitution value from `$9D11` into the display-text pipeline

The printer that follows decides whether that byte is treated like an item id, a PSI id, or some other one-byte text argument.

See also [class2-cc19-1f-cross-segment-reuse.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-1f-cross-segment-reuse.md).
