# Battle PSI User-Selection Front End `C1:B5B6 .. B7C6`

This note captures the current best local model for the battle-side front end rooted at `C1:B5B6`.

See also [battle-psi-menu-controller-c1cc39-ce73.md](notes/battle-psi-menu-controller-c1cc39-ce73.md).
See also [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md).
See also [battle-psi-category-list-family-c1caf5-c1cb7f.md](notes/battle-psi-category-list-family-c1caf5-c1cb7f.md).
See also [battle-targetting-resolver-c1adb4-af50.md](notes/battle-targetting-resolver-c1adb4-af50.md).
See also [battle-selection-snapshot-export-c2b930.md](notes/battle-selection-snapshot-export-c2b930.md).

## Main result

The strongest current local read is:

- `C1:B5B6 .. B7C6` is the outer battle PSI user-selection front end
- it chooses which party member will act as the current PSI user
- it stages that result in `$9D16`
- it then opens a direct PSI-entry picker through `C1:C8BC`
- and the back half either routes through ordinary PSI targetting or through a separate special-event branch before returning success or restart state

That is stronger than the older vague wording that treated `B5B6` as only a generic battle choice controller.

`C1:B5B6..BB71` is now promoted into byte-equivalent source at `src/c1/c1_b5b6_open_battle_psi_user_selection.asm`. The promoted interval includes the outer user-selection front end, the selected-action writeback path, the adjacent PSI snapshot/text lane, and the small finalizer at `C1:BB06`.

2026-05-05 follow-up polish tightened the source vocabulary for this module:

- `$9D16/$9D18/$9D19` are named as the selected PSI user byte, single-user fast-path latch, and highlighted PSI row byte.
- `D5:8A50` PSI ability rows and `D5:7B68` battle action rows now carry the same field names used by the lower PSI controller and row formatter.
- the PP guard names the action-row PP-cost byte, the chosen user's current PP word at `$9A19`, and the insufficient-PP text pointer.
- the category-8 branch names the map-context, event-flag, region-blocker, C0:DD53 event branch, and blocked-text guard.
- the ordinary success side names the `$9FFA` battle selection snapshot root, `$A972` active snapshot pointer, `+0x1D` exported state byte, and live `$99DC` state mirror copyback.
- the `C1:BB06` finalizer names the help-text window refresh path through `C1:C8BC`, `D5:8A50 +0x0B`, and the generic text pointer printer.

## Direct caller bridge

There is still only one pinned direct caller in the current ROM:

- `C1:3B89 -> C1:B5B6`

That caller sits on the ordinary battle command-selection side, and the reference `battle_psi_menu_redirect.asm` bridge points to the same user-facing lane through `REDIRECT_BATTLE_PSI_MENU`.

So the safest current statement is:

- `B5B6` is directly on the battle PSI command path
- but its local shape is broader than the already-separated lower controller at `CC39 .. CE73`

## User-selection stage

The front half is still the cleanest local gain.

### Single eligible-user fast path

`B5CC .. B5FC` reads cleanly as a fast path for the case where only one party member can currently use the relevant PSI lane:

- `C1:C3B6` counts eligible users
- when that count is `1`, `C1:C373` finds the first eligible user
- the resulting party-member id is read from `$986F + X`
- `C1:C853` is called with that user id
- the `BattlePsiSingleUserFastPathLatch` byte is set to `1`
- and the chosen user id later lands in `BattlePsiSelectedUserByte`

So the strongest current local read is that `BattlePsiSingleUserFastPathLatch` is a small auto-selected-user latch for this front end, while `BattlePsiSelectedUserByte` is the live chosen PSI user id.

### Multi-user selection path

The alternative path at `B5FE .. B628` is also much healthier now.

It installs two callback pointers:

- `$0E/$10 = C1:C853`
- `$12/$14 = C1:C367`

Then it calls the generic menu helper at `C1:27EF`, stores the resulting chosen user id in `$26`, and then writes that id into `BattlePsiSelectedUserByte`.

The strongest current local model is:

- `C367` is a tiny PSI-user eligibility predicate wrapper over `C1:C32A`
- `C853` is the display-side PSI metadata helper used to refresh the current user-facing PSI row data
- `27EF` is the generic menu runner that uses those callbacks to drive a party-member selection stage

## Direct PSI-entry picker handoff

After `BattlePsiSelectedUserByte` is staged, `B63C .. B67E` immediately drops into a second-stage PSI entry picker:

- it installs callback pointer `C1:C8BC`
- it calls the ordinary menu loop through `C1:1F5A / 196A / 1F8A`
- the selected PSI-table row id is kept in local `$01`

That means this front end is not the same thing as `CC39 .. CE73`.

The safest current split is now:

- `B5B6 .. B7C6` = outer battle PSI user-selection front end
- `C8BC` = direct PSI-entry row formatter used by that front end
- `CC39 .. CE73` = separate ordinary battle PSI category-plus-entry controller lane

## Entry-side validation and branch split

The back half at `B694 .. B7C6` is now healthier than before.

For ordinary entries it:

- indexes the selected `D5:8A50` PSI row
- resolves the associated `D5:7B68` action row from `+4`
- compares associated action-row PP cost against the chosen user's live PP field at `$9A19`
- shows the same `FAAA` insufficient-PP family on failure
- and for ordinary entries later calls the shared targetting resolver `C1:ADB4`

One especially useful local refinement is the category-side split inside this region:

- a selected PSI row with category byte `+2 == 8` takes its own special branch before the ordinary `ADB4` targetting path
- the `D5:8A50` table now makes that much more concrete: the only live category-`8` rows are the Teleport pair

So the healthiest current wording is now narrower:

- the front end has a special battle Teleport or other-PSI branch
- the ordinary PSI side later rejoins the shared battle targetting path

## Ordinary writeback and snapshot export

The ordinary success side after `B7C6` is now much clearer.

It does three distinct things:

1. seeds `$9FFA`
- `B859 -> C2:B930` exports the chosen user into the `$9FFA`-rooted battle selection snapshot block
- this overlaps the formal `battle_menu_selection` struct at the front, but it writes far past the first 6 bytes

2. resolves and displays the associated action text side
- `B9AD .. B9F8` resolves the associated `D5:7B68` row from the chosen `D5:8A50` entry
- installs its pointer into `$00BC/$00BE`
- and dispatches it through `C0:9279`

3. projects exported row state back into live slot state
- `BA03 .. BA40` and `BAB1 .. BAEF` copy byte `+0x1D` from the exported `$A972`-selected block back into live `$99DC + slot`
- then `BAF1 -> C3:EE4D` performs a shared battle-side close or sync finalizer

So the outer front end does more than just choose a user and return an action id. It also seeds the battle snapshot block and mirrors row state back into the live per-slot state family.

## Special branch and restart behavior

The special branch rooted at `B839 .. B84D` is now strong enough to keep separate:

- when the PSI row category byte is `8`, the front end reads one more byte from the chosen PSI row
- that category now lines up best with the Teleport pair in the `OTHER` PSI bucket
- it feeds the extra Teleport-side selector byte into `C0:DD53`
- and then jumps out through `B8E7`

The ordinary resolver path behaves differently:

- `B79A -> C1:ADB4` resolves targetting from the associated action id
- zero result restarts the direct PSI-entry picker through `B642`
- nonzero result continues into the ordinary writeback path

So the safest current statement is:

- category `8` bypasses ordinary targetting and uses the `DD53` event or transition path
- ordinary categories stay on the shared PSI targetting and writeback side

## `$9D16`, `$9D18`, and `$9D19`

The local meanings of these front-end bytes are much healthier now:

- `$9D16` / `BattlePsiSelectedUserByte` = currently chosen PSI user id for this front end
- `$9D18` / `BattlePsiSingleUserFastPathLatch` = auto-selected-user latch or fast-path marker
- `$9D19` / `BattlePsiHighlightedRowByte` = last highlighted PSI row used by the help-text refresh finalizer

That fits the current access pattern well:

- `B62F` writes `$9D16`
- `CAAF` later reads `$9D16` and routes it back into `C1:C853`
- `B5C9/B5F9/B681` use `$9D18` only inside this front end's fast path and refresh gating
- `BB13/BB19/BB2F` use `$9D19` to skip redundant help-text redraws for the same highlighted row

## Safest current interpretation

The safest current summary is:

- `B5B6 .. B7C6` is the outer battle PSI user-selection front end
- it first decides which party member is the current PSI user
- it stages that user in `$9D16`
- it then opens the direct PSI-entry picker using `C1:C8BC`
- category `8` PSI rows, now strongest as the Teleport pair in the `OTHER` PSI bucket, take a separate `C0:DD53` branch
- ordinary PSI rows later feed the shared PP-check and targetting machinery through the associated `D5:7B68` action row
- the ordinary success side seeds the `$9FFA` battle selection snapshot block and mirrors row byte `+0x1D` back into live `$99DC` slot state

The remaining soft edge is the exact player-facing identity of the category `8` branch and the exact full symbolic name of the larger `$9FFA`-rooted snapshot block, not whether this front end is real.

## Working Names

- `C1:B5B6` = `OpenBattlePsiUserSelection`
- `C1:B7C6` = `WriteSelectedPsiActionIntoBattleSelection`
- `C1:B850` = `BuildPsiSelectionSnapshotAndText`
- `C1:B997` = `DisplayBattlePsiActionText`
- `C1:BB06` = `FinalizeBattlePsiSelectionState`

