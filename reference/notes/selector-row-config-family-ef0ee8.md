# Selector-Row Config Family (`EF:0EE8` / `D5:F645` / `C21628`)

This note records the corrected current read for the far setup family that feeds `0A38 -> 0E5E -> 2C22`.

See also [selector-row-zero-caveat.md](notes/selector-row-zero-caveat.md).
See also [visual-selector-family-c0780f-c3f2b5.md](notes/visual-selector-family-c0780f-c3f2b5.md).
See also [delivery-row-helpers-ef0e67-ef0ead.md](notes/delivery-row-helpers-ef0e67-ef0ead.md).

## Correction

An earlier version of this note misread `EF:0EE8` and treated `D5:F645` record word `0` as the event-flag gate.

That was wrong.

The current local disassembly now makes the split clear:

- record word `0` = sprite/object descriptor id used by visual setup
- record word `1` = event-flag id passed to `C21628`
- the selected row id is still the matching **record index** stored to `0A38`

## Main result

`EF:0EE8` is a 10-entry table walker over `D5:F645`.

For each 20-byte record, it:

1. computes the row base
2. loads record word `1` at offset `+0x02`
3. tests that value with `C21628`
4. if the flag is set, stores the row index to `0A38`
5. reloads record word `0` at offset `+0x00`
6. passes that descriptor id into `C01E49`

If record word `0` is zero, it falls back to a placeholder choice via `C08E9A`, masks it with `#0003`, indexes `C3:FDBD`, and uses that result instead.

So the strongest current local read is:

- `D5:F645` = small event-gated delivery/service configuration table
- record word `0` = sprite/object descriptor id
- record word `1` = event-flag gate
- `0A38` = selected row id copied from the matching row index

## Why `C21628` is now clearer

`C21628` is a direct event-flag membership test over the bitfield rooted at `7E:9C08`:

- decrement the incoming id
- divide by `8`
- use the quotient as the byte index into `$9C08+X`
- use `DATA_C4562F = 01 02 04 08 10 20 40 80` as the bit mask
- return `1` if the bit is set, otherwise `0`

So `EF:0EE8` is not translating metadata through a lookup. It is testing a real event-flag field inside the table.

## Corrected record shape at `D5:F645`

The live ROM shows 10 records of 20 bytes each:

- word `0` = sprite/object descriptor id
- word `1` = event flag
- word `2` = retry-threshold / max-attempt field, usually `0006`, except `FFFF` for the HoiHoi row
- word `3` = retry-wait field in one-second units, usually `000F`, except `FFFF` for the HoiHoi row
- word `4` = delivery_time countdown field
- bytes `10..15` = two packed 24-bit script pointers
- word 8 = enter_speed-like scalar
- word 9 = exit_speed-like scalar

Sample entries:

- `0`: `0097 00B4 0006 000F 00B4 4BBF F8C6 C64C 0200 0200`
- `1`: `0087 00B5 0006 000F 000A 42A3 15C6 C645 0180 0180`
- `2`: `0087 0285 0006 000F 000A 3EB0 1AC6 C645 0180 0180`
- `3`: `0037 01BE 0006 000F 0001 D844 F1C5 C5DD 0280 0280`
- `4`: `006C 0286 0006 000F 0002 D858 F1C5 C5DD 0280 0280`
- `5`: `0070 0287 0006 000F 0003 D86C F1C5 C5DD 0280 0280`
- `6`: `0055 0288 0006 000F 0004 D880 F1C5 C5DD 0280 0280`
- `7`: `0097 02A3 00FF 00FF 0005 A542 D9C7 C7A7 0180 0180`
- `8`: `0087 02B6 0006 000F 000A 943A ACC6 C695 0180 0180`
- `9`: `0087 02B7 0006 000F 000A 94F4 B3C6 C695 0180 0180`

## Strong match to the reference `timed_delivery` struct

The `ebsrc` reference tree defines a 20-byte `timed_delivery` struct:

