# Class2 D5 7B68 Battle Action Table Match

This note captures the strongest current cross-check for the `D5:7B68` table reached from descriptor field `D5:9589 + 0x4E`.

See also `notes/class2-descriptor-field-4e-and-d57b68.md`.
See also `notes/class2-second-pointer-consumer-40a4.md`.
See also `notes/class2-d57b68-early-entry-name-crosswalk.md`.

## Current strongest claim

The safest current reading is no longer just that `D5:7B68` is "battle-action-like." The first 12-byte records in the local ROM match the `ebsrc` battle action table layout so closely that the best working model is:

- byte `+0x00`: action direction
- byte `+0x01`: action target
- byte `+0x02`: action type
- byte `+0x03`: PP or cost byte
- dword `+0x04`: message pointer
- dword `+0x08`: action pointer

This is still framed as a ROM-plus-reference inference, not a pure local proof from every downstream consumer, but the match is unusually strong.

## Why the match is strong

From the local ROM, the first entries at `D5:7B68` decode like this:

- `0x0000`: `(1, 0, 0, 0)` + `C7:7EFF` + `C2:9039`
- `0x0001`: `(1, 0, 4, 0)` + `C7:7DCE` + `C2:9039`
- `0x0004`: `(0, 1, 1, 0)` + `EF:848C` + `C2:859F`
- `0x0005`: `(0, 1, 2, 0)` + `EF:84B6` + `C2:8740`
- `0x0006`: `(0, 1, 5, 0)` + `EF:8530` + `C2:8770`
- `0x0007`: `(1, 0, 5, 0)` + `EF:89E0` + `C2:AD1B`
- `0x000A`: `(0, 4, 3, 10)` + `EF:8543` + `C2:9556`
- `0x000B`: `(0, 4, 3, 14)` + `EF:8543` + `C2:955F`
- `0x000E`: `(0, 3, 3, 6)` + `EF:8543` + `C2:95AB`
- `0x0012`: `(0, 1, 3, 4)` + `EF:8543` + `C2:9647`
- `0x0016`: `(0, 4, 3, 3)` + `EF:8543` + `C2:9871`

From the quarantined `ebsrc` reference, the battle action enums define:

- direction `0 = PARTY`, `1 = ENEMY`
- target `0 = NONE`, `1 = ONE`, `2 = RANDOM`, `3 = ROW`, `4 = ALL`
- type `0 = NOTHING`, `1 = PHYSICAL`, `2 = PIERCING_PHYSICAL`, `3 = PSI`, `4 = ITEM`, `5 = OTHER`

That enum layout fits the local bytes immediately and cleanly.

## Concrete early-entry matches

The best sample matches are:

- `0x0000`: `ENEMY / NONE / NOTHING / 0`, which lines up with the reference table's `NO_EFFECT`
- `0x0001`: `ENEMY / NONE / ITEM / 0`, which lines up with `USE_NO_EFFECT`
- `0x0004`: `PARTY / ONE / PHYSICAL / 0`, which lines up with `BASH`
- `0x0005`: `PARTY / ONE / PIERCING_PHYSICAL / 0`, which lines up with `SHOOT`
- `0x0006`: `PARTY / ONE / OTHER / 0`, which lines up with `SPY`
- `0x0007`: `ENEMY / NONE / OTHER / 0`, which lines up with `PRAY`

Those are not vague thematic matches. They fit the exact byte patterns expected from the reference action table order.

## Early PSI handler families now have a stable local map

The table-order crosswalk is no longer standing alone. The local wrapper bodies now give a stable early-family map too:

- `0x000A..0x000D` -> Rockin alpha/beta/gamma/omega -> wrappers `C2:9556..9571` -> shared helper `C2:9516`
- `0x000E..0x0011` -> Fire alpha/beta/gamma/omega -> wrappers `C2:95AB..95C6` -> shared helper `C2:957A`
- `0x0012..0x0015` -> Freeze alpha/beta/gamma/omega -> wrappers `C2:9647..9662` -> shared helper `C2:95CF`
- `0x0016..0x0019` -> Thunder alpha/beta/gamma/omega -> wrappers `C2:9871..9895` -> shared helper `C2:966B`

That makes the early PSI slice of `D5:7B68` one of the strongest action-family crosswalks in the current project: table metadata, entry ordering, wrapper quartets, and shared helper signatures all agree.

## PSI families line up too

The PSI-like runs are even stronger because they preserve both targeting shape and cost progression:

- `0x000A..0x000D`: `PARTY / ALL / PSI / 10, 14, 40, 98`
  This matches the reference `PSI_ROCKIN_ALPHA/BETA/GAMMA/OMEGA` run.
- `0x000E..0x0011`: `PARTY / ROW / PSI / 6, 12, 20, 42`
  This matches the reference `PSI_FIRE_ALPHA/BETA/GAMMA/OMEGA` run.
- `0x0012..0x0015`: `PARTY / ONE / PSI / 4, 9, 18, 28`
  This matches the reference `PSI_FREEZE_ALPHA/BETA/GAMMA/OMEGA` run.
- `0x0016..0x0017`: `PARTY / ALL / PSI / 3, 7`
  This matches the reference `PSI_THUNDER_ALPHA/BETA` start of the next run.

The shared first pointer `EF:8543` across those entries also fits the reference shape well, because the reference PSI actions reuse a common `MSG_BTL_PSI` message pointer while varying the action handler.

## Why this matters for the local model

This narrows several earlier uncertainties:

- the front four bytes of each `D5:7B68` entry are best read as four independent metadata bytes, not two opaque control words
- the first pointer is much more likely to be a battle message or presentation pointer
- the second pointer is much more likely to be a battle action handler pointer consumed by `C2:40A4`
- descriptor field `D5:9589 + 0x4E` now looks like a selector into a bona fide action-descriptor table, not just an arbitrary paired-pointer table

That also makes the late selected-row controller look less like a generic scripted interaction path and more like a subsystem that can route into battle-style action descriptors when a selected row reaches the appropriate phase.

## Remaining caution

Two cautions still matter:

- this is still a cross-check aided by the `ebsrc` reference tree, so it should remain tagged as an inference until more local consumers are named end to end
- a few tail `+0x4E` outliers in the wider scan still do not fit the simple active-entry picture cleanly

Neither caveat weakens the early-entry match itself very much. The first chunk of the table is about as clean a structural match as we could hope for.

## Current takeaway

The current best takeaway is:

- `D5:7B68` is very likely the same battle action descriptor family represented in the `ebsrc` reference action table
- its first four bytes strongly match `direction`, `target`, `type`, and `cost`
- its first pointer behaves like a battle message pointer
- its second pointer behaves like a battle action handler pointer consumed by `C2:40A4`

That is a materially stronger statement than our earlier "battle-action-like" wording.

## Later status-action anchors are improving too

The later table is no longer only "mystery tails after the PSI quartets."

Two stronger late anchors now exist:

- `C2:8D5A` and `C2:A3D1` as a shared concentration or PSI-seal apply family over `battler::afflictions+4 = 4`
- `C2:A5EC` as a live item-side damage-plus-solidification entry over `battler::afflictions+2 = 4`

Those do not yet give the whole late table final names, but they materially strengthen the claim that `D5:7B68` remains a gameplay-facing battle action table well beyond the early PSI runs. See [class2-concentration-seal-family-c28d5a-c2a3d1.md](notes/class2-concentration-seal-family-c28d5a-c2a3d1.md) and [class2-solidification-item-action-c2a5ec-a630.md](notes/class2-solidification-item-action-c2a5ec-a630.md).

## Later stat and resource anchors are improving too

The late table now has a second non-status cluster with clean local bodies:

- `C2:8E42` -> one-target PP-reduction or PP-sapping action over battler `pp_target`
- `C2:8EAE` -> guts-cutting action over battler `guts`
- `C2:8F21` -> paired offense-and-defense reduction action
- `C2:9E38` -> one-target offense-up body over row `+0x26`
- `C2:9E7F` -> all-target offense-up wrapper over `C2:9E38`

That matters because these entries do not just look battle-action-like from table metadata. Their second-pointer bodies mutate concrete battler fields and then route amount-bearing text through `C1:DC66`, which is exactly the sort of gameplay-facing behavior we would expect from live battle action descriptors. See [class2-late-stat-and-resource-family-c28e42-c29e38.md](notes/class2-late-stat-and-resource-family-c28e42-c29e38.md).



## Later physical or special-action anchors

The late table now has a clearer physical-and-special slice too:

- `C2:8F97` -> strongest current local fit for a level-2 poison physical action, with live row `100` and poison-fangs text `EF:7EAC`
- `C2:8FF9` -> exact double-wrapper over `C2:859F`, promoted as `BTLACT_DOUBLE_BASH`, with live row `102` and attack-continuously text `EF:7F02`
- `C2:900B` -> one-target fire-damage or flaming-fireball action, with live row `104` and flaming-fireball text `EF:7F32`

