# Bank C2 First Pass

## Main result

Bank `C2` is the main battle runtime and battle UI support bank, with additional
party/inventory/status helpers and late battle visual support. It owns HP/PP
window refresh, event-flag wrappers, derived character stat recalculation,
party overlay helpers, battle target/action dispatch, status and resource
effects, PSI/item effect implementations, battle text consequences, battle
background/palette effects, enemy sprite loading, and battle palette tails.

Primary artifacts:

- `notes/bank-c2-progress-audit.md`
- `notes/bank-c2-working-name-proposals.md`
- `notes/data-contracts-c0-c4.md`
- `src/c2/bank_c2_helpers_asar.asm`
- `notes/bank-c2-source-scaffold-handoff.md`

## Source scaffold status

Bank `C2` is structurally closed for the source-scaffold phase:

- range manifest: `build/c2-build-candidate-ranges.json`
- residual map: `notes/c2-source-residual-map.md`
- byte-equivalence report: `notes/c2-byte-equivalence-validation.md`
- validation: `C2 byte-equivalence: OK, 212 module(s), 0 mismatch(es).`

The current scaffold is working-name anchored: each interval between known C2
labels is preserved as exact ROM bytes. This is byte closure, not final
semantic source; the next phase is replacing battle-runtime corridors with
decoded source while keeping the same validation loop.

The audit currently reports:

- reference include entries: `406`
- reference address-bearing include entries: `86`
- address-bearing unknown include entries: `86`
- local notes mention `563` distinct `C2:xxxx` addresses
- reference addresses mentioned by local notes: `90 / 90`
- unknown include entries not directly mentioned in local notes: `0`

## Bank layout

The current high-level C2 subsystem map is:

- `C2:00B9..108C`: HP/PP window, title/window buffer, menu scan, event-state
  snapshot/restore, HP/PP roller, and early symbol-only utility helpers.
- `C2:16AD..307B`: party/inventory/status corridor, including music state,
  party overlay arbitration, event flags, derived equipment/stat recalculation,
  inventory transfer, and temporary party-state save/restore.
- `C2:30F3..654C`: battle setup and candidate/target/action front half,
  including battle text context building, second-pointer payload handling,
  stealable-item selection, target selection, encounter text, enemy init,
  instant-win, and Magic Butterfly support.
- `C2:69DE..A821`: class-2 battle action runtime, including masks, afflictions,
  healing, status actions, stat/resource changes, PSI Rockin/Fire/Freeze/Thunder
  common handlers, PSI Flash, Starstorm, recovery, item effects, bombs, and
  special event actions.
- `C2:AF1F..C6F0`: battle consequence and late narrative controllers,
  including reflected-hit normalization, stat/HP/PP consequences, enemy battler
  initialization, PP loss, Final Prayer phases, and special battle sequences.
- `C2:CFE5..E0E7`: battle background load, HDMA/letterbox, palette dim/restore,
  and layer visual setup/teardown.
- `C2:E6B3..EA74`: PSI swirl/battle overlay animation state.
- `C2:EACF..FF9A`: battle effect waits, enemy battle sprite loading, row/order
  assignment, sprite rendering, color-wave palettes, palette loading/dimming,
  and overworld-position hash tail helper.

## Current C2 confidence boundary

High confidence:

- C2 has full local coverage of every reference address-bearing unknown include
  start.
- The bank's central role is battle runtime/action/effect execution, not just
  UI support.
- The C2 notes contain stable names for `211` addresses.
- C2's major table contracts are cross-bank anchored by the C0-C4 data contract
  manifest: `BATTLERS_TABLE`, `BATTLE_SELECTION_SNAPSHOT`,
  `BATTLE_ACTION_TABLE`, `PSI_ABILITY_TABLE`, `ENEMY_CONFIGURATION_TABLE`,
  and loaded battle background state.
- The late battle visual tail is mapped well enough to separate background,
  PSI overlay, enemy sprite, palette, and color-wave responsibilities.

Still intentionally out of scope:

- Final names for every class-2 action leaf and every incidental local branch.
- Full source-grade modeling of all battler status substate bytes.
- Exact decompilation of every battle visual effect script/data payload.
- Treating all `proposed` working names as stable upstream-style symbols.

## Recommended next move

C2 is source-planning ready in slices. The best follow-up is to promote the
table-backed battle contracts first, then extract action families around the
already stable local names: target selection, action dispatch, affliction/status
effects, PSI common handlers, Final Prayer, and battle visual tails.
