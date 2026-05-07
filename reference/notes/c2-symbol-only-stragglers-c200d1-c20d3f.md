# C2 symbol-only stragglers

This note closes the two bank-`C2` addresses that appear only through the reference symbol table rather than as separate address-bearing include files:

- `C2:00D1`
- `C2:0D3F`

Both are useful to document because the progress audit unions include-map addresses with symbol-table addresses.

## `C2:00D1` - window reset coordinate/config data

Suggested working name: `WindowResetInitialCoordinateData`

Direct callers:

- none found

The reference symbol table exposes `UNKNOWN_C200D1`, but the bank include map begins the callable reset routine at `unknown/C2/C200D9.asm`. Decoding from `C2:00B9` shows data-like words through `C2:00D8`; decoding from `C2:00D9` shows a normal routine prologue (`REP`, `PHD`, direct-page setup) and direct callers from C0, C1, C4, and EF.

Observed local data around `C2:00D1`:

- `C2:00D0..00D1`: word `0x1E00` if read from the even boundary
- `C2:00D2..00D3`: word `0x3300`
- `C2:00D4..00D5`: word `0x1E00`
- `C2:00D6..00D7`: word `0x3300`
- `C2:00D8`: trailing zero byte immediately before the `C2:00D9` routine prologue

Given the surrounding reset routine clears `$89C9`, `$89CA..$89D2`, `$9622..$9624`, `$9641`, the open-window chain at `$88E0/$88E2`, and several window/status tables, this symbol is best treated as a small coordinate/config data tail owned by the global window/text reset block rather than a callable routine.

Source polish:

- 2026-05-06: `src/c2/c2_00d1_window_reset_initial_coordinate_data.asm`
  now names the main structural reset contracts: the `$88E0/$88E2` open-window
  chain, `$88E4` window-record index table, `$8650` window-record base and
  `0x52` stride, `$894E` title-upload slot table, `$89D4` text-entry record
  base and `0x2D` stride, `$8958` current focus id, HP/PP tilemap clear range,
  text display/sound latches, and the C4 `$1AD6` mask-table reload helper
  `C4:3F53`.

## `C2:0D3F` - split a value into three decimal digits

Suggested working name: `SplitValueIntoThreeDecimalDigitsAt8966`

Direct callers:

- `C2:0F17`
- `C2:0F49`

The reference include map places this region among the named HP/PP window helpers:

- `text/hp_pp_window/separate_decimal_digits.asm`
- `text/hp_pp_window/fill_tile_buffer_x.asm`
- `text/hp_pp_window/fill_tile_buffer.asm`
- `text/hp_pp_window/fill_character_hp_tile_buffer.asm`
- `text/hp_pp_window/fill_character_pp_tile_buffer.asm`

Observed behavior:

- input `A` is saved as the working value
- initializes `X = $8968`
- uses C0 division/remainder helpers with divisor `10`
- stores one digit byte at `$8968`
- divides the working value by `10`
- stores the next digit byte at `$8967`
- divides once more by `10`
- stores the final digit byte at `$8966`
- returns with the three decimal digits staged in descending memory order `$8966..$8968`

The callers at `C2:0F17` and `C2:0F49` are wrappers immediately before `C2:0F58`, the HP/PP roller prelude already documented in the window/HPPP note. One path directly fills a tile buffer after splitting the input value; the other branches between reusing an existing tile-buffer descriptor (`C2:0D89`) and splitting/filling a fresh value through `C2:0D3F` plus `C2:0DC5`.

Source polish:

- 2026-05-01: `src/c2/c2_0d3f_split_value_into_three_decimal_digits_at8966.asm`
  now names the digit staging bytes `$8966..$8968`, divisor `10`, HP/PP tile
  buffer roots `$896D/$8975`, tile source offset bases, blank/visible digit
  offsets, second-row tile delta, and the callable `C2:0F08/0F26` HP/PP
  wrapper entries.

## Working Names

- `C2:00D1` = `WindowResetInitialCoordinateData`
- `C2:0D3F` = `SplitValueIntoThreeDecimalDigitsAt8966`
- `C2:0D89` = `FillHpPpTileBufferX`
- `C2:0DC5` = `FillHpPpTileBuffer`
- `C2:0F08` = `FillCharacterHpTileBuffer`
- `C2:0F26` = `FillCharacterPpTileBuffer`
