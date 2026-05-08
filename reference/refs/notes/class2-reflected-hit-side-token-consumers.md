# Class2 Reflected Hit Side Token Consumers

This note tightens the bank-`C3` consumers that read `$5E77` / `$5E78` after the reflected-hit rebuild path.

See also [class2-reflected-hit-side-buffer-flags.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-reflected-hit-side-buffer-flags.md).
See also [class2-reflected-hit-text-context.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-reflected-hit-text-context.md).
See also [class2-reflected-hit-context-rebuild.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-reflected-hit-context-rebuild.md).
See also [class2-row-position-text-cluster-c454f0.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-row-position-text-cluster-c454f0.md).

## Current strongest claim

The appended bytes tracked by `$5E77` and `$5E78` now look much more like battle text control tokens than raw text suffix bytes.

The safe version of that claim is:

- the reflected-hit rebuild can append a short side-specific token pair into the rebuilt side buffer
- bank `C3` later detects that append through `$5E77` / `$5E78`
- the follow-up path does not treat the bytes like plain printable text
- instead it routes through the same bank-`C4` token machinery that handles battle text control bytes in the `0x50..0x7F` range

That is a materially stronger statement than our earlier "optional suffix" wording.

## What `C3:E773` and `C3:E78F` are doing

The two consumers are paired.

Local behavior from the ROM bytes:

- `C3:E773` handles the first side and falls back to `$9658`
- `C3:E78F` handles the second side and falls back to `$965A`
- both first check whether the side id is `FFFF`
- if so, they clear the companion side flag (`$5E77` or `$5E78`) and skip the special handling
- otherwise they read the corresponding flag and only continue if it is nonzero
- then they resolve the current side id through selector `#$005E` into the `D5:9589` descriptor family
- they read descriptor byte `+0x00` and require it to be nonzero before continuing
- then they branch on `$5E76`
- if `$5E76 == #$0070`, they pass pointer `C2:0998` to `C4:47FB`
- otherwise they pass pointer `C2:099C` to `C4:47FB`

That branch is now much less mysterious than before. `0x70` is not just an arbitrary side-token id; it is very likely the ordinary non-printing `@` text control byte from the EarthBound text encoding.

So the pair is no longer best described as "check a flag and maybe do some formatting." It is selecting one of two side-token helper data blocks and dispatching them through a dedicated bank-`C4` routine.

## Why `$5E76` matters more now

The strongest local clue came from widening into bank `C4`.

`C4:44E61` is a generic battle text control-token handler for the `0x50..0x7F` family. In that handler:

- the incoming token code is kept in `Y`
- the current token code is stored to `$5E76`
- the code computes `(token - 0x50)`
- that index is used to walk the token metadata table at `C3:F054`
- the handler manages `$5E75` as a small "already handled" suppression flag for part of that token family

That means `$5E76` is not vague transient state. It is the last active text control byte from the `0x50..0x7F` family seen by this formatter.

The key refinement is that `C4:44E61` is not battle-specific. The same routine is reached from other generic text-building paths too, which makes `$5E76 == #$0070` much more likely to mean `the current text stream just hit the ordinary EBTEXT @ control code` than `some battle-only row token fired`.

## Why the appended bytes now read like control tokens

This matters because the reflected-hit rebuild side already showed an optional append of bytes shaped like:

- `0x50`
- `0x70 + something row-local`

At first those looked like arbitrary side suffix bytes.

After tracing `C4:44E61`, the safer interpretation is:

- the rebuild is appending battle text control-token bytes
- `$5E77` / `$5E78` record that one of those side-specific token sequences was appended
- `$5E76` remembers the active token code from that family
- `C3:E773` / `C3:E78F` later resolve a special subset of that token family through `C4:47FB`

So the flags are no longer just "extra bytes were appended." They are now best read as "a side-specific control-token sequence was appended and still needs late resolution."

## What `C4:47FB` seems to do

`C4:47FB` still is not fully named, but the local control flow is much less mysterious now.

It takes:

- a far pointer from `$0E/$10`, which in this path is either `C2:0998` or `C2:099C`
- a small argument in `A`, which is `#$0004` here
- current battle-side state through `$9658/$965A`, the selected-row resolver, and the `D5:9589` descriptor family

Then it:

- resolves the current row/descriptor again through selector `#$0052`
- folds in a small row-local state nibble from `9E23`
- computes a threshold-like value from descriptor and helper data
- compares that against descriptor byte `+0x0A`
- if the compare passes, it calls `C1:0C79` and sets `$5E75 = 1`
- then it restores the caller-supplied pointer and calls `C1:0C8C`

The important part is the bank-`C1` targets:

- `C1:0C79` is just a wrapper over `C4:38B1`
- `C1:0C8C` is in the same battle text/UI helper family we have already been using for textbox-context work

So this still looks like text-control resolution, not gameplay logic.

## What the two `C2` data blocks probably represent