- `sprite`
- `event_flag`
- `unknown4`
- `unknown6`
- `delivery_time`
- `text_pointer_1`
- `text_pointer_2`
- `enter_speed`
- `exit_speed`

Our local bytes now line up strongly with that shape:

- word `0` = `sprite`
- word `1` = `event_flag`
- words `5..7` = `text_pointer_1` / `text_pointer_2`
- words `8..9` = very likely `enter_speed` / `exit_speed`

The table is now largely mapped: words `2..3` look like retry threshold and retry wait, word `4` is the delivery countdown field, and the trailing pair still look like enter/exit speeds.

## Delivery-row helper family in bank `EF`

The surrounding helpers make the table much less abstract:

- `EF:0E67` reads the current row from `0E5E[current_entity]` and returns record word `8`
- `EF:0E8A` reads the current row from `0E5E[current_entity]` and returns record word `9`
- `EF:0EAD` takes a 1-based row selector in `A`, stores `A-1` to `0A38`, loads record word `0`, and instantiates that sprite or a placeholder through `C01E49`
- `EF:0EE8` scans all 10 rows by record word `1` and instantiates the first enabled row through `C01E49`

See the focused helper note: [delivery-row-helpers-ef0e67-ef0ead.md](notes/delivery-row-helpers-ef0e67-ef0ead.md).

## Service-family interpretation

The row contents now read much more concretely than a generic selector table.

The strongest current entry mapping is:

- row `0`: `MACH_PIZZA_GUY` + `FLG_DELIVERY_PIZZA`
- row `1`: `ESCARGO_EXPRESS_GUY` + `FLG_DELIVERY_UNSOU`
- row `2`: `ESCARGO_EXPRESS_GUY` + `FLG_DELIVERY_UNSOU_B`
- rows `3..6`: customer-side delivery rows
- row `7`: `MACH_PIZZA_GUY` + `FLG_DELIVERY_HOIHOI`
- rows `8..9`: special Escargo rows for `TAKOKESHI` / `TAKANOME`

The script-pointer pairs reinforce that:

- `C6:4BBF` / `C6:4CF8` = Mach Pizza arrival / follow-up family
- `C6:42A3` / `C6:4515` = ordinary Escargo arrival / follow-up family
- `C6:3EB0` / `C6:C61A` = alternate Escargo family
- `C5:D844` / `C5:DDF1` and siblings = customer-side family

So the cleanest current thematic read is:

- `D5:F645` = small delivery-service / delivery-customer configuration table

## Relationship to the selector-row family

This still feeds the same higher-level selector-row path:

- `0A38 -> 0E5E -> 2C22`

But the important semantic correction is:

- the matching row index becomes the selector row id
- the tested flag lives in record word `1`
- the descriptor handed to `C01E49` lives in record word `0`

So selector row `0` still means only "row 0 of this table matched," not a uniquely named actor class.

## Current-object cache split still matters

The broader `0A38..0A4A` block should still be kept separate from the delivery table itself.

`EF:0EE8` only provides:

- the selected row index to `0A38`
- the descriptor id to `C01E49`

Then the generic setup chain fills the rest of the visual cache and later copies it into per-entity state such as `0E5E`, `0E9A`, `0ED6`, and friends.

So the safest current split remains:

- `D5:F645` = delivery/service selection source plus service-script payloads
- `0A38..0A4A` = generic current-object setup cache

## Shared post-transition hook

The only pinned direct table walker is still `EF:0EE8`, reached through `C06B21`.

`C06B21` remains best read as a shared post-transition or post-setup hook:

- it first runs a fixed Andonuts-scene script hook
- then it runs the broader `D5:F645` delivery/service scan at `EF:0EE8`

That keeps the selector-row and service-table interpretations adjacent, but not identical.

## Debug-table correction still stands

The compact pointer table at `C5:8CF4` is still useful only as a script-reuse bridge.

It lives inside `EDEBUG::_DBG_SCRIPT`, so it proves that some Mach Pizza / Escargo scripts are reused in the debug menu, but it is **not** the normal runtime selector for the delivery table.



