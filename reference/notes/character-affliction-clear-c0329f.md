# Character Affliction Clear `C0:329F`

This note covers the first new audit-led `C0` gap after the entity placement pass.

## Reference Status

- `ebsrc-main` still labels this body as `UNKNOWN_C0329F`.
- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank00.asm` places it after `adjust_position_vertical.asm` and immediately before `UNKNOWN_C032EC`, `UPDATE_PARTY`, and the `$986F/$988B` registry builders.
- Direct control-flow xrefs were not found locally, so this is likely reached through an indirect pointer path or a caller shape not covered by the current xref helper.

## Working Names

- `C0:329F` = `Clear_CharacterAfflictionBytes`

## Working Model

Suggested local name:

- `Clear_CharacterAfflictionBytes`

Input:

- `A` = character/party record selector accepted by `C0:8FF7` with stride selector `#$005F`

Behavior:

1. Save input `A` in the local DP frame.
2. Call `C0:8FF7` with `Y = #$005F`.
3. Use the result as an offset into the party-character record family rooted at `$99CE`.
4. Clear seven bytes starting at `$99DC + offset`.

The current curated WRAM lookup identifies:

```text
$99CE = PARTY_CHARACTERS root
record stride = $005F
$99DC = PARTY_CHARACTERS + $0E
$99DC..$99E2 = afflictions[0..6]
```

So this routine mechanically clears the seven-byte affliction/status group for one character record.

The byte loop is straightforward:

```text
offset = MapIndex(A, $005F)
for i in 0..6:
    byte[$99DC + offset + i] = 0
```

## Why This Matters

Several older notes described `$99DC` as a per-slot selector/state byte because many C1/C2 consumers branch on values loaded from that address family. The WRAM map now gives the cleaner base identity: those selector-like values are the first affliction/status byte inside each party-character record.

That does not invalidate the observed reader behavior. It narrows it:

- `$99DC` is `afflictions[0]`, not an arbitrary object selector.
- `$99DD..$99E2` are the companion affliction/status bytes cleared by the same helper.
- C2 readers that treat `$99DC == 1/2/3/4` as state classes are reading encoded status/affliction state, not an unrelated dispatch selector.

This also strengthens the existing battle-side notes that connected exported row byte `+0x1D` back into live `$99DC`: they are projecting a status/affliction byte back into the party-character struct.

## Naming Caution

The reference map calls the first byte `afflictions[0] (PERSISTENT_EASYHEAL)`, but the exact value map for every observed `$99DC` value still belongs in the C2 status/action notes. This helper proves the clear span and character-record root; it does not by itself label every status value.

## Next Seam

`C0:32EC` is already covered by the `$986F/$988B` registry notes, so the next seam should be selected from the refreshed progress audit rather than hard-coded here. Keeping future addresses out of this note prevents the audit from counting them as locally documented before they have a real write-up.
