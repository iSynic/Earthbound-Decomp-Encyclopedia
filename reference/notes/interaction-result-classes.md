# Interaction Result Classes

This note pulls together the current ROM-first model for the result classes stored in the `CF:8985` interaction-result table.

## Current class split

- class `1`: actor-facing interaction path
- class `2`: event-flag-aware structured interaction path with extra context setup
- class `3`: direct structured-output path

## Class `1`

The primary selector at `C1:3187` is the only normal table-driven path that accepts class `1`.

Its sequence is:

- call `C0:4452` to resolve the front-interaction result
- use `$5D62` as a `CF:8985` record index
- call `C0:42C2` with raw probe result `$5D64`
- return the class record payload at `+9`

`C0:42C2` now decodes well enough to describe:

- it treats the input as an actor-like target index
- it maps player facing through `C3:E168`
- it stores the mapped facing into `$2AF6,target`
- it clears several motion/state fields through `C0:9907`
- it refreshes the target through `C0:A48F`

Working interpretation:

- class `1` is the talk-to / face-target interaction class

## Class `2`

The secondary selector at `C1:323B` is the main class-`2` consumer.

Its setup sequence is:

- resolve the current interaction context base through `C1:0301`
- consume the auxiliary word at record offset `+13`
- always call `C1:045D`, which writes `$1C/$1E` into context offset `+$17`
- if the auxiliary word is `>= #$0100`, also call `C1:0489`, which writes another pointer into context offset `+$1B`
- store record word `+6` into `$9C88` as an event-flag id
- return the record payload at `+9`

Working interpretation:

- class `2` prepares one or two context-specific pointers before the final interaction payload is consumed
- it also installs an event-flag id in `$9C88`, which ties it directly to the standard event-flag bitfield helpers in bank `C2`
- it likely represents a richer event-aware checking-object interaction than simple actor talk

## Class `3`

The secondary selector returns class `3` records directly:

- no `C1:045D`
- no `C1:0489`
- no `$9C88` setup
- just return the record payload at `+9`

Working interpretation:

- class `3` is the simplest non-actor structured interaction class currently visible in this pipeline

## Shared unresolved pieces

The main unresolved pieces are now narrower than before:

- what exact structure `C1:0301` returns
- what fields `+$17` and `+$1B` mean in gameplay/UI terms
- what subsystem consumes `$9C88`
- what exact data type the returned payload at `+9` represents before `EB_ProcessTextboxData_Main` sees it

## Best next target

- Trace the higher-level C2 state family around `99DC`, and pair that with object-refresh helpers that consume `$2AF6`, so selector values `1/2` and target states `0/4` can be named from behavior instead of control flow.
