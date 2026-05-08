# Text Entry Builder `C1:13D1` / `89D4`

This note captures the current best local model for the shared bank-`01` text-entry builder rooted at `C1:13D1`.

See also [short-text-staging-buffer-9c9f.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/short-text-staging-buffer-9c9f.md), [text-command-family-19-data-and-substitution.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-19-data-and-substitution.md), and [naming-buffer-commit-family-c1ead6-c4d065.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/naming-buffer-commit-family-c1ead6-c4d065.md).

## Main result

`C1:13D1` is now best read as a shared active text-entry allocator or installer over the record table rooted at `$89D4`, not as a stable selector-buffer writer.

That matters because it gives the current `$9C9F` story a clean downstream boundary:

- non-naming item/equipment-side producers stage text into `$9C9F`
- they then feed `C1:13D1` or nearby shared builders
- `C1:13D1` installs a live text-entry record in the current active context
- that path does not locally imply any commit into selector buffer `$9801`

## Caller families

Pinned direct callers:

- `C1:14F8`
- `C1:1629`
- `C1:2EB2`
- `C1:7881`
- `C1:78DD`
- `C1:99E8`
- `C1:9B15`

That spread is useful by itself: loaded-string, item-side, equipment-side, and other menu/display paths all reuse the same builder.

## Strong local shape

The strongest current local model is:

1. resolve the current active context through `$8958 -> $88E4 -> $8650`
2. allocate or reuse one entry in the table rooted at `$89D4`
3. link that entry back into the active context and the local per-context chain fields
4. copy caller-supplied text bytes from source pointer `$06/$08` into the entry body
5. store caller-supplied companion pointers or metadata from `$0A/$0C`
6. initialize per-entry state bytes and words before returning the entry base

The important practical point is that the builder is record-oriented and context-oriented. It is not just copying bytes into one global string field.

## `89D4` table behavior

Two local helpers sharpen the table side:

- `C1:1354` scans the `89D4` family for a free slot and returns an index or `-1`
- `C1:13D1` then installs the selected entry and returns its base address

The strongest currently visible table behavior is:

- record `+0` acts like an active or allocated marker
- record `+2` acts like a chain or next-link field and is initialized to `-1`
- record `+4` is also chain-related and is updated from the active-context side
- record `+0x0F` receives caller-supplied companion metadata or pointer words from `$0A/$0C`
- record `+0x13` receives copied text bytes from source pointer `$06/$08`

I am keeping those field names deliberately soft, because the chain semantics are not yet fully closed. But the allocator/installer model itself is in good shape.

## Why this matters for `$9C9F`

The non-naming producers at `C1:99E8` and `C1:9B15` are the key local bridge here.

Those paths:

- stage item-side text through `$9C9F`
- set source pointer `$06/$08` to that staging buffer
- then call `C1:13D1`

So the current best local read is:

- `$9C9F` is a short-text staging buffer
- `C1:13D1` is the shared live-entry installer that consumes staged text
- neither step, by itself, materializes selector buffer `$9801`

That is stronger and cleaner than treating `$9801` as the generic endpoint of all small dynamic text paths.

## Relation to loaded-string queue path

The loaded-string side around `C1:7881 / 78DD` also reuses `C1:13D1`, which makes the builder look even more general.

So the safest current split is:

- `$97D7/$97CA` = queued loaded-string input side
- `$9C9F` = one important short-text staging source among several
- `C1:13D1` = shared active text-entry allocator/installer
- `$9801` = separate naming-side committed selector buffer with its own proved write bridge

## Confidence boundaries

### Locally proved

- `C1:13D1` is shared by loaded-string, item-side, and equipment-side callers
- `C1:1354` scans the `89D4` family for a free entry and returns `-1` on failure
- `C1:13D1` returns an installed entry base, not just a scalar result
- `C1:99E8` and `C1:9B15` feed staged `$9C9F` text into `C1:13D1`

### Still open

- the exact final names of the `89D4` record fields
- the exact chain semantics of the `+2` and `+4` words
- whether every `C1:13D1` caller uses the entry body in exactly the same display pipeline

## Best current interpretation

The safest current interpretation is that `C1:13D1` is the shared live text-entry builder for the bank-`01` text and menu side. It allocates or reuses a record in the `89D4` table, links it into the current active context, copies caller-supplied text into the record body, and returns the entry base for later display-side work.

That gives the current selector and staging notes a healthier boundary: `$9C9F` is a broader short-text staging buffer, while `$9801` remains a separate naming-side committed buffer with its own dedicated write path.
