# Class2 Row Position Text Cluster at C4:54F0

This note captures the small battle-text cluster that begins immediately after `C4:51FA` / `LayoutActiveTextEntryChainForWindow` and helps anchor the late side-token path in player-visible row-position text.

See also [class2-reflected-hit-side-token-consumers.md](notes/class2-reflected-hit-side-token-consumers.md).
See also [class2-reflected-hit-text-context.md](notes/class2-reflected-hit-text-context.md).

## Why this cluster matters

The best recent question was whether the delayed article choice around `$5E76`, `$5E77`, and `$5E78` was feeding some generic side phrase or something more specific.

The local ROM plus the quarantined `ebsrc` reference now give a better anchor.

In `ebsrc`, the US bank-`C4` include order is:

- `unknown/C4/C451FA.asm`
- `data/text/battle_to_text.asm`
- `data/text/battle_front_row_text.asm`
- `data/text/battle_back_row_text.asm`

That places a row-position text family immediately after `C4:51FA`.

## What the local ROM bytes show

The local bytes line up with that layout cleanly.

At `C4:54F0` through `C4:550D`, the cluster is:

- `C4:54F0..C4:54F1`: two still-unresolved bytes, almost certainly the tiny `battle_to_text` block from the include order
- `C4:54F2..C4:5501`: `To the Front Row`
- `C4:5502..C4:550D`: `the Back Row`

The two decoded strings come straight from the local US ROM bytes using the ordinary EarthBound US text mapping:

- `C4:54F2 = 84 9F 50 A4 98 95 50 76 A2 9F 9E A4 50 82 9F A7 = "To the Front Row"`
- `C4:5502 = A4 98 95 50 72 91 93 9B 50 82 9F A7 = "the Back Row"`

The leading two-byte block at `C4:54F0` is not safely decoded yet, so I am not forcing a literal reading for it. The include name `battle_to_text.asm` makes it very likely that it belongs to the same row-position phrase family rather than being unrelated data.

## Why the local code supports the same read

The nearby routine body around `C4:51FA` gives one more useful local clue.

`C4:51FA`, now named `LayoutActiveTextEntryChainForWindow`, calls `C4:3E31` with length `#$001E` while measuring the text pointer stored at each active `$89D4` entry's `record + 13`. That same `0x001E` length matches the size of the whole row-position text cluster from `C4:54F0` through `C4:550D` exactly.

So even without trusting the reference filenames, the local code is already treating that region like one compact 30-byte text block.

## Safest current interpretation

The safest current interpretation is:

- the bank-`C3` side-token/article machinery lives right next to a real row-position text family
- that family includes explicit front-row and back-row phrases in the local ROM
- the late `$5E76/$5E77/$5E78` resolution path is therefore more likely to be feeding battle row-position wording than a generic side suffix

I am still leaving one part open:

- the exact semantic condition represented by `$5E76 == #$0070`
- the exact role of the unresolved two-byte `C4:54F0` block

## Practical takeaway

This does not prove the entire sentence template yet, but it does materially narrow the space.

The late side-token path now looks much more like battle textbox formatting around row-position phrases such as `To the Front Row` and `the Back Row`, rather than a generic side-label system.
