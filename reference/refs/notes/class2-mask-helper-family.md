# Class2 Mask Helper Family

This note captures the current ROM-first model for the bitmask helper cluster used by the class-`2` timed transition family.

See also `notes/class2-handoff-4477-4703.md`.

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

### `C2:6E77` -> subtract a family of bits from the working set

Behavior:

- iterates over the 32 candidate slots rooted at `9FAC`
- for each slot with nonzero `+0C` and nonzero `+0F`, loads the one-hot mask for that candidate index
- inverts that mask
- ANDs it into `$A96C/$A96E`

So this is not a generic intersection helper. It is a set-subtraction pass that removes a family of occupied or blocked candidate bits from the current working set.

Current best working name:

- `MaskSet_RemoveActiveTypedCandidates`

### `C2:6BFB` -> build a union of active typed candidates

Behavior:

- clears `$A96C/$A96E`
- iterates the same 32 candidate slots rooted at `9FAC`
- for each slot with nonzero `+0C`, nonzero `+0E`, and nonzero `+0F`, ORs in the candidate bit

Current best working name:

- `MaskSet_BuildActiveTypedCandidates`

### `C2:6C82` -> build a union of phase-1 candidates

Behavior:

- clears `$A96C/$A96E`
- iterates the 32 candidate slots rooted at `9FAC`
- for each slot with nonzero `+0C` and `+0E == 1`, ORs in the candidate bit

Current best working name:

- `MaskSet_BuildPhase1Candidates`

## Higher-level helper roles

### `C2:70E4`

This routine iterates candidate indices `0..31`, tests each bit with `C2:7029`, and for matching candidates checks metadata at `9FC9`.

When that metadata byte is `1`, it clears the bit through `C2:7089`.

Current best reading:

- this is a metadata-based pruning pass over the working set

Current best working name:

- `MaskSet_PruneFlaggedCandidates`

### `C2:6EF8`

This routine takes a candidate range in `$24/$26`, walks bit indices, intersects each with the working set, and returns the first matching index through `$1C/$1E`.

Current best reading:

- it finds the first surviving candidate inside a requested range

Current best working name:

- `MaskSet_FindFirstMatchInRange`

## What this says about the class-`2` family

The family is now much more concrete:

- `C2:4477` derives a compact action code and parameter
- `C2:4703` dispatches into a helper family that builds and filters a 32-bit candidate set
- the candidate set is represented by `$A96C/$A96E`
- candidates are addressed by one-hot bits from `C4:A279`
- multiple passes build unions, subtract blocked candidates, test membership, and prune metadata-marked candidates

This strongly suggests the family is selecting from a bounded 32-entry neighborhood, candidate list, or adjacency graph rather than merely toggling a timer or message branch.

## Candidate-domain note

See `notes/class2-candidate-table-9fac.md` for the current WRAM candidate-pool model. The strongest new gain there is that the domain is backed by live runtime entries with parallel fields like `9FB8`, `9FBA`, `9FBB`, `9FBC`, `9FBF`, and `9FC9`, not just anonymous bits.

## Remaining unknowns

- what the 32 candidate entries rooted near `9FAC` represent in gameplay terms
- what linked value is stored in the candidate-side arrays mapped through selector `#$005F`
- whether the domain is best interpreted as neighboring tiles, nearby nodes, exits, or local object links

## Best next target

- See `notes/class2-candidate-population-and-ranking.md` for the current setup-versus-ranking split. The best next move is to trace where the source values in the `986F` family come from, or decode the linked candidate-side bytes near `9FAE` and `9FF0`, so the 32-bit domain can be named from actual gameplay structure rather than just bitset behavior.
