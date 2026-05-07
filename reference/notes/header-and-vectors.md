# EarthBound Header and Vectors

- ROM: `EarthBound (USA).sfc`
- Verified: `True`
- SHA-1: `d67a8ef36ef616bc39306aa1b486e1bd3047815a`
- Title: `EARTH BOUND`
- Map mode: `0x31`
- Cart type: `0x02`
- Checksum: `0x4048`
- Complement: `0xBFB7`

## Interrupt / Reset Vectors

| Vector | Header Offset | CPU Address | File Offset | Canonical ROM Mirror |
| --- | --- | --- | --- | --- |
| native_cop | 0xFFE4 | 0x005FFF | n/a | not directly mapped in ROM |
| native_brk | 0xFFE6 | 0x005FFF | n/a | not directly mapped in ROM |
| native_abort | 0xFFE8 | 0x005FFF | n/a | not directly mapped in ROM |
| native_nmi | 0xFFEA | 0x008147 | 0x008147 | 0xC08147 (0xC0) |
| native_irq | 0xFFEE | 0x00814B | 0x00814B | 0xC0814B (0xC0) |
| emulation_cop | 0xFFF4 | 0x005FFF | n/a | not directly mapped in ROM |
| emulation_abort | 0xFFF8 | 0x005FFF | n/a | not directly mapped in ROM |
| emulation_nmi | 0xFFFA | 0x005FFF | n/a | not directly mapped in ROM |
| emulation_reset | 0xFFFC | 0x008141 | 0x008141 | 0xC08141 (0xC0) |
| emulation_irqbrk | 0xFFFE | 0x005FFF | n/a | not directly mapped in ROM |

## Notes

- The reset vector starts execution at CPU address `0x008141`.
- On this HiROM cart, that reset trampoline mirrors to `0xC08141` and lives at file offset `0x008141`.
- The native NMI and IRQ trampolines likewise mirror to `0xC08147` and `0xC0814B`.
- Several other exception vectors point to `00:5FFF`, which is not directly mapped to ROM in bank `00`; treat those as unresolved until code tracing proves otherwise.
- The useful first-pass disassembly targets are the canonical bank `C0` routines reached by those trampolines: `C0:8000`, `C0:814F`, and `C0:8170`.
