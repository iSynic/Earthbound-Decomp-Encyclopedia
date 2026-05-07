# Audio Gate 2 Scheduler Frontier

Status: isolated-harness SMP-main scheduling is implemented; fuller DSP/system
scheduling still needs a full-system ares harness.

## Current Result

The fused `CHANGE_MUSIC -> C0:AB06 -> live driver -> C0:ABBD` path can now
advance the post-command boundary through `ares::SuperFamicom::smp.main()`
instead of calling raw `smp.instruction()` directly. The harness initializes a
minimal ares node/debugger tree before entering `SMP::main`, records the
post-command scheduler mode, and writes per-record scheduler counters in the
fusion frontier and timing metrics so Gate 2 evidence is explicit instead of
implicit.

Attempting to extend this all the way to a cooperative `smp.main() + dsp.main()`
step is still not safe inside the isolated C0:AB06 harness. The DSP path expects
full thread/audio-node state that this helper deliberately does not create.

## Implemented Guardrail

- `tools/ares_c0ab06_loader_handshake/main.cpp` accepts
  `--post-command-scheduler-mode`.
- `smp_main` is the safe default and is recorded in output JSON.
- `smp_instruction` remains available as a comparison mode.
- `smp_dsp_cooperative` fails fast with an explanatory error instead of
  crashing the process.
- `tools/collect_audio_c0ab06_change_music_fusion_frontier.py` propagates the
  scheduler mode into frontier metadata.
- `tools/collect_audio_fusion_timing_metrics.py` and the validators require the
  scheduler mode/counter fields so future scheduler evidence cannot be omitted.

## Next Implementation Step

Gate 2's next step should move into a full-system ares helper that powers/loads
enough of the SFC system for `DSP::main` and full scheduler/thread state to be
valid. Use the current fusion frontier as the positive oracle:

1. Boot through the real SMP IPL and C0:AB06 loader path as today.
2. Deliver the final C0:ABBD APUIO0 command through the CPU/APU bridge.
3. Advance with full ares scheduler/thread state, not direct isolated calls.
4. Capture command-read, zero-ack, key-on, SPC registers, DSP registers, timer
   state, and APUIO mailbox state at a stable boundary.
5. Compare against the current `smp_main` fusion corpus and the
   no-command negative control.

The first regression target should remain track `046` (`ONETT`), then the
20-track representative corpus, then the all-track corpus.
