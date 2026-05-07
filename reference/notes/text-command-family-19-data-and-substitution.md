# Text Command Family `0x19` (Data Return / Substitution / Queue Helpers)

This note captures the current best local map for bank-`01` text command family `0x19`.

See also [class2-cc19-1f-display-text-bridge.md](notes/class2-cc19-1f-display-text-bridge.md).
See also [class2-cc19-1f-cross-segment-reuse.md](notes/class2-cc19-1f-cross-segment-reuse.md).
See also [class2-cc19-20-eshop2-single-use.md](notes/class2-cc19-20-eshop2-single-use.md).
See also [text-command-family-1d-inventory-money.md](notes/text-command-family-1d-inventory-money.md).
See also [statistic-selector-family-c4550f-c3ee7a.md](notes/statistic-selector-family-c4550f-c3ee7a.md).
See also [respawn-warp-target-snapshot-helper-c230f3.md](notes/respawn-warp-target-snapshot-helper-c230f3.md).
See also [saved-coordinate-reload-path-c4c718-c0b967.md](notes/saved-coordinate-reload-path-c4c718-c0b967.md).
See also [transition-landing-mode-family-9f3f-9f41.md](notes/transition-landing-mode-family-9f3f-9f41.md).
See also [landing-destination-table-d57880.md](notes/landing-destination-table-d57880.md).
See also [naming-buffer-commit-family-c1ead6-c4d065.md](notes/naming-buffer-commit-family-c1ead6-c4d065.md).
See also [short-text-staging-buffer-9c9f.md](notes/short-text-staging-buffer-9c9f.md).
See also [text-entry-builder-c113d1-89d4.md](notes/text-entry-builder-c113d1-89d4.md).

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
- `0x20 -> C1:7B0D` (`LOAD_MUSHROOMIZED_SELECTOR_BYTE`)
- `0x21 -> C1:7B29 -> C1:6143` (food category helper)
- `0x22 -> C1:7B2E -> C1:68A0` (character-to-object direction helper)
- `0x23 -> C1:7B33 -> C1:6947` (NPC-to-object direction helper)
- `0x24 -> C1:7B38 -> C1:6A7B` (generated-sprite direction helper)
- `0x25 -> C1:7B3D -> C1:6F9F` (food condiment helper)
- `0x26 -> C1:7B42 -> C1:7037` (transition landing snapshot helper)
- `0x27 -> C1:7B47 -> C1:776A` (statistic-selector value helper)
- `0x28 -> C1:7B4C -> C1:4819` (statistic-selector character helper)
- default -> `C1:7B51 -> 0`

Parser/runtime cross-check looks healthy here: the current exposed script set hits nearly the whole late half of the family, and unlike the earlier false-lead families there is no evidence that the ordinary live center itself is misidentified.

## Source scaffold promotion

