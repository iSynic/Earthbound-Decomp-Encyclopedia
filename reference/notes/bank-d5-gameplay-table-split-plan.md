# Bank D5 Gameplay Table Split Plan

Status: complete as of `tools/build_d5_table_splits.py`. The exact generated
outputs are `notes/d5-table-splits.md` and `build/d5-table-splits.json`; this
file is retained as the rationale and historical plan.

## Why D5 Is The Remaining Hard Spot

The `D5:5000..D5:FFFF` region is the only large non-padding unresolved region in
the `D5-EE` closure. The bank config names the whole region, but several
generated source files are absent from the checked-in reference tree. Because
the first missing include is `data/items.asm`, all later exact CPU offsets are
blocked until we recover or infer the missing table sizes.

Region size:

- `D5:5000..D5:FFFF`
- `45056` bytes

## Known Existing Source Byte Budget

These included source files exist in the reference tree and have countable US
retail byte sizes:

| Include | Estimated bytes | Notes |
| --- | ---: | --- |
| `data/battle/action_table.asm` | `3816` | action records with byte/dword fields |
| `data/battle/psi_abilities.asm` | `810` | PSI ability records |
| `data/battle/psi_names.asm` | `425` | 17 names, `PSI_NAME_SIZE = 25` |
| `data/battle/npc_ai_table.asm` | `38` | byte table |
| `data/battle/enemies.asm` | `21714` | enemy records |
| `data/condiment_table.asm` | `308` | condiment table |
| `data/dont_care_names.asm` | `294` | 49 default names, 6 bytes each |

Known existing-source total: `27405` bytes.

Remaining bytes, if those estimates are exact: `17651` bytes.

## Missing Or Generated Includes To Account For

These source-order includes are missing and likely occupy most or all of the
remaining `17651` bytes:

- `data/items.asm`
- `data/store_inventories.asm`
- `data/psi_teleport_destinations.asm`
- `data/telephone_contacts.asm`
- `data/exp_table.asm`
- `data/stats_growth_vars.asm`
- `data/map/teleport_destinations.asm`
- `data/map/hotspot_coordinates.asm`
- `data/timed_item_transformation_table.asm`
- `data/initial_stats.asm`
- `data/timed_delivery_table.asm`

## Split Strategy

1. Start with fixed-width tables that have obvious engine consumers:
   `items`, `store_inventories`, `exp_table`, `initial_stats`, and
   `timed_delivery_table`.
2. Use known source byte counts as anchors for the later existing blocks:
   action table, PSI abilities/names, NPC AI, enemies, condiment table, and
   default names.
3. Work from both ends of the region:
   - forward from `D5:5000` using item/shop/teleport/phone formats.
   - backward from `D5:FFFF` using timed delivery, initial stats, default names,
     timed item transformations, hotspots, and teleport destinations.
4. Reconcile against the `17651` missing-byte budget.
5. Once each missing table has a byte count, update
   `tools/build_asset_bank_manifest.py` or add a D5-specific splitter so the
   manifest can promote `D5:5000..D5:FFFF` from one blocked region into exact
   source-order spans.

## Resolution

The table splitter reconciles the whole `D5:5000..D5:FFFF` region exactly:

- post-pad region bytes: `45056`
- accounted table/tail bytes: `45056`
- table/tail split rows: `20`
- named zero island: `D5:7A70..D5:7AAD`, `62` bytes
- zero tail: `D5:F711..D5:FFFF`, `2287` bytes

The key correction is that `ITEM_CONFIGURATION_TABLE` has `254` rows, not
`256`. At `0x27` bytes per row, it ends at `D5:76B1`, and `STORE_TABLE` starts
immediately at `D5:76B2`.

## Current Confidence

High confidence:

- D5 contains no executable code.
- The order of table families is known from the bank config.
- The exact post-pad table/tail byte budget is reconciled for US retail.

Still unresolved:

- Consumer-confirmed subfield ordering for `TIMED_DELIVERY_TABLE`.
