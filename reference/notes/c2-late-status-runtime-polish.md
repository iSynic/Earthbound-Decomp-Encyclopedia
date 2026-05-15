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

## Phase 2 Caller Matrix Slice

This note owns the late-status portion of the Phase 2 `C2:724A` trace oracle.
Each row should be captured as caller, selected row source, `X` subgroup slot,
`Y` value, chance/resistance gate, and EF text result.

Current locally pinned rows:

| Lane | Caller | X slot | Y | Gate before writer | EF text result |
| --- | --- | --- | --- | --- | --- |
| persistent status | `C2:8BBE` | `1 -> +0x1E` | `1` | default target blocker | `EF:6B81` / `EF:766E` |
| persistent status | `C2:8BFD` | `1 -> +0x1E` | `2` | default target blocker plus row `+0x0E` check | `EF:6B98` / `EF:766E` |
| asleep PSI status | `C2:9F06` | `2 -> +0x1F` | `1` | selected-row `+0x3C` through `C2:6BB8` | `EF:6C55` / `EF:766E` |
| crying status | `C2:8C69` | `2 -> +0x1F` | `2` | selected-row `+0x39` through `C2:6BB8` | `EF:6BBB` / `EF:766E` |
| immobilized status | `C2:8CB8` | `2 -> +0x1F` | `3` | default target blocker | `EF:6BD3` / `EF:766E` |
| solidification | `C2:8CF1` | `2 -> +0x1F` | `4` | `C2:7C96` threshold gate | `EF:6BEF` / `EF:766E` |
| strange PSI status | `C2:A056` | `3 -> +0x20` | `1` | selected-row `+0x3B` through `C2:6BB8` | `EF:6C3A` / `EF:766E` |
| paralysis PSI status | `C2:9FFE` | `0 -> +0x1D` | `3` | selected-row `+0x37` through `C2:6BB8` | `EF:6AE0` / `EF:766E` |

The resist-checked PSI status trio is the trace priority inside this slice:
`C2:9F06`, `C2:9FFE`, and `C2:A056` look like one host-gate shape with distinct
payload outcomes. That grouping is locally plausible from the gate/helper/text
shape, while any stronger C-port-facing name should wait for traces that record
the selected row source and gate result for each caller.

Item-side statuses and concentration seal stay linked to this lane through the
shared affliction/status contract, but their focused runtime notes own the
item-side selected-row provenance. In particular, concentration seal writes
`+0x21 = 4` directly and is not a `724A` caller.

## Remaining Soft Spots

- final user-facing names for subgroup `+0x1E` values should stay tied to
  evidence notes until more table entries are joined
- selected-row gate bytes `+0x37/+0x39/+0x3B/+0x3C` still need a broader
  resistance/immunity pass
- `C2:9FFE`'s historical wrapper name and success text remain a naming soft spot
  until the action-table row is rechecked end to end
