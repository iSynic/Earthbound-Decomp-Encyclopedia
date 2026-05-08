# Timed Delivery Special Row `0x02A3`

This note records the current local read for the special timed-delivery row gated by flag `0x02A3`.

See also [timed-delivery-controller-499-500-common.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-controller-499-500-common.md).
See also [timed-delivery-warning-text-gates.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-warning-text-gates.md).

## Main result

The `0x02A3` row is no longer just a weird service-table outlier.

Its success-side script at `C7:A542` is the Zombie Paper delivery scene: a Mach-Pizza-Guy-family courier says that a weird guy asked him to deliver something to someone wandering around Threed, then hands over Apple Kid's item.

That makes the row best read as a special Apple Kid / Zombie Paper delivery case that reuses the Mach Pizza delivery actor family rather than an ordinary Escargo row.

## Script anchors

The row data in `D5:F645` uses:

- success pointer `C7:A542`
- failure pointer `C7:A7D9`
- flag `0x02A3`
- sprite/object descriptor id in the Mach-Pizza-Guy family

In the extracted script dump at [data_31.ccs](/F:/Earthbound%20Decomp%20-%20Codex/refs/eb-decompile-4ef92/ccscript/data_31.ccs):

- a phone-side script sets `flag 675` (`0x02A3`) and `flag 754`
- `C7:A542` is the delivery-success text and item handoff scene
- the scene explicitly says the courier was delivering pizza when a weird guy asked him to help out
- the delivered item is Apple Kid's thingamajig, which matches the Zombie Paper / Threed storyline context
- the success tail unsets `flag 675`
- the failure pointer `C7:A7D9` is effectively empty, just `eob`

## Why this helps the warning-text asymmetry

This special row was the main mismatch in [timed-delivery-warning-text-gates.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/timed-delivery-warning-text-gates.md):

- the teleport warning groups `0x02A3` with Escargo-style wording
- the Exit Mouse warning groups `0x02A3` with pizza-style wording

Now that the row itself is clearer, that asymmetry makes more sense. The row is not a pure Escargo row or a pure normal-pizza row. It is a special story delivery that uses the Mach Pizza delivery actor family while also living in the broader service-pending warning family.

So the safest current wording is:

- `0x02A3` is a special Mach-Pizza-Guy-family delivery row for Apple Kid's Zombie Paper handoff
- the mixed warning text is best treated as script-side categorization drift around that hybrid case, not as evidence that the local row decode is wrong

## Reference-side cross-check

The third data dump still helps here too. In [timed_delivery_table.yml](/F:/Earthbound%20Decomp%20-%20Codex/refs/eb-decompile-4ef92/timed_delivery_table.yml), row `7` has:

- event flag `0x2A3`
- sprite group `151`
- a five-second timer
- success pointer `C7:A542`
- failure pointer `C7:A7D9`

That matches the local row shape and the extracted script anchors cleanly.
