# Bank CC Source Scaffold Residual Map

This file lists byte ranges not yet protected by the source-bank scaffold.
Classifications are planning hints, not final semantic proof.

## Summary

- bank bytes: `65536`
- protected bytes: `65536` (`100.0%`)
- residual bytes: `0`
- residual ranges: `0`

## Classification Totals

| Class | Ranges | Bytes |
| --- | ---: | ---: |

## Largest Residual Ranges

| Range | Size | Class | Reason | Top ebsrc overlaps | First bytes |
| --- | ---: | --- | --- | --- | --- |

## All Residual Ranges

| Range | Size | Class | Reason | Overlap Count | First bytes |
| --- | ---: | --- | --- | ---: | --- |

## Recommended Closure Order

1. Promote small `source-frontier` ranges with direct code evidence.
2. Split `mixed-code-data` ranges into explicit source segments and data gaps.
3. Move `script-data`, `text-data`, `battle-data`, and `data` ranges into structured asset manifests.
4. Leave `blank-data` and padding-like ranges as explicit data contracts only when a caller or table boundary needs them.
