# EF Save/SRAM Runtime Polish

This note records the first EF runtime semantic polish slice. It promotes the
save/SRAM helper contracts in `src/ef/ef_05a9_0c3d_save_sram_helpers.asm`
without changing emitted bytes.

Primary context:

- `notes/ef-runtime-semantic-polish-plan.md`
- `notes/sram-template-contracts.md`
- `notes/ef-front-source-closure-0000-0ca7.md`
- `notes/c1-file-select-runtime-polish.md`

## Source-Facing Contracts

The save helper source now names the stable SRAM layout constants used across
the family:

- `SaveBlockSize = 0x0500`
- `SaveSlotPairSize = 0x0A00`
- `SaveBlockSramBaseLo = 0x6000`
- `SaveBlockPayloadBaseLo = 0x6020`
- checksum header fields at `0x601C` and `0x601E`
- payload sizes for game state, party character records, and event flags:
  `0x01D9`, `0x023A`, and `0x0080`

The helper at `C0:9032` is now referenced by its source-backed contract name,
`C09032_Multiply16By16_ViaHardwareRegisters`, instead of the older misleading
local divide-style alias. In the save helpers it is used to scale block and
slot indices into SRAM offsets.

## Runtime Flow

`EF:05A9` erases one 0x500-byte SRAM block, then restores the `HAL Laboratory,
inc.` signature and the adjacent missing-save slot mask bytes from
`EF:0591..EF:05A8`.

`EF:0630` validates one block signature and erases/reinitializes the block when
the signature compare fails. `EF:0683` applies that signature check to the
normal six retail blocks: primary/backup pairs for save slots 0, 1, and 2.

`EF:0734` computes the additive checksum over bytes `0x020..0x4FF` of one
save block. `EF:077B` computes the wordwise XOR complement over the same
payload. `EF:07C0` compares both computed values against header fields
`+0x1C` and `+0x1E`.

`EF:0825` validates one user save slot pair. If one copy fails, it erases the
bad block and copies the surviving block over it. If both copies fail, it erases
both and ORs the slot's missing-save bit into `$9F79`.

`EF:088F` saves one block by copying the live game-state, party-character, and
event-flag regions into the block payload, writing the additive checksum, then
writing the XOR complement. `EF:0A4D` calls that block writer for both copies in
one slot pair.

`EF:0A68` loads from the primary copy of a slot pair into the same live regions
and restores the active map pointer from `$99C9/$99CB` back to `$00A7/$00A9`.

`EF:0B9E` checks the SRAM integrity marker at `$30:7FFE`, clears the normal
0x2000-byte SRAM region when it is absent, initializes signatures, clears the
missing-save mask, then validates/repairs the three user save slots.

`EF:0BFA` erases both blocks in a save slot pair. `EF:0C15` copies both blocks
from one save slot pair to another.

## C1 Join Points

The C1 file-select setup paths persist text speed, sound, and window flavour
through `EF:0A4D(current_slot - 1)`. The action menu delete and copy paths call
`EF:0BFA(current_slot - 1)` and `EF:0C15(current_slot - 1, destination - 1)`.

Those C1 callers use one-based visible file slots; the EF helpers use zero-based
slot indices and expand each index to a primary/backup block pair.

The C1 setup source now names the `EF:0A4D` edge as `EF0A4D_SaveGameSlot`,
matching the EF source label. The C1-specific meaning is still "persist current
file setup state"; the callee-level contract is the broader save-slot writer.

## Validation

The source edit is byte-neutral:

```powershell
python tools\build_source_bank_scaffold.py --bank EF
python tools\validate_source_bank_byte_equivalence.py --bank EF --module all --combined --scaffold src\ef\bank_ef_helpers_asar.asm --strict
```

Current result:

- `EF byte-equivalence: OK, 28 module(s), 0 mismatch(es).`

## Remaining Soft Spots

- The live-copy helper calls still use their existing broad C0 names until the
  shared long-copy/clear/compare calling convention gets a dedicated polish
  pass.
- Reserved SRAM template blocks 6 and 7 remain outside the retail EF slot loops
  and should stay reserve records until a concrete caller proves another role.
