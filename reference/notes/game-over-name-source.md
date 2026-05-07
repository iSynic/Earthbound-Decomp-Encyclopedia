# Game Over Name Source

The game-over retry prompt is `MSG_SYS_COMEBACK` at `C7:DE7D`.

Readable/decompiler-style form of the start of the same script:

```js
// $C7DE7D
L_C7DE7D:
    call(L_C7DE11)
    call(SUB_CancelTimedEvents)
    window_open(1)
    call(L_C7DFA4)
    "•{name(argument)}!" next
    "•It looks like you got your head handed to you." next
```

The first line is:

```asm
C7DE8F: 70              EBTEXT "@"
C7DE90: 1C 02 00        EBTEXT_PRINT_CHAR_NAME $00
C7DE93: 51              EBTEXT "!"
```

`EBTEXT_PRINT_CHAR_NAME arg` encodes as:

```asm
.BYTE $1C, $02, arg
```

The `arg = $00` case is special in the handler `CC_1C_02`: it calls `GET_ARGUMENT_MEMORY` and prints the current text argument. In the main game-over path that usually resolves to Ness's name, but the message calls `_SUB_Q_NESSJEFF` first:

```asm
C7DE8A: 08 A4 DF C7     EBTEXT_CALL_TEXT _SUB_Q_NESSJEFF
...
C7DFA4:             _SUB_Q_NESSJEFF:
C7DFA4: 06 0E 00 B9 DF C7 00  EBTEXT_JUMP_IF_FLAG_SET _NESSJEFF_NESS, EVENT_FLAG::FLG_JEFF
C7DFAB: 07 80 00              EBTEXT_CHECK_EVENT_FLAG EVENT_FLAG::FLG_WINS_START
C7DFAE: 1B 02 B9 DF C7 00     EBTEXT_JUMP_IF_FALSE _NESSJEFF_NESS
C7DFB4: 0E 03                 EBTEXT_STORE_TO_ARGMEM $03
C7DFB6: 0D 01                 EBTEXT_COPY_TO_ARGMEM $01
C7DFB8: 02                    EBTEXT_END_BLOCK
C7DFB9:             _NESSJEFF_NESS:
C7DFB9: 0E 01                 EBTEXT_STORE_TO_ARGMEM $01
C7DFBB: 0D 01                 EBTEXT_COPY_TO_ARGMEM $01
C7DFBD: 02                    EBTEXT_END_BLOCK
```

So vanilla already has a Ness/Jeff switch for this prompt. The later yes/no branch text also prints the same current argument:

Interpretation: vanilla chooses Jeff during the solo Winters segment. `_SUB_Q_NESSJEFF` prints Ness if `FLG_JEFF` is already set, and also prints Ness if `FLG_WINS_START` is not set. The only path that stores `$03` is:

- `FLG_WINS_START` set
- `FLG_JEFF` clear

That matches "Jeff has started Winters, but has not joined the main party yet." Once Jeff joins Ness and Paula, `FLG_JEFF` is set and the game-over prompt falls back to Ness.

Equivalent readable/decompiler-style form:

```js
// $C7DFA4
L_C7DFA4:
    goto_ifset(JEFF_JOINS, L_C7DFB9)
    isset(JEFF_STARTS_HIS_JOURNEY)
    goto_false(L_C7DFB9)
    counter(3)
    ctoarg
    eob

// $C7DFB9
L_C7DFB9:
    counter(1)
    ctoarg
    eob
```

Here `JEFF_JOINS` corresponds to `FLG_JEFF`, and
`JEFF_STARTS_HIS_JOURNEY` corresponds to `FLG_WINS_START`.
`counter(3); ctoarg` is the readable form of storing/copying character ID
`$03` to argument memory; the `$01` branch stores Ness.

An alternate hack can replace the helper itself:

```js
ROM[0xC7DFA4] = {
    get_char_at_pos(1)
    rtoarg
    eob
}
```

That is not the same as hardcoding Jeff. It changes the helper from
"Ness unless the vanilla Jeff-Winters flags say Jeff" to "use the character in
party position 1," assuming this command returns the same 1-based character IDs
expected by `{name(argument)}`. Because the game-over text calls this helper once
and then uses `{name(argument)}` later, this replacement should affect all
name prints in that comeback prompt consistently.

```asm
C7DF3D: 1C 02 00        EBTEXT_PRINT_CHAR_NAME $00 ; "{name} decided..."
C7DF99: 1C 02 00        EBTEXT_PRINT_CHAR_NAME $00 ; "See you, {name}!"
```

For literal party character names, the script-visible IDs are:

- `$01` = Ness
- `$02` = Paula
- `$03` = Jeff
- `$04` = Poo

So a simple hardcoded Jeff hack for only the first visible "{name}!" line would change:

```hex
1C 02 00
```

to:

```hex
1C 02 03
```

at the game-over message's print-name command, i.e. change the argument byte at `C7:DE92` from `$00` to `$03`.

That should only affect the displayed name in that one line. It bypasses the `_SUB_Q_NESSJEFF` argument for that print only; the later comeback branch lines will still use `$00` and therefore still follow the vanilla Ness/Jeff argument unless patched too.

To force Jeff consistently in this whole prompt, patch all three `PRINT_CHAR_NAME $00` instances in `MSG_SYS_COMEBACK`:

- `C7:DE92` from `$00` to `$03` for the opening "{name}!"
- `C7:DF3F` from `$00` to `$03` for "{name} decided..."
- `C7:DF9B` from `$00` to `$03` for "See you, {name}!"

SNES Game Genie encodings:

| Effect | Raw patch | Game Genie |
| --- | --- | --- |
| Opening "{name}!" only | `C7DE92:03` | `D72B-8DBE` |
| "{name} decided..." | `C7DF3F:03` | `D727-E72E` |
| "See you, {name}!" | `C7DF9B:03` | `D72B-E42E` |

The rest of the comeback/game-over flow is driven by the surrounding routine in bank `C4`, especially `UNKNOWN_C4C64D`, which displays `MSG_SYS_COMEBACK`.
