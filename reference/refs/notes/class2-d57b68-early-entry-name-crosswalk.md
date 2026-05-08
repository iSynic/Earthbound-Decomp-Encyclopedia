# Class2 D5 7B68 Early Entry Name Crosswalk

This note records the strongest early-entry name crosswalk between the local `D5:7B68` table and the quarantined `ebsrc` battle action table.

See also `notes/class2-d57b68-battle-action-table-match.md`.
See also `notes/class2-second-pointer-consumer-40a4.md`.
See also `notes/class2-psi-action-wrapper-local-verification.md`.

## Why this crosswalk is useful

The table-format match already made `D5:7B68` look very likely to be a battle action descriptor table.

The next useful step is to ask whether specific local second-pointer targets can be tentatively named by entry order. For the early portion of the table, the answer is yes: the local entries line up with the reference action names cleanly enough to give us a practical working crosswalk.

This is still an inference from table order and metadata, not a full local re-derivation of each handler body.

## Early action-slot crosswalk

The first chunk lines up like this:

- `0x0000` -> `NO_EFFECT` -> second pointer `C2:9039` (default no-op tail)
- `0x0001` -> `USE_NO_EFFECT` -> second pointer `C2:9039` (default no-op tail)
- `0x0002` -> `ACTION_002` -> second pointer `C2:9039` (default no-op tail)
- `0x0003` -> `ACTION_003` -> second pointer `C2:9039` (default no-op tail)
- `0x0004` -> `BASH` -> second pointer `C2:859F`
- `0x0005` -> `SHOOT` -> second pointer `C2:8740`
- `0x0006` -> `SPY` -> second pointer `C2:8770`
- `0x0007` -> `PRAY` -> second pointer `C2:AD1B`
- `0x0008` -> `GUARD` -> second pointer `C2:889B`
- `0x0009` -> `ACTION_009` -> second pointer `C2:903C` (isolated no-op tail)
- `0x0055` -> strongest current local fit for a concentration or PSI-seal enemy action -> second pointer `C2:8D5A`
- `0x003A` -> strongest current local fit for a one-target PSI strange-status action -> second pointer `C2:A056`
- `0x0035` -> strongest current local fit for an all-target asleep-status PSI action -> second pointer `C2:9F57`
- `0x009F` -> strongest current local fit for an item-side concentration or PSI-seal action -> second pointer `C2:A3D1`

That already gives several concrete local anchors: `C2:859F`, `C2:8740`, `C2:8770`, `C2:889B`, and `C2:AD1B` are now strong candidates for the local `BASH`, `SHOOT`, `SPY`, `GUARD`, and `PRAY` action families.

## PSI handler families line up in order too

The PSI runs are even more useful because they form clean local handler families.

### Rockin family

- `0x000A` -> `PSI_ROCKIN_ALPHA` -> `C2:9556`
- `0x000B` -> `PSI_ROCKIN_BETA` -> `C2:955F`
- `0x000C` -> `PSI_ROCKIN_GAMMA` -> `C2:9568`
- `0x000D` -> `PSI_ROCKIN_OMEGA` -> `C2:9571`

These four entries share the same message pointer and use a tight run of local wrapper routines, which is exactly what we would expect from tiered action variants.

### Fire family

- `0x000E` -> `PSI_FIRE_ALPHA` -> `C2:95AB`
- `0x000F` -> `PSI_FIRE_BETA` -> `C2:95B4`
- `0x0010` -> `PSI_FIRE_GAMMA` -> `C2:95BD`
- `0x0011` -> `PSI_FIRE_OMEGA` -> `C2:95C6`

Again, the local targets form a compact sequential wrapper family.

### Freeze family

- `0x0012` -> `PSI_FREEZE_ALPHA` -> `C2:9647`
- `0x0013` -> `PSI_FREEZE_BETA` -> `C2:9650`
- `0x0014` -> `PSI_FREEZE_GAMMA` -> `C2:9659`
- `0x0015` -> `PSI_FREEZE_OMEGA` -> `C2:9662`

