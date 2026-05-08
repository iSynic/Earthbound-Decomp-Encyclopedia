# Timed Delivery Warning Text Gates

This note records the user-facing script gates that warn the player not to teleport or use the Exit Mouse while timed-delivery or customer-arrival services are pending.

See also [timed-delivery-controller-499-500-common.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-controller-499-500-common.md).
See also [timed-delivery-state-helpers-ef0f60-fdb-ff6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-state-helpers-ef0f60-fdb-ff6.md).
See also [selector-row-config-family-ef0ee8.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/selector-row-config-family-ef0ee8.md).
See also [timed-delivery-system-flags-754-779.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-system-flags-754-779.md).
See also [timed-delivery-special-row-02a3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-special-row-02a3.md).

## Main result

The extracted text scripts now give a strong gameplay-side cross-check for the timed-delivery subsystem.

Both the teleport warning script and the Exit Mouse warning script branch on the same delivery-style event flags that appear in the `D5:F645` timed-delivery table, and they resolve those flags into three user-facing pending-service categories:

- pizza pending
- customer pending
- Escargo Express pending

That is much stronger than a vague thematic match. The script-side flag groups line up directly with the local row-family decode.

## Teleport warning script

In [data_32.ccs](/F:/Earthbound%20Decomp%20-%20Codex/refs/eb-decompile-4ef92/ccscript/data_32.ccs), the script at `C7:C865` is the specialized branch behind the generic line:

- `"You cannot teleport now."`

It then dispatches to more specific warning text by pending flag:

- `flag 0x00B4` -> `"You should wait to teleport until after the pizza arrives."`
- `flags 0x01BE / 0x0286 / 0x0287 / 0x0288` -> `"You should wait to teleport until after a customer has shown up."`
- `flags 0x00B5 / 0x0285 / 0x02A3 / 0x02B6 / 0x02B7` -> `"You should wait to teleport until after Escargo Express arrives."`

There is also a separate Dungeon Man case at `0x02F4`, which is clearly outside the timed-delivery family.

## Exit Mouse warning script

In [data_60.ccs](/F:/Earthbound%20Decomp%20-%20Codex/refs/eb-decompile-4ef92/ccscript/data_60.ccs), the Exit Mouse refusal script uses the same delivery-side split:

- `flag 0x00B4` -> `"You shouldn't let the mouse go until the pizza has arrived."`
- `flags 0x01BE / 0x0286 / 0x0287 / 0x0288` -> `"If you release the mouse now, it might be stepped on by the approaching customer."`
- `flags 0x00B5 / 0x0285 / 0x02B6 / 0x02B7` -> `"Please stick around until Escargo Express arrives."`
- `flag 0x02A3` -> pizza-style wording again

That last case is especially useful, because it matches the local row picture where `0x02A3` is a Mach-Pizza-Guy-family entry rather than a plain Escargo row. The row now has its own focused note in [timed-delivery-special-row-02a3.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-special-row-02a3.md).

## Crosswalk to the local timed-delivery rows

These message groups line up neatly with the current best `D5:F645` row decode:

- `0x00B4` = pizza row
- `0x00B5`, `0x0285`, `0x02B6`, `0x02B7` = Escargo-style rows
- `0x01BE`, `0x0286`, `0x0287`, `0x0288` = customer-side rows
- `0x02A3` = special Mach Pizza / HoiHoi row

So the local row-family split is now supported by both:

- controller-side helpers in bank `EF`
- player-visible warning text in extracted script data

## Why this matters for `$5D98`

This does not prove that `$5D98` is the one exact flag source tested by those scripts.

But it does strengthen the broader interpretation from [timed-delivery-state-helpers-ef0f60-fdb-ff6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-state-helpers-ef0f60-fdb-ff6.md): the game really does have a shared pending-service state family that blocks teleport-style escape systems while pizza, customer, or Escargo arrivals are active.

That makes it much easier to believe that `$5D98` is a broader service-pending latch rather than a tiny one-off animation flag.
