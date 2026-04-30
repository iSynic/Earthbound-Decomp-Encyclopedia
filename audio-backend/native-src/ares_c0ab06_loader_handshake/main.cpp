#include <sfc/sfc.hpp>

#include <array>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

namespace fs = std::filesystem;

std::vector<std::uint8_t> readBytes(const fs::path& path) {
  std::ifstream in(path, std::ios::binary);
  if (!in) throw std::runtime_error("could not open " + path.string());
  return std::vector<std::uint8_t>((std::istreambuf_iterator<char>(in)), std::istreambuf_iterator<char>());
}

void writeBytes(const fs::path& path, const std::uint8_t* data, std::size_t size) {
  fs::create_directories(path.parent_path());
  std::ofstream out(path, std::ios::binary);
  if (!out) throw std::runtime_error("could not write " + path.string());
  out.write(reinterpret_cast<const char*>(data), static_cast<std::streamsize>(size));
}

fs::path argPath(int argc, char** argv, const std::string& name) {
  for (int i = 1; i + 1 < argc; ++i) {
    if (argv[i] == name) return fs::path(argv[i + 1]);
  }
  return {};
}

int argInt(int argc, char** argv, const std::string& name, int fallback) {
  for (int i = 1; i + 1 < argc; ++i) {
    if (argv[i] == name) return std::stoi(argv[i + 1], nullptr, 0);
  }
  return fallback;
}

std::string argString(int argc, char** argv, const std::string& name, const std::string& fallback) {
  for (int i = 1; i + 1 < argc; ++i) {
    if (argv[i] == name) return argv[i + 1];
  }
  return fallback;
}

std::vector<std::pair<std::uint8_t, std::uint16_t>> parseSequence(const std::string& text) {
  std::vector<std::pair<std::uint8_t, std::uint16_t>> sequence;
  std::size_t cursor = 0;
  while (cursor < text.size()) {
    const std::size_t separator = text.find_first_of(":=", cursor);
    if (separator == std::string::npos) throw std::runtime_error("invalid --sequence entry; expected BANK:ADDR");
    const std::size_t end = text.find_first_of(",;", separator + 1);
    const std::string bankText = text.substr(cursor, separator - cursor);
    const std::string addressText = text.substr(separator + 1, (end == std::string::npos ? text.size() : end) - separator - 1);
    const int bank = std::stoi(bankText, nullptr, 0);
    const int address = std::stoi(addressText, nullptr, 0);
    if (bank < 0 || bank > 0xff || address < 0 || address > 0xffff) throw std::runtime_error("invalid --sequence bank/address");
    sequence.push_back({static_cast<std::uint8_t>(bank), static_cast<std::uint16_t>(address)});
    if (end == std::string::npos) break;
    cursor = end + 1;
  }
  return sequence;
}

bool hasFlag(int argc, char** argv, const std::string& name) {
  for (int i = 1; i < argc; ++i) {
    if (argv[i] == name) return true;
  }
  return false;
}

std::string hexByte(std::uint8_t value) {
  std::ostringstream out;
  out << "0x" << std::hex << std::uppercase << std::setw(2) << std::setfill('0') << static_cast<unsigned>(value);
  return out.str();
}

std::string hexWord(std::uint16_t value) {
  std::ostringstream out;
  out << "0x" << std::hex << std::uppercase << std::setw(4) << std::setfill('0') << static_cast<unsigned>(value);
  return out.str();
}

std::string hexLong(std::uint32_t value) {
  std::ostringstream out;
  out << "0x" << std::hex << std::uppercase << std::setw(6) << std::setfill('0') << value;
  return out.str();
}

struct C0AB06LoaderProbe : ares::WDC65816 {
  std::vector<std::uint8_t> loaderBytes;
  std::vector<std::uint8_t> romBytes;
  std::unordered_map<std::uint32_t, std::uint8_t> memory;
  std::array<std::uint8_t, 0x10000> apuRam{};
  std::array<std::uint8_t, 4> apuio{0xaa, 0xbb, 0x00, 0x00};
  std::uint8_t streamBank = 0;
  std::uint16_t streamAddress = 0;
  std::uint16_t currentDestination = 0;
  std::uint32_t currentPayloadOffset = 0;
  bool pendingPort0 = false;
  bool terminalZeroArmed = false;
  std::uint8_t pendingPort0Value = 0;
  std::uint8_t blockMode = 0;
  int instructionCount = 0;
  int payloadWrites = 0;
  int payloadBytes = 0;
  int blockStartTokens = 0;
  int terminalTokens = 0;
  int apuioReads = 0;
  int apuioWrites = 0;
  int smpInstructions = 0;
  int smpPrebootInstructions = 0;
  bool useRealSmpIplReceiver = false;
  bool smpBootSignatureObserved = false;
  std::uint16_t smpFinalPc = 0;
  std::uint32_t finalPc = 0;
  int bootstrapInstructionCount = 0;
  int bootstrapSmpInstructions = 0;
  int bootstrapPayloadBytes = 0;
  bool bootstrapOk = false;
  bool runFullChangeMusic = false;
  bool insideLoadSpc700DataCall = false;
  std::uint8_t trackCommand = 0;
  int changeMusicInstructionCount = 0;
  int changeMusicLoadCalls = 0;
  int commandWrites = 0;
  int commandWriteSmpBurst = 0;
  int commandReadStep = -1;
  int zeroAckStep = -1;
  int keyOnStep = -1;
  std::uint8_t keyOnData = 0;
  bool reachedCommandRead = false;
  bool reachedZeroAck = false;
  bool reachedKeyOn = false;
  std::uint16_t lastKeyOnPc = 0;
  std::uint16_t lastKeyOnYa = 0;
  std::uint8_t lastKeyOnX = 0;
  std::uint8_t lastKeyOnS = 0;
  std::uint8_t lastKeyOnP = 0;
  std::vector<std::uint8_t> lastKeyOnSnapshot;
  std::uint32_t changeMusicFinalPc = 0;
  struct ChangeMusicLoadStep {
    std::uint8_t bank = 0;
    std::uint16_t address = 0;
    int payloadBytes = 0;
    int blockStartTokens = 0;
    int terminalTokens = 0;
  };
  std::vector<ChangeMusicLoadStep> changeMusicLoadSteps;
  struct SequenceStep {
    std::uint8_t bank = 0;
    std::uint16_t address = 0;
    bool ok = false;
    int instructionCount = 0;
    int payloadBytes = 0;
    int blockStartTokens = 0;
    int terminalTokens = 0;
    std::uint32_t finalPc = 0;
    std::uint16_t smpFinalPc = 0;
  };
  std::vector<SequenceStep> sequenceSteps;

