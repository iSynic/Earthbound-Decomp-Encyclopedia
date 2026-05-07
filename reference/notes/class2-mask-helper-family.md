# Class2 Mask Helper Family

This note captures the current ROM-first model for the bitmask helper cluster used by the class-`2` timed transition family.

See also `notes/class2-handoff-4477-4703.md`.

## Working Names

- `C2:6BFB` = `MaskSet_BuildActiveTypedBattlers`
- `C2:6C82` = `MaskSet_BuildEnemySideBattlers`
- `C2:6E00` = `MaskSet_BuildActiveBattlers`
- `C2:6E77` = `MaskSet_RemoveActiveNpcBattlers`
- `C2:6EF8` = `MaskSet_FindFirstMatchInRange`
- `C2:6FDC` = `MaskSet_AddBit`
- `C2:7029` = `MaskSet_TestBit`
- `C2:7089` = `MaskSet_ClearBit`
- `C2:70E4` = `MaskSet_PruneAfflictionFlaggedBattlers`

## `C4:A279` is a 32-entry one-hot bitmask table

The table at `C4:A279` is not arbitrary data. It is a 32-entry table of 32-bit one-hot masks:

- entry `0` -> `00000001`
- entry `1` -> `00000002`
- entry `2` -> `00000004`
- ...
- entry `31` -> `80000000`

That means the helper family is operating on a 32-slot set represented by the working pair `$A96C/$A96E`.

## Core working pair

Current best reading:

- `$A96C/$A96E` is a 32-bit working set for the current class-`2` resolution step
- helper routines build, intersect, clear, and test bits in that set

This is much stronger than the earlier generic "bitmask-oriented" description. The family is doing explicit set algebra over a 32-element domain.

Implementation update: the promoted source modules now carry this vocabulary
directly. `src/c2/c2_6bfb_mask_set_build_active_typed_candidates.asm`,
`src/c2/c2_6c82_mask_set_build_phase1_candidates.asm`,
`src/c2/c2_6e77_mask_set_remove_active_typed_candidates.asm`,
`src/c2/c2_6fdc_mask_set_add_bit.asm`,
`src/c2/c2_7029_mask_set_test_bit.asm`, and
`src/c2/c2_7089_mask_set_clear_bit.asm` name the `C4:A279` one-hot table,
`$A96C/$A96E` current target mask, `$9FAC` battler rows, and the shared
`0x4E` row stride at their local use sites.

Follow-up implementation update: `src/c2/c2_6ef8_mask_set_find_first_match_in_range.asm`
and `src/c2/c2_70e4_mask_set_prune_flagged_candidates.asm` now use the same
one-hot table, bit-index, battler-row stride, and target-set helper names.
That closes the currently documented `C2:6BFB..70E4` mask helper family for
source-facing vocabulary.

Random-start follow-up: `C2:6EF8` now calls the local `C2:69EF` random helper
as `GetRandomByte` before masking the low five bits for its target-bit retry
count. That keeps `MaskSet_FindFirstMatchInRange` tied to a randomized scan
start rather than reading as a fixed first-set-bit walker.

Second follow-up update: the source modules above now reserve "candidate" for
the ranked front/back selection lists where it is still useful. The `$9FAC`
domain itself is named as `BattlersTableBase` / `BattlerRowSize`, with field
names such as `consciousness`, `ally_or_enemy`, `npc_id`, `row`, and
`afflictions` replacing the older generic row/metadata wording.

Third follow-up update: the embedded `C2:6E00` helper inside
`src/c2/c2_6c82_mask_set_build_phase1_candidates.asm` now has its own source
label as `MaskSet_BuildActiveBattlers`. It builds the current target mask
from every conscious battler row, and the A89D item/status payload tail now
uses that named helper plus the named `6BFB/6C82/6E77/6EF8/70E4` mask helpers.

Fourth follow-up update: the source-facing helper aliases now use the battler
domain names directly while keeping the older candidate-style aliases as
compatibility labels. `6C82` is named for the enemy-side battler union,
`6E77` for active NPC battler removal, `6E00` for all active battlers, and
`70E4` for affliction-flagged battler pruning. Dispatch, target text-context,
Thunder, normalization, and A89D payload-tail consumers now call those
contracts instead of the inherited `TARGET_*`/candidate labels.

## Confirmed helper roles

### `C2:6FDC` -> add one bit to the working set

Input:

- `A` = bit index `0..31`

Behavior:

- loads one-hot mask `1 << A` from `C4:A279`
- ORs that mask into `$A96C/$A96E`
- stores the updated working set back

Current best working name:

- `MaskSet_AddBit`

### `C2:7029` -> test whether one bit is present in the working set

Input:

- `A` = bit index `0..31`

Behavior:

- loads one-hot mask `1 << A` from `C4:A279`
- ANDs it with `$A96C/$A96E`
- returns `1` if the intersection is nonzero, else `0`

