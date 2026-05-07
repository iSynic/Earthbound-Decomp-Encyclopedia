# C3 Battle Visual Effect Dispatch Source Contract `C3:F981`

This note closes the extraction caveat for `C3:F981`. The routine is source-ready as long as the two colour-token tables remain explicit data tables next to the dispatcher.

## Working Names

- `C3:F981` = `DispatchBattleVisualEffectToken`
- `C3:F951` = `BattleVisualToken23To2dColourTriples`
- `C3:F972` = `BattleVisualToken31To35ColourTriples`
- `C3:F9A2` = `ApplyBattleVisualToken23To2dColourEffect`
- `C3:FA4A` = `ApplyBattleVisualToken31To35ColourEffect`
- `C3:FAC7` = `ReturnFromBattleVisualEffectTokenDispatch`

## Entry Contract

- Input `A` is a battle visual/effect token.
- The routine is called locally by `C3:FAC9`, which is in turn called by the battle text command path at `C1:7400`.
- It returns with no meaningful numeric result; the caller-facing result belongs to `C3:FAC9`.

## Dispatch Ranges

`C3:F981` is a range dispatcher:

| Token range | Behavior |
| --- | --- |
| `< 0x23` | Pass token directly to `C2:E116`. |
| `0x23..0x2D` | Load one 3-byte row from `C3:F951`, call `C2:DE0F`, then apply the fixed-colour path. |
| `0x2E` | Store `0x0090` to `$AD92`. |
| `0x2F` | Store `0x012C` to `$AD94`. |
| `0x30` | No-op. |
| `0x31..0x35` | Load one 3-byte row from `C3:F972`, call `C2:DE0F`, then apply the fixed-colour path. |
| `>= 0x36` | No-op. |

## Colour Triple Tables

The two tables are fixed 3-byte rows:

- `C3:F951`: 11 rows for tokens `0x23..0x2D`
- `C3:F972`: 5 rows for tokens `0x31..0x35`

The branch bodies consume each row in reverse call-register order:

1. row byte `+2` -> `A`
2. row byte `+1` -> `X`
3. row byte `+0` -> `Y`
4. `C0:B01A(A, X, Y)` applies the selected fixed-colour components

The existing working note names the table values as colour triples in source order. For extraction, the important rule is to preserve the row tables and symbolic row indexing rather than flattening the current rows into per-token code.

## Shared Colour Path

Both table-backed paths do the same core work:

1. `C2:DE0F`
2. read the selected 3-byte row
3. `C0:B01A(row[2], row[1], row[0])`
4. `C0:B039(A = 0x10, X = 0x3F)`
5. `C4:A67E(...)`

The `C4:A67E` parameters differ by range:

- tokens `0x23..0x2D`: `A = 5`, `X = 7`
- tokens `0x31..0x34`: `A = 4`, `X = 5`
- token `0x35`: `A = 2`, `X = 4`

## Wrapper Contract

`C3:FAC9` wraps this dispatcher for the battle text command path:

- it reads the current battle actor record pointer from `$A972`
- if actor byte `+0x0F == 0xD5`, it returns `1` without dispatching
- if actor byte `+0x0E == 0`, it dispatches the explicit input token and returns `0`
- otherwise it dispatches the original `X`/secondary token and returns `1`

`C1:73C0` stages that `0/1` result through `C1:045D`, which matches the text-command use as a PSI/battle animation display helper.

That bank-`01` wrapper is now source-backed in `src/c1/c1_7274_stage_bank_deposit_accumulator_text_value.asm` as `StageBattleVisualEffectResultTextCommand`.

## Source Translation Notes

A source version should keep this shape:

```text
if token < 0x23:
    dispatch_base_effect(token)
elif token <= 0x2D:
    apply_colour_triple(TOKEN_23_TO_2D[token - 0x23], duration_a=5, duration_x=7)
elif token == 0x2E:
    WOBBLE_DURATION = 0x0090
elif token == 0x2F:
    SHAKE_DURATION = 0x012C
elif 0x31 <= token <= 0x35:
    if token < 0x35:
        apply_colour_triple(TOKEN_31_TO_35[token - 0x31], duration_a=4, duration_x=5)
    else:
        apply_colour_triple(TOKEN_31_TO_35[token - 0x31], duration_a=2, duration_x=4)
```

The names `WOBBLE_DURATION` and `SHAKE_DURATION` are source-contract placeholders for `$AD92` and `$AD94`; final global names should come from the broader battle visual state pass.

## Confidence

- Dispatch ranges: high confidence
- Table boundaries and row counts: high confidence
- Row byte consumption order: high confidence
- Exact player-facing meaning of each token: intentionally deferred to battle action/effect caller documentation
