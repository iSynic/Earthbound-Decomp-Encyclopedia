# Class2 Battlers Table Layout 9F8A 9FAC

This note captures a major structural correction in the local battle-side model.

See also [class2-candidate-table-9fac.md](notes/class2-candidate-table-9fac.md).
See also [class2-source-families-986f-9f8a.md](notes/class2-source-families-986f-9f8a.md).
See also [class2-battler-core-field-crosswalk.md](notes/class2-battler-core-field-crosswalk.md).
See also [class2-local-enemy-id-to-battler-init-chain.md](notes/class2-local-enemy-id-to-battler-init-chain.md).

## Main result

The local WRAM region we had been describing as a generic 32-entry candidate-row family is now very likely the real battle battler region.

The exact local pattern is:

- `9F8A` as a 2-byte count-like value
- `9F8C` as a 32-byte value list
- `9FAC + 0x4E * n` as a 32-entry row family

The reference `ebsrc` RAM layout matches that shape exactly:

- `ENEMIES_IN_BATTLE` is 2 bytes
- `ENEMIES_IN_BATTLE_IDS` is `2 * 16 = 32` bytes
- `BATTLERS_TABLE` starts immediately after that block
- `.SIZEOF(battler) = 78 = 0x4E`

That is not a vague thematic similarity. It is an exact contiguous layout match.

## Exact stride match

The strongest single fact is the stride.

Reference `battler` layout:

- last named field is `id2` at byte `77`
- therefore `.SIZEOF(battler) = 78 decimal = 0x4E`

Local battle-row family:

- our selected-row and scan notes have repeatedly used `9FAC + 0x4E * n`

So the row family we have been tracing is not merely battler-layout-compatible in the abstract. Its stride matches the reference battler struct exactly.

## Exact leading layout match

The preceding WRAM also matches cleanly.

Reference RAM order:

- `ENEMIES_IN_BATTLE`
- `ENEMIES_IN_BATTLE_IDS`
- `BATTLERS_TABLE`

Local WRAM order we already established:

- `9F8A` behaves like a count
- `9F8C` behaves like an upstream id list
- `9FAC` begins the 32-entry `0x4E`-stride row family

The size math is exact:

- `9F8A..9F8B` = 2 bytes
- `9F8C..9FAB` = 32 bytes = 16 words
- `9FAC` is the next address after that block

That is exactly what the reference RAM layout would produce for `ENEMIES_IN_BATTLE`, `ENEMIES_IN_BATTLE_IDS`, then `BATTLERS_TABLE`.

## What this corrects

This forces an important correction to our earlier language.

Earlier notes often described:

- a generic candidate pool rooted at `9FAC`
- parallel metadata arrays at `9FB8`, `9FBA`, `9FBB`, `9FBC`, `9FBF`, and `9FC9`

That framing is now too loose.

Those addresses are better understood as battler-field offsets inside the `BATTLERS_TABLE` region:

- `9FB8 = 9FAC + 0x0C` -> `battler::consciousness`
- `9FBA = 9FAC + 0x0E` -> `battler::ally_or_enemy`
- `9FBB = 9FAC + 0x0F` -> `battler::npc_id`
- `9FBC = 9FAC + 0x10` -> `battler::row`
- `9FC9 = 9FAC + 0x1D` -> `battler::afflictions`

So several earlier "parallel array" reads were really per-field scans over battlers.

## Local control-flow bridge

The new init-chain note strengthens this from layout matching into explicit local control flow.

See [class2-local-enemy-id-to-battler-init-chain.md](notes/class2-local-enemy-id-to-battler-init-chain.md) for the direct bridge.

The short version is:

- local `C2:B6EB` behaves like `BATTLE_INIT_ENEMY_STATS`
- local callers such as `C2:4A24` compute battler bases in `9FAC + 0x4E * n`
- those same paths load enemy ids from `9F8C`
- then they call `C2:B6EB` to seed the battler entry from `D5:9589` enemy data

That is the direct local chain we wanted.

## What now looks much stronger

This exact layout match plus the local init chain strengthens several earlier results all at once:

- the affliction crosswalk at `+0x1F/+0x20/+0x21` was not just a local coincidence
- the lower-field crosswalk for `+0x0C`, `+0x10`, and `+0x0B` now sits inside a real battler-sized region
- `C4:A228` provides a C4-side writer for `+0x0A`, mapping ranked `AD7A/AD82` entries back into `battler.current_target`
- `$A970/$A972` now look much more like active battler pointers than like abstract controller-row anchors
- `9F8C` now looks much more like `ENEMIES_IN_BATTLE_IDS` than like a generic upstream list

## Source-backed text-context update

The `C2:3BCF` and `C2:3D05` battle-text context builders now carry this
interpretation directly in source comments and aliases.

The attacker side names `$A970` as the active attacker battler pointer and uses
the battler row fields `+0x00`, `+0x0B`, `+0x0E`, `+0x0F`, `+0x10`, and `+0x4C`
while building the `$A983` attacker-name buffer and `$5E77` article flag.

The target side names `$A972` as the active target battler pointer and mirrors
the same field vocabulary for the `$A99E` target-name buffer and `$5E78` article
flag. Its helper tails also name the `$A96C/$A96E` current target mask and the
`9FAC + 0x4E * n` battler pointer rebuild used before calling
`FIX_TARGET_NAME`.

That makes the `$A970/$A972` active-battler interpretation source-backed in the
same battle-text cluster that previously provided some of the strongest field
crosswalk evidence.

## Source-backed action/mask update

The action-dispatch and target-mask sources now carry the same correction:

- `C2:4477` names battler `current_action` (`+0x04`), `action_targeting`
  (`+0x09`), `current_target` (`+0x0A`), and `ally_or_enemy` (`+0x0E`) while
  deriving target-mask instructions from the `D5:7B68` action table.
- `C2:4703` consumes those battler fields while dispatching into the mask
  helper family.
- `C2:40A4` names `$9FAC` as the battler target domain for the second-pointer
  payload pass and prunes by `consciousness` / `afflictions`.
- `C2:6BFB..70E4` now names the `$9FAC` root and `0x4E` stride as
  `BattlersTableBase` and `BattlerRowSize`, with field names replacing the
  older generic candidate-row offsets.

That lets the remaining "candidate" language stay focused on ranked target
lists such as `$AD7A/$AD82`, instead of blurring the underlying battler table
itself.

## Current safest interpretation

The safest current interpretation is:

- `9F8A` is very likely `ENEMIES_IN_BATTLE`
- `9F8C` is very likely `ENEMIES_IN_BATTLE_IDS`
- `9FAC` is very likely the start of `BATTLERS_TABLE`
- the `0x4E`-stride row family we have been tracing consists of battler entries, not abstract candidate records
- local `C2:B6EB` is very likely `BATTLE_INIT_ENEMY_STATS`

That is now stronger than a mere layout-compatible hunch.

## Best next target

The best next move is to trace one of the `C2:B6EB` caller families like `C2:4D01` or `C2:760C`, because that should tell us why those paths are spawning or reinitializing battlers instead of only proving that they can.
