# C1 File-Select Runtime Polish

This note records the byte-neutral C1 file-select polish slice. It promotes the
runtime contracts around save-slot state, action/copy/delete menus, setup
settings, window-flavour preview, and the bank-C1 file-select session wrapper.

Primary source modules:

- `src/c1/c1_ec8f_preview_window_flavour_and_redraw.asm`
- `src/c1/c1_ecd1_preview_packed_high_byte_window_flavour.asm`
- `src/c1/c1_f07e_open_file_select_action_menu.asm`
- `src/c1/c1_f14f_open_copy_destination_menu.asm`
- `src/c1/c1_f2a8_open_delete_file_confirmation_menu.asm`
- `src/c1/c1_f497_open_or_refresh_text_speed_selection.asm`
- `src/c1/c1_f616_open_or_refresh_sound_setting_selection.asm`
- `src/c1/c1_ff2c_update_lead_entity_type_redraw_flag.asm`
- `src/c1/c1_ff6b_run_file_select_session.asm`
- `src/c1/c1_ff99_compute_centered_text_layout_metric.asm`

Related evidence notes:

- `notes/file-select-window-flavour-refresh-c1ec8f-ecd1.md`
- `notes/file-select-action-copy-delete-menus-c1f07e-f14f-f2a8.md`
- `notes/file-select-setup-option-menus-c1f497-c1f616.md`
- `notes/file-select-tail-helpers-c1ff2c-ff6b-ff99.md`

## Save-Slot State

`C1:ED5B` builds the visible three-slot file-select menu and records slot state
in `$B49E..$B4A0`.

- nonzero byte = valid save slot
- zero byte = empty or invalid slot

The selected 1-based slot is stored in `$B4A1` by `C1:F03E` before the routine
returns the selected slot after an EF checksum probe. The corrupt-save notice at
`C1:ECDC` consumes and clears `$9F79`.

`C1:ECD1` is only a packed-row adapter for window-flavour preview: it extracts a
high byte and forwards it to `C1:EC8F`. `C1:EC8F` temporarily writes `$99CD`,
runs the C4 redraw sequence, marks `$0030 = 0x18`, and restores the previous
window-flavour byte.

## Action Menus

`C1:F07E` opens file-select action window `0x14`. It always inserts Continue,
Delete, and Set Up, and inserts Copy only if a non-current slot in
`$B49E..$B4A0` is empty.

The menu result contract is:

| Result | Meaning |
| --- | --- |
| `0` | cancel / close |
| `1` | continue selected file |
| `2` | copy selected file |
| `3` | delete selected file |
| `4` | setup |

`C1:F14F` opens the copy destination menu. It chooses compact window `0x16` when
there is exactly one destination and window `0x15` otherwise. A nonzero
selection calls `EF:0C15(current_slot - 1, destination - 1)`.

`C1:F2A8` opens delete confirmation window `0x17`. It prints `$B4A1`, the
selected-file character summary, and `$99D3` as the level byte. A nonzero
confirmation calls `EF:0BFA(current_slot - 1)`.

## Setup Settings

`C1:F3C2` builds the text-speed menu in window `0x18` and selects `$98B6`.
`C1:F497` is the wrapper around that menu:

- A == 0: run the selection loop, write a nonzero result to `$98B6`, and call
  `EF:0A4D(current_slot - 1)`
- A != 0: rebuild/redraw the current `$98B6` row without prompting

`C1:F568` builds the sound menu in window `0x19`, and `C1:F616` is the matching
wrapper for `$98B7`. It persists through the same `EF:0A4D` setup-state helper.

`C1:F6E3` builds the window-flavour menu in window `0x32`, previews candidate
rows through `C1:EC8F`, commits `$99CD` on nonzero selection, and persists setup
state through `EF:0A4D`.

The setup source now also names the local UI caller contract around these
wrappers: active focus `$8958`, descriptor lookup through `$88E4/$8650+0x2B`,
the `$89D4` text-entry chain stride and selected-row text offsets, cancel
results passed between the three setup stages, and the explicit `C1:EC8F`
preview callback low/bank pair used by the window-flavour menu.

The visible action/copy/delete/setup menu builders now also name their C4
file-select text pointer lows and bank word in source. This covers the action
labels, copy-destination prompt and generated slot-label buffer, delete
confirmation prompt/options, text-speed prompt/options, sound prompt/options,
and window-flavour prompt/options.

The new-file naming and confirmation branch inside `C1:F616` now names the
same caller-side text contract. The source exposes the `C4:C194` 0x28-byte
prompt table, character-record stride/base for the four party-name commits,
the fixed `$9819/$981F/$9829` pet/food/thing commit buffers, and the
confirmation-screen labels/options at `C4:C2AC..C2D9`. This keeps the C4 data
source untouched while making the C1 text-entry caller contract explicit.

