# Text Command Family `1F`: Deferred Callbacks And Event Helpers

This note is the top-level overview for bank-`01` text command family `0x1F`.

See also [timed-event-callback-family-bank01.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-event-callback-family-bank01.md).
See also [timed-event-callback-invoker-c187cc.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-event-callback-invoker-c187cc.md).
See also [try-fix-item-callback-d0.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/try-fix-item-callback-d0.md).

## Main result

The safest current local read is that `0x1F` is the bank-`01` deferred-callback and event-helper family.

In the live parser path, top-level command byte `0x1F` dispatches through the bank-`01` family rooted at `C1:81BB`. The family includes both immediate helper-style leaves and deferred same-bank callback leaves that later execute through the callback invoker at `C1:87CC`.

## Best current family shape

The strongest currently pinned members are:

- `0x1F D0` -> Jeff repair / broken-item callback family
- `0x1F D1` -> immediate nearby magic-truffle direction helper
- `0x1F D2` -> strongest current fit wandering-photographer summon branch
- `0x1F D3` -> timed-delivery callback branch

The most concretely proved deferred branch is `0x1F D3`:

- script uses `[1F D3 xx]`
- bank `01` resolves the leaf to low word `C1:7440`
- `C1:87CC` invokes that low word with an RTS-as-JSR same-bank callback step
- `C1:7440` forwards `X` into `EF:0EAD`

The callback interface is now locally pinned too:

- callback low word comes from `Y`
- `X` is loaded from `$14`
- `$14` is the first byte fetched from the callback payload stream at `C1:87A7`

So for timed delivery, the payload byte after `0x1F D3` becomes the 1-based delivery row selector.

## Why this family matters

`0x1F` is broader than a timed-delivery-only mechanism.

The manager around `C1:80B2` selects among several small same-bank low-word workers, and the surrounding queue state comes from ordinary bank-`01` text-command machinery such as `$97BA/$97CA`. That makes the family read much better as a deferred text-command callback framework with a few immediate neighboring event helpers, not as one private delivery-state machine.

This matters because it explains why very different gameplay-side effects can share one command family:

- timed delivery
- Jeff repair
- magic-truffle direction
- wandering photographer

They are all being routed through the same bank-`01` deferred-callback / event-helper machinery.

## Best current interpretation

The safest current interpretation is that `0x1F` is the bank-`01` deferred callback family, with same-bank low-word workers executed later by `C1:87CC`, plus a few closely related immediate event-helper branches in the same top-level family.
