# Short-Text Staging Buffer `$9C9F`

This note captures the current best local model for WRAM buffer `$9C9F` in the bank-`01` text and menu side.

See also [naming-buffer-commit-family-c1ead6-c4d065.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/naming-buffer-commit-family-c1ead6-c4d065.md), [statistic-selector-family-c4550f-c3ee7a.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/statistic-selector-family-c4550f-c3ee7a.md), [text-command-family-19-data-and-substitution.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-command-family-19-data-and-substitution.md), and [text-entry-builder-c113d1-89d4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-entry-builder-c113d1-89d4.md).

## Main result

`$9C9F` is now best read as a broader short-text staging buffer, not as a naming-only field and not as the same thing as selector-`2` backing buffer `$9801`.

The clearest local split is:

- `$9C9F` = live short-text staging buffer reused by naming and non-naming menu/text producers
- `$9801` = naming-side committed normalized buffer
- `$97F5` = naming-side direct-copy companion buffer

That boundary is healthier than the older "selector-`2` as general temp string" model, because the non-naming producers we have pinned so far write to `$9C9F` and then feed shared text-entry or display builders without any proved commit into `$9801`.

## Strong local non-naming producers

The strongest pinned non-naming writers are:

- `C1:9963`
- `C1:A103`
- `C1:A86D`

All three are bank-`01` item or equipment-side paths.

Common structure:

- they resolve an item record from `D5:5000`
- they stage text-like record data into `$9C9F` or `$9CA0`
- they then hand that staged buffer to shared bank-`01` builders

The two common builder-side families visible from these paths are:

- [text-entry-builder-c113d1-89d4.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/text-entry-builder-c113d1-89d4.md), the broader live text-entry allocator/installer
- `C1:0EFC` plus nearby menu/display helpers, especially in the equipment preview side

So the clean local model is that item/equipment paths reuse `$9C9F` as a short-text work area rather than materializing stable selector buffers directly.

## `C0:8ED2`

One useful correction falls out of these callers:

`C0:8ED2` takes:

- source from long pointer `$0E`
- destination from `A`
- copy length from `X`

Locally it copies 16-bit words, so odd byte counts should be treated cautiously. The important part for this note is the calling convention:

- bank-`01` item/equipment callers set `A = $9C9F` or `$9CA0`
- naming commit sets `A = $97F5`

That means the function is a generic bulk copy helper around the staging buffer family, not a `$9801`-specific writer.

## Naming-side bridge stays separate

The naming-side commit note still holds:

- `C1:EBA0..EBDD` treats `$9C9F` as the current naming-entry work buffer
- `C4:D065` remaps that staged text into `$9801`
- `C0:8ED2` copies the same staged text into `$97F5`

So the naming path is now best read as one specific commit use of the broader `$9C9F` staging family, not as proof that every `$9C9F` producer also commits into the selector buffers.

## Why this matters for selector `2`

This is the strongest current negative evidence against a broad selector-`2` temp-buffer identity:

- raw immediate setup of `$9801` is still only pinned in the naming path
- the non-naming bank-`01` producers we have pinned so far stop at `$9C9F` and shared builders
- no non-naming local bridge from `$9C9F` into `$9801` is currently proved

So the safest current read is:

- selector `2` stays closer to a committed player-name buffer
- broader reusable short-text staging belongs to `$9C9F`

## Confidence boundaries

### Locally proved

- `C1:9963 / A103 / A86D` write to `$9C9F`
- those paths are non-naming item/equipment-side producers
- `C1:EBA0..EBDD` also uses `$9C9F`, but commits it into `$9801` and `$97F5`
- `C0:8ED2` takes source from `$0E`, destination from `A`, and length from `X`

### Still open

- the exact per-caller semantic role of the staged text in each non-naming producer family
- whether any non-naming producer later commits `$9C9F` into one of the stable selector buffers
- whether `$9CA0` should be treated as just the second byte of the same staging buffer or as a meaningful sibling entry point in some callers

## Best current interpretation

The safest current interpretation is that `$9C9F` is the bank-`01` short-text staging buffer that multiple UI and text-side systems reuse before handing data to downstream builders. The naming subsystem has one proved commit bridge from that staging buffer into stable selector-backed fields, but the item/equipment-side producers do not currently show the same commit behavior.
