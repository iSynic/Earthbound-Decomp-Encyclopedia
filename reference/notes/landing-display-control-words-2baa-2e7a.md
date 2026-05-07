# Landing Display Control Words `$2BAA` And `$2E7A`

This note captures the current best local read on the producer-side control words that steer the landing-display stream dispatcher.

See also [landing-display-assembly-cluster-c007b6-c4b26b.md](notes/landing-display-assembly-cluster-c007b6-c4b26b.md).
See also [landing-display-profile-overview.md](notes/landing-display-profile-overview.md).

## Main result

The safest current local read is that `$2BAA` and `$2E7A` are small per-record control words for the landing-display producer side, not generic unrelated state.

They are read directly by `C0:AC43`, the record-driven dispatcher that decides which timed stream families are ticked before renderer records are enqueued through `C08C58`.

## `$2E7A` as a runtime dispatch-flag word

`$2E7A` is currently the cleaner of the two words.

Locally proved behavior:

- `C0:7846` clears the active record's `$2E7A`
- `C0:78A9..78AF` sets bit `0x8000`
- `C0:78D5..78DB` sets bit `0x4000`
- `C0:ACD9..AD1F` later tests sign and bit `0x4000` from the same word

The current safest dispatch-side read is:

- sign bit `0x8000` enables the later `2F6A / 2FE2` stream family at `C0:ACE6..AD17`
- bit `0x4000` enables the later `2EB6 / 2F2E` stream family at `C0:AD19..AD55`

So `$2E7A` is best read as a runtime stream-enable flag word for the later producer pass.

I am still keeping the player-facing meaning of those two enabled stream families open.

## `$2BAA` as a richer per-record control word

`$2BAA` is broader and slightly less closed than `$2E7A`, but several bits now have useful local roles.

### Bit `0`

`C0:AC4E..AC59` tests bit `0` and chooses either `0` or `5` as a small bias added to later emitted stream values.

So the safest current read is:

- bit `0` selects between two closely related emitted-value variants or phase offsets

### Bits `2-3`

`C0:AC5B..AC66` masks `$2BAA & 0x000C` before the first dispatch branch.

Current locally proved behavior:

- `0x0000` skips the first timed-stream branch entirely and falls through to the later producer logic
- `0x0004` jumps directly into the `2F6A / 2FE2` branch at `C0:ACE1`
- any other nonzero value reaches the `301E / 3096` versus `30D2 / 314A` side first, with `$2A7E == #$0040` choosing the former and other values choosing the latter

So the safest current read is:

- bits `2-3` are the main producer-side stream-group selector field inside `$2BAA`

### Bits `2` and `3` in the earlier setup-side readers

Two earlier helpers, `C0:A508..A53D` and `C0:A7C8..A7FD`, also read the same two bits.

Current locally proved behavior there:

- bit `3` (`0x0008`) enables an extra prepass through `C0:A56E`
- bit `2` (`0x0004`) enables a second optional extra pass through that same helper after the first succeeds

Those setup paths now read more concretely than before. In `C0:A508..A56D` and `C0:A7C8..A82E`, the extra passes do not branch into the later queue families directly. Instead they seed `C0:A56E`, which repeatedly mutates the local `$0094/$0092/$0097` geometry words and calls `C0:8643`.

`C0:8643` itself now has a stronger local split:

- with nonnegative `$0D`, it appends 8-byte DMA descriptor records into the live `$0400` queue family
- with negative `$0D`, it instead performs an immediate DMA-style path through `$4310/$4312/$4314/$4315` and `$2115/$2116`

That nonnegative path is now locally pinned one step farther too: `C0:8240` is the consumer of those `$0400` records, treating each 8-byte entry as a standard DMA descriptor with transfer mode and VRAM increment source in word `+0`, size at `+1`, source CPU address at `+3/+5`, and VRAM destination at `+6`.

In the `$2BAA`-gated setup callers, the working values loaded into `$0091/$0094/$0096/$0097` make this look much more like extra pre-render DMA strip generation than extra queue-family selection. The split is now a little tighter too:

- the extra setup-side passes seed a fixed bank-`C4` source at `$0BE8`
- the later main per-record pass seeds its source from `$341A & #$FFFE` plus record bank byte `$2A42`

So the safest current read is:

- bits `2-3` do not only choose later stream groups
- they also control how many extra setup-side DMA strip-generation passes are applied before the main landing display object is staged
- those extra passes look more like auxiliary or common strip uploads layered around the record's main DMA path than like alternate queue-family selection

The exact visual meaning of those extra generated DMA strips or descriptors is still open.

## Supporting cross-check: `C0:7994`

`C0:7994` gives one useful secondary anchor on `$2BAA & 0x000C`.

### Working Names

- `C0:7994` = `SetLandingDisplayTimerFromControlBits`

Locally, it maps:

- `0x000C` -> `0x0018`
- `0x0008` -> `0x0010`
- otherwise -> `0x0008`

and stores that result into `$0F12` for the current record.

That strengthens the current read that bits `2-3` are a real three-state producer-side control field, not just incidental flags.

## Best current interpretation

The safest current interpretation is:

- `$2E7A` is a runtime stream-enable word, with at least bits `0x8000` and `0x4000` controlling whether the later `2F6A / 2FE2` and `2EB6 / 2F2E` producer branches run
- `$2BAA` is a richer per-record control word, with:
  - bit `0` choosing a small emitted-value variant or bias
  - bits `2-3` choosing the initial stream-group path in `C0:AC43`
  - those same bits also controlling extra setup-side passes through `C0:A56E`

## What is still open

- the exact visual or player-facing meaning of the extra DMA strip or descriptor records generated by the `$2BAA`-gated `C0:A56E` passes
- the exact semantic names of the three `$2BAA & 0x000C` states
- the exact player-facing role of the stream families enabled by `$2E7A`
- whether any additional `$2E7A` bits matter outside the currently pinned `0x8000` and `0x4000`