This gives us a third clean local wrapper family with extremely plausible tier ordering.

### Thunder family

- `0x0016` -> `PSI_THUNDER_ALPHA` -> `C2:9871`
- `0x0017` -> `PSI_THUNDER_BETA` -> `C2:987D`
- `0x0018` -> `PSI_THUNDER_GAMMA` -> `C2:9889`
- `0x0019` -> `PSI_THUNDER_OMEGA` -> `C2:9895`

This continues the same pattern.

### Flash family

- `0x001A` -> `PSI_FLASH_ALPHA` -> `C2:9987`
- `0x001B` -> `PSI_FLASH_BETA` -> `C2:99AE`
- `0x001C` -> `PSI_FLASH_GAMMA` -> `C2:99EF`
- `0x001D` -> `PSI_FLASH_OMEGA` -> `C2:9A35`

The spacing widens here, but the family ordering still matches the reference table cleanly.

### Starstorm family

- `0x001E` -> `PSI_STARSTORM_ALPHA` -> `C2:9AA6`
- `0x001F` -> `PSI_STARSTORM_OMEGA` -> `C2:9AAF`

Even the shortened two-entry family matches the reference table order exactly.

These early PSI names are now strong enough to use as working final family names in the notes, with one caveat: some of the underlying `C2:` code addresses are reused by later non-PSI table entries. So the safest wording is still that the early `0x000A..0x001F` records are the canonical PSI-family uses of those wrapper helpers, not that every later action-table reuse inherits the same PSI name.

## What this buys us locally

This crosswalk gives us a practical naming bridge for many local `C2:` routines even before we fully decode their bodies.

The safest current working labels are still "candidate local handler for" rather than final routine names, but the confidence is good enough to use them in notes when discussing families of action behavior.

In particular, the following local regions now look like canonical PSI-family action clusters rather than anonymous wrappers:

- `C2:9556..9571` -> Rockin family
- `C2:95AB..95C6` -> Fire family
- `C2:9647..9662` -> Freeze family
- `C2:9871..9895` -> Thunder family
- `C2:9987..9A35` -> Flash family
- `C2:9AA6..9AAF` -> Starstorm family

## Best next target

The best next move is to pick one local family such as `C2:95AB..95C6` or `C2:9871..9895` and decode its shared helper path. That would turn this crosswalk from a strong order-based inference into a locally verified action-family interpretation.

## Later concentration or PSI-seal anchors

A useful later-table bridge landed after the early PSI pass.

Two non-early entries now have a concrete shared effect shape:

- entry `0x0055` (`85`) -> `C2:8D5A`
- entry `0x009F` (`159`) -> `C2:A3D1`

Those two bodies are not simple table-order guesses. Locally, both converge on the same target-side concentration or PSI-seal write:

- zero-check battler row byte `+0x21`
- write `4`
- display `EF:6C0B`
- otherwise fail through `EF:766E`

So while the exact reference export names for those two slots still stay one notch cautious, they are now strong anchors for the `battler::afflictions+4` concentration group documented in [class2-concentration-seal-family-c28d5a-c2a3d1.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-concentration-seal-family-c28d5a-c2a3d1.md).

## Later item-side solidification anchor

A second late-table anchor is now in place for the temporary-status byte at `battler::afflictions+2`.

- entry `0x00A6` (`166`) -> `C2:A5EC`

This is no longer just a loose neighboring item action. Locally, `C2:A5EC`:

- gates the target
- computes direct damage from `100 - target defense`
- routes that damage through `C2:8125`
- then calls `C2:724A` with `X = 2`, `Y = 4`
- displays `EF:6BEF` on success and `EF:766E` on failure

That makes it the strongest current late-table anchor for an item-side solidification action, with [class2-solidification-item-action-c2a5ec-a630.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-solidification-item-action-c2a5ec-a630.md) documenting the focused local case. The best current reference-backed candidate is `BTLACT_HANDBAG_STRAP`.

