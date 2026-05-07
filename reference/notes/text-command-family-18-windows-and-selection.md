# Text Command Family 18 Windows And Selection

This note captures the current best local map for bank-`01` text command family `0x18`.

See also [text-command-family-1a-menus.md](notes/text-command-family-1a-menus.md).
See also [timed-event-slot-block-7440-and-c20abc.md](notes/timed-event-slot-block-7440-and-c20abc.md).
See also [equipment-preview-and-derived-state-cluster.md](notes/equipment-preview-and-derived-state-cluster.md).

## Main result

`0x18` now reads as the bank-`01` text family for window management, window-relative selection helpers, and a small status-display tail.

The ordinary script parser routes it through:

- top-level text parser `C1:890E`
- `0x18 -> C1:8ACC`
- callback family root `C1:790B`

The live ordinary-script case map at `C1:790B` currently covers:

- `0x00`
- `0x01`
- `0x02`
- `0x03`
- `0x04`
- `0x05`
- `0x06`
- `0x07`
- `0x08`
- `0x09`
- `0x0A`
- `0x0D`

So the safest current read is that `0x18` is the family for opening, closing, switching, clearing, and aligning text windows, plus a few menu/status commands that explicitly operate relative to the current window state.

## Local dispatcher proof

The live local `C1:790B` case map is:

- `0x00 -> C1:7954 -> C1:0084`
- `0x01 -> C1:7959 -> C1:43C2`
- `0x02 -> C1:795E`
- `0x03 -> C1:7971 -> C1:43CC`
- `0x04 -> C1:7976 -> C1:008E + C1:0A1D + C1:2DD5`
- `0x05 -> C1:7982 -> C1:4509`
- `0x06 -> C1:7987 -> C1:0FA3`
- `0x07 -> C1:798C -> C1:528D`
- `0x08 -> C1:7991 -> C1:5529`
- `0x09 -> C1:7996 -> C1:554E`
- `0x0A -> C1:799B -> C1:AA18`
- `0x0D -> C1:79A0 -> C1:5B46`
- default -> `0`

Parser/runtime cross-check now looks healthy:

- the stable live center matches the community control-code docs unusually well
- `0x08` and `0x0D` are runtime-only in currently exposed parsed hits, but both have strong local bodies and good doc alignment

## Source scaffold promotion

The window-relative comparison and selection leaves at `C1:528D`, `C1:5529`, and `C1:554E` are now decoded source in `src/c1/c1_4eab_handle_text_command10_parameterized_pause.asm`. The status-display tail at `C1:5B46` is also decoded in `src/c1/c1_575d_test_equipped_item_presence_for_text_command.asm`. That promotes the `0x18 07`, `0x18 08`, `0x18 09`, and `0x18 0D` local bodies from byte-preserved corridors into byte-equivalent checked-in source.

Source polish follow-up (2026-05-06): the `C1:790B` dispatcher front inside
`src/c1/c1_78f7_start_loaded_string_inline_collector.asm` now names its
helper-call and callback-return edges directly. `0x18 00/04/06/0A` call the
close-focus, close-and-drain, hide-HP/PP, text-tick, clear-active-window, and
wallet/status refresh helpers by name; `0x18 02` names the `C20A20` managed
slot snapshot helper before activating `slot + 4`; and `0x18 01/03/05/07/08/09/0D`
return named callback low words for the open-window, switch-window,
force-alignment, register-compare, window-selection, and status-display leaves.

Source polish follow-up (2026-05-06): that dispatcher front now names the
selector comparisons themselves too. The live `0x18` window-family ladder is
source-facing for `00/01/02/03/04/05/06/07/08/09/0A/0D`, and the managed-slot
branch names the saved callback-frame pointer it later writes at `+4`.

Source polish follow-up (2026-05-06): the `0x18 07` comparison body at
`C1:528D` now names the queued source bytes and callback return inside the leaf
itself. The source reads `$97BA..$97BD` as the four assembled comparison bytes,
then compares the result against either the active text-context value, the next
text argument, or current work memory depending on the caller selector.

Source polish follow-up (2026-05-06): the `0x18 0D` status-window body at
`C1:5B46` now names its one-byte deferred character selector and callback
return inside the leaf. The body still leaves the submode split cautious, but
the staged selector and status-window display handoff now use the same source
vocabulary as the adjacent inventory/money callback leaves.

Source polish follow-up (2026-05-06): the same `0x18 0D` leaf now names its
preserved caller submode slot as `StatusWindowDisplayModeArgument`. That keeps
the source clear about the split between the deferred character selector and
the display-mode argument used to choose the status-rendering branch.

Source polish follow-up (2026-05-06): the adjacent `0x18 05` forced-alignment
leaf at `C1:4509` now names its one-byte queued argument, queue count,
self-return callback low word, low-byte mask, and C4 glyph-versus-cursor staging
helpers in the source unit that also houses `CALL_TEXT`.

Source polish follow-up (2026-05-06): the shared temporary-focus selector at
`C1:9A11` now names the saved focus/window selector, preserved selection mode,
and restored selection result around the managed text-event slot snapshot. The
routine remains a generic UI caller helper; this pass only makes its local ABI
visible to the `0x18`/`0x1A` selection-family call sites.

## Best current case map

### `0x18 00`

Best current read:

- close current window

Confidence:

- locally strong

Why:

- exact parsed hits are abundant
- local leaf is the compact close-window helper `C1:0084`
- community docs match the observed usage cleanly

