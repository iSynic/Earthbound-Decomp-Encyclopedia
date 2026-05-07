# Text Engine Entry, Wait, and Window Gates (`C1:0000-C1:07AF`)

This note captures the current best local read of the early bank-`01` text-engine helper strip around `C1:0000..C1:07AF`.

The `ebsrc-main` bank map is useful corroboration here: this area is interleaved with named text helpers such as `enable_blinking_triangle`, `get_window_focus`, `close_focus_window`, `lock_input`, `unlock_input`, `text/ccs/halt`, and `get_active_window_address`, while several glue routines remain in `unknown/C1/*.asm`.

## Main result

The early C1 strip is not a mystery command-family region. It is a compact text-engine service layer:

Source-scaffold promotion:

- `C1:0000..0166` is now decoded source through the shared prompt/input wait
  gate boundary.
- `C1:0166..02D0` is now decoded source for the shared `0x13`/`0x14`
  halt-control worker.
- `C1:02D0..0301` is now decoded source for the `$9641` text-state wait.
- `C1:0301..078D` is now decoded source for the active interaction/text
  context helper family and window descriptor bind path.
- `C1:078D..07AF` is now decoded source for the tilemap staging initializer.
- The source-promoted files are
  `src/c1/c1_0000_run_text_display_setup_wrapper.asm`,
  `src/c1/c1_0004_process_textbox_data_from_caller_pointer.asm`,
  `src/c1/c1_004e_pump_text_wait_frame.asm`,
  `src/c1/c1_008e_close_and_drain_all_windows.asm`,
  `src/c1/c1_00d6_wait_text_ticks.asm`, and
  `src/c1/c1_00fe_wait_for_text_prompt_or_input_gate.asm`,
  plus `src/c1/c1_0166_run_text_halt_control_worker.asm`,
  `src/c1/c1_02d0_wait_for_text_state_flag9641.asm`, and the
  `C1:0301..07AF` context/window helper modules.
