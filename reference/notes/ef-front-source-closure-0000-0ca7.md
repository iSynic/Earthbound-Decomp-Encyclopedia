# EF Front Source Closure, `EF:0000..EF:0CA7`

This note closes the large front preserved corridor left in the EF readable
source dashboard.

## Reference Order

The split follows the opening include order in
`refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`:

- `battle/enemy_flashing_off.asm`
- `battle/enemy_flashing_on.asm`
- `unknown/EF/EF00BB.asm` through `unknown/EF/EF01D2.asm`
- `audio/pause_music.asm`
- `unknown/EF/EF0262.asm`
- `audio/resume_music.asm`
- `unknown/EF/EF027D.asm` through `unknown/EF/EF04DC.asm`
- `data/sram_signature.asm`
- `data/unknown/EF05A6.asm`
- `system/saves/*`
- `unknown/EF/EF0C3D.asm`, `EF0C87.asm`, and `EF0C97.asm`

The ebsrc tree includes the battle enemy-flashing and audio pause/resume bodies,
but the `unknown/EF` and `system/saves` file bodies are absent. For those
missing files, the source split uses bankconfig anchors, direct ROM decode, and
byte-equivalence validation.

## Promoted Source

| Range | File | Role |
| --- | --- | --- |
| `EF:0000..EF:00BB` | `src/ef/ef_0000_00bb_enemy_flashing_helpers.asm` | Enemy target flashing off/on helpers, matching the ebsrc battle helper bodies. |
| `EF:00BB..EF:0256` | `src/ef/ef_00bb_0256_battle_overworld_visual_helpers.asm` | Visual helper cluster for battle sprite/effect state and related overworld scratch updates. |
| `EF:0256..EF:027D` | `src/ef/ef_0256_027d_audio_pause_resume_flags.asm` | Pause/resume music and HP/PP meter speed flags, matching the ebsrc audio helpers. |
| `EF:027D..EF:0591` | `src/ef/ef_027d_0591_overworld_entity_snapshot_helpers.asm` | Overworld entity snapshot and transition helper cluster before SRAM data. |
| `EF:05A9..EF:0C3D` | `src/ef/ef_05a9_0c3d_save_sram_helpers.asm` | Save-block and save-slot SRAM helper family. |
| `EF:0C3D..EF:0CA7` | `src/ef/ef_0c3d_0ca7_front_unknown_tail_helpers.asm` | Small load-slot/overworld refresh tail immediately before the delivery selector helpers. |

## Preserved Data

| Range | File | Role |
| --- | --- | --- |
| `EF:0591..EF:05A9` | `src/ef/ef_0591_05a9_sram_signature_and_save_block_flags.asm` | `SRAM_SIGNATURE` string plus the three save-block present bit masks from `data/unknown/EF05A6.asm`. |

## Save Helper Boundary Map

The save/SRAM source family uses these entry anchors:

- `EF:05A9` erase save block
- `EF:0630` check save block signature
- `EF:0683` check all save block signatures
- `EF:06A2` copy save block
- `EF:0734` calculate save block checksum
- `EF:077B` calculate checksum complement
- `EF:07C0` validate save block checksums
- `EF:0825` check save corruption
- `EF:088F` save game block
- `EF:0A4D` save game slot
- `EF:0A68` load game slot
- `EF:0B9E` check SRAM integrity
- `EF:0BFA` erase save slot
- `EF:0C15` copy save slot

The slot/block ownership is now pinned in `notes/sram-template-contracts.md`.
The retail helpers treat SRAM blocks `0/1`, `2/3`, and `4/5` as the
primary/backup pairs for user save slots `0`, `1`, and `2`. `EF:0A4D` saves
both copies, `EF:0A68` loads from the primary block, `EF:0825` validates and
repairs a pair from the surviving copy, and `EF:0BFA`/`EF:0C15` erase/copy both
blocks in a pair. The decompressed E0 template also contains blocks `6/7`, but
those are outside the normal `EF:0683`/`EF:0825` slot loops and are preserved as
reserve template records until a caller proves a narrower role.

These names mirror the include order, with local labels promoted from the ROM
entry points.

## Validation Contract

This corridor is source-bank build-candidate material. It is accepted because
the combined EF scaffold preserves byte equivalence against the original ROM,
the source/data cuts match ebsrc include anchors, and the only non-code bytes in
the corridor are isolated as the SRAM signature/flag data island.
