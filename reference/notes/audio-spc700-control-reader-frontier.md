# Audio SPC700 Control Reader Frontier

Status: runtime control-byte reader PCs identified; command effects remain unpromoted.

## Summary

- reader PCs: `10`
- control reads: `4242`
- command counts: `{'0x00': 4107, '0xEF': 119, '0xFD': 1, '0xFE': 5, '0xFF': 10}`
- source-backed reader labels: `{'0x0955': 'GetNextByte', '0x0957': 'SkipByte'}`
- exact-duration promotion allowed: `False`
- semantic status: `reader_paths_known_effects_unpromoted`

## Reader PCs

| PC | Source label | Control reads | Commands | Driver offset | First byte | Window SHA-1 |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `0x2DB0` | `None` | 957 | `{'0x00': 957}` | `0x28B0` | `0xD0` | `617b11afc4d1b78051b8590c6d9687445820e1ad` |
| `0x2DDA` | `None` | 955 | `{'0x00': 955}` | `0x28DA` | `0xD0` | `463b22d6a538f0a6fe2e863d4e4b6b11f2df9729` |
| `0x2DF8` | `None` | 955 | `{'0x00': 955}` | `0x28F8` | `0xD0` | `21ab0edf7758b50e76287a619649bcfc812ea9a9` |
| `0x2E3D` | `None` | 952 | `{'0x00': 952}` | `0x293D` | `0xF0` | `a8473735e4138a6d916e7eb9c0f6a9272a18a4b1` |
| `0x0B8A` | `None` | 179 | `{'0x00': 84, '0xEF': 95}` | `0x068A` | `0x68` | `1a6168ece78aea4a63985c4573db7a916a776d2d` |
| `0x0957` | `SkipByte` | 151 | `{'0x00': 114, '0xEF': 23, '0xFE': 4, '0xFF': 10}` | `0x0457` | `0xBB` | `1bacf73e7baf6f7c3225d8165f0b470cbc2bc6e2` |
| `0x0847` | `None` | 75 | `{'0x00': 73, '0xFD': 1, '0xFE': 1}` | `0x0347` | `0xD6` | `15e34dc26f3612b79ab5667e1a597921a9edb610` |
| `0x0782` | `None` | 8 | `{'0x00': 8}` | `0x0282` | `0xDA` | `e6e6c3a2551ecdcb98dded66c9c8bfe91b8af37e` |
| `0x07A6` | `None` | 8 | `{'0x00': 8}` | `0x02A6` | `0x5F` | `79ddb0bfb08126e98da9f100e62d691c45e96e76` |
| `0x0D12` | `None` | 2 | `{'0x00': 1, '0xEF': 1}` | `0x0812` | `0xF0` | `b6f5d5dfa93d252f4c74fff8726c534bccf71187` |

## Findings

- Runtime traces now identify concrete SPC700 PCs that read sequence control bytes.
- The checked-in byte-perfect source labels the strongest helper readers as GetNextByte and SkipByte.
- The control reader PCs are stronger next targets than the provisional high-command dispatch table for current exact-duration work.
- This frontier records offsets, counts, hashes, and sampled register context only; it does not embed ROM-derived driver byte windows.

## Next Work

- decode reader PCs that observe 0x00 because they are now the primary end-vs-return proof target
- decode reader PC 0x0957 because it observes FF, FE, and EF control bytes
- decode reader PC 0x0847 because it observes FD and FE control bytes
- decode reader PC 0x0B8A because it is the dominant EF reader in the sampled corpus
