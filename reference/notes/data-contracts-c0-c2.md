# C0-C2 data contract manifest

Generated from local notes plus quarantined reference structs. This is the machine-readable struct/table front door for C0-C2 work; edit `tools/build_data_contract_manifest.py`, then regenerate this file.

## Summary

- schema: `earthbound-decomp.data-contracts.v1`
- contracts: `10`
- fields: `271`

| Contract | Domain | Address | Stride | Count | Struct | Fields | Confidence |
| --- | --- | --- | ---: | ---: | --- | ---: | --- |
| GAME_STATE | wram-root | `7E:9801` | `0x1D9` | 1 | `game_state` | 26 | corroborated |
| PARTY_CHARACTERS | wram-root | `7E:99CE` | `0x5F` | 6 | `char_struct` | 41 | corroborated |
| BATTLERS_TABLE | wram-root | `7E:9FAC` | `0x4E` | 32 | `battler` | 49 | corroborated |
| ITEM_CONFIGURATION_TABLE | rom-table | `D5:5000` | `0x27` | 254 | `item` | 7 | corroborated |
| BATTLE_ACTION_TABLE | rom-table | `D5:7B68` | `0xC` | 318 | `battle_action` | 6 | corroborated |
| PSI_ABILITY_TABLE | rom-table | `D5:8A50` | `0xF` | 54 | `psi_ability` | 11 | corroborated |
| ENEMY_CONFIGURATION_TABLE | rom-table | `D5:9589` | `0x5E` | 231 | `enemy_data` | 42 | corroborated |
| BATTLE_SELECTION_SNAPSHOT | wram-overlay | `7E:9FFA` | `0x4E` | 1 | `battle_menu_selection_header_plus_snapshot` | 17 | corroborated-overlay |
| LOADED_BG_DATA_LAYER1 | wram-root | `7E:ADD4` | `0x77` | 1 | `loaded_bg_data` | 36 | corroborated |
| LOADED_BG_DATA_LAYER2 | wram-root | `7E:AE4B` | `0x77` | 1 | `loaded_bg_data` | 36 | corroborated |

## Contracts

### GAME_STATE

