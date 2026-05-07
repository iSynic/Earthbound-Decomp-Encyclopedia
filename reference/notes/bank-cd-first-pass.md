# Bank CD First Pass

## Main result

Bank `CD` is a pure battle-sprite graphics payload bank. It contains no code,
no inline tables, and no slack: the `55` compressed sprite assets fill the full
`CD:0000..CD:FFFF` bank.

Follow-up source-scaffold status:

- durable scaffold: `src/cd/bank_cd_helpers_asar.asm`
- manifest: `build/cd-build-candidate-ranges.json`
- handoff: `notes/bank-cd-source-scaffold-handoff.md`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `55`
- byte-equivalence: `OK`, `0` mismatches

Primary artifacts:

- `notes/bank-cd-asset-data-map.md`
- `build/asset-bank-cd.json`

The generated map accounts for:

- binary assets: `55`
- binary asset bytes: `65536`
- asset mix: `55` compressed graphics payloads (`gfx`)
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `0`
- missing payload metadata: `0`

## Bank layout

The full bank is a source-order run of compressed `battle_sprites/*.gfx.lzhal`
payloads:

- first asset: `BATTLE_SPRITE_107`, `CD:0000..CD:0E25`, `3622` bytes.
- largest asset: `BATTLE_SPRITE_107`, `3622` bytes.
- locale-resolved assets:
  - `BATTLE_SPRITE_62`, `CD:CCCF..CD:D01C`, `846` bytes.
  - `BATTLE_SPRITE_23`, `CD:FC6C..CD:FFFF`, `916` bytes.
- final asset: `BATTLE_SPRITE_23`, ending exactly at `CD:FFFF`.

There are no pointer/config table includes in this bank. The battle sprite
pointer table is separate, at
`refs/ebsrc-main/ebsrc-main/src/data/battle/battle_sprites_pointers.asm`.

## Runtime corroboration

The runtime path is in `refs/ebsrc-main/ebsrc-main/src/battle/load_battle_sprite.asm`:

- sprite IDs are decremented and multiplied by `5`, matching a five-byte
  `BATTLE_SPRITES_POINTERS` entry format.
- the fifth byte of each pointer entry is used as a battle-sprite shape code.
- `LOAD_BATTLE_SPRITE` dereferences the pointer entry and passes the selected
  compressed sprite payload to `DECOMP`.

The width/height helpers corroborate the shape-code interpretation:

- `GET_BATTLE_SPRITE_WIDTH` maps shape codes `1/3` to `4`, `2/4` to `8`, and
  `5/6` to `16`.
- `GET_BATTLE_SPRITE_HEIGHT` maps shape codes `1/2` to `4`, `3/4/5` to `8`,
  and `6` to `16`.

So CD stores payload bytes only; dimensions and sprite selection are controlled
by the external `BATTLE_SPRITES_POINTERS` table and loader code.

## Current CD confidence boundary

High confidence:

- CD is a full-bank battle-sprite payload slab.
- Every byte from `CD:0000` through `CD:FFFF` belongs to one of the `55`
  compressed graphics assets.
- `LOCALEBINARY` resolution is required for the US versions of sprites `62` and
  `23`.
- No source-level table reconstruction is needed inside this bank.

Still intentionally out of scope:

- This pass does not decompress or render the battle sprites.
- Sprite IDs, dimensions, and enemy associations depend on the external
  `BATTLE_SPRITES_POINTERS` table and enemy/battle data in other banks.
- The internal compressed graphics format remains handled as opaque LZHAL data.

## Recommended next move

Treat CD as structurally complete and byte-protected for the current
bank-coverage phase. Proceed to `CE`; if it introduces the pointer table or
enemy association data, use the CD runtime notes above to name that structure
explicitly.
