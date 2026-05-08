# Class2 Enemy Text Pointer Consumers

This note tightens the `enemy_data::encounter_text_ptr` and `enemy_data::death_text_ptr` interpretation by comparing the local `D5:9589` field consumers against the `ebsrc` battle flow.

See also [class2-d59589-enemy-data-crosswalk.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-d59589-enemy-data-crosswalk.md).
See also [class2-reflected-hit-text-context.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-reflected-hit-text-context.md).
See also [class2-reflected-hit-side-token-consumers.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-reflected-hit-side-token-consumers.md).

## Main result

The `+0x2D` and `+0x31` fields in the `D5:9589` enemy records now look much more specific than generic script pointers.

The safest current reading is:

- `+0x2D` is the enemy battle-start or encounter text pointer
- `+0x31` is the enemy KO or death text pointer

That is still a crosswalk, not a byte-perfect local label proof, but the reference call structure fits our local field behavior unusually well.

## Reference: battle-start encounter text

In `refs/ebsrc-main/ebsrc-main/src/battle/main_battle_routine.asm`, the opening battle flow does the following:

1. set the current attacker to the first enemy battler slot
2. call `FIX_ATTACKER_NAME`
3. load the first enemy id from `ENEMIES_IN_BATTLE_IDS`
4. scale by `.SIZEOF(enemy_data)`
5. add `enemy_data::encounter_text_ptr`
6. dereference the resulting far pointer
7. call `DISPLAY_IN_BATTLE_TEXT`

That is a very clean behavioral match for a per-enemy appearance or encounter message.

The important structural clue is the order: attacker-name context is prepared before the text pointer is displayed. That makes this field part of the same battle text system that uses the enemy-name formatting helpers.

## Reference: KO death text

In `refs/ebsrc-main/ebsrc-main/src/battle/ko_target.asm`, the enemy KO path does the following for a live enemy target:

1. load the target's enemy id from `battler::id`
2. scale by `.SIZEOF(enemy_data)`
3. add `enemy_data::death_text_ptr`
4. dereference the resulting far pointer
5. call `DISPLAY_IN_BATTLE_TEXT`
6. only after that, clear `battler::consciousness`

That is a very strong fit for a per-enemy defeat or death message.

Again, the placement is informative: the death text is emitted in the same KO flow where attacker and target name context is still meaningful.

## What this says about the local `D5:9589` consumers

Our local note chain already established these field reads:

- `C2:4F0D` consumes `D5:9589 + 0x2D`
- `C2:7680+` consumes `D5:9589 + 0x31`
- both ultimately dispatch through `C1:DC1C`

Before the enemy-data crosswalk, the safest phrasing was "textbox or script-data pointer" and "late text or presentation pointer."

After the crosswalk, the safer and more specific phrasing is:

- the local `+0x2D` consumer is very likely using enemy encounter text
- the local `+0x31` consumer is very likely using enemy death text

I am still keeping the wording slightly cautious because we have not yet identified the local `C1:DC1C` body one-for-one with reference `DISPLAY_IN_BATTLE_TEXT`. But behaviorally, the fit is now strong.

## Why this matters for the name and article work

This bridge helps the late text-formatting notes too.

The reference battle-start flow explicitly does `FIX_ATTACKER_NAME` before the encounter text is displayed. That means enemy-specific text pointers and enemy-name/article formatting are not separate systems that merely happen to live nearby; they are part of the same battle text pipeline.

Combined with the local side-token work:

- enemy record byte `+0x00` now looks like `enemy_data::the_flag`
- enemy record byte `+0x5B` now looks like `enemy_data::row`
- the late bank-`C3` text path chooses `"The "` versus `"the "`
- the nearby bank-`C4` text cluster includes `To the Front Row` and `the Back Row`

That makes it materially safer to read the late formatter as enemy-name and row-aware battle text formatting rather than some generic token pass.

## Sample data alignment

The reference `enemies.asm` entries also fit the two-pointer story naturally.

For early entries:

- `Insane Cultist` has a nontrivial encounter-text pointer and a distinct death-text pointer
- `Dept. Store Spook` does too
- `Armored Frog` and `Bad Buffalo` do as well

That matches the local expectation that these fields carry per-enemy message payloads rather than one shared hardcoded pointer family.

## Current safest takeaway

The safest takeaway is:

- `D5:9589 + 0x2D` is best read as the enemy's battle-start text pointer
- `D5:9589 + 0x31` is best read as the enemy's KO or death text pointer
- the local `C1`/`C2`/`C3` name and article machinery is therefore very likely upstream or adjacent support code for those same enemy battle messages

## Best next target

The best next move is to tighten the local `C1:DC1C` dispatch path further, or to connect one of these pointer consumers directly to the local attacker-name or target-name rebuild helpers so we can replace the remaining cautious wording with a firmer local label.

## Update: local battle-text dispatch stack

A later cross-check tightened the `C1` side of this path.

The strongest current model is now:

- `C1:86B1` is the generic textbox-data processor
- local `C1:DC1C` is very likely the battle-text display entry or a close wrapper in the `DISPLAY_IN_BATTLE_TEXT` family
- `C1:DD70` / `C1:DD76` are nearby battle-text context refresh helpers rather than unrelated utilities

The key reason this got stronger is the `ebsrc` bank-`C1` symbol order. `DISPLAY_IN_BATTLE_TEXT` and `DISPLAY_IN_BATTLE_TEXT_NO_PROMPT` are exported immediately before `UNKNOWN_C1DCCB` / `UNKNOWN_C1DD5F`, which is exactly the local address neighborhood we have been using for `C1:DC1C` and the surrounding name-refresh helpers.

That means the local `+0x2D` and `+0x31` enemy pointer consumers are now best read as battle-message dispatch through a battle-text wrapper, not as generic script dispatch.

See also [class2-battle-text-dispatch-stack.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/class2-battle-text-dispatch-stack.md).