- domain: `wram-root`
- address: `7E:9801`
- stride: `0x1D9`
- count: `1`
- struct: `game_state`
- confidence: `corroborated`
- note: saveblock game_state root from ebsrc ram.asm
- evidence: `tools/lookup_wram_field.py`, `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/ram.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `mother2_playername` | 1 | 12 | 12-byte Mother 2 carryover name buffer |
| `0xC` | `earthbound_playername` | 1 | 24 | 24-byte EarthBound player-name buffer |
| `0x24` | `pet_name` | 1 | 6 | 6-byte pet-name buffer |
| `0x2A` | `favourite_food` | 1 | 6 | 6-byte favourite-food buffer |
| `0x30` | `favourite_thing` | 1 | 12 | 12-byte favourite-thing / PSI naming buffer |
| `0x3C` | `money_carried` | 4 | 1 | party money carried |
| `0x40` | `bank_balance` | 4 | 1 | bank account balance |
| `0x44` | `party_psi` | 1 | 1 | party PSI latch byte |
| `0x45` | `party_npc_1` | 1 | 1 | party NPC slot 1 id |
| `0x46` | `party_npc_2` | 1 | 1 | party NPC slot 2 id |
| `0x4B` | `party_status` | 1 | 1 | party status byte |
| `0x52` | `wallet_backup` | 4 | 1 | wallet backup dword |
| `0x56` | `escargo_express_items` | 1 | 36 | Escargo Express stored-item queue |
| `0x7A` | `party_members` | 1 | 6 | party member ids |
| `0x82` | `leader_x_coord` | 2 | 1 | leader X coordinate |
| `0x86` | `leader_y_coord` | 2 | 1 | leader Y coordinate |
| `0x8A` | `leader_direction` | 2 | 1 | leader facing direction |
| `0x8C` | `trodden_tile_type` | 2 | 1 | trodden tile type |
| `0x8E` | `walking_style` | 2 | 1 | walking style |
| `0x94` | `current_party_members` | 2 | 1 | current party-members word |
| `0xAE` | `party_count` | 1 | 1 | party count |
| `0xAF` | `player_controlled_party_count` | 1 | 1 | player-controlled party count |
| `0xC1` | `text_speed` | 1 | 1 | selected text speed |
| `0xC2` | `sound_setting` | 1 | 1 | sound setting |
| `0x1D4` | `timer` | 4 | 1 | global timer dword |
| `0x1D8` | `text_flavour` | 1 | 1 | text flavour byte |

### PARTY_CHARACTERS

- domain: `wram-root`
- address: `7E:99CE`
- stride: `0x5F`
- count: `6`
- struct: `char_struct`
- confidence: `corroborated`
- note: party char_struct array from ebsrc ram.asm
- evidence: `tools/lookup_wram_field.py`, `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/ram.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `name` | 1 | 5 | 5-byte party member name buffer |
| `0x5` | `level` | 1 | 1 | level |
| `0x6` | `exp` | 4 | 1 | experience dword |
| `0xA` | `max_hp` | 2 | 1 | max HP |
| `0xC` | `max_pp` | 2 | 1 | max PP |
| `0xE` | `afflictions` | 1 | 7 | char_struct affliction-group bytes |
| `0x15` | `offense` | 1 | 1 | display-facing offense |
| `0x16` | `defense` | 1 | 1 | display-facing defense |
| `0x17` | `speed` | 1 | 1 | display-facing speed |
| `0x18` | `guts` | 1 | 1 | display-facing guts |
| `0x19` | `luck` | 1 | 1 | display-facing luck |
| `0x1A` | `vitality` | 1 | 1 | display-facing vitality |
| `0x1B` | `iq` | 1 | 1 | display-facing IQ |
| `0x1C` | `base_offense` | 1 | 1 | base offense before equipment refresh |
| `0x1D` | `base_defense` | 1 | 1 | base defense before equipment refresh |
| `0x1E` | `base_speed` | 1 | 1 | base speed |
| `0x1F` | `base_guts` | 1 | 1 | base guts |
| `0x20` | `base_luck` | 1 | 1 | base luck |
| `0x21` | `base_vitality` | 1 | 1 | base vitality |
| `0x22` | `base_iq` | 1 | 1 | base IQ |
| `0x23` | `items` | 1 | 14 | inventory item ids |
| `0x31` | `equipment` | 1 | 4 | equipped item ids by slot family |
| `0x3D` | `position_index` | 2 | 1 | position index word |
| `0x43` | `current_hp_fraction` | 2 | 1 | HP rolling fraction |
| `0x45` | `current_hp` | 2 | 1 | current HP |
| `0x47` | `current_hp_target` | 2 | 1 | HP target |
| `0x49` | `current_pp_fraction` | 2 | 1 | PP rolling fraction |
| `0x4B` | `current_pp` | 2 | 1 | current PP |
| `0x4D` | `current_pp_target` | 2 | 1 | PP target |
| `0x4F` | `hp_pp_window_options` | 2 | 1 | HP/PP window options |
| `0x51` | `miss_rate` | 1 | 1 | miss-rate byte |
| `0x52` | `fire_resist` | 1 | 1 | fire resistance |
| `0x53` | `freeze_resist` | 1 | 1 | freeze resistance |
| `0x54` | `flash_resist` | 1 | 1 | flash resistance |
| `0x55` | `paralysis_resist` | 1 | 1 | paralysis resistance |
| `0x56` | `hypnosis_brainshock_resist` | 1 | 1 | hypnosis/brainshock resistance |
| `0x57` | `boosted_speed` | 1 | 1 | boosted speed adder |
| `0x58` | `boosted_guts` | 1 | 1 | boosted guts adder |
| `0x59` | `boosted_vitality` | 1 | 1 | boosted vitality adder |
| `0x5A` | `boosted_iq` | 1 | 1 | boosted IQ adder |
| `0x5B` | `boosted_luck` | 1 | 1 | boosted luck adder |

