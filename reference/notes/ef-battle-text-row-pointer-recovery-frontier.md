# EF Battle Text Row-Pointer Recovery Frontier

This note captures the exact evidence gap behind the remaining
`D5:7B68` row-message frontier. It is scoped to EF battle-text naming and the
C1/C2 consumer contract; it does not promote D5 source or edit C1/C2.

## Current Local Evidence

The current checkout now has enough local row bytes to recover targeted row
`+4` action-message pointers directly:

- `src/d5/table_battle_action_table.asm` proves the table span
  `D5:7B68..D5:8A50`, row count `318`, and stride `0x0C`, but preserves the
  table as a data gap rather than checked-in row bytes.
- `tools/inspect_battle_action.py` can recover row metadata, row `+4` message
  pointer, row `+8` C2 behavior pointer, and a short text preview, but it needs
  a local ROM.
- This checkout has a local ROM at `EarthBound (USA).sfc`, so targeted
  inspections can now prove exact row `+4/+8` joins.
- Set `PYTHONIOENCODING=utf-8` in PowerShell before broad scans; some note-hit
  output contains characters that the default console code page cannot encode.

That means the remaining frontier is no longer all blocked. Rows recovered in
the latest EF pass should move into the concrete crosswalk, while still-unknown
rows remain framed as pointer recovery rather than EF source renaming.

## Recovery Command

Run targeted row inspections first:

```powershell
$env:PYTHONIOENCODING='utf-8'
python tools\inspect_battle_action.py 10
python tools\inspect_battle_action.py 31
python tools\inspect_battle_action.py 32
python tools\inspect_battle_action.py 35
python tools\inspect_battle_action.py 48
python tools\inspect_battle_action.py 49
python tools\inspect_battle_action.py 64
python tools\inspect_battle_action.py 65
python tools\inspect_battle_action.py 95
python tools\inspect_battle_action.py 98
python tools\inspect_battle_action.py 119
python tools\inspect_battle_action.py 134
python tools\inspect_battle_action.py 251
python tools\inspect_battle_action.py 258
```

For a focused behavior-body scan, use the code-address selector:

```powershell
$env:PYTHONIOENCODING='utf-8'
python tools\inspect_battle_action.py C2:9AC6 --limit 8
python tools\inspect_battle_action.py C2:9AD8 --limit 8
python tools\inspect_battle_action.py C2:8F21 --limit 8
python tools\inspect_battle_action.py C2:9033 --limit 24
python tools\inspect_battle_action.py C2:A821 --limit 8
```

Record each recovered row as:

- row id
- row `+0..+3` direction/target/type/cost metadata
- row `+4` message pointer and bank
- row `+8` C2 behavior pointer
- secondary result scripts emitted by the behavior body

## Inspection Output Triage

Sort each recovered row into exactly one row-message bucket before editing any
EF source label:

| Bucket | Condition | Follow-up |
| --- | --- | --- |
| Proved EF row message | Row `+4` points to `EF:*` and row `+8` is known | Add or update the concrete row table in `notes/ef-battle-text-row-message-crosswalk.md`. |
| Non-EF row message | Row `+4` points to `C7:*`, `C8:*`, or `C9:*` | Add or update the non-EF row-message lane table; do not create EF anchors. |
| Result-only EF emission | Row `+4` is unknown/non-EF, but row `+8` emits `EF:*` through `DC1C`/`DC66` | Document the EF script as a direct/amount result payload, not a row message. |
| Still behavior-only | Row `+8` behavior is known, but row `+4` is not recovered | Keep the row in this frontier. |

Use `notes/ef-battle-text-consumer-lane-contracts.md` as the lane decision
table when a recovered row looks ambiguous.

## First Rows To Recover

Rows `32..35`, `48`, `49`, `62..94`, `95..98`, `103`, `105..116`,
`119..134`, `160`, `161`, `176`, `201..206`, `208..210`, `211..236`, `238`,
`241`, `242`, `251..257`, `260..266`, `274`, and `300..307` are now recovered
and moved into the concrete row-message crosswalk.
The exact row-backed battle-action label frontier is closed. Continue with
adjacent status/result islands only when the C1/C2 consumer lane is proved.
The all-row generated navigation layer is now
`notes/battle-action-row-crosswalk.md`, which records every D5 row `+4`
message pointer and row `+8` behavior pointer without promoting source names by
itself.

| Priority | Rows | Why they matter |
| ---: | --- | --- |
| `1` | direct-result/status islands adjacent to recovered row messages | These are `DC1C`/`DC66` result consumers, not row `+4` presentation anchors; keep lane proof before renaming. |

## Recovered No-Op And Flavor Joins

The no-op/flavor pass recovered the highest-risk behavior-only family:

- rows `119..134` point at EBATTLE2 flavor text and share `C2:9033`;
- rows `251..256` point at EF status/event/result text and use tiny no-op
  tails `C2:903F..904E`;
- the neighboring no-op-tail sweep is complete: `C2:903C` is only row `9` with
  a C7 empty/default message, and `C2:903F`, `9042`, `9045`, `9048`, `904B`,
  and `904E` are exactly rows `251..256`;
- row `257` and rows `260..266` point at EBATTLE4 event/flavor text and share
  `C2:9033`;
- rows `186..188`, `0..3`, `9`, and `258` prove non-EF row-message lanes
  through C7/C9, so they belong in the crosswalk but should not rename EF
  anchors.
- the complete `C2:9039` pass splits cleanly by row `+4` bank: EF default rows
  `60/61`, item-use rows `259`, `270`, and `271`, flee row `279`, and EBATTLE3
  flavor rows `309` and `313..317` now have proved joins, while rows
  `190..200`, `272/276`, `281/282`, `284..289`, `308`, and `312` stay in
  non-EF C7/C9/C6 presentation lanes.
- the EBATTLE2 exact `MSG_BTL_*` action rows `103`, `105..116`, `201..206`,
  `208..210`, and reuse row `238` now have `RowPresentationText` source names
  and concrete crosswalk entries.
- the EBATTLE3 exact `MSG_BTL_*` action rows `160/161/176`, `211..227`,
  `229..231`, `241/242`, and `274/300..307` now have `RowPresentationText`
  source names; no-op rows `235/236` carry `FlavorRowPresentationText`.
- the EBATTLE1 exact `MSG_BTL_*` action-tail rows `62/63`, `66..74`, `77`,
  `88/89`, and `91..94` now have `RowPresentationText` source names. The only
  row-backed EGOODS2 scripts now have `ItemUsePayloadText` labels instead of
  inherited battle-message shells.

The EBATTLE2 `119..134` anchors now carry `FlavorRowPresentationText` names in
source. The EBATTLE4/status rows keep their existing event/status/result labels
because several are dual-use scripts rather than pure flavor strings.

## Recovered Lifeup Join

Rows `32..35` are no longer in the pointer-recovery frontier:

- local row inspection proves all four rows use `EF:8543` as row `+4`;
- local C2 notes prove the Lifeup behavior wrappers at `C2:9AC6`, `C2:9ACF`,
  `C2:9AD8`, and `C2:9AE1`;
- EF Lifeup explanation text at `EF:5173..51BB` and enemy-action flavor text
  at `EF:8D4C` are separate anchors and should not be treated as row `32..35`
  presentation messages.

This is exactly the kind of case where the row `+8` behavior body was already
strong, but the `C1:DD9F` presentation text still needed the row `+4` pointer.
The pointer is now recovered, so the shared PSI row-presentation label covers
rows `10..35`, `48`, `49`, `53`, `58`, `60`, and `61`.

The EF source comments should keep the negative guardrails at `EF:5173..51BB`
and `EF:8D4C`, but those guardrails now mean "not the Lifeup row message"
rather than "Lifeup row message unrecovered."

## Recovered Explosive Join

Rows `64` and `65` are also no longer in the pointer-recovery frontier:

- local notes prove both rows reach the `C2:A821` super-bomb/explosive wrapper;
- row `101` proves one `C2:A821` row-message join at `EF:7ED5`;
- local row inspection proves `64 -> EF:9A7E -> C2:A821` and
  `65 -> EF:9A9E -> C2:A821`.

The EF source comments now mark `EF:9A7E/9A9E` as row-presentation text, not
candidate flavor. Keep row `101 -> EF:7ED5` separate because it reaches the
same C2 explosive wrapper with fired-missile presentation text.

## Promotion Rules

Use the recovered row `+4` bank to decide the follow-up:

- `EF:*`: add the row to `notes/ef-battle-text-row-message-crosswalk.md` only
  when the row id, EF message pointer, and row `+8` behavior pointer are all
  known.
- `C7:*`, `C8:*`, or `C9:*`: add the row to the non-EF row-message lane table;
  do not create or rename EF anchors for it.
- Behavior body emits `EF:*` through `DC1C` or `DC66`: document that as a
  secondary result payload, not as the row `+4` action-message pointer.
- Behavior body emits C8/C9 amount or narrative text: keep the row-message
  anchor conservative and point the result lane to the C2-focused note.

## Source Boundary

Do not promote D5 source data or regenerate broad table docs as part of an EF
battle-text row-message pass. If D5 table bytes are later promoted in a separate
owned pass, this EF note can consume that result, but it should not drive broad
source/manifold churn from within the EF battle-text scope.
