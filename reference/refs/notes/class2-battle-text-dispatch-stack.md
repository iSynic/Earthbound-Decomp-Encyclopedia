# Class2 Battle Text Dispatch Stack

This note captures the current best model for the local battle-text dispatch path centered on `C1:DC1C`, and how it relates to the enemy text-pointer and name-formatting work.

See also [class2-enemy-text-pointer-consumers.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-enemy-text-pointer-consumers.md).
See also [class2-reflected-hit-text-context.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-reflected-hit-text-context.md).
See also [class2-reflected-hit-side-token-consumers.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-reflected-hit-side-token-consumers.md).
See also [battle-action-stat-change-family-c2b2e0-b5d7.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-action-stat-change-family-c2b2e0-b5d7.md).

## Main result

We still do not have a byte-for-byte local proof of the exact `C1:DC1C` routine body, but the current evidence is now strong enough to describe a likely dispatch stack.

The safest current stack model is:

- `C1:86B1` is the generic textbox-data processor
- `C1:DC1C` is very likely a battle-text dispatch wrapper or entry in the `DISPLAY_IN_BATTLE_TEXT` family
- `C1:DC66` is now locally strong as a companion two-input battle-text wrapper that first stages a secondary pointer-like input through `C1:AD0A`, then displays the primary pointer through the same `C1:86B1` path; reference-side battle-action call patterns are now strong enough to promote it as the final match for `DISPLAY_TEXT_WAIT`
- the newly mapped `C2:B2E0` battle stat-change family gives `C1:DC66` another strong local caller bridge, because its direct IQ/guts/speed/vitality/luck-up leaves all stage `{delta}` through `DC66` with fixed `C8:F7xx/F8xx` message pointers
- `C1:DCCB` now looks best as `INITIALIZE_PARTY_BATTLE_START_STATE`, an adjacent party-side battle-start initializer rather than another display entry
- `C1:DD5F` is now best treated locally as `BATTLE_DISPLAY_CLOSE_AND_SYNC_WAIT`, a richer close/reset/sync-and-wait wrapper rather than a plain one-stage wait helper
- `C1:DD70` and `C1:DD76` are nearby battle-text context refresh helpers, especially for attacker and target naming plus substitution state

That is still slightly cautious wording, but it is tighter and more useful than treating `C1:DC1C` as an anonymous pointer sink. See also [battle-text-entry-family-c1dc1c-dd7c.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-text-entry-family-c1dc1c-dd7c.md). See also [battle-text-entry-tail-dd82-dd9f.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/battle-text-entry-tail-dd82-dd9f.md).

## Anchor 1: `C1:86B1` is the generic textbox processor

The legacy reference gives us one solid local anchor:

- `C1:86B1` is labeled `EB_ProcessTextboxData` in `Routine_Macros_EB.asm`

That matters because several of our earlier local notes already converged on a `C1:DC1C -> C1:86B1` relationship when following pointer-based message dispatch.

So the generic bottom of the stack is no longer in doubt. The open question is what kind of wrapper `C1:DC1C` is.

## Anchor 2: `ebsrc` symbol ordering in bank `C1`

The `ebsrc` `bank01` symbol exports are in ascending address order, and the relevant stretch is:

- `DISPLAY_IN_BATTLE_TEXT`
- `DISPLAY_IN_BATTLE_TEXT_NO_PROMPT`
- `DISPLAY_TEXT_WAIT`
- `UNKNOWN_C1DCCB`
- `UNKNOWN_C1DD5F`
- redirect helpers for `C1:AC4A`, `C1:ACA1`, and `C1:ACF8`

That is a strong neighborhood clue.

Our local work had already been treating `C1:DC1C` as the main pointer-dispatch target for battle-style message payloads. The `ebsrc` symbol ordering now makes it materially safer to say that local `C1:DC1C` is probably the battle text display entry or a very close wrapper within that same family.

I am still stopping short of an absolute rename because we have not matched the body instruction-for-instruction yet.

## Anchor 3: the enemy pointer consumers fit `DISPLAY_IN_BATTLE_TEXT`

The enemy-data crosswalk made two local pointer fields much more specific:

- `D5:9589 + 0x2D` is very likely `enemy_data::encounter_text_ptr`
- `D5:9589 + 0x31` is very likely `enemy_data::death_text_ptr`

In the `ebsrc` reference:

- battle start fixes attacker name and then calls `DISPLAY_IN_BATTLE_TEXT` on `encounter_text_ptr`
- enemy KO calls `DISPLAY_IN_BATTLE_TEXT` on `death_text_ptr` before clearing the enemy battler

Locally, the same two fields are consumed by:

- `C2:4F0D` for `+0x2D`
- `C2:7680+` for `+0x31`

and both ultimately dispatch through `C1:DC1C`.

That is the strongest behavioral argument we currently have that `C1:DC1C` belongs to the local battle-text display family rather than being a generic non-battle text hook.

## Anchor 4: nearby name-context rebuild helpers

The reflected-hit notes already established a second nearby family:

- `C1:DD70` / `C1:DD76` refresh battle textbox context
- `C1:AC4A` and `C1:ACA1` line up best with attacker-name and target-name buffer refresh
- `C1:ACF8` and `C1:AD0A` look like substitution or argument setter helpers used by textbox expansion