  static constexpr std::uint32_t loaderBase = 0xC0AB06;
  static constexpr std::uint32_t loaderEnd = 0xC0ABA8;
  static constexpr std::uint32_t commandSenderBase = 0xC0ABBD;
  static constexpr std::uint32_t stopMusicBase = 0xC0ABC6;
  static constexpr std::uint32_t playSoundUnknownBase = 0xC0AC01;
  static constexpr std::uint32_t stopMusicTransitionBase = 0xC0AC0C;
  static constexpr std::uint32_t changeMusicBase = 0xC4FBBD;
  static constexpr std::uint32_t musicDatasetTableBase = 0xC4F70A;

  static auto hiromOffset(std::uint8_t bank, std::uint16_t address) -> std::size_t {
    if (bank < 0xC0) throw std::runtime_error("expected canonical HiROM bank");
    return static_cast<std::size_t>(bank - 0xC0) * 0x10000u + address;
  }

  auto idle() -> void override {}
  auto stepSmp(int count = 16) -> void {
    if (!useRealSmpIplReceiver) return;
    for (int index = 0; index < count; ++index) {
      ares::SuperFamicom::smp.instruction();
      ++smpInstructions;
    }
    smpFinalPc = static_cast<std::uint16_t>(ares::SuperFamicom::smp.r.pc.w);
  }

  auto lastCycle() -> void override {}
  auto interruptPending() const -> bool override { return false; }
  auto synchronizing() const -> bool override { return false; }

  auto streamRead(std::uint32_t rawAddress) const -> std::uint8_t {
    const std::uint8_t bank = static_cast<std::uint8_t>(rawAddress >> 16);
    const std::uint16_t address = static_cast<std::uint16_t>(rawAddress & 0xffff);
    const std::size_t offset = hiromOffset(bank, address);
    if (offset >= romBytes.size()) return 0xff;
    return romBytes[offset];
  }

  auto read(n24 address) -> n8 override {
    const std::uint32_t rawAddress = static_cast<std::uint32_t>(address);
    if (runFullChangeMusic && rawAddress == loaderBase) {
      if (!insideLoadSpc700DataCall) {
        insideLoadSpc700DataCall = true;
        ++changeMusicLoadCalls;
        changeMusicLoadSteps.push_back({
          static_cast<std::uint8_t>(r.x.w & 0xff),
          static_cast<std::uint16_t>(r.a.w),
          0,
          0,
          0,
        });
      }
    }
    if (runFullChangeMusic && (
      rawAddress == stopMusicBase ||
      rawAddress == playSoundUnknownBase ||
      rawAddress == stopMusicTransitionBase
    )) {
      return 0x6b; // RTL helper stub; the isolated harness pre-satisfies unrelated side effects.
    }
    if (auto found = memory.find(rawAddress); found != memory.end()) return found->second;
    if (rawAddress >= loaderBase && rawAddress < loaderBase + loaderBytes.size()) {
      return loaderBytes[rawAddress - loaderBase];
    }
    if ((rawAddress >> 16) >= 0xC0) {
      return streamRead(rawAddress);
    }
    if (runFullChangeMusic) {
      if (rawAddress == 0x00b4b6 || rawAddress == 0x00b4b7) return 0x01; // CreditsPlaybackActive: skip unrelated PLAY_SOUND helper.
      if (rawAddress == 0x00b53b) return 0x00; // CurrentMusicTrack low: force change path.
      if (rawAddress == 0x00b53c) return 0x00;
      if (rawAddress >= 0x00b53d && rawAddress <= 0x00b548) return 0xff; // Current pack variables intentionally unsatisfied.
    }
    if (rawAddress >= 0x002140 && rawAddress <= 0x002143) {
      ++apuioReads;
      const unsigned port = rawAddress - 0x002140;
      if (useRealSmpIplReceiver) {
        stepSmp();
        return ares::SuperFamicom::smp.portRead(port);
      }
      if (port == 0 && pendingPort0) {
        pendingPort0 = false;
        apuio[0] = pendingPort0Value;
        if (blockMode == 0) terminalZeroArmed = true;
        return apuio[0];
      }
      if (port == 0 && terminalZeroArmed) {
        apuio[0] = 0x00;
        apuio[1] = 0x00;
      }
      return apuio[port];
    }
    return 0x00;
  }