### BATTLERS_TABLE

- domain: `wram-root`
- address: `7E:9FAC`
- stride: `0x4E`
- count: `32`
- struct: `battler`
- confidence: `corroborated`
- note: battler array from ebsrc ram.asm
- evidence: `tools/lookup_wram_field.py`, `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/ram.asm`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `id` | 2 | 1 | battler id |
| `0x2` | `sprite` | 1 | 1 | sprite id |
| `0x4` | `current_action` | 2 | 1 | current action id |
| `0x6` | `action_order_var` | 1 | 1 | action-order variable |
| `0x7` | `action_item_slot` | 1 | 1 | selected item slot |
| `0x8` | `current_action_argument` | 1 | 1 | current action argument |
| `0x9` | `action_targetting` | 1 | 1 | action targeting mode |
| `0xA` | `current_target` | 1 | 1 | current target id |
| `0xB` | `the_flag` | 1 | 1 | enemy data the_flag copy |
| `0xC` | `consciousness` | 1 | 1 | consciousness gate byte |
| `0xD` | `has_taken_turn` | 1 | 1 | turn-taken latch |
| `0xE` | `ally_or_enemy` | 1 | 1 | ally-or-enemy side byte |
| `0xF` | `npc_id` | 1 | 1 | NPC or enemy id |
| `0x10` | `row` | 1 | 1 | front/back row byte |
| `0x11` | `hp` | 2 | 1 | battle HP |
| `0x13` | `hp_target` | 2 | 1 | battle HP target |
| `0x15` | `hp_max` | 2 | 1 | battle max HP |
| `0x17` | `pp` | 2 | 1 | battle PP |
| `0x19` | `pp_target` | 2 | 1 | battle PP target |
| `0x1B` | `pp_max` | 2 | 1 | battle max PP |
| `0x1D` | `afflictions` | 1 | 7 | battler affliction-group bytes |
| `0x24` | `guarding` | 1 | 1 | guarding flag |
| `0x25` | `shield_hp` | 1 | 1 | shield HP |
| `0x26` | `offense` | 2 | 1 | battle offense |
| `0x28` | `defense` | 2 | 1 | battle defense |
| `0x2A` | `speed` | 2 | 1 | battle speed |
| `0x2C` | `guts` | 2 | 1 | battle guts |
| `0x2E` | `luck` | 2 | 1 | battle luck |
| `0x30` | `vitality` | 1 | 1 | battle vitality |
| `0x31` | `iq` | 1 | 1 | battle IQ |
| `0x32` | `base_offense` | 1 | 1 | base offense |
| `0x33` | `base_defense` | 1 | 1 | base defense |
| `0x34` | `base_speed` | 1 | 1 | base speed |
| `0x35` | `base_guts` | 1 | 1 | base guts |
| `0x36` | `base_luck` | 1 | 1 | base luck |
| `0x37` | `paralysis_resist` | 1 | 1 | paralysis resistance |
| `0x38` | `freeze_resist` | 1 | 1 | freeze resistance |
| `0x39` | `flash_resist` | 1 | 1 | flash resistance |
| `0x3A` | `fire_resist` | 1 | 1 | fire resistance |
| `0x3B` | `brainshock_resist` | 1 | 1 | brainshock resistance |
| `0x3C` | `hypnosis_resist` | 1 | 1 | hypnosis resistance |
| `0x3D` | `money` | 2 | 1 | money drop |
| `0x3F` | `exp` | 4 | 1 | experience yield |
| `0x43` | `vram_sprite_index` | 1 | 1 | VRAM sprite index |
| `0x44` | `sprite_x` | 1 | 1 | battle sprite X |
| `0x45` | `sprite_y` | 1 | 1 | battle sprite Y |
| `0x46` | `initiative` | 1 | 1 | initiative byte |
| `0x4B` | `use_alt_spritemap` | 1 | 1 | alternate spritemap flag |
| `0x4D` | `id2` | 1 | 1 | secondary id byte |

