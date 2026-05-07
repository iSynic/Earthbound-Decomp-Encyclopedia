# Text Command Loaded-String Pointer Finalizers (`C1:7796-C1:7AE3`)

This note covers the loaded-string helper cluster at `C1:7796`, `C1:7889`, and `C1:78F7`.

See also [text-command-family-19-data-and-substitution.md](notes/text-command-family-19-data-and-substitution.md) and [text-entry-builder-c113d1-89d4.md](notes/text-entry-builder-c113d1-89d4.md).

## Main Result

`C1:7796` is the pointer-backed loaded-string finalizer for the `0x19 02` command family.

## Source Promotion

This cluster is now promoted as decoded source modules:

- `src/c1/c1_7796_finalize_loaded_string_with_companion_pointer.asm` (`C1:7796..C1:7889`)
- `src/c1/c1_7889_continue_loaded_string_inline_collector.asm` (`C1:7889..C1:78F7`)
- `src/c1/c1_78f7_start_loaded_string_inline_collector.asm` (`C1:78F7..C1:7AE3`)

Source polish follow-up (2026-05-06): the `C1:78F7..7AE3` source now names the
adjacent `0x18` window-family dispatcher helpers and callback return targets
that share this module. The loaded-string collector behavior is unchanged, but
the module boundary is clearer: the first entry stages `0x19 02` bytes, while
the later dispatcher front names close/drain/clear window helpers, managed-slot
snapshotting through `C20A20`, and the open/switch/selection/status callback
low words.

## Working Names

- `C1:7796` = `FinalizeLoadedStringWithCompanionPointer`
- `C1:78F7` = `StartLoadedStringInlineCollector`
- `C1:7889` = `ContinueLoadedStringInlineCollector`

The reference macro file corroborates the byte-level format:

- `EBTEXT_LOAD_STRING_TO_MEMORY_WITH_SELECT_SCRIPT ptr` emits `$19, $02`, the string body, `$01`, then a dword pointer
- `EBTEXT_LOAD_STRING_TO_MEMORY str` emits `$19, $02`, the string body, then `$02`

That matches the local callback split:

- ordinary string bytes are collected into `$97D7` by `C1:78F7` and `C1:7889`
- terminator `01` null-terminates `$97D7`, clears `$97CA`, and returns callback `C1:7796` to collect the following dword
- terminator `02` null-terminates `$97D7` and immediately installs it through `C1:13D1` with a zero companion pointer

So the best current name for this small cluster is a loaded-string-to-memory state machine, with `C1:7796` as the select-script or companion-pointer finalizer.

## Inline String Collector

`C1:78F7` is the entry used by the `0x19 02` dispatcher:

1. take the current text byte from `X`
2. store its low byte at `$97D7 + $97CA`
3. increment `$97CA`
4. return callback low word `C1:7889`

`C1:7889` then continues the same stream:

- if the byte is `01`, write a zero terminator into `$97D7 + $97CA`, clear `$97CA`, and return `C1:7796`
- if the byte is `02`, write a zero terminator, set source pointer `$0E/$10` to `$97D7`, set companion pointer `$12/$14` to zero, call `C1:13D1`, and return zero
- otherwise append the byte to `$97D7 + $97CA`, increment `$97CA`, and return `C1:7889`

The `$97D7/$97CA` pair is therefore a temporary inline loaded-string buffer and cursor for this command family, not the final display record itself.

## Pointer-Backed Finalizer

`C1:7796` is entered after the inline collector sees terminator byte `01`.

Its first phase collects the following dword one byte at a time:

- while `$97CA < 3`, store the current byte into `$97BA + $97CA`
- increment `$97CA`
- return callback low word `C1:7796`

On the fourth byte, it assembles a 32-bit pointer from:

- current byte shifted left by 24
- `$97BC` shifted left by 16
- `$97BB` shifted left by 8
- `$97BA`

It then prepares the shared text-entry builder inputs:

- `$0E/$10` = pointer to the loaded string in `$97D7`
- `$12/$14` = the assembled dword pointer
- `JSR C1:13D1`

After the builder call it returns zero, ending this command continuation chain.

## Relation to `C1:13D1`

The important boundary is that this cluster does not itself display or interpret the loaded string. It stages one inline string, optionally pairs it with a following dword pointer, and hands both pieces to the shared `$89D4` text-entry builder.

The exact meaning of the companion pointer is still softer than the byte mechanics. The reference macro name `LOAD_STRING_TO_MEMORY_WITH_SELECT_SCRIPT` makes "select script" a good candidate label, but the locally proved behavior is narrower: `C1:7796` installs `$97D7` with an extra caller-supplied dword in the companion pointer slots consumed by `C1:13D1`.

## Practical Conclusion

The unknown start `C1:7796` is now covered as the hidden dword-continuation finalizer for `0x19 02` loaded strings. Together with `C1:78F7` and `C1:7889`, it accounts for both reference macro endings:

- `... string, 02` installs the loaded string directly
- `... string, 01, dword` installs the loaded string with an additional pointer-backed companion script
