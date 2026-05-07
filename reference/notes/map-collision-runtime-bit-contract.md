# Map Collision Runtime Bit Contract

This contract takes the now-verified collision byte and records how C0
actually masks it at runtime. Storage is high confidence; some gameplay
labels remain intentionally provisional.

## Summary

- confidence: `high-structural / medium-semantic`
- supported high collision mask: `0x00C0`
- observed high-collision values in D8: `0x80`, `0x82`, `0x84`, `0x90`, `0x92`, `0x94`
- runtime-supported but unobserved high bit: `0x40`
- observed special-latch values in D8: `0x10`, `0x90`, `0x92`, `0x94`
- terrain compatibility mask: `0x000C`
- single-mode masks from `C2:00D1`: `0x001E`, `0x0033`, `0x001E`, `0x0033`

## Runtime Masks

| Mask | Working Name | D8 Cells | Full `.fts` Cells | Scene Cells | Role |
| ---: | --- | ---: | ---: | ---: | --- |
| `0x00C0` | `high_collision_block_mask` | 13822 | 110422 | 522397 | C0:5769, C0:3C4B, player/bicycle movement, pathfinding, teleport, and movement-script probes treat any selected bit as blocking/high collision. |
| `0x00D0` | `movement_cache_stop_mask` | 13951 | 110673 | 523258 | Per-slot collision caches store and later gate movement on $5DA4 & #$00D0, combining the high collision family with the 0x10 special-surface latch bit. |
| `0x0010` | `special_surface_coord_latch` | 411 | 867 | 2618 | C0:54C9 stores the raw probed coordinates into $5DA8/$5DAA when this bit is present; player movement later calls C0:7526 with that latched coordinate pair. |
| `0x000C` | `entity_terrain_compatibility_class` | 3853 | 8667 | 28066 | C0:5DE7 maps A & #$000C into a three-way permission mask against the entity metadata byte at D5:9589 + mapped_offset + 0x20. |
| `0x003F` | `returned_surface_modifier_mask` | 10423 | 24762 | 82774 | C0:5B7B strips high collision bits before returning a movement/surface modifier byte to the player movement caller. |

## Sample Points

`C0:5769` uses six sample points. It returns a six-bit occupancy
result where bit `N` is set when selected sample point `N` had
`collision_byte & #$00C0`.

| Slot | X Offset | Y Offset |
| ---: | ---: | ---: |
| 0 | -8 | 0 |
| 1 | 0 | 0 |
| 2 | 7 | 0 |
| 3 | -8 | 7 |
| 4 | 0 | 7 |
| 5 | 7 | 7 |

## Surface Decoders

| Routine | Mask | Slots | Possible Results | Handled-But-Impossible Results |
| --- | ---: | --- | --- | --- |
| `C0:57E8 Resolve_SurfaceMask0007` | `0x0007` | 0, 1, 2 | `0x00`, `0x01`, `0x02`, `0x03`, `0x04`, `0x05`, `0x06`, `0x07` | `none` |
| `C0:583C Resolve_SurfaceMask0038` | `0x0038` | 3, 4, 5 | `0x00`, `0x08`, `0x10`, `0x18`, `0x20`, `0x28`, `0x30`, `0x38` | `0x07` |
| `C0:5890 Resolve_SurfaceMask0009` | `0x0009` | 0, 3 | `0x00`, `0x01`, `0x08`, `0x09` | `none` |
| `C0:59EF Resolve_SurfaceMask0024` | `0x0024` | 2, 5 | `0x00`, `0x04`, `0x20`, `0x24` | `none` |
| `C0:5B4E single-mode masks for modes 1/5` | `0x001E` | 1, 2, 3, 4 | `0x00`, `0x02`, `0x04`, `0x06`, `0x08`, `0x0A`, `0x0C`, `0x0E`, `0x10`, `0x12`, `0x14`, `0x16`, `0x18`, `0x1A`, `0x1C`, `0x1E` | `none` |
| `C0:5B4E single-mode masks for modes 3/7` | `0x0033` | 0, 1, 4, 5 | `0x00`, `0x01`, `0x02`, `0x03`, `0x10`, `0x11`, `0x12`, `0x13`, `0x20`, `0x21`, `0x22`, `0x23`, `0x30`, `0x31`, `0x32`, `0x33` | `none` |

## Bit Role Boundary

- `0x80` is the observed solid/high-collision bit in the verified D8 and `.fts` data.
- `0x40` is tested by the runtime high-collision mask, but is not present in the verified map collision data.
- `0x10` latches a probed coordinate pair and participates in the per-slot movement cache stop mask.
- `0x04` and `0x08` are proved as entity terrain-compatibility class bits through `C0:5DE7`.
- `0x01` and `0x02` remain low surface modifier bits; they are preserved through the low-six-bit return path, but their final human gameplay labels need more caller-side evidence.

## Machine-Readable Data

`notes/map-collision-runtime-bit-contract.json` records mask counts,
sample-point tables, possible surface-probe results, runtime anchors,
and interpretation boundaries.