### ITEM_CONFIGURATION_TABLE

- domain: `rom-table`
- address: `D5:5000`
- stride: `0x27`
- count: `254`
- struct: `item`
- confidence: `corroborated`
- note: Fixed-stride item table used by C1/C2 inventory, equipment, and item-effect helpers.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/include/symbols/misc.inc.asm`, `notes/item-byte-19-packed-class-and-slot.md`, `notes/d5-table-splits.md`, `manifests/coilsnake-field-semantics.json`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `name` | 1 | 25 | USA item-name buffer |
| `0x19` | `packed_class_and_slot` | 1 | 1 | item type byte; local notes decode class/equipment slot packing |
| `0x1A` | `cost` | 2 | 1 | store cost; CoilSnake `item-cost-probe` is runtime-correlated to the shop item row builder |
| `0x1C` | `flags` | 1 | 1 | item flags |
| `0x1D` | `effect` | 2 | 1 | item effect id |
| `0x1F` | `params` | 4 | 1 | item parameter dword |
| `0x23` | `help_text` | 4 | 1 | help text pointer |

### BATTLE_ACTION_TABLE

- domain: `rom-table`
- address: `D5:7B68`
- stride: `0xC`
- count: `318`
- struct: `battle_action`
- confidence: `corroborated`
- note: Battle action rows consumed by targetting, menu, PP-cost, text, and battle-function dispatch paths.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/data/battle/action_table.asm`, `notes/battle-targetting-resolver-c1adb4-af50.md`, `notes/battle-psi-menu-controller-c1cc39-ce73.md`, `manifests/coilsnake-field-semantics.json`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `direction` | 1 | 1 | enemy/ally/immediate direction selector |
| `0x1` | `target` | 1 | 1 | target subtype consumed by the C1 targetting resolver |
| `0x2` | `type` | 1 | 1 | battle action type |
| `0x3` | `pp_cost` | 1 | 1 | PSI/action PP cost; CoilSnake `battle-action-pp-cost-probe` is runtime-correlated to the C1:CC39 battle PSI PP guard |
| `0x4` | `description_text_pointer` | 4 | 1 | battle text pointer |
| `0x8` | `battle_function_pointer` | 4 | 1 | battle action handler pointer |

### PSI_ABILITY_TABLE

- domain: `rom-table`
- address: `D5:8A50`
- stride: `0xF`
- count: `54`
- struct: `psi_ability`
- confidence: `corroborated`
- note: PSI menu metadata table, including linked battle action ids and learn levels.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/include/symbols/misc.inc.asm`, `notes/battle-psi-ability-table-d58a50.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `name` | 1 | 1 | PSI name id |
| `0x1` | `level` | 1 | 1 | PSI alpha/beta/gamma/omega level |
| `0x2` | `category` | 1 | 1 |  |
| `0x3` | `usability` | 1 | 1 | menu/use gating byte |
| `0x4` | `battle_action` | 2 | 1 | linked D5:7B68 battle action id |
| `0x6` | `ness_level` | 1 | 1 |  |
| `0x7` | `paula_level` | 1 | 1 |  |
| `0x8` | `poo_level` | 1 | 1 |  |
| `0x9` | `menu_x` | 1 | 1 |  |
| `0xA` | `menu_y` | 1 | 1 |  |
| `0xB` | `text` | 4 | 1 | description text pointer |

### ENEMY_CONFIGURATION_TABLE