  auto write(n24 address, n8 data) -> void override {
    const std::uint32_t rawAddress = static_cast<std::uint32_t>(address);
    const std::uint8_t byte = static_cast<std::uint8_t>(data);
    if (rawAddress >= 0x002140 && rawAddress <= 0x002143) {
      ++apuioWrites;
      const unsigned port = rawAddress - 0x002140;
      if (useRealSmpIplReceiver) {
        if (runFullChangeMusic && !insideLoadSpc700DataCall && port == 0) {
          ++commandWrites;
          ares::SuperFamicom::smp.portWrite(port, byte);
          stepSmp(commandWriteSmpBurst);
          return;
        }
        if (port == 1 && pendingPort0) {
          ++payloadWrites;
          ++payloadBytes;
          if (!changeMusicLoadSteps.empty()) ++changeMusicLoadSteps.back().payloadBytes;
          ares::SuperFamicom::smp.portWrite(port, byte);
          pendingPort0 = false;
          stepSmp(24);
          return;
        } else if (port == 0) {
          pendingPort0 = true;
          pendingPort0Value = byte;
          ares::SuperFamicom::smp.portWrite(port, byte);
          return;
        } else if (port == 1) {
          blockMode = byte;
          if (blockMode == 0) {
            ++terminalTokens;
            if (!changeMusicLoadSteps.empty()) ++changeMusicLoadSteps.back().terminalTokens;
          } else {
            ++blockStartTokens;
            if (!changeMusicLoadSteps.empty()) ++changeMusicLoadSteps.back().blockStartTokens;
          }
          ares::SuperFamicom::smp.portWrite(port, byte);
          return;
        }
        ares::SuperFamicom::smp.portWrite(port, byte);
        return;
      }
      if (port == 0) {
        pendingPort0 = true;
        pendingPort0Value = byte;
        apuio[0] = byte;
        return;
      }
      if (port == 1 && pendingPort0) {
        const std::uint32_t target = static_cast<std::uint32_t>(currentDestination) + currentPayloadOffset;
        if (target < apuRam.size()) apuRam[target] = byte;
        ++currentPayloadOffset;
        ++payloadWrites;
        ++payloadBytes;
        apuio[0] = pendingPort0Value;
        apuio[1] = byte;
        pendingPort0 = false;
        return;
      }
      if (port == 1) {
        blockMode = byte;
        if (blockMode == 0) ++terminalTokens;
        else ++blockStartTokens;
        apuio[1] = byte;
        return;
      }
      if (port == 2) {
        currentDestination = static_cast<std::uint16_t>((currentDestination & 0xff00) | byte);
        currentPayloadOffset = 0;
        apuio[2] = byte;
        return;
      }
      if (port == 3) {
        currentDestination = static_cast<std::uint16_t>((currentDestination & 0x00ff) | (byte << 8));
        apuio[3] = byte;
        return;
      }
    }
    memory[rawAddress] = byte;
  }

  auto bootRealSmpIpl(const std::vector<std::uint8_t>& iplrom, int maxPrebootInstructions, bool clearApuRam) -> void {
    if (iplrom.size() != 64) throw std::runtime_error("SFC IPL ROM must be exactly 64 bytes");
    std::copy(iplrom.begin(), iplrom.end(), ares::SuperFamicom::smp.iplrom);
    if (clearApuRam) std::fill(ares::SuperFamicom::dsp.apuram, ares::SuperFamicom::dsp.apuram + 65536, 0);
    ares::SuperFamicom::smp.SPC700::power();
    ares::SuperFamicom::smp.r.pc.byte.l = ares::SuperFamicom::smp.iplrom[62];
    ares::SuperFamicom::smp.r.pc.byte.h = ares::SuperFamicom::smp.iplrom[63];
    for (int index = 0; index < maxPrebootInstructions; ++index) {
      ares::SuperFamicom::smp.instruction();
      ++smpInstructions;
      ++smpPrebootInstructions;
      smpFinalPc = static_cast<std::uint16_t>(ares::SuperFamicom::smp.r.pc.w);
      if (static_cast<std::uint8_t>(ares::SuperFamicom::smp.portRead(0)) == 0xaa
        && static_cast<std::uint8_t>(ares::SuperFamicom::smp.portRead(1)) == 0xbb) {
        smpBootSignatureObserved = true;
        return;
      }
    }
  }

  auto resetCpuForLoader(std::uint8_t bank, std::uint16_t stream) -> void {
    streamBank = bank;
    streamAddress = stream;
    memory.clear();
    apuio = {0xaa, 0xbb, 0x00, 0x00};
    currentDestination = 0;
    currentPayloadOffset = 0;
    pendingPort0 = false;
    terminalZeroArmed = false;
    payloadWrites = 0;
    payloadBytes = 0;
    blockStartTokens = 0;
    terminalTokens = 0;
    apuioReads = 0;
    apuioWrites = 0;
    memory[0x0001fb] = 0x03;
    memory[0x0001fc] = 0x80;
    memory[0x0001fd] = 0x00;
    power();
    r.pc.d = loaderBase;
    r.a.w = streamAddress;
    r.x.w = streamBank;
    r.y.w = 0;
    r.s.w = 0x01fa;
    r.d.w = 0;
    r.b = 0;
    r.e = 0;
    r.p = 0x00;
    instructionCount = 0;
  }

