# Service Script Pointer Table (`C5:8CF4`)

This note captures a useful but narrower-than-expected bridge that surfaced while tracing the delivery-script pointers from `D5:F645`.

## Core result

A raw pointer search found that some `D5:F645` script pointers are not unique to the delivery table.

In particular:

- `C6:42A3` appears at `D5:F663` and `C5:8CF4`
- `C6:3EB0` appears at `D5:F677` and `C5:8CF8`
- `C6:4BBF` appears at `D5:F64F` and `C5:8CFC`

So the delivery table is not the only holder of those service scripts.

## Important correction: this table lives in `EDEBUG`, not in mainline service flow

The bank map makes the local context much clearer.

Bank `05B` in `ebsrc` is laid out as:

- `EDEBUG`
- `ESHOP1`
- `EEVENT0`

And the `earthbound.yml` map places offset `0x0C88` in `EDEBUG` as `_DBG_SCRIPT`, with:

- `0x0D09` = `_DBG_SOUND`

That lines up with the local bytes perfectly:

- `C5:8CF0` decodes as a text-engine branch command (`JUMP_MULTI2 count=5`)
- `C5:8CF4` is the following 5-entry local pointer table
- the bytes after it flow straight into the debug-side sound/BGM/effect menu text

So `C5:8CF4` is **not** a mainline runtime selector table. It is a debug-script-local pointer list inside `EDEBUG::_DBG_SCRIPT`.

## Raw table shape at `C5:8CF4`

The local 20-byte table is five packed 24-bit pointers with zero separators:

- `C6:42A3`
- `C6:3EB0`
- `C6:4BBF`
- `C6:5243`
- `C6:55B1`

Raw bytes:

- `A3 42 C6 00`
- `B0 3E C6 00`
- `BF 4B C6 00`
- `43 52 C6 00`
- `B1 55 C6 00`

The full 20-byte pattern only occurs once in the ROM.

## What the pointed scripts look like

The first three entries are still the familiar delivery/service families:

- `C6:42A3` = ordinary Escargo Express delivery/payment script family
- `C6:3EB0` = alternate Escargo Express delivery/payment script family
- `C6:4BBF` = Mach Pizza delivery/payment script family

The last two entries broaden the debug menu rather than the delivery table:

- `C6:5243` is another service-style menu/script family
- `C6:55B1` is another service-style menu/script family with prompt gating

So the `_DBG_SCRIPT` table appears to be a debug-side service-script chooser that reuses several ordinary service flows as test targets.

## What this means for `D5:F645`

This is still a real bridge, but it is no longer a likely runtime bridge.

The safest combined reading is now:

- `D5:F645` = delivery-focused selector/config table
- `C5:8CF4` = debug-only local pointer list inside `EDEBUG::_DBG_SCRIPT`
- some Escargo/Mach Pizza script families are shared between the real delivery table and the debug script chooser

So this table confirms script-family reuse, but it does **not** explain how the mainline game chooses those delivery scripts at runtime.

## Best next target

- Return to the mainline side and trace how one `D5:F645` delivery record reaches its script-pointer pair without relying on the debug menu context.
