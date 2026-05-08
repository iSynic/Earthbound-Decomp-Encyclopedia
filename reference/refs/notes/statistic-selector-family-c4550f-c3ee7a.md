# Statistic Selector Family `C4:550F` / `C3:EE7A`

This note captures the current best local model for the small statistic-selector family shared by the `0x19 27` and `0x19 28` text commands.

See also [text-command-family-19-data-and-substitution.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-19-data-and-substitution.md), [short-text-staging-buffer-9c9f.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/short-text-staging-buffer-9c9f.md), [text-entry-builder-c113d1-89d4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-entry-builder-c113d1-89d4.md), and [early-naming-buffers-9819-9829.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/early-naming-buffers-9819-9829.md).

## Main result

The late `0x19` statistic tail is now more grounded locally than it first looked.

The strongest shared anchor is the compact 3-byte selector table at `C4:550F`, used by:

- `C3:EE7A`, the live worker behind `0x19 27`
- `C1:4819`, the live worker behind `0x19 28`
- `C1:9249`, the bank-`01` statistic-display side used by `C1:40C7`

So the safest current read is that `0x19 27` and `0x19 28` are not unrelated one-offs. They are two views into the same statistic-selector table:

- `0x19 27` = resolve the selected statistic to its current value domain
- `0x19 28` = read one character from the selected statistic or dynamic string form

## Shared selector table

The selector table at `C4:550F` is a fixed 3-byte record stream.

Representative records:

- record `0`: `00 00 00`
- record `1`: `0C F5 97`
- record `2`: `18 01 98`
- record `3`: `06 19 98`
- record `4`: `06 1F 98`
- record `5`: `0C 25 98`
- record `6`: `84 31 98`
- record `7`: `84 35 98`
- record `8`: `05 CE 99`
- record `9`: `81 D3 99`
- record `10`: `84 D4 99`
- record `11`: `82 13 9A`

The first byte is now best read as a compact type/shape byte, while the trailing word is the payload.

## Partial selector-index crosswalk

The late half of the table is now much more grounded locally, because its payloads line up directly with the character-record and displayed-stat families we already mapped elsewhere.

Safest current partial crosswalk:

- selector `11` -> `$9A13` = HP-present / HP-active marker
- selector `12` -> `$9A15` = max HP
- selector `13` -> `$99D8` = current HP
- selector `14` -> `$9A19` = PP-present / PP-active marker
- selector `15` -> `$9A1B` = max PP
- selector `16` -> `$99DA` = current PP
- selector `17` -> `$99E3` = displayed offense
- selector `18` -> `$99E4` = displayed defense
- selector `19` -> `$99E5` = displayed speed
- selector `20` -> `$99E6` = displayed guts
- selector `21` -> `$99E7` = displayed luck
- selector `22` -> `$99E8` = displayed vitality
- selector `23` -> `$99E9` = displayed IQ

Why this is healthy locally:

- selectors `17..23` point straight at the seven-byte displayed-stat block rooted at `$99E3`
- bank-`01` status display code at `C1:9660` reads those same seven bytes in the known menu-stat family
- selectors `12/13/15/16` point straight at the current and max HP/PP word fields already cross-checked through the recovery and growth notes
- selectors `11/14` point to the paired HP/PP-present markers already identified in the recovery quartet notes

The early and middle selector block is healthier now too:

- selector `8` -> `$99CE` = fixed-width 5-byte character-name field
- selector `9` -> `$99D3` = strongest current fit for level
- selector `10` -> `$99D4` = strongest current fit for current experience quantity

Selector `8` is now healthier locally too:

- its table record is `05 CE 99`, which makes it the same inline fixed-width form as the other early string-like selectors
- `C1:4819` treats that inline form as "max character count plus backing buffer base"
- `C1:EDB4` and `C2:3B91` both copy null-terminated bytes from `$99CE..$99D2` with an explicit 5-byte cap
- that makes `$99CE` the strongest current local fit for the current character's fixed-width name field

Why these two are now healthier locally:

- `C1:D8D0` seeds `$99D3` to `1` during the same character bootstrap that seeds HP/PP and the derived-stat refresh chain
- `C4:5F40` uses `$99D3` as an ordered byte threshold, which fits level unusually well
- `C4:59A0` treats `$99D3 == 99` as a terminal cap and otherwise uses it to index the `D5:8F49` experience-threshold table
- that same path subtracts the current quantity at `$99D4..` from the next-threshold value, which is the strongest current local fit for current experience


## Early fixed-width string selectors

The early non-high-bit selector records are now much healthier than just "inline/local payloads."

The strongest current local read is that the low 7 bits in those records are fixed-width string capacities, while the trailing word is the backing WRAM field or buffer base.

Current locally supported examples:

