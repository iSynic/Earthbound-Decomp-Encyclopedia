# Bank `01` Text Command Map `00..1F`

This note is the current top-level map of the ordinary bank-`01` text command range `0x00..0x1F`.

See also [lower-bank01-text-control-strip-00-17.md](notes/lower-bank01-text-control-strip-00-17.md).
See also [text-command-family-18-windows-and-selection.md](notes/text-command-family-18-windows-and-selection.md).
See also [text-command-family-19-data-and-substitution.md](notes/text-command-family-19-data-and-substitution.md).
See also [text-command-family-1a-menus.md](notes/text-command-family-1a-menus.md).
See also [text-command-family-1b-memory-context.md](notes/text-command-family-1b-memory-context.md).
See also [text-command-family-1c-print-display.md](notes/text-command-family-1c-print-display.md).
See also [text-command-family-1d-inventory-money.md](notes/text-command-family-1d-inventory-money.md).
See also [text-command-family-1e-stat-recovery.md](notes/text-command-family-1e-stat-recovery.md).
See also [text-command-family-1f-deferred-callbacks.md](notes/text-command-family-1f-deferred-callbacks.md).

## Main result

The ordinary bank-`01` text command range now reads as a coherent layered command map rather than a flat list of parser macros.

The strongest current high-level split is:

- `0x00..0x17` = low-level control, flag, branch, memory, and parser-side helper strip
- `0x18..0x1F` = structured higher families for windows, substitution/data, menus, memory/context, print/display, inventory/status, stat recovery, and deferred callbacks

A useful caution also survives at the top level: `0x15..0x17` are best treated as compressed-bank parser pseudo-opcodes, not ordinary runtime families.

## Lower control strip `00..17`

The current safest map for the lower strip is:

- `0x00` = `LINE_BREAK`
- `0x01` = `START_NEW_LINE`
- `0x02` = `END_BLOCK`
- `0x03` = `HALT_WITH_PROMPT`
- `0x04` = `SET_EVENT_FLAG`
- `0x05` = `CLEAR_EVENT_FLAG`
- `0x06` = `JUMP_IF_FLAG_SET`
- `0x07` = `CHECK_EVENT_FLAG`
- `0x08` = `CALL_TEXT`
- `0x09` = `JUMP_MULTI`
- `0x0A` = direct 24-bit `JUMP`
- `0x0B` = parameterized `TEST_IF_WORKMEM_TRUE`
- `0x0C` = parameterized `TEST_IF_WORKMEM_FALSE`
- `0x0D` = parameterized `COPY_TO_ARGMEM`
- `0x0E` = parameterized `STORE_TO_ARGMEM`
- `0x0F` = parameterized `INCREMENT_WORKMEM`
- `0x10` = parameterized `PAUSE`
- `0x11` = selection-menu setup helper
- `0x12` = line/menu display control helper
- `0x13` and `0x14` = the later halt/control pair through `C1:0166`
- `0x15..0x17` = compressed-bank parser pseudo-opcodes

So the lower strip is now much cleaner than the inherited parser view suggested: it is mostly a compact control and state-manipulation layer, not a set of mini-families.

## Structured family strip `18..1F`

The structured upper families now read as:

- `0x18` = windows and selection helpers
- `0x19` = data loading, substitution, fixed-width buffer selectors, and statistic selectors
- `0x1A` = menu and menu-display family
- `0x1B` = memory / context manipulation family
- `0x1C` = print / display family
- `0x1D` = inventory / money / storage / equipment helper family
- `0x1E` = HP/PP/stat recovery and stat-add family
- `0x1F` = deferred callback and event-helper family

The live family roots in the ordinary parser path are:

- `0x18` -> `C1:790B`
- `0x19` -> `C1:79AA`
- `0x1A` -> `C1:7B56`
- `0x1B` -> `C1:7C36`
- `0x1C` -> `C1:7D94`
- `0x1D` -> `C1:7F11`
- `0x1E` -> `C1:811F`
- `0x1F` -> `C1:81BB`

Source polish follow-up (2026-05-06): the top-level parser source in
`src/c1/c1_87cc_invoke_text_engine_callback_low_word.asm` now names these
callback roots directly, along with the lower-strip callback roots for
`0x04..10`. The same pass gives cautious names to the compressed-bank pointer
tables used by pseudo-opcodes `0x15..17`, matching the caution above that those
three entries are not ordinary runtime families.

Source polish follow-up (2026-05-06): the adjacent dynamic source-selector
source now names the returned low-word leaves behind the `0x1A`, `0x1C`,
`0x1D`, `0x1E`, and `0x1F` family dispatchers. The labels are local callback
contracts only; they preserve the same return values while making the menu,
display, inventory/money, stat-recovery, and deferred-callback tables readable
without relying on bare addresses.

Source polish follow-up (2026-05-06): the deferred callback leaf bodies now use
the same naming at the consumer side. The shared queued-byte block
`$97BA..$97BE/$97CA` is named in the `1F C0` and adjacent `1F` callback tail,
and the late `1E` stat-recovery leaves now name their staged bytes and target
character-record fields.

