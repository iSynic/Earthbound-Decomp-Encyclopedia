# Early Naming Buffers `$9819` / `$981F` / `$9825` / `$9829`

This note captures the current best local model for the early fixed-width selector buffers behind `0x19 28` selectors `3..5`.

See also [statistic-selector-family-c4550f-c3ee7a.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/statistic-selector-family-c4550f-c3ee7a.md) and [naming-buffer-commit-family-c1ead6-c4d065.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/naming-buffer-commit-family-c1ead6-c4d065.md).

## Main result

The early selector buffers after `$9801` are now more grounded locally than just "community names attached to table records."

Safest current local split:

- `$9819` = committed 6-byte naming-screen buffer
- `$981F` = committed 6-byte naming-screen buffer
- `$9825..9828` = fixed `"PSI "` prefix buffer
- `$9829..` = committed naming-screen suffix buffer paired with that prefix

That means selector `5` is no longer best read as just a plain `"PSI "` literal buffer. It is better read as a composite PSI-name field rooted at `$9825`, with a fixed prefix at `$9825..9828` and a separately committed suffix beginning at `$9829`.

## Selector-table side

The selector table at `C4:550F` still gives the base records:

- selector `3` -> `06 19 98`
- selector `4` -> `06 1F 98`
- selector `5` -> `0C 25 98`

So the safest current record-level read is still:

- selector `3` = 6-byte field rooted at `$9819`
- selector `4` = 6-byte field rooted at `$981F`
- selector `5` = 12-byte field rooted at `$9825`

What has improved is the local write-side interpretation of those fields.

## Local writer proof for `$9819` and `$981F`

The strongest current local writers sit in the naming-side family around `C1:F9A5..FA31`.

There:

- field id `4` writes through `C1:EC04` with destination `X = $9819` and width `6`
- field id `5` writes through `C1:EC04` with destination `X = $981F` and width `6`

Those are clean committed-buffer writes, not just reads.

That gives a much healthier local model:

- selectors `3` and `4` are real committed naming-screen buffers
- the community labels `pet name` and `favorite food` are now reference-backed and locally consistent rather than floating guesses

## Local writer proof for selector `5`

Selector `5` is a little more interesting.

The strongest current local pattern is:

- `C1:FE39..FE48` writes four bytes directly to `$9825..9828`
- those bytes decode through the local text table as `P`, `S`, `I`, and space
- naming-side code at `C1:FA7D` does not write to `$9825`; it writes the variable text through `C1:EC04` with destination `X = $9829`
- nearby menu-side readers also walk from `$9829`

So the safest current local read is:

- `$9825..9828` = fixed `"PSI "` prefix
- `$9829..` = variable suffix field committed by the naming-side path
- selector `5` record still points to `$9825` because the whole displayed field is the composite prefix-plus-suffix string

## Why this matters

This is a cleaner and more honest improvement over the old wording:

- selector `3` is no longer just a community pet-name guess; it is a real 6-byte committed naming buffer with a reasonable pet-name fit
- selector `4` is no longer just a community favorite-food guess; it is a real 6-byte committed naming buffer with a reasonable favorite-food fit
- selector `5` should not be described too narrowly as just `"PSI "`; the locally stronger read is a composite PSI-name field or favorite-thing display field rooted at `$9825`

## Confidence boundaries

### Locally proved

- selector-table records `3`, `4`, and `5` point to `$9819`, `$981F`, and `$9825`
- naming-side code writes committed 6-byte buffers to `$9819` and `$981F`
- `C1:FE39..FE48` seeds `$9825..9828` with `"PSI "`
- naming-side code writes the variable continuation for that field starting at `$9829`

### Reference-backed and locally consistent

- selector `3` = pet-name field
- selector `4` = favorite-food field
- selector `5` = favorite-thing / PSI-name field

## Best current interpretation

The safest current interpretation is that selectors `3..5` are all naming-screen-era committed fields, but selector `5` is structurally different from selectors `3` and `4`. Instead of being just one plain variable buffer, it is a composite field rooted at `$9825` whose visible text is built from a fixed `"PSI "` prefix plus a separately committed suffix beginning at `$9829`.
