# Naming Buffer Commit Family `C1:EAD6..EBDD` / `C4:D065`

This note captures the first clean local write-side bridge into the fixed-width selector buffers behind `0x19 28`.

See also [statistic-selector-family-c4550f-c3ee7a.md](notes/statistic-selector-family-c4550f-c3ee7a.md), [text-command-family-19-data-and-substitution.md](notes/text-command-family-19-data-and-substitution.md), and [short-text-staging-buffer-9c9f.md](notes/short-text-staging-buffer-9c9f.md).

## Main result

The write-side bridge into `$9801` is not the generic queued loaded-string path around `$97D7`, and it is not the downstream naming-side display compilers `C4:41B7 / C4:40B5`.

## Working Names

- `C1:EAD6` = `RunNamingBufferCommitFlow`
- `C1:EC04` = `CommitNamingBufferFieldWithPreview`
- `C4:D065` = `NormalizeNamingBufferToCommittedSelectorText`

`C1:EAD6..EC8F` is now source-backed at `src/c1/c1_ead6_run_naming_buffer_commit_flow.asm`.

The first clean local producer is the naming commit path at `C1:EBA0..EBDD`.

That path:

- treats `$9C9F` as the current naming-entry work buffer
- calls `JSL C4:D065` with:
  - `X = $9801`
  - `A = $9C9F`
- then copies `0x0C` bytes from `$9C9F` to `$97F5` through `JSL C0:8ED2`

So the safest current local split is:

- `$9801` = normalized committed naming buffer
- `$97F5` = direct-copy companion naming buffer

## `C4:D065`

`C4:D065` has one direct local caller:

- `C1:EBBF`

Locally, it behaves like a byte-by-byte naming-buffer normalizer or remapper:

- reads NUL-terminated bytes from the source buffer
- writes remapped bytes to the destination buffer
- explicitly special-cases:
  - `A`
  - `I`
  - `U`
  - `E`
  - `O`
- also has a broader uppercase-letter range path
- appends a final NUL terminator

That makes `$9801` look much more like a committed normalized naming buffer than a raw live-entry field.

## `C0:8ED2`

`C0:8ED2` is a generic bulk-copy helper:

- source from long pointer at `$0E`
- destination from `A`
- copy length from `X`

Locally it copies 16-bit words, so odd lengths should be treated cautiously.

In this naming path, the caller sets:

- source = `$9C9F`
- destination = `$97F5`
- length = `0x000C`

So the `$97F5` side is not being normalized by `C4:D065` here. It receives a direct fixed-length copy of the same naming-entry work buffer.

## Surrounding naming flow

The surrounding naming-side flow uses both buffers immediately after commit:

- `$9801` is displayed through the usual fixed-width selector/display path
- `$97F5` is copied and displayed as a parallel companion buffer

That is why the nearby `C4:41B7 / C4:40B5` helpers now read better as downstream naming-side display compilers rather than the write-side producers of either stable buffer.

## Confidence boundaries

### Locally proved

- `C1:EBA0..EBDD` is a naming-side commit path that writes `$9801` and `$97F5`
- `C4:D065` is called only from that path locally
- `C4:D065` remaps bytes from source buffer to destination buffer and NUL-terminates the result
- `C0:8ED2` is a generic bulk-copy helper and is used here to copy `0x0C` bytes from `$9C9F` to `$97F5`

### Still open

- the exact human-facing meaning of the `C4:D065` remap, beyond "naming-side normalization"
- whether non-naming ordinary script flows also materialize `$9801` through some other upstream loader path
- the exact global identity of `$9C9F` outside this naming/UI seam; [short-text-staging-buffer-9c9f.md](notes/short-text-staging-buffer-9c9f.md) now captures the strongest current local read that it is reused as a broader short-text staging buffer, not a naming-only field

## Best current interpretation

The safest current local interpretation is that the selector-`2` backing buffer at `$9801` has a dedicated naming-side commit path, while selector `1` at `$97F5` is filled in parallel by direct copy from the same work buffer.

That is materially stronger than the earlier model where the early selector buffers were only known as fixed-width readers with unclear producers. It also keeps the boundaries honest: `$9C9F` itself now looks broader than naming, while the `C1:EBA0..EBDD -> C4:D065` path is specifically the naming-side commit use of that broader staging buffer family. Just as importantly, no separate non-naming immediate materialization of `$9801` is currently pinned, so the broader reusable short-text staging role belongs more naturally to `$9C9F` than to selector `2` itself.