## Later persistent-status anchors

A third late-table bridge is now in place for the persistent hard-heal subgroup byte at `battler::afflictions+1`.

Two adjacent late entries now have a strong local action-entry read:

- entry `0x004B` (`75`) -> `C2:8BBE`
- entry `0x004C` (`76`) -> `C2:8BFD`

Locally, both are enemy one-target `other` actions that route through `C2:724A` with `X = 1`:

- `C2:8BBE` writes `Y = 1` and displays `EF:6B81`
- `C2:8BFD` writes `Y = 2` and displays `EF:6B98`

That makes them strong late-table anchors for the `STATUS_1` subgroup values now documented in [class2-persistent-status-action-pair-c28bbe-c28bfd.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-persistent-status-action-pair-c28bbe-c28bfd.md). The strongest current reference-backed candidates are `BTLACT_MUSHROOMIZE` and `BTLACT_POSSESS`.

## Later temporary-status cluster

The next late-table slice is now usable too.

Three neighboring enemy one-target `other` entries now read as a temporary-status cluster over `battler::afflictions+2`:

- entry `0x004E` (`78`) -> `C2:8C69` -> crying family
- entries `0x004F..0x0052` (`79..82`) -> `C2:8CB8` -> immobilized or could-not-move family
- entry `0x0053` (`83`) -> `C2:8CF1` -> solidification family
- entry `0x0054` (`84`) -> `C2:8D3A` -> strange-status wrapper over `C2:A056`
- entry `0x0056` (`86`) -> `C2:8DBB` -> direct strange-status sibling
- entry `0x0057` (`87`) -> `C2:8DFC` -> all-target crying sibling
- entry `0x005A` (`90`) -> `C2:9F57` -> all-target asleep-status wrapper
- entry `0x00CF` (`207`) -> `C2:8D3A` -> second strange-status wrapper reuse

The strongest focused summaries are now in [class2-asleep-family-c29f06-c29f57.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-asleep-family-c29f06-c29f57.md), [class2-temporary-status-action-cluster-c28c69-c28cb8-c28cf1.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-temporary-status-action-cluster-c28c69-c28cb8-c28cf1.md), and [class2-strange-status-family-c28d3a-c28dbb-c2a056.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-strange-status-family-c28d3a-c28dbb-c2a056.md).

## Later stat and resource mutation cluster

The next late slice is no longer best treated as "non-status leftovers."

Entries `95..98` now form a real numeric-effect cluster:

- entry `0x005F` (`95`) -> `C2:8E42` -> strongest current local fit for a one-target PP-reduction or PP-sapping action
- entry `0x0030` (`48`) -> `C2:9E38` -> strongest current local fit for `DEFENSE_SPRAY`
- entry `0x0031` (`49`) -> `C2:9E7F` -> strongest current local fit for `DEFENSE_SHOWER`
- entry `0x0060` (`96`) -> `C2:9E38` -> defense-up family
- entry `0x0061` (`97`) -> `C2:8EAE` -> guts-cutting family
- entry `0x0062` (`98`) -> `C2:8F21` -> paired offense-and-defense reduction family

There are also useful later reuses:

- entries `0x00E9` and `0x00EA` (`233`, `234`) -> `C2:8F21`
- `C2:9E7F` -> trivial wrapper over `C2:9E38`

The focused local summary is now in [class2-late-stat-and-resource-family-c28e42-c29e38.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-late-stat-and-resource-family-c28e42-c29e38.md). The strongest current reference-backed fits are:

- `C2:8E42` -> `BTLACT_REDUCEPP`
- `C2:8EAE` -> `BTLACT_CUTGUTS`
- `C2:8F21` -> `BTLACT_REDUCEOFFDEF`
- `C2:9E38` -> `BTLACT_DEFENSE_SPRAY`
- `C2:9E7F` -> `BTLACT_DEFENSE_SHOWER`