- selector `1`: `0C F5 97` -> fixed-width 12-byte buffer at `$97F5`
- selector `2`: `18 01 98` -> fixed-width 24-byte buffer at `$9801`
- selector `3`: `06 19 98` -> fixed-width 6-byte buffer at `$9819`
- selector `4`: `06 1F 98` -> fixed-width 6-byte buffer at `$981F`
- selector `5`: `0C 25 98` -> fixed-width 12-byte buffer at `$9825`
- selector `8`: `05 CE 99` -> fixed-width 5-byte character-name field at `$99CE`

Best current reference-backed baseline identities for that early block:

- selector `1` -> transliterated or kana-style player-name buffer
- selector `2` -> baseline player-name buffer; current prayer/system script hits are still locally compatible with ordinary player-name iteration, and no separate non-naming producer into `$9801` is pinned yet
- selector `3` -> baseline pet-name field
- selector `4` -> baseline favorite-food field
- selector `5` -> baseline favorite-thing or PSI-name field rooted at `$9825`

Why this is healthy locally:

- `C1:4819` compares the current character index against the record's first byte directly, which makes that byte act like a max character count
- if the index is in range, it reads the selected byte from the trailing-word base plus index
- every currently exposed `0x19 28` hit uses selector `2`, and all of them loop it character-by-character in prayer/system text neighborhoods
- raw immediate setup of `$9801` currently appears only in the naming path at `C1:EAD6` and `C1:EBA0`, which makes the prayer/system uses compatible with ordinary player-name reads rather than forcing a broader selector-`2` temp-buffer identity
- the selector `8` backing field at `$99CE` is also copied elsewhere as a 5-byte NUL-terminated string
- `C1:EAD6..EBE4` treats `$9801` and `$97F5` as paired display buffers in the same naming-side UI flow
- [text-entry-builder-c113d1-89d4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-entry-builder-c113d1-89d4.md) now tightens the adjacent `C1:13D1` helper family into a shared active text-entry allocator/installer rather than a selector-`2`-specific loader
- the nearby `C4:41B7 / C4:40B5` helpers then compile naming-side display rows through `1B56/1B6E/1B86`, which makes them downstream display builders over the buffers, not the buffer-materialization step itself
- [naming-buffer-commit-family-c1ead6-c4d065.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/naming-buffer-commit-family-c1ead6-c4d065.md) now pins the first clean write-side bridge:
  - `C1:EBA0..EBDD` commits the live naming-entry work buffer at `$9C9F`
  - `C4:D065` remaps that buffer into `$9801`
  - `C0:8ED2` copies `0x0C` bytes from the same work buffer into `$97F5`
- bank-`01` item/equipment-side writers at `C1:9963 / A103 / A86D` also reuse `$9C9F`; [short-text-staging-buffer-9c9f.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/short-text-staging-buffer-9c9f.md) now captures the safer boundary: `$9C9F` is a broader short-text staging buffer, while the naming note pins one specific naming-side commit use of it
- [early-naming-buffers-9819-9829.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/early-naming-buffers-9819-9829.md) now gives the stronger local split for selectors `3..5`: `$9819` and `$981F` are committed 6-byte naming-screen buffers, while selector `5` is a composite field rooted at `$9825`, with fixed `"PSI "` prefix bytes at `$9825..9828` and variable suffix writes beginning at `$9829`
- the community RAM map independently names `$97F5/$9801/$9819/$981F/$9825` as a player-name transliteration buffer, player name, pet name, favorite food, and `"PSI "` respectively
- but the exposed `0x19 28` prayer/system loops do not currently prove a distinct non-naming producer into `$9801`; at the moment they remain locally compatible with ordinary player-name iteration

So the safest current read is that the early selector block is not generic inline math or address payload. It is a small family of fixed-width dynamic text buffers or committed naming fields, with selector `8` doubling as the current-character-name entry and selectors `1..5` retaining softer caller-specific semantics. Selector `2` should currently stay closer to a committed player-name buffer than to a proven general-purpose temp string slot.

## Local worker proof: `C3:EE7A`

`C1:776A` is the live ordinary-script leaf for `0x19 27`, and it directly `JSL`s `C3:EE7A`.

`C3:EE7A` does the following:

1. indexes the `C4:550F` table with `selector * 3`
2. reads the first byte as a type/shape byte
3. branches on bit `7`
4. uses the trailing word as a payload source
5. returns one of several value forms

The strongest current local split is:

- high bit clear (`kind < 0x80`): fixed-width inline string-buffer form, where the low 7 bits act like character capacity
- `0x81`: indirect one-byte scalar
- `0x82`: indirect one-word scalar
- `0x84`: indirect pointer-form payload

That means the statistic family really is mixed-domain:

- some selectors resolve to fixed-width dynamic text buffers
- some selectors resolve to current numeric bytes
- some resolve to current numeric words
- some resolve to pointer-based string data

