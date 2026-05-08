# Interaction Result Consumers

This note captures the current ROM-first interpretation of the code that consumes the front-interaction result state in `$5D62`, `$5D64`, `$5DDC`, and `$5DDE/$5DE0`.

See also `notes/interaction-context-and-event-flags.md and `notes/class2-c2-handlers.md and `notes/class2-dispatch-family.md``` for the current structure-level model behind `C1:0301` and `$9C88`.

## High-level picture

The interaction probes in bank `C0` do not directly launch text or scripts.
Instead, bank `C1` contains selector logic that turns the probe result into an interaction-context structure plus a returned pointer-like value used by the checking-object flow.

The strongest current model is:

- bank `C0` resolves an interaction result code into `$5D62`
- `$5D64` carries the raw target identifier for ordinary front interactions
- special cached-door fallback data lives in `$5DDC/$5DDE/$5DE0`
- bank `C1` selectors normalize those values into a final output consumed by the checking-object pipeline

## Main consumer pair in bank `C1`

A narrow legacy cross-check shows two closely related consumers:

- `C1:3187` calls `C0:4452`, which is our main `Resolve_FrontInteractionTarget` path
- `C1:323B` calls `C0:4279`, which is the sibling `Resolve_InteractableAlongFacingTarget` path

Both routines interpret `$5D62` the same way at the top level:

- `0` -> no result
- `#$FFFF` -> invalid or blocked result
- `#$FFFE` -> use the cached fallback pointer from `$5DDE/$5DE0`
- anything else -> index a table rooted at `CF:8985`

That means the cached type-`6` door candidate is already a first-class interaction result by the time bank `C1` sees it.

## `CF:8985` result table

The consumers index `CF:8985` with `result * 17`, so the table is built from 17-byte records.

Working record layout from the observed access pattern:

- `+0`: result class byte
- `+6`: event-flag-like word stored to `$9C88` by the class-`2` path
- `+9`: returned pointer-like payload used by classes `1`, `2`, and `3`
- `+13`: auxiliary word consumed only by result class `2`

The returned payload is not yet proven to be a plain text pointer. The consumers treat it as structured output that eventually feeds `EB_ProcessTextboxData_Main`.

## Shared interaction-context helper at `C1:0301`

The class-`2` setup helpers both call `C1:0301` first.

Current best reading of `C1:0301`:

- it resolves a base pointer for the active interaction context structure
- if `$88E0 != #$FFFF`, it uses the current slot from `$88E4/$8958`
- otherwise it falls back through `C3:E4EF`
- in both cases it runs the chosen value through `C0:8FF7` and adds `#$8650`
- the returned address is then used as a structure base for later field writes

That makes `C1:0301` the strongest current candidate for "get current interaction/talk context record."

## Helper pair `C1:045D` and `C1:0489`

The raw bytes decode cleanly now:

- `C1:045D` writes the pointer in `$1C/$1E` into the structure returned by `C1:0301` at offset `+$17`, then mirrors that same pointer into `$14/$16`
- `C1:0489` does the same thing at offset `+$1B`

Working interpretation:

- class `2` seeds one or two pointer slots inside the active interaction context before returning its own output payload
- `C1:0489` is a companion/secondary pointer installer used only by the high-range branch of the class-`2` setup

## `C1:3187` primary selector

What the consumer code shows:

- Calls `C0:4452`
- If `$5D62` is `0` or `#$FFFF`, returns no output
- If `$5D62 == #$FFFE`, returns the cached pointer from `$5DDE/$5DE0`
- Otherwise indexes `CF:8985`
- If the record class byte at `+0` is `1`, it calls `C0:42C2` with `$5D64` and then returns the record payload at `+9`
- If the record class byte is `2` or `3`, it does not resolve an output in this path and falls through with the default null output

The important new clue is `C0:42C2`.

Current best reading of `C0:42C2`:

- treats `$5D64` as an actor-like target index
- maps the player-facing direction through the small table at `C3:E168`
- stores that result into `$2AF6,target`
- clears several per-target motion/state fields through `C0:9907`
- refreshes the target state through `C0:A48F`

Working interpretation:

- result class `1` is an actor-facing interaction class
- the raw front-probe result in `$5D64` looks like an interactable actor/object index, not a text id
- the primary selector is the "face the target, then return its interaction payload" path

## `C1:323B` secondary selector

What the consumer code shows:

- Calls `C0:4279`, the sibling facing-based interaction resolver
- Handles `0`, `#$FFFF`, and `#$FFFE` the same way as the primary selector
- Otherwise indexes the same `CF:8985` table
- If the record class byte is `1`, it returns no output in this path
- If the record class byte is `2`, it consumes the auxiliary word at `+13`
- For class `2`, values below `#$0100` go through `C1:045D`; values `>= #$0100` go through `C1:045D` and then `C1:0489` with the adjusted high-range value
- After the class-`2` setup, it stores the word at `+6` into `$9C88` and then returns the record payload at `+9`
- If the record class byte is `3`, it returns the record payload at `+9` directly

Working interpretation:

- result class `2` is an event-flag-aware two-state structured interaction class that prepares the active interaction context before returning its payload
- result class `3` is a more direct structured-output class with no extra setup beyond returning the payload
- `$9C88` now looks like an event-flag id for the class-`2` interaction flow

## Checking-object caller

The legacy entry `EB_HandlePlayerCheckingObject_Main` at `C1:3C32` makes the layering especially clear:

- it first calls the primary selector (`C1:3187` -> `C0:4452`)
- if that produced no output, it calls the secondary selector (`C1:323B` -> `C0:4279`)
- if both fail, it falls back to default text at `C7:C59E`
- then it passes the chosen output into `EB_ProcessTextboxData_Main`

Working interpretation:

- these selectors feed the player checking/talking pipeline
- the ordinary result path, the cached type-`6` door fallback, and the default fallback text all converge here

## Current best model

- `$5D62` is an interaction-result code, not just a movement-side scratch value
- `$5D64` is a raw actor/object-like target id used by class `1`
- `$5DDE/$5DE0` hold a cached fallback pointer for the special `#$FFFE` case
- `CF:8985` is a 17-byte interaction-result table with at least three behavior classes
- class `1` is now best understood as an actor-facing interaction path
- class `2` prepares one or two context pointers plus an event-flag id in `$9C88` before returning its payload
- bank `C2` can then refresh the raw target in `$5D64` into one of two local states through `C0:C30C`
- class `3` behaves like a direct structured-output class in the secondary selector

## Best next target

- Trace the higher-level C2 state family around `99DC`, and pair that with object-refresh helpers that consume `$2AF6`, so selector values `1/2` and target states `0/4` can be named from behavior instead of control flow.
