# Class2 Handoff 4477 4703

This note captures the current ROM-first model for the handoff after `C2:7550`, centered on `C2:4477` and `C2:4703`.

See also `notes/class2-slot-fields-and-transition-start.md`.

## Working Names

- `C2:4477` = `BuildClass2DerivedActionCode`
- `C2:4703` = `DispatchClass2DerivedAction`

## `C2:4477` behaves like an action-code builder

Direct callers found so far:

- `C2:54D1`
- `C2:59D5`
- `C2:5A40`
- `C2:7937`

Current best reading:

- it takes a slot pointer or slot base in `A`
- it probes two local candidate lists rooted at `AD7A` and `AD82` through `C4:A1F5`
- it consults the slot's type data through the `D5:7B68` table family
- from that combination, it writes a small action code to slot byte `+09`
- it also writes a small action parameter to slot byte `+0A`

The important result is structural: this routine is deriving a compact action description for the slot, not directly performing the behavior itself.

## `+09` and `+0A` are now meaningfully constrained

### `+09`

This byte behaves like a derived action code.

Why that fits:

- `C2:4477` writes it after probing candidate lists and slot type data
- `C2:4703` immediately dispatches on it as a multi-way branch
- observed branch cases include `1`, `2`, `4`, `11`, `12`, and `14`

Current best interpretation:

- `+09` is the current action or behavior code selected for the active slot

### `+0A`

This byte behaves like a per-action parameter or index.

Why that fits:

- `C2:4477` writes it alongside `+09`
- `C2:4703` consumes it in several branches, sometimes decrementing it before calling the next helper
- one branch compares `+0A` against local counts and uses it to index `AD7A` or `AD82`

Current best interpretation:

- `+0A` is a small parameter, index, or count attached to the derived action code in `+09`

## `C2:4703` is the behavior dispatcher for that derived action

Direct callers found so far:

- `C2:59F5`
- `C2:5A47`
- `C2:793E`

Current best reading:

- it clears the working mask pair at `$A96C/$A96E`
- it branches on slot byte `+09`
- each branch routes into a helper cluster such as `C2:6FDC`, `C2:6BFB`, `C2:6D04`, `C2:6C82`, `C2:6E77`, `C2:7029`, or `C2:416F`
- several branches also consume slot byte `+0A`

That makes `C2:4703` the current best candidate for `Dispatch_Class2DerivedAction` or similar.

## The downstream helper family is bitmask-oriented

The strongest new concrete clue is that the helpers reached from `C2:4703` operate on a two-word working pair at `$A96C/$A96E`.

Current best reading:

- `C2:6E77` removes a family of active typed candidate bits from `$A96C/$A96E`
- `C2:6FDC` loads a one-hot mask from `C4:A279` and ORs it into `$A96C/$A96E`
- `C2:7029` tests whether a selected bit is present in the working set
- `C2:7089` clears a selected bit from the working set

This is strong evidence that the post-`7550` behavior is set-membership or spatial-mask driven, not just plain dialogue timing.

## What this adds to the family model

The current safest interpretation is:

- `C2:7550` starts or primes the family for a slot
- `C2:4477` derives a compact action code in `+09` and parameter in `+0A`
- `C2:4703` dispatches that action into a bitmask-based helper family
- the bitmask helpers build and filter a 32-bit candidate set through `$A96C/$A96E`
- so this timed class-`2` family appears to be solving some local membership or adjacency problem before choosing its visible outcome

That still does not give us the final gameplay name, but it is enough to say the family is not just a generic text or timer script.

## Best next target

- See `notes/class2-mask-helper-family.md` and `notes/class2-candidate-table-9fac.md` for the current bitset and candidate-pool model. The best next move is to trace the setup path that first populates `9FB8..9FC9`, or decode the ranking fields around `9FF0`, `AD5A`, `AD62`, and `AD7A`, so the 32-entry domain can be named from actual gameplay structure.
