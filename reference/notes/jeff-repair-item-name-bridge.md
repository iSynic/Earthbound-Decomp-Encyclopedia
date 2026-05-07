# Jeff Repair Item-Name Bridge

This note captures the current local picture of how the `1F D0` Jeff-repair callback family connects to the visible `[1C 05 00]` item-name placeholders in the repair script.

See also [try-fix-item-callback-d0.md](notes/try-fix-item-callback-d0.md).
See also [class2-c1-display-text-substitution-handler-7af3.md](notes/class2-c1-display-text-substitution-handler-7af3.md).

## Main result

The Jeff-repair script is now tied to a real local `PRINT_ITEM_NAME` path instead of just a generic text placeholder.

The script-side anchor is straightforward:

- `ebsrc` defines `EBTEXT_PRINT_ITEM_NAME arg` as `.BYTE $1C, $05, arg`
- the Jeff-repair script uses `[1C 05 00]` three times around the repair text
- the middle line uses `{swap}` immediately before the third print, while keeping the same `PRINT_ITEM_NAME 0x00` selector

That makes the local question very specific: what does `PRINT_ITEM_NAME 0x00` resolve to, and why is `{swap}` enough to change the printed item name from the broken item to the repaired item?

## Local `1B` / `1C` family split

The strongest local runtime anchor is now the generic bank-`01` control-code dispatcher at `C1:890E`, not the earlier proxy leaf at `C1:7A00+`. In that live parser path, command byte `0x1B` dispatches through `C1:8ADC`, which installs callback low word `C1:7C36`, while command byte `0x1C` dispatches through `C1:8AE4`, which installs callback low word `C1:7D94`.

That matters because it upgrades the structural split from a good guess to a direct local execution path:

- `0x1A` runs through callback family `C1:7B56`
- `0x1B` runs through the memory/context-manipulation family rooted at `C1:7C36`
- `0x1C` runs through the print-family rooted at `C1:7D94`
- `0x1D` runs through callback family `C1:7F11`
- `0x1E` runs through callback family `C1:811F`
- `0x1F` runs through callback family `C1:81BB`

So Jeff repair's `{swap}` and `[1C 05 00]` are not just conceptually different commands. In the live parser, they are definitely entering two different bank-`01` callback families before they interact through the paired context slots.

One more local bridge still helps explain the `1B` side. The older proxy leaf at `C1:5C36` forwards its incoming `X` through `C1:2BD5`, and `C1:2BD5` is not hopping into unrelated overworld logic. It resolves the current `8650+` context through the same `C1:0301`-adjacent object family, reads field `+0x2B` from that live context, and then passes the result to `C1:138D`. `C1:138D` in turn walks a terminator-delimited table rooted at `89D4` through the familiar `C08FF7` mapper until it counts out the requested entry. So even where the exact parser plumbing is still being tightened, the bank-`01` side is clearly operating on current text-context data rather than some unrelated external subsystem.

## Locally proved `1B` mapping

The biggest gain from the latest pass is that most of the `0x1B` family is no longer just macro-backed inference. The live callback body at `C1:7C36` dispatches directly on the one-byte `0x1B` subselector in `X`, and several entries now line up cleanly with the script macro names:

- subcommand `0` -> `C1:7C70 -> C1:0324`
  This is the backup helper that copies live `+0x17/+0x1B/+0x1F` into saved `+0x21/+0x25/+0x29`, so it is now a good local fit for `COPY_ACTIVE_MEMORY_TO_STORAGE`.
- subcommand `1` -> `C1:7C76 -> C1:0380`
  This is the matching restore helper that copies `+0x21/+0x25/+0x29` back into live `+0x17/+0x1B/+0x1F`, so it is now a good local fit for `COPY_STORAGE_MEMORY_TO_ACTIVE`.
- subcommand `4` -> `C1:7CF8`
  This path snapshots live `+0x17`, reads live `+0x1B`, then installs the two sides back in opposite order through `C1:045D` and `C1:0489`, so it is now a good local fit for `SWAP_WORKING_AND_ARG_MEMORY`.
