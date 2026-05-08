# Timed Delivery System Flags `754` / `779`

This note records the best current read for the shared system-side flags and scripts that sit next to the timed-delivery rows.

See also [timed-delivery-warning-text-gates.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-warning-text-gates.md).
See also [timed-delivery-state-helpers-ef0f60-fdb-ff6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-state-helpers-ef0f60-fdb-ff6.md).
See also [timed-delivery-row-index-command-1f-d3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-row-index-command-1f-d3.md).

## Main result

The script-side support flags used by the delivery family now have useful reference-backed names:

- `flag 754` = `FLG_SYS_DISTLPT`
- `flag 779` = `FLG_SYS_DISTLPT_EVENT`

The important correction is that these do **not** look delivery-exclusive.

The delivery scripts use them heavily, but unrelated script families do too. So the safest current reading is broader:

- `754` looks like a shared system-level teleport or escape restriction flag
- `779` looks like a smaller companion event-state flag in that same broader restriction family

## Why `754` still matters for timed delivery

Across the delivery-family scripts, the same pattern repeats:

- set one row-specific pending flag such as `0x00B4`, `0x00B5`, `0x01BE`, `0x0285`, `0x0286`, `0x0287`, `0x0288`, `0x02A3`, `0x02B6`, or `0x02B7`
- also set `flag 754`
- later unset the row-specific flag and unset `754` when the delivery sequence completes or is cancelled

That matches the user-facing warning scripts well:

- teleport warning text checks the row-specific pending flags directly
- Exit Mouse warning text checks the same row-specific pending flags directly
- many cleanup tails also explicitly unset `754`

So the delivery subsystem clearly participates in the `754` system, even if it does not own it exclusively.

## Why `754` now looks broader than delivery

A broader script scan found several non-delivery families also setting `754`, often alongside `779`.

Examples include:

- delivery/customer scripts in `data_17`, `data_18`, `data_31`, and `data_55`
- multiple unrelated system or cutscene flows in `data_25` and `data_52`

That wider reuse fits the reference name `FLG_SYS_DISTLPT` much better than a narrow "delivery active" label. The cleanest current inference is that `DISTLPT` is shorthand for a system-level teleport disable or escape restriction state.

## `EVENT_754`

The dedicated script [754.asm](/F:/Earthbound%20Decomp%20-%20Codex/refs/ebsrc-main/ebsrc-main/src/data/events/scripts/754.asm) is also revealing.

It is not a text script. It is a small movement/staging controller that:

- places an entity at `X=$0180`, `Y=$1E58`
- runs a movement helper through `C0:A685`
- starts a task
- halts after yielding to text

So `EVENT_754` looks like a live script-side controller attached to this broader restriction system, not merely a raw boolean marker.

## `EVENT_779`

The companion script [779.asm](/F:/Earthbound%20Decomp%20-%20Codex/refs/ebsrc-main/ebsrc-main/src/data/events/scripts/779.asm) is much smaller:

- sets a physics callback
- zeroes velocity
- faces left
- halts

That makes `779` look like a lighter companion event-state hook rather than the main restriction flag.

## Neighboring system flag

The same reference block also names:

- `flag 778` = `FLG_SYS_DIS_MOUSE`

That is useful because the Exit Mouse refusal scripts live right beside the timed-delivery warning family. I am not claiming a full local mapping yet, but the neighborhood fit is strong: timed delivery, teleport refusal, and Exit Mouse refusal all seem to live in one broader restriction cluster.

## Best current practical interpretation

The current best layered model is:

- row-specific `D5:F645` flags choose which delivery or customer case is active
- `754` is a broader script-visible teleport or escape restriction flag that timed delivery reuses
- `779` is a smaller companion event-state flag in that same restriction family
- these script-visible flags fit well with the broader engine-side latch behavior we have been modeling around `$5D98`

That is not a full proof that `$5D98 == flag 754`, and I am not claiming that. But it is now a stronger, healthier statement than the older "754 is the delivery system flag" wording.
