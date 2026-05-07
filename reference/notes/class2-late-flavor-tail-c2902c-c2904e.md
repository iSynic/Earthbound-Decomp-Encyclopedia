# Class2 Late Flavor Tail C2902C C2904E

This note captures the strongest current local model for the small late `D5:7B68` tail around `C2:902C` and the neighboring `C2:9033..904E` stubs.

See also [class2-d57b68-battle-action-table-match.md](notes/class2-d57b68-battle-action-table-match.md).
See also [class2-d57b68-early-entry-name-crosswalk.md](notes/class2-d57b68-early-entry-name-crosswalk.md).
See also [class2-late-physical-special-family-c28f97-c2900b.md](notes/class2-late-physical-special-family-c28f97-c2900b.md).

## Working Names

- `C2:902C` = `RunAllTargetPhysicalFlavorWrapper`
- `C2:9033` = `RunFlavorOnlyNoOpTail`
- `C2:904E` = `RunLateMessageOnlyNoOpTail`

## Main result

This small tail is not one more meaningful gameplay family.

The safest current split is:

- `C2:902C` = thin all-target wrapper over the already-mapped `C2:8651` physical family
- `C2:9033` = pure flavor-only no-op tail reused by a long run of enemy `none/other` and item `none/item` rows
- `C2:9039`, `903C`, `903F`, `9042`, `9045`, `9048`, `904B`, and `904E` = tiny no-op tails that leave behavior entirely to the message side or to upstream script selection

So this region is mostly a table-side parking lot for presentation-only or metadata-only rows, with one real wrapper at `902C`.

## `C2:902C` is the all-target physical wrapper

`C2:902C` is straightforward locally:

- `JSL C28651`
- `RTL`

That makes it a direct all-target wrapper over the already-mapped `C2:8651` physical damage family.

The live table anchors fit that exactly:

- entry `117` -> `C2:902C` -> enemy all-target piercing-physical -> tornado text `EF:80C4`
- entry `118` -> `C2:902C` -> enemy all-target piercing-physical -> gigantic-blast text `EF:80E4`

So `902C` should not be treated as a separate mechanics family. It is just the all-target reuse of the broader `8651` physical common path.

## `C2:9033` is the big flavor-only tail

`C2:9033` is just:

- `REP #$31`
- `RTL`

That means any rows pointing at it have no gameplay-side second-pointer effect at all. Their behavior is carried entirely by the message pointer or by other surrounding controller state.

This one stub is reused unusually widely:

- enemy `none/other` rows `119..134`, each with taunt, smile, laughter, muttering, wobbling, staring, or similar text-only flavor
- item `none/item` rows `186..188`
- additional late `other` rows like `257`, `260..266`

That is strong enough to treat `9033` as the main flavor-only tail for message-driven battle rows.

## The neighboring no-op tails are real but smaller

The surrounding addresses `9039..904E` are also tiny `REP/RTL` stubs.

Useful local anchors:

- `C2:9039` -> strongest current local fit for the default no-effect or placeholder tail
  - used by early rows `0..3`
  - reused by some later none-target item or other rows such as `258`
- `C2:903C` -> isolated no-op tail used by early row `9`
- `C2:903F`, `9042`, `9045`, `9048`, `904B`, `904E` -> tiny message-only tails used by the later row run `251..256`

These should not be overnamed. Locally they really are just address-distinct no-op tails chosen by the table.

## Current safest interpretation

The safest current interpretation is:

- `902C` is a real thin wrapper, but only over `8651`
- `9033` is the main late flavor-only no-op tail
- `9039..904E` are mostly table-distinct no-op selectors for rows whose entire visible behavior comes from text or higher-level control flow

## What is still open

Still open:

- whether `9039` deserves a slightly stronger symbolic name than default no-effect tail
- whether the later `251..256` run should be grouped by message semantics in a separate battle-flavor note
- whether any upstream controller path uses the distinction among `9039`, `903C`, `903F`, `9042`, `9045`, `9048`, `904B`, and `904E` for bookkeeping rather than pure table identity

## Current takeaway

The safest current takeaway is:

- the late table is getting cleaner partly because some rows really do have no gameplay handler
- `9033` and its neighbors are not unresolved mechanics; they are mostly no-op flavor tails
- `902C` is the only real action wrapper in this little block, and it belongs with `8651`, not as a standalone family