- subcommand `5` -> `C1:7D36`
  This path copies live `+0x17/+0x1B/+0x1F` into scratch `97CC/97CE/97D0/97D2/97D4`, so it is now a good local fit for `COPY_ACTIVE_MEMORY_TO_WORKING_MEMORY`.
- subcommand `6` -> `C1:7D5A`
  This path restores `97CC/97CE/97D0/97D2/97D4` back into live `+0x17/+0x1B/+0x1F`, so it is now a good local fit for `COPY_WORKING_MEMORY_TO_ACTIVE_MEMORY`.

The branch-style pair at subcommands `2` and `3` is now very close to full local proof. Both paths start by reading live `+0x17` through `C1:040A`, compare it against zero, and then either advance the current script pointer by four bytes or return low word `0x4103`. Case `2` returns `0x4103` only when live `+0x17` is zero, while case `3` returns `0x4103` only when live `+0x17` is nonzero, so they now line up very naturally with `JUMP_IF_FALSE` and `JUMP_IF_TRUE`.

The missing piece was `C1:4103` itself. Locally, that routine is a three-byte queue builder over `$97BA/$97BB/$97BC`: it gathers three queued payload bytes through the same `C09246` conversion helper family, ORs the resulting chunks together, and writes the assembled result back to the current callback slot pointer. That gives the branch pair the exact surrounding behavior we wanted: the `1B 02/03` handlers decide whether to skip the next four script bytes or hand those queued bytes to `C1:4103` so the generic parser can install the branch destination.

## Stronger read on the `1B` leaf itself

The most useful cleanup from the latest local pass is negative: the bank-`01` helpers at `C1:5C58`, `C1:5D6B`, and `C1:5E5C` are not hidden second-stage branches of `0x1B`. They belong to the separate `0x1F` subcommand dispatcher rooted at `C1:8320`, where values like `0x80`, `0xD0`, `0xD1`, `0xD2`, and `0xD3` are routed through the shared `C1:866B` wrapper. So those routines are useful parser context, but they are not local proof for `1B 04/05/06`.

What still holds up locally is the narrower `C1:2BD5` story. `C1:5C36` forwards its incoming `X` through `C1:2BD5`, and the other three direct callers of `C1:2BD5` make that helper look much more like a current-context remapper or predicate source than a global hardcoded subdispatch table. In `C1:9507`, `C1:ABD5`, and `C1:BC3B`, the callers pass only `0` or `1`, then simply test whether the returned value is nonzero before continuing down context-specific branches. Combined with the `867B -> 138D -> 89D4` chain, the safest current read is that `C1:2BD5` maps a small requested code through the live text/interaction context and returns a small remapped result or truthy/falsey capability value.

That does not fully solve the script-side `1B 02/03` dword question yet, but it does improve the local shape of the problem. The cleanest current explanation is no longer "`C1:5C36` must contain the whole memory-command switch". It is "`C1:5C36` likely resolves the one-byte `0x1B` subselector through current context, while the generic text parser may still be responsible for any extra command payload like the branch destinations used by `JUMP_IF_FALSE` and `JUMP_IF_TRUE`." I am still treating that last sentence as informed inference rather than proved local dispatch, but it fits the ROM evidence much better than trying to force `5C58/5D6B/5E5C` back into the `1B` family.

## Stronger local `1C` runtime mapping

`0x1C` now has the same kind of live-parser anchor. In the generic dispatcher, `0x1C` installs callback low word `C1:7D94`, and `C1:7D94` then dispatches on the `0x1C` subselector in `X`. The Jeff-repair print path is subcommand `5`, which routes through `C1:7E65` and returns low word `C1:46BF`. That gives us a cleaner local stack for the visible placeholder than before:

- top-level control code `0x1C` -> runtime family `C1:7D94`
- subcommand `0x05` -> item-name family `C1:46BF`
- selector `0` later resolves through the already-pinned `C1:463B` branch

So the earlier `C1:463B` result still holds, but it now sits inside a firmer local hierarchy: generic `0x1C` parser family, then `PRINT_ITEM_NAME`, then selector-`0`.

The first chunk of the `C1:7D94` case map is now local too:

