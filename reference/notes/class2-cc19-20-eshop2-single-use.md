# Class2 CC19 20 ESHOP2 Single Use

This note captures the current best local model for text control code `0x19 0x20` after the broader `0x19 0x1F` reuse scan and the follow-up bank-`00` mushroomized-walking work.

See also [class2-cc19-1f-cross-segment-reuse.md](notes/class2-cc19-1f-cross-segment-reuse.md).
See also [class2-c1-display-text-substitution-handler-7af3.md](notes/class2-c1-display-text-substitution-handler-7af3.md).
See also [mushroomized-walking-remap-family.md](notes/mushroomized-walking-remap-family.md).

## Main result

`0x19 0x20` still does not look like a broad sibling of `0x19 0x1F`.

A scan of `US/text_data` segments still finds exactly one local hit:

- `C9:1A91` in `ESHOP2`

That is a very different profile from `0x19 0x1F`, which appears broadly across battle and goods text.

## Local handler body

The local body behind this selector is pinned.

`0x19 0x20` dispatches to `C1:7B0D`, whose bytes decode as:

- `SEP #$20`
- `LDA $98A4`
- `STA $06`
- `STZ $07`
- `STZ $08`
- `STZ $09`
- `REP #$20`
- `LDA $06`
- `STA $0E`
- `LDA $08`
- `STA $10`
- `JSR C1:045D`
- `BRA C1:7B51`

So mechanically it is the same tiny source-loader pattern as `C1:7AF3`, except that it reads its byte from `$98A4` instead of `$9D11`.

That means the unresolved part is not the loader shape. The unresolved part is the source meaning of `$98A4`.

## Local script context is clearer now

The lone local hit decodes as the opening of the `ESHOP2` hospital / mushroom-girl region:

- `C9:1A91  0x19 0x20`
- `C9:1A93  STORE_TO_ARGMEM 0x01`
- `C9:1A95  COPY_TO_ARGMEM 0x01`
- followed by a loop over party-member checks
- including `GET_CHARACTER_NUMBER 0x00`
- and `CHARACTER_HAS_AILMENT 0x00, 0x02, 0x02`

The surrounding script is the `earthbound.yml` region beginning at:

- `ESHOP2 + 0x00F9` -> `MSG_SUB_GRFD_KINOKOGIRL`

So the safest local read is still that this helper exposes one small preloaded byte to the mushroom-girl clinic flow before the script scans party members for the mushroomized ailment.

## What the writer side adds now

The writer side is stronger than it was in the earlier pass.

Bank `00` now shows that `$98A4` belongs inside a larger mushroomized-walking controller family rather than a stray global flag.

The important local points are:

- `C0:32F0..3318` scans the six-entry source family at `$986F` and stores the resulting stop index into `$98A4`
- `C0:369B` / `C0:34D6` / `C0:3A24` reveal that the surrounding family is a six-entry active controller, not a single remap byte
- `$98A3` is now much more clearly the active-entry count
- `$988B`, `$9891`, `$9897`, and `$9A0B` are coordinated per-entry state in that same family

So `$98A4` now fits better as the selected or boundary index inside that controller than as a generic mushroomized state bit.

## Why not give `$98A4` a single global name yet

A quick local opcode scan still shows other uses of `$98A4` outside the narrow clinic path.

- `C1:7B0D` reads it for the `0x19 0x20` text handler
- there are other `LDA $98A4` readers in banks `C1` and `C2`
- there are a few direct `STA $98A4` writers in `C0` and `C2`
- there are several clear paths that zero it together with nearby controller state

So `$98A4` is a real shared WRAM byte, not a text-only scratch value.

That means the safest wording is still context-sensitive:

- the exposed script use at `0x19 0x20` is in the mushroom-girl clinic flow
- the strongest writer evidence places it in the mushroomized-walking controller family
- but the raw WRAM address may still have reuse outside that narrow script path

## Current safest interpretation

The safest interpretation is:

- `0x19 0x20` is still a narrow single-script helper in `ESHOP2`
- the helper body at `C1:7B0D` simply loads the current byte from `$98A4` into the display-text working pipeline
- the only observed text use is the `MSG_SUB_GRFD_KINOKOGIRL` mushroom-girl clinic script
- and the strongest local writer evidence ties `$98A4` to the selected or boundary index in the overworld mushroomized-walking controller family

So the best current read is that `0x19 0x20` exposes a mushroomized-walking controller index to the clinic script, not a broad generic substitution source.

## Best next target

The best next move is to tighten one more downstream consumer of `$9897`, `$9A0B`, `$0B16`, and `$0B52`, because that should decide whether the controller payload trio is best named in overlay terms or with a slightly different local vocabulary.
