# Timed-Event Callback Family In Bank `01`

This note captures the current local picture of the bank-`01` callback-style low-word family that the managed timed-event slot system appears to queue and later invoke.

See also [timed-event-slot-block-7440-and-c20abc.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-event-slot-block-7440-and-c20abc.md).
See also [timed-delivery-row-index-command-1f-d3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-row-index-command-1f-d3.md).
See also [delivery-row-helpers-ef0e67-ef0ead.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/delivery-row-helpers-ef0e67-ef0ead.md).
See also [timed-event-callback-invoker-c187cc.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-event-callback-invoker-c187cc.md).
See also [try-fix-item-callback-d0.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/try-fix-item-callback-d0.md).

## Main result

The strongest current read is that the managed bank-`01` timed-event slots do not just hold raw data words. They appear to hold callback-like low words for small bank-`01` adapter routines.

The clearest locally pinned member is `C1:7440`:

- text command `0x1F D3` selects low word `$7440`
- `C1:7440` begins with `TXA`
- it then does `JSL EF:0EAD`
- and returns `0`

That is exactly the shape we would expect for a queued callback adapter: take the current `X` value from the manager, forward it to a subsystem helper, then report completion.

## Proven timed-delivery bridge

`EF:0EAD` is already the locally mapped helper that takes a 1-based delivery row selector and instantiates the chosen delivery sprite or placeholder.

So the strongest direct bridge now is:

1. script uses `[1F D3 xx]`
2. bank `01` resolves the `D3` leaf to callback low word `C1:7440`
3. the managed slot system queues that low word in the front half of a `96AA + 0x1A * n` slot
4. when invoked, `C1:7440` forwards `X` into `EF:0EAD`

That invocation path is now pinned at `C1:87CC`, which uses an RTS-as-JSR trick to call the low word currently held in `Y`. The immediately preceding setup at `C1:87A7` shows that `X` comes from the first byte of the callback payload stream, not from the slot id. So for the timed-delivery branch, the current safest read is that the queued callback stream supplies the 1-based delivery row selector directly.

## Sibling callback-style entries

The bank-`01` manager around `C1:80B2` appears to select among several similar low-word callback entries, not just `7440`.

A useful new boundary came out of the sibling scan: this looks broader than a timed-delivery-only mechanism. The selector helper `C14070` is not reading delivery rows. It scans the byte queue at `97BA` with count `97CA`, and that same queue is populated by ordinary bank-`01` text-command handlers such as `C1:4265` and `C1:42AD`. So the sibling callback family now reads best as a deferred text-command callback framework that timed delivery plugs into, not as a private delivery-state machine with a few extra branches.

The strongest current candidates surfaced in the same manager block are:

- `C1:61F0`
- `C1:7274`
- `C1:7440`
- `C1:7708`

The first bytes of those entries are consistent with small bank-`01` worker or adapter routines rather than plain data blobs.

Three of those siblings are now strong enough to name cautiously from local-plus-reference evidence:

- `D0 -> C1:85E7 -> C1:63A7` is now the strongest `EBTEXT_TRY_FIX_ITEM` candidate. The script macro is explicit in `ebsrc` (`.BYTE $1F, $D0, arg`), and the only currently exposed uses in the `eb-decompile` script dump are the two `1F D0` calls inside the Jeff-repair script family that prints `Working through the night, [Jeff] fixed the [broken item].` and sets `FLG_WINS_JEFF_REPAIR`. Locally, this callback family uses private scratch `$97D5`, shared byte-queue state `$97BA/$97CA`, and helper bytes `$97BB/$97BC`, which makes it read like a stateful broken-item/repair resolver rather than a one-shot timed-delivery adapter. The exact meanings of the helper bytes and the two observed arguments (`0x64` and `0x19`) still need tighter local proof, so the semantic name should stay cautious for now.
- `D1 -> C1:85ED` is the immediate magic-truffle branch. It does `JSL C4:90EE`, and `ebsrc` exposes a nearby bank-`04` symbol `GET_DISTANCE_TO_MAGIC_TRUFFLE`. Combined with the macro name `EBTEXT_GET_DIRECTION_OF_NEARBY_TRUFFLE`, the safest current read is that this is the immediate nearby-magic-truffle direction helper rather than a queued callback.
- `D2 -> C1:8602 -> C1:7304` is the strongest current wandering-photographer candidate. The macro name is `EBTEXT_SUMMON_WANDERING_PHOTOGRAPHER`, and the local callback chain fans into `C4:B54A` and `C4:B565`, two bank-`04` helpers that sit in the same general area as photographer-related data in the reference project. So the safest current read is that `7304/7325/...` are the deferred photographer-event callback chain.

The clearest fully pinned callback remains `C1:7440`, because it has a direct `JSL EF:0EAD` bridge. But `C1:61F0 / C1:63A7` no longer looks like an anonymous sibling. It now looks much more like the deferred broken-item/Jeff-repair member of the same bank-`01` framework.

## Why this matters

This shifts the slot-family model in a useful way.

Before this pass, the front half of the `0x1A` slot records looked like anonymous payload words. After this pass, the safer model is:

- front-half words can include callback low words selected by `0x1F` text-command leaves
- the back half still holds the saved active-slot/object snapshot handled by `C20A20` / `C20ABC`

So the timed-event manager now looks more like a queued callback-and-context system than a plain argument buffer.

## Best current interpretation

The current safest interpretation is that the bank-`01` timed-event slot system queues small callback adapters plus a saved object/context snapshot.

For the timed-delivery branch specifically, that adapter is `C1:7440`, and its target helper is `EF:0EAD`.
