# C2 Battle Trace Oracle Mesen Runner

This note describes the local Mesen execution bridge for the Phase 2 C2
trace-oracle queue. It is intentionally fixture-light: ROMs, save states, raw
traces, and run summaries stay under ignored local paths.

## Role

The Mesen runner is a runtime evidence collector, not a source authority. It
executes the generated per-job Lua skeletons from
`build/c2/battle-trace-oracles/mesen-runner-assets/`, writes raw JSONL traces
under `build/c2/battle-trace-oracles/<oracle>/`, and optionally writes a
non-proof unresolved result. Reviewed proof-grade results still have to pass
`tools/validate_c2_battle_trace_oracle_result.py` and the collector before any
source-facing semantic promotion.

Generated skeletons accept `C2_ORACLE_INPUT_PATTERN` through the wrapper. The
pattern reuses the prior Mesen route syntax: `atom:frames,atom:frames`. Locally
proven atoms are `neutral`, `none`, `right`, `left`, `up`, `down`,
`down_right`, `up_right`, `up_left`, `down_left`, `a`, `start`, and `a_start`.
Current skeletons emit rich breakpoint rows using `emu.getState()`: CPU
`A/X/Y/DB/DP/P/SP/K/PC`, cycle count, a direct-page byte window, the `$A972`
selected-target pointer, and the pointed-to 96-byte battler row. For the
`selected_target_row` watch, `address` is now the resolved row pointer and
`pointerAddress` records the original `$A972` pointer cell.

Route-gap probe hints from the oracle handoff are now emitted as optional
non-required Lua breakpoints. They carry `probeSource = route_group_hint` and a
`routeGroup`, so raw summaries split them into `probe_breakpoint_hit_counts` /
`probe_observed_addresses` instead of proof-facing `breakpoint_hit_counts` /
`observed_addresses`. This keeps helper call-site discovery out of result
promotion gates while still showing whether the run approached `C2:B930` or
`C2:40A4`.

## Local Fixture Status

- `F:\Mesen2\Mesen.exe` and `F:\Mesen\Mesen.exe` are known local Mesen2
  executable paths used by testRunner work.
- `EarthBound (USA).sfc` is discoverable through `tools/rom_tools.py` in this
  checkout.
- Older local save states exist under `F:\Mesen\SaveStates`; the current
  battle fixture set is the numbered `F:\Mesen2\SaveStates` set documented
  below.
- A boot-only smoke run with `c1_c2_target_action_staging` and a 10-frame limit
  launches Mesen and writes an ignored run summary/raw trace successfully. It
  records no C2 proof hits and should not be treated as behavior evidence.
- The local save-state probe lane tested all seven currently discoverable
  `F:\Mesen\SaveStates\*.mss` files for `c1_c2_target_action_staging`.
  Mesen loaded every state and produced nonempty traces, but none hit the
  minimum C1/C2 battle-command addresses (`C1:ADB4`, `C1:CE85`, `C1:CFC6`,
  `C2:B930`). Those states are useful runner smoke fixtures, not ready battle
  proof fixtures.
- The fixture scout then tested those same seven states under neutral, confirm,
  and small movement-loop patterns against ordinary battle-entry and command
  PCs. All 21 runs completed, but none reached `C0:D19B`, `C0:D323`,
  `C0:44DA`, `C0:B731`, `C2:E8E0`, `C2:2F38`, `C2:4821`, `C2:311B`,
  `C1:ADB4`, `C1:CE85`, `C1:CFC6`, `C2:B930`, or `C2:BAC5`.
- An overwritten earlier save-state slot captured the start of the first dog
  random battle and proved the Mesen route can reach `C2:BAC5` and `C2:8125`.
  That file is no longer the live numbered fixture. Use the hashes in this note
  for the current `EarthBound (USA)_1..7.mss` set.
- The current numbered fixture set under `F:\Mesen2\SaveStates` is the best
  C2 runtime input so far:

