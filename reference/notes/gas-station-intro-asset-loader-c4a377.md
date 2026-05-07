# Gas Station Intro Asset Loader (`C4:A377`)

This note documents the previously unmentioned bank-`C4` code chunk called from the gas-station intro load path.

See also [intro-logo-wait-and-gas-station-helpers-c0efe1-c0f21e.md](notes/intro-logo-wait-and-gas-station-helpers-c0efe1-c0f21e.md).
See also [landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md](notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md).

## Working Names

- `C4:A377` = `LoadGasStationIntroGraphicsAndTilemap`

## Main result

`C4:A377` is a C4-side graphics/tilemap loader used by the intro gas-station screen setup.

The strongest anchor is its only direct caller: `C0:F16C`, inside the reference-named `intro/gas_station_load.asm` block. The caller has just decompressed intro assets and queued VRAM transfers, then calls `C4:A377`, mirrors the CGRAM shadow through `C4:96F9`, and initializes palette interpolation through `C4:96E7`.

So the safest current name is `LoadGasStationIntroGraphicsAndTilemap`.

## Local behavior

The routine starts by clearing/preparing display memory:

- calls `C0:8D79(3)`
- clears `$7E:0000..77FF` through `C0:8D9E`
- clears/fills the `$7C00` region through `C0:8DDE`

It then uses `CA:F038` as a compact byte script. For the first byte, it indexes the legacy `DATA_CAD7A1` GFX pointer table, decompresses the selected asset through `C4:1A9E` into `$7F:0000`, and queues `$2000` bytes to VRAM destination `$6000` through `C0:8616`.

It then uses the same script byte to index the legacy `DATA_CAD93D` tilemap pointer table, decompresses that tilemap through `C4:1A9E`, applies a simple attribute-bit rewrite across `$7F:0000..$7F:07FF`, and queues `$0800` bytes to VRAM destination `$7C00`.

The legacy reference labels are useful corroboration here:

- `DATA_CAD7A1`: GFX file pointer table
- `DATA_CAD93D`: tilemap file pointer table
- `DATA_CAF038`: the compact selector/script bytes consumed by this loader

## Tail setup

After the main GFX/tilemap loads, the routine continues through more `CA:` pointer-table selections and copies `$20`-byte chunks into local staging buffers via `C0:8ED2`. It then writes `$ADD4 = 2`, calls `C2:C92D`, clears `$AE4B`, restores direct page, and returns.

That tail is still softer than the main asset-load contract. It is very likely part of the same screen setup, but the exact meaning of `$ADD4/$AE4B` in this intro context should stay open until the surrounding C2/C4 presentation state is named more tightly.

Source polish: `src/c4/gas_station_intro_visual_loader.asm` now names the
display mode and clear selector, pointer-table bank-field offset, upload
selector, tilemap attribute high-byte offset and bit rewrite, battle-visual
tile-state word, `$ADE0/$AE00` chunk destinations, `$20` chunk size, script
start value, and zero/byte-mask sentinels used by the loader tail.

2026-05-06 source polish follow-up: the source now documents the loader phases
at the call sites rather than only naming the constants. C4 owns the CA:F038
selector byte, the CA:D7A1/CA:D93D graphics and tilemap pointer-table walks,
the `$7F:0000` decompression staging buffer, the `$6000/$7C00` VRAM queue
arguments, and the high-byte tilemap rewrite (`clear $20`, set `$08`). The tail
is still intentionally bounded: C4 seeds `$ADD4`, `$AE20`, `$AE4B`, and the
`$ADE0/$AE00` chunks, while C2 owns the decompressed battle-visual asset format
and script runner behavior.

## Why this is not the battle overlay interpreter

The include order places `C4:A377` near Giygas/static-transition and battle overlay data, and the next documented code family at `C4:A67E..A7B0` is the battle overlay script interpreter.

But `C4:A377` itself is reached from `intro/gas_station_load.asm`, uses GFX/tilemap pointer tables, writes VRAM ranges `$6000` and `$7C00`, and is followed by the gas-station palette setup in C0. Locally, it is therefore an intro screen asset loader rather than a battle overlay state machine.

## Practical conclusion

`C4:A377` can come off the unmentioned frontier as a gas-station intro graphics/tilemap loader.

The next useful data pass around this region should classify `C4:A591` and the neighboring `C4:A5CE/A5FA/A626/A652` records together, because those are data payloads adjacent to this loader and the already-named battle overlay script state.