The important point here is adjacency of purpose, not just address.

`ebsrc` exports `DISPLAY_IN_BATTLE_TEXT` in the same region immediately before `UNKNOWN_C1DCCB` / `UNKNOWN_C1DD5F`, and our local analysis already put the name refresh helpers right after the `DCxx` display family. The new family note also makes the local middle strip cleaner: `DC1C` and `DC66` now look like the main display-entry pair, `DCCB` looks like a party-side battle-state priming helper, `DD3B .. DD53` look like the short redirect strip, `DD5F` looks like a shared wait-and-sync helper, and `DD70 / DD76 / DD7C` are the battle-text context refresh redirects. That makes the overall bank-`C1` battle-text layout read coherently:

1. battle-text display entry
2. nearby battle-text support helpers
3. attacker/target name refresh redirects
4. substitution-state refresh helpers

## Current safest model for the local stack

The best current local model is:

1. some battle-side caller selects or loads a text pointer
2. the pointer is dispatched through `C1:DC1C`
3. that path eventually feeds the generic textbox processor rooted at `C1:86B1`
4. nearby helpers in the `C1:DD70` / `C1:DD76` family refresh attacker-name, target-name, and substitution state so the printed battle text expands correctly

That is a much cleaner stack description than our older "script dispatch" wording.

## What this changes in the existing notes

This update sharpens several older phrases:

- local `C1:DC1C` should now be read as a likely battle-text display wrapper, not just a generic script sink
- `D5:9589 + 0x2D` and `+0x31` now look like battle message pointers displayed through that wrapper
- the reflected-hit rebuild family now looks even more strongly like support code for battle text context rather than a mixed gameplay-text hybrid

## Current safest takeaway

The safest takeaway is:

- `C1:86B1` is the generic textbox-data processor
- local `C1:DC1C` is very likely the battle-text display entry or a close wrapper in the `DISPLAY_IN_BATTLE_TEXT` family
- `C1:DD70` / `C1:DD76` then refresh attacker or target naming context and related substitution state around that display flow

## Best next target

The best next move is to connect one concrete local `C1:DC1C` call site to one concrete `C1:DD70` / `C1:DD76` refresh path, or to pin down whether `C1:DC1C` and `DISPLAY_IN_BATTLE_TEXT` are the exact same address rather than just the same local family.

## Update: concrete local caller bridges

A later local pass tightened this note from both ends.

The strongest concrete local bridge now is `C2:4F00+`:

- it begins with `JSL C2:3BCF`
- our earlier notes already tie `C2:3BCF` to `C1:DD70`
- it then loads `enemy_data::encounter_text_ptr` from `D5:9589 + 0x2D`
- it copies that far pointer into `$0E/$10`
- and it dispatches the result through `C1:DC1C`

That gives us one real local chain from context refresh into display dispatch:

- `C2:3BCF -> C1:DD70`
- then `C1:DC1C` on the staged enemy encounter-text pointer

A second concrete local path at `C2:7680+` now shows the same `$0E/$10 -> C1:DC1C` convention for `enemy_data::death_text_ptr` from record `+0x31`.

See also [class2-concrete-battle-text-call-paths.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-concrete-battle-text-call-paths.md).

## Update: companion-side concrete bridge

A later local pass found the missing `DD76` companion bridge.

The clearest path so far is `C2:4F62+`:

- it begins with `JSL C2:3D05`
- our earlier notes already tie `C2:3D05` to `C1:DD76`
- it then stages hardcoded far pointers like `EF:843F`, `EF:8444`, and `EF:8445` in `$0E/$10`
- and it dispatches each one through `C1:DC1C`

So the local battle-text bridge story is now balanced on both sides:

- `C2:3BCF -> C1:DD70 -> C1:DC1C`
- `C2:3D05 -> C1:DD76 -> C1:DC1C`

That is the strongest local evidence yet that the `DD70/DD76` pair really is adjacent battle-text context setup for the `DC1C` display wrapper.

See also [class2-concrete-battle-text-call-paths.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-concrete-battle-text-call-paths.md).

## Update: target-side start-of-battle status messages

A later pass identified the hardcoded `EF` message family used after the `C2:3D05 -> C1:DD76` bridge.

Those pointers are not arbitrary:

- `EF:843F` = `EBATTLE0 + 0x0000` = `MSG_BTL_AT_START_NEMURI`
- `EF:8444` = `EBATTLE0 + 0x0005` = `MSG_BTL_AT_START_FUUIN`
- `EF:8445` = `EBATTLE0 + 0x0006` = `MSG_BTL_AT_START_HEN`

That makes `C2:4F62+` much more specific. It now looks like a target-side start-of-battle status-announcement path that:

- refreshes target-side battle text context through `C2:3D05 -> C1:DD76`
- then emits the asleep, sealed, and strange status messages through `C1:DC1C`

This is a strong local-plus-reference match for the `ebsrc` battle-start flow where target name is fixed and then those same three start-of-battle status messages are conditionally displayed.

See also [class2-concrete-battle-text-call-paths.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-concrete-battle-text-call-paths.md).