The new-file initialization tail also names its caller-side startup contracts.
`C1:FD0E..FEC2` now exposes the `D5:F5F5` initial-stats table pointer, the
row offsets consumed by the C1 party setup loop, the HP/PP rolling display
fields initialized from `$99D8/$99DA`, the inventory seed and starting-money
loads, the fixed `"PSI "` prefix at `$9825..$9828`, the `$98B8/$9D1F/$9D21`
landing snapshot, the C5 start-script pointer, and the C3 text-speed timing
table used to populate `$9625/$9627/$9629/$964B` before the C7 start-file text
handoff.

The source now names that persistence edge as `EF0A4D_SaveGameSlot`, matching
the EF save/SRAM contract: C1 passes the visible one-based slot minus one, and
EF expands it to the primary/backup save-block pair.

The setup triad is therefore:

| Setting | State byte | Window | Builder/wrapper |
| --- | --- | --- | --- |
| text speed | `$98B6` | `0x18` | `C1:F3C2` / `C1:F497` |
| sound | `$98B7` | `0x19` | `C1:F568` / `C1:F616` |
| window flavour | `$99CD` | `0x32` | `C1:F6E3` / `C1:EC8F` |

## Session Flow

`C1:F805` is the file-select menu loop. Existing save slots dispatch through
the action menu; empty slots enter the new-file setup and naming flow. Continuing
an existing save calls the C0/C7 setup path through `C0:64D4`, `C0:7213`, and
the shared start-file tail at `C1:FEC2`.

The `C1:F805` source now names the local action/copy/delete/setup helpers
directly (`C1:F07E`, `C1:F14F`, `C1:F2A8`, `C1:F3C2`, `C1:F497`,
`C1:F568`, and `C1:F6E3`). The new-file branch also calls the C4 file-select
pose/entity helpers and C3 party-overlay sync by contract names. A later
source-polish follow-up also named the `C1:D9E9` experience-award handoff used
while initializing the new-file party records, so this file-select source unit
now has no raw helper-call edges outside the deliberately deferred local
character-selection dispatcher.

`C1:FF6B` is the bank-C1 file-select session wrapper. It clears `$5E6E`, sets
`$B49D`, runs `C1:F805`, pumps post-loop display updates, clears `$B4B6/$B4A2`,
restores `$5E6E = 0x00FF`, clears `$B49D`, and returns zero.

`C1:FF2C` is the lead-entity redraw predicate used near the file-select return
path. It reads object byte `+0x0E` for the active lead party entity, maps values
1 and 2 to transient state 1, maps all other values to state 0, stores `$B4A2`,
and returns 1 only when that state changed.

`C1:FF99` is adjacent bank-end renderer glue rather than file-select control
logic. It measures a C4 text/control value, centers it against incoming X
multiplied by 8, and stores fine/coarse metrics in `$9E23/$9E25`.

## Decomp Value

This slice makes the file-select path useful to future SRAM/setup work:

- save-slot validity, selected slot, and action-menu results now have local
  runtime contracts in source comments
- EF save helpers are linked to the exact UI paths that call them
- setup bytes `$98B6`, `$98B7`, and `$99CD` are tied to their preview, commit,
  and persistence paths
- the setup UI wrappers now expose their window ids, cancel contract, active
  descriptor lookup, text-entry selected-row offsets, and window-flavour
  preview callback pointer as source names
- visible C4 file-select menu text pointers now have local source names without
  leaving the new-file naming confirmation tail as raw C4 pointer loads
- new-file startup now names its D5 initial-stats row consumers, favorite-thing
  prefix seed, landing snapshot, start-script handoff, and text-speed timing
  state updates
- the bank-C1 session wrapper and transient redraw latch are separated from the
  larger menu loop
- the main file-select loop now has named source edges for its submenu
  dispatch, setup-menu backtracking, file-select pose/entity refresh, and final
  party-overlay sync
- the save-slot and window-flavour selection loops now name their preview row
  formatter callback installs through the shared `C1:1F5A` `$0E/$10` callback
  ABI, including the save-slot corruption/preview adapter at `C1:ECD1` and the
  setup-window flavour preview callback at `C1:EC8F`
- the `C1:ECD1..F07E` save-slot menu source now also names the corrupt-save
  notice loop index, battle-text substitution source, slot-choice mode,
  save-slot row index, one-based row result, packed row metadata, text-entry
  source/metadata, C4 copy source/destination pairs, level decimal source,
  preserved print buffer, and active text-entry pointer used for selected-slot
  redraws
- the setup-menu wrappers at `C1:F616` and `C1:F6E3` now name their refresh
  mode/result slots, active text-entry pointer, redraw text source,
  window-flavour prompt/option text sources, text-entry metadata, persisted
  setting pointer, and preview-selection result around the shared setup
  selection loops
- the new-file naming loop at `C1:F902..FAAE` now exposes its working/current
  field index pair, advance delta/mirror, party-name destination index, and
  C4 prompt-table pointer/stride staging before each `C1:EC04` naming-buffer
  commit

## Remaining Soft Spots

The main unresolved areas are downstream rather than the C1 control surface:

- final semantic names for the C0/C7 new-file start helpers
- exact object-record byte `+0x0E` vocabulary behind the `C1:FF2C` state map
- further cleanup of the known width-sensitive decode patch inside
  `C1:F6E3`'s cancel/preview tail, without changing its byte model
