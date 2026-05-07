# Battle Selection Snapshot Export `C2:B930 .. BAC4`

This note captures the current best local model for the recurring helper at `C2:B930`.

See also [battle-choice-text-family-c1b2ec-b997.md](notes/battle-choice-text-family-c1b2ec-b997.md).
See also [battle-psi-user-selection-front-end-c1b5b6-b7c6.md](notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md).
See also [battle-psi-menu-controller-c1cc39-ce73.md](notes/battle-psi-menu-controller-c1cc39-ce73.md).

## Main result

## Working Names

- `C2:B930` = `ExportBattleSelectionSnapshot`

Source-scaffold promotion:

- `C2:B930..BAC5` is now decoded source in `src/c2/c2_b930_export_battle_selection_snapshot.asm`.
- The source-backed split preserves `C2:B6EB..B930` as the remaining data-gap tail of `InitializeEnemyBattlerStatsFromEnemyId`; `C2:B930` is a standalone direct-call target.
- The combined C2 scaffold validates after promotion: `C2 byte-equivalence: OK, 218 module(s), 0 mismatch(es).`

The strongest current local read is:

- `C2:B930` exports a larger battle selection or battler snapshot block
- input `A` is a `1`-based party or battler slot id
- input `X` or `Y` is the destination base
- the helper resolves the live `0x5F`-stride slot at `$99CE`
- then seeds the destination with both a small selection header and a wider copy of live battler-facing fields

So the safest current wording is not merely "write battle_menu_selection::user". The first bytes overlap the formal 6-byte `battle_menu_selection` struct at `$9FFA`, but the helper clearly writes well past it into a larger adjacent runtime block.

## Current strongest input-output model

The current best local model is:

- destination `+0` = selected user or battler id from input `A`
- destination `+2` = cleared word
- destination `+0C` = set to `1`
- destination `+0E/+0F` = cleared bytes
- destination `+10` = zero-based selected user or battler id

Then the helper copies several live slot fields from the selected `$99CE + n * 0x5F` row into the destination:

- `slot + 0x45 -> dest + 0x11`
- `slot + 0x47 -> dest + 0x13`
- `slot + 0x0A -> dest + 0x15`
- `slot + 0x4B -> dest + 0x17`
- `slot + 0x4D -> dest + 0x19`
- `slot + 0x0C -> dest + 0x1B`

It then copies the affliction and status-facing slice rooted at `slot + 0x0E` into the destination block beginning at `+0x1D`, and later derives more compact bytes from the late slot fields around `+0x52 .. +0x56` into destination bytes `+0x37 .. +0x3C`.

## Why `$9FFA` needs careful wording

Reference `ebsrc` still gives the formal struct at `$9FFA` as:

- `user`
- `param1`
- `selected_action`
- `targetting`
- `selected_target`

That remains useful for the ordinary menu-side writers in the lower PSI controller and the ordinary battle menu handlers.

But `C2:B930` writes far beyond those first 6 bytes, so the healthiest current local statement is:

- `$9FFA` starts with the ordinary `battle_menu_selection` header
- some callers, including the outer PSI-user-selection front end, also treat the same base as the start of a larger adjacent battle snapshot block

2026-05-05 C1 follow-up source polish makes that PSI-side use explicit in
`src/c1/c1_b5b6_open_battle_psi_user_selection.asm`:

- `BattleSelectionSnapshotBase = $9FFA` is staged before repeated `C2:B930`
  exports.
- `ActiveTargetSnapshotPointer = $A972` records the active exported block base.
- `BattleSelectionSnapshotStateByte = +0x1D` is copied back into live
  `PartyRuntimeStateBase = $99DC` state bytes after action text dispatch.

## Best current callers

Pinned callers now include:

- `C1:B3DB`
- `C1:B462`
- `C1:B505`
- `C1:B859`
- `C1:B9A9`
- `C1:BA60`
- `C2:38AF`
- `C2:4984`
- `C2:4AB2`
- `C2:630B`
- `C2:9332`

So this helper is not PSI-only. It is a reusable battle-side exporter that multiple menu and event-result lanes rely on.

## Safest current interpretation

The safest current summary is:

- `C2:B930` exports a selected live battler or party slot into a larger battle selection snapshot block
- when the destination is `$9FFA`, the formal `battle_menu_selection` struct lives at the front of that block
- the helper should therefore be treated as a snapshot exporter, not only as a menu-struct writer

The remaining soft edge is the exact full symbolic identity of the larger destination block, not whether the export itself is real.