- `0x1C 00` -> leaf `C1:40F9`
- `0x1C 01` -> leaf `C1:40B0`
- `0x1C 02` -> leaf `C1:4FD7`
- `0x1C 03` -> leaf `C1:488D`
- `0x1C 04` -> special inline handler `C1:7E5F`
- `0x1C 05` -> leaf `C1:46BF`
- `0x1C 06` -> leaf `C1:46DE`
- `0x1C 07` -> leaf `C1:45CA`
- `0x1C 08` -> leaf `C1:43B8`
- `0x1C 09` -> leaf `C1:40EF` (`SET_ACTIVE_WINDOW_TEXT_MODE`)
- `0x1C 0A` -> leaf `C1:53AF`
- `0x1C 0B` -> leaf `C1:5573`
- `0x1C 0C` -> leaf `C1:5BA7`

The `C1:4FD7`, `C1:516B`, `C1:51FC`, `C1:53AF`, and `C1:5573` leaves in that chunk are now checked in as decoded source in `src/c1/c1_4eab_handle_text_command10_parameterized_pause.asm`; `C1:5BA7` and `C1:61D1` are source-backed in `src/c1/c1_575d_test_equipped_item_presence_for_text_command.asm`. The combined C1 scaffold still validates byte-for-byte.

The script-side cross-checks are now good enough to put a few practical names on that chunk instead of only listing addresses:

- `0x1C 01` behaves like `PRINT_STAT`. It has very broad reuse, and a spot check at `C7:500D` shows it printing a stat in ordinary event text.
- `0x1C 02` behaves like `PRINT_CHAR_NAME`. It is one of the most common print-family commands in the script corpus, and shop/event text uses it exactly the way that name suggests.
- `0x1C 03` behaves like `PRINT_CHAR`. Its script use is much narrower, including battle-text loops like `C9:F74D` that repeatedly print character bytes.
- `0x1C 0A` behaves like `PRINT_NUMBER`. It is heavily concentrated in shops and hint-style text, and a live shop sample at `C5:1B93` prints a numeric price right after an item name.
- `0x1C 0C` behaves like `PRINT_VERTICAL_TEXT_STRING`. A clean script anchor at `C9:1870` uses it exactly that way in a menu-selection flow.

That makes the print-family landscape healthier than before: `PRINT_ITEM_NAME` now sits inside a real local subcommand table instead of looking like a one-off path that only happened to matter for Jeff repair.

The battle-facing tail of the same `0x1C` family is now shaping up cleanly too. The parser-backed hit counts are a useful sanity check here: `0x1C 0D` has 225 exact parsed hits, `0x1C 0E` has 99, `0x1C 0F` has 40, `0x1C 12` has 7, and `0x1C 13` has 80. Those are concentrated exactly where we would want them if the reference macro names were right: overwhelmingly in `EBATTLE*`, with a few spillovers into battle-adjacent goods/system text.

The dispatcher side also helps. In `C1:7D94`, the late cases route as:

- `0x1C 0D` -> `C1:7E9F`
- `0x1C 0E` -> `C1:7EC6`
- `0x1C 0F` -> `C1:7EED`
- `0x1C 12` -> `C1:7F02`
- `0x1C 13` -> `C1:7F07`

The first two are especially nice locally. `0x1C 0D` calls `C3:E75D` with `A = 0`, then uses `C1:AC9B`, which simply returns pointer `9CD7`; `0x1C 0E` does the same with `A = 1` and `C1:ACF2`, which returns pointer `9CF5`. Both then print a fixed `0x50`-byte fragment through `C447FB`. That is a very strong local fit for `PRINT_ACTION_USER_NAME` versus `PRINT_ACTION_TARGET_NAME`: same print machinery, different selected battle-name buffer.

`0x1C 0F` is also in decent shape now. It routes through `C1:AD26`, which reads the shared long pointer slot at `9D12/9D14` back into the active direct-page pointer pair, then immediately prints through the common `C1:0DF6` path. Combined with the exact-hit distribution, that still reads best as `PRINT_ACTION_AMOUNT`.

