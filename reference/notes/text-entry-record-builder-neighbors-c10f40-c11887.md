# Text Entry Record Builder Neighbors (`C1:0F40-C1:1887`)

This note documents the still-unaccounted starts around the bank-`01` text entry builder and active-window text display helpers.

See also [text-entry-builder-c113d1-89d4.md](notes/text-entry-builder-c113d1-89d4.md) for the core `C1:13D1` allocator/installer over the `$89D4` record table.

## Main result

The remaining unknown starts in this range are mostly neighbors of already-understood systems:

Source-scaffold promotion:

- `C1:0F40..134B` is now decoded source in
  `src/c1/c1_0f40_clear_window_content_by_focus_index.asm`.
- `C1:134B..138D` is now decoded source in
  `src/c1/c1_134b_setup_text_display_with_wallet_status.asm`.
- `C1:138D..13D1` is now decoded source in
  `src/c1/c1_138d_count_text_entry_chain_records_local.asm`.
- `C1:13D1..14B1` is now decoded source in
  `src/c1/c1_13d1_install_text_entry_record.asm`.
- `C1:14B1..153B`, `C1:153B..1596`, `C1:1596..15F4`, and
  `C1:15F4..17E2` are now decoded source in their matching text-entry
  constructor modules under `src/c1/`.
- `C1:181B..1887` is now decoded source in
  `src/c1/c1_181b_select_active_text_entry_by_y.asm`.
- `C1:1887..1F8A` is now decoded source in
  `src/c1/c1_1887_select_active_text_entry_by_a.asm`; this includes the
  heavily reused `C1:196A` active text-entry selection/menu loop.