That matters because this is another late-table slice where the local second-pointer bodies are no longer generic gameplay placeholders. One entry is a concrete poison-on-hit physical action, one is a concrete double-hit wrapper, and one is a concrete fire-damage special action. See [class2-late-physical-special-family-c28f97-c2900b.md](notes/class2-late-physical-special-family-c28f97-c2900b.md).

## Late flavor-tail anchors

A small late tail is now clearer too:

- `C2:902C` is a direct all-target wrapper over `C2:8651`, used by the tornado and gigantic-blast rows `117` and `118`
- `C2:9033` is a pure no-op flavor tail reused by a long run of taunt, gesture, mutter, smile, and similar message-driven rows
- `C2:9039..904E` are mostly address-distinct no-op tails chosen by the table rather than by unique gameplay mechanics

That matters because this strip should no longer be treated as one unresolved mechanics family. It is mostly a presentation-side parking lot plus one real all-target physical wrapper. See [class2-late-flavor-tail-c2902c-c2904e.md](notes/class2-late-flavor-tail-c2902c-c2904e.md).

## Later special event result anchors

A neighboring late slice is now much cleaner too:

- entry `0x00F3` (`243`) -> `C2:9298` -> strongest current local fit for `RUNAWAY_FIVE_EVENT`
- entry `0x00F4` (`244`) -> `C2:92EE` -> strongest current local fit for `MASTER_BARF_DEFEAT`
- entry `0x0122` (`290`) -> `C2:C14E` -> rainbow-colors or Master Belch-side special event family

The focused local writeup is now in [class2-special-event-results-c29298-c2c14e.md](notes/class2-special-event-results-c29298-c2c14e.md).

## Later normalization, diamondize, and odor anchors

A neighboring late slice is now much cleaner too:

- `C2:90C6` -> live rows `247` and `248` -> battler-normalization or return-to-original-form family
- `C2:916E` -> live row `228` -> one-target diamondize action
- `C2:9254` -> live rows `232` and `273` -> odor or stinky-gas offense-reduction family
- queued helper `C2:9051` -> stat-and-shield normalization callback installed by `90C6`

That matters because this area should no longer be treated as one unresolved late controller seam. The local bodies now split into a queued battler-normalization path, a true diamondize action, and a true offense-cut stink family. See [class2-late-normalization-and-odor-family-c29051-c29254.md](notes/class2-late-normalization-and-odor-family-c29051-c29254.md).

## Later explosive or bomb-family anchors

The late table now has a stronger projectile-or-explosive common-worker bridge too:

- `C2:A818` and `C2:A821` are thin wrappers over `C2:A658`
- those wrappers pass `90` and `270`, exactly matching the reference `BOMB` and `SUPER_BOMB` base-damage literals
- `C2:A658` itself now has a strong local fit for the shared splash-damage worker, because it scans battler rows by side, row, and spatial fields before applying secondary damage

That gives the action table one more clean non-status, non-stat family beyond the PSI quartets and late healing or debuff clusters. See [class2-bomb-common-family-c2a658-c2a821.md](notes/class2-bomb-common-family-c2a658-c2a821.md).


## Final Prayer ladder

The next late none-target `other` slice is now mapped too:

- entry `0x0123` (`291`) -> `C2:C572`
- entry `0x0124` (`292`) -> `C2:C5D1`
- entry `0x0125` (`293`) -> `C2:C5FA`
- entry `0x0126` (`294`) -> `C2:C623`
- entry `0x0127` (`295`) -> `C2:C64C`
- entry `0x0128` (`296`) -> `C2:C675`
- entry `0x0129` (`297`) -> `C2:C69E`
- entry `0x012A` (`298`) -> `C2:C6D0`
- entry `0x012B` (`299`) -> `C2:C6F0`

This is not just a thematic guess from the text. The local bodies form a real phase ladder:

- all nine rows are `enemy / none / other`
- all nine use the distinctive prayer message family at `C9:F0B8..F3EC`
- `291..298` write consecutive values `5..12` to `$A97A`
- `292..297` call the same damage-side helper with doubling amounts `0x32, `0x64, `0x00C8, `0x0190, `0x0320, `0x0640`
- `299` is the full finale controller, with the last four damage calls plus the final noise, music, and defeat sequence

So the strongest current local-plus-reference-backed fit is:

- `291..299` = `FINAL_PRAYER_1..9`

The focused local writeup is now in [class2-final-prayer-family-c2c572-c2c6f0.md](notes/class2-final-prayer-family-c2c572-c2c6f0.md).

