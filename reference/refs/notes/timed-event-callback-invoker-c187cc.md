# Timed-Event Callback Invoker At `C1:87CC`

This note captures the local bank-`01` execution step that actually invokes callback-style low-word handlers such as `C1:7440`.

See also [timed-event-callback-family-bank01.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-event-callback-family-bank01.md).
See also [timed-event-slot-block-7440-and-c20abc.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-event-slot-block-7440-and-c20abc.md).
See also [timed-delivery-row-index-command-1f-d3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-row-index-command-1f-d3.md).

## Main result

The missing invocation path is now pinned locally.

At `C1:87CC`, if `$1E` is nonzero, the bank-`01` text engine performs a same-bank callback call through the low word currently held in `Y`.

The code does this with an RTS-as-JSR trick:

- `LDA $14`
- `TAX`
- `LDA $12`
- `STY $02`
- `STA $00C0`
- `PEA (return_addr - 1)`
- `LDA $02`
- `DEC`
- `PHA`
- `LDA $00C0`
- `RTS`

Because `RTS` pulls the manually pushed low word and return address from the stack, this effectively jumps to the same-bank routine whose low word was in `Y`.

## Why this closes the loop for `C1:7440`

`0x1F D3` resolves to low word `C1:7440`, and `C1:7440` is already locally pinned as a tiny adapter:

- `REP #$31`
- `TXA`
- `JSL EF:0EAD`
- `LDA #$0000`
- `RTS`

So the callback execution path is now concrete:

1. the text-command tree resolves a callback low word such as `7440`
2. the wider bank-`01` wrapper carries that low word in the callback state
3. `C1:87CC` invokes it with the RTS-as-JSR pattern
4. `C1:7440` receives the current `X` value, forwards it to `EF:0EAD`, and returns `0`

That is the first fully local execution bridge from the `0x1F D3` command family into the timed-delivery row-instantiation helper.

## Call interface visible at `C1:87CC`

The current visible calling convention at this bank-`01` callback step is:

- callback low word comes from `Y`
- `X` is loaded from `$14` before the call
- `A` is loaded from `$12` immediately before the call
- callback return value comes back in `A`
- on return, `C1:87E7` does `TAY` and stores the returned value back to `$1E`

The important new refinement is where `$14` comes from. In the immediately preceding callback-stream setup at `C1:87A7`, the engine:

- reads the current stream pointer from the structure addressed through `$12`
- loads the first byte at that stream pointer
- stores that byte to `$14`
- increments the stream pointer and writes it back

So for this callback family, `X` is not a slot id. It is the current one-byte callback argument fetched from the callback's own payload stream.

That makes the callback family look stateful rather than one-shot: the callback can return a next-state or continuation code in `A`, and the wrapper keeps it in `$1E` for the next pass.

## Best current interpretation

The safest current interpretation is that `$1E` in this bank-`01` text-engine path is the active same-bank callback low word, and `C1:87CC` is the execution step that dispatches it.

For the timed-delivery branch, the callback low word is `7440`, and the important argument is the one-byte callback payload fetched into `X` just before dispatch. `C1:7440` forwards that byte into `EF:0EAD`, which makes the current safest local read: the first payload byte after `0x1F D3` becomes the 1-based delivery row selector.
