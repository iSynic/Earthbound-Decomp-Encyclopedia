# Character Selection Prompt Cluster (`C1:1F8A-C1:242E`)

This note captures the current best local read of the unknown starts immediately before `text/character_select_prompt.asm`.

The reference include order is useful context: this region follows `move_cursor`, `selection_menu`, and a covered `C1:1F5A` helper, then leads into `C1:244C` and the named `character_select_prompt` include.

## Main result

`C1:1F8A..C1:242E` is a selection-prompt controller over two candidate lists:

Source-scaffold promotion:

- `C1:1F8A..2012` was already decoded source across the scratch, candidate
  byte read, and eligibility helpers.
- `C1:2012..2070`, `C1:2070..20D6`, `C1:20D6..21B8`,
  `C1:21B8..2362`, and `C1:2362..242E` are now decoded source in their
  matching `src/c1/` selection-prompt modules.
- The promoted source validates through the durable C1 scaffold:
  `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`
- The follow-on corridor `C1:242E..2BF3` (dispatch wrapper + character select
  prompt core) is now decoded source as well; see
  `notes/character-selection-prompt-dispatch-c1242e-c12bf3.md`.

## Working Names

- `C1:1F8A` = `ClearActiveSelectionPromptScratch`
- `C1:1FBC` = `ReadSelectionPromptCandidateByte`
- `C1:1FD4` = `IsSelectionPromptCandidateEligible`
- `C1:2012` = `FindNextSelectionPromptCandidate`
- `C1:2070` = `FindPreviousSelectionPromptCandidate`
- `C1:20D6` = `RefreshSelectionPromptCandidateText`
- `C1:21B8` = `RunTwoListCharacterSelectionPrompt`
- `C1:2362` = `RunSimpleSideSelectionPrompt`
- `C1:242E` = `DispatchCharacterSelectionPromptMode`
- `C4:35E4` = `ClearBattleTargetRowHighlightFlags`
- `C4:3657` = `SetBattleTargetRowHighlightFlags`

- list counts live at `$AD56` and `$AD58`
- list byte entries live at `$AD5A+` and `$AD6A+`
- the controller can scan forward or backward for the next valid candidate
- it can switch between the two lists when both are present
- it paints current selection text through the existing print/string helpers
- it accepts, cancels, or closes the prompt based on joypad state

The safest user-facing name is "character/party selection prompt cluster", with table names still cautious until the producers of the `$AD5A/$AD6A` lists are fully documented.

## Candidate and State Helpers

`C1:1F8A` clears a four-byte field in the current active window descriptor.

It resolves current focus through `$8958 -> $88E4 -> descriptor * $52`, then writes zero to the two words rooted at `$8687 + descriptor_offset`. This is likely a current selection or cursor scratch field attached to the active prompt descriptor.

`C1:1FBC` returns one byte from either candidate list.

Its inputs are:

- `A = 0` selects the `$AD5A` list
- `A != 0` selects the `$AD6A` list
- `Y` is the candidate index

It returns the selected byte zero-extended to 16 bits.

`C1:1FD4` is a candidate validity filter. In the ordinary case it returns `1`. In the special `A == 1` path, it inspects an entry in long table `D5:7B68+`, checks a type byte for `1`, then calls `C2:FAD2`; only when that call returns zero does the filter return `0`.

The exact table meaning is still open, but locally this helper is clearly a per-candidate eligibility predicate used by both forward and backward scans.

## Forward and Backward Scans

`C1:2012` scans forward through one of the two candidate lists.

It chooses count/base from `$AD56/$AD5A` or `$AD58/$AD6A`, then walks upward from the low end looking for the first entry greater than the supplied threshold and accepted by `C1:1FD4`. It returns the matching index or `FFFF`.

`C1:2070` is the reverse scan.

It chooses the same count/base pair, starts from the high end, walks downward, and returns the first entry lower than the supplied threshold and accepted by `C1:1FD4`. It also returns `FFFF` when no candidate matches.

Together, these are the "next valid candidate" and "previous valid candidate" primitives for the prompt controller.

## Selection Display Worker

`C1:20D6` refreshes the visible selection text for one list/index pair.

It sets up text/window state, prints a small fixed bank-`04` string through `C1:0EFC`, maps the selected index into battle/party-facing helpers (`C2:3E8A`, `C3:E75D`, `C1:AC9B`), then prints either a candidate-specific string derived from `$AD7A/$AD82` and `$9FC9` or one of two fallback strings at `C4:54F5` / `C4:5502`. It finishes by refreshing text state through `C3:E4CA`.

The exact display labels still need table naming, but this routine is visibly the "paint current candidate" worker for the prompt.

## Main Prompt Controllers

`C1:21B8` is the fuller two-list selection controller.

It chooses an initial active list from `$AD56/$AD58` and `$A97A`, paints the current candidate through `C1:20D6`, then loops through `C1:2DD5` and `C1:2E42` while reading `$006D`:

- `$0800` and `$0400` switch between lists when the opposite list exists
- `$0200` uses `C1:2070` to move backward, first in the current list and then in the opposite list
- `$0100` uses `C1:2012` to move forward, first in the current list and then in the opposite list
- `$00A0` accepts and returns a 1-based combined candidate index
- `$A000` can cancel/back out when the incoming mode permits it

On selection or cancel it closes the focused window through `C1:0084` and returns the selected value, or `0` for the cancel path.

`C1:2362` is a simpler two-choice/list-side prompt controller.

It starts from whichever list is present, calls `C4:3657` and `C1:20D6` to display that side, then handles left/right switching and accept/cancel with a smaller state machine. It also closes the focused window before returning.

The called bank-`04` helper pair now has a clearer contract:

- `C4:3657` closes any previous side through `C4:35E4`, stores the selected side in `$89CE`, walks either `$AD7A/$AD56` or `$AD82/$AD58`, maps each battler id through stride `#$004E`, and sets byte `$9FF6 + battler*#$4E = 1`
- `C4:35E4` walks the side currently stored in `$89CE`, clears the same `$9FF6` highlight bytes, clears `$ADA2`, resets `$89CE` to `FFFF`, and marks redraw through `$9623`

So `$89CE` is the active highlighted target-row side, `$ADA2` acts as a "row highlight active" latch, and `$9FF6` is the per-battler byte that the renderer sees for the highlighted set. The note still keeps the row names cautious because the `$AD7A/$AD82` producers remain the stronger authority for front/back naming.

`C1:242E` is a wrapper that chooses between the two prompt controllers:

- when incoming `X` is nonzero, it calls `C1:2362`
- when incoming `X` is zero, it calls `C1:21B8`

That makes `C1:242E` the local dispatch wrapper for selection-prompt mode.

## Practical Conclusion

The unknown starts `C1:1F8A`, `C1:1FBC`, `C1:1FD4`, `C1:2012`, `C1:2070`, `C1:20D6`, `C1:21B8`, `C1:2362`, and `C1:242E` are now locally accounted for as the support layer and controllers for the character/party selection prompt, with `C1:1F8A..242E` promoted into source-backed scaffold form.

The remaining uncertainty is not their structure; it is the exact semantic names of the `$AD5A/$AD6A` candidate lists and the `D5:7B68` eligibility metadata.
