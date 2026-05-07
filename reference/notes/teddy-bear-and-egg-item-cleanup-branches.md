# Teddy Bear and Egg Item Cleanup Branches

These are the two item-sensitive cleanup branches reached from [inventory-slot-removal-helper-c18c27.md](notes/inventory-slot-removal-helper-c18c27.md).

## Working Names

- `C2:29BB` = `RemovePartyOverlayTrackedItemId`

Source polish follow-up (2026-05-06): the C1 inventory insertion/removal source
now names these hooks directly. The insertion path calls
`C216DB_ArbitratePartyOverlayEntityPresence` and
`C3EAD0_RefreshEggFamilyLifecycleOnInsert`; the removal path calls
`C229BB_RemovePartyOverlayTrackedItemId`,
`C216DB_ArbitratePartyOverlayEntityPresence`, and
`C3EB1C_RefreshEggFamilyLifecycleOnRemove`.

## Main result

The extra cleanup in `C1:8C27` is no longer just a vague item-type side effect.

The two branches now read best as:

- item type `4` = Teddy Bear family cleanup
- item flags bit `0x10` = Fresh Egg / Chick / Chicken family refresh

## Type `4` branch

The item-table cross-check is unusually clean here.

Using the local item table plus the extracted `item_configuration_table.yml`, the only items with type byte `+0x19 == 4` are:

- `2 = Teddy bear`
- `3 = Super plush bear`

That means the `C1:8C27` branch through `C2:29BB` and `C2:16DB` is not a generic equipment-removal path. It is a Teddy-Bear-family side system.

### What `C2:29BB` looks like locally

`C2:29BB` is a removal helper over a shared six-entry ordered id list at `$986F`, with companion count/state at `$98A3` and follow-up refresh through `C0:3903`.

Locally it:

- scans `$986F..` for the selected byte id
- removes that id and compacts later nonzero entries left
- zeroes the vacated tail slot
- runs a small refresh path through `C0:3903`
- for ids `< 4`, also calls `C2:16DB` and `C3:EBCA`

The matching insert helper at `C2:28F8` performs the opposite packed-list update and is also used from the same broad family.

The exact broader meaning of this six-entry list is still a little open in local-only terms, so the safest wording is: Teddy Bear removal updates a shared ordered active-id list, not just the inventory byte array.

## Flags bit `0x10` branch

This branch is even tighter at the item-table level.

The only items with byte `+0x1C` bit `0x10` set are:

- `92 = Fresh Egg`
- `168 = Chick`
- `169 = Chicken`

So the `C1:8C27 -> C3:EB1C` branch now reads strongly as an egg/chick/chicken-family tracker refresh, not a generic item-flag hook.

### What `C3:EB1C` looks like locally

`C3:EB1C` takes the removed item id as an 8-bit input and does three notable things:

- maps that item through a tiny 5-byte-step table at `D5:F4BB`
- calls `C4:8F98` with the resulting small table index
- scans the active character inventory records of the current active-party/active-member family, looking through the 14-byte inventory region at `99F1..99FE`
- if it finds the same item id still present, it calls `C4:8EEB` with that small table index

That is a much better fit for a special tracked item family than for ordinary item deletion. The safest current read is: this helper refreshes a small runtime registry for the Fresh Egg / Chick / Chicken lifecycle family based on whether those items are still present in active inventories.

## Best current interpretation

The safest current local read is:

- Teddy Bear and Super Plush Bear trigger a shared ordered-id-list cleanup path on removal
- Fresh Egg, Chick, and Chicken trigger a special inventory-presence refresh path on removal

So `C1:8C27` is not only maintaining character inventory slots. It also acts as the bridge into two small item-family-specific side systems.

## Confidence

- type `4` as Teddy Bear / Super Plush Bear family: high confidence
- flags bit `0x10` as Fresh Egg / Chick / Chicken family: high confidence
- `C3:EB1C` as a special tracked-item presence refresh for that family: moderately high confidence
- exact subsystem name of the `$986F` six-entry ordered-id list: still cautious
