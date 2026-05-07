# Reference: `eb-decompile_4ef92`

Extracted at:

- [refs/eb-decompile-4ef92](refs/eb-decompile-4ef92)

## What it is

This archive does **not** look like a traditional assembly/disassembly project.

It looks much more like a large CoilSnake-style project or structured ROM data dump:

- many top-level YAML tables
- large extracted asset folders (`Music`, `SpriteGroups`, `BattleBGs`, `BattleSprites`, `Tilesets`, `Swirls`, `WindowGraphics`, etc.)
- CCScript text dumps under `ccscript/`
- a `Project.snake` manifest listing modules and resources

So this is best treated as a **data-oriented reference project**, not a code-first decomp.

## Why it is useful

This project is immediately helpful for table and asset work.

Representative examples:

- [timed_delivery_table.yml](refs/eb-decompile-4ef92/timed_delivery_table.yml)
- [battle_action_table.yml](refs/eb-decompile-4ef92/battle_action_table.yml)
- [enemy_configuration_table.yml](refs/eb-decompile-4ef92/enemy_configuration_table.yml)
- [npc_config_table.yml](refs/eb-decompile-4ef92/npc_config_table.yml)
- [ccscript/main.ccs](refs/eb-decompile-4ef92/ccscript/main.ccs)
- [Project.snake](refs/eb-decompile-4ef92/Project.snake)

For the delivery-table work in particular, `timed_delivery_table.yml` already matches our corrected local read very well:

- sprite group
- event flag
- two script/text pointers
- timer-like middle field
- trailing speed-like pair

That makes this archive especially good for validating table field meanings and for giving friendlier names to asset/data records.

## Where it is weaker

For our current ROM-first reverse-engineering work, it is weaker than the other two references in one important way:

- it does not give us assembly control flow or code-side call relationships

So it will help a lot with:

- table identities
- field naming
- asset relationships
- script/text data

But it will help much less with:

- routine behavior
- caller/callee tracing
- CPU-state-sensitive control-flow analysis

## Best use

The safest way to use this archive is:

- use `ebsrc` and the legacy assembly tree for code-side structure and labels
- use `eb-decompile_4ef92` for data/table confirmation and asset-side context

That makes it a strong third reference, just not a replacement for the code-oriented ones.
