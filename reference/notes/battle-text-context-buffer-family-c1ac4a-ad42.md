# Battle Text Context Buffer Family `C1:AC4A .. AD42`

This note captures the current best local model for the small bank-`01` helper cluster around `C1:AC4A`, `C1:ACA1`, `C1:ACF8`, `C1:AD0A`, `C1:AD26`, and `C1:AD42`.

See also [battle-text-entry-family-c1dc1c-dd7c.md](notes/battle-text-entry-family-c1dc1c-dd7c.md).
See also [class2-reflected-hit-text-context.md](notes/class2-reflected-hit-text-context.md).
See also [class2-c1acf8-substitution-byte-family.md](notes/class2-c1acf8-substitution-byte-family.md).
See also [interaction-result-consumers.md](notes/interaction-result-consumers.md).
See also [level-up-stat-gain-text-family-c1d15b-d76d.md](notes/level-up-stat-gain-text-family-c1d15b-d76d.md).
See also [battle-choice-text-family-c1b2ec-b997.md](notes/battle-choice-text-family-c1b2ec-b997.md).

## Main result

This neighborhood now reads as two small helper families that happen to touch each other in memory:

- battle-text context builders and substitution slots at `AC4A .. AD26`
- a separate interaction-result class reader at `AD42`

Source-scaffold promotion:

- `C1:AC4A..AD7D` is now decoded source, including the separate `AD42`
  interaction-result reader that follows the battle-text substitution helpers.
- `src/c1/c1_ac4a_build_battle_attacker_name_buffer.asm` through
  `src/c1/c1_ad42_get_front_interaction_result_class.asm` assemble as
  source segments in `build/c1-build-candidate-ranges.json`.
- The substitution leaves now name their processor-width masks, caller-frame
  alias shifts, local return slots, and `$9D11/$9D12/$9D14` byte/pointer
  payload slots directly in source.
- Validation remains clean: `C1 byte-equivalence: OK, 172 module(s), 0
  mismatch(es).`

## Working Names

- `C1:AC4A` = `BuildBattleAttackerNameBuffer`
- `C1:AC9B` = `GetBattleAttackerNameBufferBase`
- `C1:ACA1` = `BuildBattleTargetNameBuffer`
- `C1:ACF2` = `GetBattleTargetNameBufferBase`
- `C1:ACF8` = `StageBattleTextSubstitutionByte`
- `C1:AD02` = `ReadBattleTextSubstitutionByte`
- `C1:AD0A` = `StageBattleTextSubstitutionPointer`
- `C1:AD26` = `LoadBattleTextSubstitutionPointer`
- `C1:AD42` = `GetFrontInteractionResultClass`

That is cleaner than the older blended wording where the whole strip was treated as vague battle or interaction glue.

## `C1:AC4A` and `C1:ACA1` are counted-copy live buffer builders

These two routines are near-perfect twins.

The strongest current local read is:

- `C1:AC4A` builds the live attacker-name text buffer at `$9CD7`
- `C1:ACA1` builds the live target-name text buffer at `$9CF5`

Shared structure:

- save incoming `A` and `X`
- seed destination pointer `$0E/$10` to either `$9CD7` or `$9CF5`
- seed source pointer `$12/$14` from the incoming caller pointer
- call `C0:8EED` with the incoming `X`-count through `TXA`
- write a terminator byte at `dest + X`
- invalidate the paired cached-state word at either `$9658` or `$965A`

That makes them stronger than abstract name-refresh helpers. They are active buffer builders for two concrete live text slots.

The nearby tiny helpers also line up with that split:

- `C1:AC9B` returns `$9CD7`
- `C1:ACF2` returns `$9CF5`

So the safest current naming is:

- `C1:AC4A` = `Build_BattleAttackerNameBuffer`
- `C1:ACA1` = `Build_BattleTargetNameBuffer`
- `C1:AC9B` / `C1:ACF2` = base-address getters for those buffers

## `C1:ACF8` and `C1:AD02` are the one-byte substitution slot

This part stays simple and strong:

- `C1:ACF8` stores the low byte of `A` to `$9D11`
- `C1:AD02` reads that byte back from `$9D11`
- `C1:DD7C` is the far wrapper for the setter

That is the same generic one-byte battle-text substitution slot already described in [class2-c1acf8-substitution-byte-family.md](notes/class2-c1acf8-substitution-byte-family.md).

## `C1:AD0A` and `C1:AD26` are the companion pointer substitution slot

The companion pair is now just as clean locally:

- `C1:AD0A` stores the caller pointer pair from `$1C/$1E` into `$9D12/$9D14`
- `C1:AD26` reads `$9D12/$9D14` back into `$06/$08` and mirrors it into `$14/$16`

That makes the cluster symmetry healthier:

- `$9D11` = current one-byte substitution slot
- `$9D12/$9D14` = current pointer substitution slot

And it matches the display-text siblings already mapped around `C1:7AE3` and `C1:7AF3`.

## Caller-side shape supports the battle-text reading

The direct callers line up well with the current battle-text model:

- `C1:B2EC`, `C1:B86E`, `C1:DBF9`, and `C1:DD72` call `AC4A`, with the new [battle-choice-text-family-c1b2ec-b997.md](notes/battle-choice-text-family-c1b2ec-b997.md) note now covering the strongest ordinary battle-side `B2xx/B8xx` caller cluster
- `C1:B339`, `C1:B450`, `C1:B88C`, `C1:B997`, `C1:D15B`, and `C1:DD78` call `ACA1`, with `B450/B88C/B997` now locally tied to the same battle choice-text family
- `C1:D177`, `D204`, `D28C`, `D31B`, `D3A5`, `D48D`, `D575`, `D606`, `D695`, `D76D`, `DCA4`, `DD9A`, and `ED22` call `AD0A`
- `C1:7AE3` and `C1:7EED` call `AD26`

The important local pattern is that battle-side display helpers first refresh one or both live name buffers, then seed one-byte or pointer substitution state, then dispatch through the ordinary text-display path. The new [level-up-stat-gain-text-family-c1d15b-d76d.md](notes/level-up-stat-gain-text-family-c1d15b-d76d.md) note is now the cleanest ordinary runtime example of that pattern.

## `C1:AD42` is not part of the battle-text side

`C1:AD42` sits right next to the substitution-slot helpers, but its body belongs to the interaction-result side instead.

The strongest current local read is:

- call `C0:4279`
- read `$5D62`
- return `0` for `0`, `#$FFFF`, or `#$FFFE`
- otherwise index `CF:8985` by `result * 17`
- return record byte `+0`

So `C1:AD42` is best treated as a compact interaction-result class reader over the front-facing probe result, not as a battle-text helper.

The safest current name is:

- `C1:AD42` = `Get_FrontInteractionResultClass`

That also explains why its only direct local caller is not in the `DCxx/DDxx` battle-text strip.

## Current safest interpretation

The safest overall split is:

- `AC4A/ACA1` = counted-copy builders for the live attacker/target name buffers
- `ACF8/AD02` = one-byte battle-text substitution slot
- `AD0A/AD26` = pointer battle-text substitution slot
- `AD42` = separate front-interaction result-class reader over `$5D62 -> CF:8985`

That makes this region much easier to reuse in later notes without blurring battle-text state and interaction-state helpers together.


