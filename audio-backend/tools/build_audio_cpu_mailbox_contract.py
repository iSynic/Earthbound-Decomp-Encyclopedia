#!/usr/bin/env python3
"""Build the CPU/APU audio mailbox contract for faithful track-start work."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
EXTERNAL_ARES_ROOT = Path(os.environ.get("EARTHBOUND_ARES_ROOT", ROOT.parent / "ares-earthbound-audio-backend"))
DEFAULT_FRONTIER = ROOT / "build" / "audio" / "command-on-first-read-jobs" / "mailbox-frontier.json"
DEFAULT_SMP_SMOKE = ROOT / "build" / "audio" / "ares-smp-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_SMP_RENDER = ROOT / "build" / "audio" / "ares-smp-mailbox-render-jobs" / "libgme-render-metrics.json"
DEFAULT_SMP_RENDER_VS_LAST_KEYON = ROOT / "build" / "audio" / "ares-smp-mailbox-render-jobs" / "smp-mailbox-vs-custom-last-keyon-render-comparison.json"
DEFAULT_SMP_RENDER_VS_BASELINE = ROOT / "build" / "audio" / "ares-smp-mailbox-render-jobs" / "smp-mailbox-vs-baseline-render-comparison.json"
DEFAULT_CPU_WRITEAPU_SMOKE = ROOT / "build" / "audio" / "ares-cpu-writeapu-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_CPU_WRITEAPU_RENDER = ROOT / "build" / "audio" / "ares-cpu-writeapu-mailbox-render-jobs" / "libgme-render-metrics.json"
DEFAULT_CPU_WRITEAPU_RENDER_VS_SMP = ROOT / "build" / "audio" / "ares-cpu-writeapu-mailbox-render-jobs" / "cpu-writeapu-vs-smp-portwrite-render-comparison.json"
DEFAULT_CPU_WRITEAPU_RENDER_VS_BASELINE = ROOT / "build" / "audio" / "ares-cpu-writeapu-mailbox-render-jobs" / "cpu-writeapu-vs-baseline-render-comparison.json"
DEFAULT_WDC65816_SMOKE = ROOT / "build" / "audio" / "ares-wdc65816-sta2140-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_WDC65816_RENDER = ROOT / "build" / "audio" / "ares-wdc65816-sta2140-mailbox-render-jobs" / "libgme-render-metrics.json"
DEFAULT_WDC65816_RENDER_VS_CPU_WRITEAPU = ROOT / "build" / "audio" / "ares-wdc65816-sta2140-mailbox-render-jobs" / "wdc65816-vs-cpu-writeapu-render-comparison.json"
DEFAULT_WDC65816_RENDER_VS_BASELINE = ROOT / "build" / "audio" / "ares-wdc65816-sta2140-mailbox-render-jobs" / "wdc65816-vs-baseline-render-comparison.json"
DEFAULT_FULL_C0ABBD_SMOKE = ROOT / "build" / "audio" / "ares-wdc65816-c0abbd-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_FULL_C0ABBD_RENDER = ROOT / "build" / "audio" / "ares-wdc65816-c0abbd-mailbox-render-jobs" / "libgme-render-metrics.json"
DEFAULT_FULL_C0ABBD_RENDER_VS_STA2140 = ROOT / "build" / "audio" / "ares-wdc65816-c0abbd-mailbox-render-jobs" / "full-c0abbd-vs-sta2140-render-comparison.json"
DEFAULT_FULL_C0ABBD_RENDER_VS_BASELINE = ROOT / "build" / "audio" / "ares-wdc65816-c0abbd-mailbox-render-jobs" / "full-c0abbd-vs-baseline-render-comparison.json"
DEFAULT_CPU_ROUTINE_FIXTURES = ROOT / "build" / "audio" / "cpu-routine-fixtures" / "audio-cpu-routine-fixtures.json"
DEFAULT_ROM_C0ABBD_SMOKE = ROOT / "build" / "audio" / "ares-wdc65816-rom-c0abbd-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_ROM_C0ABBD_RENDER = ROOT / "build" / "audio" / "ares-wdc65816-rom-c0abbd-mailbox-render-jobs" / "libgme-render-metrics.json"
DEFAULT_ROM_C0ABBD_RENDER_VS_MODELED = ROOT / "build" / "audio" / "ares-wdc65816-rom-c0abbd-mailbox-render-jobs" / "rom-c0abbd-vs-modeled-c0abbd-render-comparison.json"
DEFAULT_ROM_C0ABBD_RENDER_VS_BASELINE = ROOT / "build" / "audio" / "ares-wdc65816-rom-c0abbd-mailbox-render-jobs" / "rom-c0abbd-vs-baseline-render-comparison.json"
DEFAULT_ROM_C0ABBD_JSL_SMOKE = ROOT / "build" / "audio" / "ares-wdc65816-rom-c0abbd-jsl-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_ROM_C0ABBD_JSL_RENDER = ROOT / "build" / "audio" / "ares-wdc65816-rom-c0abbd-jsl-mailbox-render-jobs" / "libgme-render-metrics.json"
DEFAULT_ROM_C0ABBD_JSL_RENDER_VS_DIRECT = ROOT / "build" / "audio" / "ares-wdc65816-rom-c0abbd-jsl-mailbox-render-jobs" / "rom-c0abbd-jsl-vs-direct-render-comparison.json"
DEFAULT_ROM_C0ABBD_JSL_RENDER_VS_BASELINE = ROOT / "build" / "audio" / "ares-wdc65816-rom-c0abbd-jsl-mailbox-render-jobs" / "rom-c0abbd-jsl-vs-baseline-render-comparison.json"
DEFAULT_CHANGE_MUSIC_TAIL_SMOKE = ROOT / "build" / "audio" / "ares-wdc65816-change-music-tail-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_CHANGE_MUSIC_TAIL_RENDER = ROOT / "build" / "audio" / "ares-wdc65816-change-music-tail-mailbox-render-jobs" / "libgme-render-metrics.json"
DEFAULT_CHANGE_MUSIC_TAIL_RENDER_VS_C0ABBD_JSL = ROOT / "build" / "audio" / "ares-wdc65816-change-music-tail-mailbox-render-jobs" / "change-music-tail-vs-c0abbd-jsl-render-comparison.json"
DEFAULT_CHANGE_MUSIC_TAIL_RENDER_VS_BASELINE = ROOT / "build" / "audio" / "ares-wdc65816-change-music-tail-mailbox-render-jobs" / "change-music-tail-vs-baseline-render-comparison.json"
DEFAULT_FULL_CHANGE_MUSIC_SMOKE = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_FULL_CHANGE_MUSIC_RENDER = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-mailbox-render-jobs" / "libgme-render-metrics.json"
DEFAULT_FULL_CHANGE_MUSIC_RENDER_VS_TAIL = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-mailbox-render-jobs" / "full-change-music-vs-tail-render-comparison.json"
DEFAULT_FULL_CHANGE_MUSIC_RENDER_VS_BASELINE = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-mailbox-render-jobs" / "full-change-music-vs-baseline-render-comparison.json"
DEFAULT_FULL_CHANGE_MUSIC_LOAD_STUB_SMOKE = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_FULL_CHANGE_MUSIC_LOAD_STUB_METRICS = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs" / "change-music-load-stub-metrics.json"
DEFAULT_FULL_CHANGE_MUSIC_LOAD_STUB_RENDER = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-stub-mailbox-render-jobs" / "libgme-render-metrics.json"
DEFAULT_FULL_CHANGE_MUSIC_LOAD_STUB_RENDER_VS_PRESATISFIED = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-stub-mailbox-render-jobs" / "full-change-music-load-stub-vs-presatisfied-render-comparison.json"
DEFAULT_FULL_CHANGE_MUSIC_LOAD_STUB_RENDER_VS_BASELINE = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-stub-mailbox-render-jobs" / "full-change-music-load-stub-vs-baseline-render-comparison.json"
DEFAULT_FULL_CHANGE_MUSIC_LOAD_APPLY_SMOKE = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-apply-mailbox-smoke-jobs" / "smp-mailbox-smoke-summary.json"
DEFAULT_FULL_CHANGE_MUSIC_LOAD_APPLY_METRICS = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-apply-mailbox-smoke-jobs" / "change-music-load-apply-metrics.json"
DEFAULT_FULL_CHANGE_MUSIC_LOAD_APPLY_RENDER = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-apply-mailbox-render-jobs" / "libgme-render-metrics.json"
DEFAULT_FULL_CHANGE_MUSIC_LOAD_APPLY_RENDER_VS_STUB = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-apply-mailbox-render-jobs" / "full-change-music-load-apply-vs-load-stub-render-comparison.json"
DEFAULT_FULL_CHANGE_MUSIC_LOAD_APPLY_RENDER_VS_BASELINE = ROOT / "build" / "audio" / "ares-wdc65816-full-change-music-load-apply-mailbox-render-jobs" / "full-change-music-load-apply-vs-baseline-render-comparison.json"
DEFAULT_JSON = ROOT / "manifests" / "audio-cpu-mailbox-contract.json"
DEFAULT_MARKDOWN = ROOT / "notes" / "audio-cpu-mailbox-contract.md"


EVIDENCE = [
    {
        "id": "change_music_sends_one_based_track_id",
        "path": "refs/ebsrc-main/ebsrc-main/src/audio/change_music.asm",
        "claim": "CHANGE_MUSIC decrements the requested track for table lookup, then increments it and calls UNKNOWN_C0ABBD, so the mailbox command is the one-based track id.",
    },
    {
        "id": "c0_abbd_writes_apuio0",
        "path": "src/c0/c0_abbd_send_apu_port0_command_byte.asm",
        "claim": "Local C0 source confirms C0:ABBD stores A low byte to CPU register $002140/APUIO0 with long-addressed STA.",
    },
    {
        "id": "c0_ac20_reads_apuio0",
        "path": "src/c0/c0_ac20_read_apu_port0_byte.asm",
        "claim": "Local C0 source confirms C0:AC20 reads CPU register $2140/APUIO0 and masks it to one byte.",
    },
    {
        "id": "stop_music_waits_for_zero_ack",
        "path": "refs/ebsrc-main/ebsrc-main/src/audio/stop_music.asm",
        "claim": "STOP_MUSIC writes zero to APUIO0 and polls C0:AC20 until APUIO0 reads back zero.",
    },
    {
        "id": "ares_cpu_apu_ports",
        "path": "external:ares/ares/sfc/cpu/io.cpp",
        "claim": "ares CPU $2140-$2143 accesses synchronize with SMP and call smp.portRead/portWrite.",
    },
    {
        "id": "ares_smp_mailbox_ports",
        "path": "external:ares/ares/sfc/smp/io.cpp",
        "claim": "ares SMP $F4-$F7 accesses synchronize with CPU and expose the reciprocal APU/CPU mailbox fields.",
    },
    {
        "id": "diagnostic_mailbox_frontier",
        "path": "build/audio/command-on-first-read-jobs/mailbox-frontier.json",
        "claim": "Generated ignored frontier proving the current diagnostic command transcript across the representative 20-track corpus.",
    },
    {
        "id": "ares_smp_mailbox_smoke",
        "path": "build/audio/ares-smp-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json",
        "claim": "Generated ignored corpus proving timed ares::SuperFamicom::smp.portWrite delivery reaches the command read, zero ack, and key-on boundary across representative tracks.",
    },
    {
        "id": "ares_smp_mailbox_spc_index",
        "path": "build/audio/ares-smp-mailbox-spc/ares-smp-mailbox-spc-snapshots.json",
        "claim": "Generated ignored index of real ares SMP mailbox snapshots captured at the key-on boundary for snes_spc/libgme rendering.",
    },
    {
        "id": "ares_smp_mailbox_render_metrics",
        "path": "build/audio/ares-smp-mailbox-render-jobs/libgme-render-metrics.json",
        "claim": "Generated ignored render metrics proving the ares SMP mailbox snapshots are audible across the representative track corpus.",
    },
    {
        "id": "ares_cpu_writeapu_mailbox_smoke",
        "path": "build/audio/ares-cpu-writeapu-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json",
        "claim": "Generated ignored corpus proving timed ares::SuperFamicom::cpu.writeAPU($2140, track) delivery reaches the same command read, zero ack, and key-on boundary across representative tracks.",
    },
    {
        "id": "ares_cpu_writeapu_render_metrics",
        "path": "build/audio/ares-cpu-writeapu-mailbox-render-jobs/libgme-render-metrics.json",
        "claim": "Generated ignored render metrics proving CPU-side ares writeAPU mailbox snapshots are audible across the representative track corpus.",
    },
    {
        "id": "ares_wdc65816_sta2140_mailbox_smoke",
        "path": "build/audio/ares-wdc65816-sta2140-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json",
        "claim": "Generated ignored corpus proving a modeled WDC65816 execution of the C0:ABBD sep/sta $2140 prefix can deliver the track command through ares' CPU/APU bridge and reach key-on across representative tracks.",
    },
    {
        "id": "ares_wdc65816_sta2140_render_metrics",
        "path": "build/audio/ares-wdc65816-sta2140-mailbox-render-jobs/libgme-render-metrics.json",
        "claim": "Generated ignored render metrics proving the WDC65816 STA $2140 bridge snapshots are audible across the representative track corpus.",
    },
    {
        "id": "ares_wdc65816_full_c0abbd_mailbox_smoke",
        "path": "build/audio/ares-wdc65816-c0abbd-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json",
        "claim": "Generated ignored corpus proving modeled execution of the full C0:ABBD routine can deliver the track command through ares' CPU/APU bridge and reach key-on across representative tracks.",
    },
    {
        "id": "ares_wdc65816_full_c0abbd_render_metrics",
        "path": "build/audio/ares-wdc65816-c0abbd-mailbox-render-jobs/libgme-render-metrics.json",
        "claim": "Generated ignored render metrics proving full C0:ABBD bridge snapshots are audible across the representative track corpus.",
    },
    {
        "id": "rom_c0abbd_cpu_routine_fixture",
        "path": "build/audio/cpu-routine-fixtures/audio-cpu-routine-fixtures.json",
        "claim": "Generated ignored fixture manifest proving the ROM bytes at C0:ABBD are E2 20 8F 40 21 00 C2 30 6B, i.e. SEP; STA long $002140; REP; RTL.",
    },
    {
        "id": "ares_wdc65816_rom_c0abbd_mailbox_smoke",
        "path": "build/audio/ares-wdc65816-rom-c0abbd-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json",
        "claim": "Generated ignored corpus proving execution of ROM-derived C0:ABBD bytes through the WDC65816 probe reaches command read, zero ack, and key-on across representative tracks.",
    },
    {
        "id": "ares_wdc65816_rom_c0abbd_render_metrics",
        "path": "build/audio/ares-wdc65816-rom-c0abbd-mailbox-render-jobs/libgme-render-metrics.json",
        "claim": "Generated ignored render metrics proving ROM-derived C0:ABBD bridge snapshots are audible across the representative track corpus.",
    },
    {
        "id": "ares_wdc65816_rom_c0abbd_jsl_mailbox_smoke",
        "path": "build/audio/ares-wdc65816-rom-c0abbd-jsl-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json",
        "claim": "Generated ignored corpus proving a real WDC65816 JSL into ROM-derived C0:ABBD reaches RTL return, command read, zero ack, and key-on across representative tracks.",
    },
    {
        "id": "ares_wdc65816_rom_c0abbd_jsl_render_metrics",
        "path": "build/audio/ares-wdc65816-rom-c0abbd-jsl-mailbox-render-jobs/libgme-render-metrics.json",
        "claim": "Generated ignored render metrics proving ROM-derived C0:ABBD JSL-call snapshots are audible across the representative track corpus.",
    },
    {
        "id": "ares_wdc65816_change_music_tail_mailbox_smoke",
        "path": "build/audio/ares-wdc65816-change-music-tail-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json",
        "claim": "Generated ignored corpus proving the ROM-derived C4:FD0E CHANGE_MUSIC tail computes the one-based track command and reaches C0:ABBD, command read, zero ack, and key-on across representative tracks.",
    },
    {
        "id": "ares_wdc65816_change_music_tail_render_metrics",
        "path": "build/audio/ares-wdc65816-change-music-tail-mailbox-render-jobs/libgme-render-metrics.json",
        "claim": "Generated ignored render metrics proving CHANGE_MUSIC tail snapshots are audible across the representative track corpus.",
    },
    {
        "id": "ares_wdc65816_full_change_music_mailbox_smoke",
        "path": "build/audio/ares-wdc65816-full-change-music-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json",
        "claim": "Generated ignored corpus proving the ROM-derived C4:FBBD CHANGE_MUSIC body can run under a pre-satisfied pack state, compute the one-based track command, call C0:ABBD, return, and reach key-on across representative tracks.",
    },
    {
        "id": "ares_wdc65816_full_change_music_render_metrics",
        "path": "build/audio/ares-wdc65816-full-change-music-mailbox-render-jobs/libgme-render-metrics.json",
        "claim": "Generated ignored render metrics proving full CHANGE_MUSIC pre-satisfied-pack snapshots are audible across the representative track corpus.",
    },
    {
        "id": "ares_wdc65816_full_change_music_load_stub_mailbox_smoke",
        "path": "build/audio/ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json",
        "claim": "Generated ignored corpus proving the ROM-derived C4:FBBD CHANGE_MUSIC body can run its real pack-decision branches, call a stubbed LOAD_SPC700_DATA for each required pack, compute the one-based track command, call C0:ABBD, return, and reach key-on across representative tracks.",
    },
    {
        "id": "ares_wdc65816_full_change_music_load_stub_metrics",
        "path": "build/audio/ares-wdc65816-full-change-music-load-stub-mailbox-smoke-jobs/change-music-load-stub-metrics.json",
        "claim": "Generated ignored metrics proving the LOAD_SPC700_DATA stub call arguments match MusicDatasetTable and MusicPackPointerTable for every representative track.",
    },
    {
        "id": "ares_wdc65816_full_change_music_load_stub_render_metrics",
        "path": "build/audio/ares-wdc65816-full-change-music-load-stub-mailbox-render-jobs/libgme-render-metrics.json",
        "claim": "Generated ignored render metrics proving full CHANGE_MUSIC load-path-stub snapshots are audible across the representative track corpus.",
    },
    {
        "id": "ares_wdc65816_full_change_music_load_apply_mailbox_smoke",
        "path": "build/audio/ares-wdc65816-full-change-music-load-apply-mailbox-smoke-jobs/smp-mailbox-smoke-summary.json",
        "claim": "Generated ignored corpus proving full CHANGE_MUSIC can start from bootstrap APU RAM, run real pack-decision branches, apply selected LOAD_SPC700_DATA payload streams into ares APU RAM, send the one-based track command, and reach key-on across representative tracks.",
    },
    {
        "id": "ares_wdc65816_full_change_music_load_apply_render_metrics",
        "path": "build/audio/ares-wdc65816-full-change-music-load-apply-mailbox-render-jobs/libgme-render-metrics.json",
        "claim": "Generated ignored render metrics proving full CHANGE_MUSIC load-apply snapshots are audible across the representative track corpus.",
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the audio CPU/APU mailbox contract.")
    parser.add_argument("--frontier", default=str(DEFAULT_FRONTIER), help="Generated mailbox frontier JSON.")
    parser.add_argument("--smp-smoke", default=str(DEFAULT_SMP_SMOKE), help="Generated ares SMP mailbox smoke summary JSON.")
    parser.add_argument("--smp-render", default=str(DEFAULT_SMP_RENDER), help="Generated ares SMP mailbox render metrics JSON.")
    parser.add_argument("--smp-render-vs-last-keyon", default=str(DEFAULT_SMP_RENDER_VS_LAST_KEYON), help="Generated ares SMP mailbox render comparison versus the custom last-key-on corpus.")
    parser.add_argument("--smp-render-vs-baseline", default=str(DEFAULT_SMP_RENDER_VS_BASELINE), help="Generated ares SMP mailbox render comparison versus the baseline diagnostic corpus.")
    parser.add_argument("--cpu-writeapu-smoke", default=str(DEFAULT_CPU_WRITEAPU_SMOKE), help="Generated ares CPU writeAPU mailbox smoke summary JSON.")
    parser.add_argument("--cpu-writeapu-render", default=str(DEFAULT_CPU_WRITEAPU_RENDER), help="Generated ares CPU writeAPU render metrics JSON.")
    parser.add_argument("--cpu-writeapu-render-vs-smp", default=str(DEFAULT_CPU_WRITEAPU_RENDER_VS_SMP), help="Generated CPU writeAPU render comparison versus direct SMP portWrite corpus.")
    parser.add_argument("--cpu-writeapu-render-vs-baseline", default=str(DEFAULT_CPU_WRITEAPU_RENDER_VS_BASELINE), help="Generated CPU writeAPU render comparison versus baseline diagnostic corpus.")
    parser.add_argument("--wdc65816-smoke", default=str(DEFAULT_WDC65816_SMOKE), help="Generated WDC65816 STA $2140 mailbox smoke summary JSON.")
    parser.add_argument("--wdc65816-render", default=str(DEFAULT_WDC65816_RENDER), help="Generated WDC65816 STA $2140 render metrics JSON.")
    parser.add_argument("--wdc65816-render-vs-cpu-writeapu", default=str(DEFAULT_WDC65816_RENDER_VS_CPU_WRITEAPU), help="Generated WDC65816 render comparison versus CPU writeAPU corpus.")
    parser.add_argument("--wdc65816-render-vs-baseline", default=str(DEFAULT_WDC65816_RENDER_VS_BASELINE), help="Generated WDC65816 render comparison versus baseline diagnostic corpus.")
    parser.add_argument("--full-c0abbd-smoke", default=str(DEFAULT_FULL_C0ABBD_SMOKE), help="Generated full C0:ABBD mailbox smoke summary JSON.")
    parser.add_argument("--full-c0abbd-render", default=str(DEFAULT_FULL_C0ABBD_RENDER), help="Generated full C0:ABBD render metrics JSON.")
    parser.add_argument("--full-c0abbd-render-vs-sta2140", default=str(DEFAULT_FULL_C0ABBD_RENDER_VS_STA2140), help="Generated full C0:ABBD render comparison versus WDC65816 STA $2140 corpus.")
    parser.add_argument("--full-c0abbd-render-vs-baseline", default=str(DEFAULT_FULL_C0ABBD_RENDER_VS_BASELINE), help="Generated full C0:ABBD render comparison versus baseline diagnostic corpus.")
    parser.add_argument("--cpu-routine-fixtures", default=str(DEFAULT_CPU_ROUTINE_FIXTURES), help="Generated ROM-derived CPU routine fixture manifest JSON.")
    parser.add_argument("--rom-c0abbd-smoke", default=str(DEFAULT_ROM_C0ABBD_SMOKE), help="Generated ROM-derived C0:ABBD mailbox smoke summary JSON.")
    parser.add_argument("--rom-c0abbd-render", default=str(DEFAULT_ROM_C0ABBD_RENDER), help="Generated ROM-derived C0:ABBD render metrics JSON.")
    parser.add_argument("--rom-c0abbd-render-vs-modeled", default=str(DEFAULT_ROM_C0ABBD_RENDER_VS_MODELED), help="Generated ROM-derived C0:ABBD render comparison versus modeled full C0:ABBD corpus.")
    parser.add_argument("--rom-c0abbd-render-vs-baseline", default=str(DEFAULT_ROM_C0ABBD_RENDER_VS_BASELINE), help="Generated ROM-derived C0:ABBD render comparison versus baseline diagnostic corpus.")
    parser.add_argument("--rom-c0abbd-jsl-smoke", default=str(DEFAULT_ROM_C0ABBD_JSL_SMOKE), help="Generated ROM-derived C0:ABBD JSL-call mailbox smoke summary JSON.")
    parser.add_argument("--rom-c0abbd-jsl-render", default=str(DEFAULT_ROM_C0ABBD_JSL_RENDER), help="Generated ROM-derived C0:ABBD JSL-call render metrics JSON.")
    parser.add_argument("--rom-c0abbd-jsl-render-vs-direct", default=str(DEFAULT_ROM_C0ABBD_JSL_RENDER_VS_DIRECT), help="Generated ROM-derived C0:ABBD JSL-call render comparison versus direct ROM-derived C0:ABBD corpus.")
    parser.add_argument("--rom-c0abbd-jsl-render-vs-baseline", default=str(DEFAULT_ROM_C0ABBD_JSL_RENDER_VS_BASELINE), help="Generated ROM-derived C0:ABBD JSL-call render comparison versus baseline diagnostic corpus.")
    parser.add_argument("--change-music-tail-smoke", default=str(DEFAULT_CHANGE_MUSIC_TAIL_SMOKE), help="Generated CHANGE_MUSIC tail mailbox smoke summary JSON.")
    parser.add_argument("--change-music-tail-render", default=str(DEFAULT_CHANGE_MUSIC_TAIL_RENDER), help="Generated CHANGE_MUSIC tail render metrics JSON.")
    parser.add_argument("--change-music-tail-render-vs-c0abbd-jsl", default=str(DEFAULT_CHANGE_MUSIC_TAIL_RENDER_VS_C0ABBD_JSL), help="Generated CHANGE_MUSIC tail render comparison versus ROM-derived C0:ABBD JSL corpus.")
    parser.add_argument("--change-music-tail-render-vs-baseline", default=str(DEFAULT_CHANGE_MUSIC_TAIL_RENDER_VS_BASELINE), help="Generated CHANGE_MUSIC tail render comparison versus baseline diagnostic corpus.")
    parser.add_argument("--full-change-music-smoke", default=str(DEFAULT_FULL_CHANGE_MUSIC_SMOKE), help="Generated full CHANGE_MUSIC mailbox smoke summary JSON.")
    parser.add_argument("--full-change-music-render", default=str(DEFAULT_FULL_CHANGE_MUSIC_RENDER), help="Generated full CHANGE_MUSIC render metrics JSON.")
    parser.add_argument("--full-change-music-render-vs-tail", default=str(DEFAULT_FULL_CHANGE_MUSIC_RENDER_VS_TAIL), help="Generated full CHANGE_MUSIC render comparison versus CHANGE_MUSIC tail corpus.")
    parser.add_argument("--full-change-music-render-vs-baseline", default=str(DEFAULT_FULL_CHANGE_MUSIC_RENDER_VS_BASELINE), help="Generated full CHANGE_MUSIC render comparison versus baseline diagnostic corpus.")
    parser.add_argument("--full-change-music-load-stub-smoke", default=str(DEFAULT_FULL_CHANGE_MUSIC_LOAD_STUB_SMOKE), help="Generated full CHANGE_MUSIC load-path-stub mailbox smoke summary JSON.")
    parser.add_argument("--full-change-music-load-stub-metrics", default=str(DEFAULT_FULL_CHANGE_MUSIC_LOAD_STUB_METRICS), help="Generated full CHANGE_MUSIC load-path-stub metrics JSON.")
    parser.add_argument("--full-change-music-load-stub-render", default=str(DEFAULT_FULL_CHANGE_MUSIC_LOAD_STUB_RENDER), help="Generated full CHANGE_MUSIC load-path-stub render metrics JSON.")
    parser.add_argument("--full-change-music-load-stub-render-vs-presatisfied", default=str(DEFAULT_FULL_CHANGE_MUSIC_LOAD_STUB_RENDER_VS_PRESATISFIED), help="Generated full CHANGE_MUSIC load-path-stub render comparison versus pre-satisfied full CHANGE_MUSIC corpus.")
    parser.add_argument("--full-change-music-load-stub-render-vs-baseline", default=str(DEFAULT_FULL_CHANGE_MUSIC_LOAD_STUB_RENDER_VS_BASELINE), help="Generated full CHANGE_MUSIC load-path-stub render comparison versus baseline diagnostic corpus.")
    parser.add_argument("--full-change-music-load-apply-smoke", default=str(DEFAULT_FULL_CHANGE_MUSIC_LOAD_APPLY_SMOKE), help="Generated full CHANGE_MUSIC load-apply mailbox smoke summary JSON.")
    parser.add_argument("--full-change-music-load-apply-metrics", default=str(DEFAULT_FULL_CHANGE_MUSIC_LOAD_APPLY_METRICS), help="Generated full CHANGE_MUSIC load-apply metrics JSON.")
    parser.add_argument("--full-change-music-load-apply-render", default=str(DEFAULT_FULL_CHANGE_MUSIC_LOAD_APPLY_RENDER), help="Generated full CHANGE_MUSIC load-apply render metrics JSON.")
    parser.add_argument("--full-change-music-load-apply-render-vs-stub", default=str(DEFAULT_FULL_CHANGE_MUSIC_LOAD_APPLY_RENDER_VS_STUB), help="Generated full CHANGE_MUSIC load-apply render comparison versus load-stub corpus.")
    parser.add_argument("--full-change-music-load-apply-render-vs-baseline", default=str(DEFAULT_FULL_CHANGE_MUSIC_LOAD_APPLY_RENDER_VS_BASELINE), help="Generated full CHANGE_MUSIC load-apply render comparison versus baseline diagnostic corpus.")
    parser.add_argument("--json", default=str(DEFAULT_JSON), help="Contract JSON output.")
    parser.add_argument("--markdown", default=str(DEFAULT_MARKDOWN), help="Contract Markdown output.")
    return parser.parse_args()


def load_json_if_exists(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def path_exists(path_text: str) -> bool:
    if path_text.startswith("external:ares/"):
        return (EXTERNAL_ARES_ROOT / path_text[len("external:ares/") :]).exists()
    return (ROOT / path_text).exists()


def repo_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def build_contract(
    frontier: dict[str, Any] | None,
    frontier_path: Path,
    smp_smoke: dict[str, Any] | None,
    smp_smoke_path: Path,
    smp_render: dict[str, Any] | None,
    smp_render_path: Path,
    smp_render_vs_last_keyon: dict[str, Any] | None,
    smp_render_vs_baseline: dict[str, Any] | None,
    cpu_writeapu_smoke: dict[str, Any] | None,
    cpu_writeapu_smoke_path: Path,
    cpu_writeapu_render: dict[str, Any] | None,
    cpu_writeapu_render_path: Path,
    cpu_writeapu_render_vs_smp: dict[str, Any] | None,
    cpu_writeapu_render_vs_baseline: dict[str, Any] | None,
    wdc65816_smoke: dict[str, Any] | None,
    wdc65816_smoke_path: Path,
    wdc65816_render: dict[str, Any] | None,
    wdc65816_render_path: Path,
    wdc65816_render_vs_cpu_writeapu: dict[str, Any] | None,
    wdc65816_render_vs_baseline: dict[str, Any] | None,
    full_c0abbd_smoke: dict[str, Any] | None,
    full_c0abbd_smoke_path: Path,
    full_c0abbd_render: dict[str, Any] | None,
    full_c0abbd_render_path: Path,
    full_c0abbd_render_vs_sta2140: dict[str, Any] | None,
    full_c0abbd_render_vs_baseline: dict[str, Any] | None,
    cpu_routine_fixtures: dict[str, Any] | None,
    cpu_routine_fixtures_path: Path,
    rom_c0abbd_smoke: dict[str, Any] | None,
    rom_c0abbd_smoke_path: Path,
    rom_c0abbd_render: dict[str, Any] | None,
    rom_c0abbd_render_path: Path,
    rom_c0abbd_render_vs_modeled: dict[str, Any] | None,
    rom_c0abbd_render_vs_baseline: dict[str, Any] | None,
    rom_c0abbd_jsl_smoke: dict[str, Any] | None,
    rom_c0abbd_jsl_smoke_path: Path,
    rom_c0abbd_jsl_render: dict[str, Any] | None,
    rom_c0abbd_jsl_render_path: Path,
    rom_c0abbd_jsl_render_vs_direct: dict[str, Any] | None,
    rom_c0abbd_jsl_render_vs_baseline: dict[str, Any] | None,
    change_music_tail_smoke: dict[str, Any] | None,
    change_music_tail_smoke_path: Path,
    change_music_tail_render: dict[str, Any] | None,
    change_music_tail_render_path: Path,
    change_music_tail_render_vs_c0abbd_jsl: dict[str, Any] | None,
    change_music_tail_render_vs_baseline: dict[str, Any] | None,
    full_change_music_smoke: dict[str, Any] | None,
    full_change_music_smoke_path: Path,
    full_change_music_render: dict[str, Any] | None,
    full_change_music_render_path: Path,
    full_change_music_render_vs_tail: dict[str, Any] | None,
    full_change_music_render_vs_baseline: dict[str, Any] | None,
    full_change_music_load_stub_smoke: dict[str, Any] | None,
    full_change_music_load_stub_smoke_path: Path,
    full_change_music_load_stub_metrics: dict[str, Any] | None,
    full_change_music_load_stub_metrics_path: Path,
    full_change_music_load_stub_render: dict[str, Any] | None,
    full_change_music_load_stub_render_path: Path,
    full_change_music_load_stub_render_vs_presatisfied: dict[str, Any] | None,
    full_change_music_load_stub_render_vs_baseline: dict[str, Any] | None,
    full_change_music_load_apply_smoke: dict[str, Any] | None,
    full_change_music_load_apply_smoke_path: Path,
    full_change_music_load_apply_metrics: dict[str, Any] | None,
    full_change_music_load_apply_metrics_path: Path,
    full_change_music_load_apply_render: dict[str, Any] | None,
    full_change_music_load_apply_render_path: Path,
    full_change_music_load_apply_render_vs_stub: dict[str, Any] | None,
    full_change_music_load_apply_render_vs_baseline: dict[str, Any] | None,
) -> dict[str, Any]:
    frontier_summary = frontier.get("summary", {}) if frontier else {}
    first_read_pc_counts = frontier_summary.get("first_read_pc_counts", {})
    first_ack_pc_counts = frontier_summary.get("first_ack_pc_counts", {})
    return {
        "schema": "earthbound-decomp.audio-cpu-mailbox-contract.v1",
        "status": "diagnostic_mailbox_transcript_pinned_full_change_music_loader_apply_bridge_apuio_handshake_and_full_scheduling_pending",
        "source_policy": {
            "requires_user_supplied_rom": True,
            "generated_frontiers_are_ignored": True,
            "generated_frontier_path": repo_path(frontier_path),
            "generated_smp_smoke_path": repo_path(smp_smoke_path),
            "generated_smp_render_path": repo_path(smp_render_path),
            "generated_cpu_writeapu_smoke_path": repo_path(cpu_writeapu_smoke_path),
            "generated_cpu_writeapu_render_path": repo_path(cpu_writeapu_render_path),
            "generated_wdc65816_smoke_path": repo_path(wdc65816_smoke_path),
            "generated_wdc65816_render_path": repo_path(wdc65816_render_path),
            "generated_full_c0abbd_smoke_path": repo_path(full_c0abbd_smoke_path),
            "generated_full_c0abbd_render_path": repo_path(full_c0abbd_render_path),
            "generated_cpu_routine_fixtures_path": repo_path(cpu_routine_fixtures_path),
            "generated_rom_c0abbd_smoke_path": repo_path(rom_c0abbd_smoke_path),
            "generated_rom_c0abbd_render_path": repo_path(rom_c0abbd_render_path),
            "generated_rom_c0abbd_jsl_smoke_path": repo_path(rom_c0abbd_jsl_smoke_path),
            "generated_rom_c0abbd_jsl_render_path": repo_path(rom_c0abbd_jsl_render_path),
            "generated_change_music_tail_smoke_path": repo_path(change_music_tail_smoke_path),
            "generated_change_music_tail_render_path": repo_path(change_music_tail_render_path),
            "generated_full_change_music_smoke_path": repo_path(full_change_music_smoke_path),
            "generated_full_change_music_render_path": repo_path(full_change_music_render_path),
            "generated_full_change_music_load_stub_smoke_path": repo_path(full_change_music_load_stub_smoke_path),
            "generated_full_change_music_load_stub_metrics_path": repo_path(full_change_music_load_stub_metrics_path),
            "generated_full_change_music_load_stub_render_path": repo_path(full_change_music_load_stub_render_path),
            "generated_full_change_music_load_apply_smoke_path": repo_path(full_change_music_load_apply_smoke_path),
            "generated_full_change_music_load_apply_metrics_path": repo_path(full_change_music_load_apply_metrics_path),
            "generated_full_change_music_load_apply_render_path": repo_path(full_change_music_load_apply_render_path),
        },
        "cpu_side_contract": {
            "send_track_command_entry": "C0:ABBD",
            "send_track_command_name": "C0ABBD_SendApuPort0CommandByte",
            "send_track_command_register": "$2140/APUIO0",
            "send_track_command_opcode": "STA long $002140",
            "send_track_command_rom_bytes": "E2 20 8F 40 21 00 C2 30 6B",
            "send_track_command_width": "A low byte",
            "track_command_value": "one_based_track_id",
            "read_ack_entry": "C0:AC20",
            "read_ack_name": "C0AC20_ReadApuPort0Byte",
            "read_ack_register": "$2140/APUIO0",
            "stop_music_ack_value": "0x00",
        },
        "apu_side_diagnostic_contract": {
            "driver_first_command_read_pc": "0x062A",
            "driver_first_command_read_address": "0x00F4",
            "driver_first_ack_write_pc": "0x062A",
            "driver_first_ack_write_address": "0x00F4",
            "driver_first_ack_write_data": "0x00",
            "keyon_must_follow_command_read": True,
            "diagnostic_mode": "on_first_port0_read",
        },
        "ares_bridge_contract": {
            "cpu_to_apu_entrypoint": "ares::SuperFamicom::cpu.writeAPU -> smp.portWrite(address.bit(0,1), data)",
            "apu_to_cpu_entrypoint": "ares::SuperFamicom::cpu.readAPU -> smp.portRead(address.bit(0,1))",
            "smp_reads_cpu_mailbox": "SMP::readIO(0x00f4) returns io.apu0 after synchronize(cpu)",
            "smp_writes_apu_mailbox": "SMP::writeIO(0x00f4, data) stores io.cpu0 after synchronize(cpu)",
            "full_fidelity_implication": "The current bridge can execute ROM-derived C4:FBBD CHANGE_MUSIC bytes under a documented pre-satisfied pack state, then route the C0:ABBD STA long $002140 write through WDC65816 semantics and ares' CPU/APU port path. The next accurate harness should replace the pre-satisfied pack/table stubs with real scheduled pack-loading context and produce the same mailbox transcript without timed injection.",
        },
        "current_frontier_summary": {
            "available": frontier is not None,
            "job_count": frontier.get("job_count", 0) if frontier else 0,
            "capture_count": int(frontier_summary.get("capture_count", 0)),
            "mode_counts": frontier_summary.get("mode_counts", {}),
            "command_read_count": int(frontier_summary.get("command_read_count", 0)),
            "command_match_count": int(frontier_summary.get("command_match_count", 0)),
            "zero_ack_write_count": int(frontier_summary.get("zero_ack_write_count", 0)),
            "keyon_after_command_read_count": int(frontier_summary.get("keyon_after_command_read_count", 0)),
            "first_read_pc_counts": first_read_pc_counts,
            "first_ack_pc_counts": first_ack_pc_counts,
        },
        "current_ares_smp_smoke_summary": {
            "available": smp_smoke is not None,
            "job_count": int(smp_smoke.get("job_count", 0)) if smp_smoke else 0,
            "success_count": int(smp_smoke.get("success_count", 0)) if smp_smoke else 0,
            "command_read_count": int(smp_smoke.get("command_read_count", 0)) if smp_smoke else 0,
            "zero_ack_count": int(smp_smoke.get("zero_ack_count", 0)) if smp_smoke else 0,
            "key_on_count": int(smp_smoke.get("key_on_count", 0)) if smp_smoke else 0,
            "delivery_mode": "ares_smp_portwrite_on_pc_062a",
        },
        "current_ares_smp_render_summary": {
            "available": smp_render is not None,
            "metric_count": int(smp_render.get("metrics_count", 0)) if smp_render else 0,
            "classification_counts": smp_render.get("classification_counts", {}) if smp_render else {},
            "versus_custom_last_keyon": {
                "available": smp_render_vs_last_keyon is not None,
                "improved_count": int(smp_render_vs_last_keyon.get("improved_count", 0)) if smp_render_vs_last_keyon else 0,
                "unchanged_count": int(smp_render_vs_last_keyon.get("unchanged_count", 0)) if smp_render_vs_last_keyon else 0,
                "worsened_count": int(smp_render_vs_last_keyon.get("worsened_count", 0)) if smp_render_vs_last_keyon else 0,
            },
            "versus_baseline": {
                "available": smp_render_vs_baseline is not None,
                "improved_count": int(smp_render_vs_baseline.get("improved_count", 0)) if smp_render_vs_baseline else 0,
                "unchanged_count": int(smp_render_vs_baseline.get("unchanged_count", 0)) if smp_render_vs_baseline else 0,
                "worsened_count": int(smp_render_vs_baseline.get("worsened_count", 0)) if smp_render_vs_baseline else 0,
            },
        },
        "current_ares_cpu_writeapu_summary": {
            "available": cpu_writeapu_smoke is not None,
            "job_count": int(cpu_writeapu_smoke.get("job_count", 0)) if cpu_writeapu_smoke else 0,
            "success_count": int(cpu_writeapu_smoke.get("success_count", 0)) if cpu_writeapu_smoke else 0,
            "command_read_count": int(cpu_writeapu_smoke.get("command_read_count", 0)) if cpu_writeapu_smoke else 0,
            "zero_ack_count": int(cpu_writeapu_smoke.get("zero_ack_count", 0)) if cpu_writeapu_smoke else 0,
            "key_on_count": int(cpu_writeapu_smoke.get("key_on_count", 0)) if cpu_writeapu_smoke else 0,
            "delivery_mode": "ares_cpu_writeapu_2140_on_pc_062a",
            "render": {
                "available": cpu_writeapu_render is not None,
                "metric_count": int(cpu_writeapu_render.get("metrics_count", 0)) if cpu_writeapu_render else 0,
                "classification_counts": cpu_writeapu_render.get("classification_counts", {}) if cpu_writeapu_render else {},
                "versus_smp_portwrite": {
                    "available": cpu_writeapu_render_vs_smp is not None,
                    "improved_count": int(cpu_writeapu_render_vs_smp.get("improved_count", 0)) if cpu_writeapu_render_vs_smp else 0,
                    "unchanged_count": int(cpu_writeapu_render_vs_smp.get("unchanged_count", 0)) if cpu_writeapu_render_vs_smp else 0,
                    "worsened_count": int(cpu_writeapu_render_vs_smp.get("worsened_count", 0)) if cpu_writeapu_render_vs_smp else 0,
                },
                "versus_baseline": {
                    "available": cpu_writeapu_render_vs_baseline is not None,
                    "improved_count": int(cpu_writeapu_render_vs_baseline.get("improved_count", 0)) if cpu_writeapu_render_vs_baseline else 0,
                    "unchanged_count": int(cpu_writeapu_render_vs_baseline.get("unchanged_count", 0)) if cpu_writeapu_render_vs_baseline else 0,
                    "worsened_count": int(cpu_writeapu_render_vs_baseline.get("worsened_count", 0)) if cpu_writeapu_render_vs_baseline else 0,
                },
            },
        },
        "current_ares_wdc65816_summary": {
            "available": wdc65816_smoke is not None,
            "job_count": int(wdc65816_smoke.get("job_count", 0)) if wdc65816_smoke else 0,
            "success_count": int(wdc65816_smoke.get("success_count", 0)) if wdc65816_smoke else 0,
            "command_read_count": int(wdc65816_smoke.get("command_read_count", 0)) if wdc65816_smoke else 0,
            "zero_ack_count": int(wdc65816_smoke.get("zero_ack_count", 0)) if wdc65816_smoke else 0,
            "key_on_count": int(wdc65816_smoke.get("key_on_count", 0)) if wdc65816_smoke else 0,
            "delivery_mode": "ares_wdc65816_sta_2140_on_pc_062a",
            "routine": "sep_20_sta_002140_prefix_of_C0ABBD",
            "render": {
                "available": wdc65816_render is not None,
                "metric_count": int(wdc65816_render.get("metrics_count", 0)) if wdc65816_render else 0,
                "classification_counts": wdc65816_render.get("classification_counts", {}) if wdc65816_render else {},
                "versus_cpu_writeapu": {
                    "available": wdc65816_render_vs_cpu_writeapu is not None,
                    "improved_count": int(wdc65816_render_vs_cpu_writeapu.get("improved_count", 0)) if wdc65816_render_vs_cpu_writeapu else 0,
                    "unchanged_count": int(wdc65816_render_vs_cpu_writeapu.get("unchanged_count", 0)) if wdc65816_render_vs_cpu_writeapu else 0,
                    "worsened_count": int(wdc65816_render_vs_cpu_writeapu.get("worsened_count", 0)) if wdc65816_render_vs_cpu_writeapu else 0,
                },
                "versus_baseline": {
                    "available": wdc65816_render_vs_baseline is not None,
                    "improved_count": int(wdc65816_render_vs_baseline.get("improved_count", 0)) if wdc65816_render_vs_baseline else 0,
                    "unchanged_count": int(wdc65816_render_vs_baseline.get("unchanged_count", 0)) if wdc65816_render_vs_baseline else 0,
                    "worsened_count": int(wdc65816_render_vs_baseline.get("worsened_count", 0)) if wdc65816_render_vs_baseline else 0,
                },
            },
        },
        "current_ares_full_c0abbd_summary": {
            "available": full_c0abbd_smoke is not None,
            "job_count": int(full_c0abbd_smoke.get("job_count", 0)) if full_c0abbd_smoke else 0,
            "success_count": int(full_c0abbd_smoke.get("success_count", 0)) if full_c0abbd_smoke else 0,
            "command_read_count": int(full_c0abbd_smoke.get("command_read_count", 0)) if full_c0abbd_smoke else 0,
            "zero_ack_count": int(full_c0abbd_smoke.get("zero_ack_count", 0)) if full_c0abbd_smoke else 0,
            "key_on_count": int(full_c0abbd_smoke.get("key_on_count", 0)) if full_c0abbd_smoke else 0,
            "delivery_mode": "ares_wdc65816_full_c0abbd_on_pc_062a",
            "routine": "full_C0ABBD_sep_sta_rep_rtl",
            "render": {
                "available": full_c0abbd_render is not None,
                "metric_count": int(full_c0abbd_render.get("metrics_count", 0)) if full_c0abbd_render else 0,
                "classification_counts": full_c0abbd_render.get("classification_counts", {}) if full_c0abbd_render else {},
                "versus_sta2140": {
                    "available": full_c0abbd_render_vs_sta2140 is not None,
                    "improved_count": int(full_c0abbd_render_vs_sta2140.get("improved_count", 0)) if full_c0abbd_render_vs_sta2140 else 0,
                    "unchanged_count": int(full_c0abbd_render_vs_sta2140.get("unchanged_count", 0)) if full_c0abbd_render_vs_sta2140 else 0,
                    "worsened_count": int(full_c0abbd_render_vs_sta2140.get("worsened_count", 0)) if full_c0abbd_render_vs_sta2140 else 0,
                },
                "versus_baseline": {
                    "available": full_c0abbd_render_vs_baseline is not None,
                    "improved_count": int(full_c0abbd_render_vs_baseline.get("improved_count", 0)) if full_c0abbd_render_vs_baseline else 0,
                    "unchanged_count": int(full_c0abbd_render_vs_baseline.get("unchanged_count", 0)) if full_c0abbd_render_vs_baseline else 0,
                    "worsened_count": int(full_c0abbd_render_vs_baseline.get("worsened_count", 0)) if full_c0abbd_render_vs_baseline else 0,
                },
            },
        },
        "current_ares_rom_c0abbd_summary": {
            "fixture_manifest_available": cpu_routine_fixtures is not None,
            "fixture_count": int(cpu_routine_fixtures.get("fixture_count", 0)) if cpu_routine_fixtures else 0,
            "available": rom_c0abbd_smoke is not None,
            "job_count": int(rom_c0abbd_smoke.get("job_count", 0)) if rom_c0abbd_smoke else 0,
            "success_count": int(rom_c0abbd_smoke.get("success_count", 0)) if rom_c0abbd_smoke else 0,
            "command_read_count": int(rom_c0abbd_smoke.get("command_read_count", 0)) if rom_c0abbd_smoke else 0,
            "zero_ack_count": int(rom_c0abbd_smoke.get("zero_ack_count", 0)) if rom_c0abbd_smoke else 0,
            "key_on_count": int(rom_c0abbd_smoke.get("key_on_count", 0)) if rom_c0abbd_smoke else 0,
            "delivery_mode": "ares_wdc65816_rom_c0abbd_on_pc_062a",
            "routine": "rom_fixture_C0ABBD_sep_sta_long_rep_rtl",
            "render": {
                "available": rom_c0abbd_render is not None,
                "metric_count": int(rom_c0abbd_render.get("metrics_count", 0)) if rom_c0abbd_render else 0,
                "classification_counts": rom_c0abbd_render.get("classification_counts", {}) if rom_c0abbd_render else {},
                "versus_modeled_full_c0abbd": {
                    "available": rom_c0abbd_render_vs_modeled is not None,
                    "improved_count": int(rom_c0abbd_render_vs_modeled.get("improved_count", 0)) if rom_c0abbd_render_vs_modeled else 0,
                    "unchanged_count": int(rom_c0abbd_render_vs_modeled.get("unchanged_count", 0)) if rom_c0abbd_render_vs_modeled else 0,
                    "worsened_count": int(rom_c0abbd_render_vs_modeled.get("worsened_count", 0)) if rom_c0abbd_render_vs_modeled else 0,
                },
                "versus_baseline": {
                    "available": rom_c0abbd_render_vs_baseline is not None,
                    "improved_count": int(rom_c0abbd_render_vs_baseline.get("improved_count", 0)) if rom_c0abbd_render_vs_baseline else 0,
                    "unchanged_count": int(rom_c0abbd_render_vs_baseline.get("unchanged_count", 0)) if rom_c0abbd_render_vs_baseline else 0,
                    "worsened_count": int(rom_c0abbd_render_vs_baseline.get("worsened_count", 0)) if rom_c0abbd_render_vs_baseline else 0,
                },
            },
        },
        "current_ares_rom_c0abbd_jsl_summary": {
            "available": rom_c0abbd_jsl_smoke is not None,
            "job_count": int(rom_c0abbd_jsl_smoke.get("job_count", 0)) if rom_c0abbd_jsl_smoke else 0,
            "success_count": int(rom_c0abbd_jsl_smoke.get("success_count", 0)) if rom_c0abbd_jsl_smoke else 0,
            "command_read_count": int(rom_c0abbd_jsl_smoke.get("command_read_count", 0)) if rom_c0abbd_jsl_smoke else 0,
            "zero_ack_count": int(rom_c0abbd_jsl_smoke.get("zero_ack_count", 0)) if rom_c0abbd_jsl_smoke else 0,
            "key_on_count": int(rom_c0abbd_jsl_smoke.get("key_on_count", 0)) if rom_c0abbd_jsl_smoke else 0,
            "delivery_mode": "ares_wdc65816_rom_c0abbd_jsl_on_pc_062a",
            "routine": "rom_fixture_C0ABBD_jsl_call_context",
            "call_shape": "JSL $C0ABBD from modeled caller, ROM-derived bytes mapped at C0:ABBD, RTL returns through modeled stack",
            "render": {
                "available": rom_c0abbd_jsl_render is not None,
                "metric_count": int(rom_c0abbd_jsl_render.get("metrics_count", 0)) if rom_c0abbd_jsl_render else 0,
                "classification_counts": rom_c0abbd_jsl_render.get("classification_counts", {}) if rom_c0abbd_jsl_render else {},
                "versus_direct_rom_c0abbd": {
                    "available": rom_c0abbd_jsl_render_vs_direct is not None,
                    "improved_count": int(rom_c0abbd_jsl_render_vs_direct.get("improved_count", 0)) if rom_c0abbd_jsl_render_vs_direct else 0,
                    "unchanged_count": int(rom_c0abbd_jsl_render_vs_direct.get("unchanged_count", 0)) if rom_c0abbd_jsl_render_vs_direct else 0,
                    "worsened_count": int(rom_c0abbd_jsl_render_vs_direct.get("worsened_count", 0)) if rom_c0abbd_jsl_render_vs_direct else 0,
                },
                "versus_baseline": {
                    "available": rom_c0abbd_jsl_render_vs_baseline is not None,
                    "improved_count": int(rom_c0abbd_jsl_render_vs_baseline.get("improved_count", 0)) if rom_c0abbd_jsl_render_vs_baseline else 0,
                    "unchanged_count": int(rom_c0abbd_jsl_render_vs_baseline.get("unchanged_count", 0)) if rom_c0abbd_jsl_render_vs_baseline else 0,
                    "worsened_count": int(rom_c0abbd_jsl_render_vs_baseline.get("worsened_count", 0)) if rom_c0abbd_jsl_render_vs_baseline else 0,
                },
            },
        },
        "current_ares_change_music_tail_summary": {
            "available": change_music_tail_smoke is not None,
            "job_count": int(change_music_tail_smoke.get("job_count", 0)) if change_music_tail_smoke else 0,
            "success_count": int(change_music_tail_smoke.get("success_count", 0)) if change_music_tail_smoke else 0,
            "command_read_count": int(change_music_tail_smoke.get("command_read_count", 0)) if change_music_tail_smoke else 0,
            "zero_ack_count": int(change_music_tail_smoke.get("zero_ack_count", 0)) if change_music_tail_smoke else 0,
            "key_on_count": int(change_music_tail_smoke.get("key_on_count", 0)) if change_music_tail_smoke else 0,
            "delivery_mode": "ares_wdc65816_change_music_tail_on_pc_062a",
            "routine": "rom_fixture_ChangeMusic_tail_to_C0ABBD",
            "tail_bytes": "A4 10 98 1A 22 BD AB C0 2B 6B",
            "call_shape": "C4:FD0E LDY $10; TYA; INC; JSL C0:ABBD; PLD; RTL with direct-page $10 preloaded to zero-based track index",
            "render": {
                "available": change_music_tail_render is not None,
                "metric_count": int(change_music_tail_render.get("metrics_count", 0)) if change_music_tail_render else 0,
                "classification_counts": change_music_tail_render.get("classification_counts", {}) if change_music_tail_render else {},
                "versus_rom_c0abbd_jsl": {
                    "available": change_music_tail_render_vs_c0abbd_jsl is not None,
                    "improved_count": int(change_music_tail_render_vs_c0abbd_jsl.get("improved_count", 0)) if change_music_tail_render_vs_c0abbd_jsl else 0,
                    "unchanged_count": int(change_music_tail_render_vs_c0abbd_jsl.get("unchanged_count", 0)) if change_music_tail_render_vs_c0abbd_jsl else 0,
                    "worsened_count": int(change_music_tail_render_vs_c0abbd_jsl.get("worsened_count", 0)) if change_music_tail_render_vs_c0abbd_jsl else 0,
                },
                "versus_baseline": {
                    "available": change_music_tail_render_vs_baseline is not None,
                    "improved_count": int(change_music_tail_render_vs_baseline.get("improved_count", 0)) if change_music_tail_render_vs_baseline else 0,
                    "unchanged_count": int(change_music_tail_render_vs_baseline.get("unchanged_count", 0)) if change_music_tail_render_vs_baseline else 0,
                    "worsened_count": int(change_music_tail_render_vs_baseline.get("worsened_count", 0)) if change_music_tail_render_vs_baseline else 0,
                },
            },
        },
        "current_ares_full_change_music_summary": {
            "available": full_change_music_smoke is not None,
            "job_count": int(full_change_music_smoke.get("job_count", 0)) if full_change_music_smoke else 0,
            "success_count": int(full_change_music_smoke.get("success_count", 0)) if full_change_music_smoke else 0,
            "command_read_count": int(full_change_music_smoke.get("command_read_count", 0)) if full_change_music_smoke else 0,
            "zero_ack_count": int(full_change_music_smoke.get("zero_ack_count", 0)) if full_change_music_smoke else 0,
            "key_on_count": int(full_change_music_smoke.get("key_on_count", 0)) if full_change_music_smoke else 0,
            "delivery_mode": "ares_wdc65816_full_change_music_on_pc_062a",
            "routine": "rom_fixture_ChangeMusic_full_presatisfied_packs",
            "call_shape": "C4:FBBD CHANGE_MUSIC body executes from ROM-derived bytes with A seeded to the requested one-based track id, MusicDatasetTable reads served from a ROM-derived fixture, current pack variables pre-satisfied to the requested track's real table row, helper side effects stubbed, and JSL C0:ABBD mapped to ROM-derived bytes.",
            "known_shortcuts": [
                "APU RAM seed is already built for the target track before the command is delivered.",
                "MusicDatasetTable bytes are real ROM-derived fixture bytes, but CurrentPrimarySamplePack, CurrentSecondarySamplePack, and CurrentSequencePack are pre-satisfied to the selected row so pack loads are skipped in this isolated CPU probe.",
                "LOAD_SPC700_DATA, STOP_MUSIC, STOP_MUSIC_TRANSITION, and PLAY_SOUND_UNKNOWN0 are RTL stubs if reached.",
                "The harness still times CPU delivery at the SMP $062A command-read boundary.",
            ],
            "render": {
                "available": full_change_music_render is not None,
                "metric_count": int(full_change_music_render.get("metrics_count", 0)) if full_change_music_render else 0,
                "classification_counts": full_change_music_render.get("classification_counts", {}) if full_change_music_render else {},
                "versus_change_music_tail": {
                    "available": full_change_music_render_vs_tail is not None,
                    "improved_count": int(full_change_music_render_vs_tail.get("improved_count", 0)) if full_change_music_render_vs_tail else 0,
                    "unchanged_count": int(full_change_music_render_vs_tail.get("unchanged_count", 0)) if full_change_music_render_vs_tail else 0,
                    "worsened_count": int(full_change_music_render_vs_tail.get("worsened_count", 0)) if full_change_music_render_vs_tail else 0,
                },
                "versus_baseline": {
                    "available": full_change_music_render_vs_baseline is not None,
                    "improved_count": int(full_change_music_render_vs_baseline.get("improved_count", 0)) if full_change_music_render_vs_baseline else 0,
                    "unchanged_count": int(full_change_music_render_vs_baseline.get("unchanged_count", 0)) if full_change_music_render_vs_baseline else 0,
                    "worsened_count": int(full_change_music_render_vs_baseline.get("worsened_count", 0)) if full_change_music_render_vs_baseline else 0,
                },
            },
        },
        "current_ares_full_change_music_load_stub_summary": {
            "available": full_change_music_load_stub_smoke is not None,
            "job_count": int(full_change_music_load_stub_smoke.get("job_count", 0)) if full_change_music_load_stub_smoke else 0,
            "success_count": int(full_change_music_load_stub_smoke.get("success_count", 0)) if full_change_music_load_stub_smoke else 0,
            "command_read_count": int(full_change_music_load_stub_smoke.get("command_read_count", 0)) if full_change_music_load_stub_smoke else 0,
            "zero_ack_count": int(full_change_music_load_stub_smoke.get("zero_ack_count", 0)) if full_change_music_load_stub_smoke else 0,
            "key_on_count": int(full_change_music_load_stub_smoke.get("key_on_count", 0)) if full_change_music_load_stub_smoke else 0,
            "delivery_mode": "ares_wdc65816_full_change_music_load_stub_on_pc_062a",
            "routine": "rom_fixture_ChangeMusic_full_load_path_stubbed_loader",
            "call_shape": "C4:FBBD CHANGE_MUSIC body executes from ROM-derived bytes with A seeded to the requested one-based track id, MusicDatasetTable and MusicPackPointerTable reads served from ROM-derived fixtures, current pack variables left unsatisfied so real pack-decision branches run, LOAD_SPC700_DATA calls recorded and stubbed, and JSL C0:ABBD mapped to ROM-derived bytes.",
            "loader_metrics": {
                "available": full_change_music_load_stub_metrics is not None,
                "job_count": int(full_change_music_load_stub_metrics.get("job_count", 0)) if full_change_music_load_stub_metrics else 0,
                "mismatch_count": int(full_change_music_load_stub_metrics.get("mismatch_count", 0)) if full_change_music_load_stub_metrics else 0,
                "call_count_distribution": full_change_music_load_stub_metrics.get("call_count_distribution", {}) if full_change_music_load_stub_metrics else {},
            },
            "known_shortcuts": [
                "APU RAM seed is already built for the target track before the command is delivered.",
                "MusicDatasetTable and MusicPackPointerTable bytes are real ROM-derived fixture bytes, and pack-current state is intentionally unsatisfied so the pack-decision branches execute.",
                "LOAD_SPC700_DATA is an RTL stub that records A/X load-stream pointer arguments instead of streaming bytes to the APU.",
                "STOP_MUSIC, STOP_MUSIC_TRANSITION, and PLAY_SOUND_UNKNOWN0 remain RTL stubs if reached.",
                "The harness still times CPU delivery at the SMP $062A command-read boundary.",
            ],
            "render": {
                "available": full_change_music_load_stub_render is not None,
                "metric_count": int(full_change_music_load_stub_render.get("metrics_count", 0)) if full_change_music_load_stub_render else 0,
                "classification_counts": full_change_music_load_stub_render.get("classification_counts", {}) if full_change_music_load_stub_render else {},
                "versus_presatisfied_full_change_music": {
                    "available": full_change_music_load_stub_render_vs_presatisfied is not None,
                    "improved_count": int(full_change_music_load_stub_render_vs_presatisfied.get("improved_count", 0)) if full_change_music_load_stub_render_vs_presatisfied else 0,
                    "unchanged_count": int(full_change_music_load_stub_render_vs_presatisfied.get("unchanged_count", 0)) if full_change_music_load_stub_render_vs_presatisfied else 0,
                    "worsened_count": int(full_change_music_load_stub_render_vs_presatisfied.get("worsened_count", 0)) if full_change_music_load_stub_render_vs_presatisfied else 0,
                },
                "versus_baseline": {
                    "available": full_change_music_load_stub_render_vs_baseline is not None,
                    "improved_count": int(full_change_music_load_stub_render_vs_baseline.get("improved_count", 0)) if full_change_music_load_stub_render_vs_baseline else 0,
                    "unchanged_count": int(full_change_music_load_stub_render_vs_baseline.get("unchanged_count", 0)) if full_change_music_load_stub_render_vs_baseline else 0,
                    "worsened_count": int(full_change_music_load_stub_render_vs_baseline.get("worsened_count", 0)) if full_change_music_load_stub_render_vs_baseline else 0,
                },
            },
        },
        "current_ares_full_change_music_load_apply_summary": {
            "available": full_change_music_load_apply_smoke is not None,
            "job_count": int(full_change_music_load_apply_smoke.get("job_count", 0)) if full_change_music_load_apply_smoke else 0,
            "success_count": int(full_change_music_load_apply_smoke.get("success_count", 0)) if full_change_music_load_apply_smoke else 0,
            "command_read_count": int(full_change_music_load_apply_smoke.get("command_read_count", 0)) if full_change_music_load_apply_smoke else 0,
            "zero_ack_count": int(full_change_music_load_apply_smoke.get("zero_ack_count", 0)) if full_change_music_load_apply_smoke else 0,
            "key_on_count": int(full_change_music_load_apply_smoke.get("key_on_count", 0)) if full_change_music_load_apply_smoke else 0,
            "delivery_mode": "ares_wdc65816_full_change_music_load_apply_on_pc_062a",
            "routine": "rom_fixture_ChangeMusic_full_load_path_applied_loader",
            "call_shape": "C4:FBBD CHANGE_MUSIC body executes from ROM-derived bytes with bootstrap-only APU RAM, real pack-decision branches, ROM-derived MusicDatasetTable and MusicPackPointerTable fixtures, and LOAD_SPC700_DATA calls that apply selected payload streams into ares APU RAM before JSL C0:ABBD sends the track command.",
            "loader_metrics": {
                "available": full_change_music_load_apply_metrics is not None,
                "job_count": int(full_change_music_load_apply_metrics.get("job_count", 0)) if full_change_music_load_apply_metrics else 0,
                "mismatch_count": int(full_change_music_load_apply_metrics.get("mismatch_count", 0)) if full_change_music_load_apply_metrics else 0,
                "call_count_distribution": full_change_music_load_apply_metrics.get("call_count_distribution", {}) if full_change_music_load_apply_metrics else {},
            },
            "applied_stream_totals": {
                "streams": sum(int(((record.get("smoke", {}) or {}).get("cpu_instruction_probe", {}) or {}).get("load_spc700_data_applied_streams", 0)) for record in full_change_music_load_apply_smoke.get("records", [])) if full_change_music_load_apply_smoke else 0,
                "blocks": sum(int(((record.get("smoke", {}) or {}).get("cpu_instruction_probe", {}) or {}).get("load_spc700_data_applied_blocks", 0)) for record in full_change_music_load_apply_smoke.get("records", [])) if full_change_music_load_apply_smoke else 0,
                "bytes": sum(int(((record.get("smoke", {}) or {}).get("cpu_instruction_probe", {}) or {}).get("load_spc700_data_applied_bytes", 0)) for record in full_change_music_load_apply_smoke.get("records", [])) if full_change_music_load_apply_smoke else 0,
                "errors": sum(int(((record.get("smoke", {}) or {}).get("cpu_instruction_probe", {}) or {}).get("load_spc700_data_apply_errors", 0)) for record in full_change_music_load_apply_smoke.get("records", [])) if full_change_music_load_apply_smoke else 0,
            },
            "known_shortcuts": [
                "Bootstrap/common APU RAM seed is still prebuilt before the command is delivered.",
                "LOAD_SPC700_DATA applies payload streams semantically from ROM bytes instead of executing the real APUIO byte handshake.",
                "STOP_MUSIC, STOP_MUSIC_TRANSITION, and PLAY_SOUND_UNKNOWN0 remain RTL stubs if reached.",
                "The harness still times CPU delivery at the SMP $062A command-read boundary.",
            ],
            "render": {
                "available": full_change_music_load_apply_render is not None,
                "metric_count": int(full_change_music_load_apply_render.get("metrics_count", 0)) if full_change_music_load_apply_render else 0,
                "classification_counts": full_change_music_load_apply_render.get("classification_counts", {}) if full_change_music_load_apply_render else {},
                "versus_load_stub": {
                    "available": full_change_music_load_apply_render_vs_stub is not None,
                    "improved_count": int(full_change_music_load_apply_render_vs_stub.get("improved_count", 0)) if full_change_music_load_apply_render_vs_stub else 0,
                    "unchanged_count": int(full_change_music_load_apply_render_vs_stub.get("unchanged_count", 0)) if full_change_music_load_apply_render_vs_stub else 0,
                    "worsened_count": int(full_change_music_load_apply_render_vs_stub.get("worsened_count", 0)) if full_change_music_load_apply_render_vs_stub else 0,
                },
                "versus_baseline": {
                    "available": full_change_music_load_apply_render_vs_baseline is not None,
                    "improved_count": int(full_change_music_load_apply_render_vs_baseline.get("improved_count", 0)) if full_change_music_load_apply_render_vs_baseline else 0,
                    "unchanged_count": int(full_change_music_load_apply_render_vs_baseline.get("unchanged_count", 0)) if full_change_music_load_apply_render_vs_baseline else 0,
                    "worsened_count": int(full_change_music_load_apply_render_vs_baseline.get("worsened_count", 0)) if full_change_music_load_apply_render_vs_baseline else 0,
                },
            },
        },
        "replacement_target": [
            "Use the WDC65816-modeled CPU-side $2140 write of the one-based track id instead of diagnostic APUIO0 injection.",
            "Until full CPU scheduling is in place, use timed WDC65816 execution of the full ROM-derived CHANGE_MUSIC body with real pack-decision branches and semantic LOAD_SPC700_DATA stream application as the current bridge step.",
            "Next replace semantic LOAD_SPC700_DATA application with the real APUIO byte handshake before reaching the same command send.",
            "Preserve the APU driver's first command read at $062A/$F4.",
            "Preserve the driver's immediate $00 write to $F4 as the first APUIO0 acknowledgement after command read.",
            "Preserve key-on after command read across the representative corpus.",
            "Keep the no-command $055A/zero-key-on run as the negative control.",
        ],
        "evidence": [
            {
                **entry,
                "exists": path_exists(entry["path"]),
            }
            for entry in EVIDENCE
        ],
    }


def render_markdown(contract: dict[str, Any]) -> str:
    summary = contract["current_frontier_summary"]
    smp_summary = contract["current_ares_smp_smoke_summary"]
    smp_render = contract["current_ares_smp_render_summary"]
    cpu_writeapu = contract["current_ares_cpu_writeapu_summary"]
    wdc65816 = contract["current_ares_wdc65816_summary"]
    full_c0abbd = contract["current_ares_full_c0abbd_summary"]
    rom_c0abbd = contract["current_ares_rom_c0abbd_summary"]
    rom_c0abbd_jsl = contract["current_ares_rom_c0abbd_jsl_summary"]
    change_music_tail = contract["current_ares_change_music_tail_summary"]
    full_change_music = contract["current_ares_full_change_music_summary"]
    full_change_music_load_stub = contract["current_ares_full_change_music_load_stub_summary"]
    full_change_music_load_apply = contract["current_ares_full_change_music_load_apply_summary"]
    evidence_rows = [
        "| `{id}` | `{path}` | `{exists}` | {claim} |".format(
            id=item["id"],
            path=item["path"],
            exists="yes" if item["exists"] else "missing",
            claim=item["claim"],
        )
        for item in contract["evidence"]
    ]
    replacement_rows = [f"- {item}" for item in contract["replacement_target"]]
    cpu = contract["cpu_side_contract"]
    apu = contract["apu_side_diagnostic_contract"]
    ares = contract["ares_bridge_contract"]
    return "\n".join(
        [
            "# Audio CPU/APU Mailbox Contract",
            "",
            "Status: diagnostic track-command mailbox transcript pinned; ROM-derived full CHANGE_MUSIC pre-satisfied-pack bridge implemented; full scheduled CPU/APU handshake still pending.",
            "",
            "This contract ties the CPU-side EarthBound source entry points to the APU-side command transcript observed in the ares diagnostic harness. It is the target for replacing timed command delivery with scheduled execution of the real C0 track-command sender.",
            "",
            "## CPU Side",
            "",
            f"- send entry: `{cpu['send_track_command_entry']}` / `{cpu['send_track_command_name']}`",
            f"- send register: `{cpu['send_track_command_register']}`",
            f"- send opcode: `{cpu['send_track_command_opcode']}`",
            f"- send ROM bytes: `{cpu['send_track_command_rom_bytes']}`",
            f"- send width: `{cpu['send_track_command_width']}`",
            f"- command value: `{cpu['track_command_value']}`",
            f"- ack read entry: `{cpu['read_ack_entry']}` / `{cpu['read_ack_name']}`",
            f"- ack read register: `{cpu['read_ack_register']}`",
            f"- stop-music ack value: `{cpu['stop_music_ack_value']}`",
            "",
            "## APU Side Target",
            "",
            f"- first command read: `{apu['driver_first_command_read_pc']}` from `{apu['driver_first_command_read_address']}`",
            f"- first ack write: `{apu['driver_first_ack_write_pc']}` to `{apu['driver_first_ack_write_address']}` with `{apu['driver_first_ack_write_data']}`",
            f"- key-on must follow command read: `{apu['keyon_must_follow_command_read']}`",
            f"- diagnostic mode pinned by frontier: `{apu['diagnostic_mode']}`",
            "",
            "## ares Bridge",
            "",
            f"- CPU to APU: `{ares['cpu_to_apu_entrypoint']}`",
            f"- APU to CPU: `{ares['apu_to_cpu_entrypoint']}`",
            f"- SMP reads CPU mailbox: `{ares['smp_reads_cpu_mailbox']}`",
            f"- SMP writes APU mailbox: `{ares['smp_writes_apu_mailbox']}`",
            f"- implication: {ares['full_fidelity_implication']}",
            "",
            "## Current Frontier",
            "",
            f"- available: `{summary['available']}`",
            f"- captures: `{summary['capture_count']} / {summary['job_count']}`",
            f"- modes: `{summary['mode_counts']}`",
            f"- command reads: `{summary['command_read_count']}`",
            f"- commands matching track id: `{summary['command_match_count']}`",
            f"- zero ack writes: `{summary['zero_ack_write_count']}`",
            f"- key-on after command read: `{summary['keyon_after_command_read_count']}`",
            f"- first read PCs: `{summary['first_read_pc_counts']}`",
            f"- first ack PCs: `{summary['first_ack_pc_counts']}`",
            "",
            "## ares SMP Smoke",
            "",
            f"- available: `{smp_summary['available']}`",
            f"- successes: `{smp_summary['success_count']} / {smp_summary['job_count']}`",
            f"- command reads: `{smp_summary['command_read_count']}`",
            f"- zero ack writes: `{smp_summary['zero_ack_count']}`",
            f"- key-on after timed portWrite: `{smp_summary['key_on_count']}`",
            f"- delivery mode: `{smp_summary['delivery_mode']}`",
            "",
            "## ares SMP Snapshot Rendering",
            "",
            f"- available: `{smp_render['available']}`",
            f"- rendered metrics: `{smp_render['metric_count']}`",
            f"- render classes: `{smp_render['classification_counts']}`",
            f"- versus custom last-key-on: `{smp_render['versus_custom_last_keyon']}`",
            f"- versus baseline diagnostic snapshots: `{smp_render['versus_baseline']}`",
            "",
            "## ares CPU writeAPU Bridge",
            "",
            f"- available: `{cpu_writeapu['available']}`",
            f"- successes: `{cpu_writeapu['success_count']} / {cpu_writeapu['job_count']}`",
            f"- command reads: `{cpu_writeapu['command_read_count']}`",
            f"- zero ack writes: `{cpu_writeapu['zero_ack_count']}`",
            f"- key-on after timed CPU writeAPU: `{cpu_writeapu['key_on_count']}`",
            f"- delivery mode: `{cpu_writeapu['delivery_mode']}`",
            f"- render classes: `{cpu_writeapu['render']['classification_counts']}`",
            f"- versus direct SMP portWrite: `{cpu_writeapu['render']['versus_smp_portwrite']}`",
            f"- versus baseline diagnostic snapshots: `{cpu_writeapu['render']['versus_baseline']}`",
            "",
            "## WDC65816 STA $2140 Bridge",
            "",
            f"- available: `{wdc65816['available']}`",
            f"- successes: `{wdc65816['success_count']} / {wdc65816['job_count']}`",
            f"- command reads: `{wdc65816['command_read_count']}`",
            f"- zero ack writes: `{wdc65816['zero_ack_count']}`",
            f"- key-on after modeled WDC65816 STA: `{wdc65816['key_on_count']}`",
            f"- delivery mode: `{wdc65816['delivery_mode']}`",
            f"- modeled routine: `{wdc65816['routine']}`",
            f"- render classes: `{wdc65816['render']['classification_counts']}`",
            f"- versus CPU writeAPU: `{wdc65816['render']['versus_cpu_writeapu']}`",
            f"- versus baseline diagnostic snapshots: `{wdc65816['render']['versus_baseline']}`",
            "",
            "## Full C0:ABBD Bridge",
            "",
            f"- available: `{full_c0abbd['available']}`",
            f"- successes: `{full_c0abbd['success_count']} / {full_c0abbd['job_count']}`",
            f"- command reads: `{full_c0abbd['command_read_count']}`",
            f"- zero ack writes: `{full_c0abbd['zero_ack_count']}`",
            f"- key-on after modeled C0:ABBD: `{full_c0abbd['key_on_count']}`",
            f"- delivery mode: `{full_c0abbd['delivery_mode']}`",
            f"- modeled routine: `{full_c0abbd['routine']}`",
            f"- render classes: `{full_c0abbd['render']['classification_counts']}`",
            f"- versus WDC65816 STA $2140: `{full_c0abbd['render']['versus_sta2140']}`",
            f"- versus baseline diagnostic snapshots: `{full_c0abbd['render']['versus_baseline']}`",
            "",
            "## ROM-Derived C0:ABBD Bridge",
            "",
            f"- fixture manifest available: `{rom_c0abbd['fixture_manifest_available']}`",
            f"- fixtures: `{rom_c0abbd['fixture_count']}`",
            f"- available: `{rom_c0abbd['available']}`",
            f"- successes: `{rom_c0abbd['success_count']} / {rom_c0abbd['job_count']}`",
            f"- command reads: `{rom_c0abbd['command_read_count']}`",
            f"- zero ack writes: `{rom_c0abbd['zero_ack_count']}`",
            f"- key-on after ROM-derived C0:ABBD: `{rom_c0abbd['key_on_count']}`",
            f"- delivery mode: `{rom_c0abbd['delivery_mode']}`",
            f"- routine: `{rom_c0abbd['routine']}`",
            f"- render classes: `{rom_c0abbd['render']['classification_counts']}`",
            f"- versus modeled full C0:ABBD: `{rom_c0abbd['render']['versus_modeled_full_c0abbd']}`",
            f"- versus baseline diagnostic snapshots: `{rom_c0abbd['render']['versus_baseline']}`",
            "",
            "## ROM-Derived C0:ABBD JSL Call Bridge",
            "",
            f"- available: `{rom_c0abbd_jsl['available']}`",
            f"- successes: `{rom_c0abbd_jsl['success_count']} / {rom_c0abbd_jsl['job_count']}`",
            f"- command reads: `{rom_c0abbd_jsl['command_read_count']}`",
            f"- zero ack writes: `{rom_c0abbd_jsl['zero_ack_count']}`",
            f"- key-on after ROM-derived C0:ABBD JSL call: `{rom_c0abbd_jsl['key_on_count']}`",
            f"- delivery mode: `{rom_c0abbd_jsl['delivery_mode']}`",
            f"- routine: `{rom_c0abbd_jsl['routine']}`",
            f"- call shape: `{rom_c0abbd_jsl['call_shape']}`",
            f"- render classes: `{rom_c0abbd_jsl['render']['classification_counts']}`",
            f"- versus direct ROM-derived C0:ABBD: `{rom_c0abbd_jsl['render']['versus_direct_rom_c0abbd']}`",
            f"- versus baseline diagnostic snapshots: `{rom_c0abbd_jsl['render']['versus_baseline']}`",
            "",
            "## CHANGE_MUSIC Tail Bridge",
            "",
            f"- available: `{change_music_tail['available']}`",
            f"- successes: `{change_music_tail['success_count']} / {change_music_tail['job_count']}`",
            f"- command reads: `{change_music_tail['command_read_count']}`",
            f"- zero ack writes: `{change_music_tail['zero_ack_count']}`",
            f"- key-on after CHANGE_MUSIC tail: `{change_music_tail['key_on_count']}`",
            f"- delivery mode: `{change_music_tail['delivery_mode']}`",
            f"- routine: `{change_music_tail['routine']}`",
            f"- tail bytes: `{change_music_tail['tail_bytes']}`",
            f"- call shape: `{change_music_tail['call_shape']}`",
            f"- render classes: `{change_music_tail['render']['classification_counts']}`",
            f"- versus ROM-derived C0:ABBD JSL call: `{change_music_tail['render']['versus_rom_c0abbd_jsl']}`",
            f"- versus baseline diagnostic snapshots: `{change_music_tail['render']['versus_baseline']}`",
            "",
            "## Full CHANGE_MUSIC Bridge",
            "",
            f"- available: `{full_change_music['available']}`",
            f"- successes: `{full_change_music['success_count']} / {full_change_music['job_count']}`",
            f"- command reads: `{full_change_music['command_read_count']}`",
            f"- zero ack writes: `{full_change_music['zero_ack_count']}`",
            f"- key-on after full CHANGE_MUSIC: `{full_change_music['key_on_count']}`",
            f"- delivery mode: `{full_change_music['delivery_mode']}`",
            f"- routine: `{full_change_music['routine']}`",
            f"- call shape: `{full_change_music['call_shape']}`",
            f"- known shortcuts: `{full_change_music['known_shortcuts']}`",
            f"- render classes: `{full_change_music['render']['classification_counts']}`",
            f"- versus CHANGE_MUSIC tail: `{full_change_music['render']['versus_change_music_tail']}`",
            f"- versus baseline diagnostic snapshots: `{full_change_music['render']['versus_baseline']}`",
            "",
            "## Full CHANGE_MUSIC Load-Path Stub Bridge",
            "",
            f"- available: `{full_change_music_load_stub['available']}`",
            f"- successes: `{full_change_music_load_stub['success_count']} / {full_change_music_load_stub['job_count']}`",
            f"- command reads: `{full_change_music_load_stub['command_read_count']}`",
            f"- zero ack writes: `{full_change_music_load_stub['zero_ack_count']}`",
            f"- key-on after full CHANGE_MUSIC load path: `{full_change_music_load_stub['key_on_count']}`",
            f"- delivery mode: `{full_change_music_load_stub['delivery_mode']}`",
            f"- routine: `{full_change_music_load_stub['routine']}`",
            f"- call shape: `{full_change_music_load_stub['call_shape']}`",
            f"- loader metrics: `{full_change_music_load_stub['loader_metrics']}`",
            f"- known shortcuts: `{full_change_music_load_stub['known_shortcuts']}`",
            f"- render classes: `{full_change_music_load_stub['render']['classification_counts']}`",
            f"- versus pre-satisfied full CHANGE_MUSIC: `{full_change_music_load_stub['render']['versus_presatisfied_full_change_music']}`",
            f"- versus baseline diagnostic snapshots: `{full_change_music_load_stub['render']['versus_baseline']}`",
            "",
            "## Full CHANGE_MUSIC Load-Apply Bridge",
            "",
            f"- available: `{full_change_music_load_apply['available']}`",
            f"- successes: `{full_change_music_load_apply['success_count']} / {full_change_music_load_apply['job_count']}`",
            f"- command reads: `{full_change_music_load_apply['command_read_count']}`",
            f"- zero ack writes: `{full_change_music_load_apply['zero_ack_count']}`",
            f"- key-on after full CHANGE_MUSIC load apply: `{full_change_music_load_apply['key_on_count']}`",
            f"- delivery mode: `{full_change_music_load_apply['delivery_mode']}`",
            f"- routine: `{full_change_music_load_apply['routine']}`",
            f"- call shape: `{full_change_music_load_apply['call_shape']}`",
            f"- loader metrics: `{full_change_music_load_apply['loader_metrics']}`",
            f"- applied stream totals: `{full_change_music_load_apply['applied_stream_totals']}`",
            f"- known shortcuts: `{full_change_music_load_apply['known_shortcuts']}`",
            f"- render classes: `{full_change_music_load_apply['render']['classification_counts']}`",
            f"- versus load-stub full CHANGE_MUSIC: `{full_change_music_load_apply['render']['versus_load_stub']}`",
            f"- versus baseline diagnostic snapshots: `{full_change_music_load_apply['render']['versus_baseline']}`",
            "",
            "## Replacement Target",
            "",
            *replacement_rows,
            "",
            "## Evidence",
            "",
            "| Evidence | Path | Exists | Claim |",
            "| --- | --- | --- | --- |",
            *evidence_rows,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    frontier_path = Path(args.frontier)
    smp_smoke_path = Path(args.smp_smoke)
    smp_render_path = Path(args.smp_render)
    cpu_writeapu_smoke_path = Path(args.cpu_writeapu_smoke)
    cpu_writeapu_render_path = Path(args.cpu_writeapu_render)
    wdc65816_smoke_path = Path(args.wdc65816_smoke)
    wdc65816_render_path = Path(args.wdc65816_render)
    full_c0abbd_smoke_path = Path(args.full_c0abbd_smoke)
    full_c0abbd_render_path = Path(args.full_c0abbd_render)
    cpu_routine_fixtures_path = Path(args.cpu_routine_fixtures)
    rom_c0abbd_smoke_path = Path(args.rom_c0abbd_smoke)
    rom_c0abbd_render_path = Path(args.rom_c0abbd_render)
    rom_c0abbd_jsl_smoke_path = Path(args.rom_c0abbd_jsl_smoke)
    rom_c0abbd_jsl_render_path = Path(args.rom_c0abbd_jsl_render)
    change_music_tail_smoke_path = Path(args.change_music_tail_smoke)
    change_music_tail_render_path = Path(args.change_music_tail_render)
    full_change_music_smoke_path = Path(args.full_change_music_smoke)
    full_change_music_render_path = Path(args.full_change_music_render)
    full_change_music_load_stub_smoke_path = Path(args.full_change_music_load_stub_smoke)
    full_change_music_load_stub_metrics_path = Path(args.full_change_music_load_stub_metrics)
    full_change_music_load_stub_render_path = Path(args.full_change_music_load_stub_render)
    full_change_music_load_apply_smoke_path = Path(args.full_change_music_load_apply_smoke)
    full_change_music_load_apply_metrics_path = Path(args.full_change_music_load_apply_metrics)
    full_change_music_load_apply_render_path = Path(args.full_change_music_load_apply_render)
    frontier = load_json_if_exists(frontier_path)
    smp_smoke = load_json_if_exists(smp_smoke_path)
    smp_render = load_json_if_exists(smp_render_path)
    smp_render_vs_last_keyon = load_json_if_exists(Path(args.smp_render_vs_last_keyon))
    smp_render_vs_baseline = load_json_if_exists(Path(args.smp_render_vs_baseline))
    cpu_writeapu_smoke = load_json_if_exists(cpu_writeapu_smoke_path)
    cpu_writeapu_render = load_json_if_exists(cpu_writeapu_render_path)
    cpu_writeapu_render_vs_smp = load_json_if_exists(Path(args.cpu_writeapu_render_vs_smp))
    cpu_writeapu_render_vs_baseline = load_json_if_exists(Path(args.cpu_writeapu_render_vs_baseline))
    wdc65816_smoke = load_json_if_exists(wdc65816_smoke_path)
    wdc65816_render = load_json_if_exists(wdc65816_render_path)
    wdc65816_render_vs_cpu_writeapu = load_json_if_exists(Path(args.wdc65816_render_vs_cpu_writeapu))
    wdc65816_render_vs_baseline = load_json_if_exists(Path(args.wdc65816_render_vs_baseline))
    full_c0abbd_smoke = load_json_if_exists(full_c0abbd_smoke_path)
    full_c0abbd_render = load_json_if_exists(full_c0abbd_render_path)
    full_c0abbd_render_vs_sta2140 = load_json_if_exists(Path(args.full_c0abbd_render_vs_sta2140))
    full_c0abbd_render_vs_baseline = load_json_if_exists(Path(args.full_c0abbd_render_vs_baseline))
    cpu_routine_fixtures = load_json_if_exists(cpu_routine_fixtures_path)
    rom_c0abbd_smoke = load_json_if_exists(rom_c0abbd_smoke_path)
    rom_c0abbd_render = load_json_if_exists(rom_c0abbd_render_path)
    rom_c0abbd_render_vs_modeled = load_json_if_exists(Path(args.rom_c0abbd_render_vs_modeled))
    rom_c0abbd_render_vs_baseline = load_json_if_exists(Path(args.rom_c0abbd_render_vs_baseline))
    rom_c0abbd_jsl_smoke = load_json_if_exists(rom_c0abbd_jsl_smoke_path)
    rom_c0abbd_jsl_render = load_json_if_exists(rom_c0abbd_jsl_render_path)
    rom_c0abbd_jsl_render_vs_direct = load_json_if_exists(Path(args.rom_c0abbd_jsl_render_vs_direct))
    rom_c0abbd_jsl_render_vs_baseline = load_json_if_exists(Path(args.rom_c0abbd_jsl_render_vs_baseline))
    change_music_tail_smoke = load_json_if_exists(change_music_tail_smoke_path)
    change_music_tail_render = load_json_if_exists(change_music_tail_render_path)
    change_music_tail_render_vs_c0abbd_jsl = load_json_if_exists(Path(args.change_music_tail_render_vs_c0abbd_jsl))
    change_music_tail_render_vs_baseline = load_json_if_exists(Path(args.change_music_tail_render_vs_baseline))
    full_change_music_smoke = load_json_if_exists(full_change_music_smoke_path)
    full_change_music_render = load_json_if_exists(full_change_music_render_path)
    full_change_music_render_vs_tail = load_json_if_exists(Path(args.full_change_music_render_vs_tail))
    full_change_music_render_vs_baseline = load_json_if_exists(Path(args.full_change_music_render_vs_baseline))
    full_change_music_load_stub_smoke = load_json_if_exists(full_change_music_load_stub_smoke_path)
    full_change_music_load_stub_metrics = load_json_if_exists(full_change_music_load_stub_metrics_path)
    full_change_music_load_stub_render = load_json_if_exists(full_change_music_load_stub_render_path)
    full_change_music_load_stub_render_vs_presatisfied = load_json_if_exists(Path(args.full_change_music_load_stub_render_vs_presatisfied))
    full_change_music_load_stub_render_vs_baseline = load_json_if_exists(Path(args.full_change_music_load_stub_render_vs_baseline))
    full_change_music_load_apply_smoke = load_json_if_exists(full_change_music_load_apply_smoke_path)
    full_change_music_load_apply_metrics = load_json_if_exists(full_change_music_load_apply_metrics_path)
    full_change_music_load_apply_render = load_json_if_exists(full_change_music_load_apply_render_path)
    full_change_music_load_apply_render_vs_stub = load_json_if_exists(Path(args.full_change_music_load_apply_render_vs_stub))
    full_change_music_load_apply_render_vs_baseline = load_json_if_exists(Path(args.full_change_music_load_apply_render_vs_baseline))
    contract = build_contract(
        frontier,
        frontier_path,
        smp_smoke,
        smp_smoke_path,
        smp_render,
        smp_render_path,
        smp_render_vs_last_keyon,
        smp_render_vs_baseline,
        cpu_writeapu_smoke,
        cpu_writeapu_smoke_path,
        cpu_writeapu_render,
        cpu_writeapu_render_path,
        cpu_writeapu_render_vs_smp,
        cpu_writeapu_render_vs_baseline,
        wdc65816_smoke,
        wdc65816_smoke_path,
        wdc65816_render,
        wdc65816_render_path,
        wdc65816_render_vs_cpu_writeapu,
        wdc65816_render_vs_baseline,
        full_c0abbd_smoke,
        full_c0abbd_smoke_path,
        full_c0abbd_render,
        full_c0abbd_render_path,
        full_c0abbd_render_vs_sta2140,
        full_c0abbd_render_vs_baseline,
        cpu_routine_fixtures,
        cpu_routine_fixtures_path,
        rom_c0abbd_smoke,
        rom_c0abbd_smoke_path,
        rom_c0abbd_render,
        rom_c0abbd_render_path,
        rom_c0abbd_render_vs_modeled,
        rom_c0abbd_render_vs_baseline,
        rom_c0abbd_jsl_smoke,
        rom_c0abbd_jsl_smoke_path,
        rom_c0abbd_jsl_render,
        rom_c0abbd_jsl_render_path,
        rom_c0abbd_jsl_render_vs_direct,
        rom_c0abbd_jsl_render_vs_baseline,
        change_music_tail_smoke,
        change_music_tail_smoke_path,
        change_music_tail_render,
        change_music_tail_render_path,
        change_music_tail_render_vs_c0abbd_jsl,
        change_music_tail_render_vs_baseline,
        full_change_music_smoke,
        full_change_music_smoke_path,
        full_change_music_render,
        full_change_music_render_path,
        full_change_music_render_vs_tail,
        full_change_music_render_vs_baseline,
        full_change_music_load_stub_smoke,
        full_change_music_load_stub_smoke_path,
        full_change_music_load_stub_metrics,
        full_change_music_load_stub_metrics_path,
        full_change_music_load_stub_render,
        full_change_music_load_stub_render_path,
        full_change_music_load_stub_render_vs_presatisfied,
        full_change_music_load_stub_render_vs_baseline,
        full_change_music_load_apply_smoke,
        full_change_music_load_apply_smoke_path,
        full_change_music_load_apply_metrics,
        full_change_music_load_apply_metrics_path,
        full_change_music_load_apply_render,
        full_change_music_load_apply_render_path,
        full_change_music_load_apply_render_vs_stub,
        full_change_music_load_apply_render_vs_baseline,
    )
    json_path = Path(args.json)
    markdown_path = Path(args.markdown)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(contract), encoding="utf-8")
    print(f"Built audio CPU/APU mailbox contract -> {json_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