Direct callers found include `C2:3E60`, `40D1`, `4126`, `419C`, `5C8D`, `70F4`, `8973`, `9684`, and `973A`.

Current best working name:

- `MaskSet_TestBit`

### `C2:7089` -> clear one bit from the working set

Input:

- `A` = bit index `0..31`

Behavior:

- loads one-hot mask `1 << A` from `C4:A279`
- inverts it
- ANDs the inverse with `$A96C/$A96E`
- stores the updated working set back

Direct callers found so far: `C2:41CC` and `C2:7116`.

Current best working name:

- `MaskSet_ClearBit`

### `C2:6E77` -> subtract a family of battler bits from the working set

Behavior:

- iterates over the 32 battler slots rooted at `9FAC`
- for each slot with nonzero `consciousness` (`+0x0C`) and nonzero `npc_id` (`+0x0F`), loads the one-hot mask for that battler index
- inverts that mask
- ANDs it into `$A96C/$A96E`

So this is not a generic intersection helper. It is a set-subtraction pass that removes a family of occupied or blocked battler bits from the current working set.

Current best working name:

- `MaskSet_RemoveActiveNpcBattlers`

### `C2:6BFB` -> build a union of active typed battlers

Behavior:

- clears `$A96C/$A96E`
- iterates the same 32 battler slots rooted at `9FAC`
- for each slot with nonzero `consciousness` (`+0x0C`), nonzero `ally_or_enemy` (`+0x0E`), and nonzero `npc_id` (`+0x0F`), ORs in the battler bit

Current best working name:

- `MaskSet_BuildActiveTypedBattlers`

### `C2:6C82` -> build a union of enemy-side battlers

Behavior:

- clears `$A96C/$A96E`
- iterates the 32 battler slots rooted at `9FAC`
- for each slot with nonzero `consciousness` (`+0x0C`) and `ally_or_enemy == 1` (`+0x0E`), ORs in the battler bit

Current best working name:

- `MaskSet_BuildEnemySideBattlers`

### `C2:6E00` -> build a union of all active battlers

Behavior:

- clears `$A96C/$A96E`
- iterates the 32 battler slots rooted at `9FAC`
- for each slot with nonzero `consciousness` (`+0x0C`), ORs in the battler bit

Current best working name:

- `MaskSet_BuildActiveBattlers`

## Higher-level helper roles

### `C2:70E4`

This routine iterates target bits `0..31`, tests each bit with `C2:7029`, and for matching battlers checks the affliction byte at `9FC9`.

When that metadata byte is `1`, it clears the bit through `C2:7089`.

Current best reading:

- this is a metadata-based pruning pass over the working set

Current best working name:

- `MaskSet_PruneAfflictionFlaggedBattlers`

### `C2:6EF8`

This routine takes an input mask in `$24/$26`, walks target bit indices, intersects each with the working set, and returns the first matching one-hot bit through `$1C/$1E`.
It seeds the scan from `C2:69EF` / `GetRandomByte`, masks the low five bits,
and then wraps through the 32-bit target domain until a requested bit survives.

Current best reading:

- it finds the first surviving target bit inside a requested mask

Current best working name:

- `MaskSet_FindFirstMatchInRange`

## What this says about the class-`2` family

The family is now much more concrete:

- `C2:4477` derives a compact action code and parameter
- `C2:4703` dispatches into a helper family that builds and filters a 32-bit target set
- the target set is represented by `$A96C/$A96E`
- battlers are addressed by one-hot bits from `C4:A279`
- multiple passes build unions, subtract blocked battlers, test membership, and prune affliction-marked battlers

This now lines up with the broader `BATTLERS_TABLE` correction: the mask family is selecting and pruning battlers, not an abstract adjacency graph.

## Battler-domain note

See `notes/class2-battlers-table-layout-9f8a-9fac.md` for the corrected WRAM
model. The strongest new gain is that the domain is the live `BATTLERS_TABLE`:
addresses like `9FB8`, `9FBA`, `9FBB`, `9FBC`, and `9FC9` are battler-field
offsets (`consciousness`, `ally_or_enemy`, `npc_id`, `row`, and `afflictions`),
not anonymous parallel candidate arrays.

## Remaining unknowns

- whether the source file names should eventually follow the newer battler
  aliases, or remain as stable scaffold-era filenames with compatibility
  labels inside the files
- the exact gameplay enum names for the action-targeting modes that feed these
  battler-mask builders
- whether every `+0x1D`/`9FC9` pruning use should be described as a specific
  affliction group or kept as a broad affliction/state byte

## Best next target

- See `notes/class2-battlers-table-layout-9f8a-9fac.md` for the corrected
  battler-table model. The best next move is to trace another `C2:B6EB` caller
  family or to continue retiring stale candidate wording in the second-stage
  selector docs now that the mask helper source is aligned.
