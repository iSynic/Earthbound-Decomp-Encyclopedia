# Class2 Reflected Hit Text Context

This note tightens the interpretation of the reflected-hit rebuild tail, especially `C1:DD70`, `C1:DD76`, `C1:AC4A`, `C1:ACA1`, `C1:ACF8`, and `C1:AD0A`.

See also `notes/class2-reflected-hit-context-rebuild.md`.
See also `notes/class2-psi-thunder-reflection-branch.md`.
See also [class2-c1acf8-substitution-byte-family.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-c1acf8-substitution-byte-family.md).

## Current strongest claim

The rebuild path behind reflected Thunder now looks much more like battle textbox-context rebuild than generic battle-state rebuild.

The strongest local-plus-reference reading is:

- `C2:7E8A` swaps reflected attacker and target rows
- `C2:3BCF` / `C2:3D05` rebuild the supporting per-side text buffers, including cleared work buffers at `A983` and `A99E`
- `C1:DD70` / `C1:DD76` then refresh battle textbox placeholder context, especially attacker name, target name, and substitution-state slots

This still leaves some buffer details open, but it is a better model than the earlier generic "context rebuild" wording.

## Why the `C1` tail now looks textbox-related

The key clue came from the `ebsrc` bank layout and call sites:

- `REDIRECT_C1ACF8` is called from battle code like `psi_shield_nullify.asm`, `main_battle_routine.asm`, and `instant_win_handler.asm`
- those call sites pass values like `current_action_argument` and dropped-item ids
- the local body at `C1:ACF8` simply stores an 8-bit value into `$9D11`
- the matching helper `C1:AD02` reads that byte back

That makes `C1:ACF8` read much more like "set the current one-byte textbox substitution value" than like a gameplay-state mutator.

## `C1:AC4A` and `C1:ACA1` line up with attacker/target name buffers

The `ebsrc` include ordering is especially useful here:

- `C1AC4A` sits next to `battle/return_battle_attacker_address.asm`
- `C1ACA1` sits next to `battle/return_battle_target_address.asm`

The small reference stubs there return:

- `BATTLE_ATTACKER_NAME`
- `BATTLE_TARGET_NAME`

The legacy bytes for `C1:ACA1` line up with that interpretation cleanly:

- it copies data into `7E:9CF5 + X`
- null-terminates the copied data
- stores `0xFFFF` to `$965A`

So the safest current reading is:

- `C1:AC4A` seeds or refreshes the attacker-name text buffer and its companion metadata
- `C1:ACA1` seeds or refreshes the target-name text buffer and its companion metadata

That is exactly the kind of state a reflected-hit rebuild would need after swapping acting and receiving sides.

The low-level helpers under those routines are now clearer too:

- `C0:8EED` is a simple counted copy helper used to copy source text into those buffers
- `C0:8EFC` is a simple fill helper used elsewhere in the same rebuild family to clear working buffers before they are repopulated

That makes the battle-text interpretation more concrete instead of purely positional.

## `C1:ACF8` and `C1:AD0A` look like textbox substitution setters

The local bytes for these helpers are compact enough to trust their broad roles:

- `C1:ACF8` stores an 8-bit value into `$9D11`
- `C1:AD02` reads that 8-bit value back from `$9D11`
- `C1:AD0A` stores a 16-bit pointer pair into `$9D12/$9D14`

Given the reference call sites, the safest current reading is:

- `$9D11` is a current action-argument, item-id, or enemy-id-like substitution byte used by battle textbox expansion
- `$9D12/$9D14` hold a companion pointer used by the same textbox-expansion family

This is a much better fit than treating those addresses like generic battle controller state.

## What this implies about `C1:DD70` and `C1:DD76`

The local tails around `C1:DD70` and `C1:DD76` call the helpers above in a tight cluster.

Current safest reading:

- they refresh attacker and target name context through `C1:AC4A` / `C1:ACA1`
- they refresh one-byte substitution state through `C1:ACF8`
- they preserve or restore a pointer pair through `C1:AD0A`
- they then continue into the nearby textbox-processing path rather than into direct damage logic

That makes the reflected-hit rebuild much easier to describe: it is rebuilding the battle text and naming context so later messages describe the reflected attacker and target correctly.

## How this sharpens the reflected Thunder model

The reflected Thunder path now reads like this:

1. `C2:966B` detects the Franklin-Badge-like special case.
2. It displays the reflection message and marks reflected PSI state.
3. `C2:7E8A` swaps `$A970/$A972`.
4. `C2:3BCF` / `C2:3D05` rebuild the side-local support buffers.
5. `C1:DD70` / `C1:DD76` refresh battle textbox context, especially attacker name, target name, and substitution state.
6. Later, `C2:94CE` finishes shield weakening and cleanup.

That explains why the reflected path needs more than a simple attacker/target swap: the message and placeholder context also has to be rebuilt so the reflected hit reads correctly to the player.

## Current safest takeaway

The safest current takeaway is:

- the reflected-hit rebuild path is now best understood as a battle textbox-context rebuild layered on top of the battle-side swap
- `A983` and `A99E` are best read as cleared output work buffers used by that rebuild, not as static source templates
- `C1:AC4A` and `C1:ACA1` likely refresh attacker and target name buffers
- `C1:ACF8` sets the current one-byte substitution value for battle textbox expansion
- `C1:AD0A` likely stores a companion substitution pointer

That is the clearest "what is this machinery for" answer we have had yet for the `C2:7E8A -> C2:3BCF/C2:3D05 -> C1:DD70/DD76` chain.

## Best next target

The best next move is to tighten the remaining ambiguous buffer pieces:

- what `A983` and `A99E` specifically encode,
- what `$5E77` and `$5E78` gate,
- and whether `C1:DD70` versus `C1:DD76` correspond cleanly to attacker-side and target-side textbox state rather than a more mixed split.