  auto resetCpuForChangeMusic(std::uint8_t command) -> void {
    runFullChangeMusic = true;
    insideLoadSpc700DataCall = false;
    trackCommand = command;
    memory.clear();
    currentDestination = 0;
    currentPayloadOffset = 0;
    pendingPort0 = false;
    terminalZeroArmed = false;
    payloadWrites = 0;
    payloadBytes = 0;
    blockStartTokens = 0;
    terminalTokens = 0;
    apuioReads = 0;
    apuioWrites = 0;
    changeMusicInstructionCount = 0;
    changeMusicLoadCalls = 0;
    commandWrites = 0;
    commandReadStep = -1;
    zeroAckStep = -1;
    keyOnStep = -1;
    keyOnData = 0;
    reachedCommandRead = false;
    reachedZeroAck = false;
    reachedKeyOn = false;
    changeMusicFinalPc = 0;
    changeMusicLoadSteps.clear();
    memory[0x0001fb] = 0x03;
    memory[0x0001fc] = 0x80;
    memory[0x0001fd] = 0x00;
    power();
    r.pc.d = changeMusicBase;
    r.a.w = command;
    r.x.w = 0;
    r.y.w = 0;
    r.s.w = 0x01fa;
    r.d.w = 0;
    r.b = 0;
    r.e = 0;
    r.p = 0x00;
  }

  auto runLoaderLoop(int maxInstructions, bool stopAfterTerminal) -> bool {
    for (int index = 0; index < maxInstructions; ++index) {
      instruction();
      stepSmp(4);
      ++instructionCount;
      finalPc = static_cast<std::uint32_t>(r.pc.d);
      if (finalPc == 0x008004) break;
      if (useRealSmpIplReceiver && stopAfterTerminal && terminalTokens == 1) {
        stepSmp(512);
        break;
      }
    }
    return (finalPc == 0x008004 || (useRealSmpIplReceiver && stopAfterTerminal && terminalTokens == 1)) && terminalTokens == 1;
  }

  auto run(std::vector<std::uint8_t> loader, std::vector<std::uint8_t> rom, std::uint8_t bank, std::uint16_t stream, int maxInstructions, bool realSmpIplReceiver, std::vector<std::uint8_t> iplrom, int maxPrebootInstructions, bool stopAfterTerminal) -> bool {
    loaderBytes = std::move(loader);
    romBytes = std::move(rom);
    useRealSmpIplReceiver = realSmpIplReceiver;
    apuRam.fill(0);
    smpInstructions = 0;
    smpPrebootInstructions = 0;
    smpBootSignatureObserved = false;
    smpFinalPc = 0;
    if (useRealSmpIplReceiver) {
      bootRealSmpIpl(iplrom, maxPrebootInstructions, true);
      if (!smpBootSignatureObserved) return false;
    }
    resetCpuForLoader(bank, stream);
    return runLoaderLoop(maxInstructions, stopAfterTerminal);
  }

  auto runChainedAfterBootstrap(std::vector<std::uint8_t> loader, std::vector<std::uint8_t> rom, std::uint8_t bootstrapBank, std::uint16_t bootstrapStream, std::uint8_t targetBank, std::uint16_t targetStream, int maxInstructions, std::vector<std::uint8_t> iplrom, int maxPrebootInstructions, bool stopAfterTerminal) -> bool {
    loaderBytes = std::move(loader);
    romBytes = std::move(rom);
    useRealSmpIplReceiver = true;
    apuRam.fill(0);
    smpInstructions = 0;
    smpPrebootInstructions = 0;
    smpBootSignatureObserved = false;
    smpFinalPc = 0;
    bootRealSmpIpl(iplrom, maxPrebootInstructions, true);
    if (!smpBootSignatureObserved) return false;
    resetCpuForLoader(bootstrapBank, bootstrapStream);
    bootstrapOk = runLoaderLoop(maxInstructions, false);
    bootstrapInstructionCount = instructionCount;
    bootstrapSmpInstructions = smpInstructions;
    bootstrapPayloadBytes = payloadBytes;
    if (!bootstrapOk) return false;
    resetCpuForLoader(targetBank, targetStream);
    return runLoaderLoop(maxInstructions, stopAfterTerminal);
  }

  auto runSequenceAfterBootstrap(std::vector<std::uint8_t> loader, std::vector<std::uint8_t> rom, std::uint8_t bootstrapBank, std::uint16_t bootstrapStream, const std::vector<std::pair<std::uint8_t, std::uint16_t>>& sequence, int maxInstructions, std::vector<std::uint8_t> iplrom, int maxPrebootInstructions) -> bool {
    loaderBytes = std::move(loader);
    romBytes = std::move(rom);
    useRealSmpIplReceiver = true;
    apuRam.fill(0);
    smpInstructions = 0;
    smpPrebootInstructions = 0;
    smpBootSignatureObserved = false;
    smpFinalPc = 0;
    sequenceSteps.clear();
    bootRealSmpIpl(iplrom, maxPrebootInstructions, true);
    if (!smpBootSignatureObserved) return false;
    resetCpuForLoader(bootstrapBank, bootstrapStream);
    bootstrapOk = runLoaderLoop(maxInstructions, false);
    bootstrapInstructionCount = instructionCount;
    bootstrapSmpInstructions = smpInstructions;
    bootstrapPayloadBytes = payloadBytes;
    if (!bootstrapOk) return false;
    bool allOk = true;
    for (const auto& item : sequence) {
      resetCpuForLoader(item.first, item.second);
      const bool stepOk = runLoaderLoop(maxInstructions, false);
      sequenceSteps.push_back({
        item.first,
        item.second,
        stepOk,
        instructionCount,
        payloadBytes,
        blockStartTokens,
        terminalTokens,
        finalPc,
        smpFinalPc,
      });
      if (!stepOk) allOk = false;
    }
    return allOk;
  }

