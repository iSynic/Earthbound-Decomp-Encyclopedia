# Audio SPC700 FF Target Review

Status: FF is outside the source-backed VCMD table; reader effect proof is still pending.

## Summary

- FF in source-backed VCMD table: `False`
- source-backed command range: `0xE0..0xFE`
- source-backed VCMD entries: `31`
- FF reader PCs: `1`
- FF runtime reads: `10`
- exact-duration promotion allowed: `False`
- semantic status: `outside_vcmd_table_reader_effect_pending`

## Source Boundary

- source role: `outside_vcmd_table`
- source label: `None`
- source target: `None`
- arg length: `None`
- effect proof status: `outside_vcmd_table_reader_effect_pending`

## Reader PCs

| Reader PC | Source label | Driver offset | FF reads |
| --- | --- | --- | ---: |
| `0x0957` | `SkipByte` | `0x0457` | 10 |

## Findings

- The checked-in byte-perfect source backs VCMD entries for 0xE0..0xFE only.
- 0xFF has no source-backed VCMD label, target, or argument length.
- Runtime reader traces still observe FF bytes, so FF remains a focused reader-effect proof lane rather than a dispatch-table entry.

## Next Work

- trace reader PC 0x0957 FF observations and record the post-read effect
- classify observed FF bytes as unreachable/data-like or EarthBound-specific control behavior
- feed only locally proven FF effects back into sequence command semantics