- domain: `rom-table`
- address: `D5:9589`
- stride: `0x5E`
- count: `231`
- struct: `enemy_data`
- confidence: `corroborated`
- note: Enemy configuration records copied into battler slots by the C2 battle-init paths.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/include/symbols/misc.inc.asm`, `notes/class2-005e-record-domain.md`, `notes/class2-local-enemy-id-to-battler-init-chain.md`, `notes/class2-d59589-enemy-data-crosswalk.md`, `manifests/coilsnake-field-semantics.json`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `the_flag` | 1 | 1 |  |
| `0x1` | `name` | 1 | 25 | USA enemy-name buffer |
| `0x1A` | `gender` | 1 | 1 |  |
| `0x1B` | `type` | 1 | 1 |  |
| `0x1C` | `battle_sprite` | 2 | 1 |  |
| `0x1E` | `overworld_sprite` | 2 | 1 |  |
| `0x20` | `run_flag` | 1 | 1 |  |
| `0x21` | `hp` | 2 | 1 |  |
| `0x23` | `pp` | 2 | 1 |  |
| `0x25` | `exp` | 4 | 1 |  |
| `0x29` | `money` | 2 | 1 |  |
| `0x2B` | `event_script` | 2 | 1 |  |
| `0x2D` | `encounter_text_ptr` | 4 | 1 |  |
| `0x31` | `death_text_ptr` | 4 | 1 |  |
| `0x35` | `battle_sprite_palette` | 1 | 1 |  |
| `0x36` | `level` | 1 | 1 |  |
| `0x37` | `music` | 1 | 1 |  |
| `0x38` | `offense` | 2 | 1 |  |
| `0x3A` | `defense` | 2 | 1 |  |
| `0x3C` | `speed` | 1 | 1 |  |
| `0x3D` | `guts` | 1 | 1 |  |
| `0x3E` | `luck` | 1 | 1 |  |
| `0x3F` | `fire_vulnerability` | 1 | 1 |  |
| `0x40` | `freeze_vulnerability` | 1 | 1 |  |
| `0x41` | `flash_vulnerability` | 1 | 1 |  |
| `0x42` | `paralysis_vulnerability` | 1 | 1 |  |
| `0x43` | `hypnosis_brainshock_vulnerability` | 1 | 1 |  |
| `0x44` | `miss_rate` | 1 | 1 |  |
| `0x45` | `action_order` | 1 | 1 |  |
| `0x46` | `actions` | 2 | 4 | normal action ids; CoilSnake `enemy-insane-cultist-action1-probe` is runtime-correlated to the C2:5024 enemy action-slot staging path |
| `0x4E` | `final_action` | 2 | 1 |  |
| `0x50` | `action_args` | 1 | 4 | arguments for normal actions |
| `0x54` | `final_action_arg` | 1 | 1 |  |
| `0x55` | `iq` | 1 | 1 |  |
| `0x56` | `boss` | 1 | 1 |  |
| `0x57` | `item_drop_rate` | 1 | 1 | locally still softer than the core 0x5E enemy record match |
| `0x58` | `item_dropped` | 1 | 1 | locally still softer than the core 0x5E enemy record match |
| `0x59` | `initial_status` | 1 | 1 |  |
| `0x5A` | `death_type` | 1 | 1 |  |
| `0x5B` | `row` | 1 | 1 |  |
| `0x5C` | `max_called` | 1 | 1 |  |
| `0x5D` | `mirror_success` | 1 | 1 |  |

### BATTLE_SELECTION_SNAPSHOT

- domain: `wram-overlay`
- address: `7E:9FFA`
- stride: `0x4E`
- count: `1`
- struct: `battle_menu_selection_header_plus_snapshot`
- confidence: `corroborated-overlay`
- note: Formal battle_menu_selection header at the front of a larger C2:B930 selected-slot snapshot overlay. This base overlaps BATTLERS_TABLE[1] in local address terms, so consumers should treat it as an overlay/scratch contract rather than an independent root.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `notes/battle-selection-snapshot-export-c2b930.md`, `notes/battle-targetting-resolver-c1adb4-af50.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `user` | 1 | 1 |  |
| `0x1` | `param1` | 1 | 1 |  |
| `0x2` | `selected_action` | 2 | 1 |  |
| `0x4` | `targetting` | 1 | 1 |  |
| `0x5` | `selected_target` | 1 | 1 |  |
| `0xC` | `snapshot_active` | 1 | 1 | C2:B930 sets this byte to 1 when exporting a live slot snapshot |
| `0xE` | `snapshot_ally_or_enemy` | 1 | 1 | snapshot byte cleared by C2:B930; same offset family as battler::ally_or_enemy |
| `0xF` | `snapshot_npc_id` | 1 | 1 | snapshot byte cleared by C2:B930; same offset family as battler::npc_id |
| `0x10` | `selected_user_zero_based` | 1 | 1 | zero-based selected user or battler id |
| `0x11` | `current_hp` | 2 | 1 | copied from selected char_struct current_hp |
| `0x13` | `current_hp_target` | 2 | 1 | copied from selected char_struct current_hp_target |
| `0x15` | `max_hp` | 2 | 1 | copied from selected char_struct max_hp |
| `0x17` | `current_pp` | 2 | 1 | copied from selected char_struct current_pp |
| `0x19` | `current_pp_target` | 2 | 1 | copied from selected char_struct current_pp_target |
| `0x1B` | `max_pp` | 2 | 1 | copied from selected char_struct max_pp |
| `0x1D` | `afflictions` | 1 | 7 | copied from selected char_struct affliction/status bytes |
| `0x37` | `resistance_summary` | 1 | 6 | derived from selected char_struct late resistance fields |

