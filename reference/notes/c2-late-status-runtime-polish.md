# C2 Late Status Runtime Polish

This note records the byte-neutral C2 late status-action polish slice. It
promotes the status bodies that reuse the generic `C2:724A` affliction writer
outside the Flash family.

Primary source modules:

- `src/c2/c2_8bbe_run_mushroomize_status_action.asm`
- `src/c2/c2_8bfd_run_possess_status_action.asm`
- `src/c2/c2_8c69_run_crying_status_action.asm`
- `src/c2/c2_8cb8_run_immobilized_status_action.asm`
- `src/c2/c2_8cf1_run_solidified_status_action.asm`
- `src/c2/c2_8d3a_run_strange_status_wrapper_action.asm`
- `src/c2/c2_8dbb_run_direct_strange_status_action.asm`
- `src/c2/c2_9f06_run_resist_checked_asleep_status_action.asm`
- `src/c2/c2_9f57_run_asleep_status_wrapper_action.asm`
- `src/c2/c2_a056_run_resist_checked_strange_status_action.asm`

Related evidence notes:

- `notes/class2-affliction-apply-helper-724a.md`
- `notes/class2-persistent-status-action-pair-c28bbe-c28bfd.md`
- `notes/class2-temporary-status-action-cluster-c28c69-c28cb8-c28cf1.md`
- `notes/class2-asleep-family-c29f06-c29f57.md`
- `notes/class2-strange-status-family-c28d3a-c28dbb-c2a056.md`
- `notes/c2-psi-flash-runtime-polish.md`

## Status Writer Join

All promoted status bodies route through `C2:724A`, whose ABI is now documented
as:

- A = selected-row base
- X = subgroup offset relative to row `+0x1D`
- Y = incoming status value
- return `1` on write, `0` on blocked/no-upgrade

This slice extends the Flash-local map into the late action-table status rows.

Source-vocabulary update: the shared writer is now named
`ApplySelectedRowAfflictionSlotValue` at source call sites, with the older
`ApplyBattlerAfflictionSubgroupValue` alias retained inside the writer module.
The late status leaves, hit-resolution status tails, asleep/strange wrappers,
and item-side solidification leaves now call the selected-row slot ABI directly
instead of the inherited `INFLICT_STATUS_BATTLE` label.

The same caller cleanup now applies to the front-door gates: late status leaves
call `C2:7CFD` as `CheckSelectedBattlerDefaultTextBlocker`, and thresholded
solidification/defense-down leaves call `C2:7C96` as
`RollSelectedRowThresholdGate`.

## Persistent Subgroup `+0x1E`

| Module | Parameters | Result |
| --- | --- | --- |
| `C2:8BBE` | `Y = 1`, `X = 1` | write `+0x1E = 1`, emit `EF:6B81` |
| `C2:8BFD` | `Y = 2`, `X = 1` | write `+0x1E = 2`, emit `EF:6B98` |

`C2:8BFD` also requires selected-row `+0x0E == 0` and may seed the
`A18C/A18D/A18F` companion route through `C2:B6EB` after a successful write.
The selected-row collapse pass now gives that companion route a concrete local
neighbor: `C2:7550/77CA` can rebuild scratch battler base `$A180` with special
enemy id `0xD5` after neighboring `+0x1E == 2` checks. See
`notes/class2-b6eb-caller-family-760c.md`.

## Temporary Subgroup `+0x1F`

| Module | Parameters | Result |
| --- | --- | --- |
| `C2:9F06` | `Y = 1`, `X = 2` | resist-checked asleep-style write, emit `EF:6C55` |
| `C2:8C69` | `Y = 2`, `X = 2` | gated crying-style write, emit `EF:6BBB` |
| `C2:8CB8` | `Y = 3`, `X = 2` | immobilized/could-not-move-style write, emit `EF:6BD3` |
| `C2:8CF1` | `Y = 4`, `X = 2` | gated solidified-style write, emit `EF:6BEF` |

The extra gates stay intentionally mechanical for now:

- `C2:9F06` tests selected-row `+0x3C` through `C2:6BB8` /
  `RollActionChanceGate`
- `C2:8C69` tests selected-row `+0x39` through `C2:6BB8` /
  `RollActionChanceGate`
- `C2:8CF1` tests through `C2:7C96` / `RollSelectedRowThresholdGate`

## Strange Subgroup `+0x20`

The strange-status bodies converge on `Y = 1`, `X = 3`, writing selected-row
`+0x20 = 1`:

- `C2:8D3A` is a thin wrapper to the resist-checked body at `C2:A056`
- `C2:8DBB` is the direct strange-status sibling without the extra `+0x3B` gate
- `C2:A056` is the resist-checked body that tests selected-row `+0x3B` through
  `C2:6BB8` / `RollActionChanceGate`

Success text is `EF:6C3A`; failure text is `EF:766E`.

## Adjacent PP And Primary-Affliction Body

The mixed `C2:9F57` source unit also contains:

- `C2:9F5E`, a PP-drain body that rolls two small random values plus two, caps
  the drain by selected-row current PP, emits amount-bearing `EF:773F`, reduces
  selected-row PP, and mirrors/clamps the active row
- `C2:9FFE`, a resist-checked primary-affliction body that tests selected-row
  `+0x37`, then writes `+0x1D = 3` through `C2:724A`

The source comments keep the historical wrapper aliases intact while documenting
the byte-level behavior.

## Decomp Value

This slice gives the late action table a concrete status layout:

- `+0x1E` now has two persistent subgroup anchors
- `+0x1F` has asleep, crying, immobilized, and solidified anchors
- `+0x20` has direct and resist-checked strange anchors
- shared no-effect handling through `EF:766E` is explicit across the cluster

## Remaining Soft Spots

- final user-facing names for subgroup `+0x1E` values should stay tied to
  evidence notes until more table entries are joined
- selected-row gate bytes `+0x37/+0x39/+0x3B/+0x3C` still need a broader
  resistance/immunity pass
- `C2:9FFE`'s historical wrapper name and success text remain a naming soft spot
  until the action-table row is rechecked end to end
