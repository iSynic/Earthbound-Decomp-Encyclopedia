# Pathfinding frontier lead-in (`C0:B9BC-C0:BA35`)

## Scope

`C0:B9BC` and `C0:BA35` are the first two unknown entries immediately before
the ebsrc `misc/find_path_to_party.asm` include. Together they prepare the
small coordinate/candidate buffers that feed the later path-to-party solver.

The routines operate in 64x64 tile space and reuse the same coordinate
conversion tables seen elsewhere in movement/entity logic:
`C4:2A1F`, `C4:2A41`, `C4:2AA7`, `C4:2AC9`, and `C4:2AEB`.

## Working Names

- `C0:B9BC` = `SnapshotPartyPositionsToPathGridRecords`
- `C0:BA35` = `BuildPathfindingOccupancyAndCandidateBuffers`

## `C0:B9BC`: normalize party/entity positions into caller records

`C0:B9BC` takes a caller record base in A, a count in X, and a Y tile offset
in Y. It also reads an X tile offset from caller DP `$26`.

For each index below the count:

- Uses `$9897[index]` to find an entity/party slot.
- Reads that slot's direction/pose selector from `$2B6E`.
- Converts `$0B8E/$0BCA` position fields through C4 coordinate tables.
- Shifts the results down by three, subtracts the caller X/Y tile offsets,
  wraps with `& $003F`, and stores the pair into the caller records at
  base + index * 4:
  - `base+$7E` receives one wrapped coordinate.
  - `base+$7C` receives the other wrapped coordinate.

This is a compact "snapshot live entity positions into 64x64 path-grid
coordinates" helper.

## `C0:BA35`: build occupancy/candidate buffers and call the path solver

`C0:BA35` is the heavier setup routine. It reserves a large local DP frame,
copies caller parameters, and uses `$7F3000` as a temporary occupancy grid.

The first pass fills the grid:

- The caller record at base + `$78/$7A` supplies width/height.
- For each wrapped tile inside that rectangle, it samples the current
  collision page at `$E000`.
- Collision bytes with high bits `$C0` become `$FD` in `$7F3000`; clear
  cells become `$00`.

The second pass scans up to 30 entity slots:

- Skips slots whose `$0A62` entry is `$FFFF`.
- Skips slots whose `$2C5E` state is not `$FFFF`.
- Converts each accepted slot's `$0B8E/$0BCA` position into wrapped grid
  coordinates, using the same C4 coordinate tables as `C0:B9BC`.
- Builds 10-byte candidate records under caller base + `$A0`, including the
  entity index, slot-derived C4 offsets, and wrapped X/Y coordinates.
- Stores the number of accepted candidates at caller base + `$9E`.

Then it calls the C4 solver layer:

- Prepares `$0E/$10 = $7F3000`, step size `4`, candidate arrays at caller
  base + `$7C` and `$A0`, and the caller-supplied target fields.
- Calls `C4:B59F` followed by repeated `C4:B595` until the solver reports a
  terminal result.
- If no path is found, marks all live slots in `$2C5E` with `1`.
- If a path is found, writes per-entity path outputs into `$2E02` and `$2E3E`
  for candidates that received a result; candidates without a result are
  marked in `$2C5E`.

## Practical decomp notes

This is the beginning of a portable pathfinding subsystem:

- `C0:B9BC` is a position snapshot/conversion pass.
- `C0:BA35` is a grid builder plus candidate extraction pass.
- The deeper route search appears to live in the named `FIND_PATH_TO_PARTY`
  region and C4 helpers `B59F/B595`.

The open work is to finish naming the caller record layout (`+$78`, `+$7A`,
`+$9C`, `+$9E`, `+$A0` and friends) and to connect the `$2E02/$2E3E` outputs
to the movement consumer that applies the returned path steps.

## C4 solver layer refinement

The `C4:B587..C05E` block is the lower-level grid solver layer used by the `C0:BA35` setup path. The names below are intentionally mechanical: they describe the byte-level role without pretending the whole route-search policy is fully solved.

- `C4:B587` advances the path-solver scratch cursor at `$B43A` by the caller's size and returns the previous cursor.
- `C4:B595` reports scratch usage as `$B43A - $B438`; the `C0:BA35` caller polls this until it reaches or exceeds the supplied `$0C00` cap.
- `C4:B59F` initializes the solver state, builds per-candidate group data, and returns the count of candidates with usable path output.
- `C4:B7A5` writes `$FD` into the outer rows/columns of the scratch grid, giving the solver a blocked border.
- `C4:B859` builds and sorts a list of candidate-record pointers by the record coordinate words at `+2/+4`.
- `C4:B923`, `C4:BAF6`, `C4:BD9A`, and `C4:BF7F` are the internal marking, propagation, route-tracing, and path-compaction stages. Their exact contracts still need a dedicated pass, but the local call graph and scratch-array traffic are now bounded.

The source scaffold now promotes eight byte-equivalent C4 solver support slices:

- `src/c4/path_solver_scratch_helpers.asm` covers `C4:B587..B59F`.
- `src/c4/path_solver_orchestration_helpers.asm` covers `C4:B59F..B7A5`.
- `src/c4/path_solver_grid_border_helpers.asm` covers `C4:B7A5..B859`.
- `src/c4/path_solver_candidate_sort_helpers.asm` covers `C4:B859..B923`.
- `src/c4/path_solver_candidate_mark_helpers.asm` covers `C4:B923..BAF6`.
- `src/c4/path_solver_route_propagation_helpers.asm` covers `C4:BAF6..BD9A`.
- `src/c4/path_solver_route_trace_helpers.asm` covers `C4:BD9A..BF7F`.
- `src/c4/path_solver_step_compaction_helpers.asm` covers `C4:BF7F..C05E`.

The lower-level C4 path-solver support corridor is now source-promoted end to
end for this phase. Remaining work is semantic tightening: name the caller
record fields and scratch-state words more explicitly, then connect the
returned step-list records to the C0 movement consumer.

## C4 Solver Working Names

- `C4:B587` = `AllocPathSolverScratchWords`
- `C4:B595` = `GetPathSolverScratchUsage`
- `C4:B59F` = `RunPathGridCandidateSolver`
- `C4:B7A5` = `MarkPathGridBorderBlocked`
- `C4:B859` = `SortPathCandidatePointersByGridPosition`
- `C4:B923` = `MarkPathCandidateFootprintsInGrid`
- `C4:BAF6` = `PropagatePathGridCandidateRoutes`
- `C4:BD9A` = `TracePathGridRouteIntoStepList`
- `C4:BF7F` = `CompressCollinearPathStepList`