- The promoted source validates through the durable C1 scaffold:
  `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

## Working Names

- `C1:0F40` = `ClearWindowContentByFocusIndex`
- `C1:0C49` = `CountTextEntryChainRecords`
- `C1:134B` = `SetupTextDisplayWithWalletStatus`
- `C1:14B1` = `CreateTextEntryRecordWithDisplayMetadata`
- `C1:153B` = `CreateTypedTextEntryRecord`
- `C1:1596` = `CreateTypedTextEntryRecordWithExtraByte`
- `C1:15F4` = `CreateTypedTextEntryRecordDirect`
- `C1:17E2` = `MeasureBoundedStringLength`
- `C1:181B` = `SelectActiveTextEntryByY`
- `C1:1887` = `SelectActiveTextEntryByA`

- `C1:0F40` is the clear-window-content worker behind the `0x18 06` clear-current-window command.
- `C1:134B` is a compact text/window setup wrapper that runs the `C1:0A04` text-display initializer and then the wallet/status-window helper at `C1:AA18`.
- `C1:14B1`, `C1:1596`, and `C1:15F4` are typed wrappers around the shared `C1:13D1` text-entry allocator.
- `C1:17E2` is a bounded string-length helper.
- `C1:0C49` is the far wrapper over the local `$89D4` linked-list count helper at `C1:138D`.
- `C1:181B` and `C1:1887` select an entry from the active `$89D4` chain and copy one record field back into the live `$8650` context before refreshing display state.

## Clear Current Window Content

`C1:0F40` takes a window/focus index in `A`. If the index is `FFFF`, it returns. Otherwise it resolves:

`A -> $88E4[A] -> $8650 + descriptor * $52`

Then it uses descriptor fields `+0A/+0C` to compute a span through `C0:9032`, walks the descriptor's `+35` buffer pointer, clears existing nonzero tile/state words through `C4:4E4D`, writes `$0040` into each slot, calls `C4:5E96`, and clears descriptor fields `+0E` and `+10`.

The active-window wrapper at `C1:0FA3` simply loads `$8958` and calls `C1:0F40`, which matches the existing `0x18 06` read as "clear current window".

Source polish: `src/c1/c1_0f40_clear_window_content_by_focus_index.asm`
now names the local helper joins used by this corridor. The clear path names
the C4 nonblank-tile release and glyph-scratch reset edges; the interactive
value-entry loop names instant-print toggles, active-window cursor setup,
decimal digit formatting, glyph printing with cleanup/sound/delay, text and
input ticks, sound effects, `MULT32`, and the shared divide helper chain.

## Text Display Setup Wrapper

`C1:134B` is tiny:

- call `C1:0A04`
- call `C1:AA18`
- return

`C1:0A04` enters a text display mode by calling `C3:E6F8`, setting `$89C9 = 1`, setting `$9623 = 1`, and writing `FFFF` to `$9647`. `C1:AA18` is already tied to the window/status-money side by the `0x18 0A` note. The safest current name for `C1:134B` is therefore a text-display setup wrapper for the wallet/status display path.

## Entry Record Wrappers

The core builder at `C1:13D1` allocates or reuses an `$89D4` entry, links it into the current `$8650` context, copies a terminator-ended source string, and returns the entry base.

`C1:14B1` is a richer wrapper around that allocator.

It stages two caller pointer pairs into the source/metadata slots consumed by `C1:13D1`, calls the builder, clears byte `record + 2C`, then writes caller metadata into `record + 08` and `record + 0A`. If `$5E71` is nonzero, it also splits the incoming `A` value: low three bits go to `record + 2C`, and the high bits become the value stored in `record + 08`.

So `C1:14B1` is best read as "create text-entry record with display metadata".

`C1:153B` is the next wrapper layer. It calls `C1:14B1`, stores the incoming `A` argument into `record + 0C`, and changes `record + 00` to `2`. This makes it a typed text/name record constructor.

`C1:1596` wraps `C1:153B` and then writes one caller-supplied byte into `record + 0E`. It is the same typed constructor with one extra byte of trailing metadata.

`C1:15F4` is a slimmer sibling that calls `C1:13D1` directly, stores the incoming selector/value into `record + 0C`, and marks `record + 00 = 2`.

The exact user-facing distinctions among these record types are still softer than the byte mechanics, but the local structure is clear: they are not independent print algorithms; they are constructors over the same `$89D4` entry format.

Source polish: `src/c1/c1_15f4_create_typed_text_entry_record_direct.asm`
now names the helper edges used by the direct constructor and the adjacent
active-chain renderer. The source names the `C1:13D1` installer, `PRINT_STRING`
and `PRINT_LETTER` paths, active-window tile-attribute setup at `C1:0FEA`,
the `C2:032B` window-title upload helper, `C0:8F22` text-length scan, and the
C4 record-marker/glyph-state/glyph-print helpers.

Source polish: `src/c1/c1_134b_setup_text_display_with_wallet_status.asm`
now names the adjacent text-display setup joins too: `SHOW_HPPP_WINDOWS`,
the wallet/status display refresh helper at `C1:AA18`, and the C3 registered
copy-chain cleanup helper called with the active focus id. A later source pass
also labels the hidden `C1:1354` free `$89D4` entry scanner and names the
constructor chain edges from `C1:13D1 -> 1354`, `C1:14B1 -> 13D1`,
`C1:153B -> 14B1`, and `C1:1596 -> 153B`.

## String Length Helper

`C1:17E2` counts nonzero bytes from a caller pointer.

It takes the pointer in `A/X` form, uses the incoming `Y` as a maximum count, increments through bytes until it hits `00` or the count expires, and returns the number of nonzero bytes seen.

This is a small bounded string-length helper used by nearby horizontal/string display paths.

## Active Entry Chain Selection

`C1:181B` and `C1:1887` both refresh display state after selecting an entry from the active context's `$89D4` chain.

Both routines:

- call `C4:51FA` / `LayoutActiveTextEntryChainForWindow` as an upstream text-entry layout helper
- resolve the current focus through `$8958 -> $88E4 -> $8650`
- write the requested ordinal/index into live context field `+2F`
- start from the current context's `+2B` entry index
- walk the `$89D4` chain through each record's `+02` link
- copy the selected record's `+06` word into live context field `+33`
- call the larger refresh/display routine at `C1:163C`

`C1:181B` takes the requested index from `Y` and treats `FFFF` as "skip selection update"; `C1:1887` takes the requested index from `A` and uses the same `FFFF` sentinel.

The larger `C1:163C` routine is still broad, but its helper edges are now
clearer: it enters instant-print mode, prints record selection markers through
`C4:3DDB`, stages animated glyph state through `C4:3CAA`, prints through
`C1:0EFC`/`C1:0CB6`, and uses the window-title upload and text-length helpers
while rendering special active-entry bodies.

`C1:0C49` is part of the same contract. It returns `0` for a `FFFF` head record and otherwise follows the `$89D4` `record + 02` next links until `FFFF`, returning the number of linked records. `C4:51FA` uses that count while assigning active-window row/page metadata to the chain.

Source polish: `src/c1/c1_181b_select_active_text_entry_by_y.asm` and
`src/c1/c1_1887_select_active_text_entry_by_a.asm` now name their helper-call
surface. The compact selector names the C4 active-entry layout pass and the
`C1:163C` active-chain renderer. The larger `C1:196A` menu loop names the C2
selectable-cell search helper, C4 cursor/glyph/string-run helpers, instant-print
and window tick helpers, active-window focus/content helpers, sound effects,
the delayed-action target dispatcher, and the EF battle-sprite-row cleanup edge
used before rerendering active selections.

## Practical Conclusion

The unknown starts `C1:0F40`, `C1:134B`, `C1:138D`, `C1:13D1`, `C1:14B1`, `C1:153B`, `C1:1596`, `C1:15F4`, `C1:181B`, and `C1:1887` are now covered as current-window clearing, display setup, text-entry record construction, and active record-chain selection helpers.

The main remaining work in this neighborhood is giving the `$89D4` record fields
and `C1:196A`'s internal selection-menu state bytes better final names, then
continuing deeper into the adjacent `C1:242E` selection-prompt dispatch/core
now that `C1:2012..242E` has named scan, refresh, two-list, and side-prompt
helper edges.
