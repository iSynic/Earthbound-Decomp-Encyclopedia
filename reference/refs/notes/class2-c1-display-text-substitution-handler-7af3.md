# Class2 C1 DisplayText Substitution Handler 7AF3

This note captures the current best local model for the `C1:7AF3` display-text handler that consumes the one-byte substitution slot at `$9D11`.

See also [class2-c1acf8-substitution-byte-family.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-c1acf8-substitution-byte-family.md).
See also [class2-battle-start-extra-message-state-4dbc-aa10.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battle-start-extra-message-state-4dbc-aa10.md).
See also [class2-battle-text-dispatch-stack.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battle-text-dispatch-stack.md).
See also [class2-cc19-1f-display-text-bridge.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-1f-display-text-bridge.md).

## Main result

`C1:7AF3` is now best understood as a display-text substitution-token loader inside the main `display_text` body in bank `C1`.

It is not the final renderer by itself. Instead, it reads the current one-byte battle-text substitution value from `$9D11`, zero-extends it, stages it through the shared display-text state helpers, and returns into the larger display-text pipeline.

That makes the role of `$9D11` more precise than before: it is not just a battle-side scratch byte, it is consumed by a real placeholder-style handler in the text engine.

## Why `C1:7AF3` belongs to the display-text engine

The `ebsrc` bank layout places the `C1:7Axx` region inside `text/display_text.asm`, after the text control-code trees and before the battle-text helper cluster at `C1:ACxx`.

So this is not battle controller logic pretending to be text. It is part of the local display engine.

## Local body of `C1:7AF3`

Local bytes decode cleanly:

- `JSR C1:AD02`
- `STA $06`
- `STZ $07`
- `STZ $08`
- `STZ $09`
- `REP #$20`
- `LDA $06`
- `STA $0E`
- `LDA $08`
- `STA $10`
- `JSR C1:045D`
- `BRA C1:7B51`

Mechanically, that means:

- read the low byte from `$9D11` through `C1:AD02`
- zero-extend it into a temporary 32-bit work area at `$06..$09`
- copy the low 16 bits into the display-text staging pair `$0E/$10`
- hand the staged value to `C1:045D`
- return to the shared display-text continuation

So `C1:7AF3` is a tiny source-loader, not a standalone printer.

## The selector is now pinned

A later local pass resolved the exact control-code selector that reaches this handler.

The dispatch chain around `C1:79F5..7A3A` now shows:

- `0x1E -> C1:7AE3`
- `0x1F -> C1:7AF3`
- `0x20 -> C1:7B0D`

So `C1:7AF3` is the concrete implementation behind text control code `0x19 0x1F`.

That matters directly for the present scripts, because they use:

- `0x19 0x1F`
- `0x1B 0x04`
- `0x1C 0x05 0x00`

which means they explicitly invoke the `$9D11` bridge before `PRINT_ITEM_NAME 0`.

## The sibling handlers matter

The nearby siblings make this interpretation much safer.

### `C1:7AE3`

This handler does:

- `JSR C1:AD26`
- copies the returned pointer into `$0E/$10`
- `JSR C1:045D`

That lines up perfectly with the known companion setter/getter family around `$9D12/$9D14`:

- `C1:AD0A` sets the pointer slot
- `C1:AD26` gets the pointer slot
- `C1:7AE3` consumes that pointer slot inside display-text

So `7AE3` and `7AF3` look like pointer-substitution and byte-substitution siblings in the same local text-engine family.

### `C1:7B0D`

This nearby handler loads a byte from `$98A4`, zero-extends it the same way, stages it into `$0E/$10`, and also calls `C1:045D`.

So the family is broader than battle-only state, but the mechanic is consistent: load some dynamic source value, normalize it, then hand it to the same display-text staging helper.

## What `C1:045D` appears to do

`C1:045D` does not look like the final text renderer.

The local body shows it writing the staged value into the active display-text state block returned by `C1:0301`, at offsets beyond the base pointer and saved window attributes.

So the safest current reading is:

- `C1:7AF3` and siblings choose or build a dynamic text source value
- `C1:045D` stores that value into the current display-text state
- later shared display-text logic renders it according to the selected placeholder/token type

## Nearby selector family at `C1:7B56`

The helper immediately after this region, `C1:7B56`, branches on small selector values `0..0B` and routes into a family of dynamic-source or rendering helpers.

Several of those cases also flow through `C1:045D` after loading their own source values.

That makes the local architecture much clearer:

- the `7AE3` / `7AF3` / `7B0D` cases are source loaders inside a shared substitution-token family
- the family itself is driven by a later selector, not by hardcoded battle-only text

