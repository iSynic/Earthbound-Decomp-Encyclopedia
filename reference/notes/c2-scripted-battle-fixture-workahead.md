# C2 Scripted Battle Fixture Workahead

This note records the next autonomous runtime-proof accelerator after the
numbered Mesen save-state scout. It is a workahead note, not proof-grade
evidence and not a source-promotion basis.

## Goal

Build an ignored fixture ROM that can enter a chosen scripted battle without a
user-provided `.mss` save state, then steer one enemy/action condition for C2
trace-oracle work.

The target entry is `C2:2F38` / `INIT_BATTLE_SCRIPTED`, not the later debug
`C2:4821` battle routine. `INIT_BATTLE_SCRIPTED` still reads the D0 battle-entry
pointer table, expands the enemy-list payload into `$9F8A/$9F8C`, sets `$4DC2`,
runs the battle swirl path, waits for transition completion, and enters common
battle init.

## Proposed Fixture Shape

- Scenario id: `scripted-entry-group0-force-enemy-action`.
- Patch `D0:D52D`, the existing group-0 enemy-list payload, to a compact list:
  `01 <enemy_id lo> <enemy_id hi> FF`.
- Keep `D0:C60D` group 0 pointing at `D0:D52D` unless a later proof requires a
  new payload island.
- Patch the chosen enemy's D5 action fields for deterministic behavior:
  `action_order`, `action_1..4`, optional `final_action`, and optional HP/speed.
- Reuse existing `tools/build_c2_fixture_roms.py` action-row steering helpers
  for lanes such as Flash/status, PSI Magnet, PP reduction, and `C2:40A4`.
- Add the smallest possible autostart hook that loads `A = #$0000` and calls
  `JSL C22F38_InitBattleScripted`.

## Implementation Checkpoint

- `tools/build_c2_fixture_roms.py` now builds
  `scripted-entry-group0-force-enemy-action`.
- The first tested `C0:B810` main-loop prelude hook did not trigger from a
  cold-boot neutral-input Mesen run, so it is not the primary no-save hook.
- The scenario now patches `C0:B9B4` to `A9 00 00 22 38 2F C2 60`,
  replacing the `GAME_INIT` tail (`STZ DEBUG; JSL MAIN_LOOP; RTS`) with
  `LDA #$0000; JSL C2:2F38; RTS`.
- The `C0:B9B4` hook runs after SRAM, music, NMI/joypad, hardware check, and
  two frame waits, but before the normal main-loop intro/file-select setup.
- The scenario patches `D0:D52D` to `01 79 00 FF`, making group 0 contain one
  Runaway Dog enemy row (`121` / `$0079`).
- The same scenario patches only that enemy row's normal-action slots to action
  `248`, the Neutralize/all row that reaches `C2:90C6 -> C2:40A4`.
- The row is also made durable and fast (`HP = 999`, `speed = 255`) so simple
  command-confirm input patterns have a better chance of letting the fixture
  action resolve before the trace budget expires.
- `tools/run_c2_battle_trace_oracle_mesen.py` now supports
  `--wram-patch-timing first-breakpoint`, which applies WRAM seeds at the first
  traced hook instead of before reset clears RAM. This is needed for no-save
  fixture ROMs that cold-boot through `GAME_INIT`.
- This is still fixture-ROM reachability evidence only. The first successful
  run should be treated as a smoke test that proves the hook reaches `C2:2F38`,
  not as ordinary game behavior.

## Smoke Results

- `C0:B810` hook attempt: no startup or C2 hits under a 4200-frame neutral-input
  cold boot, because the target was not a true executed instruction boundary.
- `C0:B9B4` hook attempt: cold boot reached `C0:B9B4`, `C2:2F38`, `C2:E8E0`,
  `C2:E9C8`, and `C0:52AA` under the same provenance-enhanced oracle.
- Delayed party-state WRAM seeding moved the fixture through `BATTLE_ROUTINE`,
  `C2:4CEF`, and the battle text-window open call at `C2:4EEC -> C1:DD47`.
- A neutral delayed-party run stalled inside `CREATE_WINDOW` before allocator
  entry because cold-boot window maps were zeroed, making window `0E` look
  already bound.
- A fixture-only window reset seed (`$88E0/$88E2/$8958 = FFFF`, logical window
  maps and allocation markers initialized to `FFFF`) moved the run through
  `C1:0528`, `C3:E4EF`, `C1:078B`, `C2:4EF6`, `C2:4F03`, and `C1:DC1C`.
- Adding an A-pulse input pattern after that same seed produced the first no-save
  scripted-entry `C2:40A4` minimum hit. The reviewed raw trace also observed the
  wrapper/callsite corridor `C2:90C6 -> C2:915C -> C2:40A4`, loop returns near
  `C2:4104`/`C2:4159`, downstream `C2:5D3D`/`C2:6088`, and dispatch target
  `C2:9051`.
- This result supersedes the earlier no-save smoke blocker, but remains
  fixture-steered reachability and wrapper-mechanics evidence. It does not prove
  natural Bash behavior or ordinary encounter provenance.

## Proof Boundary

This fixture can prove fixture reachability and downstream helper mechanics. It
cannot prove ordinary overworld encounter provenance, natural enemy action
probabilities, natural C1 command-menu routing, or any C2 source semantics
without a reviewed trace result.

The first success criterion is only:

- generated ROM boots far enough to call `C2:2F38`
- the trace observes `C2:E8E0` or the common battle-init route
- a chosen downstream target, such as `C2:40A4`, `C2:724A`, `C2:9F5E`, or
  `C2:8E42`, becomes reachable without a user save state

## Files To Touch

- `tools/build_c2_fixture_roms.py`: add the scenario, D0 payload patch, D5 enemy
  row patching, and caveats.
- `tools/run_c2_battle_trace_oracle_mesen.py`: already supports no-state runs,
  and its local fixture template includes an autostart fixture-ROM role.
- `tools/validate_c2_battle_trace_local_fixtures.py`: allow a
  `fixture_rom_autostart` role where `save_state_path` is absent.
- `tools/build_c2_battle_trace_oracle_manifest.py`: optionally add `C2:2F38`,
  `C2:E8E0`, `C2:E9C8`, and `C052AA` as startup provenance hints.

## Safety Rules

- Generated ROMs remain ignored under `build/c2/fixture-roms/`.
- Every byte patch must be recorded in the generated fixture manifest.
- Autostart hooks are reachability tools only.
- Do not promote source comments or names from scripted-entry fixture traces
  until local ASM agreement and reviewed trace results exist.
