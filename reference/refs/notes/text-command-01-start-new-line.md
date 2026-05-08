# Text Command `0x01` as Start-New-Line Opcode

This note captures the current best local read of script byte `0x01`.

See also [text-command-02-end-block.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-02-end-block.md).
See also [text-command-03-halt-with-prompt.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-03-halt-with-prompt.md).

## Main result

`0x01` is the ordinary start-new-line opcode in the bank-`01` text engine.

The parser label is directionally right, but the runtime shape is slightly more specific than a blind "always insert a line break":

- `0x01` = `START_NEW_LINE`
- it first checks current live text/display state through `C1:04B5`
- if no active line/display context is present, it does nothing
- if active context is present, it calls shared worker `C4:38B1` to advance the text window to the next line state

So this is a real ordinary one-byte control opcode, not a family.

## Local parser proof

The ordinary top-level parser at `C1:890E` dispatches:

- `0x01 -> C1:8A0B`

The `0x01` leaf is tiny:

- `C1:8A0B`: `JSR C1:04B5 ; CMP #0 ; BNE C1:8A16 ; JMP C1:8754`
- `C1:8A16`: `JSL C4:38B1 ; JMP C1:8754`

So the local structure is explicit: test state, and only then perform the new-line worker call.

## Gating helper at `C1:04B5`

`C1:04B5` is a small current-text-context state reader.

The strongest local flow is:

- it reads current text-entry selector `$8958`
- if `$8958 == FFFF`, it returns `0`
- otherwise it resolves the active text/display object through `$88E4 -> C08FF7 -> $865E`
- then returns that state word

That is why `0x01` is slightly more conditional than the simple parser label suggests: it only runs the line-advance worker when a live text/display context is present.

## Worker behavior at `C4:38B1`

`C4:38B1` is the shared new-line or line-advance worker.

The strongest local anchors are:

- it resolves the live text/display object through `$8958 -> $88E4 -> C08FF7 -> $8650`
- it uses `C4:5E96` and a few line-position/counter fields in the current object
- it either increments the current line position/counter or calls `C4:37B8` when the current line capacity is exhausted
- it clears object field `+0x0E` before returning

So the safest local phrasing is: `C4:38B1` advances the current text window to a new line when that is possible, and rolls into the window's next display-line state when the current line is already full.

I am still keeping the exact user-facing display semantics of every internal counter field cautious, but the overall `START_NEW_LINE` interpretation is well supported.

## Script-side usage pattern

The exposed hits fit that model directly.

Typical neighborhoods look like:

- text
- `LINE_BREAK`
- `START_NEW_LINE`
- then more text or action on the next displayed line context

In many ordinary dialogs, repeated `START_NEW_LINE` opcodes appear where the script is clearly forcing the display cursor onto a fresh line before continuing.

## Relationship to nearby standalone control opcodes

The lower standalone control layer now looks much cleaner:

- `0x01` = start new line
- `0x02` = end block
- `0x03` = halt with prompt

Then below that comes the lower flag-control cluster and the small call/jump cluster.

## Confidence boundaries

### Locally proved

- `0x01` dispatches through `C1:8A0B`
- `C1:8A0B` calls `C1:04B5` and only proceeds when the returned value is nonzero
- on success it calls `C4:38B1`
- `0x01` has no subcommand family structure of its own

### Locally supported and strong

- `0x01` is best named `START_NEW_LINE`
- the opcode is display-state-sensitive rather than an unconditional raw line-break insert

### Still open

- the cleanest exact mapping of the line/capacity fields inside the current text/display object that `C4:38B1` manipulates
- how sharply `START_NEW_LINE` should be distinguished from ordinary `LINE_BREAK` in final user-facing terminology, since both affect visible line progression but at different layers of the window state machine

## Practical conclusion

Treat `0x01` as the ordinary `START_NEW_LINE` opcode, with the important refinement that it first checks whether a live text/display context is active before advancing the current window to the next line state.
