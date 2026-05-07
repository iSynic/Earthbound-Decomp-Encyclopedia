# Overworld Visible Entity Refresh Slice (`C0:7B52..7C5A`)

This note captures the strongest current render-side candidate for the remaining overworld judder now that the camera path itself looks healthy.

See also [overworld-timing-scroll-commit-slice-c08b20-c08284.md](notes/overworld-timing-scroll-commit-slice-c08b20-c08284.md).
See also [overworld-companion-family-priority-a794.md](notes/overworld-companion-family-priority-a794.md).

## Working Names

- `C0:7B52` = `Refresh_VisibleEntityScreenPositions`
- `C0:A780` = `RefreshCompanionVisualProfileForEntry`
- `C0:A794` = `RefreshCompanionVisualProfile_PhaseBiased`

## Main result

`C0:7B52..7C5A` is the strongest current fit for the ordinary per-entry visible entity refresh loop that runs after camera motion has already been resolved.

Locally, it:

1. iterates over a small entry range beginning at selector value `0x18`
2. resolves each active entry into a slot record rooted at `99CE + offset`
3. refreshes world-position-like fields into working tables at `0B8E/0BCA` and variant state at `2AF6`
4. computes screen-space positions by subtracting the smooth camera shadow words `$31/$33`
5. stores those screen-relative values into `0B16/0B52`
6. calls `C0:A780`, which is inside the companion visual descriptor family that later feeds `A794`

So this routine is one of the strongest current seams where a perfectly smooth camera can still produce visible judder if entry screen positions or companion visuals update on a different cadence.

## Locally proved

### `7B52` is live and has ordinary movement-side callers

Local xrefs include:

- `C0:4008  JSL $C07B52`
- `C0:51F4  JSL $C07B52`
- `C0:B768  JSL $C07B52`

So `7B52` is not an isolated setup helper. It is used from normal bank-`C0` runtime paths.

### The loop walks a bounded entry set

The routine initializes:

- `$14 = $9A0B`
- `$12 = #$0018`

and loops until `$12 >= #$001E`.

So the strongest current local read is that it refreshes a small fixed set of high-priority visible entries rather than the whole slot universe.

### It resolves per-entry slot records rooted at `$99CE`

At `7B8D..7B9B`:

- `LDA $0E9A,X`
- `JSL $C08FF7`
- `ADC #$99CE`
- `TAX`

This converts the current entry selector into a slot-record base in the same `$99CE + stride` family we have already been using in the overworld notes.

### It refreshes world-position-like fields before screen-space fields

Two paths converge at `7C2D`:

- a fast path that copies current canonical values from `$9877/$987B/$987F` into per-entry tables
- an alternate path that loads entry-specific data from a descriptor table rooted near `$5156`

In both cases, by `7C2D` the routine has populated:

- `0B8E,X`
- `0BCA,X`
- `2AF6,X`

The healthiest current read is that these are world-position and variant/state tables used for the visible entry refresh.

### Screen-space coordinates are derived from smooth camera shadows `$31/$33`

The key screen-space math is:

- `C0:7C31  LDA $0B8E,X`
- `C0:7C35  SBC $0031`
- `C0:7C38  STA $0B16,X`
- `C0:7C3B  LDA $0BCA,X`
- `C0:7C3F  SBC $0033`
- `C0:7C42  STA $0B52,X`

So the visible entry positions are derived by subtracting the already-smooth camera shadows from per-entry world positions.

That makes this one of the strongest current places where a visible layer can appear uneven even while the camera itself updates smoothly.

### `7C45` flows directly into the companion visual descriptor family

Immediately after the screen-space subtracts:

- `C0:7C45  LDA $12`
- `C0:7C47  JSL $C0A780`

`A780` sits in the same family as `A794`, which we already know is active in busy diagonal-render frames.

So `7B52` is not merely calculating positions. It hands each refreshed entry into the same companion visual lane that later emits descriptor traffic.

## Decomp-backed and locally consistent

### Why this slice now matters more than the camera-publish path

Recent emulator work showed:

- movement inputs feeding `4010` look orderly
- `1558` writes `$31/$33` smoothly
- `8B51/8B57` publish smoothly
- `8284` commits normally

That weakens the idea that the remaining judder is a camera-state timing problem.

`7B52..7C5A` is a better next suspect because it sits after the smooth camera path and directly computes what visible entries should do relative to that camera.

### Why this also fits the earlier `A794` evidence

Busy-frame call-stack samples around `C08643` already showed live activity from:

- `A56E`
- `A794`
- especially paths through `A750` and `A81A`

This new note makes that less abstract: `7B52` computes per-entry visible positions from `$31/$33`, then immediately feeds `A780`, which lives in that same companion descriptor lane.

So the healthier current model is:

- camera motion itself is smooth
- visible entity refresh and companion descriptor emission happen downstream
- the remaining judder may be what the eye sees when those entry visuals lag or quantize relative to the smooth camera

## Still uncertain

### Exact semantic meaning of the `0B8E/0BCA/0B16/0B52` tables

Locally the roles are strong:

- `0B8E/0BCA` behave like world-space coordinates
- `0B16/0B52` behave like screen-space coordinates

But the exact symbolic names are still open.

### Whether the visible judder comes from screen-space recompute cadence or from the downstream `A780/A794` visual emission

This note proves both are adjacent. It does not yet prove which substep is the one the eye is catching.

## Best next emulator workflow

### 1. Watch the screen-space subtract layer directly

The best next breakpoints are:

- `C0:7C35`
- `C0:7C3F`

Those are the exact subtracts from smooth camera shadows into visible entry screen positions.

### 2. Compare the immediate handoff into the companion lane

Also watch:

- `C0:7C47` (`JSL $C0A780`)

If `7C35/7C3F` update steadily but the resulting visible behavior still looks uneven, the next suspect becomes `A780/A794` rather than the screen-position math itself.

## Bottom line

The best current render-side seam is no longer the camera path itself.
It is `C0:7B52..7C5A`, where a small set of visible entries are converted from world-space values into screen-space values relative to the already-smooth camera shadows, and then handed directly into the companion visual descriptor family.

That is now the healthiest place to investigate why diagonal walking still looks visually uneven on vanilla.
