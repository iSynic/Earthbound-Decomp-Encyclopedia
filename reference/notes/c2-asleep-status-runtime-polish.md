# C2 Asleep Status Runtime Polish

This note records the byte-neutral C2 asleep-status polish slice. It promotes
the resist-checked asleep body at `C2:9F06` and its reusable wrapper at
`C2:9F57`.

Primary source modules:

- `src/c2/c2_9f06_run_resist_checked_asleep_status_action.asm`
- `src/c2/c2_9f57_run_asleep_status_wrapper_action.asm`

Related evidence notes:

- `notes/class2-asleep-family-c29f06-c29f57.md`
- `notes/class2-affliction-apply-helper-724a.md`
- `notes/class2-battler-affliction-crosswalk.md`
- `notes/c2-late-status-runtime-polish.md`
- `notes/data-contracts-c0-c4.md`

## Asleep Body

`C2:9F06` is the shared asleep-status apply body. It gates through the selected
battler default blocker, reads selected-row byte `+0x3C`, and passes that byte
through `C2:6BB8` / `RollActionChanceGate` before applying a
temporary-subgroup status value.

Promoted runtime contract:

| Contract | Runtime shape |
| --- | --- |
| blocker | `C2:7CFD` |
| resistance byte | selected row `+0x3C`, locally named `hypnosis_resist` |
| resistance helper | `C2:6BB8` / `RollActionChanceGate` |
| status writer | `C2:724A` / `ApplySelectedRowAfflictionSlotValue` |
| writer args | `Y = 1`, `X = 2` |
| target field | selected row `+0x1F = 1` |
| success text | `EF:6C55` |
| failure text | `EF:766E` |

This gives the temporary subgroup byte `+0x1F` another concrete runtime anchor:
value `1` is asleep in this apply family and in the matching recovery path.

The source call site now names both the selected-row action chance gate and the
selected-row slot writer directly, rather than entering through inherited or
overbroad helper labels.

## Wrapper Reuse

`C2:9F57` is only a thin wrapper over `C2:9F06`. It is still useful to keep as a
separate source-facing routine because action-table rows can target the wrapper
as their second pointer without duplicating the effect body.

Current local action-table anchors:

| Entry | Shape | Second pointer |
| --- | --- | --- |
| `0x0035` / `53` | enemy/all/PSI, cost `18` | `C2:9F57` |
| `0x005A` / `90` | enemy/all/other | `C2:9F57` |

The safe wording is therefore not "this is only Hypnosis alpha" or "this is only
an enemy action." It is a reusable all-target asleep-status wrapper with at
least one PSI-side use and one `other` use.

## Adjacent PP Drain And Paralysis Tail

The same source module also carries the adjacent `C2:9F5E..A04F` tail:

- `C2:9F5E` drains PP and emits amount-bearing `EF:773F` through
  `C1:DC66`.
- `C2:9FFE` is the `BTLACT_PARALYSIS_A` body. It writes primary affliction
  byte `+0x1D = 3` and emits `EF:6AE0`, now cross-checked in the EF text
  payload split as the body-numb result text.
- `C2:A04F` is the far wrapper for that paralysis body.

The earlier local "poison" wording was too broad for this tail. Actual
poison-inflicted text remains the separate `EF:6B18` script used by the
item/status cluster.

## Decomp Value

This slice joins three contracts that were easy to read separately:

- `D5:7B68` second-pointer rows can dispatch through `C2:9F57`.
- `C2:9F57` redirects to the single asleep body at `C2:9F06`.
- `C2:9F06` joins selected-row resistance byte `+0x3C` to temporary subgroup
  byte `+0x1F = 1` through the generic status writer.

That gives contributors a clean path from editor-visible action metadata to the
runtime row fields involved in asleep application and recovery.

## Remaining Soft Spots

- `C2:6BB8` is now locally named as the generic action chance gate; the exact
  human-facing interpretation of selected-row `+0x3C` still belongs to the
  broader resistance/immunity pass.
- The exact player-facing names for action-table entries `53` and `90` remain
  table-crosswalk followups.
- Global enum promotion for `+0x1F` should remain scoped until all non-recovery
  readers are checked.
