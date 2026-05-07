# C3 byte-equivalence validation

This report assembles a scratch Asar translation of one C3 pilot module into a clean ROM copy at its original `org`, then compares the protected byte range against the original ROM.

- status: `OK`
- source path: `src/c3/hp_pp_adjustment_helpers.asm`
- range: `C3:EC1F..C3:EE14`
- size: `501` bytes
- mismatches: `0`
- generated asm: `build/c3-byte-equivalence/hp-pp-adjustment.byte-equivalence.asar.asm`
- patched ROM: `build/c3-byte-equivalence/hp-pp-adjustment.byte-equivalence.sfc`
