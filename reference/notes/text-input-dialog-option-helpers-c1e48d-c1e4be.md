# Text Input Dialog Option Helpers `C1:E48D` and `C1:E4BE`

This note covers the unknown includes immediately before `text/text_input_dialog.asm`.

See also [early-naming-buffers-9819-9829.md](notes/early-naming-buffers-9819-9829.md).

## Main Result

`C1:E48D` and `C1:E4BE` are helper wrappers for the name/text input dialog family.

`C1:E4BE..EAD6` is now promoted into byte-equivalent source at `src/c1/c1_e4be_build_text_input_option_strip.asm`. The promoted interval covers the option-strip builder, the main text-input dialog body at `C1:E57F`, and the first prelude of the name-entry special-event wrapper at `C1:EAA6`.

The bank include order is the clearest placement evidence:

- `battle/enemy_select_mode.asm`
- `unknown/C1/C1E48D.asm`
- `unknown/C1/C1E4BE.asm`
- `text/text_input_dialog.asm`
- `text/enter_your_name_please.asm`
- `intro/name_a_character.asm`

The local code also matches that context: both helpers work through active text/window focus, the common text-entry positioning functions, and a character table at `D5:F4CF`.

## Working Names

- `C1:E48D` = `RenderSingleTextInputOptionRowScoped`
- `C1:E4BE` = `BuildTextInputOptionStrip`
- `C1:E57F` = `RunTextInputDialog`
- `C1:EAA6` = `RunNameEntrySpecialEventPrelude`
- `C4:406A` = `ReadNameEntryGridCharacter`
- `C4:40B5` = `BuildTextInputStringGlyphMetrics`
- `C4:41B7` = `InitializeTextInputOptionGlyphMetrics`
- `C4:424A` = `SetTextInputOptionMetricSlot`
- `C4:42AC` = `RenderTextInputOptionStrip`

## `C1:E48D`: Single Text-Input Row Wrapper

`C1:E48D` takes three inputs:

- `A` = window/focus id
- `X` and `Y` = parameters passed through to the row renderer

It:

- opens an update scope with `C3:E4D4`
- focuses the requested window through `C1:007E(A)`
- calls `C4:42AC` with the original `A/X/Y`
- saves the result
- restores focus to window `0x1C`
- returns the `C4:42AC` result

This is best treated as a small scoped wrapper around the text-input row renderer.

## `C1:E4BE`: Text-Input Option Strip Builder

`C1:E4BE` is the wider helper. It takes:

- `A` = window/focus id
- `X` = input-dialog mode or alphabet/page selector
- `Y` = current cursor/option index

It:

- opens an update scope through `C3:E4D4`
- activates the requested text/window context with `C1:04EE(A)`
- resolves the active window record from `$8958`, `$88E4`, and a `0x52`-byte stride
- chooses renderer width `5` or `6` depending on whether `X <= 4`
- initializes the renderer through `C4:41B7`
- positions at the active window's word at offset `+0x10` through `C4:38A5`
- advances the starting option index, wrapping `6 -> 0`
- indexes `D5:F4CF` using a composite of page/mode, option index, and loop index
- calls `C4:42AC` for each nonzero byte in that table
- restores focus to window `0x1C`
- returns the next starting option index

So the safest current label is "text-input option strip builder." It is not the whole text input dialog; the larger dialog body starts at `C1:E57F`.

## C4 Renderer Layer

The C4 helpers behind those C1 wrappers now line up as a small name-entry/text-input rendering layer:

Source scaffold status: `src/c4/active_window_glyph_print_and_cursor_read_helpers.asm`
now preserves the name-entry grid reader at `C4:406A..C4:40B5`.
`src/c4/text_input_option_metric_and_strip_render_helpers.asm` then preserves
the option metric/render cluster at `C4:40B5..C4:44FB`, so this document's
C4 renderer layer is source-backed through the option-strip upload path.

- `C4:406A` indexes the name-entry grid. It selects a pointer from the long table at `EF:A6D3`, uses the caller's row/column-style inputs plus the `C2:0912` offset table, and returns one zero-extended byte from the selected grid/table.
- `C4:40B5` compiles a caller string into three parallel display/metric buffers: original bytes in `$1B86`, normalized character indices in `$1B56`, and width-plus-spacing bytes in `$1B6E`. It clears the metric span first, walks until terminator or caller limit, calls `C4:4E61` for each produced glyph, and pads the remainder with the spacing/sentinel entries used by this renderer.
- `C4:41B7` initializes the option-strip metrics. It clears the large `$3492` tile-state scratch span, resets `$9662`, clears `$1B86`, seeds `$1B56[0] = #$20`, and fills the remaining slots up to the caller count with the small default option marker `#$03` plus widths from `C3:F054`.
- `C4:424A` updates one option slot at index `$9662`: it stores or clears the original byte in `$1B86`, writes the normalized character index to `$1B56`, and writes width-plus-spacing to `$1B6E`. The special byte `#$70` clears the source-byte slot.
- `C4:42AC` is the full renderer/update routine. It resets the animated glyph-state scratch at `$3492`, updates the selected option slot through `C4:424A`, rebuilds the corresponding tile-state rows through C3 width/glyph tables and `C4:4B3A`, and uploads 16-byte strips to VRAM through `C0:8616`. It returns early through `C4:44F9` when the cursor cannot advance.

This confirms that the C1 routines are wrappers and policy. The actual option-strip state lives in the C4 metric buffers and the `$3492` scratch rows.

## Source Polish Follow-Up

2026-05-06 source polish names the remaining helper-call surface in
`src/c1/c1_e4be_build_text_input_option_strip.asm`. The main dialog body now
calls through local contracts for the C3 window update-scope exit and light
tick helpers, C1 tile-attribute/glyph-print/text-system ticks, C1/C2 movement
candidate search helpers, C0 sound effects, C1:E48D single-row render wrapper,
and C0 text-length measurement edge. The source unit has no remaining raw
helper-call edges while preserving C1 byte equivalence.

2026-05-06 follow-up: the adjacent naming-buffer commit source now calls
`C1E57F_RunTextInputDialog` through the promoted contract name, keeping the
`EAD6..EC8F` naming flow aligned with the dialog body named here.

## Remaining Soft Edge

The exact layout of `D5:F4CF` still needs a table dump before assigning final names to each page/mode. The routine shape is already clear enough for decompilation work:

- `E48D` = scoped single-row render wrapper
- `E4BE` = table-driven option strip/page renderer used by the text-input dialog
- `EAA6` begins the special-event name-entry wrapper used by text command `[1F 41]` cases `03/04`; its full body continues into the neighboring `EAD6..EC8F` source interval.
