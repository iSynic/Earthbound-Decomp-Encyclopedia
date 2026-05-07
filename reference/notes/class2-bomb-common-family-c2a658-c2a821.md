# Class2 Bomb Common Family C2A658 C2A821

This note captures the strongest current local model for the projectile or explosive common helper at `C2:A658` and its two thin wrappers `C2:A818` and `C2:A821`.

See also [class2-d57b68-battle-action-table-match.md](notes/class2-d57b68-battle-action-table-match.md).
See also [class2-d57b68-early-entry-name-crosswalk.md](notes/class2-d57b68-early-entry-name-crosswalk.md).
See also [class2-second-pointer-consumer-40a4.md](notes/class2-second-pointer-consumer-40a4.md).

## Working Names

- `C2:A658` = `RunBombCommonSplashDamage`
- `C2:A818` = `RunBombAction`
- `C2:A821` = `RunSuperBombAction`

## Main result

`C2:A658` is now a strong local-plus-reference-backed fit for the common bomb or explosive splash-damage worker.

The two thin wrappers are:

- `C2:A818` -> passes `0x005A` (`90`)
- `C2:A821` -> passes `0x010E` (`270`)

Those exact wrapper constants match the `ebsrc` bomb action files unusually well:

- `BTLACT_BOMB` -> `90`
- `BTLACT_SUPER_BOMB` -> `270`

That is strong enough to treat the current best local fits as:

- `C2:A818` = `BTLACT_BOMB`
- `C2:A821` = `BTLACT_SUPER_BOMB`
- `C2:A658` = `BOMB_COMMON`

## Why `C2:A658` matches bomb common

The local body has the same broad shape as the reference `BOMB_COMMON`:

- incoming `A` is treated as the base damage parameter
- `C2:6A44` / `RollRandomAmount` shapes that parameter into the applied damage amount
- damage is routed through `C2:8125` / `ApplyDamageToSelectedTarget`
- if the current target is in the ordinary battler domain, the helper then scans other battler rows rather than stopping at one target
- it compares candidate rows against the current target's side, row, and spatial fields before deciding whether to include them
- selected secondary targets are then revisited and damaged through the same common amount path

That is not a status-writer shape or an item-oneoff shape. It is a real splash-damage or area-damage common worker.

## What the local scan is doing

The local helper is not just "loop through everyone."

Current strongest read:

- it uses the battler table rooted at `$9FAC`
- it checks side through `ally_or_enemy`
- it checks row through battler `row`
- it calls `C2:EFFD` / `GetBattleSpriteWidthBucket` for the current and candidate sprite ids
- it compares position-related or sprite-width-derived spatial fields before accepting secondary targets
- it then reapplies the damage amount to accepted nearby targets

That is a very healthy local fit for an explosive or blast-radius family.

## Action-table anchors

The currently useful table anchors are:

- entries `64` and `65` -> `C2:A821` -> enemy one-target `other`
- entry `101` -> `C2:A821` -> enemy one-target `other`, text `EF:7ED5`
- entry `167` -> `C2:A818` -> enemy one-target `item`, text `C9:7EB7`
- entry `168` -> `C2:A821` -> enemy one-target `item`, text `C9:7EB7`
- entry `310` -> `C2:A818` -> enemy one-target `item`, text `C9:7E9E`
- entry `311` -> `C2:A821` -> enemy one-target `item`, text `C9:7E9E`

The message side reinforces the projectile or explosive flavor:

- `EF:9A7E` = exploded-to-bits style text
- `EF:9A9E` = burst-into-flames style text
- `EF:7ED5` = fired-a-missile style text
- `C9:7EB7` and `C9:7E9E` are thrown-or-fired item wrappers

## Why `C2:A821` should not be confused with the nearby solidification helper

The neighborhood right after `C2:A821` includes `C2:A82A`, which is a straightforward solidification apply path over `C2:724A` with success text `EF:6BEF`.

That proximity could have made `A821` look like another solidification wrapper at first glance, but the bodies are different:

- `A821` is just a damage-parameter wrapper over `A658`
- `A82A` is the direct status-application sibling

So `A821` belongs with the explosive or bomb common family, not with the pure solidification wrappers.

## Current safest interpretation

The safest current interpretation is:

- `C2:A658` is the shared explosive splash-damage worker
- `C2:A818` and `C2:A821` are the small bomb-family wrappers over that worker
- the exact wrapper constants and the reference `bomb.asm` or `super_bomb.asm` files now line up cleanly enough to promote those two wrapper identities
- the wrapper sources now call `C2:A658` by the same `RunBombCommonSplashDamage` contract as the full bomb-common body
- the secondary-target overlap check now shares named width-bucket vocabulary with the call-for-help sprite-width budget path

## What is still open

Still open:

- whether every `C2:A821` reuse should be described strictly as bomb-family, or whether some later enemy-only entries are best called broader explosive clones
- whether the projectile-flavored entry texts around `A821` should get their own small follow-up note later

## Current takeaway

The safest current takeaway is:

- `A658` is no longer an unresolved common worker
- it is now best understood as the local `BOMB_COMMON` equivalent
- `A818` and `A821` are the best current local fits for `BOMB` and `SUPER_BOMB`, and both source wrappers now name their common worker call

## Best next target

The best next move is to pin the exact live table rows for `C2:A818` and then decide whether the surrounding projectile-flavored `A821` reuses deserve a small projectile-or-explosive subfamily note of their own.