  auto startDirectSmpDriverFromModeledRam() -> void {
    useRealSmpIplReceiver = true;
    smpBootSignatureObserved = true;
    ares::SuperFamicom::smp.SPC700::power();
    std::copy(apuRam.begin(), apuRam.end(), ares::SuperFamicom::dsp.apuram);
    std::fill(ares::SuperFamicom::dsp.registers, ares::SuperFamicom::dsp.registers + 128, 0);
    ares::SuperFamicom::smp.r.pc.byte.l = 0x00;
    ares::SuperFamicom::smp.r.pc.byte.h = 0x05;
    ares::SuperFamicom::smp.r.s = 0xef;
    smpFinalPc = 0x0500;
  }

  auto runChangeMusicCommandAndCapture(std::uint8_t command, int maxInstructions, int postCommandSmpInstructions) -> bool {
    resetCpuForChangeMusic(command);
    for (int index = 0; index < maxInstructions; ++index) {
      instruction();
      stepSmp(4);
      ++changeMusicInstructionCount;
      changeMusicFinalPc = static_cast<std::uint32_t>(r.pc.d);
      if (insideLoadSpc700DataCall && !changeMusicLoadSteps.empty()) {
        const auto& step = changeMusicLoadSteps.back();
        if (step.terminalTokens >= 1 && (changeMusicFinalPc < loaderBase || changeMusicFinalPc >= loaderEnd)) {
          insideLoadSpc700DataCall = false;
        }
      }
      if (commandWrites == 1 && changeMusicFinalPc == 0x008004) break;
    }

    for (int index = 0; index < postCommandSmpInstructions; ++index) {
      const std::uint16_t pc = static_cast<std::uint16_t>(ares::SuperFamicom::smp.r.pc.w);
      if (pc == 0x062a && !reachedCommandRead) {
        reachedCommandRead = true;
        commandReadStep = index;
      }
      ares::SuperFamicom::smp.instruction();
      ++smpInstructions;
      smpFinalPc = static_cast<std::uint16_t>(ares::SuperFamicom::smp.r.pc.w);
      if (reachedCommandRead && !reachedZeroAck && static_cast<std::uint8_t>(ares::SuperFamicom::smp.portRead(0)) == 0x00) {
        reachedZeroAck = true;
        zeroAckStep = index;
      }
      const std::uint8_t kon = static_cast<std::uint8_t>(ares::SuperFamicom::dsp.registers[0x4c]);
      if (reachedZeroAck && kon) {
        reachedKeyOn = true;
        keyOnStep = index;
        keyOnData = kon;
        lastKeyOnPc = static_cast<std::uint16_t>(ares::SuperFamicom::smp.r.pc.w);
        lastKeyOnYa = static_cast<std::uint16_t>(ares::SuperFamicom::smp.r.ya.w);
        lastKeyOnX = static_cast<std::uint8_t>(ares::SuperFamicom::smp.r.x);
        lastKeyOnS = static_cast<std::uint8_t>(ares::SuperFamicom::smp.r.s);
        lastKeyOnP = static_cast<std::uint8_t>(static_cast<unsigned>(ares::SuperFamicom::smp.r.p));
        lastKeyOnSnapshot = buildSpcSnapshot(lastKeyOnPc, lastKeyOnYa, lastKeyOnX, lastKeyOnS, lastKeyOnP);
        break;
      }
    }

    return changeMusicFinalPc == 0x008004
      && commandWrites == 1
      && changeMusicLoadCalls > 0
      && terminalTokens == changeMusicLoadCalls
      && reachedCommandRead
      && reachedZeroAck
      && reachedKeyOn;
  }

  auto runChangeMusicAfterDirectBootstrap(std::vector<std::uint8_t> loader, std::vector<std::uint8_t> rom, std::uint8_t bootstrapBank, std::uint16_t bootstrapStream, std::uint8_t command, int maxInstructions, int postCommandSmpInstructions, int commandWriteBurst) -> bool {
    loaderBytes = std::move(loader);
    romBytes = std::move(rom);
    useRealSmpIplReceiver = false;
    runFullChangeMusic = false;
    commandWriteSmpBurst = commandWriteBurst;
    apuRam.fill(0);
    smpInstructions = 0;
    smpPrebootInstructions = 0;
    smpBootSignatureObserved = false;
    smpFinalPc = 0;
    resetCpuForLoader(bootstrapBank, bootstrapStream);
    bootstrapOk = runLoaderLoop(maxInstructions, false);
    bootstrapInstructionCount = instructionCount;
    bootstrapSmpInstructions = smpInstructions;
    bootstrapPayloadBytes = payloadBytes;
    if (!bootstrapOk) return false;
    startDirectSmpDriverFromModeledRam();
    return runChangeMusicCommandAndCapture(command, maxInstructions, postCommandSmpInstructions);
  }

