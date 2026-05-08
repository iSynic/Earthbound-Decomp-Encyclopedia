# Class2 Busy Helper EACF And Window Setup

This note captures the current ROM-first model for `C2:EACF`, the helper polled by `C2:40A4` before the bit-driven action payload loop begins.

See also `notes/class2-second-pointer-consumer-40a4.md`.
See also `notes/class2-descriptor-field-4e-and-d57b68.md`.

## Why this helper matters

`C2:40A4` begins by looping on `C2:EACF` until it returns zero.

Understanding that helper matters because it tells us whether the second `D5:7B68` pointer is immediately executable action data or whether it is gated behind a presentation or effect phase first.

## `C2:EACF` itself is just a tiny busy check

The local bytes at `C2:EACF` are simple.

Current safest reading:

- it checks byte-like state at `1B9E`
- if that value is nonzero, it returns `1`
- otherwise it checks byte-like state at `AEC2`
- if that value is nonzero, it returns `1`
- if both are zero, it returns `0`

So `EACF` is not the worker itself. It is a small "still busy?" predicate.

## The side reference confirms the wait-loop behavior

The `ebsrc` side reference strengthens that reading in a useful way.

In both battle main-routine code and `psi_thunder_common.asm`, the reference loops like this:

- tick the window system
- call `UNKNOWN_C2EACF`
- keep waiting while the helper returns nonzero

That matches the local `40A4` polling loop very well.

## What feeds the `AEC2` side of the busy state

The strongest local setup path is at `C2:EAAA`.

Current safest reading:

- it clears `AEC2`
- it clears pointer pair `AECC/AECE`
- it calls `C0:AE34` with value `3`
- it calls `C0:B047` with zeroed arguments

A nearby battle path does the same general pattern with a variable sourced from `AEC9`, then calls the same two `C0` helpers.

That strongly suggests `AEC2`, `AECC`, and `AECE` are the local control block for a staged presentation or effect process.

## The reference side shows how that control block advances

The legacy reference is especially helpful here.

Current safest reading from the traced `C4:A7C3+` region:

- when `AEC2` is zero, the update path exits early
- otherwise the path decrements `AEC2`
- when the countdown reaches zero, it reads a new byte count from the stream pointed to by `AECC/AECE`
- it then reads several words from that same stream into `AED0`, `AED2`, `AED4`, `AED6`, and `AED8`
- later branches either clear `AEC2/AECC/AECE` and finish, or refill `AEC2` and re-run the setup side through `C0:AE34` and `C0:B047`

That makes `AEC2` look like a step countdown for a pointer-driven effect script, with `AECC/AECE` holding the active stream pointer.

## The `AECC/AECE` stream now looks like a fixed-size effect record

The traced `C4:A7FD+` path is structured enough to describe the stream layout provisionally.

Current safest reading:

- at stream offset `+0x00`, the engine reads an 8-bit countdown and stores it to `AEC2`
- it then reads 16-bit words from offsets `+0x02` through `+0x14` into the working block `AED0`, `AED2`, `AED4`, `AED6`, `AED8`, `AEDA`, `AEDC`, `AEDE`, `AEE0`, and `AEE2`
- after loading those fields, it advances the stream pointer by `0x0016` bytes

That means the active stream record is best modeled as a 22-byte effect step:

- `+0x00`: step duration or countdown byte
- `+0x01`: still unresolved or unused by the traced path
- `+0x02..+0x08`: initial 16-bit state values copied into `AED0..AED6`
- `+0x0A..+0x14`: per-step 16-bit deltas copied into `AED8..AEE2`

The important behavioral point is that this does not look like variable-length script bytecode. It looks like a compact fixed-stride effect-step table.

## How the loaded fields are used each tick

The next `C4:A915+` block makes the loaded fields much more interpretable.

Current safest reading:

- `AED0` and `AED2` are incremented every tick by `AED8` and `AEDA`
- `AED4` and `AED6` are then updated toward zero using `AEDC` and `AEDE`, with clamping when the value would cross zero
- when both `AED4` and `AED6` reach zero, the current effect step ends and the control block is cleared
- otherwise the high bytes of `AED6` and `AED4` are extracted and passed, together with `AED0` and `AED2`, to `C0:B149`

That makes the state block look less like abstract scratch RAM and more like an animated window or mask effect with two position-like values and two size-or-radius-like values that shrink toward zero over time.

## Working interpretation of the stream format

The safest current interpretation is:

- `AECC/AECE` points at a table of fixed-size effect-step records
- each record seeds initial state and per-step deltas
- `AEC2` is the step duration countdown
- the `C4` update path integrates those values each frame and programs SNES window-mask state through `C0:B149`, `C0:B0EF`, and `C0:B047`

So the busy state behind `C2:EACF` now looks specifically like a staged window or masking animation record stream, not just a generic presentation queue.

## `C0:AE34` and `C0:B047` look like window-mask setup helpers

The two `C0` helpers being called before the busy loop now have a usable shape.

Current safest reading:

- `C0:AE34` masks bits in local state byte `$001F` through a small eight-entry mask table `FE, FD, FB, F7, EF, DF, BF, 7F`
- `C0:B047` writes directly to SNES window-mask registers for BG layers, objects, and main/sub-screen window masks

That makes the setup side look much more like a screen-window or masking effect initializer than a generic battle-state helper.

## Working interpretation

Putting the pieces together, the safest current interpretation is:

- the second `D5:7B68` pointer reaches `C2:40A4`
- `40A4` waits for any currently running window or effect script to finish by polling `C2:EACF`
- the busy state behind `EACF` is at least partly driven by `AEC2` and the `AECC/AECE` script pointer pair
- the setup side programs SNES window-mask registers through `C0:AE34` and `C0:B047`
- once that presentation or masking phase is clear, `40A4` begins its bit-driven action application loop

That makes the second pointer family feel even more battle-oriented: not just action logic, but action logic coordinated with a staged screen or masking effect.

## What is still unresolved

Still open:

- the precise role of `1B9E` relative to the `AEC2` effect countdown
- the exact meaning of the unresolved byte at stream offset `+0x01`, and the precise gameplay names for the loaded words in `AED0..AEE2`
- whether all `C2:40A4` payloads rely on the same window-mask effect machinery or only some families do
- how the bit-driven dispatch loop in `40A4` synchronizes with the separate `AEC2`-driven countdown path

## Current safest takeaway

The safest current takeaway is:

- `C2:EACF` is a tiny busy predicate, not the worker itself
- the real busy state is tied to an `AEC2` countdown and an `AECC/AECE` stream pointer pair
- the setup helpers `C0:AE34` and `C0:B047` look like SNES window-mask configuration helpers
- the second `D5:7B68` pointer therefore appears to drive battle-action payloads that are coordinated with a window or masking presentation effect

That is a much stronger gameplay-facing statement than the earlier "companion action pointer" model.

## Best next target

- map a few concrete `D5:7B68` entries to named battle actions in the side reference, or tighten what `C0:B149` is doing with the `AED0/AED2/AED4/AED6` state tuple, so the effect-step table can be described with less hedging.
