# Class2 CC19 1F Cross-Segment Reuse

This note captures the broader local reuse of text control code `0x19 0x1F` after the original UFO/present path was pinned.

See also [class2-cc19-1f-display-text-bridge.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-1f-display-text-bridge.md).
See also [class2-c1acf8-substitution-byte-family.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-c1acf8-substitution-byte-family.md).
See also [class2-ufo-present-message-family.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-ufo-present-message-family.md).

## Main result

`0x19 0x1F` is not a UFO-only present helper.

The stronger current local interpretation is:

- `0x19 0x1F` is the generic text-engine loader for the one-byte substitution slot at `$9D11`
- scripts commonly follow it with `0x1B 0x04` (`SWAP_WORKING_AND_ARG_MEMORY`)
- the resulting argument then feeds a printer like `PRINT_ITEM_NAME 0` or `PRINT_PSI_NAME 0`

So the semantic center of this command is the source slot, not any one specific printer.

## Scanner result

Using [find_ebtext_sequence.py](/F:/Earthbound%20Decomp%20-%20Codex/tools/find_ebtext_sequence.py), the local ROM currently shows 57 `19 1F` hits inside `US/text_data` segments.

The heaviest buckets are:

- `EGOODS0`: 21
- `EGOODS1`: 8
- `EGOODS4`: 6
- `EBATTLE3`: 5
- `EBATTLE8`: 5
- `EBATTLE0`: 3
- `EBATTLE5`: 2

That distribution already argues against a narrow "present message only" interpretation.

## Representative local uses

### UFO present family: item printing

In `EBATTLE8`, the already-pinned present scripts use:

- `0x19 0x1F`
- `0x1B 0x04`
- `0x1C 0x05 0x00` -> `PRINT_ITEM_NAME 0`

That is the clean local bridge from `$AA10 -> C1:DD7C -> $9D11` into the visible present item name.

### Food and drink battle text: item printing

`EGOODS0` reuses the same pattern heavily. At `C9:7B6B` and nearby branches, the local script flow shows:

- `0x19 0x1F`
- `0x1B 0x04`
- item checks like `IS_ITEM_DRINK 0` or `IS_ITEM_CONDIMENT 0`
- later `PRINT_ITEM_NAME 0`

So the same command is clearly part of ordinary item-use battle text, not just UFO presents.

### PSI battle text: PSI-name printing

The battle-text banks show an equally important second use.

At representative spots like:

- `EF:8558` in `EBATTLE0`
- `EF:8E2B` in `EBATTLE3`
- `EF:70E4` in `EBATTLE5`

the local scripts use:

- `0x19 0x1F`
- `0x1B 0x04`
- `0x1C 0x12 0x00` -> `PRINT_PSI_NAME 0`

That means the loaded byte is not item-specific. The same slot can drive PSI-name formatting too.

## What this says about `$9D11`

This broad reuse sharpens the earlier `C1:ACF8` note.

The safest current interpretation is:

- `$9D11` is a generic one-byte battle-text substitution slot
- the display-text command `0x19 0x1F` loads that byte into the text pipeline
- later script commands decide how to interpret it, such as item id versus PSI id

So the item-specific meaning belongs to the caller and the printer, not to the slot itself.

## Current safest interpretation

The safest interpretation is:

- `C1:ACF8` / `C1:DD7C` set the current one-byte substitution value at `$9D11`
- `C1:7AF3` reads it back through the `0x19 0x1F` display-text command
- scripts commonly pair that loader with `SWAP_WORKING_AND_ARG_MEMORY`
- the loaded byte is then consumed by a domain-specific printer such as `PRINT_ITEM_NAME` or `PRINT_PSI_NAME`

## Best next target

The best next move is to give `0x19 0x20` the same treatment, since it is the obvious byte-source sibling and now stands out much more clearly as part of the same text-loader family.

## Update: `0x19 0x20` is much narrower

A quick follow-up scan of `0x19 0x20` found only one `US/text_data` hit, at `C9:1A91` in `ESHOP2`, inside the mushroom-girl clinic script family.

So at the moment the sibling does not look like another broad battle-text feeder. It looks like a separate specialized helper, which actually makes the broad reuse of `0x19 0x1F` stand out even more clearly.

See also [class2-cc19-20-eshop2-single-use.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-20-eshop2-single-use.md).