| Save | Local State | SHA-256 | Role |
| --- | --- | --- | --- |
| `1` | `EarthBound (USA)_1.mss` | `3602e383b607f3098250e9e7c239633d2b3bb7b3f60aa459654268420f3d51c5` | Ness queued highest-level Healing on sunstroke-afflicted Paula; effect is resolving |
| `2` | `EarthBound (USA)_2.mss` | `5aec7c75f902b606bc3a24943f62702ef11cd3785df50871fb52cb22040771df` | current live slot not re-audited in this note after local save refresh |
| `3` | `EarthBound (USA)_3.mss` | `26cd24f40f17a8aa720b9421026a2ee74dfb30922400a6a747a867be883d35fe` | PSI menu, Offense highlighted |
| `4` | `EarthBound (USA)_4.mss` | `5f6958127bda0a6940d204ab1dcc25dae366d11c2ef153f2c906ad5fffd18451` | Dread Scorpion stinger is afflicting Jeff with poison |
| `5` | `EarthBound (USA)_5.mss` | `239155e944acc4e13f7b0cb045d4b28872140a84b1a419c3ebdca03ffa697a23` | Ness used Large Pizza; party HP recovery is resolving |
| `6` | `EarthBound (USA)_6.mss` | `b70d49925f8fbf84b83ed510a0eb324bfd6a8dda1046d1e83f4b216c1d609716` | Paula already has sunstroke |
| `7` | `EarthBound (USA)_7.mss` | `d38c3cf5513b30b83943bf433c61a99d2b817bb2b22d47f52ca398ffb3d162c5` | current live slot not re-audited in this note after local save refresh |
| `8` | `EarthBound (USA)_8.mss` | `bb9f66fbb11d7fe9d7bc7e8d80fa987311e224b32ae95cf1e3fcdf02448c7b0a` | Paula queued PSI Freeze against Great Crested Booka A; battle execution is already running and Freeze resolves after Paula's sunstroke tick |

- The save slots are intentionally volatile local fixtures. Checked-in matrices
  now consume the SHA-256 captured in each ignored run summary rather than
  re-hashing the live slot after later replacements.
- The historical seven-save fixture scout ran neutral plus one-through-four confirm
  patterns: 35 completed runs, 22 battle-entry candidates, and 0 full command
  candidates. The useful C1 hits are `C1:ADB4` from the PSI/menu target path
  and `C1:CE85` from the Goods path. The current probes still do not hit
  `C1:CFC6` or `C2:B930`, so `c1_c2_target_action_staging` remains split across
  partial traces rather than a single ready fixture.
- A follow-up route probe from save 1 found the missing C1 inventory-selection
  loop: `neutral:20,right:6,neutral:12,a:4,neutral:20,a:4,neutral:900` reaches
  `C1:CFC6`, `C1:CE85`, and `C2:BAC5`. This confirms the existing command-menu
  fixture can exercise the item-selection path, but `C2:B930` still has not
  appeared in the Mesen route probes. Treat `C2:B930` as the remaining
  snapshot-export fixture gap for `c1_c2_target_action_staging`.
- Extending that route with one more confirm
  (`...,neutral:900,a:4,neutral:1800`) still does not reach `C2:B930`. The
  manual probe matrix now reports linked route-group coverage: inventory
  selection and target counting are covered by existing probes, while snapshot
  export remains uncovered.
- Targeted first-pass oracle runs produced 51 valid Mesen/raw-trace summaries.
  The strongest result is `c2_8125_damage_abi_boundary`: saves 1, 2, 3, 4, 5,
  and 7 satisfy the minimum `C2:8125` hit under either a complete-turn confirm
  pattern or a neutral wait. Save 3 also reaches `C2:941D`, giving a useful PSI
  damage/status-gate sample.
- Save 5 has also been rerun through the richer canonical
  `c2_8125_damage_abi_boundary` output path. The reviewed result validates as
  non-stub `ok` / `needs_followup`: it proves `C2:8125` reachability with
  captured amount input `A = 0x0045`, damage selector `X = 0x00FF`, direct page,
  and selected target row pointer `$A21C`, but keeps downstream text/collapse
  interpretation blocked until those fields are decoded.
- Save 7 now validates as the canonical `hp_roller_collapse_boundary`
  fixture. A neutral 1800-frame run observes `C2:8125`, `C2:7550`, `C2:77CA`,
  `C1:DC66`, `C1:DC1C`, and `C2:BB18`, with row snapshots showing live HP at
  `+0x11` reaching zero before collapse handling. The reviewed result remains
  `needs_followup` because this run does not hit `C2:7680` or `C2:BC5C` and
  does not prove HP-roller visual timing across the whole collapse family.
- Save 8 adds a queued offensive-PSI runtime fixture. A neutral 1800-frame
  Paula Freeze run satisfies `c2_8125_damage_abi_boundary` and
  `hp_roller_collapse_boundary`: it observes `C2:941D`, four `C2:8125` damage
  ABI entries, four `C2:7EAF` amount/selector neighbors, `C2:7550`, `C2:77CA`,
  `C2:BB18`, and the C1 text/display joins `C1:DC66`/`C1:DC1C`. It is useful
  evidence that offensive PSI damage shares the direct C2 damage/text family,
  not proof of the `C2:40A4` second-pointer wrapper.
