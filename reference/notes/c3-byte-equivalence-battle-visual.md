# C3 byte-equivalence validation

This report assembles a scratch Asar translation of one C3 pilot module into a clean ROM copy at its original `org`, then compares the protected byte range against the original ROM.

- status: `OK`
- source path: `src/c3/battle_visual_effect_helpers.asm`
- range: `C3:F5F9..C3:FB1F`
- size: `1318` bytes
- mismatches: `0`
- generated asm: `build/c3-byte-equivalence/battle-visual-effect.byte-equivalence.asar.asm`
- patched ROM: `build/c3-byte-equivalence/battle-visual-effect.byte-equivalence.sfc`
