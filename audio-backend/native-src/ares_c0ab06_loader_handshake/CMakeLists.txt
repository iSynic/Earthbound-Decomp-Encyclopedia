cmake_minimum_required(VERSION 3.28)
project(earthbound_ares_c0ab06_loader_handshake LANGUAGES CXX)

set(ARES_ROOT "" CACHE PATH "Local ares source checkout")
if(NOT ARES_ROOT)
  message(FATAL_ERROR "Set ARES_ROOT to the local ares checkout path")
endif()

set(ARES_BUILD "${ARES_ROOT}/build_msvc" CACHE PATH "Local ares build directory")

add_executable(earthbound_ares_c0ab06_loader_handshake main.cpp)
target_compile_features(earthbound_ares_c0ab06_loader_handshake PRIVATE cxx_std_20)
target_compile_definitions(
  earthbound_ares_c0ab06_loader_handshake
  PRIVATE
    WIN32
    _WINDOWS
    NDEBUG
    PROFILE_PERFORMANCE
    VULKAN
    VK_USE_PLATFORM_WIN32_KHR
    CORE_SFC
    EXCLUDE_MANIFEST_FROM_RC
    _WIN32_WINNT=0x0A00
    _CRT_SECURE_NO_WARNINGS
    _CRT_NONSTDC_NO_WARNINGS
    ARES_ENABLE_CHD
    BUILD_RELEASE
    BUILD_LOCAL
    SLJIT_HAVE_CONFIG_PRE=1
    SLJIT_HAVE_CONFIG_POST=1
)
target_include_directories(
  earthbound_ares_c0ab06_loader_handshake
  PRIVATE
    "${ARES_BUILD}/ares"
    "${ARES_ROOT}/ares"
    "${ARES_ROOT}/nall"
    "${ARES_ROOT}/libco/.."
    "${ARES_ROOT}/thirdparty/lzma"
    "${ARES_BUILD}/thirdparty/libchdr/include"
    "${ARES_ROOT}/thirdparty/libchdr/include"
    "${ARES_ROOT}/thirdparty"
    "${ARES_ROOT}/thirdparty/ymfm/src"
    "${ARES_ROOT}/ares/n64/vulkan/parallel-rdp/parallel-rdp"
    "${ARES_ROOT}/ares/n64/vulkan/parallel-rdp/volk"
    "${ARES_ROOT}/ares/n64/vulkan/parallel-rdp/vulkan"
    "${ARES_ROOT}/ares/n64/vulkan/parallel-rdp/vulkan-headers/include"
    "${ARES_ROOT}/ares/n64/vulkan/parallel-rdp/util"
)
target_link_libraries(
  earthbound_ares_c0ab06_loader_handshake
  PRIVATE
    "${ARES_BUILD}/ares/RelWithDebInfo/ares.lib"
    "${ARES_BUILD}/nall/nall/nall.dir/RelWithDebInfo/nall.lib"
    "${ARES_BUILD}/libco/RelWithDebInfo/libco.lib"
    "${ARES_BUILD}/thirdparty/RelWithDebInfo/chdr-static.lib"
    "${ARES_BUILD}/thirdparty/libchdr/deps/lzma-24.05/RelWithDebInfo/lzma.lib"
    "${ARES_BUILD}/thirdparty/libchdr/deps/zlib-1.3.1/RelWithDebInfo/zlibstatic.lib"
    "${ARES_BUILD}/thirdparty/libchdr/deps/zstd-1.5.6/build/cmake/lib/RelWithDebInfo/zstd_static.lib"
    "${ARES_BUILD}/thirdparty/RelWithDebInfo/sljit.lib"
    uuid
    kernel32
    user32
    gdi32
    comctl32
    comdlg32
    shell32
    shlwapi
    advapi32
    ole32
    ws2_32
)
