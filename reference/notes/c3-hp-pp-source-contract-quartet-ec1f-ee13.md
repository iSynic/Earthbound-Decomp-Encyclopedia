# C3 HP / PP Source Contract Quartet `C3:EC1F` .. `C3:EE13`

This note promotes the four bank-`03` HP/PP adjustment workers into source-contract form. It is the C3-local counterpart to [hp-pp-adjust-helper-quartet-c18f0e-c19010.md](notes/hp-pp-adjust-helper-quartet-c18f0e-c19010.md) and [text-command-family-1e-stat-recovery.md](notes/text-command-family-1e-stat-recovery.md).

## Working Names

- `C3:EC1F` = `DepleteCharacterHp`
- `C3:EC8B` = `RecoverCharacterHp`
- `C3:ED2C` = `DepleteCharacterPp`
- `C3:ED98` = `RecoverCharacterPp`

## Shared Entry Contract

All four workers share the same calling convention:

- `A` is a 1-based character id; `A = 0` returns without changing state
- `X` is either a direct amount or a percent value
- `Y = 0` means percent mode
- `Y != 0` means direct amount mode; the C1 wrappers use `Y = 1`

Each worker maps the 1-based character id into the character-record stride by subtracting one, then calling `C0:8FF7` to compute `(character - 1) * 0x5F`.

In percent mode, the worker computes `max * X / 100` through `C0:9086` and `C0:90FF`. In direct mode, it uses `X` as the amount unchanged.

## HP Workers

The HP pair uses:

- `$99D8 + offset` = max HP
- `$9A15 + offset` = current HP
- `$9A13 + offset` = HP marker or mirror field

`C3:EC1F` subtracts the resolved amount from current HP at `$9A15 + offset`. It detects underflow or wrap by comparing the post-subtract value against max HP at `$99D8 + offset`; if the result is greater than max HP, it stores `0`.

Source contract:

- `current_hp = max(current_hp - amount, 0)`

`C3:EC8B` adds the resolved amount to current HP at `$9A15 + offset`, sets `$9A13 + offset` to `1` if that marker is still `0`, and caps current HP at max HP.

Source contract:

- `current_hp = min(current_hp + amount, max_hp)`
- `hp_marker = 1` if `hp_marker == 0`

## PP Workers

The PP pair uses:

- `$99DA + offset` = max PP
- `$9A1B + offset` = current PP
- `$9A19 + offset` = PP marker or current-value mirror field

`C3:ED2C` subtracts the resolved amount from current PP at `$9A1B + offset`. Like the HP depletion worker, it detects underflow or wrap by comparing the post-subtract value against max PP at `$99DA + offset`; if the result is greater than max PP, it stores `0`.

Source contract:

- `current_pp = max(current_pp - amount, 0)`

`C3:ED98` adds the resolved amount to current PP at `$9A1B + offset` and caps current PP at max PP. Unlike `C3:EC8B`, this worker does not write `$9A19 + offset`.

Source contract:

- `current_pp = min(current_pp + amount, max_pp)`

## Direct Callers

Known direct callers from the local xref scan:

- `C3:EC1F`: `C1:8F3E`, `C1:8F5E`
- `C3:EC8B`: `C1:8F94`, `C1:8FB4`
- `C3:ED2C`: `C1:8FEA`, `C1:900A`, `C1:B81A`
- `C3:ED98`: `C1:9040`, `C1:9060`

The paired `C1:8F0E`, `C1:8F64`, `C1:8FBA`, and `C1:9010` wrappers support either a direct target id or wildcard `A = #$00FF`. On wildcard input, they iterate active-party ids from `$986F` up to boundary `$98A4` and call the same C3 worker for each selected active character.

`C1:B81A` is the extra direct caller into `C3:ED2C`; it is a battle/action-side PP depletion path rather than one of the text-command wrappers.

## Confidence

- quartet field split and HP/PP max/current pairs: high confidence
- `Y = 0` percent mode and `Y != 0` direct amount mode: high confidence
- `C3:ED98` not writing `$9A19`: high confidence
- `$9A19` as a PP marker or current-value mirror field maintained elsewhere: medium confidence