The front, middle, and display-side local `0x19` leaves now have additional checked-in source coverage. `C1:4819..48AC` covers the statistic-selector/string-character helper, `src/c1/c1_9249_print_statistic_selector_value.asm` covers the display-side statistic-selector value printer, `src/c1/c1_461a_handle_text_command0_estore_to_argmem.asm` covers `0x19 10/11`, `src/c1/c1_4eab_handle_text_command10_parameterized_pause.asm` covers `C1:5007..506F` for `0x19 16`, `C1:506F..50E4` for `0x19 05`, and `C1:5384..53AF` for `0x19 18`, `src/c1/c1_575d_test_equipped_item_presence_for_text_command.asm` covers `0x19 19/1A/1B/1C/1D/21`, and `src/c1/c1_621f_finalize_text_command1_fc0_jump_multi2_target.asm` covers `0x19 22/23/24/25/26`. `src/c1/c1_461a_handle_text_command0_estore_to_argmem.asm` now names the `0x19 10` active overworld registry type-code read, the `0x19 11` character-name pointer resolver through `C2:22D3`, current text-context character index use, one-based name-letter lookup, and primary text-context staging outputs. `src/c1/c1_4eab_handle_text_command10_parameterized_pause.asm` now names the `0x19 05/16/18` status and experience helper contracts into `C4:58AF`, `C4:58FE`, and `C4:599A`. `src/c1/c1_575d_test_equipped_item_presence_for_text_command.asm` now names the `0x19 19/1A/1B` inventory, Escargo storage, and loaded-string count staging contracts, plus the `0x19 1C/1D` delivery/pickup queue layout, pending-item versus character-inventory removal paths, and primary/secondary text staging outputs. `src/c1/c1_7796_finalize_loaded_string_with_companion_pointer.asm`, `src/c1/c1_7889_continue_loaded_string_inline_collector.asm`, and `src/c1/c1_78f7_start_loaded_string_inline_collector.asm` now name the loaded-string byte buffer, companion-byte queue, callback return values, `C1:13D1` text-entry install contract, and the Escargo `0x19 14` staging path. `src/c1/c1_7b0d_load_display_text_mushroomized_selector_byte.asm` now names the `0x19 21..28` tail helper targets directly, `src/c1/c1_7708_classify_equipped_item_offensive_defensive.asm` names the `0x19 27` statistic-selector staging contract, and `src/c1/c1_4819_read_statistic_selector_string_character.asm` names the matching `0x19 28` selector-character reader. The source-backed C1 scaffold validates byte-for-byte: `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

Source polish follow-up (2026-05-06): the `C1:575D..621F` module is now
helper-call clean for its `0x19 19/1A/1B/1C/1D/21` leaves. The delivery and
pickup queue paths now name the pending-item removal, character-inventory slot
read/removal, delivery queue store, and primary/secondary context staging
contracts directly, which makes this loaded-string/inventory bridge easier to
carry into the next bank joins.

Source polish follow-up (2026-05-06): the same module now names the
consumer-side queued-byte ABI for `0x19 19/1C/1D`. The character inventory-slot
reader, delivery/pickup queue writer, and delivery/pickup queue reader all
stage one byte through `$97BA/$97CA` and now return named callback low words,
so the `0x19` queue helpers match the surrounding `0x1D` source vocabulary.

Source polish follow-up (2026-05-06): the `C1:575D..621F` data-return leaves
now expose their caller-frame output ABI too. `0x19 19`, `0x19 1A`, `0x19 1B`,
and `0x19 1D` stage inventory-slot item bytes, selected character ids, Escargo
storage bytes, loaded-string counts, and delivery queue owner/item bytes
through named `$0E/$10` text-context source aliases before primary or
secondary context installation. The queue scan temporaries remain named only
where they are used as real scan state.

Source polish follow-up (2026-05-06): the `C1:621F..7274` module now names the
helper edges for `0x19 22/23/24/25/26` directly. The three direction helpers
call the C4 registry, visual-type, and pose-descriptor facing-octant helpers by
name; the condiment leaf calls the C1 condiment lookup helper; and the landing
snapshot leaf calls `C2:30F3` by name after resolving its staged argument.

Source polish follow-up (2026-05-06): the three `0x19 22/23/24` direction
helpers now name their output staging too. Each helper increments the C4-facing
octant result and installs it through the named `$0E/$10` text-context source
aliases before returning through the secondary context, matching the adjacent
condiment and scripted-battle result handoffs.

Source polish follow-up (2026-05-06): the `0x19 25` condiment leaf now also
names its local staging in the same source module. It resolves either the
incoming food-item byte or the next text argument, calls the condiment lookup
helper, and installs the result through the shared `$06/$08 -> $0E/$10`
text-context result path.

Source polish follow-up (2026-05-06): the adjacent `0x19 26` leaf now has an
explicit source label at `C1:7037` and names its one-word argument fallback
before the `C2:30F3` snapshot handoff. This keeps the local transition-landing
snapshot adapter visible without promoting the broader respawn/warp wording
into the C1 source name.

Source polish follow-up (2026-05-06): the `C1:78F7..7AE3` dispatcher module now
also names the shared `0x18` window-helper edge surface that lives beside the
`0x19` loaded-string dispatcher. This does not change the `0x19` case map, but
it makes the mixed module's two dispatcher roles explicit: `C1:78F7` remains
the loaded-string collector entry for `0x19 02`, while the adjacent `C1:790B`
window-family front now has named callback returns and named window/context
helper calls.

Source polish follow-up (2026-05-06): the `0x19` side of the same dispatcher
now names its selector ladder in source. The comparisons cover the live
data-return map from `0x19 02/04/05/10/11/14/16/18/19/1A/1B/1C/1D/1E/1F/20`
through the `21..28` food, direction, condiment, landing, and statistic
selector tail, so the helper-pointer table reads as a family dispatch instead
of a numeric ladder.

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
- the source now names `$97D7` as the loaded-string byte buffer, `$97CA` as
  the collector count, `C1:7889` as the continuation callback, and `C1:7796`
  as the companion-byte finalizer that packs three queued bytes plus the final
  byte before calling `C1:13D1`
- its flush-side branch at `C1:78B2` null-terminates the queue and hands it to [text-entry-builder-c113d1-89d4.md](notes/text-entry-builder-c113d1-89d4.md), which installs a live `89D4` text-entry record rather than a stable selector buffer
- [text-entry-builder-c113d1-89d4.md](notes/text-entry-builder-c113d1-89d4.md) still should be treated as adjacent shared infrastructure rather than the defining source of selector-`2` semantics
- the first clean local write-side bridge into selector `2` is now naming-specific:
  - [naming-buffer-commit-family-c1ead6-c4d065.md](notes/naming-buffer-commit-family-c1ead6-c4d065.md) pins `C1:EBA0..EBDD`
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
- the source now names the deferred status target/effect arguments, status-group
  selector, `C4:58FE` status write helper, and result staging through `C1:045D`

### `0x19 10`

Best current read:

- get character number

Confidence:

- locally decent; parser-backed

Why:

- abundant exact parsed hits
- local leaf `C1:4723`
- the source now names the `C1:90E6` active overworld registry type-code
  reader and the primary text-context output staging contract
- script neighborhoods use it exactly like "party slot to actual character id" conversion

### `0x19 11`

Best current read:

- get one letter from a character name

Confidence:

- parser-backed and locally consistent

Why:

- local leaf `C1:47CC`
- the source now names the `C2:22D3` character-name pointer resolver,
  current text-context character index, one-based byte lookup, and primary
  text-context output staging contract
- script neighborhoods print the resulting letter immediately afterward

### `0x19 14`

Best current read:

- return one item from Escargo storage and advance the secondary-memory index

Confidence:

- locally decent; community-doc-backed and locally consistent

Why:

- live ordinary dispatcher includes it directly
- local body at `C1:7A96` reads from `$984B` using the value from `C1:0400`, then stages the result through `C1:045D` and increments the secondary-memory side through `C1:042E`
- the source now names that staging path as an Escargo storage item-byte read
  into the ordinary display-text source pointer pair
- exact parsed hits appear only in `ESHOP3`, which is exactly where Escargo storage enumeration belongs

### `0x19 16`

Best current read:

- get one byte of character status

Confidence:

- parser-backed and locally consistent

Why:

- local leaf `C1:5007`
- resolves one character selector and one status-group byte, then hands them to bank-`04` helper `C4:58AF`
- the source now names the deferred target selector, status-group selector,
  `C4:58AF` status-byte read helper, and primary text-context staging output
- exact parsed hits occur in `ESHOP2`

### `0x19 18`

Best current read:

- return amount of experience needed to level up

Confidence:

- parser-backed and locally consistent

Why:

- exact parsed hits occur in `ESHOP3`
- local leaf `C1:5384` is a compact single-argument reader that feeds bank-`04` helper `C4:599A`
- the source now names `C4:599A` as the required-experience remaining helper
  and stages its returned word pair through the primary text-context output
- the community docs and the sparse local use both match Dad/save-style progress text much better than any inventory or menu reading

### `0x19 19`

Best current read:

- return one item from a character inventory slot

Confidence:

- locally strong

Why:

- the inherited parser label `ADD_ITEM_ID_TO_WORK_MEMORY` is too vague
- local leaf `C1:597F` resolves one character id and one inventory slot index, calls [C3:E977](notes/item-slot-helper-pair-c3e977-c3ee14.md), stages the found item through `C1:0489`, and stages the source character id through `C1:045D`
- the source now names the deferred character selector, inventory-slot selector,
  `C3:E977` item-byte read, secondary item output, and primary character output
- exact parsed hits cluster in inventory / service text neighborhoods

So this now reads better as a real character-inventory item lookup than as a generic memory-add helper.

### `0x19 1A`

Best current read:

- return one item from Escargo storage

Confidence:

- locally strong

Why:

- local body `C1:5B0E` resolves the item index, reads from `$984B`, and stages the result through `C1:045D`
- the source now names `$984B` as the Escargo storage byte array and stages the
  selected item byte through the primary text-context output
- exact parsed hits occur only in `ESHOP3` plus one debug hit

### `0x19 1B`

Best current read:

- return number of strings loaded for a window

Confidence:

- parser-backed and locally consistent

Why:

- local body `C1:5C36` reads the one-byte selector and routes through context helper `C1:2BD5`, then stages the result through `C1:045D`
- the source now names the `C1:2BD5` loaded-string count helper and its primary
  text-context output staging
- exact parsed hits occur in `ESHOP1`, which is full of window-relative loaded-string use

### `0x19 1C`

Best current read:

- queue item for delivery or pickup

Confidence:

- locally decent; community-doc-backed and locally consistent

Why:

- local body `C1:5FF7` removes an item either from Escargo storage (`0xFF` path) or from a character inventory slot through [C1:8C27](notes/inventory-slot-removal-helper-c18c27.md), then hands the result to queue helper `C1:5FB1`
- the source now names the three-entry delivery queue rooted at `$97F5`,
  the owner/source byte side at `+0xB6`, the item byte side at `+0xB9`, and
  the `C1:91B0` pending-item versus `C3:E977`/`C1:8C27` inventory-removal
  split
- exact parsed hits cluster entirely in `ESHOP3`

### `0x19 1D`

Best current read:

- return information about one queued delivery or pickup item

Confidence:

- locally decent; community-doc-backed and locally consistent

Why:

- local body `C1:6080` resolves an entry index, reads paired queue fields near `97F5+`, stages one through `C1:045D` and the other through `C1:0489`, and optionally clears the queue slot
- the source now names the primary item byte and secondary owner/source byte
  staging outputs, plus the optional queue-slot clear path after readback
- exact parsed hits occur entirely in `ESHOP3`

### `0x19 1E`

Best current read:

- load pointer substitution

Confidence:

- locally strong

Why:

- this case is already pinned in the battle-text substitution family
- local body `C1:7AE3` reads through `C1:AD26` and stages the resulting pointer through the text pipeline
- the source now comments this as the display-text `19 1E` consumer of the
  `$9D12/$9D14` pointer payload staged by `C1:AD0A`
- exact parsed hits occur only in `EBATTLE8`

See also [class2-cc19-1f-display-text-bridge.md](notes/class2-cc19-1f-display-text-bridge.md).

### `0x19 1F`

Best current read:

- load byte substitution

Confidence:

- locally strong

Why:

- this case is already pinned end-to-end
- local body `C1:7AF3` reads the one-byte substitution slot at `$9D11`
- exact parsed hits are broad across goods and battle text

See also [class2-cc19-1f-display-text-bridge.md](notes/class2-cc19-1f-display-text-bridge.md) and [class2-cc19-1f-cross-segment-reuse.md](notes/class2-cc19-1f-cross-segment-reuse.md).

### `0x19 20`

Best current read:

- load the current `$98A4` byte into the text pipeline

Confidence:

- locally strong on mechanism; narrower semantic meaning still contextual

Why:

- local body `C1:7B0D` is pinned
- only one exact parsed hit exists, in `ESHOP2`
- the strongest WRAM-side evidence ties `$98A4` to the overworld entity / mushroomized-adjacent controller family

See also [class2-cc19-20-eshop2-single-use.md](notes/class2-cc19-20-eshop2-single-use.md).

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
- `C1:776A` resolves one statistic selector and feeds it through `C3:EE7A`, then stages the result into the text pipeline; this leaf is now source-backed in `src/c1/c1_7708_classify_equipped_item_offensive_defensive.asm`
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
- `0x19 27 / 28` as the shared statistic-selector tail; see [statistic-selector-family-c4550f-c3ee7a.md](notes/statistic-selector-family-c4550f-c3ee7a.md)

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