`0x1C 12` and `0x1C 13` are a little thinner but still good enough to place. `0x1C 12 -> C1:61D1` either takes explicit `X` or falls back to live `+0x1B`, then calls `C1:CA06` before returning; paired with the seven exact battle-only `PRINT_PSI_NAME 0x00` hits, that is now a good local fit for `PRINT_PSI_NAME`. `0x1C 13 -> C1:73C0` is more obviously parameter-driven: it consumes a queued one-byte argument, normalizes it through `C3:FAC9`, stages the result through `C1:045D`, and is backed by 80 exact parsed `DISPLAY_PSI_ANIMATION a, b` hits. So the practical local read there is now quite solid too: it is the PSI-animation display branch rather than just another opaque battle helper.

The remaining late cases are finally narrow enough to describe without hand-waving. `0x1C 14` and `0x1C 15` now line up well with the reference macro names `LOAD_SPECIAL` and `LOAD_SPECIAL_FOR_JUMP_MULTI`. The parser-backed part is especially helpful: all exact exposed hits for both appear immediately before `JUMP_MULTI` branches in `EBATTLE5`, `EBATTLE8`, and `ESYSTEM`. The local script slices make that concrete. In `EBATTLE8`, `LOAD_SPECIAL 0x02` is followed by a three-way `JUMP_MULTI` that selects among action-user text variants including a visible `cohorts` branch. In `ESYSTEM`, `LOAD_SPECIAL 0x01` and `LOAD_SPECIAL_FOR_JUMP_MULTI 0x01` sit directly in front of `JUMP_MULTI count=3` pronoun branches for `he / she / it` and `He / She / It`.

The local bank-`01` side matches that broad shape. `0x1C 14 -> C1:516B` and `0x1C 15 -> C1:51FC` both compute a small `1..3`-style selector from current battle state, selected battler rows, and enemy-data byte `+0x1A`, then stage that selector through `C1:045D` for later text use. So the safest current read is that these two are special jump-selector loaders for later multi-way text branching, not ordinary printers. I am still keeping their exact semantic difference slightly cautious, but the script-side and code-side stories now agree: both are load-before-branch helpers.

`0x1C 11` is still the one awkward late case. The family summary now shows only five exact parsed hits, four in `EBATTLE7` and one in `ESYSTEM`, all with argument `0x00`. Locally, `0x1C 11 -> C1:40CF` either takes explicit `X` or falls back to live `+0x1B`, then calls `EF:01D2` and returns. Since `EF:01D2` itself computes a small context-sensitive selector and touches later text-control state, the safest current wording is that `0x1C 11` is another narrow special-selector loader in the same general neighborhood as `0x1C 14/15`, but it still does not have a clean player-visible name yet.

A quick pass over the immediate neighbors also helps narrow the family's shape. Case `0x1C 06 -> C1:46DE` is no longer just "some table-backed label printer." It resolves either `X` or live `+0x1B`, maps that value through `C08FF7` with selector `#$001F`, lands in a `D5:7880`-rooted table, and prints a fixed `#$0019`-byte fragment through `C447FB`. A direct text dump of the first live records at `D5:789F+` gives `Onett`, `Twoson`, `Threed`, `Saturn Valley`, `Fourside`, `Winters`, and `Summers`, so `0x1C 06` is now a good local fit for a town-name printer rather than another item-specific helper. One useful caution from the exact-command search: there are currently zero parsed `1C 06` hits in the exposed `text_data` segments, so this name is table-backed and reference-backed more than script-backed right now.

Case `0x1C 07 -> C1:45CA` is still narrower, but it also got cleaner. It resolves either `X` or live `+0x1B`, then forwards that value into `C1:180D` with `Y=0` and `X=1`. `C1:180D` is now best read as `LayoutActiveTextEntriesAndRefresh`: it calls `C4:51FA` / `LayoutActiveTextEntryChainForWindow`, then refreshes display state through `C1:163C`. One confirmed local caller is the battle PSI menu path in `ebsrc`'s `battle_psi_menu.asm`, where `UNKNOWN_C1180D` is called during the menu setup flow before the menu items are printed. The parser-backed cross-check now helps too: the exact-command search finds 191 current `1C 07` hits spread across ordinary event, shop, and system segments. So `0x1C 07` no longer looks like a second Jeff-specific text trick. It now looks like the runtime leaf behind a broadly reused horizontal text-entry layout/display helper.

