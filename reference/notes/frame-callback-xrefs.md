# Frame Callback Cross-References

- ROM: `EarthBound (USA).sfc`
- Callback dispatcher: `C0:8518` (`JMP ($0020)`)
- Callback setter: `C0:851C`
- Default callback stub: `C0:851B`
- Default-reset helper: `C0:8522`

## Direct Callback Installs

| Call Site | Target | Evidence |
| --- | --- | --- |
| `C0:B6CB` | `C0:DC4E` | `LDA #$DC4E ; JSL $C0851C` |
| `C4:F595` | `C0:F41E` | `LDA #$F41E ; JSL $C0851C` |
| `C4:F701` | `C0:DC4E` | `LDA #$DC4E ; JSL $C0851C` |
| `EF:E2CA` | `C0:DC4E` | `LDA #$DC4E ; JSL $C0851C` |

## Explicit Resets To Default Callback

| Call Site | Behavior |
| --- | --- |
| `C4:F673` | `JSL C0:8522`, which writes `#$851B` to `$20/$21` |

## Observations

- All discovered installed callback targets are `C0:` addresses, which matches the 16-bit indirect `JMP ($0020)` dispatcher in bank `C0`.
- `C0:B6C8`, `C4:F6FE`, and `EF:E2C7` all install `C0:DC4E`.
- `C4:F592` installs `C0:F41E`.
- `C4:F673` explicitly restores the default callback stub through `C0:8522`.
- `NMI_FinalizeFrame` runs the callback with `DBR=7E` and `DP=0200` immediately before returning from interrupt.
