# Battle Text Entry Tail `C1:DD82 .. DD9F`

This note captures the current best local model for the small tail immediately after the better-understood `C1:DC1C .. DD7C` battle-text entry family.

See also [battle-text-entry-family-c1dc1c-dd7c.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-text-entry-family-c1dc1c-dd7c.md).
See also [class2-battle-text-dispatch-stack.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battle-text-dispatch-stack.md).
See also [battle-text-display-mode-latch-964d.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-text-display-mode-latch-964d.md).

## Main result

The local `DD82 .. DD9F` tail now looks like a small pair of battle-text-adjacent entry helpers rather than random spillover from the next subsystem.

The safest current split is:

- `C1:DD82`
  - context-only pointer setter through `C1:AD0A`
- `C1:DD9F`
  - table-selected battle-action text wrapper with explicit mode `1`, best named locally as `DISPLAY_CURRENT_ACTION_TABLE_TEXT_MODE1`, and now promoted as the best final match for reference `DISPLAY_IN_BATTLE_TEXT_NO_PROMPT`

I am intentionally keeping the symbolic identities cautious here. The `ebsrc` tree still exports `UNKNOWN_C1DD9F`, and we do not yet have a clean reference-backed name for `C1:DD82` at all.

## `C1:DD82` as a context-only setter

The local body of `C1:DD82` is very small:

- copies caller pointer pair from `$20/$22` into local `$06/$08`
- stages that pair into `$0E/$10`
- calls `C1:AD0A`
- returns without invoking `C1:86B1`

That makes the safest current wording:

- `C1:DD82` is a context-only companion setter for the same pointer-like state that `C1:DC66` commits through `C1:AD0A -> $9D12/$9D14`
- unlike `C1:DC66`, it does not also dispatch visible text through `C1:86B1`

Direct local callers still have not been pinned cleanly by xref, JSL or JSR byte search, or the small set of surviving raw word hits. The remaining raw `DD82` word matches currently look like data-side noise rather than live control-flow users, so this should stay as a body-based interpretation for now.

## `C1:DD9F` as a one-pointer display wrapper with explicit mode `1`

`C1:DD9F` is much cleaner locally than its surviving reference placeholder name suggests.

The body is:

- copies caller pointer pair from `$20/$22` into local `$06/$08`
- loads `A = #$0001`
- calls `JSR $0036`
- stages the pointer into `$0E/$10`
- calls `C1:86B1`
- finishes through `JSR $003C`

That makes the safest current local read:

- `C1:DD9F` is another one-pointer battle-text-style display wrapper
- it is structurally very close to `C1:DC1C`
- the main local difference is that it always forces mode `1` through `JSR $0036` before dispatch

I am intentionally not promoting that mode to a user-facing label like `no prompt` yet. The reader side now shows that mode `1` takes a shorter abbreviated write path, but the final user-facing meaning still needs cleaner proof. See also [battle-text-display-mode-latch-964d.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-text-display-mode-latch-964d.md).

## Concrete local caller for `C1:DD9F`

`C1:DD9F` currently has one pinned direct caller:

- `C2:5C66`

At that caller:

- a far pointer is assembled from a `D5:7B68`-rooted table into `$0E/$10`
- `C1:DD9F` displays that pointer through the explicit mode-`1` wrapper
- the surrounding routine then continues into battle-side state and message selection logic

That is enough to treat `C1:DD9F` as live and meaningful, and it now supports a narrower local symbolic name:

- `C1:DD9F` is best treated locally as `DISPLAY_CURRENT_ACTION_TABLE_TEXT_MODE1`
- the currently pinned caller is the `main_battle_routine` path that selects a pointer from the `D5:7B68` battle-action table and displays it before the later target-resolution loop continues
- the wrapper's visible distinction is still the explicit mode-`1` write before dispatch, not a fully proved user-facing `no_prompt` meaning

The reference side is still useful here as a caution marker rather than a naming shortcut:

- `ebsrc` still exports this body as `UNKNOWN_C1DD9F`
- one of its visible battle callers in `main_battle_routine.asm` is the same kind of table-driven action-text path we see locally at `C2:5C66`

The reference-side picture is now strong enough to promote the export match too. Once `DISPLAY_TEXT_WAIT` is assigned to `C1:DC66`, the remaining named export `DISPLAY_IN_BATTLE_TEXT_NO_PROMPT` points directly at `C1:DD9F`, and the local caller behavior supports it: `C2:5C66` calls `DD9F`, then immediately takes over the manual `WINDOW_TICK / C2EACF` wait loop itself instead of relying on the wrapper to own the whole display-and-wait sequence. So the healthiest final mapping is:

- local behavioral name: `DISPLAY_CURRENT_ACTION_TABLE_TEXT_MODE1`
- best final reference/export match: `DISPLAY_IN_BATTLE_TEXT_NO_PROMPT`

## Safest current interpretation

The safest current summary is:

- `C1:DD82` is a context-only pointer setter through `C1:AD0A`
- `C1:DD9F` is best treated locally as `DISPLAY_CURRENT_ACTION_TABLE_TEXT_MODE1`: a one-pointer display wrapper parallel to `C1:DC1C`, but specifically used on the current-action table path and forcing an explicit pre-display mode write through `JSR $0036`
- `C1:DD82` remains the real unresolved tail helper here: locally meaningful by body, but still without a pinned live caller family

## What is still open

- the exact caller family for `C1:DD82`
- the exact semantic meaning of `JSR $0036` mode `1` in `C1:DD9F`
- whether the promoted `DISPLAY_IN_BATTLE_TEXT_NO_PROMPT -> C1:DD9F` mapping should eventually replace the narrower local helper-style name in summaries
