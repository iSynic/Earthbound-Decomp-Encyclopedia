# Localization Display / Inventory Alias Model

This note consolidates recovered `.MSG` display and inventory authoring
commands against the already documented bank-`01` Text VM families. It uses
generated command counts and runtime hints only; recovered dialogue, raw
argument values, labels, and full source records remain ignored.

## Inputs

- `notes/localization-authoring-command-frontier.md`
- `notes/localization-macro-expansion-frontier.md`
- `notes/text-command-family-1c-print-display.md`
- `notes/text-command-family-1d-inventory-money.md`
- `notes/text-command-family-1a-menus.md`
- `notes/text-command-semantics-manifest.md`

## Main Result

Most high-count display and inventory authoring commands are not mysterious new
bytecode. They are source-facing names over existing Text VM families:

- `0x1C`: print/display aliases
- `0x1D`: inventory, money, possession, shop, and service checks
- `0x1A`: menu/selection helpers
- `0x19`: data/substitution helpers that feed display or inventory text

The unresolved work is mostly alias granularity: deciding whether a recovered
source command lowers directly to one VM command, or whether it is a source
macro that stages context and then uses one or more VM commands.

## Direct Display Aliases

These recovered commands already have conservative runtime hints into `0x1C`
and can be treated as near-direct print/display aliases for this phase:

| Source command | Count | Current VM read | Source-level role |
| --- | ---: | --- | --- |
| `@DSP_STS` | 786 | `0x1C 01` `PRINT_STAT` | print a stat/status value |
| `@DSP_NAME` | 686 | `0x1C 02` `PRINT_CHAR_NAME` | print a character name |
| `@DSP_GOODS` | 469 | `0x1C 05` `PRINT_ITEM_NAME` | print an item/goods name |
| `@DSP_ITEM` | 203 | `0x1C 05` `PRINT_ITEM_NAME` | print an item/goods name in selection-oriented contexts |
| `@DSP_NUM` | 169 | `0x1C 0A` `PRINT_NUMBER` | print staged numeric value |
| `@DSP_CNUM` | 80 | `0x1C 0A` `PRINT_NUMBER` | source variant for current/staged number print |
| `@DSP_PSI` | 15 | `0x1C 12` `PRINT_PSI_NAME` | print PSI name |
| `@DSP_CHAR` | 13 | `0x1C 03` `PRINT_CHAR` | print one character/glyph-style value |

The important distinction is `@DSP_GOODS` versus `@DSP_ITEM`: both currently
join to the item-name display leaf, but `@DSP_ITEM` is heavily tied to
`@SELGOTO` selection-branch setup. A reassembly-friendly source format should
preserve that source distinction even if both lower through the same `0x1C 05`
runtime primitive.

## Display Aliases Still Needing Context

The display-macro lane still has several commands without direct runtime hints:

| Source command | Count | Current read |
| --- | ---: | --- |
| `@DSP_ACTOR` | 447 | likely actor/entity-name or actor-context display alias |
| `@DSP_OBJECT` | 193 | likely object-context display alias |
| `@WINR_MONEY` | 100 | likely money/window result display helper |
| `@DSP_PL` | 36 | likely player/party display alias |
| `@DSP_LCNAME` | 35 | likely location-name display alias |
| `@DSP_ITEML` | 24 | likely long item-list or item-line display alias |
| `@DSP_PLAYER_GOODS` | 10 | likely selected-player item display alias |
| `@GET_OBJECT` | 7 | likely object-context producer before display/control flow |
| `@GET_ACTOR` | 5 | likely actor-context producer before display/control flow |
| `@GET_PLAYER_NAME` | 2 | likely player-name producer before display |

These should not be forced into new `0x1C` leaves yet. Several probably stage
context through `0x19` or event/actionscript state before a normal display
command consumes the value.

## Direct Inventory / Money Aliases

These recovered commands already have conservative runtime hints into `0x1D`
and can be treated as near-direct aliases for this phase:

| Source command | Count | Current VM read | Source-level role |
| --- | ---: | --- | --- |
| `@GOODSIN_PLAYER` | 183 | `0x1D 00` `GIVE_ITEM_TO_CHARACTER` | give an item/goods to a character |
| `@GOODSIN` | 3 | `0x1D 00` `GIVE_ITEM_TO_CHARACTER` | give item/goods, shorter source alias |
| `@GOODSOUT_PLAYER` | 33 | `0x1D 01` `TAKE_ITEM_FROM_CHARACTER` | remove item/goods from a character |
| `@GOODSOUT` | 25 | `0x1D 01` `TAKE_ITEM_FROM_CHARACTER` | remove item/goods, shorter source alias |
| `@Q_GOODSFULL` | 101 | `0x1D 03` `GET_PLAYER_HAS_INVENTORY_ROOM` | test party/character inventory room |
| `@Q_HAVE` | 23 | `0x1D 05` `CHECK_IF_CHARACTER_HAS_ITEM` | test possession of an item/goods |
| `@MONEYIN` | 18 | `0x1D 08` `ADD_TO_WALLET` | add money to wallet |
| `@MONEYOUT` | 54 | `0x1D 09` `TAKE_FROM_WALLET` | remove money from wallet |
| `@Q_MONEY` | 58 | `0x1D 14` `HAVE_ENOUGH_MONEY` | test wallet balance |
| `@Q_BANK_MONEY` | 11 | `0x1D 17` `HAVE_ENOUGH_MONEY_IN_ATM` | test bank balance |
| `@DEPOSIT_MONEY_BANK` | 11 | `0x1D 06` `ADD_TO_ATM` | add to bank/ATM balance |
| `@DRAW_MONEY_BANK` | 5 | `0x1D 07` `TAKE_FROM_ATM` | remove from bank/ATM balance |
| `@Q_MEMBER` | 18 | `0x1D 19` `HAVE_X_PARTY_MEMBERS` | test party member count |
| `@RAND` | 17 | `0x1D 21` `GENERATE_RANDOM_NUMBER` | stage random number |
| `@Q_EQUIP` | 1 | `0x1D 10` `CHECK_ITEM_EQUIPPED` | test equipped item/reference |

These should be safe to expose to romhackers as source aliases once operand
syntax is documented. They are much more readable than raw `0x1D` byte forms
and match already documented local C1 behavior.

## Inventory / Shop Aliases Still Needing Context

The inventory-macro lane still contains higher-level source helpers:

| Source command | Count | Current read |
| --- | ---: | --- |
| `@GET_ORDER_PLAYER` | 165 | source helper for selecting/order-indexing a party member |
| `@GET_PLAYER_GOODS` | 82 | source helper for selected-player item lookup |
| `@SEL_SHOP_TAKE` | 60 | shop selection/take helper |
| `@GET_CITEM` | 54 | current item helper |
| `@GET_TRANS_GOODS` | 31 | transfer item/goods helper |
| `@EQUIP_PLAYER_GOODS` | 16 | equipment application helper |
| `@Q_TRACY` | 12 | Tracy/Escargo storage predicate |
| `@DELIVERY` | 11 | delivery/Escargo service helper |
| `@GOODS_SELL_MONEY` | 9 | item sell-price/money helper |
| `@TRACY_IN` | 8 | Tracy/Escargo store-in helper |
| `@SET_TRANS_GOODS` | 7 | transfer item/goods staging helper |
| `@GOODS_TAKE_MONEY` | 5 | item purchase/take-money helper |
| `@SEL_TRACY_OUT` | 5 | Tracy/Escargo withdraw selection helper |
| `@WIN_SEL_ITEMQ` | 5 | item-selection window helper |
| `@GET_TRACY` | 4 | Tracy/Escargo storage helper |
| `@GET_TRACY_GOODS` | 4 | Tracy/Escargo item lookup helper |

These are probably not single raw opcodes. They likely expand to combinations
of `0x1A` selection helpers, `0x1D` inventory/money leaves, `0x19` data
producers, and `0x1C` display aliases.

## Source Contract For Reassembly

For this phase, the source contract should be:

- preserve direct display aliases such as `@DSP_NAME`, `@DSP_GOODS`, and
  `@DSP_NUM` as readable source forms over `0x1C`
- preserve direct inventory aliases such as `@GOODSIN_PLAYER`,
  `@GOODSOUT_PLAYER`, `@Q_GOODSFULL`, and `@Q_MONEY` as readable source forms
  over `0x1D`
- preserve higher-level shop/Escargo/display helpers as macros until their
  exact multi-command lowering is proven
- do not invent new runtime opcodes for authoring conveniences

This keeps the recovered source vocabulary useful for romhackers while staying
honest about what is locally proved.

## Confidence

High confidence:

- high-count direct display aliases are wrappers around `0x1C` print/display
  leaves
- high-count direct inventory and money aliases are wrappers around `0x1D`
  leaves
- `@DSP_ITEM` is selection-adjacent even though it shares the item-name display
  leaf with `@DSP_GOODS`

Medium confidence:

- unresolved display aliases stage actor/object/location context before normal
  display leaves consume it
- unresolved shop/Escargo aliases are multi-command source macros over `0x1A`,
  `0x19`, `0x1C`, and `0x1D`

Still open:

- exact operand syntax for each direct alias
- exact lowering for shop/Escargo helpers
- whether actor/object display aliases depend on event/actionscript state,
  text memory state, or both

## Next Proof

The next useful milestone-3 proof is a cleanup/closeout pass:

1. mark the control-flow macro lane as phase-good-enough with three focused
   lowering notes
2. mark display/inventory aliases as split into direct VM aliases versus
   source macros
3. decide whether remaining runtime-only leaves and parser artifacts need any
   new notes before milestone 3 closes