- The replaced-slot fixture pass adds three targeted runtime states. Save 1
  validates another `c2_8125_damage_abi_boundary` minimum hit for highest-level
  Healing on Paula and reaches the HP/text display family. Save 4 reaches the
  `C2:724A` affliction writer once from Dread Scorpion poison, dispatching
  through `C2:8B2C`, but does not satisfy the paired `C2:9917` status-gate
  minimum. Save 5 validates another `c2_8125_damage_abi_boundary` minimum hit
  for Large Pizza party HP recovery and reaches `C2:B27D` as a new
  payload-adjacent direct-dispatch target.
- `c2_40a4_current_action_payload` does not yet hit its minimum `C2:40A4`, but
  saves 1, 2, 3, 4, 5, 7, and 8 repeatedly hit nearby `C2:3D05`. The new
  Healing, poison, and Large Pizza fixtures also stay in the same direct
  dispatch family rather than the `C2:40A4` wrapper. Treat those as route hints
  only.
- The generated runner assets now install route-gap probe breakpoints for the
  two open lanes. For `c1_c2_target_action_staging`, the extra non-required
  breakpoints are `C1:B3DB`, `C1:B462`, `C1:B505`, `C1:B859`, `C1:B9A9`, and
  `C1:BA60`. For `c2_40a4_current_action_payload`, they are `C2:77CA`,
  `C2:90C6`, `C2:A89D`, and `C0:9279`. These are discovery aids only; the
  minimum gates remain `C2:B930` and `C2:40A4`.
- The enhanced route-gap probe sweep added four `c2_40a4_current_action_payload`
  route-hint fixtures. Saves 5, 7, 11, and the PSI-menu save reached `C0:9279`;
  save 7 also reached `C2:77CA`. None reached `C2:40A4`, so the useful next
  fixture is still an action state immediately before a real second-pointer
  payload is applied rather than a post-result or text-context neighbor.
- A follow-up dispatch-target sweep now records the actual `$00BC` trampoline
  target and stack return for each `C0:9279` hit. The C2-side route hints return
  through `C2:5D3D` and dispatch to payload-adjacent targets including
  `C2:859F`, `C2:8651`, `C2:8740`, and `C2:9033`; the PSI-menu neighbor dispatch
  instead targets `C1:C8BC` and returns through `C1:1AE2`. These are still
  approach-path facts, not `C2:40A4` proof.
- The `c2_40a4_current_action_payload` runner now watches the three known
  static `C2:40A4` callsites: `C2:79D1`, `C2:915C`, and `C2:AF0D`. It also
  captures `$A970/$A972`, `$A96C/$A96E`, `$00BC/$00BE`, and the
  `$1B9E/$AEC2/$AECC/$AECE` busy gate around payload-adjacent dispatches.
  Physical damage, PSI damage, Healing, Dread Scorpion poison, and Large Pizza
  recovery fixtures hit `C2:4703`, `C2:3E32`, `C2:416F`, downstream `C2:3D05`,
  and `C0:9279` in different combinations, but not the `C2:40A4` wrapper or
  any of the three pre-call sites. The dispatch-lane summary classifies those
  `C0:9279` hits as `c2_battle_start_candidate_direct_dispatch` via return
  `C2:5D3D`, so the current fixture set is useful for payload-target
  identities, but not for proving the second-pointer wrapper contract.
- `tools/build_c2_fixture_roms.py` now builds ignored table-patched fixture
  ROMs under `build/c2/fixture-roms/`. These are not source edits and are not
  behavior proof by themselves; they are deterministic setup aids for local
  Mesen runs. The first scenarios patch only `ENEMY_CONFIGURATION_TABLE` rows:
  both Runaway Dog rows can force the `C2:90C6 -> C2:40A4` neutralize/all lane
  as a normal action, both Runaway Dog rows can gain a 1-HP KO final-action
  version of the same lane, and Dread Skelpion can repeatedly choose its known
  poison action row `72` for faster `C2:724A` reruns. The Bash-row scenario is
  deliberately more artificial: it patches `BATTLE_ACTION_TABLE` row `4` so an
  existing command-menu save can confirm Bash and still dispatch through
  `C2:90C6 -> C2:40A4`.
- The enhanced `c1_c2_target_action_staging` route sweep still did not reach
  `C2:B930` or its six C1 pre-export probe sites. Save 11 repeatedly hits
  `C2:BAC5`, which makes it another target-count fixture, not a snapshot-export
  fixture.
