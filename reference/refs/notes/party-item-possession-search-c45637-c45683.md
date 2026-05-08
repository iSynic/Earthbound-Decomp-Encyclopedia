# Party Item Possession Search `C4:5637` / `C4:5683`

This note captures the local role of the bank-`04` helper pair at `C4:5637` and `C4:5683`, and their bank-`01` `0x1D 05` wrapper.

## Main result

The safest current local read is:

- `C4:5637` = search one character inventory for a requested item id and return that character id on success
- `C4:5683` = wrapper around that search, supporting either one explicit character or wildcard `A = #$00FF` over the active party range
- `0x1D 05 -> C1:4D93` = text-command front end to that search family

So `0x1D 05` is now better than a vague possession predicate. At the low level it behaves like "find the first matching party member who has this item," even though many scripts only use the result as a truthy or falsey branch condition.

## `C4:5637`

Entry behavior:

- `A` behaves like a 1-based character id
- `X` behaves like a 1-based item id to search for

The helper then:

1. decrements the character id and maps it through `C0:8FF7` with stride `#$005F`
2. lands on the selected character record at `$99F1 + 0x5F * (character - 1)`
3. scans 14 bytes of the item area starting at `$99F1`
4. compares each byte directly against the requested item id
5. returns the original character id on the first match, otherwise `0`

The important point is that this is a general inventory scan, not the four-byte equipped-item predicate already mapped at [equipped-item-presence-predicate-c3e9a0.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/equipped-item-presence-predicate-c3e9a0.md).

## `C4:5683`

This is the wrapper that makes the search family script-friendly.

- If `A != #$00FF`, it just forwards the explicit character id to `C4:5637`.
- If `A == #$00FF`, it loops over the leading party-range entries in `$986F`, stopping at `$98A4`, and calls `C4:5637` for each active party character code until a match is found.
- On success it returns the matching character id.
- On failure it returns `0`.

That wildcard behavior is important: the helper does not scan arbitrary entities. It only scans the party-range portion of `$986F`, which is why the newer `$986F/$98A4` registry work matters here too.

## `0x1D 05 -> C1:4D93`

The bank-`01` leaf at `C1:4D93` wraps the same search family in the usual text-command shape:

- it accepts either an explicit character id or wildcard `0x00FF`
- it resolves the requested item id from either queued command bytes or the live text context
- it calls `C4:5683`
- it stages the returned character id through `C1:045D`

At the script level, that still fits `CHECK_IF_CHARACTER_HAS_ITEM`, because most callers immediately use `JUMP_IF_TRUE` / `JUMP_IF_FALSE`. But the local low-level result is more informative than a pure boolean: on success the command returns the first matching character id.

## Useful local cross-checks

A few non-`0x1D` callers make the same behavior plausible.

- `C1:3CED` calls `C4:5683` with wildcard `A = #$00FF` and item `#$00CA`, then branches only on zero vs nonzero, which matches a party-wide item-presence check.
- `C3:EBE0` also calls `C4:5683` with wildcard `A = #$00FF`, then uses the returned nonzero character id to choose between two different downstream item-display paths.

So the helper family is broader than one text command, but the common core is stable: search party inventories and return the matching holder id if any.

## Confidence

- `C4:5637` as per-character 14-slot inventory search: high confidence
- `C4:5683` as explicit-or-wildcard wrapper over that search: high confidence
- `0x1D 05` as front end to that search family: high confidence
- script-level label `CHECK_IF_CHARACTER_HAS_ITEM` as behaviorally correct but low-level incomplete: high confidence