So the community wording for `0x19 27` now fits the ROM much better than before: "return the value of a statistic, but some statistics are not plain numbers."

## Local worker proof: `C1:4819`

`C1:4819` is the live ordinary-script leaf for `0x19 28`.

It uses the same `C4:550F` table, but instead of returning the raw value domain it:

1. resolves the selected 3-byte table record
2. reads the current index from `C1:0400`
3. checks the statistic's string length byte
4. either returns `0` if the requested character position is out of range
5. or returns the requested character from the statistic string

That makes the safest current read of `0x19 28` much stronger:

- it is not a generic string-letter helper
- it is specifically the statistic-string and dynamic-buffer sibling of the `0x19 27` selector family

## Bank-`01` display-side reuse: `C1:9249`

The same `C4:550F` table is reused by `C1:9249`, reached from `C1:40C7`.

That path branches on the same type/shape byte and then either:

- prints a byte scalar
- prints a word scalar
- prints a pointer-based statistic string
- or follows the inline payload form

So the local code now gives a clean structural reason why the community docs describe the statistic domain as mixed numeric and string data. The selector table itself is mixed-domain, and both the text-command tail and the display-side helper honor that split.

## Safest current type-byte interpretation

The safest current interpretation of the first byte in each `C4:550F` record is:

- bit `7` clear: fixed-width inline string-buffer form
- low 7 bits in that form: maximum character count
- `0x81`: indirect byte statistic
- `0x82`: indirect word statistic
- `0x84`: indirect pointer/string statistic

What still stays softer is the exact user-facing identity of each fixed-width backing buffer, especially `$97F5`, `$9819`, `$981F`, and `$9825`.

## What this says about `0x19 27`

The safest current upgrade for `0x19 27` is:

- it is a real live statistic-selector leaf, not just a runtime-only oddball
- it uses `C3:EE7A` plus `C4:550F`
- and it returns the selected statistic in its natural local domain, which may be:
  - byte scalar
  - word scalar
  - pointer/string form
  - or one of the fixed-width dynamic string-buffer forms

That is materially stronger than the earlier note wording that only said "community-doc-backed and locally consistent."

## What this says about `0x19 28`

The safest current upgrade for `0x19 28` is:

- it is the string-letter sibling of the same selector family
- its local behavior now directly supports the community docs' "one letter from a statistic" wording
- and its out-of-range behavior is also locally visible through the string-length check

## Confidence boundaries

### Locally proved

- `C1:776A` directly calls `C3:EE7A`
- `C3:EE7A` indexes `C4:550F` as a 3-byte selector table
- `C1:4819` also indexes `C4:550F`
- `C1:9249` also indexes `C4:550F`
- the first byte is a real type/shape discriminator, not just part of a flat pointer
- the family supports mixed fixed-width string, numeric, and pointer outputs
- selectors `17..23` line up locally with the displayed-stat block at `$99E3..$99E9`
- selectors `12/13/15/16` line up locally with the current/max HP/PP word family
- selectors `11/14` line up locally with the paired HP/PP-present markers
- selector `8` has a strong local current-character-name fit
- selector `9` has a strong local level fit
- selector `10` has a strong local current-experience fit

### Reference-backed and locally consistent

- `0x19 27` = return value of a statistic
- `0x19 28` = return one letter from a statistic
- selector `1` = baseline transliterated or kana-style player-name buffer
- selector `2` = baseline player-name buffer
- selector `3` = baseline pet-name field
- selector `4` = baseline favorite-food field
- selector `5` = baseline favorite-thing or PSI-name field

### Still open

- the exact semantic identity of each selector index in `C4:550F`
- whether any loaded-string path besides the current `0x19 02 -> $97D7/$97CA -> C1:13D1 -> 89D4` live-entry route feeds or refreshes the stable fixed-width buffers like `$9801` in concrete caller families
- the non-naming write-side bridges into `$9801`, if any, now that [naming-buffer-commit-family-c1ead6-c4d065.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/naming-buffer-commit-family-c1ead6-c4d065.md) and [short-text-staging-buffer-9c9f.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/short-text-staging-buffer-9c9f.md) make the currently pinned split much sharper
- whether the community names for `$97F5`, `$9801`, `$9819`, `$981F`, and the composite `$9825/$9829` field hold cleanly across every local caller
- whether the displayed-stat and menu-stat families use every selector in the same way as the text-command leaves

## Best next target

The cleanest next move is now the early and middle selector block rather than the already-healthy late stat block.

Best remaining targets:

- selectors `1..5`, to decide what each fixed-width WRAM string buffer actually represents in gameplay terms
- selector `2` specifically, because every currently exposed `0x19 28` hit loops over it as a character string in prayer/system text
- whether any ordinary script path exposes selector `8` directly as the current-character-name entry