- A stack-context rerun of the save 1, save 3, save 4, and save 11 routes still
  reaches only the C1 menu/target-count neighbors plus `C2:BAC5`, not the
  `C2:B930` export. This confirms the current fixture set is outside the narrow
  post-choice/pre-text export window. The runner now captures C1 direct-page
  fields `$00..$2C`, the `$99CE` source slot row selected by `A`, destination
  `X/Y` rows, and a `post_call_snapshot` after `C2:B930` returns, so the next
  correctly timed fixture should produce before/after export evidence without
  another tooling change.
- The current set now reaches the first affliction-writer minimum address:
  save 4 hits `C2:724A` for Dread Scorpion poison. The full
  `c2_724a_affliction_writer_matrix` result remains partial because the paired
  `C2:9917` path has not been observed.
- The runner now supports named post-savestate WRAM profiles with
  `--wram-patch-profile`, plus ad hoc `--wram-patch` records for one-off local
  probes. The resource lane uses these only as fixture evidence: a Magnet run
  seeded selected-target PP and active-row PP max, observing target PP
  `32 -> 27` and active row PP `0 -> 5`; a PP-reduction run seeded
  selected-target PP and observed target PP `32 -> 30` with no active-row
  recovery. Natural PP-bearing target traces are still required for proof-grade
  promotion.
- `notes/c2-resource-amount-natural-candidates.md` now lists vanilla enemy/action
  users for the natural resource probe. Current top lanes are Gigantic Ant or
  Starman for row `54`/`C2:9F5E` PSI Magnet transfer, and Guardian General or
  accessible Mad Duck/Armored Frog encounters for row `95`/`C2:8E42` PP
  reduction.
- `notes/c2-save-state-battler-scout.md` inventories the current local `.mss`
  set through Mesen and records selected target/active row pointers plus
  PP-bearing `$9FAC` battler rows. It is a probe picker only; it does not
  promote resource semantics without a matching natural action trace.

The first useful fixture to create is an ordinary battle state just before
choosing a command. That should target `c1_c2_target_action_staging`, because it
only needs the C1 target/action staging path and C2 candidate export path.

The least invasive proof route is a normal overworld enemy encounter, then a
local Mesen save at the first battle command prompt. The ordinary-entry
provenance chain to confirm is:

1. `C0:D19B` prepares the encounter slot and battle id.
2. `C0:D323` builds `$9F8A/$9F8C` enemy entries.
3. `C0:44DA` sets `$4DC2 = FFFF` after the encounter countdown.
4. `C0:B731` enters the overworld battle initializer with `$4DC2 != 0`.
5. `C2:4821` reaches the shared battle runtime while skipping the `$4DC2 == 0`
   debug/default seed block at `C2:4830`.

## Commands

Initialize and validate the ignored local fixture config:

```powershell
python tools\run_c2_battle_trace_oracle_mesen.py --init-fixtures-template
python tools\validate_c2_battle_trace_local_fixtures.py --allow-template-placeholders
```

The validator checks local paths, declared oracle ids, named WRAM patch profiles,
and `initial` versus `first-breakpoint` WRAM patch timing.

After creating a local ordinary-battle save state, edit
`build/c2/battle-trace-oracles/local-fixtures.json`, replace the placeholder
`save_state_path`, and validate without `--allow-template-placeholders`.

Regenerate runner assets:

```powershell
python tools\build_c2_battle_trace_oracle_runner_assets.py
python tools\validate_c2_battle_trace_oracle_runner_assets.py
```

Dry-run a job against the local Mesen/ROM discovery path:

```powershell
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id c1_c2_target_action_staging --dry-run
```

Run a local battle fixture:

```powershell
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id c1_c2_target_action_staging --fixture-id ordinary_battle_pre_command --frame-limit 3600 --summarize-trace
```

Run a controlled WRAM-patched PP reducer probe. These runs are navigation
evidence only; they must stay below proof-grade until repeated with a natural
PP-bearing target state:

```powershell
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id resource_amount_pair_magnet_vs_pp_loss --rom build\c2\fixture-roms\bash-row-psi-magnet-force-reducer\EarthBound-USA-bash-row-psi-magnet-force-reducer.sfc --state "F:\Mesen2\SaveStates\EarthBound (USA)_2.mss" --input-pattern neutral:20,a:4,neutral:1000 --frame-limit 1200 --summarize-trace --output-dir build\c2\battle-trace-oracles\manual-probes\resource-wram-patched\psi-magnet-target-pp32 --wram-patch-profile resource-magnet-transfer-pp32
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id resource_amount_pair_magnet_vs_pp_loss --rom build\c2\fixture-roms\bash-row-pp-reduction\EarthBound-USA-bash-row-pp-reduction.sfc --state "F:\Mesen2\SaveStates\EarthBound (USA)_2.mss" --input-pattern neutral:20,a:4,neutral:1000 --frame-limit 1200 --summarize-trace --output-dir build\c2\battle-trace-oracles\manual-probes\resource-wram-patched\pp-reduction-target-pp32 --wram-patch-profile resource-target-pp32
```

