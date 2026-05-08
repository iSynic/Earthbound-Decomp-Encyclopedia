# Class2 Late Stat And Resource Family C28E42 C29E38

This note captures the strongest current local model for the late `D5:7B68` action-entry cluster around `C2:8E42`, `C2:8EAE`, `C2:8F21`, and `C2:9E38`.

See also [class2-d57b68-battle-action-table-match.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-d57b68-battle-action-table-match.md).
See also [class2-d57b68-early-entry-name-crosswalk.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-d57b68-early-entry-name-crosswalk.md).
See also [class2-second-pointer-consumer-40a4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-second-pointer-consumer-40a4.md).
See also [class2-battle-text-cluster-overview.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battle-text-cluster-overview.md).

## Main result

This slice of the late action table is no longer best treated as a grab bag of anonymous non-status tails.

The current safest local split is:

- `C2:8E42` = PP-reduction or PP-sapping action
- `C2:8EAE` = guts-cutting action
- `C2:8F21` = paired offense-and-defense reduction action
- `C2:9E38` = strongest current local fit for `DEFENSE_SPRAY`
- `C2:9E7F` = strongest current local fit for `DEFENSE_SHOWER`

All four bodies are real gameplay-side mutators, not presentation-only helpers. They gate targets through the same battle-side success checks, mutate live battler fields, and then print the resulting amount deltas through `C1:DC66`.

## Why this family holds together

The bodies are structurally parallel in three ways:

- they enter as live second-pointer targets from `D5:7B68`
- they use the ordinary success or eligibility path through `C2:7CFD`
- they display the resulting amount through `C1:DC66`, which is now our best local battle-text wrapper for amount-bearing action messages

That makes them a useful late-table numeric-effect family parallel to the already-mapped late-table affliction families.

## `C2:8E42` is the PP-reduction side

`C2:8E42` is still the softest member of the group, but it is no longer vague.

Current strongest local read:

- gates on target battler `pp_target` at row `+0x19`
- if that field is zero, fails through the ordinary no-effect path
- otherwise reads the high nibble of battler `pp_max` at row `+0x1B`
- runs that value through `C2:6A44` to get the action amount
- passes the target row plus that amount into `C2:721D`
- then displays `EF:7755`, the `PRINT_ACTION_AMOUNT PP!` loss text family, through `C1:DC66`

`C2:721D` is a useful local anchor here. Its body behaves like a capped resource reducer over battler row `+0x19`: if the requested reduction exceeds the current value, it clamps to zero before handing the final amount into `C2:7191`.

That makes the safest current interpretation:

- `C2:8E42` is a single-target PP-reduction or PP-sapping action

The strongest current reference-backed candidate is `BTLACT_REDUCEPP`, but I am keeping that one notch cautious because the exact amount source still rests partly on reader-side field naming plus the side reference.

## `C2:8EAE` is the guts-cutting side

`C2:8EAE` is now much healthier locally.

Current strongest read:

- gates through `C2:7CFD`
- snapshots target battler `guts` at row `+0x2C`
- reduces current guts to roughly three quarters of its prior value
- reads base battler `base_guts` at row `+0x35`
- computes a lower clamp from that base value
- prevents the new guts value from dropping below that clamp
- prints the resulting delta through `C1:DC66` with `C8:F7EE`

That is a strong local fit for a guts-cutting action rather than a generic stat debuff. The strongest current reference-backed candidate is `BTLACT_CUTGUTS`.

## `C2:8F21` is the paired offense and defense reduction side

`C2:8F21` now has the cleanest local identity in the group.

The body does the same two-step pattern twice:

- snapshot target battler `offense` at row `+0x26`
- run `C2:7DDC`
- print the delta through `C1:DC66` with `C8:F885`

then:

- snapshot target battler `defense` at row `+0x28`
- run `C2:7E33`
- print the delta through `C1:DC66` with `C8:F8A2`

That makes the safest local name a paired offense-and-defense reduction action. The strongest current reference-backed candidate is `BTLACT_REDUCEOFFDEF`.

## `C2:9E38` is the defense-increase side

`C2:9E38` is also in good shape now.

Current strongest read:

- gates through `C2:7CFD`
- snapshots target battler `defense` at row `+0x28`
- runs `C2:7D28`
- prints the positive delta through `C1:DC66` with `C8:F77D`

The nearby `C2:9E7F` is a trivial all-target wrapper that immediately `JSL`s `C2:9E38` and returns.

That split now matches the action-table metadata unusually well:

- entry `48` -> `C2:9E38` -> one-target PSI action
- entry `49` -> `C2:9E7F` -> all-target PSI action

Together with the reference action files, that is strong enough to promote the current best fits to `BTLACT_DEFENSE_SPRAY` for `C2:9E38` and `BTLACT_DEFENSE_SHOWER` for `C2:9E7F`.

## Field-level bridge to battler state

The current battler-field bridge for this family is:

- row `+0x19` = `pp_target`
- row `+0x1B` = `pp_max`
- row `+0x26` = `offense`
- row `+0x28` = `defense`
- row `+0x2C` = `guts`
- row `+0x35` = `base_guts`

That matters because this cluster is no longer resting just on message-text vibes. The bodies line up with specific battler fields and mutate them in ways that fit the corresponding amount texts.

## Action-table anchors

The current useful anchors from `D5:7B68` are:

- entry `95` -> `C2:8E42` -> one-target `other` PP-reduction family
- entry `48` -> `C2:9E38` -> one-target defense-up family
- entry `49` -> `C2:9E7F` -> all-target defense-up family
- entry `96` -> `C2:9E38` -> defense-up family
- entry `97` -> `C2:8EAE` -> guts-cutting family
- entry `98` -> `C2:8F21` -> paired offense-and-defense reduction family

There are also later reuses:

- entries `233` and `234` reuse `C2:8F21`
- `C2:9E7F` is a wrapper reuse of the `9E38` defense-up body

## Current safest interpretation

The safest current interpretation is:

- the late action table has a real numeric-effect cluster immediately after the temporary-status and strange-status entries
- `8E42` is a PP-reduction action over `pp_target`
- `8EAE` is a guts-cutting action
- `8F21` is a paired offense-and-defense reduction action
- `9E38` is the one-target defense-up action and best current local fit for `DEFENSE_SPRAY`
- `9E7F` is the all-target wrapper and best current local fit for `DEFENSE_SHOWER`

This is materially stronger than the older “neighboring non-affliction cluster” wording.

## What is still open

Still open:

- whether `C2:8E42` should be promoted all the way to the final reference name `BTLACT_REDUCEPP`
- whether `C8:F77D` versus its nearby sibling messages let us split `9E38` and `9E7F` more concretely into distinct spray or shower identities
- whether the later `8F21` reuses at entries `233` and `234` are strict clones or only metadata-distinct table aliases

## Current takeaway

The safest current takeaway is:

- the late `D5:7B68` table is no longer only status writers plus anonymous leftovers
- entries `95..98` form a real stat-and-resource mutation cluster
- those entries mutate `pp_target`, `guts`, `offense`, and `defense`
- the resulting messages are all routed through the same amount-bearing battle-text path at `C1:DC66`

## Best next target

The best next move is to keep following the next neighboring late entries that still print numeric deltas, because this cluster now gives us a clean pattern for separating status families from stat or resource mutation families.