Case `0x1C 08 -> C1:43B8` also sharpened a bit. It is still just a tiny wrapper over `C1:0EE3`, but the command-aware search makes the usage split very clean: there are only four exact parsed hits, all in `EBATTLE4` and `EBATTLE8`. So even without fully naming `C1:0EE3` yet, the practical read is much better than before: `0x1C 08` is a battle-only special-graphics print branch, not just an anonymous neighbor.

The exact-command pass also helped clean up the awkward edge cases. `0x1C 09 -> C1:40EF` is now pinned as `SET_ACTIVE_WINDOW_TEXT_MODE`. There are currently zero exact parsed hits in the exposed `text_data` segments, but the runtime body is real: it forwards the command argument to `C1:0EB4`, which writes active window text mode byte `$8662`. By contrast, `0x1C 00 -> C1:40F9` and `0x1C 0B -> C1:5573` currently have zero exact parsed hits in the exposed `text_data` segments.

The deeper code-side pass is still useful here, though, because it shows these are not dead parser stubs. `C1:40EF -> C1:0EB4` stores the command's low byte into live context field `8662`, while `C1:40F9 -> C1:0FEA` maps the command argument through `C09032` with `Y = #$0400` and stores the result into live context field `8663`. Bank `02` later copies `8662`, `8663`, and neighboring `8665` into a working record at `C2:0A68+`, so both branches are feeding real per-context state even if only one currently shows up in exposed scripts. That means the safest current wording is:

- `0x1C 00` still keeps the reference macro name `TEXT_COLOUR_EFFECTS`, but now with local support as a real live-context setter even though no exposed `text_data` script currently uses it.
- `0x1C 09` is `SET_ACTIVE_WINDOW_TEXT_MODE`, a runtime-only live-context setter that writes `$8662`.
- `0x1C 0B` still keeps the reference macro name `PRINT_MONEY_AMOUNT`, but only as a cautious code-side label until a live local script use or stronger consumer-side proof turns up.

Even with that remaining caution on the deepest helper names, the local structure now says the same thing consistently: `0x1C` is a broad print/data-display family, and Jeff's item-name branch is one well-behaved member inside it.

## Local `1C 05` dispatcher

The local command dispatcher confirms that `0x1C` is the `PRINT_ITEM_NAME` family.

At the top level, bank `01` compares `#$001C` and jumps to `C1:7AD9`. The important part is that `C1:7AD9` itself is tiny; the real subselector logic lives in the shared tail at `C1:7B56+`.

That shared tail uses `X` as the item-name source selector. The currently pinned branches are:

- selector `0` -> `C1:463B`
- selector `1` -> `C1:467D`
- selector `4` -> `C1:196A` with `A = 0`
- selector `5` -> fixed low word `C1:549E`
- selector `6` -> fixed low word `C1:4EB5`
- selector `7` -> `C1:9A43`
- selector `8` -> `C1:196A` with `A = 0`
- selector `9` -> `C1:196A` with `A = 1`
- selector `0x0A` -> `C1:AC00`
- selector `0x0B` -> `C1:AAFA`

So Jeff repair's `[1C 05 00]` is now pinned to the selector-`0` branch, which resolves to `C1:463B`.

## The matched `0` / `1` helper pair

`C1:463B` and `C1:467D` are a matched pair.

Locally they both:

- gate on `$97CA < 0x10`
- push a one-byte value into the deferred byte queue at `$97BA + $97CA`
- increment `$97CA`
- then call `C1:244C` with `A = #$97BA` and `Y = 0` or `Y = 1`
- stage the resulting word through the common `C1:045D` helper

The only meaningful difference between the two is the final `Y` value:

- `C1:463B` uses `Y = 0`
- `C1:467D` uses `Y = 1`

That makes them look strongly like two sibling item-name sources over the same queued-byte family, not unrelated generic routines.