### LOADED_BG_DATA_LAYER1

- domain: `wram-root`
- address: `7E:ADD4`
- stride: `0x77`
- count: `1`
- struct: `loaded_bg_data`
- confidence: `corroborated`
- note: Layer 1 runtime state for battle background palette, scroll, and distortion effects.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/ram.asm`, `notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `target_layer` | 1 | 1 |  |
| `0x1` | `bitdepth` | 1 | 1 |  |
| `0x2` | `freeze_palette_scrolling` | 1 | 1 |  |
| `0x3` | `palette_shifting_style` | 1 | 1 |  |
| `0x4` | `palette_cycle_1_first` | 1 | 1 |  |
| `0x5` | `palette_cycle_1_last` | 1 | 1 |  |
| `0x6` | `palette_cycle_2_first` | 1 | 1 |  |
| `0x7` | `palette_cycle_2_last` | 1 | 1 |  |
| `0x8` | `palette_cycle_1_step` | 1 | 1 |  |
| `0x9` | `palette_cycle_2_step` | 1 | 1 |  |
| `0xA` | `palette_change_speed` | 1 | 1 |  |
| `0xB` | `palette_change_duration_left` | 1 | 1 |  |
| `0xC` | `palette` | 2 | 16 | current RGB555 palette words |
| `0x2C` | `palette2` | 2 | 16 | backup/original RGB555 palette words |
| `0x4C` | `palette_pointer` | 2 | 1 | displayed palette destination pointer |
| `0x4E` | `scrolling_movements` | 1 | 4 |  |
| `0x52` | `current_scrolling_movement` | 1 | 1 |  |
| `0x53` | `scrolling_duration_left` | 2 | 1 |  |
| `0x55` | `horizontal_position` | 2 | 1 |  |
| `0x57` | `vertical_position` | 2 | 1 |  |
| `0x59` | `horizontal_velocity` | 2 | 1 |  |
| `0x5B` | `vertical_velocity` | 2 | 1 |  |
| `0x5D` | `horizontal_acceleration` | 2 | 1 |  |
| `0x5F` | `vertical_acceleration` | 2 | 1 |  |
| `0x61` | `distortion_styles` | 1 | 4 |  |
| `0x65` | `current_distortion_style_index` | 1 | 1 |  |
| `0x66` | `distortion_duration_left` | 2 | 1 |  |
| `0x68` | `distortion_type` | 1 | 1 |  |
| `0x69` | `distortion_ripple_frequency` | 2 | 1 |  |
| `0x6B` | `distortion_ripple_amplitude` | 2 | 1 |  |
| `0x6D` | `distortion_speed` | 1 | 1 |  |
| `0x6E` | `distortion_compression_rate` | 2 | 1 |  |
| `0x70` | `distortion_ripple_frequency_acceleration` | 2 | 1 |  |
| `0x72` | `distortion_ripple_amplitude_acceleration` | 2 | 1 |  |
| `0x74` | `distortion_speed_acceleration` | 1 | 1 |  |
| `0x75` | `distortion_compression_acceleration` | 2 | 1 |  |

