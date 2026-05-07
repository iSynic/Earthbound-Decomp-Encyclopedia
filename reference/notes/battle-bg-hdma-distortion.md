# Battle Background HDMA Distortion

EarthBound's trippy battle backgrounds are data-driven HDMA effects.

Important data:

- `refs/ebsrc-main/ebsrc-main/src/data/battle/backgrounds/config_table.asm`
  - each `bg_layer_config_entry` includes four scrolling movement IDs and four
    distortion style IDs
- `refs/ebsrc-main/ebsrc-main/src/data/battle/backgrounds/distortion_table.asm`
  - `BG_DISTORTION_TABLE`
  - rows are `distortion_entry` structs
- `refs/ebsrc-main/ebsrc-main/include/structs.asm`
  - `distortion_entry`
  - `loaded_bg_data`

`distortion_entry` fields:

```asm
duration
style
ripple_frequency
ripple_amplitude
speed
compression_rate
ripple_frequency_acceleration
ripple_amplitude_acceleration
speed_acceleration
compression_acceleration
```

Known style enum:

```asm
DISTORTION_STYLE::NONE                 = 0
DISTORTION_STYLE::HORIZONTAL_SMOOTH    = 1
DISTORTION_STYLE::HORIZONTAL_INTERLACED = 2
DISTORTION_STYLE::VERTICAL_SMOOTH      = 3
DISTORTION_STYLE::UNKNOWN              = 4
```

Runtime path:

1. `LOAD_BATTLEBG` reads the config row from `BG_DATA_TABLE` and copies the
   distortion style IDs into `LOADED_BG_DATA_LAYER1` / `LOADED_BG_DATA_LAYER2`.
2. `GENERATE_BATTLEBG_FRAME` (`C2:C92D`) advances palette cycling, scrolling,
   and distortion state for one loaded background layer.
3. When the current distortion segment expires, it loads a new row from
   `BG_DISTORTION_TABLE` at `CA:F708` into the `loaded_bg_data` distortion
   fields.
4. It installs the correct HDMA target lane with `DO_BATTLEBG_DMA`
   (`C0:ADB2`).
5. Per frame, it advances frequency/amplitude/speed/compression by their
   acceleration fields, projects the current phase, and calls the C0 helper at
   `C0:AE5A` to write per-scanline offset values into the active HDMA buffer.

HDMA RAM layout:

```asm
ANIMATED_BACKGROUND_LAYER_1_HDMA_TABLE  ; $7E3C32, 7 bytes
ANIMATED_BACKGROUND_LAYER_2_HDMA_TABLE  ; $7E3C3C, 7 bytes
ANIMATED_BACKGROUND_LAYER_1_HDMA_BUFFER ; $7E3C46, 448 bytes
ANIMATED_BACKGROUND_LAYER_2_HDMA_BUFFER ; $7E3E06, 448 bytes
```

`DO_BATTLEBG_DMA` programs SNES HDMA channels using `DMAP = $42`:

- bit 6 set: indirect HDMA
- transfer mode 2: write two bytes to one PPU register
- `BBAD` chosen from `DMA_TARGET_REGISTERS`

The target register table starts:

```asm
db $80,$0D,$0F,$11,$13,$0E,$10,$12,$14
```

Those correspond to the low-byte PPU register numbers for the BG scroll
registers:

- `$210D` BG1HOFS
- `$210F` BG2HOFS
- `$2111` BG3HOFS
- `$2113` BG4HOFS
- `$210E` BG1VOFS
- `$2110` BG2VOFS
- `$2112` BG3VOFS
- `$2114` BG4VOFS

The NMI path disables HDMA at entry (`stz $420C`) while updating PPU state, then
re-enables it from the mirror byte `$1F` near the end of the scroll/register
commit. This is why the effect can be rebuilt safely every frame.

Plain-English model:

The bitmap/tilemap itself is not being redrawn into trippy shapes. The game
draws a normal tiled battle background, then HDMA rewrites that background
layer's horizontal or vertical scroll register on each scanline. The distortion
table controls the wave shape over time: frequency, amplitude, speed,
compression, and accelerations. Smooth/interlaced/vertical styles change how
those per-line offsets are emitted into the HDMA buffer.