Run the no-save scripted-entry fixture with the named delayed WRAM seed profile:

```powershell
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id c2_40a4_current_action_payload --rom build\c2\fixture-roms\scripted-entry-group0-force-enemy-action\EarthBound-USA-scripted-entry-group0-force-enemy-action.sfc --input-pattern neutral:240,a:4,neutral:36,a:4 --frame-limit 24000 --summarize-trace --wram-patch-timing first-breakpoint --wram-patch-profile scripted-entry-party-window-reset
```

Resource scripted-entry probes can combine early startup seeding with an
entry-specific PP seed. `--wram-patch-profile-on-hit LABEL=profile` applies the
named profile once, immediately before that breakpoint is captured:

```powershell
python tools\build_c2_fixture_roms.py --scenario scripted-entry-gigantic-ant-natural-magnet --scenario scripted-entry-guardian-general-natural-pp-reduction --scenario scripted-entry-gigantic-ant-force-magnet-action --scenario scripted-entry-guardian-general-force-pp-reduction
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id resource_amount_pair_magnet_vs_pp_loss --rom build\c2\fixture-roms\scripted-entry-gigantic-ant-natural-magnet\EarthBound-USA-scripted-entry-gigantic-ant-natural-magnet.sfc --input-pattern neutral:240,a:4,neutral:36,a:4,neutral:36,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4 --frame-limit 24000 --summarize-trace --output-dir build\c2\battle-trace-oracles\manual-probes\resource-natural-scripted-entry\gigantic-ant-natural-magnet-onhit-target32-active0-confirm-cycle --wram-patch-timing first-breakpoint --wram-patch-profile scripted-entry-party-window-reset --wram-patch-profile-on-hit C2:9F5E=resource-selected-row-9fac-pp32 --wram-patch-profile-on-hit C2:9F5E=resource-active-row-a21c-pp0-max81
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id resource_amount_pair_magnet_vs_pp_loss --rom build\c2\fixture-roms\scripted-entry-guardian-general-natural-pp-reduction\EarthBound-USA-scripted-entry-guardian-general-natural-pp-reduction.sfc --input-pattern neutral:240,a:4,neutral:36,a:4,neutral:36,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4 --frame-limit 24000 --summarize-trace --output-dir build\c2\battle-trace-oracles\manual-probes\resource-natural-scripted-entry\guardian-general-natural-pp-reduction-onhit-target32-confirm-cycle --wram-patch-timing first-breakpoint --wram-patch-profile scripted-entry-party-window-reset --wram-patch-profile-on-hit C2:8E42=resource-selected-row-9fac-pp32
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id resource_amount_pair_magnet_vs_pp_loss --rom build\c2\fixture-roms\scripted-entry-gigantic-ant-force-magnet-action\EarthBound-USA-scripted-entry-gigantic-ant-force-magnet-action.sfc --input-pattern neutral:240,a:4,neutral:36,a:4,neutral:36,a:4,neutral:360,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:1200 --frame-limit 2200 --summarize-trace --output-dir build\c2\battle-trace-oracles\manual-probes\resource-natural-scripted-entry\gigantic-ant-force-magnet-onhit-target32-active0-single-confirm --wram-patch-timing first-breakpoint --wram-patch-profile scripted-entry-party-window-reset --wram-patch-profile-on-hit C2:9F5E=resource-selected-row-9fac-pp32 --wram-patch-profile-on-hit C2:9F5E=resource-active-row-a21c-pp0-max81
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id resource_amount_pair_magnet_vs_pp_loss --rom build\c2\fixture-roms\scripted-entry-guardian-general-force-pp-reduction\EarthBound-USA-scripted-entry-guardian-general-force-pp-reduction.sfc --input-pattern neutral:240,a:4,neutral:36,a:4,neutral:36,a:4,neutral:12000 --frame-limit 16000 --summarize-trace --output-dir build\c2\battle-trace-oracles\manual-probes\resource-natural-scripted-entry\guardian-general-force-pp-reduction-onhit-9fac-pp32 --wram-patch-timing first-breakpoint --wram-patch-profile scripted-entry-party-window-reset --wram-patch-profile-on-hit C2:8E42=resource-selected-row-9fac-pp32
```

