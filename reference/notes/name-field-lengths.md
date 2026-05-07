# Naming Screen Field Lengths

## Favorite Food Gotcha

`$C1FA23` is not the favorite-food input length. In the US listing:

```asm
C1FA20: A9 28 00        LDA #NAME_THEM_STRING_LENGTH
C1FA23: 85 12           STA @LOCAL01
...
C1FA2B: A2 1F 98        LDX #.LOWORD(GAME_STATE) + game_state::favourite_food
C1FA2E: A9 06 00        LDA #.SIZEOF(game_state::favourite_food)
C1FA31: 20 04 EC        JSR NAME_A_CHARACTER
```

The `$28` loaded at `C1FA20` is the length of the "Please name..." prompt string. The actual destination buffer length passed to `NAME_A_CHARACTER` is the `$0006` immediate at `C1FA2E`.

Changing only that input length is not safe, because `favourite_food` is a fixed 6-byte field inside `game_state`.

## Relevant `game_state` Layout

Base shown by listing references is `GAME_STATE = $97F5`.

| Field | Address | Size |
| --- | ---: | ---: |
| `pet_name` | `$9819` | 6 |
| `favourite_food` | `$981F` | 6 |
| `favourite_thing` | `$9825` | 12 |
| `favourite_thing + 4` custom PSI part | `$9829` | normally 6-byte input |
| `money_carried` | `$9831` | 4 |

So if favorite food is allowed to exceed its 6-byte field, it overwrites the beginning of `favourite_thing`. This matches the observed confirmation-screen corruption where the food tail joins onto the custom PSI name.

## Text Field Table

Bank `C4` also has fixed field descriptors used by text/name printing:

```asm
C45512: 0C F5 97   ; mother2_playername, 12
C45515: 18 01 98   ; earthbound_playername, 24
C45518: 06 19 98   ; pet_name, 6
C4551B: 06 1F 98   ; favourite_food, 6
C4551E: 0C 25 98   ; favourite_thing, 12
```

This table is another place that must be considered if fields are relocated or resized.

## Practical Options

Safest short hack: keep favorite food at 5 visible characters plus terminator, and only lengthen/customize favorite thing within the existing `favourite_thing` budget.

Real longer favorite food: relocate it or expand `game_state`, then patch all fixed pointers/lengths:

- naming input destination and length
- confirmation-screen `STRLEN` / `PRINT_STRING` pointers
- text-control-code field table in bank `C4`
- any event/text references to `$981F`
- save/SRAM layout and checksum/version assumptions if the struct size changes

Changing only the immediate at `C1FA2E` will make the input accept more characters, but it turns into a controlled buffer overflow into `favourite_thing`.
