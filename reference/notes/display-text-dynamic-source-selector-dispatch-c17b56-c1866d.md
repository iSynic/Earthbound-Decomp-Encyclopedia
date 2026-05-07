# Display-Text Dynamic Source Selector Dispatch (`C1:7B56-C1:866D`)

This note captures the current best local model for the `C1:7B56..866D`
display-text dynamic source selector corridor.

See also:

- [class2-c1-display-text-substitution-handler-7af3.md](notes/class2-c1-display-text-substitution-handler-7af3.md)
- [text-command-family-1a-menus.md](notes/text-command-family-1a-menus.md)
- [text-command-15-compressed-bank-1-pseudo-opcode.md](notes/text-command-15-compressed-bank-1-pseudo-opcode.md)
- [text-command-16-compressed-bank-2-pseudo-opcode.md](notes/text-command-16-compressed-bank-2-pseudo-opcode.md)
- [text-command-17-compressed-bank-3-pseudo-opcode.md](notes/text-command-17-compressed-bank-3-pseudo-opcode.md)

## Source Promotion Status

- Promoted to decoded assembly source:
  - `src/c1/c1_7b56_dispatch_display_text_dynamic_source_selector.asm` (`C1:7B56..C1:866D`)
- Intended validation:
  - `python tools\\validate_source_bank_byte_equivalence.py --bank C1 --module all --combined --scaffold src\\c1\\bank_c1_helpers_asar.asm --strict`

## Entry Points

- `C1:7B56` = `DispatchDisplayTextDynamicSourceSelector`

## High-level Behavior (Current Read)

- The first local routine at `C1:7B56` is a narrow dispatcher that branches on
  small selector values and routes into a menu/selection-oriented helper set.
  The best current map is recorded in `notes/text-command-family-1a-menus.md`.
- The source now names the shared menu/result staging edges inside that first
  routine: the active text-entry selection loop, loaded-text-string clear,
  Escargo storage, phone-contact, teleport-destination, and primary text-context
  install helpers.
- A follow-up pass also names the `0x1A` subselector ids, the cancellable versus
  uncancellable `C1:196A` selection-loop mode values, the no-follow-up return
  value, and the local `$06/$08` menu result staging pair before it is installed
  as the primary text context.
- The adjacent `0x1B` memory/context dispatcher now names its `1B 01..06`
  subselector ids, null primary-context branch tests, four-byte jump-target
  skip, saved parser argument pointer, primary/secondary context staging pairs,
  swap temporaries, and `$97CC..$97D4` scratch context snapshot.
- The battle-facing display leaves now name the `0x1C 0D/0E/0F` contract:
  reflected-hit side article-token setup, attacker/target name-buffer base
  reads, fixed-string preflight printing, and the `$9D12/$9D14` amount pointer
  consumed by the decimal printer.
- The front `0x1C` dispatcher also names its stable subselector ids for
  `01..0F` and `11..15`, plus the battle user/target selector values,
  staged name-buffer pointer bytes, text-context handoff pair, fixed-string
  preflight length, and no-follow-up return value.
- The adjacent `0x1D` inventory/money dispatcher now names its live
  subselector ids for `01..15`, `17..19`, and `20..24`, while keeping the
  absent `16` and parser-artifact `1C` gaps visible. Its inline `20` and `22`
  predicate bodies also name their boolean result staging, battle name-buffer
  comparison, current map-position inputs, map-class mask, and exit-mouse class.
- The adjacent `0x1E` recovery/stat dispatcher now names its live `01..0E`
  subselector ids, keeps `00` as the zero branch to HP-percent recovery, and
  uses the shared no-follow-up return for anything outside the live range.
- The `0x1F` deferred-callback/event dispatcher now names its wide selector
  ladder from the low music/sound strip through the `F4` tail, including
  callback leaves, immediate helper leaves, and the shared no-follow-up return.
- The later `1F` command corridor now names the text-context snapshot/restore,
  primary/secondary context loads and installs, text input lock/unlock, wait
  gate, transition music restore, interaction-flag helpers, save-current-game
  wrapper, and teleport landing state refresh edges.
- The immediate `1F` helper leaves now also name the C1-side staging behind
  teleport landing snapshot/refresh, phone-contact result installation,
  current-interaction flag set/clear/get, and nearby Magic Truffle direction
  result installation.
- The remaining presentation/runtime joins in this source are now named too:
  map-position context lookup, auto sector-music latch writes, the active-window
  glyph-mode flag helper at `C1:0FAC`, nearby Magic Truffle direction lookup,
  selected-mode slot clear, and the C0 bicycle-entry helper.
- The broader corridor through `C1:866D` decodes cleanly as linear 65816 code
  (no embedded tables required for byte-equivalence), and this source no longer
  has raw `jsr $...` or `jsl $...` edges.
