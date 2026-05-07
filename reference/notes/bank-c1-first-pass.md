# Bank C1 First Pass

## Main result

Bank `C1` is the text/menu/UI coordination bank with substantial battle-facing
front-end work. It owns the text engine and text command VM surface, window and
selection helpers, inventory/equipment/item naming front ends, PSI and target
selection menus, battle text entry wrappers, file-select menus, text input, and
name-entry/file-select tail glue.

Primary artifacts:

- `notes/bank-c1-progress-audit.md`
- `notes/bank-c1-subsystem-and-symbol-synthesis.md`
- `notes/bank-c1-working-name-proposals.md`
- `src/c1/bank_c1_helpers_asar.asm`
- `notes/bank-c1-source-scaffold-handoff.md`

## Source scaffold status

Bank `C1` is structurally closed for the source-scaffold phase:

- range manifest: `build/c1-build-candidate-ranges.json`
- residual map: `notes/c1-source-residual-map.md`
- byte-equivalence report: `notes/c1-byte-equivalence-validation.md`
- validation: `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

The current scaffold is working-name anchored: each interval between known C1
labels is preserved as exact ROM bytes. This is byte closure, not final
semantic source; the next phase is replacing text/menu/UI corridors with
decoded source while keeping the same validation loop.

The audit currently reports:

- reference include entries: `427`
- reference address-bearing include entries: `132`
- address-bearing unknown include entries: `131`
- local notes mention `695` distinct `C1:xxxx` addresses
- reference addresses mentioned by local notes: `132 / 132`
- unknown include entries not directly mentioned in local notes: `0`

## Bank layout

The current high-level C1 subsystem map is:

- `C1:0000..2E42`: text engine core, window loop, low-level print/render
  primitives, character select prompt, and window tick/debug hooks.
- `C1:339E..4070`: field menu prelude, debug menu hooks, timed-event callback
  dispatch, and early text-command leaves.
- `C1:4070..81BB`: EB text command dispatcher leaves, including event flags,
  jumps, argument/secondary/work memory, inventory/money, stat recovery,
  teleport, timed events, and special events.
- `C1:866D..9F29`: inventory, item names, equipment display, item slot
  insertion/removal/search helpers, and item/PSI display front ends.
- `C1:A1D8..AAFA`: equipment menu controller and derived equipment cache flows.
- `C1:AAFA..BEFC`: battle/field choice text, targetting, field PSI/teleport
  destination picker, and special event dispatch.
- `C1:C046..CFC6`: battle PSI and item selection, including PSI row formatting,
  category lists, selection refresh, PP gates, item-action resolution, and the
  small Jeff repair item mapper at `C1:D038`.
- `C1:D08B..D76D`: level-up growth helpers and stat-gain narration leaves.
- `C1:DC1C..DD9F`: battle text display wrappers and context-buffer rebuilds.
- `C1:E1A2..EC8F`: enemy select, text input, naming buffer commits, and window
  flavor preview.
- `C1:ECDC..FFFF`: save corruption/file-select/setup menu bodies, text-speed,
  sound/flavor options, file-select session entry, layout callback, and SRAM
  checksum tail glue.

## Current C1 confidence boundary

High confidence:

- C1 has full local coverage of every reference address-bearing unknown include
  start.
- The bank's main role is text/menu/UI coordination with battle and file-select
  front ends.
- The text command dispatcher and many menu/naming/inventory/equipment families
  have direct focused notes and working-name proposals.
- C1's battle-facing PSI/item/text routines are strongly cross-linked with C2,
  D5, and EF table/text consumers.

Still intentionally out of scope:

- Treating every proposed working name as final source nomenclature.
- Full source-ready struct naming for file-select/session state bytes.
- Full semantic closure of C1 routines whose proof depends on deeper C2 battle
  internals or C4 renderer internals.
- Rebuilding the whole CCS/text VM as source; the dispatcher leaves are mapped,
  but source-grade VM documentation remains a larger phase.

## Recommended next move

C1 is ready for source-extraction planning as a set of subsystem slices. The
best follow-up is not more discovery, but promotion: choose high-traffic working
names, pair them with C2/C4 consumer proof, and emit source labels/contracts for
the text/menu/file-select paths that already have stable notes.