### LOADED_BG_DATA_LAYER2

- domain: `wram-root`
- address: `7E:AE4B`
- stride: `0x77`
- count: `1`
- struct: `loaded_bg_data`
- confidence: `corroborated`
- note: Layer 2 runtime state for battle background palette, scroll, and distortion effects.
- evidence: `refs/ebsrc-main/ebsrc-main/include/structs.asm`, `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/ram.asm`, `notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`

| Offset | Field | Size | Count | Note |
| ---: | --- | ---: | ---: | --- |
| `0x0` | `target_layer` | 1 | 1 |  |
| `0x1` | `bitdepth` | 1 | 1 |  |
| `0x2` | `freeze_palette_scrolling` | 1 | 1 |  |
| `0x3` | `palette_shifting_style` | 1 | 1 |  |
| `0x4` | `palette_cycle_1_first` | 1 | 1 |  |
| `0x5` | `palette_cycle_1_last` | 1 | 1 |  |
| `0x6` | `palette_cycle_2_first` | 1 | 1 |  |
| `0x7` | `palette_cycle_2_last` | 1 | 1 |  |
| `0x8` | `palette_cycle_1_step` | 1 | 1 |  |
| `0x9` | `palette_cycle_2_step` | 1 | 1 |  |
| `0xA` | `palette_change_speed` | 1 | 1 |  |
| `0xB` | `palette_change_duration_left` | 1 | 1 |  |
| `0xC` | `palette` | 2 | 16 | current RGB555 palette words |
| `0x2C` | `palette2` | 2 | 16 | backup/original RGB555 palette words |
| `0x4C` | `palette_pointer` | 2 | 1 | displayed palette destination pointer |
| `0x4E` | `scrolling_movements` | 1 | 4 |  |
| `0x52` | `current_scrolling_movement` | 1 | 1 |  |
| `0x53` | `scrolling_duration_left` | 2 | 1 |  |
| `0x55` | `horizontal_position` | 2 | 1 |  |
| `0x57` | `vertical_position` | 2 | 1 |  |
| `0x59` | `horizontal_velocity` | 2 | 1 |  |
| `0x5B` | `vertical_velocity` | 2 | 1 |  |
| `0x5D` | `horizontal_acceleration` | 2 | 1 |  |
| `0x5F` | `vertical_acceleration` | 2 | 1 |  |
| `0x61` | `distortion_styles` | 1 | 4 |  |
| `0x65` | `current_distortion_style_index` | 1 | 1 |  |
| `0x66` | `distortion_duration_left` | 2 | 1 |  |
| `0x68` | `distortion_type` | 1 | 1 |  |
| `0x69` | `distortion_ripple_frequency` | 2 | 1 |  |
| `0x6B` | `distortion_ripple_amplitude` | 2 | 1 |  |
| `0x6D` | `distortion_speed` | 1 | 1 |  |
| `0x6E` | `distortion_compression_rate` | 2 | 1 |  |
| `0x70` | `distortion_ripple_frequency_acceleration` | 2 | 1 |  |
| `0x72` | `distortion_ripple_amplitude_acceleration` | 2 | 1 |  |
| `0x74` | `distortion_speed_acceleration` | 1 | 1 |  |
| `0x75` | `distortion_compression_acceleration` | 2 | 1 |  |