## Early healing family

The early non-damaging PSI healing quartet is now in much better shape too.

- `0x0020` (`32`) -> `C2:9AC6` -> strongest current local fit for `LIFEUP_ALPHA`
- `0x0021` (`33`) -> `C2:9ACF` -> strongest current local fit for `LIFEUP_BETA`
- `0x0022` (`34`) -> `C2:9AD8` -> strongest current local fit for `LIFEUP_GAMMA`
- `0x0023` (`35`) -> `C2:9AE1` -> strongest current local fit for `LIFEUP_OMEGA`

The shared local core is now documented in [class2-healing-amount-family-c29ab8-c29ae1.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-healing-amount-family-c29ab8-c29ae1.md). The strongest current local model is a four-wrapper healing family over fixed amounts `100`, `300`, `10000`, and `400`, with the `Omega` wrapper as the all-target sibling.

## Later physical or special-action anchors

A neighboring late slice is now in much better shape too.

- entry `0x0064` (`100`) -> `C2:8F97` -> strongest current local fit for a level-2 poison physical action
- entry `0x0066` (`102`) -> `C2:8FF9` -> `DOUBLE_BASH`
- entry `0x0068` (`104`) -> `C2:900B` -> one-target fire-damage or flaming-fireball action

The focused local writeup is now in [class2-late-physical-special-family-c28f97-c2900b.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-late-physical-special-family-c28f97-c2900b.md). The strongest current takeaways are:

- `C2:8F97` = strongest current local-plus-reference-backed fit for `BTLACT_LEVEL_2_ATK_POISON`
- `C2:8FF9` = `BTLACT_DOUBLE_BASH`
- `C2:900B` = one-target fire-damage wrapper, still one notch short of a final promoted reference export

## Late flavor-tail anchors

A small late tail is now much clearer too.

- entry `0x0075` (`117`) and `0x0076` (`118`) -> `C2:902C` -> all-target wrapper over the `C2:8651` physical family
- `C2:9033` -> the main flavor-only no-op tail, reused by a long run of enemy `none/other` and item `none/item` rows
- `C2:9039..904E` -> small address-distinct no-op tails for rows whose visible behavior is message-driven

The focused local writeup is now in [class2-late-flavor-tail-c2902c-c2904e.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-late-flavor-tail-c2902c-c2904e.md).

## Later normalization, diamondize, and odor anchors

A neighboring late slice is now much cleaner too.

- entry `0x00E4` (`228`) -> `C2:916E` -> one-target diamondize family
- entry `0x00E8` (`232`) -> `C2:9254` -> horrid-odor offense-cut family
- entries `0x00F7` and `0x00F8` (`247`, `248`) -> `C2:90C6` -> battler-normalization or return-to-original-form family
- entry `0x0111` (`273`) -> `C2:9254` -> stinky-gas offense-cut reuse

The focused local writeup is now in [class2-late-normalization-and-odor-family-c29051-c29254.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-late-normalization-and-odor-family-c29051-c29254.md). The safest current local split is:

- `C2:9051` = queued battler stat-and-shield normalization callback
- `C2:90C6` = special normalization or return-to-original-form wrapper
- `C2:916E` = one-target diamondize action
- `C2:9254` = odor or stinky-gas offense-reduction family

## Later explosive or bomb-family anchors

The later table now has a stronger explosive common-worker bridge too.

- `C2:A818` -> strongest current local fit for `BTLACT_BOMB`
- `C2:A821` -> strongest current local fit for `BTLACT_SUPER_BOMB`
- shared helper `C2:A658` -> strongest current local fit for `BOMB_COMMON`

This is not resting only on text flavor. The two wrappers pass the exact reference base-damage literals `90` and `270`, and the common body matches the reference splash-damage shape unusually well. The focused local writeup is now in [class2-bomb-common-family-c2a658-c2a821.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-bomb-common-family-c2a658-c2a821.md).
