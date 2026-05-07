# Active Text Entry Chain Layout (`C4:51FA`)

This note names and documents the bank-`C4` helper immediately before the row-position text data at `C4:54F0`.

See also [text-entry-record-builder-neighbors-c10f40-c11887.md](notes/text-entry-record-builder-neighbors-c10f40-c11887.md).
See also [text-entry-builder-c113d1-89d4.md](notes/text-entry-builder-c113d1-89d4.md).
See also [class2-row-position-text-cluster-c454f0.md](notes/class2-row-position-text-cluster-c454f0.md).

## Working Names

- `C4:51FA` = `LayoutActiveTextEntryChainForWindow`
- `C1:0C49` = `CountTextEntryChainRecords`
- `C1:138D` = `CountTextEntryChainRecordsLocal`
- `C1:180D` = `LayoutActiveTextEntriesAndRefresh`

## Main result

`C4:51FA` lays out the active window's linked `$89D4` text-entry chain.

It does not allocate records and it does not render glyphs directly. Instead, it resolves the live `$8650` window/context descriptor, finds the descriptor's head text-entry index at `+2B`, walks the `$89D4` linked list, measures entry text when variable spacing is requested, and writes layout metadata back into each record.

The safest current name is `LayoutActiveTextEntryChainForWindow`.

## Callers

The direct local callers are:

- `C1:180D`
- `C1:181B`
- `C1:36DA`

`C1:180D` passes through the caller's count/selector, supplies the spacing mode, calls `C4:51FA`, then immediately refreshes display state through `C1:163C`. This is the wrapper used by the broad `0x1C 07` text command path, so the practical name there is `LayoutActiveTextEntriesAndRefresh`.

`C1:181B` and `C1:1887` use the same layout helper before selecting a requested record from the active chain and copying that record's row/page field back into the live context.

`C1:36DA` reaches it during a menu setup path with `A=1`, `X=0`, and `Y=0`, which matches a single-column/default-layout setup before the same selection/display refresh family takes over.

## Local contract

Inputs are staged into direct page:

- `A` -> `$28`
- `X` -> `$2A`
- `Y` -> `$2C`

The routine resolves the active window descriptor by reading `$8958`, indexing `$88E4`, mapping through `C0:8FF7` with selector `#$0052`, and adding the `$8650` context base.

If descriptor field `+2B` is `FFFF`, there is no active text-entry chain and the routine exits. Otherwise it:

- writes the incoming `A` value to descriptor field `+31`
- maps the head record index through `C0:8FF7` with selector `#$002D`
- treats `$89D4 + mapped_offset` as the first text-entry record
- clears a four-byte scratch width table at `$968D`
- fills a four-byte scratch spacing table at `$9691` with `FF`

## Variable spacing path

When `$2C` is nonzero, the routine walks the linked `$89D4` chain and measures each record's text pointer at `record + 13`.

Each record is measured through `C4:3E31` with length `#$001E`. The returned width is padded by 8 and stored in `$968D[index]`; the total padded width is accumulated separately.

After the pass, the routine computes a scale factor from descriptor field `+0A` and the accumulated width using the shared multiply/divide helpers at `C0:9032` and `C0:915B`. It then derives one spacing byte per measured entry and stores the results in `$9691`.

This makes `$968D/$9691` local scratch for proportional entry widths or spacing, not durable game state.

## Uniform spacing path

When `$2C` is zero, the routine skips string measurement and computes one uniform spacing value:

`((A - 1) * X + descriptor[+0A]) / A`

That value is later used as the per-entry horizontal step while the linked records are updated.

The `0x1C 07` path reaches `C1:180D` with `X=1` and `Y=0`, so it uses this uniform-layout branch with the wrapper controlling the rounding term.

## Record fields touched

The layout pass writes into each `$89D4` text-entry record while following `record + 02` as the next-link field.

The important writes are:

- `record + 08`: horizontal offset or spacing-derived position
- `record + 0A`: vertical/row offset inside the active descriptor
- `record + 06`: row/page/group number copied later by `C1:181B` / `C1:1887`

The routine also uses descriptor field `+0C / 2` as the available row capacity and descriptor field `+0A` as the active horizontal span.

## Count helper

`C1:0C49` is just a far wrapper over `C1:138D`.

`C1:138D` returns `0` for an input record index of `FFFF`; otherwise it maps the starting index into `$89D4`, follows `record + 02` until `FFFF`, and returns the number of records seen.

So `C4:51FA` is explicitly using a text-entry chain count, not a string-byte count or table selector.

## Overflow tail

The tail recomputes the active chain count and compares it against descriptor field `+0C / 2`.

If the chain fits, it returns. If it overflows the available row capacity, it walks to a later record, stages pointer `C3:E44C`, clears the companion pointer slots, calls `C1:0BFE`, then resolves descriptor field `+2D` and clears the selected record's row/page field.

The exact user-visible effect of that tail is still a little soft, but the shape is clear: after laying out an oversized active entry chain, it forces a display/update helper and resets one current selection/row marker.

## Practical conclusion

`C4:51FA` closes the largest remaining unnamed routine in the `C4:4E61..51FA` text-formatting cluster.

The surrounding cluster now reads as:

- `C4:4E61` = token glyph-run staging for the active window
- `C4:4FF3` = bounded glyph byte-run width measurement
- `C4:507A` = right-aligned decimal printing in the active window
- `C4:51FA` = active text-entry chain layout for the current window

The remaining uncertainty is mostly field naming inside the `$89D4` record and `$8650` descriptor contracts, not the purpose of this routine.
