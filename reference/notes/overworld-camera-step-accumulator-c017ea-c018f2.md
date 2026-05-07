# Overworld Camera Step Accumulator (`C0:17EA..18F2`)

This note isolates the routine that updates the live camera position before `C0:1558` republishes it into the scroll shadow chain.

See also [overworld-timing-scroll-commit-slice-c08b20-c08284.md](notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md).
See also [rom-patch-overworld-stutter-plan.md](notes/rom-patch-overworld-stutter-plan.md).

## Main result

`C0:17EA..18F2` is now the strongest current fit for the ordinary camera-step accumulator that runs ahead of `C0:1558`.

## Working Names

- `C0:17EA` = `AccumulateOverworldCameraStep`

Locally, it:

1. reads movement or direction flags from `$0065`
2. derives signed X and Y step deltas into DP locals `$10` and `Y`
3. scales those deltas by several movement-speed bits
4. adds the resulting deltas into live camera position words `$4380/$4382`
5. compares the new position against the last published copy in `$437C/$437E`
6. calls `C0:1558` only when the camera position actually changed
7. then copies `$4380/$4382` back into `$437C/$437E`

That means `1558` is not the origin of camera motion. It is the incremental refresh controller that reacts after `17EA..18F2` has already advanced the camera position.

## Locally proved

### Entry and exit shape

The local decode around `C0:17EA` shows a self-contained RTL routine:

- `C0:17EA` starts with `REP #$31`, `PHD`, DP relocation
- `C0:18F1` restores DP
- `C0:18F2` returns with `RTL`

So `17EA..18F2` is one camera-step worker, not just a branch tail inside `1558`.

### `$0065` drives signed step deltas

The decode shows the signed direction bits are derived from `$0065`:

- bit `0400` -> `Y = +1`
- bit `0800` -> `Y = -1`
- bit `0100` -> `$10 = +1`
- bit `0200` -> `$10 = -1`

This is the strongest current local read for the ordinary movement-direction input into the camera step.

### Additional speed bits scale both axes

After the signed unit deltas are established, several further bits in `$0065` scale both X and Y by powers of two:

- bit `0020` multiplies both by `4`
- bit `0010` multiplies both by `2`
- bit `0040` multiplies both by `2`

So the routine is not just choosing direction. It is also deriving movement magnitude from the same flag word.

### `$4380/$4382` are the live camera position words

The key update sequence is:

- `C0:187E  ADC $4380`
- `C0:1882  STX $4380`
- `C0:1887  ADC $4382`
- `C0:188C  STA $4382`

So `17EA..18F2` accumulates camera X into `$4380` and camera Y into `$4382`.

### `$437C/$437E` are the last position seen by the refresh side

Immediately after the new position is computed:

- `C0:188F  CPX $437C`
- `C0:1894  CMP $437E`
- if equal, branch to `18AD` and skip the ordinary `1558` refresh call
- if different, compute screen-relative values and `JSR $1558` at `C0:18A8`

Then at routine end:

- `C0:18E5  LDA $4380`
- `C0:18E8  STA $437C`
- `C0:18EB  LDA $4382`
- `C0:18EE  STA $437E`

So the healthiest current local read is:

- `$4380/$4382` = live camera position
- `$437C/$437E` = last camera position already handed to the refresh side

### `1558` is downstream, not upstream

Because `17EA..18F2` computes the new camera position first and only then calls `1558`, the ordinary chain is now:

1. movement flags in `$0065`
2. camera-step accumulator at `17EA..18F2`
3. incremental refresh controller `1558`
4. runtime scroll shadows `$31/$33`
5. publish through `8B51/8B57`
6. NMI commit through `8284`

This is a stronger and cleaner model than the older "`1558` itself moves the camera" wording.

### There is also a snap or align path

When the new camera position equals the previous one but `$02 & #$0080` is set, the routine takes the `18B4..18E1` branch:

- sets `$4370/$436E = FFFF`
- masks `$4380/$4382` down with `AND #$FFF8`
- calls `C08726`
- converts the aligned positions into tile coordinates
- calls `C013F6`
- calls `C08744`

So this routine contains both the ordinary incremental camera-step path and a separate aligned or snap-style refresh path.

Source polish follow-up: `src/c0/c0_17ea_accumulate_overworld_camera_step.asm`
now names the downstream helper-call surface for the ordinary and snap paths.
The source calls `C0:1558` as the incremental refresh controller, `C0:13F6` as
the load-map-at-position path, `C0:12ED` as the reload-map-at-position path,
`C0:68F4/C0:69AF` as the current-position transition/music context pair, and
`C0:3FA9` as post-transition entity placement refresh.

## Decomp-backed and locally consistent

### Why this matters for the judder question

The recent emulator work already showed:

- `1558` updates `$31/$33` smoothly
- `8B51/8B57` publish smoothly
- `8284` commits normally in NMI

This note moves the question one step earlier.

If diagonal walking still looks uneven, the next healthy hypothesis is that the visible cadence may already be present in the deltas produced here at `17EA..18F2`, not only in the later render workload.

### Connection to the movement-time refresh lane

`C0:18A8` is one of the direct callers into `1558`, and it sits inside this accumulator routine. So the newer picture is internally consistent with the earlier timing note: `18xx` advances the camera, then `1558` reacts to it.

## Still uncertain

### Exact semantic name of `$0065`

Locally it is clearly a movement or direction flag word with speed modifiers, but the exact high-level field name is still open.

### Whether diagonal judder is inherent in the produced delta pattern

This note proves where the deltas are produced, but not yet what the per-frame diagonal pattern looks like on vanilla.

That is now the most useful remaining question.

## Best next emulator workflow

### 1. Trace the actual camera deltas, not the later publish chain

The best next breakpoints are now:

- `C0:1882` for writes into `$4380`
- `C0:188C` for writes into `$4382`

During diagonal walking, compare successive values to see whether the X/Y deltas follow a repeating non-uniform cadence.

### 2. Compare diagonal against single-axis walking

For each case, note a short sequence of successive values written at `1882/188C`.

If diagonal already alternates in a non-uniform pattern while single-axis stays visually even, the current safest conclusion will be that the remaining judder is native to the camera-step algorithm itself rather than primarily a load or queue artifact.

## Bottom line

`C0:17EA..18F2` is now the strongest current fit for the true camera-step accumulator.

It decodes movement flags from `$0065`, updates live camera position in `$4380/$4382`, and only then calls `1558` when the camera position has changed.

So the next useful question is no longer "is publish late?" but rather:

- what per-frame delta pattern does this routine produce during diagonal walking?