One new local detail makes `C1:244C` easier to read than before: these helpers also pass in an implicit queue position through `X`. They begin by doing `TXA`, pushing that one-byte value into `$97BA[$97CA]`, then incrementing `$97CA`. But they do not restore the original `X` before `JSR C1244C`; at that point `X` still holds the queue index that was just used for the write. `C1:244C` immediately saves that incoming `X` to `$26` and branches on `$26 == 1`.

That changes the cleanest interpretation of the branch. The byte being queued here is the item-name selector itself, not a Jeff-only payload byte. So `$26 == 1` is best read as "this is the second `PRINT_ITEM_NAME` occurrence in the current text run" rather than "second staged callback byte". In the Jeff repair script, that lines up unusually well with the second `[1C 05 00]` after `{swap}`.

So the strongest current caller-side picture is:

- the original `X` value becomes the queued one-byte item-name selector in `$97BA`
- `Y = 0/1` selects which sibling source slot is being built
- the inherited `X = queue index` tells `C1:244C` whether it is shaping the first or second selector-`0` print in the current message

## Stronger slot-layout picture

The bank-`01` helper cluster is now much less abstract than when this note started.

A neighboring script-side cross-check makes this slot picture more believable. `ebsrc`'s text macros name `1B 04` as `SWAP_WORKING_AND_ARG_MEMORY`, `1B 05` as `COPY_ACTIVE_MEMORY_TO_WORKING_MEMORY`, and `1B 06` as `COPY_WORKING_MEMORY_TO_ACTIVE_MEMORY`. Locally, the helper pair at `C1:0327` and `C1:0381` matches that pattern very well: `C1:0327` copies `+0x17/+0x1B/+0x1F` into `+0x21/+0x25/+0x29`, while `C1:0381` copies the saved `+0x21/+0x25/+0x29` values back into `+0x17/+0x1B/+0x1F`. I am still treating the exact one-to-one command mapping as a strong inference rather than a proved local dispatch, but it is the cleanest current explanation of why Jeff repair can print the same selector twice with `{swap}` in between and get two different item names.

The current local slot picture is:

- `C1:045D` writes the local `$1C/$1E` pair to `current_context + 0x17`
- `C1:0489` writes the local `$1C/$1E` pair to `current_context + 0x1B`
- `C1:03DC` is the paired reader for `current_context + 0x1B`
- the neighboring helper at `C1:040A` reads `current_context + 0x17`
- `C1:0400` returns `current_context + 0x1F`, and `C1:0443` writes that same `+0x1F` byte

The `1C` shared tail also lets us promote a few earlier guesses into firmer local statements. `C1:0324` is now clearly a backup helper: it copies `+0x17 -> +0x21`, `+0x1B -> +0x25`, and `+0x1F -> +0x29`. `C1:0380` is the matching restore helper: it copies `+0x21 -> +0x17`, `+0x25 -> +0x1B`, and `+0x29 -> +0x1F`. That means the context does not just have a live pair of pointer slots; it also has a saved shadow pair plus a saved companion mode byte.

So the safest current read is that `+0x17` and `+0x1B` are the live paired pointer slots inside the current text context, `+0x1F` is their live companion selector or mode byte, and `+0x21/+0x25/+0x29` are the saved shadow copies that later copy/swap-style helpers can restore. That matches the Jeff-repair behavior well: the success branch appears to install a paired before/after item-name context, and the script later flips between the two with `{swap}` rather than changing the visible `PRINT_ITEM_NAME` selector.

## Why Jeff repair uses `{swap}` with the same selector

The Jeff-repair script does not use `PRINT_ITEM_NAME 0x01` for the second item name. It uses `PRINT_ITEM_NAME 0x00`, then `{swap}`, then `PRINT_ITEM_NAME 0x00` again.

That is useful local evidence by itself.

`ebsrc` defines:

- `1B 04` = `EBTEXT_SWAP_WORKING_AND_ARG_MEMORY`
- `1B 05` = `EBTEXT_COPY_ACTIVE_MEMORY_TO_WORKING_MEMORY`