Source polish follow-up (2026-05-06): the lower queued leaves now share that
consumer-side vocabulary too. The `0x1D 08/09`, `0x1E 00..07`, `0x1D 00/01`,
`0x1F 81`, `0x1D 0D/0E/0F`, `0x18 07`, `0x1A 05`, and `0x1C 0A/0B` bodies
name their queued-byte slots and callback self-returns, tightening the contract
between family dispatchers and the callback leaves without changing emitted
bytes.

Source polish follow-up (2026-05-06): the same queued-selector names now cover
the previously raw front possession checks in `C1:4CEE..4EAB`: `0x1D 04`,
`0x1D 05`, and adjacent `0x1F 20` stage a one-byte selector in `$97BA`, count
it with `$97CA`, and return through named self-callback low words instead of
raw literals.

Source polish follow-up (2026-05-06): the `C1:575D..621F` continuation now
uses the same vocabulary for the next dense strip. This covers `0x1D
10/11/12/13/14/15/17`, `0x18 0D`, `0x19 19/1C/1D`, and the adjacent `0x1F
71/83` callback leaves, including the shared money-byte assemblers and the
wallet/ATM comparison state.

Source polish follow-up (2026-05-06): the lower control strip now has matching
consumer-side names too. The `0x04..0x08`, `0x0A`, and adjacent `0x18 05`
callback bodies name their queued-byte slots, queue count, callback self-return
low words, 24-bit assembly scratch, event-flag staging, and call-text or
forced-alignment output slots.

Source polish follow-up (2026-05-06): the lower `0x1F` consumer corridor now
also names packed-payload assembly for `1F 63` and `1F 66`, plus the paired
selector assembly for `1F F1/F2`. The callback low words are unchanged, but
the movement-record, hotspot-activation, visual-script, and pose-script
handoffs are now readable at the source boundary.

Source polish follow-up (2026-05-06): the same `0x1F` corridor now promotes
the neighboring entity-helper callback names rather than leaving them as
numbered callback placeholders. The dispatcher and callback source now name the
`13..1F` frame-selector, dynamic visual entity, attached-child, no-op absorber,
and cached-pose script leaves, plus the `E1/E4..EF` landing-profile, C4 entity
flag, registry `8000`, and mode-slot selector leaves.

Source polish follow-up (2026-05-06): the remaining named-but-generic `0x1F`
low-word returns now expose their contracts as well: text sound mode,
presentation SFX, scripted-battle init, blinking-triangle state, movement
record enqueue, hotspot activation/disable, record-backed visual/pose scripts,
and pose-descriptor attached-child spawn/clear. This leaves the high-family
callback map readable by behavior rather than by numbered placeholders.

Source polish follow-up (2026-05-06): the adjacent `0x19 25` and `0x1D 0C`
consumer leaves in `C1:6F9F..711A` now expose their result staging too. The
condiment helper and Escargo storage-status classifier both install their
outputs through the shared text-context result pair instead of bare direct-page
scratch names.

Source polish follow-up (2026-05-06): the same corridor now names `1F 23` and
`19 26` staging. The scripted-battle init leaf shows its queued selector and
signed result install, while the transition-landing snapshot leaf is labeled at
`C1:7037` with its direct-argument fallback into `C2:30F3`.

Source polish follow-up (2026-05-06): the dynamic source selector dispatcher at
`C1:7B56..866D` now exposes the family-specific caller-frame offsets for
`0x1A`, `0x1B`, `0x1C`, `0x1D`, and `0x1F`. The front `1A/1B` result and
context reinstall sites now use the same `$0E/$10` text-context source pointer
aliases used by the print/display and predicate leaves, keeping the dispatcher
ABI readable across all high families.

Source polish follow-up (2026-05-06): the top-level invoker/parser root at
`C1:87CC..8B2C` now names its local callback ABI and lower-strip leaves. The
source exposes `$1E` as the active same-bank callback low word, `$14` as the
current callback argument or opcode byte, and `$12` as the managed text-event
slot pointer. It also names the `0x15..17` compressed-bank pseudo-opcode
resolver paths and the `0x11` selection-menu context installer, so the lower
control strip now reads from the same source-facing contract vocabulary as the
deferred `0x1F` callback leaves.

The same pass replaced the root dispatcher's raw compare literals with
`TextOpcode*` aliases through `0x1F`, including the `0x15..17` compressed-bank
sentinels and the first literal-glyph cutoff at `0x20`.

## Pairings and system shape

A few family pairings are now important enough to state at the top level:

- `0x1B` and `0x1C` are the core memory/display pair.
  `0x1B` manipulates live and saved text-context slots, while `0x1C` reads and displays from those slots.
- `0x09` and `0x0A` are the lower control-flow core.
  `0x09` is multi-way branch, and `0x0A` is direct 24-bit jump.
- `0x1D` and `0x1E` sit on top of the character/item/stat record families rather than acting like generic text helpers.
- `0x1F` is broader than timed delivery alone.
  It is the deferred-callback / event-helper family that also covers Jeff repair, magic-truffle direction, and wandering-photographer behavior.

## Best current interpretation

The safest current interpretation is that bank `01` text commands are now mapped well enough to be treated as a real runtime architecture:

- a low control strip at `0x00..0x17`
- a structured family strip at `0x18..0x1F`
- parser-only compressed-bank pseudo-opcodes at `0x15..0x17`

That gives the project a stable command-map backbone for future subsystem work instead of forcing every new text-engine question to start from raw opcode lists.
