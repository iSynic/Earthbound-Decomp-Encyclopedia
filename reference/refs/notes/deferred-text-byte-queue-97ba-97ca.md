# Deferred Text Byte Queue At `97BA` / `97CA`

This note records the current local picture of the bank-`01` byte queue that sits next to the timed-event callback family.

See also [timed-event-callback-family-bank01.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-event-callback-family-bank01.md).
See also [timed-event-callback-invoker-c187cc.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-event-callback-invoker-c187cc.md).

## Main result

`97BA` / `97CA` now look like a small deferred byte-command queue in bank `01`.

The strongest local anchors are:

- `C1:4265`
- `C1:42AD`
- `C14070`

## Producers

`C1:4265` and `C1:42AD` both follow the same shape:

- if `97CA == 0`, they store a one-byte value into `97BA + 97CA`
- increment `97CA`
- return a small callback low word (`4265` / `42AD`)

If `97CA` is already nonzero, they take a different immediate path instead of queueing another deferred byte.

That makes `97BA` look like queued byte payload storage, and `97CA` like the current queued-byte count.

## Selector helper

`C14070` scans the `97BA` byte list using `97CA` as the active count.

Its current best local read is:

- walk the queued byte list
- compare against the requested byte/state in `$0E`
- return a small result measuring match or difference rather than just a yes/no flag

The exact return semantics are still not fully named, but it is clearly consuming the same `97BA/97CA` queue populated by the ordinary text-command handlers above.

## Why this matters for the callback family

The bank-`01` manager around `C1:80B2` uses `C14070` before choosing sibling low-word callbacks like:

- `61F0`
- `7274`
- `7440`
- `7708`

So the callback family is now best read as part of a broader deferred text-command framework. Timed delivery is one proven callback branch inside that framework, not the whole system.

## Best current interpretation

The safest current interpretation is:

- `97BA` = queued one-byte deferred text-command payloads
- `97CA` = count or fill level for that byte queue
- `C14070` = queue-state selector/helper used by the sibling callback dispatcher at `C1:80B2`
