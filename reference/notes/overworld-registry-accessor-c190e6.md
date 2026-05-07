# Overworld Registry Accessor (`C1:90E6`)

This note covers the small remaining unknown start `C1:90E6`.

See also [overworld-entity-type-registry-9887-98a4.md](notes/overworld-entity-type-registry-9887-98a4.md) and [mushroomized-walking-remap-family.md](notes/mushroomized-walking-remap-family.md).

## Main Result

`C1:90E6` is a one-based accessor into the derived active-overworld type list at `$988B`.

## Working Names

- `C1:90E6` = `ReadActiveOverworldRegistryTypeCode`

Source-scaffold promotion:

- `C1:90E6..90F1` is now decoded source in `src/c1/c1_90e6_read_active_overworld_registry_type_code.asm`.
- The same module also covers `C1:90F1..913D`, now named `CheckEscargoStorageQueueFull`.
- The combined C1 scaffold validates byte-for-byte after promotion: `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

The whole routine is:

1. take the incoming `A`
2. convert it to a zero-based index with `DEX`
3. read byte `$988B + index`
4. return it zero-extended

So mechanically:

`return byte($988B[A - 1])`

## Why `$988B` Matters Here

The newer registry notes identify `$988B` as the sorted active type-code layer built from the broader source array at `$986F`. It sits beside:

- `$9891`: compact live-slot offsets
- `$9897`: live entity slot words
- `$98A3`: active registry-entry count
- `$98A4`: active party-member count / leading party-code boundary

That gives `C1:90E6` a cleaner role than "anonymous RAM byte reader." It returns the active type code for an ordinal position in the derived registry list.

## Confidence Boundary

The routine itself is trivial and high-confidence. The only reason to keep the name slightly broad is that `$988B` is shared by several overworld and text-side consumers. This helper returns the registry code; it does not by itself prove the caller's higher-level gameplay purpose.