Startup-only variants omit the resource-specific on-hit PP seed. They are a
cleaner diagnostic tier: the forced-action ROMs reach `C2:9F5E` and `C2:8E42`,
but selected target PP remains zero and `C2:721D` is not reached:

```powershell
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id resource_amount_pair_magnet_vs_pp_loss --rom build\c2\fixture-roms\scripted-entry-gigantic-ant-force-magnet-action\EarthBound-USA-scripted-entry-gigantic-ant-force-magnet-action.sfc --input-pattern neutral:240,a:4,neutral:36,a:4,neutral:36,a:4,neutral:360,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:1200 --frame-limit 2200 --summarize-trace --output-dir build\c2\battle-trace-oracles\manual-probes\resource-startup-only-scripted-entry\gigantic-ant-force-magnet-startup-only --wram-patch-timing first-breakpoint --wram-patch-profile scripted-entry-party-window-reset
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id resource_amount_pair_magnet_vs_pp_loss --rom build\c2\fixture-roms\scripted-entry-guardian-general-force-pp-reduction\EarthBound-USA-scripted-entry-guardian-general-force-pp-reduction.sfc --input-pattern neutral:240,a:4,neutral:36,a:4,neutral:36,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:120,a:4,neutral:1200 --frame-limit 2200 --summarize-trace --output-dir build\c2\battle-trace-oracles\manual-probes\resource-startup-only-scripted-entry\guardian-general-force-pp-reduction-startup-only --wram-patch-timing first-breakpoint --wram-patch-profile scripted-entry-party-window-reset
```

ROM-only variants omit even the startup WRAM profile. They reach battle
startup/front-end breakpoints, but do not enter enemy action resolution yet;
the next cleaner fixture needs ROM-side selected-target PP setup, not another
input-pattern retry.

These scripted-entry resource probes are still fixture evidence: the natural
enemy/action rows are useful navigation, but generated ROM entry and any WRAM
startup or PP seeding keep those specific runs in the controlled-evidence tier.
Natural vanilla PSI Magnet and Mad Duck PP-loss save-state captures are tracked
separately in `notes/psi-magnet-drain-amount.md`.

Validate the ignored run summary:

```powershell
python tools\validate_c2_battle_trace_oracle_mesen_run_summary.py build\c2\battle-trace-oracles\c1_c2_target_action_staging\mesen-run-summary.json
python tools\summarize_c2_battle_trace_oracle_raw_trace.py --oracle-id c1_c2_target_action_staging
python tools\validate_c2_battle_trace_oracle_raw_trace_summary.py build\c2\battle-trace-oracles\c1_c2_target_action_staging\raw-trace-summary.json
```

Probe existing local Mesen save states without overwriting packet output paths:

```powershell
python tools\probe_c2_battle_trace_save_states.py --mesen F:\Mesen2\Mesen.exe
python tools\validate_c2_battle_trace_save_state_probes.py
python tools\probe_c2_battle_fixture_scout.py --mesen F:\Mesen2\Mesen.exe
python tools\validate_c2_battle_fixture_scout.py
```

Probe output stays under
`build/c2/battle-trace-oracles/save-state-probes/` and
`build/c2/battle-trace-oracles/fixture-scout/`. A probe that satisfies minimum
hits is only a fixture candidate; it still needs manual trace review and the
normal result builder/validator before it can affect source comments.

Build the sanitized tracked matrix from the ignored manual probe summaries:

```powershell
python tools\build_c2_battle_trace_manual_probe_matrix.py
python tools\validate_c2_battle_trace_manual_probe_matrix.py
```

The matrix is written to
`manifests/c2-battle-trace-manual-probe-matrix.json` and
`notes/c2-battle-trace-manual-probe-matrix.md`. It records useful fixture
hits, redacts local save-state paths, and does not promote source behavior.

Reproduce the save-1 inventory-selection route probe without overwriting the
canonical oracle output:

```powershell
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id c1_c2_target_action_staging --mesen F:\Mesen2\Mesen.exe --state "F:\Mesen2\SaveStates\EarthBound (USA)_1.mss" --input-pattern neutral:20,right:6,neutral:12,a:4,neutral:20,a:4,neutral:900 --frame-limit 1400 --timeout 180 --summarize-trace --output-dir build\c2\battle-trace-oracles\route-probes\c1-c2-target-action-staging\save1-right-confirm
```

Continue the same route one more confirm:

```powershell
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id c1_c2_target_action_staging --mesen F:\Mesen2\Mesen.exe --state "F:\Mesen2\SaveStates\EarthBound (USA)_1.mss" --input-pattern neutral:20,right:6,neutral:12,a:4,neutral:20,a:4,neutral:900,a:4,neutral:1800 --frame-limit 3600 --timeout 240 --summarize-trace --output-dir build\c2\battle-trace-oracles\route-probes\c1-c2-target-action-staging\save1-right-confirm-continue
```

