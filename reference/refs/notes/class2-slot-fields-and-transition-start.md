# Class2 Slot Fields And Transition Start

This note captures the current ROM-first model for bank `C2` slot fields used by the class-`2` timed transition family.

See also `notes/class2-state-machine-99xx.md`.

## `C2:7550` is a selected-row startup helper for the same family

A direct-call scan found calls to `C2:7550` from:

- `C2:599F`
- `C2:81F0`
- `C2:8259`
- `C2:99D8`
- `C2:9A1E`
- `C2:9A69`
- `C2:A4F1`

That makes it much broader than a one-off branch in the `99xx` cluster.

Current best reading:

- it validates that the current selected row is in a startable phase
- it scans a small candidate table family rooted near `9FAC` through `9FC9`
- on success it clears a block of transient selected-row state
- it sets selected-row byte `+1D` to `1`
- it seeds additional row-local fields such as `+0F`, `+11`, and `+13`
- it emits either the hardcoded collapse script `EF:6C6B` or a descriptor-backed death-style pointer, then later clears row byte `+0x0C`
- it then hands off into the action builder at `C2:4477` and the dispatcher at `C2:4703`

That makes `C2:7550` the current best candidate for a selected-battler collapse or affliction startup helper rather than a generic timed-transition starter.

## Current best field roles

### `+0F`

This byte looks like a subtype or behavior id.

Why that fits:

- `C2:7CFD` treats nonzero `+0F` as a blocker that forces the default text path
- `C2:7550` loads `+0F` from the `983A` table family during a successful start path
- one later branch special-cases `+0F == #$00D5`
- legacy cross-reference around `C2:78B2` shows `+0F == 1` and `+0F == 2` causing distinct behavior

So `+0F` is no longer just an unknown status byte. It behaves like a configured object subtype or mode id.

### `+1D`

This byte no longer reads best as a plain active-transition flag.

Why that fits:

- `C2:7550` sets `+1D = 1` on successful start paths
- several other routines check `+1D == 1` before continuing their work
- the same start path clears other transient fields first, then raises `+1D`

Current best interpretation:

- in this startup path, `+1D = 1` now aligns better with the broader battler affliction or collapse-state family than with a generic active bit
- the strongest current local fit is that value `1` marks the selected battler as unconscious or collapsed while the surrounding controller installs follow-up state
- newer reader-side checks strengthen that correction: several party-level scans treat `1` as the only consistently hard-blocked state, while `1` and `2` are grouped together as a special-handling pair rather than as ordinary active states

### `+1E`

This byte behaves like a phase gate.

Why that fits:

- `C2:7550` requires `+1E == 2` before it will start
- on a successful start, it clears `+1E`

Current best interpretation:

- `+1E` is a pre-start phase or readiness state for the family

### `+1F` through `+23`

These bytes behave like a compact transient-state block.

Why that fits:

- `C2:7550` clears `+1F`, `+20`, `+21`, `+22`, and `+23` together when a transition starts
- the same reset pattern appears again near `C2:7AE0`
- later logic in `C2:941D` and `C2:94CE` gives `+23` a special role as the current timed substate

Current best interpretation:

- `+1F` through `+22` are transient working bytes for the family
- `+23` is the current local timed substate byte layered on top of that block

### `+25`

This byte behaves like the countdown for `+23`.

Why that fits:

- `C2:94CE` decrements `+25` while the family countdown flag is active
- when `+25` reaches zero, `C2:94CE` clears `+23`
- other routines write `+25` when installing state or duration

Current best interpretation:

- `+25` is the remaining duration for the current timed substate in `+23`

### `+38`, `+39`, and `+3A`

These bytes behave like per-object configuration parameters, not generic runtime flags.

Why that fits:

- they are populated from object setup data in the `C2:B820+` loader path
- later logic does not simply toggle them; it tests them through helper comparators such as `C2:8125` and `C2:6BB8`
- if they contain `#$FF`, the family falls back to default message paths in several places

Current best interpretation:

- `+38`, `+39`, and `+3A` are script or setup parameters consumed by the timed transition controller
- at least some of them look threshold-like or duration-like, but the exact gameplay meaning is still open

## What this adds to the family model

Taken together with the `99xx` controller note, the current safest reading is:

- `99DC` selects a per-slot state family, with `1` now the strongest blocked or collapsed value and `1/2` the strongest party-level special-handling pair
- `C2:7550` is now best read as the startup branch that installs one selected battler into a collapse or affliction-handling path for that family
- `+1D` participates in that collapse or affliction state rather than acting like a pure generic active flag
- `+1E` is the pre-start phase gate
- `+1F` through `+23` are the transient working-state bytes, with `+23` as the current timed substate
- `+25` is the countdown for that substate
- `+38`, `+39`, and `+3A` are configured object parameters consulted by the controller

This is enough to stop treating the `99xx` work as a generic black-box state machine. It is now a specific per-slot transition family with a visible start routine and a recognizable field layout.

## Best next target

- See `notes/class2-mask-helper-family.md` for the decoded set-logic layer. The best next move is to map the candidate list rooted at `9FAC` or decode the metadata tables around `9FC9`, so the `4477` / `4703` handoff can be turned into a concrete gameplay name.