  auto runChangeMusicAfterBootstrap(std::vector<std::uint8_t> loader, std::vector<std::uint8_t> rom, std::uint8_t bootstrapBank, std::uint16_t bootstrapStream, std::uint8_t command, int maxInstructions, std::vector<std::uint8_t> iplrom, int maxPrebootInstructions, int postCommandSmpInstructions, int commandWriteBurst) -> bool {
    loaderBytes = std::move(loader);
    romBytes = std::move(rom);
    useRealSmpIplReceiver = true;
    runFullChangeMusic = false;
    commandWriteSmpBurst = commandWriteBurst;
    apuRam.fill(0);
    smpInstructions = 0;
    smpPrebootInstructions = 0;
    smpBootSignatureObserved = false;
    smpFinalPc = 0;
    bootRealSmpIpl(iplrom, maxPrebootInstructions, true);
    if (!smpBootSignatureObserved) return false;
    resetCpuForLoader(bootstrapBank, bootstrapStream);
    bootstrapOk = runLoaderLoop(maxInstructions, false);
    bootstrapInstructionCount = instructionCount;
    bootstrapSmpInstructions = smpInstructions;
    bootstrapPayloadBytes = payloadBytes;
    if (!bootstrapOk) return false;
    return runChangeMusicCommandAndCapture(command, maxInstructions, postCommandSmpInstructions);
  }

  auto buildSpcSnapshot(std::uint16_t pc, std::uint16_t ya, std::uint8_t x, std::uint8_t s, std::uint8_t p) -> std::vector<std::uint8_t> {
    std::vector<std::uint8_t> snapshot(0x10200, 0);
    const std::string signature = "SNES-SPC700 Sound File Data v0.30";
    std::copy(signature.begin(), signature.end(), snapshot.begin());
    snapshot[0x21] = 0x1a;
    snapshot[0x22] = 0x1a;
    snapshot[0x23] = 0x1a;
    snapshot[0x24] = 0x1a;
    snapshot[0x25] = static_cast<std::uint8_t>(pc & 0xff);
    snapshot[0x26] = static_cast<std::uint8_t>(pc >> 8);
    snapshot[0x27] = static_cast<std::uint8_t>(ya & 0xff);
    snapshot[0x28] = x;
    snapshot[0x29] = static_cast<std::uint8_t>(ya >> 8);
    snapshot[0x2a] = p;
    snapshot[0x2b] = s;
    std::copy(ares::SuperFamicom::dsp.apuram, ares::SuperFamicom::dsp.apuram + 65536, snapshot.begin() + 0x100);
    std::copy(ares::SuperFamicom::dsp.registers, ares::SuperFamicom::dsp.registers + 128, snapshot.begin() + 0x10100);
    return snapshot;
  }
};

