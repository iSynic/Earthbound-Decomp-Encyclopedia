# Overworld Position Context Byte (`C1:AD7D`)

This note covers the small unknown start `C1:AD7D`.

See also [text-command-family-1d-inventory-money.md](notes/text-command-family-1d-inventory-money.md) for another bank-`01` use of `C0:0AA1`, and [battle-targetting-resolver-c1adb4-af50.md](notes/battle-targetting-resolver-c1adb4-af50.md) for the neighboring resolver that follows this helper.

## Main Result

`C1:AD7D` is a compact current-overworld-position context reader.

Source-scaffold promotion:

- `src/c1/c1_ad7d_read_overworld_position_context_byte.asm` now assembles as
  a source segment in `build/c1-build-candidate-ranges.json`.
- Validation remains clean: `C1 byte-equivalence: OK, 172 module(s), 0
  mismatch(es).`

## Working Names

- `C1:AD7D` = `ReadOverworldPositionContextByte`

It:

1. loads current position words from `$9877/$987B`
2. calls `C0:0AA1`
3. keeps the returned word in a local
4. checks event flag `0x0049` through `C2:1628`
5. if that flag is set and the low three bits of the `C0:0AA1` result are zero, returns `0x00B0`
6. otherwise returns the high byte of the `C0:0AA1` result

Mechanically, the ordinary path is:

`return (C0:0AA1($9877, $987B) >> 8) & 0xFF`

with one flag-gated override to `0xB0`.

## Why The Name Stays Broad

`C0:0AA1` is already used elsewhere as a current-map tile/context classifier. For example, the `0x1D 22` exit-mouse check reads the current tile/context class from `C0:0AA1` and tests it for a specific value.

This helper is adjacent to battle-facing code, but `C1:AD7D` itself does not inspect battlers or actions. Its local proof is position/context oriented:

- input source is overworld position state
- helper call is `C0:0AA1`
- event-flag override uses `C2:1628(0x0049)`
- output is one byte of context data

So the safest current label is "current overworld position context byte," with the exact gameplay meaning of the `0xB0` override still open.

## Practical Conclusion

The unknown start `C1:AD7D` is now accounted for as a small current-position context accessor with an event-flag `0x49` override. It is not part of the `C1:ADB4` targetting resolver even though it sits immediately before it in the bank include order.
