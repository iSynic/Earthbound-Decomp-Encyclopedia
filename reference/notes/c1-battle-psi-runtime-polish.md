# C1 Battle PSI Runtime Polish

Status: second C1 battle-facing polish slice.

This note records byte-neutral source comments added after
`notes/c1-battle-front-end-runtime-polish.md`. The slice focuses on the battle
PSI user-selection front end, category and entry-list builders, row formatting,
and ordinary battle PSI controller.

## Source Modules Touched

| Source module | Runtime contract pinned |
| --- | --- |
| `src/c1/c1_b5b6_open_battle_psi_user_selection.asm` | Chooses the active PSI user, stages it in `$9D16`, uses `$9D18` for the single-user fast path, selects a D5:8A50 PSI row, handles category-8 special rows, and exports ordinary success state into the `$9FFA` battle selection snapshot family. |
| `src/c1/c1_c452_build_shared_battle_psi_entry_list.asm` | Builds PSI entry lists from D5:8A50 15-byte rows using caller-staged usability/category masks, character learn-level bytes, menu position bytes, and PSI family/rank fields. |
| `src/c1/c1_c853_resolve_battle_psi_targeting_metadata.asm` | Resolves the chosen PSI user/party record and delegates broad all-category list/metadata refresh work to C1:C452. |
| `src/c1/c1_c8bc_format_battle_psi_menu_entry_row.asm` | Formats second-stage PSI rows from D5:8A50 and associated D5:7B68 action rows, including the Thunder direct-row bypass and C3:F124/C3:F11C encoded row/tail blocks. |
| `src/c1/c1_ca06_build_psi_rank_name.asm` | Prints the PSI family from D5:8A50 byte +0 and the rank suffix through C3:F112 from byte +1. |
| `src/c1/c1_ca72_refresh_battle_psi_selection.asm` | Refreshes active-user PSI metadata through `$9D16 -> C1:C853` and redraws the selected row's PSI family name. |
| `src/c1/c1_caf5_build_battle_psi_category_entry_list.asm` | Maps battle PSI categories to C1:C452 mask pairs: offense, recover, assist, and other. |
| `src/c1/c1_cb7f_has_battle_psi_category_entries.asm` | Validates ordinary battle PSI categories, runs the category/entry picker, checks PP against associated D5:7B68 action rows, resolves targets through C1:ADB4, and writes the final six-byte menu-selection record. |

## Evidence Inputs

- `notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md`
- `notes/battle-psi-menu-controller-c1cc39-ce73.md`
- `notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md`
- `notes/battle-psi-category-list-family-c1caf5-c1cb7f.md`
- `notes/battle-psi-menu-table-helpers-c1c046-c1c165.md`
- `notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md`
- `notes/battle-psi-selection-refresh-c1ca72.md`
- `notes/battle-psi-ability-table-d58a50.md`

## Runtime Contract

D5:8A50 is the battle PSI ability table with 15-byte rows. The polished source
comments now pin the fields most heavily used by C1:

- byte `+0`: PSI family id
- byte `+1`: PSI rank
- byte `+2`: PSI category mask
- byte `+3`: battle usability/target mask
- word `+4`: associated D5:7B68 battle action id
- bytes `+6..+8`: character learn-level gates
- byte `+9`: menu x position
- byte `+10`: menu y position
- bytes `+11..+13`: help-text pointer

The ordinary battle PSI controller at C1:CC39 uses category selection first,
then a D5:8A50 entry list. After a row is selected it checks current PP against
the associated D5:7B68 action row, calls C1:ADB4 for targetting, and writes the
final selection record fields:

- `+1`: selected PSI row id
- `+2..+3`: associated battle action id
- `+4`: mapped targetting class
- `+5`: selected target

The outer front end at C1:B5B6 is intentionally separate from that lower
controller. It first chooses the PSI user, stages `$9D16`, and handles the
direct PSI-entry picker and snapshot/text side effects used by the battle command
path.

Follow-up source polish now pins the lower controller/formatter vocabulary in
source:

- `C1:C8BC` names `D5:8A50` as the 15-byte PSI ability table and `D5:7B68` as
  the associated action table used for coarse menu-entry row selection and PP
  cost display
- `C1:C8BC` names the fixed encoded `C3:F124` 20-byte menu-entry rows and the
  fixed `C3:F11C` 8-byte companion tail
- `C1:CB7F..CE73` names the PP guard as `D5:7B68 + 0x03` compared against the
  acting party member's current PP target word
- the final six-byte battle menu selection writes now carry explicit field
  names for PSI row, associated action word, targetting byte, and selected
  target byte

The adjacent outer front end now carries the same source vocabulary:

- `C1:B5B6..BB71` names the selected-user byte, single-user fast-path latch,
  highlighted help-text row byte, PP guard, category-8 blocker/event branch,
  and D5:8A50/D5:7B68 table joins.
- Its ordinary success lane names the `$9FFA` battle selection snapshot root,
  `$A972` active snapshot pointer, exported `+0x1D` state byte, and live
  `$99DC` state mirror copyback.
- The `C1:BB06` finalizer names the help-text window refresh path through
  `C1:C8BC` and `D5:8A50 +0x0B`.

## Promotion Boundary

This slice promotes source comments and local runtime wording only. It does not
assign final names to every encoded C3:F124/C3:F11C row, prove every
player-facing category-8 branch detail, or rename C1:C046/C1:C165 beyond their
existing source-backed labels.

Open followups:

- correlate the category-8 B5B6 branch with C0:DD53 event/transition semantics
- decode the C3:F124 encoded row contents and C3:F11C fixed tail at the glyph
  level
- cross-check D5:8A50 field names against CoilSnake PSI table schemas once more
  diff-confirmed probes exist
- carry the same polish style into C1 text command leaves and file-select flows

Completed followups:

- `C1:B5B6..BB71` now has source-backed constants for the outer PSI
  user-selection, snapshot export, action-text, and help-text refresh lane.
- `C1:C452`, `C1:C853`, `C1:CA06`, `C1:CA72`, `C1:CAF5`, and `C1:CB7F` now
  name their remaining helper-call surface in source. The pass covers text-entry
  chain clearing, window update/tick helpers, cursor positioning, fixed-string
  PSI rank printing, battle-sprite row effect clearing, category focus, and the
  `CA72 -> C853` metadata refresh join.
- `C1:B5B6`, `C1:BB71`, and `C1:CB7F` now name the shared callback pointer ABI
  at their caller edges. The outer PSI user prompt stages display and
  eligibility callbacks for `C1:27EF` through named `$0E/$10` and `$12/$14`
  pairs, while the direct PSI-entry, field-PSI category, finalizer, and ordinary
  battle-PSI category/entry loops install row formatter callbacks for
  `C1:1F5A` through named `$0E/$10` pairs.

## Validation

Run after source-comment edits:

```powershell
python tools\validate_source_bank_byte_equivalence.py --bank C1 --module all --combined --scaffold src\c1\bank_c1_helpers_asar.asm --strict
```
