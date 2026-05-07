# Level-Up Stat Gain Text Family `C1:D15B .. D76D`

This note captures the current best local model for the bank-`01` level-up and stat-gain narration family that repeatedly uses `C1:ACA1` and `C1:AD0A` before dispatching fixed `EF:7A66..7B46` battle-text scripts.

See also [battle-text-context-buffer-family-c1ac4a-ad42.md](notes/battle-text-context-buffer-family-c1ac4a-ad42.md).
See also [equipped-item-derived-cache-family-c21857-c21e03.md](notes/equipped-item-derived-cache-family-c21857-c21e03.md).

## Main result

This `D1xx..D7xx` stretch is now much healthier as a concrete battle-text consumer family.

The surrounding `C1:D109..DC1C` routine is now promoted into byte-equivalent source at `src/c1/c1_d109_level_up_character_and_refresh_derived_stats.asm`, with the fixed message leaves below preserved as source labels.

Source polish follow-up (2026-05-06): the surrounding level-up source now names
the helper edges that feed the stat refresh and narration flow, including the
remaining IQ/Luck recalculators, max HP/PP random bump helper, battle-text mode
clear, focus/window close, attacker-name buffer, and text tick calls. The fixed
message leaves remain byte-equivalent source labels.

Source polish follow-up (2026-05-06): the three local exits that skip or finish
late PP/Sound Stone narration now jump through the named
`C1D8C7_ClearBattleTextDisplayModeAndReturn` contract instead of the raw
`$D8C7` target.

The strongest current local read is:

- `C1:ACA1` builds the live target-name buffer for the affected character
- each leaf computes a signed or unsigned stat delta
- `C1:AD0A` stages that delta through the pointer substitution slot at `$9D12/$9D14`
- the leaf then dispatches a fixed `EF:7A66..7B46` script through `C1:86B1`

So this family is a clean local bridge from character-record stat changes into the standard target-name-plus-amount battle-text formatting path.

## Shared local pattern

The repeated shape is unusually consistent:

1. resolve the current character row through the `#$005F` stride and build the target-name buffer with `C1:ACA1`
2. compute one stat delta from a base or derived pair
3. if the delta is positive, sign-extend or zero-extend it into `$0E/$10`
4. call `C1:AD0A` to stage that amount-like payload
5. load a fixed `EF:` message pointer into `$0E/$10`
6. dispatch through `JSL C186B1`

That makes this a very good caller family for the `ACA1` and `AD0A` helper cluster.

## Fixed message ladder

The fixed scripts now give the family a concrete message map:

- `EF:7A66` = level-up announcement with `PRINT_ACTION_TARGET_NAME` and `PRINT_ACTION_AMOUNT`
- `EF:7A7D` = offense went up by `{delta}`
- `EF:7A97` = defense went up by `{delta}`
- `EF:7AB1` = speed went up by `{delta}`
- `EF:7AC9` = guts went up by `{delta}`
- `EF:7AE0` = vitality went up by `{delta}`
- `EF:7AFB` = IQ went up by `{delta}`
- `EF:7B11` = luck went up by `{delta}`
- `EF:7B28` = maximum HP went up by `{delta}`
- `EF:7B46` = maximum PP went up by `{delta}`

That script ladder is the strongest reason this note can now stay local and concrete instead of reference-led.

## Current strongest leaf map

The current safest local anchors are:

- `C1:D15B / D177` = target-name build plus level-up announcement through `EF:7A66`
- `C1:D204` = offense delta message through `EF:7A7D`
- `C1:D28C` = defense delta message through `EF:7A97`
- `C1:D31B` = speed delta message through `EF:7AB1`
- `C1:D3A5` = guts delta message through `EF:7AC9`
- `C1:D48D` = vitality delta message through `EF:7AE0`
- `C1:D575` = IQ delta message through `EF:7AFB`
- `C1:D606` = luck delta message through `EF:7B11`
- `C1:D695` = maximum HP delta message through `EF:7B28`
- `C1:D76D` = maximum PP delta message through `EF:7B46`

I am still keeping the wider surrounding `D1xx..D8xx` control flow cautious, but this repeated message side is now in good shape.

## Working Names

- `C1:D15B` = `BuildLevelUpTargetNameAndAnnouncement`
- `C1:D177` = `StageLevelUpAnnouncementAmount`
- `C1:D204` = `PrintOffenseGainMessage`
- `C1:D28C` = `PrintDefenseGainMessage`
- `C1:D31B` = `PrintSpeedGainMessage`
- `C1:D3A5` = `PrintGutsGainMessage`
- `C1:D48D` = `PrintVitalityGainMessage`
- `C1:D575` = `PrintIqGainMessage`
- `C1:D606` = `PrintLuckGainMessage`
- `C1:D695` = `PrintMaximumHpGainMessage`
- `C1:D76D` = `PrintMaximumPpGainMessage`

## Why this matters for the helper cluster

This family gives the helper neighborhood a very concrete consumer:

- `C1:ACA1` is not just a probable target-name helper; it is the live target-name buffer builder used immediately before these character-growth messages.
- `C1:AD0A` is not just a probable pointer setter; it is the common amount-like payload staging hook used immediately before the fixed `PRINT_ACTION_AMOUNT` scripts.

That makes the `ACxx/ADxx` battle-text context note much more grounded in ordinary runtime behavior.

## Current safest interpretation

The safest current interpretation is:

- this family is the level-up and stat-gain narration layer for character-side growth
- it uses the ordinary battle-text context machinery rather than a special one-off printer
- the target-name buffer and amount substitution slots are reused cleanly for level-up text, not just for battle actions and reflected-hit messages

## EF source-anchor update

A later EF payload split promoted the whole `EF:7A66..7B64` message ladder as
source anchors in `src/ef/ef_4e20_c51b_text_payload_data.asm`. The split also
corrected the local guts-message address to `EF:7AC9`, matching the EBATTLE8
listing and the generated EF range manifest.
