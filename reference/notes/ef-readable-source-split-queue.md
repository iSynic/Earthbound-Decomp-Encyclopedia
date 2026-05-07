# EF Readable Source Split Queue

This note began as the EF first-pass source-bank closure queue. It now records
the split strategy and the completed checkpoints that retired the broad EF
preserved corridors.

## Current Boundary

- Structural scaffold: closed and byte-equivalent.
- Readable source closure: closed for EF; `notes/readable-source-bank-closure.md`
  now reports `0` EF preserved-corridor bytes.
- Remaining EF work is decoder maturity and asset/data semantics, especially
  text/table payloads and the late named tail after `EF:F0D7`.

## Source Order From Refs

The strongest global guide is still:

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`
- `notes/bank-ef-first-pass.md`
- `notes/bank-ef-reference-frontier.md`
- `notes/bank-ef-asset-data-map.md`

Those refs do not give us every local file body, but they do give source order,
include names, and many encoded address anchors. That was enough to split the
coarse corridor into safer lanes.

## Split Lanes

| Lane | Range | Current Read | Closure Type | Best Evidence |
| --- | --- | --- | --- | --- |
| EF front helpers | `EF:0000..EF:05A5` | Enemy flashing, audio pause/resume, early unknown helpers, SRAM signature setup. | decoded source plus small data | `bank2f.asm`, C1/C2 local mentions |
| Save/SRAM family | `EF:05A6..EF:0C3C` | Save block/slot erase, copy, checksum, integrity, load/save helpers. | decoded source | named `system/saves/*` includes |
| Delivery/selector helpers | `EF:0C3D..EF:101A` | Timed-delivery/service row helpers around `D5:F645`, plus adjacent unknown helpers. | decoded source first | `notes/delivery-row-helpers-ef0e67-ef0ead.md`, `notes/selector-row-config-family-ef0ee8.md` |
| Map tables | `EF:101B..EF:4A3F` | Tileset table, graphics/arrangement/palette/collision/animation pointer tables, animation properties, sprite grouping pointers/data. | typed data contracts | map milestone contracts, EF sprite grouping pointer table users |
| Sound Stone data | `EF:4A40..EF:4E1F` | Sound Stone presentation data. | typed data/asset | `C4:AC57` pointer table anchors |
| Text run | `EF:4E20..EF:C51A` | PSI help, battle text, goods text, command/status text, keyboard/name input, unknown text, town-map data. | text/script asset split | D5 PSI pointers, C1 text/menu consumers |
| Glyph masks | `EF:C51B..EF:D56E` | Text-token glyph merge mask and carry-mask regions. | typed data contracts | `C4:4B3A` consumers |
| Debug/menu source | `EF:D56F..EF:EB5E` | Debug strings, debug overlay helpers, cursor/menu processing, and remaining unknown routines. | decoded source plus data | `notes/debug-menu-reachability-c0-c1-ef.md`, `bank2f.asm` |
| Exact debug graphics | `EF:EB5F..EF:EF6F`, `EF:EFB7..EF:F0D6` | Debug font and cursor graphics. | already exact assets | `asset-manifests/ef-debug-assets.json` |
| Late tail | `EF:F0D7..EF:FFFF` | Named unknown/version/unused/debug cursor spritemap tail. | typed data split | `bank2f.asm`, asset map gap |

## Historical First Practical Promotion Target

The first readable-source promotion seam was:

```text
EF:0CA7..EF:101B
```

Why this one first:

- It is executable helper code, not text or opaque asset data.
- Existing notes already explain most of the semantics.
- It connects to a typed D5 table contract (`D5:F645`) instead of relying only
  on local instruction shape.
- It ends immediately before the `EF:101B` map table data, which keeps the
  following payload classified as data instead of decoding into false
  `BRK`/`COP`-looking instructions.
- It is small enough to split out of the coarse EF corridor without redesigning
  the whole EF scaffold at once.

Expected source-facing labels:

- `EF:0CA7` delivery retry threshold helper
- `EF:0D23` current-row retry wait getter
- `EF:0D46` seed current-row delivery countdown
- `EF:0D73` decrement current-row delivery countdown
- `EF:0D8D` queue current-row pointer 1
- `EF:0DFA` queue current-row pointer 2
- `EF:0E67` current-row enter-speed getter
- `EF:0E8A` current-row exit-speed getter
- `EF:0EAD` instantiate delivery row sprite/placeholder
- `EF:0EE8` scan delivery/service rows by event flag
- `EF:0F60` delivery-arrival readiness check
- `EF:0FDB` begin delivery success arrival state
- `EF:0FF6` reset delivery arrival state

## Historical Second Practical Target

After that, split `EF:101B..EF:4A3F` as typed data, not source. This does not
make EF "more decoded asm," but it removes a large amount of false source debt
from the preserved corridor by reclassifying map tables and sprite grouping
tables into explicit data contracts.

## Completed Split Checkpoints

- `EF:0000..EF:0CA7` is now closed as source/data lanes: enemy flashing
  helpers, battle/overworld visual helpers, audio flag helpers, overworld
  entity snapshot helpers, the SRAM signature/flag island, save/SRAM helpers,
  and the load-slot/overworld refresh tail. The retired preserved-corridor
  scaffold has been replaced by the promoted modules documented in
  `notes/ef-front-source-closure-0000-0ca7.md`.
- `EF:0CA7..EF:101B` is now promoted into
  `src/ef/ef_0ca7_delivery_selector_helper_cluster.asm` as decoded helper
  source. The split was the first step in retiring the broad EF front corridor
  and isolating the later table/text/debug lanes.
- `EF:101B..EF:D56F` is now split into broad typed data/text lanes:
  map tileset and sprite grouping tables, Sound Stone presentation data, text
  payload data, and text glyph mask tables. This keeps the largest known
  data/text payloads out of the remaining source-heavy debug corridor.
- `EF:D56F..EF:EB5F` is now closed as explicit source/data lanes, centered on
  debug menu strings/helpers and the one known non-debug overworld caller seam
  around `EF:E759`.
- `EF:D56F..EF:D6D4` is now promoted into
  `src/ef/ef_d56f_d6d4_debug_sound_menu_helpers.asm` as decoded source for the
  debug sound-menu tile/value helper prefix.
- `EF:D6D4..EF:DABD` is now split into the decoded sound-menu controller,
  debug menu option strings, and decoded graphics/state initialization helpers.
- `EF:DABD..EF:DF0B` is now split into decoded menu text and number formatting
  helpers plus the check-position and view-character overlay writers.
- `EF:DF0B..EF:EB5F` is now split into decoded overlay tile helpers, the debug
  menu runtime/cursor/command/input-playback helper cluster, the `EF:EB2A`
  color-math reset helper, and two tiny preserved data islands at
  `EF:EB1D..EF:EB2A` and `EF:EB3D..EF:EB5F`.
- `notes/ef-byte-equivalence-validation.md` confirms the combined EF scaffold
  still matches the original ROM with `0` mismatches.

## Remaining Success Criteria

Future EF refinement should:

1. keep the EF front source/data contract validated; the late tail after
   `EF:F0D7` is now asset/data maturity work rather than ordinary
   readable-source debt
2. preserve byte equivalence with `validate_source_bank_byte_equivalence.py`
3. rerun `tools/build_readable_source_bank_closure.py`
4. keep remaining known payloads in the `known data/assets` bucket instead of
   reintroducing broad preserved corridors
5. leave unresolved text, table, and tail lanes documented rather than hidden

That gives us a clean loop for any future bank: source/data split, validate,
rerun the closure dashboard, then choose the next lane by measured remaining
debt.