`C2:0998` and `C2:099C` now look very likely to be tiny text fragments rather than opaque helper records.

Their first bytes decode cleanly with the EarthBound text table:

- `C2:0998 = "The "`
- `C2:099C = "the "`

That lines up unusually well with the local call pattern:

- `C3:E773` / `C3:E78F` pass one of those addresses to `C4:47FB`
- they also pass `#$0004` in `A`
- the selected data length matches a 4-character article exactly

So the safest current read is no longer "two related helper records." It is:

- `C2:0998` is a capitalized article fragment, `"The "`
- `C2:099C` is the lowercase companion, `"the "`
- the two fragments overlap in ROM exactly the way we would expect for fixed strings starting at adjacent bytes
- `C3:E773` / `C3:E78F` choose between them based on whether `$5E76` is exactly `0x70`

The remaining uncertainty is now much narrower. The fragment itself is no longer in doubt, and the best current interpretation of `$5E76 == #$0070` is simply `the last control byte was @`, i.e. sentence-start or forced-capitalization context.

A nearby reuse of `C4:3E31` makes this safer. In `C4:51FA`, the same helper is called with a normal text pointer and length `#$001E` while building battle-side text layout state, which makes `C4:3E31` read like a tokenized text-width or text-metrics walker rather than a gameplay selector. That is exactly the kind of helper we would expect `C4:47FB` to use when deciding whether to inject `"The "` or `"the "`.

Two more local-plus-reference clues support the `@` reading:

- `C4:4424A` special-cases incoming token `#$0070` and clears an auxiliary per-character byte instead of storing a normal visible glyph marker, which is a strong fit for a non-printing formatting control
- the `ebsrc` text phrase lists contain `@The `, `@You `, plain `The `, and plain `the ` as separate entries, which matches the idea that `@` marks capitalization context rather than literal printed text

## New row-position anchor

A useful local-plus-reference anchor now sits immediately after `C4:51FA`.

From the `ebsrc` bank-`C4` include order plus the local bytes:

- `C4:54F0..C4:54F1` is a tiny unresolved `battle_to_text` block
- `C4:54F2..C4:5501` decodes locally to `To the Front Row`
- `C4:5502..C4:550D` decodes locally to `the Back Row`

That does not prove the whole sentence template yet, but it does move the side-token path out of the generic `maybe some side phrase` bucket. The article-choice machinery now sits right next to a real battle row-position phrase family, which makes a row-text interpretation materially safer.

## How this sharpens the player-visible interpretation

The reflected-hit rebuild path now looks like this:

1. swap the acting and receiving rows
2. rebuild attacker-side and target-side text-context buffers
3. optionally append side-specific battle text control tokens
4. record those appends in `$5E77` / `$5E78`
5. later, bank `C3` resolves those tokenized side markers through `C4:47FB`
6. battle text/UI helpers in bank `C1` finish the late formatting step

That is a stronger and narrower statement than "there is an optional suffix." It now looks like a real delayed token-resolution stage inside battle textbox formatting.

## Current safest takeaway

The safest takeaway now is:

- `$5E77` and `$5E78` gate late side-token resolution, not raw text copying
- `$5E76` stores the current text control byte from the `0x50..0x7F` formatter family, and `#$0070` now looks best as the ordinary non-printing `@` control code
- `C3:E773` and `C3:E78F` dispatch side-specific token helpers only when those side flags are set
- the follow-up path is text/control-token machinery in banks `C4` and `C1`, not gameplay logic
- the most likely user-facing meaning is now a delayed article choice driven by capitalization context: `"The "` after `@`-style sentence-start control, otherwise `"the "`, inside a row-position-aware battle text fragment family that sits next to `To the Front Row` and `the Back Row`

## Best next target

The best next move is to name the text-control condition behind `$5E76 == #$0070` more tightly, or to identify the side/row phrase that receives the selected article after `C4:47FB` finishes.

## Update: enemy-data anchor

A later cross-check tightened this note substantially.

The `D5:9589` record family reached through selector `#$005E` now lines up very strongly with the `ebsrc` `enemy_data` struct and `ENEMY_CONFIGURATION_TABLE`.

That matters directly here because the byte these two consumers check at record `+0x00` is no longer just an anonymous gate. It now very likely matches `enemy_data::the_flag`, which is exactly the kind of enemy-name article flag we would expect for a `"The "` versus `"the "` branch.

That makes the local article-selection path sharper:

- `C3:E773` / `C3:E78F` resolve an enemy record
- they require `enemy_data::the_flag` to be nonzero
- then they choose `"The "` or `"the "` based on text-control context from `$5E76`

Combined with the nearby row-position text cluster and the `enemy_data::row` field at record `+0x5B`, the current safest interpretation is that this late token path is doing enemy-name and row-aware battle text formatting rather than a generic side suffix pass.

See also [class2-d59589-enemy-data-crosswalk.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-d59589-enemy-data-crosswalk.md).