- The promoted source still validates through the durable C1 scaffold:
  `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

## Working Names

- `C1:0000` = `RunTextDisplaySetupWrapper`
- `C1:0004` = `ProcessTextboxDataFromCallerPointer`
- `C1:004E` = `PumpTextWaitFrame`
- `C1:008E` = `CloseAndDrainAllWindows`
- `C1:00FE` = `WaitForTextPromptOrInputGate`
- `C1:0166` = `RunTextHaltControlWorker`
- `C1:02D0` = `WaitForTextStateFlag9641`

- entry wrappers for starting or resuming text processing
- tiny latches for blinking prompt and text sound/display mode state
- a shared frame pump used by text waits
- window focus close/drain helpers
- input locks and counted waits
- halt/prompt gates that bridge script commands to window redraw and joypad state
- active-window descriptor lookup for later memory and cursor helpers

## Entry wrappers and latches

`C1:0000` is a far-call wrapper around the local helper at `C1:0A1D`.

It simply calls `C1:0A1D` and returns long. The surrounding reference include still calls it `unknown/C1/C10000.asm`, but structurally it is just an exported entry veneer into the lower text print/helper strip.

`C1:0004` is the larger text-entry wrapper already seen from script and transition callers. It stages the caller pointer from `$20/$22`, enters the `C0:943C` setup region, calls the main textbox-data processor at `C1:86B1`, ticks `C1:2DD5` until `$B4A8 == FFFF`, then leaves through `C0:9451`.

`C1:0036`, `C1:003C`, `C1:0042`, and `C1:0048` are tiny state latches:

- `C1:0036` stores the accumulator into `$964D`
- `C1:003C` clears `$964D`
- `C1:0042` returns `$964D`
- `C1:0048` stores the accumulator into `$964F`

The reference map names the first three as blinking-prompt helpers and `C1:0048` as `set_text_sound_mode`, which fits the shape of these single-slot state setters/getters.

## Frame and Window Pump

`C1:004E` is the shared text/wait frame pump.

It first checks `$89C9 & 00FF`; if set, it calls `C3:E450`. Then it branches on `$9643`: when nonzero it calls `C4:3568`, otherwise it performs the normal frame service chain through `C0:88B1`, `C0:9466`, `C0:8B26`, and `C0:8756`.

`C4:3568` is that alternate `$9643` mode path: it waits one frame through `C0:8756`, then ticks the battle-background/palette effect updater at `C2:DB3F`. That makes `C1:004E` the right abstraction for "advance one text/overworld wait frame", with a battle-background update path when battle text display mode is active.

`C1:0078`, `C1:007E`, and `C1:0084` are the reference-named focus helpers:

- `C1:0078` returns `$8958`
- `C1:007E` stores the accumulator into `$8958`
- `C1:0084` closes the currently focused window by passing `$8958` to `C3:E521`

`C1:008E` drains all queued/current windows rather than only the focus slot. It sets byte `$5E70` while repeatedly resolving `$88E2` through the `$8650` window table and calling `C3:E521`; after no more `$88E2` window remains, it runs `C3:E4CA`, `C1:2DD5`, clears `$5E70`, and calls `C4:3F53`.

So the safest name for `C1:008E` is a close/drain-all-windows helper. The reference symbol `REDIRECT_C1008E` reinforces that this routine is exported through a redirect rather than being a text command by itself.

## Input Locks and Wait Gates

`C1:00C7` and `C1:00D0` are the reference-named input lock pair:

- `C1:00C7` sets `$9645 = 1`
- `C1:00D0` clears `$9645`

`C1:00D6` is a counted text tick wait. It stores the incoming count, refreshes window/text state through `C3:E4CA` and `C1:2DD5`, then calls the window tick at `C1:2E42` until the count expires.

`C1:00FE` is the input-gated prompt/pause wait used underneath halt-like text controls.

Its shape is:

- take the incoming accumulator as an optional tick count
- in the `$436C != 0 && $4DC2 == 0` path, tick `C1:2E42` until `$006D & A0A0` reports an accepted input
- while input is locked by `$9645`, allow the `$006D & 8010 == 8010` debug/control chord to clear the lock
- use the explicit count when nonzero, otherwise fall back to `$964B`
- tick `C1:2E42` until either the count expires or `$006D & A0A0` indicates input

This is why opcode notes for `0x03`, `0x10`, `0x13`, and `0x14` should describe `C1:00FE` as the shared low-level wait/prompt gate, not as a standalone command family.

`C1:0166..02D0`, immediately after this cluster, is the larger shared halt/control worker for text commands `0x13` and `0x14`.

The source version makes the mode split clearer:

- it waits for input lock `$9645` to clear, with the `$006D & 8010 == 8010`
  debug/control chord as an escape when `$436C` is active
- it refreshes text/window state through `C3:E4CA` and `C1:2DD5`
- in battle-text display mode, it can service `EF:0256`, or delegate to
  `C1:00FE` when `$964B` supplies the low-level wait gate
- it resolves the active descriptor through `$8958 -> $88E4 -> C0:8FF7 ->
  $8650`
- mode `0` waits for `$006D & A0A0`
- the prompting mode alternates the two small prompt tiles at `C3:E416` and
  `C3:E418`, then writes the accepted/wait pair at `C3:E41A`
- each prompt tile upload goes through `C0:8616`, and completion flows through
  `EF:026E`

## Text-State Wait

`C1:02D0` is a wait-until-text-state gate.

It clears `$9641`, refreshes window/text state through `C3:E4CA` and `C1:2DD5`, then loops until `$9641` becomes nonzero. During the loop it calls the shared frame pump at `C1:004E`. There is also a debug/control escape when `$436C` is active and `$0065` has both `$1000` and `$2000` set.

On normal completion it clears `$9641` again before returning. The best current name is "wait for text state/event flag `$9641`", with the caveat that the producer of `$9641` should be documented from its callers before we give the flag a more specific user-facing name.

## Active Window Context

`C1:0301` begins the next named helper run. It resolves the active text window descriptor:

- if `$88E0 == FFFF`, return the fallback descriptor base `$85FE`
- otherwise use focus index `$8958`, lookup `$88E4[index]`, multiply by descriptor size `$52` through `C0:8FF7`, and return `$8650 + offset`

The memory helpers after it operate on offsets inside this descriptor. The source scaffold now carries this full front strip as assembly: `C1:0000..C1:0301` sets up entries, waits, prompt/input gates, and window focus state; `C1:0301..078D` handles descriptor-field access and descriptor binding; `C1:078D` begins the tilemap/rendering primitive layer.

## Practical Conclusion

The early bank-`01` unknowns `C1:0000`, `C1:004E`, `C1:00FE`, and `C1:02D0` are now locally explained as text-engine glue, not as independent gameplay routines.

This also tightens the lower text-command notes: the script opcodes are small leaves, while this area is the shared machinery that makes those leaves wait, prompt, close windows, and advance text frames.

## Working Names

- `C4:3568` = `PumpBattleBgEffectFrameAndPollInput`
