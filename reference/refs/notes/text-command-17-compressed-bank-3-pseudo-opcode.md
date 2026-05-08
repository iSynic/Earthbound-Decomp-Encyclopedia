# Text Command `0x17` as Compressed-Bank-3 Pseudo-Opcode

This note captures the current best local read of script byte `0x17`.

See also [text-command-15-compressed-bank-1-pseudo-opcode.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-15-compressed-bank-1-pseudo-opcode.md).
See also [text-command-16-compressed-bank-2-pseudo-opcode.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-16-compressed-bank-2-pseudo-opcode.md).

## Main result

`0x17` is not best read as another ordinary bank-`01` text-command family like `0x18`, `0x19`, or `0x1D`.

The safest current local read is:

- `0x17` is a compressed-bank-3 parser-side pseudo-opcode in the script dumps
- the many parsed `0x17 xx` hits should not be treated as evidence of a broad live runtime family
- only a narrow low-subcommand helper block at `C1:7B56` is locally real, and it should be treated cautiously as adjacent text-engine plumbing rather than a new large subsystem

## Top-level parser proof

The ordinary parser root at `C1:890E` explicitly handles:

- `0x13 -> C1:8AB0`
- `0x14 -> C1:8ABA`
- `0x18 -> C1:8AC4`

What matters is the gap:

- there are no explicit ordinary-runtime branches for `0x15`, `0x16`, or `0x17`

So whatever the script disassembly calls `0x17 xx`, it is not entering the same top-level ordinary-runtime family machinery as `0x18`, `0x19`, `0x1A`, `0x1B`, `0x1C`, `0x1D`, `0x1E`, or `0x1F`.

That is the key reason not to overmap it as a normal command family.

## Why parser-backed hit counts are misleading here

Parser-side tools report heavy `0x17 xx` usage across ordinary event text, shops, hints, system text, and battle text.

That distribution is actually a warning sign, not proof of a rich gameplay family:

- the hits are broad and text-heavy in exactly the way compressed text-bank escapes would be
- many `0x17 xx` values appear with no plausible runtime dispatch support
- the top-level parser gap for `0x15..0x17` makes a broad live-family interpretation untenable

So the current parsed hit counts are best treated as text compression or parser artifact evidence, not as direct runtime-family evidence.

## Narrow live helper block at `C1:7B56`

There is still a small locally real dispatcher at `C1:7B56` that accepts subcommands:

- `0`
- `1`
- `4`
- `5`
- `6`
- `7`
- `8`
- `9`
- `0x0A`
- `0x0B`

with default fallback for the rest.

The strongest visible leaves in that block are:

- `0 -> 0x463B`
- `1 -> 0x467D`
- `5 -> 0x549E`
- `6 -> 0x4EB5`
- `7 -> C1:9A43`
- `0x0A -> C1:AC00`
- `0x0B -> C1:AAFA`

But because the top-level parser does not route ordinary `0x17` through a real family root, the safest interpretation is that this block is adjacent text-engine plumbing reused by compressed-bank handling or other internal paths, not a normal user-facing command family.

## Best current interpretation

The safest current interpretation is:

- keep `0x17` out of the ordinary text-command family roadmap
- treat script-dump `0x17 xx` hits primarily as compressed-bank-3 pseudo-opcode usage
- treat `C1:7B56` as a narrow internal helper block that happens to overlap some of the same subcommand numbering, without promoting it to a full standalone gameplay family

## Confidence boundaries

### Locally proved

- `C1:890E` has no ordinary-runtime top-level branches for `0x15`, `0x16`, or `0x17`
- parsed script dumps still expose many `0x17 xx` hits
- `C1:7B56` is a real small dispatcher with the limited case set listed above

### Still open

- the exact relationship among parser-side compressed-bank handling, `0x13/0x14`, and the narrow helper block at `C1:7B56`
- whether `0x15` should get a parallel quarantine note for the same reason

## Practical conclusion

This is a good place to stop rather than overdig.

`0x17` should currently be treated as a compressed-bank-3 pseudo-opcode or parser-side escape, not as the next adjacent bank-`01` runtime family to map.
