# Text Command `1F C0` Jump-Multi2 Target Builder (`C1:621F`)

This note covers the reference unknown include `unknown/C1/C1621F.asm`, which sits immediately before `text/ccs/jump_multi2.asm` in bank `01`.

The external macro corroboration is unusually strong here:

```asm
.MACRO EBTEXT_JUMP_MULTI2 dest0, dest1, ...
    .BYTE $1F, $C0, .PARAMCOUNT
    .DWORD dest0
    .DWORD dest1
    ...
.ENDMACRO
```

## Main result

`C1:621F` is the deferred dword-target finalizer for `1F C0` / `JUMP_MULTI2`.

## Working Names

- `C1:621F` = `FinalizeTextCommand1FC0JumpMulti2Target`

It is a sibling of the older `C1:4103` 24-bit target builder, but this branch handles four-byte table entries and then skips the remaining unused entries in the `JUMP_MULTI2` operand block.

This range is now source-backed in `src/c1/c1_621f_finalize_text_command1_fc0_jump_multi2_target.asm`; the C1 scaffold validates byte-for-byte with this helper promoted.

## How `JUMP_MULTI2` reaches it

The visible `JUMP_MULTI2` body starts at `C1:6308`.

That routine takes:

- incoming `A` as the parser/current-pointer storage slot to rewrite
- incoming `X` as the destination count from the macro's `.PARAMCOUNT`
- the live selector from the active text context via `C1:040A`

If the selector is zero or outside the destination count, it advances the parser pointer by `count * 4`, effectively skipping the whole dword table.

If the selector is in range, it:

- computes `selector - 1`
- advances the parser pointer to the selected dword entry
- stores `count - selector` in `$97D5`
- clears `$97CA`
- returns callback low word `C1:621F`

That makes `$97D5` the number of four-byte destination entries still to skip after the selected target is consumed.

## `C1:621F` finalizer behavior

`C1:621F` gathers the selected dword target one byte at a time using the shared deferred byte queue:

- while `$97CA < 3`, append the current byte from `X` to `$97BA + $97CA`
- increment `$97CA`
- return `C1:621F` so the parser keeps feeding bytes

Once the queued bytes plus the current byte make a full dword target, it assembles:

- current byte shifted by 24
- `$97BC` shifted by 16
- `$97BB` shifted by 8
- `$97BA` as the low byte

The assembled value is placed in `$0E/$10` and passed to `C1:86B1`, the same core text-pointer processor reached by other text-entry paths.

After that, it uses `$97D5 * 4` to advance the parser/current-pointer slot past the unselected trailing destinations and returns zero.

## Relationship to the older target builders

This is not a general-purpose text helper.

It is the `JUMP_MULTI2` version of the existing queue-and-assemble control-flow machinery:

- `C1:4103` builds a three-byte target for ordinary `0x0A` / conditional branch-style control flow.
- `C1:621F` builds a four-byte table entry for `1F C0` / `JUMP_MULTI2`, then skips the remaining dword entries.

The repeated use of `$97BA/$97BB/$97BC/$97CA` is therefore intentional: it is the parser's small operand-byte queue, reused by several delayed target installers.

## Practical Conclusion

`C1:621F` is now locally covered as the hidden `JUMP_MULTI2` selected-target reader/finalizer. The unknown include boundary in `ebsrc-main` is explained by code shape and macro shape: it is shared support for the named `text/ccs/jump_multi2.asm` routine that follows it.

Source polish follow-up (2026-05-06): `src/c1/c1_621f_finalize_text_command1_fc0_jump_multi2_target.asm`
now names the shift, context-load, text-printer, and callback helper calls in
this finalizer directly, with C1 byte-equivalence still green.

Source polish follow-up (2026-05-06): the same source now names the deferred
argument queue itself. The selected-target collector reads as
`DeferredCommandByteQueue`, `DeferredCommandByte1/2`, and
`DeferredCommandQueueCount`, and its pending self-return uses
`TextCommand1FC0JumpMulti2FinalizerCallback` instead of the raw `$621F` low
word. `$97D5` is named as the remaining unselected destination count before the
final parser-pointer advance.