### `0x18 01`

Best current read:

- open text window

Confidence:

- locally strong

Why:

- exact parsed hits are abundant
- local leaf is `C1:43C2`
- scripts use the single byte argument exactly like a window type id

### `0x18 02`

Best current read:

- save text window state

Confidence:

- locally strong; reference-backed and locally consistent on exact semantics

Why:

- local body `C1:795E` snapshots `current_callback_slot + 6` through `C20A20` and then writes `1` to `slot + 4`
- this is the same timed-event slot infrastructure already mapped in [timed-event-slot-block-7440-and-c20abc.md](notes/timed-event-slot-block-7440-and-c20abc.md)
- the source now names this helper edge as
  `C20A20_SnapshotManagedTextEventSlotState`
- exact parsed hits cluster in `ESHOP1/2/3` and `EDEBUG`, where later rendering/menu flows clearly rely on saved window context
- community docs describe it as saving cursor position, font, color, and number-padding state for later restoration

So the safest current local read is that `0x18 02` is the generic save-current-window-context helper.

### `0x18 03`

Best current read:

- switch to window

Confidence:

- locally strong

Why:

- exact parsed hits are abundant
- scripts pass a single window id byte
- local leaf is `C1:43CC`, the clear sibling of the open-window leaf

### `0x18 04`

Best current read:

- close all windows

Confidence:

- locally strong

Why:

- exact parsed hits are abundant
- local body `C1:7976` chains the close/reset side through `C1:008E`, `C1:0A1D`, and `C1:2DD5`
- community docs match the observed broad use before movement, teleport, and scene transitions

### `0x18 05`

Best current read:

- force text alignment

Confidence:

- reference-backed and locally consistent

Why:

- exact parsed hits are abundant, especially in keyboard/status/menu contexts
- local leaf is `C1:4509`
- community docs describe its two arguments as forced X/Y alignment inside the current window, which fits usage unusually well

### `0x18 06`

Best current read:

- clear current window

Confidence:

- locally strong

Why:

- exact parsed hits exist in battle text
- local body `C1:7987 -> C1:0FA3` is a real active-window clear path

### `0x18 07`

Best current read:

- compare window register to number

Confidence:

- reference-backed and locally consistent

Why:

- exact parsed hits are abundant, especially in `EDEBUG`
- local leaf `C1:528D` now clearly builds the compare value from `$97BA/$97BB/$97BC`, compares it against one of three local text-register sources, and stages a three-way result `0/1/2` through `C1:045D`
- community docs describe it as a comparison against one of the text/window register domains, returning a small comparison result

The local source split is now clearer too:

- selector `0` uses `C1:040A`, the live `+0x17` pointer slot
- selector `1` uses `C1:03DC`, the live `+0x1B` sibling pointer slot
- selector `2` falls through `C1:0400`, the live `+0x1F` companion selector/control word

So the community wording about three window/text register domains still fits the ROM well, even though I am keeping the final human-facing names slightly cautious until those three domains are described in one dedicated local note instead of only through their callers.

### `0x18 08`

Best current read:

- selection menu in window, no cancelling

Confidence:

- reference-backed and locally consistent

Why:

- live local case exists through `C1:5529`
- its immediate helper pattern is the close sibling of `0x18 09`
- community docs describe it as the no-cancel window-relative selection-menu variant

Caution:

- no exact currently exposed parsed hits

### `0x18 09`

Best current read:

- selection menu in window

Confidence:

- locally decent; reference-backed and locally consistent

Why:

- exact parsed hits exist in `ESHOP1`
- those scripts call `0x18 09 0x02` immediately after inventory display and then branch on the result, exactly the way a window-relative selection menu would
- local body `C1:554E` is the cancellable sibling of `0x18 08`, built on the same queue/callback framework
- community docs describe it as the window-relative variant of the ordinary selection menu

### `0x18 0A`

Best current read:

- show wallet window

Confidence:

- locally strong

Why:

- exact parsed hits are abundant in stores and phone flows
- local body `C1:799B -> C1:AA18`
- community docs match the observed shop/telephone usage cleanly

### `0x18 0D`

Best current read:

- print character status info

Confidence:

- locally decent; reference-backed and locally consistent

Why:

- live local case exists through `C1:5B46`
- `C1:5B46` takes a character id, resolves a working-memory fallback when needed, and then branches by a small selector in `Y` to status-oriented helpers (`C1:952F` and `C3:EF23`) before returning to text memory
- `C1:952F` is now source-backed as `RenderCharacterStatusWindowBlock` inside `src/c1/c1_9437_close_target_selection_prompt_label.asm`; the helper renders the status block through the existing fixed-string, decimal, glyph, and HP/PP status-tile helpers
- exact parsed hits are not currently exposed, but the community docs give a very plausible user-facing read: open status window 8 and display a character's status block there

I am keeping the exact submode semantics cautious until more direct script usage turns up.

## Current safest interpretation

The safest current interpretation is:

- `0x18` is the bank-`01` text family for window management and a few menu/status helpers that are explicitly tied to current window state
- the stable locally proved center is:
  - close/open/switch/close-all/clear window
  - save current window state
  - show wallet window
- the stable reference-backed-and-locally-consistent tail is:
  - force text alignment
  - compare window register to number
  - selection menu in window
  - print character status info

## Best next target

The best next move is to pin the exact user-facing semantics of `0x18 0D` from one concrete status-window caller, since both `0x18 07` and `0x18 0D` now have source-backed queued-byte bodies.
