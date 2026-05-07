# Child-Entity Spawn Family (`C4:B3D0`, `C4:0DE8`, `C4:B4xx`)

This note documents the family of routines that spawn and clear attached child entities on top of parent overworld entities, plus the table that drives them.

See also [secondary-visual-descriptor-c42b0d.md](notes/secondary-visual-descriptor-c42b0d.md).
See also [sprite-pose-descriptor-cache-2a06-2cd6.md](notes/sprite-pose-descriptor-cache-2a06-2cd6.md).
See also [visual-frame-selector-update-family-c4-62ff.md](notes/visual-frame-selector-update-family-c4-62ff.md).
See also [overworld-entity-type-registry-9887-98a4.md](notes/overworld-entity-type-registry-9887-98a4.md).

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

This helper takes the placement-type byte in `A` and the parent entity's geometry category in `X`, then adjusts the parent-relative base position before the signed X/Y offsets are applied.

The caller has already seeded the base coordinate scratch words from the parent entity position:

- `$B3F8` = parent base X
- `$B3FA` = parent base Y

`C4:B329` then applies placement-type-specific corrections from the geometry dimension tables `C4:2A1F` and `C4:2A41`:

| placement type | adjustment |
|---|---|
| `1` | `Y -= C4:2A41[geometry] + 8`, then falls through to type `4` |
| `4` | `X -= C4:2A1F[geometry] - 8` |
| `2` | `Y -= C4:2A41[geometry] - 8` |
| `3` | `Y -= C4:2A41[geometry] + 8`, then falls through to type `6` |
| `6` | `X -= C4:2A1F[geometry] + 8` |
| `5` or other | no geometry adjustment |

After this helper returns, `C4:B3D0` applies the child record's signed X/Y bytes on top of the adjusted base. The safest current statement is still: the child attachment point is `parent position`, then geometry-aware anchor adjustment, then signed child offset.

Source polish: `src/c4/landing_child_anchor_spawn_helpers.asm` now names
the placement-adjust modes, `$B3F8/$B3FA` child-anchor pair, the
half-tile footprint adjustment, and the geometry-table driven anchor cases.

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

Source polish: the spawn source now names the live entity status, world
position, footprint selector, attached-parent, and control-word tables, plus
the child-definition placement/X/Y offsets, signed-byte extension masks,
`C01E49` no-parent argument, `#$0311` spawn descriptor, and high-bit
attached-parent tag.

## `C4:B4BE` clear/despawn worker

This looks like the matched cleanup path. It scans active entries for the tagged child-entity state pattern and clears/despawns matching entries.

So the safest current read is: `C4:B4BE` clears previously spawned attached child entities rather than doing general unrelated cleanup.

Source polish: `src/c4/landing_attached_child_lookup_helpers.asm` now names
the `$103E` attached-parent scan table, missing-parent sentinel, high-bit
attached-parent tag, live-slot loop bounds, zero clear value, and the fixed
base-slot/default-child wrapper arguments.

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

The source now routes the resolver-backed spawn wrappers through the named
`C4B3D0_SpawnAttachedChildEntityFromParentSlot` contract instead of the legacy
`SPAWN_FLOATING_SPRITE` label.

The registry-backed pair is stronger than before now that the underlying RAM block is better understood: `C4:608C` is operating over the small `$988B/$9891/$9897/$98A3` overworld type registry, not just an anonymous six-entry list.

So the safest current read is: the engine can attach or clear child entities by several different identity domains, not just one.

The two tiny hard-coded wrappers at `C4:B570` and `C4:B57D` use the same worker pair with parent/live slot `#$0018` and child definition/index `#$0001`. They read like a fixed "base slot" attached-child spawn/clear pair rather than a fourth resolver family.

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

## Working Names

- `C4:B329` = `AdjustChildEntityAnchorForParentGeometry`
- `C4:B3D0` = `SpawnAttachedChildEntityFromParentSlot`
- `C4:B4BE` = `ClearAttachedChildEntitiesByParentSlot`
- `C4:B4FE` = `SpawnAttachedChildForRegistryTypeCode`
- `C4:B519` = `ClearAttachedChildForRegistryTypeCode`
- `C4:B524` = `SpawnAttachedChildForVisualTypeId`
- `C4:B53F` = `ClearAttachedChildForVisualTypeId`
- `C4:B54A` = `SpawnAttachedChildForPoseDescriptorId`
- `C4:B565` = `ClearAttachedChildForPoseDescriptorId`
- `C4:B570` = `SpawnDefaultAttachedChildForBaseSlot18`
- `C4:B57D` = `ClearDefaultAttachedChildForBaseSlot18`

## Best next target

The best next move is to tighten the parent lookup families and the small registry RAM block they use, because that should clarify which gameplay-visible situations choose the `$2C9A`, `$2CD6`, or registry-backed child attach paths.