## Why this sharpens the `$AA10` battle-start path

The later `C2` callers now connect directly to a concrete display-text handler shape.

At `C2:6003`:

- if `$AA10 != 0`, the code switches to 8-bit `A`
- loads `$AA10`
- calls `JSL C1:DD7C`
- stages `EF:7BDF` in `$0E/$10`
- calls `JSL C1:DC1C`

At `C2:8881`:

- if `$AA10 != 0`, the code switches to 8-bit `A`
- loads `$AA10`
- calls `JSL C1:DD7C`
- stages `EF:7DD5` in `$0E/$10`
- calls `JSL C1:DC1C`

Since `C1:DD7C` is just the far wrapper around `C1:ACF8`, those two battle-start message paths are definitely populating `$9D11` immediately before dispatching real battle text.

## Why `EF:7BDF` and `EF:7DD5` matter

The raw bytes at those `EF` addresses confirm that they are real battle-text scripts, not arbitrary data.

The clearest local anchor is `EF:7DD5`, which begins:

- `01`
- `70`
- `1C 0D`

Using the text macro crosswalk, that start is best read as:

- new-line control
- `@`-style formatting control
- `1C 0D` = `PRINT_ACTION_USER_NAME`

A later pass identified them exactly as `MSG_BTL_PRESENT` and `MSG_BTL_CHECK_PRESENT_GET`, and the script control flow now shows that the present-family messages explicitly invoke `0x19 0x1F` before `PRINT_ITEM_NAME 0`.

So the `$AA10 -> $9D11` path definitely feeds live battle-text script expansion rather than generic menu formatting or hidden state.

## Current safest interpretation

The safest interpretation is:

- `C1:7AF3` is the display-text handler that consumes the one-byte substitution slot at `$9D11`
- it is the concrete implementation behind text control code `0x19 0x1F`
- it is a source-loader in the local display-text engine, not the final renderer by itself
- `C1:7AE3` is the pointer-substitution sibling for `$9D12/$9D14`
- the `$AA10` UFO-present family populates `$9D11` immediately before dispatching concrete present-opening battle-text scripts
- therefore `$9D11` is best read as a real battle-text substitution slot used by at least one placeholder-style text-engine handler

## What is still open

The remaining open point is the semantic name.

I can now pin the exact control code, but I am still not naming `0x19 0x1F` with a fully confident symbolic name like `LOAD_ITEM_SUBSTITUTION` unless we see the same handler reused in enough non-UFO contexts to be sure it is not present-specific.

## Update: `C1:7B0D` is now bounded more tightly

A later pass tightened the neighboring byte-source sibling.

- `C1:7B0D` is the implementation behind `0x19 0x20`
- it reads its byte from `$98A4`
- and a text-segment scan currently finds only one `0x19 0x20` use, at `C9:1A91` in `ESHOP2`
- that script sits in the `MSG_SUB_GRFD_KINOKOGIRL` region and immediately enters a party-member / ailment scan using `CHARACTER_HAS_AILMENT 0x00, 0x02, 0x02`

So the current best read is that `7B0D` is still a generic loader mechanically, but its exposed script use is a narrow clinic-script helper rather than a broad battle-text source like `7AF3`.

See also [class2-cc19-20-eshop2-single-use.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-20-eshop2-single-use.md).

## Update: `0x19 0x20` now has a stronger overworld clue

A later pass tightened the only observed script use of `C1:7B0D`.

- the lone `0x19 0x20` text hit is still `C9:1A91` in `MSG_SUB_GRFD_KINOKOGIRL`
- that script now decodes more clearly as argument setup followed by a party-member mushroomized-ailment scan
- and one of the local `$98A4` writer or clear families sits in the same bank-`00` mushroomized-walking include region just before `C0:2D29`

So the current best read is that `7B0D` is still a generic loader mechanically, but the only exposed text use is very likely reading an overworld mushroomized-state byte rather than a battle-text source like `7AF3`.

See also [class2-cc19-20-eshop2-single-use.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-20-eshop2-single-use.md).


## Update: `$98A4` now looks index-like

A later bank-`00` pass tightened the strongest local writer at `C0:3318`.

That write is fed by a six-entry scan over `$986F + Y` and stores `TYA` into `$98A4` when the scan reaches the first `0` or `>= 5` entry. So the current best read is that `$98A4` is not a free-form flag; it is more likely a small selector or boundary index in the mushroomized-walking family.

That makes the `0x19 0x20` clinic-script use easier to understand as well, since the script saves and restores the loaded byte during a party-member / ailment scan rather than printing it directly.