The Jeff-repair script sequence is:

- run `1F D0` to attempt repair
- `1B 05` copy active memory to working memory
- print `PRINT_ITEM_NAME 0x00`
- later do `{swap}`
- print `PRINT_ITEM_NAME 0x00` again

So the safest current interpretation is:

- selector `0` is the ordinary Jeff-repair item-name slot used by the current working/arg-memory context
- the script gets the second visible item name by swapping working and arg memory, not by changing the `PRINT_ITEM_NAME` selector

That is already enough to explain the user-visible behavior of the repair message locally, even though the exact `C1:244C` slot semantics are still being tightened.

## Stronger success-path bridge

The local `1F D0` success path now supports the text-side model more directly than before.

After `C1:63A7` calls the repair core at `C3:F1EC` and gets a nonzero item id back, it immediately runs that id through `C1:D038`. The `C3:F1EC` body now proves the returned id is the original broken item: on success it has already written the repaired item id into the matched Jeff inventory slot, then returns the saved broken item id. `C1:D038` is only directly referenced from this Jeff-repair path, and its bytes read item byte `+0x21` from the same `D5:5000` table, so it is best read as the broken-item -> repaired-item mapper used for text staging.

Right after that, the success path stages two text-side values in sequence:

- one through `C1:045D`
- one through `C1:0489`

That matters because `C1:045D` and `C1:0489` are the same paired text-state helpers we have already seen elsewhere when two related print contexts need to be installed side by side. So the safest current read is no longer just ?Jeff repair later prints two names somehow.? It is now:

- `1F D0` resolves a successful broken-item result through `C3:F1EC`
- `C1:D038` then maps that broken item id to the repaired item id
- the success branch stages both values through the paired text-state helpers `C1:045D` and `C1:0489`
- the script prints selector `0`, swaps working and arg memory, then prints selector `0` again

That is still slightly short of a byte-for-byte proof of which helper call is the active-side install and which is the arg-side install, but the order now fits the script unusually well: if `C1:0489` installs the ordinary active-side value and `C1:045D` installs the swapped partner, the Jeff script naturally prints the broken item first and the repaired item after `{swap}`.

## Helpful cross-check

The rarity of `PRINT_ITEM_NAME 0x01` helps here.

A fresh text scan found only three current `1C 05 01` uses, while `1C 05 00` appears all over the game. That makes Jeff repair's choice much more meaningful: it is not ignoring an equally common alternate selector. It is deliberately using the common selector-`0` path with a memory-context swap.

## What is solid vs. still open

Solid now:

- Jeff repair's visible item placeholder is the local `0x1C 05` item-name family
- `[1C 05 00]` resolves to selector `0`
- selector `0` maps to `C1:463B`
- selector `1` maps to the sibling helper `C1:467D`
- `{swap}` is the script-side mechanism that changes the second printed item name while leaving the selector at `0`
- `current_context + 0x17` and `current_context + 0x1B` now look like the paired text-context slots behind that swap

Still open:

- the exact semantic names of the `Y = 0` and `Y = 1` slots inside `C1:244C`
- the exact meaning of the `X == 1` second-entry special case inside `C1:244C`
- whether `current_context + 0x17` is the active-side item slot and `current_context + 0x1B` is the arg-side item slot, or vice versa
- the precise point where the `1F D0` callback family seeds the before-fix and after-fix item ids into the text-engine memory blocks that `{swap}` exchanges
- which of the paired `C1:045D` and `C1:0489` installs becomes the pre-swap slot and which becomes the post-swap slot

## Best current interpretation

The safest current local read is that Jeff repair now has a real end-to-end bridge: `1F D0` resolves a successful broken-item result, the success path maps that through `C1:D038` to the repaired item id, stages both values through paired text-state helpers, and then the repair text uses the common `PRINT_ITEM_NAME 0x00` helper twice, with `SWAP_WORKING_AND_ARG_MEMORY` in between, to print the broken item first and the repaired item second. The newer `C1:244C` caller-side reading also suggests that the text engine is explicitly building that pair as a two-entry staged item context rather than implicitly deriving the second name later.