For `c2_40a4_current_action_payload`, current fixtures only reach the adjacent
`C2:3D05` target text-context builder. Use a targeted local save immediately
before confirming a curative, recovery, item-status, or random
damage/status-item second-pointer payload:

```powershell
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id c2_40a4_current_action_payload --mesen F:\Mesen2\Mesen.exe --state "<local .mss>" --input-pattern neutral:20,a:4,neutral:20,a:4,neutral:1800 --frame-limit 2600 --timeout 180 --summarize-trace --output-dir build\c2\battle-trace-oracles\manual-probes\c2-40a4-targeted\<fixture-id>
python tools\build_c2_battle_trace_manual_probe_matrix.py --probe-root build\c2\battle-trace-oracles\manual-probes\battle-fixtures-1-7 --probe-root build\c2\battle-trace-oracles\manual-probes\c2-40a4-targeted
```

Build deterministic local fixture ROMs when save-state hunting becomes the
limiting factor:

```powershell
python tools\build_c2_fixture_roms.py
```

The generated ROMs and manifests are ignored build artifacts:

- `build/c2/fixture-roms/runaway-dog-neutralize-c240a4/`: early Runaway Dog
  encounters force action row `248`, which ebsrc shows calling `C2:40A4` from
  `C2:90C6`.
- `build/c2/fixture-roms/runaway-dog-final-neutralize-c240a4/`: Runaway Dog
  rows have 1 HP plus final action row `248`, aiming at the KO final-action
  caller family.
- `build/c2/fixture-roms/dread-skelpion-poison-fast/`: Dread Skelpion repeats
  action row `72`, the known poison status action used for `C2:724A` reruns.
- `build/c2/fixture-roms/bash-row-neutralize-c240a4/`: battle action row `4`
  keeps its Bash presentation but points its behavior pointer at `C2:90C6`, so
  a command-menu save can test the `C2:40A4` wrapper without relying on enemy
  row setup.

Load these ROMs only as local probe fixtures. If a generated ROM produces a
useful trace, review the raw runner output and promote the result through the
normal oracle-result path rather than promoting directly from the patch recipe.

After manual review, assemble and validate a result:

```powershell
python tools\build_c2_battle_trace_oracle_mesen_capture_fields.py --oracle-id c2_8125_damage_abi_boundary --classification refined_contract
python tools\build_c2_battle_trace_oracle_result_from_evidence.py --oracle-id c2_8125_damage_abi_boundary --status ok --classification refined_contract --classification-rationale "<reviewed trace rationale>" --observed-address C2:8125 --observed-address C2:7EAF --observed-address C1:DC66 --observed-address C1:AD0A --observed-address C1:7EED --observed-address C1:AD26 --observed-address C1:0DF6 --captured-fields-json build\c2\battle-trace-oracles\c2_8125_damage_abi_boundary\captured-fields.json
python tools\validate_c2_battle_trace_oracle_result.py build\c2\battle-trace-oracles\c2_8125_damage_abi_boundary\result.json
python tools\collect_c2_battle_trace_oracle_results.py
python tools\validate_c2_battle_trace_oracle_results_summary.py
```

The same capture assembler supports `hp_roller_collapse_boundary` after a
canonical run from save 7:

```powershell
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id hp_roller_collapse_boundary --mesen F:\Mesen2\Mesen.exe --state "F:\Mesen2\SaveStates\EarthBound (USA)_7.mss" --input-pattern neutral:1800 --frame-limit 1800 --timeout 240 --summarize-trace
python tools\build_c2_battle_trace_oracle_mesen_capture_fields.py --oracle-id hp_roller_collapse_boundary --classification refined_contract
python tools\build_c2_battle_trace_oracle_result_from_evidence.py --oracle-id hp_roller_collapse_boundary --status ok --classification refined_contract --classification-rationale "<reviewed collapse-boundary rationale>" --observed-address C2:8125 --observed-address C2:7550 --observed-address C2:77CA --observed-address C2:BB18 --observed-address C1:DC66 --observed-address C1:DC1C --captured-fields-json build\c2\battle-trace-oracles\hp_roller_collapse_boundary\captured-fields.json
python tools\validate_c2_battle_trace_oracle_result.py build\c2\battle-trace-oracles\hp_roller_collapse_boundary\result.json
```

