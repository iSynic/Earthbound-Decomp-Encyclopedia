# C2 Late Normalization And Odor Runtime Polish

This note records the byte-neutral source polish pass over the late
normalization/metamorphosis and condiment/odor continuation leaves.

Primary source modules:

- `src/c2/c2_af1f_snapshot_restore_battler_normalization_context.asm`
- `src/c2/c2_b172_resolve_late_normalization_and_odor_continuation.asm`

Related evidence:

- `notes/class2-late-normalization-and-odor-family-c29051-c29254.md`
- `notes/c2-ef-battle-text-contract-workahead.md`
- `notes/data-contracts-c0-c4.md`
- `notes/bank-c9-text-data-map.md`
- `refs/EB-M2-Listing-v1/US/bank09.txt`
- `refs/EB-M2-Listing-v1/US/bank2F.txt`

## Metamorphosis Snapshot Path

`C2:AF1F` still keeps its cautious source name,
`SnapshotRestoreBattlerNormalizationContext`, because the byte corridor is
mostly pointer merge work. The runtime tail now has named local contracts for
the stable pieces:

- enemy records use stride `$005E`
- enemy row `+0x5D` is the `mirror_success` byte
- the roll gate uses the shared `C2:6A2D` / `GetRandomBelow` helper with limit
  `$0064`
- the temporary battler staging block is `$AA14`, with `$AA12` carrying the
  selected battler id and `$AA62 = $0010` marking the staging mode
- success emits `EF:6A99` (`MSG_BTL_METAMORPHOSE_OK`)
- failure emits `EF:6AB3` (`MSG_BTL_METAMORPHOSE_NG`)

The direct battle-text call is now named as the `C1:DC1C` far-pointer dispatch
ABI, keeping `$0E/$10` visibly tied to an EF battle-text script pointer.

## Condiment Continuation

`C2:B172` is now clearer as the late condiment continuation used by the
normalization/odor neighborhood.

Stable promoted anchors:

- `C1:DB33` is the far `FIND_CONDIMENT` helper used to look up the condiment
  candidate for the selected food item
- `C1:8EAD` is the active-inventory search/removal helper used after a
  condiment is found
- `D5:EA77` is the 7-byte condiment-rule table; this source leaf scans rule
  rows and stages the effect byte as the base for the later recovery result
- matched/missed condiment text uses C9 scripts `MSG_BTL_EAT_SPICE_ATARI` at
  `C9:7C9D` and `MSG_BTL_EAT_SPICE_HAZURE` at `C9:7CB1`
- fallback item recovery uses the `D5:5000` item table, stride `$0027`, params
  field `+0x1F`
- the later party-member gate uses stride `$005F` and still preserves the
  original special-case id `4` behavior with a named local constant rather than
  over-explaining it
- blocked status continues to emit the shared no-effect script `EF:766E`, then
  returns through the neighboring stat-consequence return tail at `C2:B606`
  without running the optional `C2:B5E3` control-byte dispatch

## Remaining Soft Spots

- The exact gameplay identity of party member id `4` in this corridor is still
  intentionally local.
- The `B172` module boundary still rejoins a neighboring stat-consequence
  return tail; the no-effect route now names that `C2:B606` edge, but the
  broader post-`B2E0` continuation remains cross-module.
- The `AF1F` pointer-copy body still needs a future field-by-field cleanup once
  the selected-row snapshot layout has stronger local evidence.
