# Child-Entity Spawn Family (`C4:B3D0`, `C4:0DE8`, `C4:B4xx`)

This note documents the family of routines that spawn and clear attached child entities on top of parent overworld entities, plus the table that drives them.

See also [secondary-visual-descriptor-c42b0d.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/secondary-visual-descriptor-c42b0d.md).
See also [sprite-pose-descriptor-cache-2a06-2cd6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/sprite-pose-descriptor-cache-2a06-2cd6.md).
See also [visual-frame-selector-update-family-c4-62ff.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/visual-frame-selector-update-family-c4-62ff.md).
See also [overworld-entity-type-registry-9887-98a4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/overworld-entity-type-registry-9887-98a4.md).

## Main result

A distinct child-entity subsystem is now visible.

The strongest local anchors are:

- `C4:B3D0` = spawn-side worker
- `C4:B4BE` = clear/despawn-side worker
- `C4:0DE8` = compact child-entity definition table
- `C4:B4FE/B519`, `C4:B524/B53F`, and `C4:B54A/B565` = resolver-backed spawn/clear pairs

The safest current read is: the game can spawn small attached child entities relative to a parent entity's world position, then later clear them through matched helper pairs.

## `C4:0DE8` child-entity table

The current best local read is a stride-5 table.

Each record currently looks like:

| offset | field | current read |
|---|---|---|
| `+0..+1` | word | child pose-descriptor index |
| `+2` | byte | placement-adjust type |
| `+3` | byte | signed X offset |
| `+4` | byte | signed Y offset |

The sign-extension for bytes `+3` and `+4` is explicit in the spawn logic, so the signed-offset part is on solid local footing.

## `C4:B329` placement-adjust helper

This helper takes the placement-type byte and the parent entity's geometry category, then adjusts the parent-relative base position before the signed X/Y offsets are applied.

The safest current statement is:

- the child attachment point is not just `parent position + raw offset`
- it is `parent position`, then geometry-aware adjustment, then signed child offset

That fits the broader sprite-pose/geometry-family work well.

## `C4:B3D0` spawn worker

The locally strongest flow is:

1. reject invalid selector values early
2. resolve parent-side geometry and position state
3. read a child definition from `C4:0DE8`
4. compute child world position from parent position plus placement-adjusted signed offsets
5. call `C01E49` to initialize the child entity
6. mark the child with a high-bit state tag in `$103E`
7. copy some display-state from the parent into the child

So the safest current read is: `C4:B3D0` spawns a child entity that inherits some visual state from its parent and is positioned relative to that parent in world space.

## `C4:B4BE` clear/despawn worker

This looks like the matched cleanup path. It scans active entries for the tagged child-entity state pattern and clears/despawns matching entries.

So the safest current read is: `C4:B4BE` clears previously spawned attached child entities rather than doing general unrelated cleanup.

## Resolver-backed caller pairs

Three paired families are now visible:

| spawn | clear | resolver used |
|---|---|---|
| `C4:B4FE` | `C4:B519` | overworld type-registry resolver |
| `C4:B524` | `C4:B53F` | `$2C9A` match resolver |
| `C4:B54A` | `C4:B565` | `$2CD6` match resolver |

The pattern is consistent:

- spawn variant resolves a parent entity, then calls `C4:B3D0`
- clear variant resolves the same family, then calls `C4:B4BE`

The registry-backed pair is stronger than before now that the underlying RAM block is better understood: `C4:608C` is operating over the small `$988B/$9891/$9897/$98A3` overworld type registry, not just an anonymous six-entry list.

So the safest current read is: the engine can attach or clear child entities by several different identity domains, not just one.

## `$2C9A` vs `$2CD6`

The distinction that matters here is:

- `$2CD6` looks like the cached pose-table index
- `$2C9A` looks like a caller-assigned visual-type or effect-type id

That means the child-entity system can look up parents either by pose identity or by a higher-level caller-defined visual identity.

## What still remains open

- the exact meaning of the auxiliary table read near the front of `C4:B3D0`
- whether `C4:0DE8` is the only child-entity definition table in this subsystem
- the exact symbolic name of the high-bit state tag written into `$103E`
- the exact semantic name of the registry family used by the `B4FE/B519` pair

## Best next target

The best next move is to tighten the parent lookup families and the small registry RAM block they use, because that should clarify which gameplay-visible situations choose the `$2C9A`, `$2CD6`, or registry-backed child attach paths.