For `c2_8125_damage_abi_boundary`, the capture assembler decodes the selected
`$A972` battler row into review fields such as the active/consciousness byte,
HP live/target/max words, primary affliction byte, timed substate, shield
countdown, offense/defense, and resistance bytes. It also decodes C1 battle
text joins: `C1:DC1C` direct `$0E/$10` text pointers, `C1:DC66` primary
`$0E/$10` text plus `$12/$14` payload, and the `$9D12/$9D14 -> C1:7EED ->
C1:AD26 -> C1:0DF6` amount-consumer path when the runner captures those
breakpoints. The reviewed result is now `refined_contract` for the damage ABI,
selected-row HP mutation, and amount-text join; caller provenance breadth stays
outside that promotion.

For `hp_roller_collapse_boundary`, the assembler captures the damage-entry
row, collapse-start row, optional collapse-text/cleanup hits, C1 text joins,
and ordered breakpoint samples. In the current save-7 trace it records
`C2:7680` and `C2:BC5C` as not observed rather than inferring those paths. The
reviewed result is now `refined_contract` for HP-to-zero collapse entry,
`C2:7550 -> C2:77CA` order, and hard/collapsed row-state installation.

Controlled helper-entry probes now cover the two optional HP/collapse-tail
helpers separately. These are fixture mechanics, not natural damage proof:

```powershell
python tools\build_c2_fixture_roms.py --scenario direct-c27550-descriptor-death-text --scenario direct-c2bc5c-cleanup
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id hp_roller_collapse_boundary --rom build\c2\fixture-roms\direct-c27550-descriptor-death-text\EarthBound-USA-direct-c27550-descriptor-death-text.sfc --input-pattern neutral:600 --frame-limit 1200 --timeout 240 --summarize-trace --output-dir build\c2\battle-trace-oracles\manual-probes\hp-roller-collapse-tail\direct-c27550-descriptor-death-text --wram-patch-timing first-breakpoint --wram-patch-profile collapse-descriptor-row-9fac-runaway-dog
python tools\run_c2_battle_trace_oracle_mesen.py --oracle-id hp_roller_collapse_boundary --rom build\c2\fixture-roms\direct-c2bc5c-cleanup\EarthBound-USA-direct-c2bc5c-cleanup.sfc --input-pattern neutral:120 --frame-limit 300 --timeout 240 --summarize-trace --output-dir build\c2\battle-trace-oracles\manual-probes\hp-roller-collapse-tail\direct-c2bc5c-cleanup-postcall --wram-patch-timing first-breakpoint --wram-patch-profile bc5c-source-entry0-live-slot0-dirty
```

The descriptor fixture observes `C0:B9B4 -> C2:7550 -> C2:7680 -> C1:DC1C`
with `$9FAC` seeded as a minimal Runaway Dog selected row. The cleanup fixture
observes `C2:BC5C` and a `return_from:C2:BC5C` post-call snapshot where live
slot bytes `+0x10/+0x11/+0x12/+0x14` change from nonzero seed values to zero.

## Promotion Rule

Do not promote source names or comments from a Mesen run summary alone. The raw
trace has to be reviewed into a non-stub result with all packet capture fields,
then collected as trace-observed or proof-grade evidence.

## Hook Fallbacks

Do not use a ROM hook for the first fixture unless a manual local battle save
state proves impractical. A cold jump into `C2:4821` / `BATTLE_ROUTINE` is too
late in the setup path for ordinary-battle proof. If a hook lane becomes
necessary later, `C2:2F38` / `INIT_BATTLE_SCRIPTED` is the safer candidate
because it reads the battle-entry pointer table, stages `$9F8A/$9F8C`, sets
`$4DC2`, runs the swirl/setup path, and reaches the shared battle init route.
Do not use EF debug `SHOW BATTLE` as the ordinary fixture, because that path
enters `C2:4821` directly and can fall through the `$4DC2 == 0` debug/default
seed block instead of proving the overworld encounter initializer.

Useful anchors:

- `C0:D19B` / encounter prep: stages the encounter slot and battle id.
- `C0:D323` / enemy-list build: fills `$9F8A/$9F8C`.
- `C0:44DA` / encounter countdown tail: sets `$4DC2 = FFFF`.
- `C0:B731` / `INIT_BATTLE_OVERWORLD`: vanilla overworld battle entry when
  `$4DC2` is set.
- `C2:2F38` / `INIT_BATTLE_SCRIPTED`: scripted battle entry using the
  `D0:C60D` battle-entry pointer table.
- `C2:4821` / `BATTLE_ROUTINE`: battle runtime entry used by debug SHOW BATTLE,
  not a complete ordinary battle initializer.
- `C2:4830`: debug/default seed block to prove skipped for ordinary-entry
  provenance.
