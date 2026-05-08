# Text Command Family `0x19` (Data Return / Substitution / Queue Helpers)

This note captures the current best local map for bank-`01` text command family `0x19`.

See also [class2-cc19-1f-display-text-bridge.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-1f-display-text-bridge.md).
See also [class2-cc19-1f-cross-segment-reuse.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-1f-cross-segment-reuse.md).
See also [class2-cc19-20-eshop2-single-use.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-20-eshop2-single-use.md).
See also [text-command-family-1d-inventory-money.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-1d-inventory-money.md).
See also [statistic-selector-family-c4550f-c3ee7a.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/statistic-selector-family-c4550f-c3ee7a.md).
See also [respawn-warp-target-snapshot-helper-c230f3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/respawn-warp-target-snapshot-helper-c230f3.md).
See also [saved-coordinate-reload-path-c4c718-c0b967.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/saved-coordinate-reload-path-c4c718-c0b967.md).
See also [transition-landing-mode-family-9f3f-9f41.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/transition-landing-mode-family-9f3f-9f41.md).
See also [landing-destination-table-d57880.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/landing-destination-table-d57880.md).
See also [naming-buffer-commit-family-c1ead6-c4d065.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/naming-buffer-commit-family-c1ead6-c4d065.md).
See also [short-text-staging-buffer-9c9f.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/short-text-staging-buffer-9c9f.md).
See also [text-entry-builder-c113d1-89d4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-entry-builder-c113d1-89d4.md).

## Main result

`0x19` is now best read as the bank-`01` text family for "return or stage some small piece of game state into the text pipeline."

Unlike the tighter adjacent families:

- `0x18` focuses on windows and selection helpers
- `0x1A` focuses on menus
- `0x1D` focuses on inventory / money / possession checks
- `0x1E` focuses on recovery / experience / stat boosts

`0x19` is a broader mixed family. Its live center includes:

- loaded-string helpers
- status / party / inventory readers
- Escargo storage and delivery-queue helpers
- battle-text substitution loaders
- direction / facing helpers
- a small mixed statistic and dynamic-string selector tail

So the safest current umbrella name is not one narrow subsystem label. It is a data-return / substitution / queue-helper family.

## Local dispatcher proof

The ordinary script parser routes this family through:

- top-level parser `C1:890E`
- `0x19 -> C1:8AC4`
- family callback root `C1:79AA`

The live local case map at `C1:79AA` is:

- `0x02 -> C1:7A78 -> C1:78F7`
- `0x04 -> C1:7A7E`
- `0x05 -> C1:7A84 -> C1:506F`
- `0x10 -> C1:7A8A -> C1:4723`
- `0x11 -> C1:7A90 -> C1:47CC`
- `0x14 -> C1:7A96`
- `0x16 -> C1:7ABB -> C1:5007`
- `0x18 -> C1:7AC1 -> C1:5384`
- `0x19 -> C1:7AC7 -> C1:597F`
- `0x1A -> C1:7ACD -> C1:5B0E`
- `0x1B -> C1:7AD3 -> C1:5C36`
- `0x1C -> C1:7AD9 -> C1:5FF7`
- `0x1D -> C1:7ADE -> C1:6080`
- `0x1E -> C1:7AE3`
- `0x1F -> C1:7AF3`
- `0x20 -> C1:7B0D`
- `0x21 -> C1:7B29 -> C1:6143`
- `0x22 -> C1:7B2E -> C1:68A0`
- `0x23 -> C1:7B33 -> C1:6947`
- `0x24 -> C1:7B38 -> C1:6A7B`
- `0x25 -> C1:7B3D -> C1:6F9F`
- `0x26 -> C1:7B42 -> C1:7037`
- `0x27 -> C1:7B47 -> C1:776A`
- `0x28 -> C1:7B4C -> C1:4819`
- default -> `C1:7B51 -> 0`

Parser/runtime cross-check looks healthy here: the current exposed script set hits nearly the whole late half of the family, and unlike the earlier false-lead families there is no evidence that the ordinary live center itself is misidentified.

## Best current case map

### `0x19 02`

Best current read:

- load string to memory

Confidence:

- locally strong; parser-backed

Why:

- abundant exact parsed hits
- local callback root `C1:78F7`
- `C1:78F7` and the small state machine at `C1:7889` now look like a queued loader over `$97D7/$97CA`
- its flush-side branch at `C1:78B2` null-terminates the queue and hands it to [text-entry-builder-c113d1-89d4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-entry-builder-c113d1-89d4.md), which installs a live `89D4` text-entry record rather than a stable selector buffer
- [text-entry-builder-c113d1-89d4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-entry-builder-c113d1-89d4.md) still should be treated as adjacent shared infrastructure rather than the defining source of selector-`2` semantics
- the first clean local write-side bridge into selector `2` is now naming-specific:
  - [naming-buffer-commit-family-c1ead6-c4d065.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/naming-buffer-commit-family-c1ead6-c4d065.md) pins `C1:EBA0..EBDD`
  - `C4:D065` remaps the live naming-entry work buffer at `$9C9F` into `$9801`
  - `C0:8ED2` copies `0x0C` bytes from the same work buffer into `$97F5`
- raw immediate setup of `$9801` currently appears only in that naming path, while the strongest pinned non-naming item/equipment producers stop at `$9C9F` and shared builders; so the current prayer/system `0x19 28 0x02` hits no longer force a broader selector-`2` temp-buffer model by themselves
- script neighborhoods match menu-option / loaded-string setup rather than ordinary printing

### `0x19 04`

Best current read:

- clear loaded strings

Confidence:

- parser-backed and locally consistent

Why:

- exact parsed hits exist
- live ordinary dispatcher includes it directly
- its placement beside `0x19 02` fits the loaded-string family cleanly

### `0x19 05`

Best current read:

- inflict status

Confidence:

- parser-backed and locally consistent

Why:

- abundant exact parsed hits in ailment-heavy script neighborhoods
- local leaf `C1:506F` is a two-argument resolver into a dedicated bank-`04` status helper (`C4:58FE`)

### `0x19 10`

Best current read:

- get character number

Confidence:

- locally decent; parser-backed

Why:

- abundant exact parsed hits
- local leaf `C1:4723`
- script neighborhoods use it exactly like "party slot to actual character id" conversion

### `0x19 11`

Best current read:

- get one letter from a character name

Confidence:

- parser-backed and locally consistent

Why:

- local leaf `C1:47CC`
- script neighborhoods print the resulting letter immediately afterward

### `0x19 14`

Best current read:

- return one item from Escargo storage and advance the secondary-memory index

Confidence:

- locally decent; community-doc-backed and locally consistent

Why:

- live ordinary dispatcher includes it directly
- local body at `C1:7A96` reads from `$984B` using the value from `C1:0400`, then stages the result through `C1:045D` and increments the secondary-memory side through `C1:042E`
- exact parsed hits appear only in `ESHOP3`, which is exactly where Escargo storage enumeration belongs

### `0x19 16`

Best current read:

- get one byte of character status

Confidence:

- parser-backed and locally consistent

Why:

- local leaf `C1:5007`
- resolves one character selector and one status-group byte, then hands them to bank-`04` helper `C4:58AF`
- exact parsed hits occur in `ESHOP2`

### `0x19 18`

Best current read:

- return amount of experience needed to level up

Confidence:

- parser-backed and locally consistent

Why:

- exact parsed hits occur in `ESHOP3`
- local leaf `C1:5384` is a compact single-argument reader that feeds bank-`04` helper `C4:599A`
- the community docs and the sparse local use both match Dad/save-style progress text much better than any inventory or menu reading

### `0x19 19`

Best current read:

- return one item from a character inventory slot

Confidence:

- locally strong

Why:

- the inherited parser label `ADD_ITEM_ID_TO_WORK_MEMORY` is too vague
- local leaf `C1:597F` resolves one character id and one inventory slot index, calls [C3:E977](/F:/Earthbound%20Decomp%20-%20Codex/notes/item-slot-helper-pair-c3e977-c3ee14.md), stages the found item through `C1:0489`, and stages the source character id through `C1:045D`
- exact parsed hits cluster in inventory / service text neighborhoods

So this now reads better as a real character-inventory item lookup than as a generic memory-add helper.

### `0x19 1A`

Best current read:

- return one item from Escargo storage

Confidence:

- locally strong

Why:

- local body `C1:5B0E` resolves the item index, reads from `$984B`, and stages the result through `C1:045D`
- exact parsed hits occur only in `ESHOP3` plus one debug hit

### `0x19 1B`

Best current read:

- return number of strings loaded for a window

Confidence:

- parser-backed and locally consistent

Why:

- local body `C1:5C36` reads the one-byte selector and routes through context helper `C1:2BD5`, then stages the result through `C1:045D`
- exact parsed hits occur in `ESHOP1`, which is full of window-relative loaded-string use

### `0x19 1C`

Best current read:

- queue item for delivery or pickup

Confidence:

- locally decent; community-doc-backed and locally consistent

Why:

- local body `C1:5FF7` removes an item either from Escargo storage (`0xFF` path) or from a character inventory slot through [C1:8C27](/F:/Earthbound%20Decomp%20-%20Codex/notes/inventory-slot-removal-helper-c18c27.md), then hands the result to queue helper `C1:5FB1`
- exact parsed hits cluster entirely in `ESHOP3`

### `0x19 1D`

Best current read:

- return information about one queued delivery or pickup item

Confidence:

- locally decent; community-doc-backed and locally consistent

Why:

- local body `C1:6080` resolves an entry index, reads paired queue fields near `97F5+`, stages one through `C1:045D` and the other through `C1:0489`, and optionally clears the queue slot
- exact parsed hits occur entirely in `ESHOP3`

### `0x19 1E`

Best current read:

- load pointer substitution

Confidence:

- locally strong

Why:

- this case is already pinned in the battle-text substitution family
- local body `C1:7AE3` reads through `C1:AD26` and stages the resulting pointer through the text pipeline
- exact parsed hits occur only in `EBATTLE8`

See also [class2-cc19-1f-display-text-bridge.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-1f-display-text-bridge.md).

### `0x19 1F`

Best current read:

- load byte substitution

Confidence:

- locally strong

Why:

- this case is already pinned end-to-end
- local body `C1:7AF3` reads the one-byte substitution slot at `$9D11`
- exact parsed hits are broad across goods and battle text

See also [class2-cc19-1f-display-text-bridge.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-1f-display-text-bridge.md) and [class2-cc19-1f-cross-segment-reuse.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-1f-cross-segment-reuse.md).

### `0x19 20`

Best current read:

- load the current `$98A4` byte into the text pipeline

Confidence:

- locally strong on mechanism; narrower semantic meaning still contextual

Why:

- local body `C1:7B0D` is pinned
- only one exact parsed hit exists, in `ESHOP2`
- the strongest WRAM-side evidence ties `$98A4` to the overworld entity / mushroomized-adjacent controller family

See also [class2-cc19-20-eshop2-single-use.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-cc19-20-eshop2-single-use.md).

### `0x19 21`

Best current read:

- return category of food item

Confidence:

- community-doc-backed and locally consistent

Why:

- local leaf `C1:6143` resolves one item id, calls `C2:2524`, and stages a small result byte
- the lone exact parsed hit is in `EGOODS0`, exactly beside the drink/condiment script logic

### `0x19 22`

Best current read:

- return direction from character to object

Confidence:

- parser-backed and locally consistent

Why:

- local body `C1:68A0` builds a three-argument deferred callback frame and resolves the final direction through `C4:62E4`
- exact parsed hits are abundant in event script

### `0x19 23`

Best current read:

- return direction from NPC to object

Confidence:

- parser-backed and locally consistent

Why:

- local body `C1:6947` is the clear sibling of `0x19 22`, with the same general three-argument direction-shaping structure

### `0x19 24`

Best current read:

- return direction from generated sprite to object

Confidence:

- parser-backed and locally consistent

Why:

- live ordinary dispatcher includes it directly as the third direction sibling
- exact parsed hits occur in event text only

### `0x19 25`

Best current read:

- return condiment to use on food

Confidence:

- community-doc-backed and locally consistent

Why:

- local leaf `C1:6F9F` belongs to the same `EGOODS0` battle-food neighborhood as `0x19 21`
- exact parsed hits are narrow but clean

### `0x19 26`

Best current read:

- snapshot current transition landing target state

Confidence:

- locally decent; community-doc-backed and locally consistent

Why:

- local leaf `C1:7037` resolves one staged byte or register value and hands it to `C2:30F3`
- `C2:30F3` snapshots current coordinates plus companion byte `$98B8`
- later `C2:ABFB -> C0:DD53` stages that byte into `$9F3F`, while caller state contributes landing mode `$9F41`
- success-side consumer `C0:DD79` uses `$9F3F` to select a `D5:7880` destination record, installs override coordinates from it, and forces a fresh landing-region/profile recomputation
- the saved coordinates are later consumed by `C4:C718` as part of a broader landing / reload path

So the old community wording "set respawn point" still looks directionally useful, but the safer local description is a transition-landing snapshot rather than the whole respawn routine.

### `0x19 27`

Best current read:

- return value of a statistic

Confidence:

- locally decent; community-doc-backed and locally consistent

Why:

- `C1:79AA` has a real live `0x27` case to `C1:776A`
- `C1:776A` resolves one statistic selector and feeds it through `C3:EE7A`, then stages the result into the text pipeline
- there are no currently exposed parsed hits in the available script dump, so this stays below the confidence of the neighboring cases

### `0x19 28`

Best current read:

- return one letter from a statistic string

Confidence:

- locally decent; community-doc-backed and locally consistent

Why:

- local body `C1:4819` uses the shared selector table at `C4:550F`, checks a string-length byte, and returns one indexed statistic character into working memory
- exact parsed hits occur in `EBATTLE7` and `ESYSTEM`

## Confidence boundaries

### Locally strong

- `0x19` routes through `C1:8AC4 -> C1:79AA`
- the live case map listed above
- `0x19 19` is a character-inventory item lookup, not just a generic "add item id" helper
- `0x19 1A` reads Escargo storage from `$984B`
- `0x19 1E` and `0x19 1F` are the pointer and byte substitution loaders
- `0x19 20` is the narrow `$98A4` loader in the mushroom-girl script path

### Community-doc-backed and locally consistent

- `0x19 14` as Escargo enumeration with secondary-memory increment
- `0x19 16` as one-byte character-status lookup
- `0x19 18` as "experience needed to level up"
- `0x19 1B` as loaded-string count for one window
- `0x19 1C / 1D` as the queued delivery/pickup pair
- `0x19 21` as food-item category
- `0x19 22 / 23 / 24` as the three direction helpers
- `0x19 25` as condiment lookup
- `0x19 26` as the transition-landing snapshot helper family
- `0x19 27 / 28` as the shared statistic-selector tail; see [statistic-selector-family-c4550f-c3ee7a.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/statistic-selector-family-c4550f-c3ee7a.md)

### Still open

- the exact gameplay names of landing modes `1..5` behind `$9F41`
- the exact queue-field layout behind `0x19 1C / 1D`
- whether `0x19 18` can be promoted from "community-doc-backed and locally consistent" to a direct local level-progress proof
- the exact early and middle selector-index crosswalk behind `C4:550F`; the late stat block plus the level/experience pair are now much healthier
- whether any non-naming queued-string path besides the current `0x19 02 -> $97D7/$97CA -> C1:13D1 -> 89D4` live-entry route ever refreshes stable selector buffers like `$9801`, now that the naming-side producer is pinned separately and the strongest non-naming text/item producers currently stop at `$9C9F`

## Best current interpretation

The safest current local interpretation is that `0x19` is the bank-`01` family for small data-return helpers that feed the text pipeline. Its center of gravity is not one subsystem but a repeated mechanic: read some current game state, stage it into working memory or argument memory, and let later script commands decide how to print or branch on it.

That makes this family the natural home for:

- loaded-string state
- inventory / storage item lookups
- queued-delivery bookkeeping
- substitution sources for battle text
- direction / facing helpers
- and a small statistics tail

The family is already in better shape than it first looked because the live dispatcher is stable and the most reused leaves (`0x1E/1F/20`, `0x19/1A`, `0x22..24`) are no longer just parser names.

## Best next target

The cleanest next move is probably the success-side branch of `0x19 26` or the selector-index side of `0x19 27 / 28`.

- `0x19 26` is no longer structurally mysterious; the remaining gap is the exact meaning of `$9F3F` and the landing modes in `$9F41`
- the statistics tail now has a real shared local anchor and a partial late-table crosswalk, so the next gain there is to name the remaining early and middle `C4:550F` selectors



