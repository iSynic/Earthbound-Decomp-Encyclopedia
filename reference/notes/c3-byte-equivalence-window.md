# C3 byte-equivalence validation

This report assembles a scratch Asar translation of one C3 pilot module into a clean ROM copy at its original `org`, then compares the protected byte range against the original ROM.

- status: `OK`
- source path: `src/c3/window_text_helpers.asm`
- range: `C3:E450..C3:E84E`
- size: `1022` bytes
- mismatches: `0`
- generated asm: `build/c3-byte-equivalence/window-text.byte-equivalence.asar.asm`
- patched ROM: `build/c3-byte-equivalence/window-text.byte-equivalence.sfc`