int main(int argc, char** argv) {
  try {
    const fs::path loaderFile = argPath(argc, argv, "--loader-file");
    const fs::path romFile = argPath(argc, argv, "--rom-file");
    if (loaderFile.empty() || romFile.empty()) {
      throw std::runtime_error("usage: earthbound_ares_c0ab06_loader_handshake --loader-file <bin> --rom-file <rom> --stream-bank 0xE2 --stream-address 0x8000");
    }
    const int streamBank = argInt(argc, argv, "--stream-bank", -1);
    const int streamAddress = argInt(argc, argv, "--stream-address", -1);
    const int maxInstructions = argInt(argc, argv, "--max-instructions", 2000000);
    const int maxPrebootInstructions = argInt(argc, argv, "--max-preboot-instructions", 20000);
    const int postCommandSmpInstructions = argInt(argc, argv, "--post-command-smp-instructions", 300000);
    const int commandWriteSmpBurst = argInt(argc, argv, "--command-write-smp-burst", 0);
    const int changeMusicTrack = argInt(argc, argv, "--change-music-track", -1);
    const std::string receiver = argString(argc, argv, "--receiver", "modeled");
    const bool stopAfterTerminal = hasFlag(argc, argv, "--stop-after-terminal");
    const int bootstrapBank = argInt(argc, argv, "--bootstrap-bank", -1);
    const int bootstrapAddress = argInt(argc, argv, "--bootstrap-address", -1);
    const std::string sequenceText = argString(argc, argv, "--sequence", "");
    const fs::path iplFile = argPath(argc, argv, "--ipl-file");
    const fs::path apuRamOut = argPath(argc, argv, "--apu-ram-out");
    const fs::path snapshotOut = argPath(argc, argv, "--snapshot-out");
    if (streamBank < 0 || streamAddress < 0) throw std::runtime_error("missing stream pointer");
    if (receiver != "modeled" && receiver != "ares_smp_ipl" && receiver != "ares_smp_builtin_ipl") throw std::runtime_error("--receiver must be modeled, ares_smp_ipl, or ares_smp_builtin_ipl");
    if (receiver == "ares_smp_ipl" && iplFile.empty()) throw std::runtime_error("--receiver ares_smp_ipl requires --ipl-file");
    C0AB06LoaderProbe probe;
    const bool directChangeMusicAfterBootstrap = receiver == "ares_smp_builtin_ipl" && bootstrapBank >= 0 && bootstrapAddress >= 0 && changeMusicTrack >= 0;
    const bool changeMusicAfterBootstrap = receiver == "ares_smp_ipl" && bootstrapBank >= 0 && bootstrapAddress >= 0 && changeMusicTrack >= 0;
    const bool sequenceAfterBootstrap = receiver == "ares_smp_ipl" && bootstrapBank >= 0 && bootstrapAddress >= 0 && !sequenceText.empty() && !changeMusicAfterBootstrap && !directChangeMusicAfterBootstrap;
    const bool chainAfterBootstrap = receiver == "ares_smp_ipl" && bootstrapBank >= 0 && bootstrapAddress >= 0 && sequenceText.empty() && !changeMusicAfterBootstrap && !directChangeMusicAfterBootstrap;
    const auto sequence = sequenceAfterBootstrap ? parseSequence(sequenceText) : std::vector<std::pair<std::uint8_t, std::uint16_t>>{};
    const bool ok = directChangeMusicAfterBootstrap
      ? probe.runChangeMusicAfterDirectBootstrap(
          readBytes(loaderFile),
          readBytes(romFile),
          static_cast<std::uint8_t>(bootstrapBank),
          static_cast<std::uint16_t>(bootstrapAddress),
          static_cast<std::uint8_t>(changeMusicTrack),
          maxInstructions,
          postCommandSmpInstructions,
          commandWriteSmpBurst
        )
      : (changeMusicAfterBootstrap
      ? probe.runChangeMusicAfterBootstrap(
          readBytes(loaderFile),
          readBytes(romFile),
          static_cast<std::uint8_t>(bootstrapBank),
          static_cast<std::uint16_t>(bootstrapAddress),
          static_cast<std::uint8_t>(changeMusicTrack),
          maxInstructions,
          readBytes(iplFile),
          maxPrebootInstructions,
          postCommandSmpInstructions,
          commandWriteSmpBurst
        )
      : (sequenceAfterBootstrap
      ? probe.runSequenceAfterBootstrap(
          readBytes(loaderFile),
          readBytes(romFile),
          static_cast<std::uint8_t>(bootstrapBank),
          static_cast<std::uint16_t>(bootstrapAddress),
          sequence,
          maxInstructions,
          readBytes(iplFile),
          maxPrebootInstructions
        )
      : (chainAfterBootstrap
      ? probe.runChainedAfterBootstrap(
          readBytes(loaderFile),
          readBytes(romFile),
          static_cast<std::uint8_t>(bootstrapBank),
          static_cast<std::uint16_t>(bootstrapAddress),
          static_cast<std::uint8_t>(streamBank),
          static_cast<std::uint16_t>(streamAddress),
          maxInstructions,
          readBytes(iplFile),
          maxPrebootInstructions,
          stopAfterTerminal
        )
      : probe.run(
          readBytes(loaderFile),
          readBytes(romFile),
          static_cast<std::uint8_t>(streamBank),
          static_cast<std::uint16_t>(streamAddress),
          maxInstructions,
          receiver == "ares_smp_ipl",
          receiver == "ares_smp_ipl" ? readBytes(iplFile) : std::vector<std::uint8_t>{},
          maxPrebootInstructions,
          stopAfterTerminal
        ))));
    if (!apuRamOut.empty()) {
      if (receiver == "ares_smp_ipl" || receiver == "ares_smp_builtin_ipl") {
        writeBytes(apuRamOut, reinterpret_cast<const std::uint8_t*>(ares::SuperFamicom::dsp.apuram), 65536);
      } else {
        writeBytes(apuRamOut, probe.apuRam.data(), probe.apuRam.size());
      }
    }    if (!snapshotOut.empty() && !probe.lastKeyOnSnapshot.empty()) {
      writeBytes(snapshotOut, probe.lastKeyOnSnapshot.data(), probe.lastKeyOnSnapshot.size());
    }
    std::cout << "{\n";
    std::cout << "  \"schema\": \"earthbound-decomp.c0ab06-loader-handshake.v1\",\n";
    std::cout << "  \"ok\": " << (ok ? "true" : "false") << ",\n";
    std::cout << "  \"receiver\": \"" << receiver << "\",\n";
    std::cout << "  \"stop_after_terminal\": " << (stopAfterTerminal ? "true" : "false") << ",\n";
    std::cout << "  \"chain_after_bootstrap\": " << (chainAfterBootstrap ? "true" : "false") << ",\n";
    std::cout << "  \"sequence_after_bootstrap\": " << (sequenceAfterBootstrap ? "true" : "false") << ",\n";
    std::cout << "  \"change_music_after_bootstrap\": " << ((changeMusicAfterBootstrap || directChangeMusicAfterBootstrap) ? "true" : "false") << ",\n";
    if (chainAfterBootstrap || sequenceAfterBootstrap || changeMusicAfterBootstrap || directChangeMusicAfterBootstrap) {
      std::cout << "  \"bootstrap\": {\"bank\": \"" << hexByte(static_cast<std::uint8_t>(bootstrapBank)) << "\", \"address\": \"" << hexWord(static_cast<std::uint16_t>(bootstrapAddress)) << "\", \"ok\": " << (probe.bootstrapOk ? "true" : "false") << ", \"instruction_count\": " << probe.bootstrapInstructionCount << ", \"smp_instructions\": " << probe.bootstrapSmpInstructions << ", \"payload_bytes\": " << probe.bootstrapPayloadBytes << "},\n";
    }
    if (sequenceAfterBootstrap) {
      std::cout << "  \"sequence\": [";
      for (std::size_t index = 0; index < probe.sequenceSteps.size(); ++index) {
        const auto& step = probe.sequenceSteps[index];
        if (index) std::cout << ", ";
        std::cout << "{\"index\": " << index
                  << ", \"bank\": \"" << hexByte(step.bank)
                  << "\", \"address\": \"" << hexWord(step.address)
                  << "\", \"ok\": " << (step.ok ? "true" : "false")
                  << ", \"instruction_count\": " << step.instructionCount
                  << ", \"payload_bytes\": " << step.payloadBytes
                  << ", \"block_start_tokens\": " << step.blockStartTokens
                  << ", \"terminal_tokens\": " << step.terminalTokens
                  << ", \"final_pc\": \"" << hexLong(step.finalPc)
                  << "\", \"smp_final_pc\": \"" << hexWord(step.smpFinalPc)
                  << "\"}";
      }
      std::cout << "],\n";
    }
    if (changeMusicAfterBootstrap) {
      std::cout << "  \"change_music\": {";
      std::cout << "\"track_command\": \"" << hexByte(static_cast<std::uint8_t>(changeMusicTrack)) << "\"";
      std::cout << ", \"instruction_count\": " << probe.changeMusicInstructionCount;
      std::cout << ", \"load_calls\": " << probe.changeMusicLoadCalls;
      std::cout << ", \"command_writes\": " << probe.commandWrites;
      std::cout << ", \"command_write_smp_burst\": " << probe.commandWriteSmpBurst;
      std::cout << ", \"final_pc\": \"" << hexLong(probe.changeMusicFinalPc) << "\"";
      std::cout << ", \"reached_command_read_pc_062a\": " << (probe.reachedCommandRead ? "true" : "false");
      std::cout << ", \"command_read_step\": " << probe.commandReadStep;
      std::cout << ", \"reached_zero_ack_shape\": " << (probe.reachedZeroAck ? "true" : "false");
      std::cout << ", \"zero_ack_step\": " << probe.zeroAckStep;
      std::cout << ", \"reached_key_on_after_ack\": " << (probe.reachedKeyOn ? "true" : "false");
      std::cout << ", \"key_on_step\": " << probe.keyOnStep;
      std::cout << ", \"key_on_data\": \"" << hexByte(probe.keyOnData) << "\"";
      std::cout << ", \"last_key_on_snapshot\": {\"available\": " << (!probe.lastKeyOnSnapshot.empty() ? "true" : "false");
      if (!probe.lastKeyOnSnapshot.empty()) {
        std::cout << ", \"path\": \"" << snapshotOut.generic_string() << "\"";
        std::cout << ", \"bytes\": " << probe.lastKeyOnSnapshot.size();
        std::cout << ", \"pc\": \"" << hexWord(probe.lastKeyOnPc) << "\"";
        std::cout << ", \"registers\": {\"ya\": \"" << hexWord(probe.lastKeyOnYa) << "\", \"x\": \"" << hexByte(probe.lastKeyOnX) << "\", \"s\": \"" << hexByte(probe.lastKeyOnS) << "\", \"p\": \"" << hexByte(probe.lastKeyOnP) << "\"}";
      }
      std::cout << "}";
      std::cout << ", \"load_steps\": [";
      for (std::size_t index = 0; index < probe.changeMusicLoadSteps.size(); ++index) {
        const auto& step = probe.changeMusicLoadSteps[index];
        if (index) std::cout << ", ";
        std::cout << "{\"index\": " << index
                  << ", \"bank\": \"" << hexByte(step.bank)
                  << "\", \"address\": \"" << hexWord(step.address)
                  << "\", \"payload_bytes\": " << step.payloadBytes
                  << ", \"block_start_tokens\": " << step.blockStartTokens
                  << ", \"terminal_tokens\": " << step.terminalTokens
                  << "}";
      }
      std::cout << "]},\n";
    }
    std::cout << "  \"stream_bank\": \"" << hexByte(static_cast<std::uint8_t>(streamBank)) << "\",\n";
    std::cout << "  \"stream_address\": \"" << hexWord(static_cast<std::uint16_t>(streamAddress)) << "\",\n";
    std::cout << "  \"instruction_count\": " << probe.instructionCount << ",\n";
    std::cout << "  \"final_pc\": \"" << hexLong(probe.finalPc) << "\",\n";
    std::cout << "  \"payload_writes\": " << probe.payloadWrites << ",\n";
    std::cout << "  \"payload_bytes\": " << probe.payloadBytes << ",\n";
    std::cout << "  \"block_start_tokens\": " << probe.blockStartTokens << ",\n";
    std::cout << "  \"terminal_tokens\": " << probe.terminalTokens << ",\n";
    std::cout << "  \"apuio_reads\": " << probe.apuioReads << ",\n";
    std::cout << "  \"apuio_writes\": " << probe.apuioWrites << ",\n";
    std::cout << "  \"smp_boot_signature_observed\": " << (probe.smpBootSignatureObserved ? "true" : "false") << ",\n";
    std::cout << "  \"smp_preboot_instructions\": " << probe.smpPrebootInstructions << ",\n";
    std::cout << "  \"smp_instructions\": " << probe.smpInstructions << ",\n";
    std::cout << "  \"smp_final_pc\": \"" << hexWord(probe.smpFinalPc) << "\"";
    if (!apuRamOut.empty()) {
      std::cout << ",\n";
      std::cout << "  \"apu_ram_out\": \"" << apuRamOut.generic_string() << "\"\n";
    } else {
      std::cout << "\n";
    }
    std::cout << "}\n";
    return ok ? 0 : 1;
  } catch (const std::exception& error) {
    std::cerr << error.what() << "\n";
    return 1;
  }
}
