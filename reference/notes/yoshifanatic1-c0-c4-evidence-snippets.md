# C0-C4 Evidence Snippets

These are short examples behind the handoff packet. They are not a substitute
for the full notes corpus, but they give a reviewer a fast way to judge the
quality and limits of the exported names/contracts.

## C4:74F6 window span radius ramp

Working name: `WhWindowSpanRadiusRampTable`

Bytes:

```text
10 10 0F 0F 0E 0D 0C 0B 09 06 03
```

Consumer: `C4:7501`.

`C4:7501` clamps a vertical edge distance to `0..10`, indexes the table in
reverse, and uses the byte as a horizontal span radius around the current
entity's screen-relative X center. The generated stream is then used by the
current-entity WH window-mask helpers.

Primary note: `notes/window-mask-and-indexed-gfx-c47501-c47b77.md`

## C4:0BE8 blank common source block

Working name: `BlankCommonTileSourceBlock`

ROM range: `C4:0BE8..0DE7`.

The block is `0x200` bytes of zero. The next nonzero/named data family begins
at `C4:0DE8`. Multiple visual/setup paths use the block as a fixed bank-C4
source for seeding or clearing graphics/tile memory; one direct visual helper
copies it to `$7C00`.

Primary note: `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`

## C4:DE78 Your Sanctuary coordinate/source table

Working name: `YourSanctuaryLocationCoordinateTable`

Shape: eight records, each two words.

| Index | Word 0 | Word 1 |
| ---: | ---: | ---: |
| 0 | `0x0097` | `0x0030` |
| 1 | `0x0183` | `0x03F5` |
| 2 | `0x0023` | `0x01E4` |
| 3 | `0x0058` | `0x029C` |
| 4 | `0x01DF` | `0x0208` |
| 5 | `0x01BD` | `0x030B` |
| 6 | `0x034B` | `0x0258` |
| 7 | `0x02FE` | `0x04CC` |

Consumer: the Your Sanctuary display helper at `C4:E281`. It indexes this table
by location id, passes the first word in `A` and the second word in `X` to
`C4:E13E`, then marks the matching `$B4BE` loaded slot.

Primary note: `notes/your-sanctuary-location-coordinate-table-c4de78.md`

## C4:8C59 staged movement pulse selector table

Working name: `MovementOctantToPulseSelectorTable`

Shape: eight words.

```text
0008 0009 0001 0005 0004 0006 0002 000A
```

The C4 staged-movement helper rounds a direction into an octant, maps that
octant through this table, and appends the resulting pulse selector to a compact
runtime movement script accumulator rooted at `$9E58/$9E59`.

Primary note: `notes/staged-movement-pulse-and-tracked-item-registry-c48c59-c48f98.md`

## C4:8D38 signed movement unit deltas

Working name: `MovementOctantSignedUnitDeltaTable`

Shape: sixteen words; best current interpretation is two eight-word signed
component arrays.

```text
0000 0001 0001 0001 0000 FFFF FFFF FFFF
FFFF 0000 0001 0001 0001 0000 FFFF FFFF
```

Confidence is lower than `C4:8C59` because the direct table consumer has not
been isolated locally yet. It is included as a proposed contract because the
shape and placement in the staged-movement corridor are strong.

Primary note: `notes/staged-movement-pulse-and-tracked-item-registry-c48c59-c48f98.md`

## C1:E48D naming conflict resolved

Final working name: `RenderSingleTextInputOptionRowScoped`

During C0-C4 integration, the label emitter caught two names for the same
address:

- `RenderTextInputRowScoped`
- `RenderSingleTextInputOptionRowScoped`

The second name was retained because the focused text-input note documents the
routine's scoped single-row behavior and inputs. The subsystem synthesis note
was updated to match, and the combined label bundle now emits without duplicate
address conflicts.

Primary notes:

- `notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`

## Fixed D5 battle/item table contracts

The C0-C4 contract manifest includes fixed D5 table shapes backed by the local
notes and reference structs:

| Contract | Address | Stride | Count |
| --- | --- | ---: | ---: |
| `ITEM_CONFIGURATION_TABLE` | `D5:5000` | `0x27` | 256 |
| `BATTLE_ACTION_TABLE` | `D5:7B68` | `0x0C` | 318 |
| `PSI_ABILITY_TABLE` | `D5:8A50` | `0x0F` | 54 |
| `ENEMY_CONFIGURATION_TABLE` | `D5:9589` | `0x5E` | 231 |

These are especially useful because C1/C2 code repeatedly consumes fields from
these records for menus, battle action dispatch, target selection, item effects,
and enemy/battler initialization.

Primary artifacts:

- `data-contracts-c0-c4.json`
- `data-contracts-c0-c4.md`

