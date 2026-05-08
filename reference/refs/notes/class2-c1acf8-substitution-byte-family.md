# Class2 C1ACF8 Substitution Byte Family

This note captures the current best local model for `C1:ACF8`, `C1:AD02`, and the tiny wrapper `C1:DD7C`.

See also [class2-battle-text-dispatch-stack.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battle-text-dispatch-stack.md).
See also [class2-reflected-hit-text-context.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-reflected-hit-text-context.md).
See also [class2-battle-start-extra-message-state-4dbc-aa10.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battle-start-extra-message-state-4dbc-aa10.md).
See also [class2-c1-display-text-substitution-handler-7af3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-c1-display-text-substitution-handler-7af3.md).
See also [class2-ufo-present-message-family.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-ufo-present-message-family.md).

## Main result

`C1:ACF8` is now best understood as a tiny setter for a one-byte battle-text substitution slot at `$9D11`.

Its immediate companion `C1:AD02` is the matching getter, and `C1:DD7C` is a thin far wrapper around the setter.

That makes this family much more concrete than the older "argument-like helper" wording.

## Local bodies are extremely small

The local bytes make the core behavior unusually easy to trust.

### `C1:ACF8`

Local body:

- `REP #$31`
- `SEP #$20`
- `STA $9D11`
- `REP #$20`
- `RTS`

So the routine simply stores the low 8 bits of `A` into `$9D11`.

### `C1:AD02`

Local body:

- `REP #$31`
- `SEP #$20`
- `LDA $9D11`
- `REP #$20`
- `RTS`

So this is the matching getter for the same one-byte slot.

### `C1:DD7C`

Local body:

- `REP #$31`
- `JSR C1:ACF8`
- `RTL`

So `C1:DD7C` is not doing its own logic. It is just the far-call wrapper for the setter.

## What `$9D11` is probably for

The safest current reading is:

- `$9D11` is a one-byte battle-text substitution value
- it is used for small placeholder-like inserts such as action arguments, item ids, or special present-content substitutions

The key point is that it behaves like text context, not gameplay controller state.

## Why this interpretation is strong

The direct callers are very consistent.

Local direct callers of `C1:ACF8` include:

- `C1:B2F3`
- `C1:B40F`
- `C1:B893`
- `C1:D7C0`
- `C1:D823`
- `C1:D885`
- `C1:DD7E`

The caller shapes split into a few useful families:

- battle code that passes `battler::current_action_argument`
- battle code that passes dropped-item ids
- UFO/present message code that passes `$AA10`

That is a very good fit for a shared one-byte textbox substitution slot.

## The getter side fits the same model

The matching getter also has a nice confirming property: it has only one direct local caller.

- `C1:AD02` is only called directly from `C1:7AF3`

That caller sits inside a larger `C1:7Axx..7Bxx` display-text branch family rather than in battle controller logic. A later local pass tightened that relationship further:

- `C1:7AF3` reads `$9D11` through `C1:AD02`
- zero-extends the value into a temporary work area
- stages it into `$0E/$10`
- and hands it to the shared display-text helper `C1:045D`

So the stored byte is not just being written and forgotten; it is consumed by a real placeholder-style handler in the text engine.

See also [class2-c1-display-text-substitution-handler-7af3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-c1-display-text-substitution-handler-7af3.md).

## Reference-side support

The `ebsrc` reference does not yet give this helper a semantic name, but it does reinforce the same direction:

- the bank layout exports `C1ACF8` and its redirect wrapper separately from the display routines
- battle code in `main_battle_routine.asm`, `instant_win_handler.asm`, `psi_shield_nullify.asm`, `spy.asm`, and other files uses `REDIRECT_C1ACF8` immediately before battle-text display
- the values passed there include `current_action_argument` and `ITEM_DROPPED`

So both the local bytes and the reference call pattern point the same way.

## Why this helps the `$AA10` analysis

This family is the strongest current support for the newer UFO/present interpretation.

At `C2:6003` and `C2:8881`, the code:

- checks `$AA10`
- switches to 8-bit `A`
- loads `$AA10`
- calls `JSL C1:DD7C`
- then dispatches hardcoded `EF` battle-text pointers through `C1:DC1C`

Since `C1:DD7C` is just the far wrapper around `C1:ACF8`, that means `$AA10` is being copied directly into `$9D11` before those messages display.

A later local pass tightened that bridge further:

- `C2:6003` uses `EF:7BDF`, now identified as `MSG_BTL_PRESENT`
- `C2:8881` uses `EF:7DD5`, now identified as `MSG_BTL_CHECK_PRESENT_GET`
- `EF:7DD5` begins with battle-text control bytes including `1C 0D`, the `PRINT_ACTION_USER_NAME` control sequence in the text macro map

So `$AA10` is not just flowing into some abstract helper family. It is being staged into `$9D11` immediately before dispatch of concrete present-opening battle-text scripts.

That makes `$AA10` look much more like an item-like present-content substitution byte than like a plain gate or message id.

## Why this helps the reflected-hit rebuild analysis

This also tightens the older `C1` textbox-context story.

The reflected-hit rebuild family already pointed to:

- `C1:AC4A` / `C1:ACA1` as attacker and target name refresh helpers
- `C1:AD0A` as a companion pointer setter at `$9D12/$9D14`

Now `C1:ACF8` fits naturally into the same cluster:

- attacker name buffer
- target name buffer
- one-byte substitution slot at `$9D11`
- pointer substitution slot at `$9D12/$9D14`

So the `C1:DD70` / `C1:DD76` tail really does look like a battle-text context refresh family rather than mixed gameplay logic.

## Current safest interpretation

The safest interpretation is:

- `C1:ACF8` sets the current one-byte battle-text substitution value at `$9D11`
- `C1:AD02` reads that same value back inside the display-text engine
- `C1:DD7C` is just the far-call wrapper around the setter
- the value stored there can represent at least action arguments, item ids, and special present-content substitutions

## Best next target

The best next move is to pin the exact local selector or control-byte that chooses the `C1:7AF3` handler, or to give the companion pointer setter/getter family around `C1:AD0A` / `C1:AD26` the same level of confidence.

## Update: `$9D11` is generic, not item-only

A later scan of text-segment reuse tightened the meaning of this slot further.

`0x19 0x1F`, the display-text command that reaches `C1:7AF3`, appears not only in the UFO/present scripts but also in:

- `EGOODS0` item-use battle text before `PRINT_ITEM_NAME 0`
- `EBATTLE0`, `EBATTLE3`, and `EBATTLE5` PSI battle text before `PRINT_PSI_NAME 0`

So the strongest current read is not "item id slot" but:

- generic one-byte battle-text substitution slot

The caller decides what byte gets stored, and the later printer decides whether that byte is interpreted as an item id, PSI id, or some other small text argument.

See also [class2-cc19-1f-cross-segment-reuse.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-1f-cross-segment-reuse.md).
