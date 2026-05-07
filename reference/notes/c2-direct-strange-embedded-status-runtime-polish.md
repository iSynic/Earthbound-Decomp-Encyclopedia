# C2 Direct Strange Embedded Status Runtime Polish

This note records the byte-neutral polish slice for the mixed source corridor at
`C2:8DBB..8E42`.

Primary source module:

- `src/c2/c2_8dbb_run_direct_strange_status_action.asm`

Related evidence notes:

- `notes/class2-strange-status-family-c28d3a-c28dbb-c2a056.md`
- `notes/class2-temporary-status-action-cluster-c28c69-c28cb8-c28cf1.md`
- `notes/c2-late-status-runtime-polish.md`
- `notes/c2-asleep-status-runtime-polish.md`

## Embedded Bodies

The corridor contains three action-table targets:

| Address | Promoted local role | Runtime effect |
| --- | --- | --- |
| `C2:8DBB` | direct strange status | `+0x20 = 1`, `EF:6C3A` |
| `C2:8DFC` | all-target crying status | `+0x1F = 2`, `EF:6BBB` |
| `C2:8E3B` | asleep far wrapper | redirects to `C2:9F06` |

The first two bodies share the generic status-writer ABI: A is the selected row,
X selects the subgroup offset relative to `+0x1D`, and Y is the status value.

## Why This Helps

Before this slice, `C2:8DFC` and `C2:8E3B` were visible as raw embedded tails
inside the direct-strange source unit. They are now explicit labels:

- `C28DFC_RunAllTargetCryingStatusAction`
- `C28E3B_RunAsleepStatusFarWrapperAction`

That makes the late temporary-status crosswalk easier to follow: one-target
crying is at `C2:8C69`, all-target crying is at `C2:8DFC`, and the all-target
asleep wrapper joins the same asleep body later documented at `C2:9F06`.

## Remaining Soft Spots

- The exact action-table names for the all-target crying and asleep wrapper rows
  should wait for row-by-row `D5:7B68` promotion.
- This slice labels the embedded bodies but keeps the surrounding generated file
  boundary intact.
