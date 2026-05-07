# ebsrc Bank C4 Reference Map

Generated from ebsrc bankconfig include order, ebsrc bank symbols, and local source-bank build-candidate spans.

## Summary

- includes: `566`
- exact spans: `485`
- promoted exact spans: `485`
- promotion candidates: `0`
- open/unresolved entries: `64`
- latest promoted end: `C4:FD4B`

## Current Open Frontier

| Start | End | Size | Status | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- | --- |

## Current Exact Frontier Candidates

| Start | End | Size | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- |

## Candidate Backlog

| Start | End | Size | Include | ebsrc Symbol | Local Name | Kind |
| --- | --- | ---: | --- | --- | --- | --- |

## Include Map

| # | Start | End | Size | Status | Promoted | Include | ebsrc Symbol | Local Name |
| ---: | --- | --- | ---: | --- | --- | --- | --- | --- |
| 0 |  |  | 0 | `support` |  | `eventmacros.asm` | `` | `` |
| 1 |  |  | 0 | `support` |  | `common.asm` | `` | `` |
| 2 |  |  | 0 | `support` |  | `config.asm` | `` | `` |
| 3 |  |  | 0 | `support` |  | `structs.asm` | `` | `` |
| 4 |  |  | 0 | `support` |  | `symbols/bank00.inc.asm` | `` | `` |
| 5 |  |  | 0 | `support` |  | `symbols/bank01.inc.asm` | `` | `` |
| 6 |  |  | 0 | `support` |  | `symbols/bank02.inc.asm` | `` | `` |
| 7 |  |  | 0 | `support` |  | `symbols/bank03.inc.asm` | `` | `` |
| 8 |  |  | 0 | `support` |  | `symbols/bank04.inc.asm` | `` | `` |
| 9 |  |  | 0 | `support` |  | `symbols/bank2f.inc.asm` | `` | `` |
| 10 |  |  | 0 | `support` |  | `symbols/audiopacks.inc.asm` | `` | `` |
| 11 |  |  | 0 | `support` |  | `symbols/doors.inc.asm` | `` | `` |
| 12 |  |  | 0 | `support` |  | `symbols/globals.inc.asm` | `` | `` |
| 13 |  |  | 0 | `support` |  | `symbols/map.inc.asm` | `` | `` |
| 14 |  |  | 0 | `support` |  | `symbols/misc.inc.asm` | `` | `` |
| 15 |  |  | 0 | `support` |  | `symbols/text.inc.asm` | `` | `` |
| 16 |  |  | 0 | `support` |  | `flyovers.symbols.asm` | `` | `` |
| 17 | C4:0000 | C4:0009 | 9 | `exact` | yes | `unknown/C4/C40000.asm` | `UNKNOWN_C40000` | `WriteAtoInidisp` |
| 18 | C4:0009 | C4:0015 | 12 | `exact` | yes | `unknown/C4/C40009.asm` | `UNKNOWN_C40009` | `RestoreInidispFromDisplayShadow` |
| 19 | C4:0015 | C4:0023 | 14 | `exact` | yes | `unknown/C4/C40015.asm` | `UNKNOWN_C40015` | `ClearCurrentSlot10f2RefreshVisualAndCheckLiveArea` |
| 20 | C4:0023 | C4:002F | 12 | `exact` | yes | `unknown/C4/C40023.asm` | `UNKNOWN_C40023` | `StoreLowNibble1a42ToCurrentScriptField1372` |
| 21 | C4:002F | C4:0085 | 86 | `exact` | yes | `unknown/C4/C4002F.asm` | `` | `SubmitTwoTextTileStripTransfers` |
| 22 | C4:0085 | C4:00D4 | 79 | `exact` | yes | `unknown/C4/C40085.asm` | `` | `ClaimTextTileBitsetSlot` |
| 23 | C4:00D4 | C4:0B51 | 2685 | `exact` | yes | `data/events/script_pointers.asm` | `` | `` |
| 24 | C4:0B51 | C4:0B59 | 8 | `exact` | yes | `unknown/C4/C40B51.asm` | `UNKNOWN_C40B51` | `SetupSystemErrorScreenDisplay` |
| 25 | C4:0B75 | C4:0BD2 | 93 | `exact` | yes | `unknown/C4/C40B75.asm` | `UNKNOWN_C40B75` | `RenderSystemErrorScreenAndHalt` |
| 26 | C4:0BD2 | C4:0BD4 | 2 | `exact` | yes | `data/map/footstep_sound_table.asm` | `FOOTSTEP_SOUND_TABLE` | `SystemErrorScreenHaltLoop` |
| 27 | C4:0BE8 |  | 0 | `open` |  | `data/unknown/C40BE8.asm` | `UNKNOWN_C40BE8` | `BlankCommonTileSourceBlock` |
| 28 |  |  | 0 | `open` |  | `data/text/floating_sprite_table.asm` | `` | `` |
| 29 |  |  | 0 | `open` |  | `data/events/scripts/785.asm` | `EVENT_785` | `` |
| 30 |  |  | 0 | `open` |  | `data/events/entity_overlays.asm` | `` | `` |
| 31 | C4:0F18 | C4:0F4A | 50 | `exact` | yes | `data/events/C40F18.asm` | `UNKNOWN_C40F18` | `` |
| 32 | C4:0F4A | C4:0F59 | 15 | `exact` | yes | `data/events/C40F4A.asm` | `UNKNOWN_C40F4A` | `` |
| 33 | C4:0F59 |  | 0 | `open` |  | `data/events/C40F59.asm` | `UNKNOWN_C40F59` | `` |
| 34 |  |  | 0 | `open` |  | `data/events/scripts/502.asm` | `EVENT_502` | `` |
| 35 |  |  | 0 | `open` |  | `data/events/scripts/503.asm` | `EVENT_503` | `` |
| 36 |  |  | 0 | `open` |  | `data/events/scripts/504.asm` | `EVENT_504` | `` |
| 37 |  |  | 0 | `open` |  | `data/events/scripts/505.asm` | `EVENT_505` | `` |
| 38 |  |  | 0 | `open` |  | `data/events/scripts/506.asm` | `EVENT_506` | `` |
| 39 |  |  | 0 | `open` |  | `data/events/scripts/507.asm` | `EVENT_507` | `` |
| 40 |  |  | 0 | `open` |  | `data/events/scripts/508.asm` | `EVENT_508` | `` |
| 41 |  |  | 0 | `open` |  | `data/events/scripts/509.asm` | `EVENT_509` | `` |
| 42 |  |  | 0 | `open` |  | `data/events/scripts/510.asm` | `EVENT_510` | `` |
| 43 |  |  | 0 | `open` |  | `data/events/scripts/511.asm` | `EVENT_511` | `` |
| 44 |  |  | 0 | `open` |  | `data/events/scripts/512.asm` | `EVENT_512` | `` |
| 45 |  |  | 0 | `open` |  | `data/events/scripts/513.asm` | `EVENT_513` | `` |
| 46 |  |  | 0 | `open` |  | `data/events/scripts/514.asm` | `EVENT_514` | `` |
| 47 |  |  | 0 | `open` |  | `data/events/scripts/515.asm` | `EVENT_515` | `` |
| 48 |  |  | 0 | `open` |  | `data/events/scripts/516.asm` | `EVENT_516` | `` |
| 49 |  |  | 0 | `open` |  | `data/events/scripts/517.asm` | `EVENT_517` | `` |
| 50 |  |  | 0 | `open` |  | `data/events/scripts/518.asm` | `EVENT_518` | `` |
| 51 |  |  | 0 | `open` |  | `data/events/scripts/519.asm` | `EVENT_519` | `` |
| 52 |  |  | 0 | `open` |  | `data/events/scripts/520.asm` | `EVENT_520` | `` |
| 53 |  |  | 0 | `open` |  | `data/events/scripts/521.asm` | `EVENT_521` | `` |
| 54 |  |  | 0 | `open` |  | `data/events/scripts/522.asm` | `EVENT_522` | `` |
| 55 |  |  | 0 | `open` |  | `data/events/scripts/523.asm` | `EVENT_523` | `` |
| 56 |  |  | 0 | `open` |  | `data/events/scripts/524.asm` | `EVENT_524` | `` |
| 57 |  |  | 0 | `open` |  | `data/events/scripts/525.asm` | `EVENT_525` | `` |
| 58 |  |  | 0 | `open` |  | `data/events/scripts/526.asm` | `EVENT_526` | `` |
| 59 |  |  | 0 | `open` |  | `data/events/scripts/527.asm` | `EVENT_527` | `` |
| 60 |  |  | 0 | `open` |  | `data/events/scripts/528.asm` | `EVENT_528` | `` |
| 61 |  |  | 0 | `open` |  | `data/events/scripts/529.asm` | `EVENT_529` | `` |
| 62 |  |  | 0 | `open` |  | `data/events/scripts/530.asm` | `EVENT_530` | `` |
| 63 |  |  | 0 | `open` |  | `data/events/scripts/534.asm` | `EVENT_534` | `` |
| 64 | C4:1036 | C4:116C | 310 | `exact` | yes | `data/events/C41036.asm` | `UNKNOWN_C41036` | `` |
| 65 | C4:116C | C4:119D | 49 | `exact` | yes | `data/events/C4116C.asm` | `UNKNOWN_C4116C` | `` |
| 66 | C4:119D | C4:11EB | 78 | `exact` | yes | `data/events/C4119D.asm` | `UNKNOWN_C4119D` | `` |
| 67 | C4:11EB | C4:121F | 52 | `exact` | yes | `data/events/C411EB.asm` | `UNKNOWN_C411EB` | `` |
| 68 | C4:121F | C4:1253 | 52 | `exact` | yes | `data/events/C4121F.asm` | `UNKNOWN_C4121F` | `` |
| 69 | C4:1253 | C4:1382 | 303 | `exact` | yes | `data/events/C41253.asm` | `UNKNOWN_C41253` | `` |
| 70 | C4:1382 | C4:13D6 | 84 | `exact` | yes | `data/events/C41382.asm` | `UNKNOWN_C41382` | `` |
| 71 | C4:13D6 | C4:1402 | 44 | `exact` | yes | `data/events/C413D6.asm` | `UNKNOWN_C413D6` | `` |
| 72 | C4:1402 | C4:144C | 74 | `exact` | yes | `data/events/C41402.asm` | `UNKNOWN_C41402` | `` |
| 73 | C4:144C | C4:152A | 222 | `exact` | yes | `data/events/C4144C.asm` | `UNKNOWN_C4144C` | `` |
| 74 | C4:152A | C4:154E | 36 | `exact` | yes | `data/events/C4152A.asm` | `UNKNOWN_C4152A` | `` |
| 75 | C4:154E | C4:158A | 60 | `exact` | yes | `data/events/C4154E.asm` | `UNKNOWN_C4154E` | `` |
| 76 | C4:158A | C4:15BA | 48 | `exact` | yes | `data/events/C4158A.asm` | `UNKNOWN_C4158A` | `` |
| 77 | C4:15BA | C4:15E7 | 45 | `exact` | yes | `data/events/C415BA.asm` | `UNKNOWN_C415BA` | `` |
| 78 | C4:15E7 | C4:160A | 35 | `exact` | yes | `data/events/C415E7.asm` | `UNKNOWN_C415E7` | `` |
| 79 | C4:160A | C4:163F | 53 | `exact` | yes | `data/events/C4160A.asm` | `UNKNOWN_C4160A` | `` |
| 80 | C4:163F | C4:16AC | 109 | `exact` | yes | `data/events/C4163F.asm` | `UNKNOWN_C4163F` | `` |
| 81 | C4:16AC | C4:170E | 98 | `exact` | yes | `data/events/C416AC.asm` | `UNKNOWN_C416AC` | `` |
| 82 | C4:170E | C4:1822 | 276 | `exact` | yes | `data/events/C4170E.asm` | `UNKNOWN_C4170E` | `` |
| 83 | C4:1822 | C4:1900 | 222 | `exact` | yes | `data/events/C41822.asm` | `UNKNOWN_C41822` | `` |
| 84 | C4:1900 | C4:1938 | 56 | `exact` | yes | `data/events/C41900.asm` | `UNKNOWN_C41900` | `` |
| 85 | C4:1938 | C4:1974 | 60 | `exact` | yes | `data/events/C41938.asm` | `UNKNOWN_C41938` | `` |
| 86 | C4:1974 | C4:198D | 25 | `exact` | yes | `data/events/C41974.asm` | `UNKNOWN_C41974` | `` |
| 87 | C4:198D | C4:19B2 | 37 | `exact` | yes | `data/events/C4198D.asm` | `UNKNOWN_C4198D` | `` |
| 88 | C4:19B2 | C4:19BF | 13 | `exact` | yes | `data/events/C419B2.asm` | `UNKNOWN_C419B2` | `` |
| 89 | C4:19BF | C4:1A2A | 107 | `exact` | yes | `data/events/C419BF.asm` | `UNKNOWN_C419BF` | `` |
| 90 | C4:1A2A | C4:1A7D | 83 | `exact` | yes | `data/events/C41A2A.asm` | `UNKNOWN_C41A2A` | `` |
| 91 | C4:1A7D |  | 0 | `open` |  | `data/events/C41A7D.asm` | `UNKNOWN_C41A7D` | `` |
| 92 |  |  | 0 | `open` |  | `system/decomp.asm` | `DECOMP` | `` |
| 93 | C4:1DB6 | C4:1EE9 | 307 | `exact` | yes | `unknown/C4/C41DB6.asm` | `UNKNOWN_C41DB6` | `RenderMaskedGlyphIntoTextTileStaging` |
| 94 | C4:1EB9 | C4:1EC9 | 16 | `exact` | yes | `data/unknown/C41EB9.asm` | `UNKNOWN_C41EB9` | `GlyphTileStagingMaskTable0` |
| 95 | C4:1EC9 | C4:1ED9 | 16 | `exact` | yes | `data/unknown/C41EC9.asm` | `UNKNOWN_C41EC9` | `GlyphTileStagingMaskTable1` |
| 96 | C4:1ED9 | C4:1EE9 | 16 | `exact` | yes | `data/unknown/C41ED9.asm` | `UNKNOWN_C41ED9` | `GlyphTileStagingMaskTable2` |
| 97 | C4:1EE9 | C4:1EF4 | 11 | `exact` | yes | `unknown/C4/C41EE9.asm` | `` | `TrackTextTileStagingMinDirtyOffset` |
| 98 | C4:1EF4 | C4:1EFF | 11 | `exact` | yes | `unknown/C4/C41EF4.asm` | `` | `TrackTextTileStagingMaxDirtyOffset` |
| 99 | C4:1EFF | C4:1FFF | 256 | `exact` | yes | `unknown/C4/C41EFF.asm` | `UNKNOWN_C41EFF` | `ComputeDirectionOctantFromDelta` |
| 100 | C4:1FC5 | C4:1FDF | 26 | `exact` | yes | `data/unknown/C41FC5.asm` | `UNKNOWN_C41FC5` | `DirectionOctantBaseAngleTable` |
| 101 | C4:1FDF | C4:1FFF | 32 | `exact` | yes | `data/unknown/C41FDF.asm` | `UNKNOWN_C41FDF` | `DirectionSlopeThresholdTable` |
| 102 | C4:1FFF | C4:213F | 320 | `exact` | yes | `unknown/C4/C41FFF.asm` | `UNKNOWN_C41FFF` | `ProjectMagnitudeByDirectionAngle` |
| 103 | C4:205D | C4:20BD | 96 | `exact` | yes | `data/unknown/C4205D.asm` | `UNKNOWN_C4205D` | `DirectionProjectionXScaleTable` |
| 104 | C4:20BD | C4:213F | 130 | `exact` | yes | `data/unknown/C420BD.asm` | `UNKNOWN_C420BD` | `DirectionProjectionYScaleTable` |
| 105 | C4:213F | C4:2172 | 51 | `exact` | yes | `unknown/C4/C4213F.asm` | `` | `ScaleU16ByU8Fraction` |
| 106 | C4:2172 | C4:23DC | 618 | `exact` | yes | `data/events/scripts/787.asm` | `EVENT_787` | `` |
| 107 | C4:23DC | C4:240A | 46 | `exact` | yes | `data/events/scripts/860.asm` | `UNKNOWN_C423DC` | `SetCenteredColorWindowRangePreset` |
| 108 | C4:220E |  | 0 | `open` |  | `data/events/C4220E.asm` | `` | `` |
| 109 |  |  | 0 | `open` |  | `data/events/scripts/789.asm` | `EVENT_789` | `` |
| 110 | C4:2235 |  | 0 | `open` |  | `data/events/C42235.asm` | `UNKNOWN_C42235` | `` |
| 111 |  |  | 0 | `open` |  | `data/events/scripts/788.asm` | `EVENT_788` | `` |
| 112 |  |  | 0 | `open` |  | `data/events/scripts/790.asm` | `EVENT_790` | `` |
| 113 |  |  | 0 | `open` |  | `data/events/scripts/791.asm` | `EVENT_791` | `` |
| 114 |  |  | 0 | `open` |  | `data/events/scripts/792.asm` | `EVENT_792` | `` |
| 115 |  |  | 0 | `open` |  | `data/events/scripts/793.asm` | `EVENT_793` | `` |
| 116 |  |  | 0 | `open` |  | `data/events/scripts/794.asm` | `EVENT_794` | `` |
| 117 |  |  | 0 | `open` |  | `data/events/scripts/795.asm` | `EVENT_795` | `` |
| 118 |  |  | 0 | `open` |  | `data/events/scripts/796.asm` | `EVENT_796` | `` |
| 119 |  |  | 0 | `open` |  | `data/events/scripts/797.asm` | `EVENT_797` | `` |
| 120 |  |  | 0 | `open` |  | `data/events/scripts/798.asm` | `EVENT_798` | `` |
| 121 | C4:23DC | C4:240A | 46 | `exact` | yes | `unknown/C4/C423DC.asm` | `UNKNOWN_C423DC` | `SetCenteredColorWindowRangePreset` |
| 122 | C4:240A | C4:2439 | 47 | `exact` | yes | `unknown/C4/C4240A.asm` | `UNKNOWN_C4240A` | `SetFullscreenColorWindowRangePreset` |
| 123 | C4:2439 | C4:245D | 36 | `exact` | yes | `unknown/C4/C42439.asm` | `UNKNOWN_C42439` | `ApplyColorMathAndFixedColorFrom9e37` |
| 124 | C4:245D | C4:248A | 45 | `exact` | yes | `unknown/C4/C4245D.asm` | `UNKNOWN_C4245D` | `StartWh0HdmaChannel4AndWhselA0` |
| 125 | C4:248A | C4:249A | 16 | `exact` | yes | `unknown/C4/C4248A.asm` | `UNKNOWN_C4248A` | `StopWh0HdmaChannel4AndClearWhsel` |
| 126 | C4:249A | C4:24D1 | 55 | `exact` | yes | `unknown/C4/C4249A.asm` | `UNKNOWN_C4249A` | `ApplyFullscreenColorMathWithFixedColorX` |
| 127 | C4:24D1 | C4:2509 | 56 | `exact` | yes | `unknown/C4/C424D1.asm` | `UNKNOWN_C424D1` | `ApplyCenteredColorSubtractHalfPreset` |
| 128 | C4:2509 | C4:2542 | 57 | `exact` | yes | `unknown/C4/C42509.asm` | `UNKNOWN_C42509` | `ApplyFullscreenColorSubtractHalfPreset` |
| 129 | C4:2542 | C4:2569 | 39 | `exact` | yes | `unknown/C4/C42542.asm` | `UNKNOWN_C42542` | `StartWh0HdmaChannel4` |
| 130 | C4:2569 | C4:2574 | 11 | `exact` | yes | `unknown/C4/C42569.asm` | `UNKNOWN_C42569` | `SetColorMathMode33` |
| 131 | C4:2574 | C4:257F | 11 | `exact` | yes | `unknown/C4/C42574.asm` | `UNKNOWN_C42574` | `SetColorMathModeB3` |
| 132 | C4:257F | C4:258C | 13 | `exact` | yes | `unknown/C4/C4257F.asm` | `UNKNOWN_C4257F` | `ClearWh0HdmaChannel4Enable` |
| 133 | C4:258C | C4:25CC | 64 | `exact` | yes | `unknown/C4/C4258C.asm` | `UNKNOWN_C4258C` | `ApplyDualCenteredColorSubtractHalfPreset` |
| 134 | C4:25CC | C4:25F3 | 39 | `exact` | yes | `unknown/C4/C425CC.asm` | `UNKNOWN_C425CC` | `StartWh0HdmaChannel4AltEntry` |
| 135 | C4:25F3 | C4:25FD | 10 | `exact` | yes | `unknown/C4/C425F3.asm` | `UNKNOWN_C425F3` | `ClearWh0HdmaChannel4EnableViaTrb` |
| 136 | C4:25FD | C4:2624 | 39 | `exact` | yes | `unknown/C4/C425FD.asm` | `UNKNOWN_C425FD` | `StartWh2HdmaChannel5` |
| 137 | C4:2624 | C4:2631 | 13 | `exact` | yes | `unknown/C4/C42624.asm` | `UNKNOWN_C42624` | `ClearWh2HdmaChannel5Enable` |
| 138 | C4:2631 | C4:268A | 89 | `exact` | yes | `unknown/C4/C42631.asm` | `UNKNOWN_C42631` | `InitScreenPositionInterpolationFromAngle` |
| 139 | C4:268A | C4:26C7 | 61 | `exact` | yes | `unknown/C4/C4268A.asm` | `UNKNOWN_C4268A` | `StepScreenPositionInterpolationAndApply` |
| 140 | C4:26C7 | C4:26ED | 38 | `exact` | yes | `unknown/C4/C426C7.asm` | `UNKNOWN_C426C7` | `RebaseLiveEntityPositionsToScreenOrigin` |
| 141 | C4:26ED | C4:279F | 178 | `exact` | yes | `unknown/C4/C426ED.asm` | `` | `StepPaletteComponentInterpolationToCgramShadow` |
| 142 | C4:279F | C4:283F | 160 | `exact` | yes | `data/events/scripts/859.asm` | `EVENT_859` | `` |
| 143 | C4:27E0 | C4:2802 | 34 | `exact` | yes | `data/events/C427E0.asm` | `UNKNOWN_C427E0` | `` |
| 144 | C4:2802 | C4:2815 | 19 | `exact` | yes | `data/events/C42802.asm` | `UNKNOWN_C42802` | `` |
| 145 | C4:2815 | C4:2828 | 19 | `exact` | yes | `data/events/C42815.asm` | `UNKNOWN_C42815` | `` |
| 146 | C4:2828 | C4:283F | 23 | `exact` | yes | `data/events/C42828.asm` | `UNKNOWN_C42828` | `` |
| 147 | C4:283F | C4:2884 | 69 | `exact` | yes | `unknown/C4/C4283F.asm` | `UNKNOWN_C4283F` | `CopySecondaryVisualProfileFrameWords` |
| 148 | C4:2884 | C4:28D1 | 77 | `exact` | yes | `unknown/C4/C42884.asm` | `UNKNOWN_C42884` | `CopyDirectionalVisualProfileFrameWords` |
| 149 | C4:28D1 | C4:28FC | 43 | `exact` | yes | `unknown/C4/C428D1.asm` | `UNKNOWN_C428D1` | `Copy7fWordsEvery16ByCount` |
| 150 | C4:28FC | C4:2965 | 105 | `exact` | yes | `unknown/C4/C428FC.asm` | `UNKNOWN_C428FC` | `MergeMasked7fTileColumnRows` |
| 151 | C4:2955 | C4:2965 | 16 | `exact` | yes | `data/unknown/C42955.asm` | `UNKNOWN_C42955` | `TileColumnWordPairMaskTable` |
| 152 | C4:2965 | C4:29AE | 73 | `exact` | yes | `unknown/C4/C42965.asm` | `UNKNOWN_C42965` | `MergeMasked7fTileColumnPair` |
| 153 | C4:29AE | C4:29E8 | 58 | `exact` | yes | `unknown/C4/C429AE.asm` | `UNKNOWN_C429AE` | `GenerateVisualProfileRenderDmaStrips` |
| 154 | C4:29E8 | C4:2A1F | 55 | `exact` | yes | `unknown/C4/C429E8.asm` | `UNKNOWN_C429E8` | `StartMainScreenLayerHdmaFromAdb8` |
| 155 | C4:2A1F | C4:30EC | 1741 | `exact` | yes | `data/unknown/C42A1F.asm` | `UNKNOWN_C42A1F` | `EntityFootprintXOffsetTable` |
| 156 | C4:2A41 | C4:2A63 | 34 | `exact` | yes | `data/unknown/C42A41.asm` | `UNKNOWN_C42A41` | `EntityFootprintYOffsetTable` |
| 157 | C4:2A63 | C4:2A85 | 34 | `exact` | yes | `data/unknown/C42A63.asm` | `UNKNOWN_C42A63` | `EntityFootprintPixelWidthTable` |
| 158 | C4:2A85 | C4:2AA7 | 34 | `exact` | yes | `data/unknown/C42A85.asm` | `UNKNOWN_C42A85` | `EntityFootprintPixelHeightTable` |
| 159 | C4:2AA7 | C4:2AC9 | 34 | `exact` | yes | `data/unknown/C42AA7.asm` | `UNKNOWN_C42AA7` | `EntityFootprintTileWidthTable` |
| 160 | C4:2AC9 | C4:2AEB | 34 | `exact` | yes | `data/unknown/C42AC9.asm` | `UNKNOWN_C42AC9` | `EntityFootprintTileHeightTable` |
| 161 | C4:2AEB | C4:2B0D | 34 | `exact` | yes | `data/unknown/C42AEB.asm` | `UNKNOWN_C42AEB` | `EntityFootprintAnchorOffsetTable` |
| 162 | C4:2B0D | C4:2B51 | 68 | `exact` | yes | `data/unknown/C42B0D.asm` | `UNKNOWN_C42B0D` | `SecondaryVisualDescriptorPointerTable` |
| 163 | C4:2B51 | C4:2B5D | 12 | `exact` | yes | `data/unknown/C42B51.asm` | `UNKNOWN_C42B51` | `SecondaryVisualDescriptor1Piece` |
| 164 | C4:2B5D | C4:2B73 | 22 | `exact` | yes | `data/unknown/C42B5D.asm` | `` | `SecondaryVisualDescriptor2PieceNarrow` |
| 165 | C4:2B73 | C4:2B89 | 22 | `exact` | yes | `data/unknown/C42B73.asm` | `` | `SecondaryVisualDescriptor2PieceWide` |
| 166 | C4:2B89 | C4:2BA9 | 32 | `exact` | yes | `data/unknown/C42B89.asm` | `` | `SecondaryVisualDescriptor3PieceColumn` |
| 167 | C4:2BA9 | C4:2BBF | 22 | `exact` | yes | `data/unknown/C42BA9.asm` | `` | `SecondaryVisualDescriptor2PieceBandSplit` |
| 168 | C4:2BBF | C4:2BE9 | 42 | `exact` | yes | `data/unknown/C42BBF.asm` | `` | `SecondaryVisualDescriptor4Piece2x2` |
| 169 | C4:2BE9 | C4:2BFF | 22 | `exact` | yes | `data/unknown/C42BE9.asm` | `` | `SecondaryVisualDescriptor2PieceBandSplitAlt` |
| 170 | C4:2BFF | C4:2C29 | 42 | `exact` | yes | `data/unknown/C42BFF.asm` | `` | `SecondaryVisualDescriptor4Piece2x2Wide` |
| 171 | C4:2C29 | C4:2C67 | 62 | `exact` | yes | `data/unknown/C42C29.asm` | `` | `SecondaryVisualDescriptor6Piece3x2` |
| 172 | C4:2C67 | C4:2CA5 | 62 | `exact` | yes | `data/unknown/C42C67.asm` | `` | `SecondaryVisualDescriptor6Piece3x2Tall` |
| 173 | C4:2CA5 | C4:2CC5 | 32 | `exact` | yes | `data/unknown/C42CA5.asm` | `` | `SecondaryVisualDescriptor3Piece1x3` |
| 174 | C4:2CC5 | C4:2D03 | 62 | `exact` | yes | `data/unknown/C42CC5.asm` | `` | `SecondaryVisualDescriptor6Piece2x3Wide` |
| 175 | C4:2D03 | C4:2D5F | 92 | `exact` | yes | `data/unknown/C42D03.asm` | `` | `SecondaryVisualDescriptor9Piece3x3` |
| 176 | C4:2D5F | C4:2DD9 | 122 | `exact` | yes | `data/unknown/C42D5F.asm` | `` | `SecondaryVisualDescriptor12Piece4x3` |
| 177 | C4:2DD9 | C4:2E7B | 162 | `exact` | yes | `data/unknown/C42DD9.asm` | `` | `SecondaryVisualDescriptor16Piece4x4` |
| 178 | C4:2E7B |  | 0 | `open` |  | `data/unknown/C42E7B.asm` | `` | `SecondaryVisualDescriptor20Piece4x5` |
| 179 |  |  | 0 | `open` |  | `overworld/set_party_tick_callbacks.asm` | `SET_PARTY_TICK_CALLBACKS` | `` |
| 180 |  |  | 0 | `open` |  | `data/map/tile_table_chunks_table.asm` | `` | `` |
| 181 | C4:2F8C | C4:303C | 176 | `exact` | yes | `data/unknown/C42F8C.asm` | `UNKNOWN_C42F8C` | `VisualTileBaseVramOffsetTable` |
| 182 | C4:303C |  | 0 | `open` |  | `data/unknown/C4303C.asm` | `UNKNOWN_C4303C` | `VisualPieceTileWordLadder` |
| 183 |  |  | 0 | `open` |  | `overworld/velocity_store.asm` | `VELOCITY_STORE` | `` |
| 184 | C4:32B1 | C4:3317 | 102 | `exact` | yes | `unknown/C4/C432B1.asm` | `UNKNOWN_C432B1` | `ResetPartyVisualMasksAndStatusBytes` |
| 185 | C4:3317 | C4:3344 | 45 | `exact` | yes | `unknown/C4/C43317.asm` | `UNKNOWN_C43317` | `RebuildPartyCharacterRecordPointerTable4dc8` |
| 186 | C4:3344 | C4:334A | 6 | `exact` | yes | `unknown/C4/C43344.asm` | `UNKNOWN_C43344` | `SetSpecialEventRestrictionLatch5d98` |
| 187 | C4:334A | C4:343E | 244 | `exact` | yes | `unknown/C4/C4334A.asm` | `UNKNOWN_C4334A` | `ProbeDoorDestinationAheadOfParty` |
| 188 | C4:343E | C4:3550 | 274 | `exact` | yes | `unknown/C4/C4343E.asm` | `UNKNOWN_C4343E` | `BuildPartyEquipmentComparisonVisualStateRows` |
| 189 | C4:3550 | C4:3568 | 24 | `exact` | yes | `data/item_use_menu_strings.asm` | `ITEM_USE_MENU_STRINGS` | `` |
| 190 | C4:3568 | C4:3573 | 11 | `exact` | yes | `unknown/C4/C43568.asm` | `UNKNOWN_C43568` | `PumpBattleBgEffectFrameAndPollInput` |
| 191 | C4:3573 | C4:35E4 | 113 | `exact` | yes | `unknown/C4/C43573.asm` | `UNKNOWN_C43573` | `SelectFocusedPartyHpPpActorAndBlankRow` |
| 192 | C4:35E4 | C4:3657 | 115 | `exact` | yes | `unknown/C4/C435E4.asm` | `UNKNOWN_C435E4` | `ClearBattleTargetRowHighlightFlags` |
| 193 | C4:3657 | C4:36D7 | 128 | `exact` | yes | `unknown/C4/C43657.asm` | `UNKNOWN_C43657` | `SetBattleTargetRowHighlightFlags` |
| 194 | C4:36D7 | C4:3739 | 98 | `exact` | yes | `unknown/C4/C436D7.asm` | `UNKNOWN_C436D7` | `FillTextWindowRowWithBlankTileWords` |
| 195 | C4:3739 | C4:37B8 | 127 | `exact` | yes | `unknown/C4/C43739.asm` | `UNKNOWN_C43739` | `ClearTextWindowRowAndDisplayObjects` |
| 196 | C4:37B8 | C4:3874 | 188 | `exact` | yes | `unknown/C4/C437B8.asm` | `UNKNOWN_C437B8` | `ScrollTextWindowBufferUpOneLine` |
| 197 | C4:3874 | C4:38A5 | 49 | `exact` | yes | `unknown/C4/C43874.asm` | `UNKNOWN_C43874` | `SetWindowDescriptorCursorFields` |
| 198 | C4:38A5 | C4:38B1 | 12 | `exact` | yes | `unknown/C4/C438A5.asm` | `UNKNOWN_C438A5` | `SetActiveWindowDescriptorCursorFields` |
| 199 | C4:38B1 | C4:3915 | 100 | `exact` | yes | `text/print_newline.asm` | `PRINT_NEWLINE` | `AdvanceActiveWindowLineOrScroll` |
| 200 | C4:3915 | C4:3B15 | 512 | `exact` | yes | `data/text/locked_tiles.asm` | `LOCKED_TILES` | `` |
| 201 | C4:3B15 | C4:3BB9 | 164 | `exact` | yes | `unknown/C4/C43B15.asm` | `UNKNOWN_C43B15` | `ApplyActiveWindowLineTileAttributeBits` |
| 202 | C4:3BB9 | C4:3CAA | 241 | `exact` | yes | `unknown/C4/C43BB9.asm` | `UNKNOWN_C43BB9` | `WriteSpecialActiveWindowStringRun` |
| 203 | C4:3CAA | C4:3CD2 | 40 | `exact` | yes | `unknown/C4/C43CAA.asm` | `UNKNOWN_C43CAA` | `AdvanceAnimatedGlyphTileStateOffset` |
| 204 | C4:3CD2 | C4:3D24 | 82 | `exact` | yes | `unknown/C4/C43CD2.asm` | `UNKNOWN_C43CD2` | `SetActiveCursorAndStageGlyphRunUpload` |
| 205 | C4:3D24 | C4:3D75 | 81 | `exact` | yes | `unknown/C4/C43D24.asm` | `UNKNOWN_C43D24` | `StagePendingGlyphVariantTileUpload` |
| 206 | C4:3D75 | C4:3D95 | 32 | `exact` | yes | `unknown/C4/C43D75.asm` | `UNKNOWN_C43D75` | `StageGlyphVariantTileState` |
| 207 | C4:3D95 | C4:3DDB | 70 | `exact` | yes | `unknown/C4/C43D95.asm` | `UNKNOWN_C43D95` | `StageActiveCursorGlyphVariantState` |
| 208 | C4:3DDB | C4:3E31 | 86 | `exact` | yes | `unknown/C4/C43DDB.asm` | `UNKNOWN_C43DDB` | `PrintRecordSelectionMarkerAndStageGlyphRun` |
| 209 | C4:3E31 | C4:3EF8 | 199 | `exact` | yes | `unknown/C4/C43E31.asm` | `UNKNOWN_C43E31` | `MeasureActiveWindowStringPixelWidth` |
| 210 | C4:3EF8 | C4:3F53 | 91 | `exact` | yes | `unknown/C4/C43EF8.asm` | `UNKNOWN_C43EF8` | `StageCenteredStringGlyphVariantState` |
| 211 | C4:3F53 | C4:3F77 | 36 | `exact` | yes | `unknown/C4/C43F53.asm` | `UNKNOWN_C43F53` | `LoadMenuNameEntryMaskTableTo1ad6` |
| 212 | C4:3F77 | C4:406A | 243 | `exact` | yes | `unknown/C4/C43F77.asm` | `UNKNOWN_C43F77` | `PrintGlyphWithTileCleanupSoundDelay` |
| 213 | C4:406A | C4:40B5 | 75 | `exact` | yes | `text/get_character_at_cursor_position.asm` | `GET_CHARACTER_AT_CURSOR_POSITION` | `ReadNameEntryGridCharacter` |
| 214 | C4:40B5 | C4:41B7 | 258 | `exact` | yes | `unknown/C4/C440B5.asm` | `UNKNOWN_C440B5` | `BuildTextInputStringGlyphMetrics` |
| 215 | C4:41B7 | C4:424A | 147 | `exact` | yes | `unknown/C4/C441B7.asm` | `UNKNOWN_C441B7` | `InitializeTextInputOptionGlyphMetrics` |
| 216 | C4:424A | C4:42AC | 98 | `exact` | yes | `unknown/C4/C4424A.asm` | `` | `SetTextInputOptionMetricSlot` |
| 217 | C4:42AC | C4:44FB | 591 | `exact` | yes | `unknown/C4/C442AC.asm` | `UNKNOWN_C442AC` | `RenderTextInputOptionStrip` |
| 218 | C4:44FB | C4:45E1 | 230 | `exact` | yes | `unknown/C4/C444FB.asm` | `UNKNOWN_C444FB` | `UploadWindowTitleGlyphTiles` |
| 219 | C4:45E1 | C4:47FB | 538 | `exact` | yes | `unknown/C4/C445E1.asm` | `UNKNOWN_C445E1` | `PreflightTextParserWrapForActiveWindow` |
| 220 | C4:47FB | C4:487C | 129 | `exact` | yes | `unknown/C4/C447FB.asm` | `UNKNOWN_C447FB` | `PrintFixedStringWithWrapPreflight` |
| 221 | C4:487C | C4:4963 | 231 | `exact` | yes | `unknown/C4/C4487C.asm` | `UNKNOWN_C4487C` | `PrintSegmentedStringBufferWithWrapPreflight` |
| 222 | C4:4963 | C4:4AD7 | 372 | `exact` | yes | `unknown/C4/C44963.asm` | `UNKNOWN_C44963` | `RefreshTextWindowVramPlanesForMode` |
| 223 | C4:4AD7 | C4:4AF7 | 32 | `exact` | yes | `data/unknown/C44AD7.asm` | `UNKNOWN_C44AD7` | `TextTileBitClearMaskTable` |
| 224 | C4:4AF7 | C4:4B3A | 67 | `exact` | yes | `text/free_tile.asm` | `FREE_TILE` | `ReleaseTextTileBitsetSlotForTileWord` |
| 225 | C4:4B3A | C4:4C6C | 306 | `exact` | yes | `unknown/C4/C44B3A.asm` | `UNKNOWN_C44B3A` | `RenderTextTokenGlyphRunToScratchRows` |
| 226 | C4:4C6C | C4:4C8C | 32 | `exact` | yes | `data/powers_of_two_16.asm` | `` | `TextTileBitMaskTable` |
| 227 | C4:4C8C | C4:4DCA | 318 | `exact` | yes | `unknown/C4/C44C8C.asm` | `` | `PlaceTextTilePairAtActiveCursor` |
| 228 | C4:4DCA | C4:4E44 | 122 | `exact` | yes | `unknown/C4/C44DCA.asm` | `UNKNOWN_C44DCA` | `CatchUpTextTileStripTransfers` |
| 229 | C4:4E44 | C4:4E4D | 9 | `exact` | yes | `unknown/C4/C44E44.asm` | `UNKNOWN_C44E44` | `ClearGlyphVariantOffsetMirrors` |
| 230 | C4:4E4D | C4:4E61 | 20 | `exact` | yes | `text/free_tile_safe.asm` | `FREE_TILE_SAFE` | `ReleaseNonBlankTextTileWord` |
| 231 | C4:4E61 | C4:4FF3 | 402 | `exact` | yes | `unknown/C4/C44E61.asm` | `UNKNOWN_C44E61` | `StageTextTokenGlyphRunForActiveWindow` |
| 232 | C4:4FF3 | C4:507A | 135 | `exact` | yes | `unknown/C4/C44FF3.asm` | `UNKNOWN_C44FF3` | `MeasureGlyphByteRunPixelWidth` |
| 233 | C4:507A | C4:51FA | 384 | `exact` | yes | `unknown/C4/C4507A.asm` | `UNKNOWN_C4507A` | `PrintRightAlignedDecimalValueInActiveWindow` |
| 234 | C4:51FA | C4:54F2 | 760 | `exact` | yes | `unknown/C4/C451FA.asm` | `UNKNOWN_C451FA` | `LayoutActiveTextEntryChainForWindow` |
| 235 | C4:54F2 | C4:550E | 28 | `exact` | yes | `data/text/battle_to_text.asm` | `BATTLE_TO_TEXT` | `` |
| 236 | C4:550E | C4:5637 | 297 | `exact` | yes | `data/text/battle_front_row_text.asm` | `BATTLE_FRONT_ROW_TEXT` | `` |
| 237 | C4:5637 | C4:577D | 326 | `exact` | yes | `data/text/battle_back_row_text.asm` | `BATTLE_BACK_ROW_TEXT` | `` |
| 238 | C4:577D | C4:58AB | 302 | `exact` | yes | `data/text/CC_1C_01_data.asm` | `` | `` |
| 239 | C4:58AB | C4:58AF | 4 | `exact` | yes | `data/powers_of_two_8.asm` | `` | `` |
| 240 | C4:58AF | C4:5963 | 180 | `exact` | yes | `misc/find_item_in_inventory.asm` | `` | `` |
| 241 | C4:5963 | C4:599A | 55 | `exact` | yes | `misc/find_item_in_inventory2.asm` | `FIND_ITEM_IN_INVENTORY2` | `` |
| 242 | C4:599A | C4:5A27 | 141 | `exact` | yes | `misc/find_inventory_space.asm` | `` | `` |
| 243 | C4:5A27 | C4:5C90 | 617 | `exact` | yes | `misc/find_inventory_space2.asm` | `FIND_INVENTORY_SPACE2` | `` |
| 244 | C4:5C90 | C4:5DDD | 333 | `exact` | yes | `misc/change_equipped_weapon.asm` | `UNKNOWN_C45C90` | `RenderMaskedGlyphRunToMenuScratchRows` |
| 245 | C4:5DDD | C4:5E96 | 185 | `exact` | yes | `misc/change_equipped_body.asm` | `UNKNOWN_C45DDD` | `FlushMenuGlyphScratchRowsToVram` |
| 246 | C4:5E96 | C4:5ECE | 56 | `exact` | yes | `misc/change_equipped_arms.asm` | `UNKNOWN_C45E96` | `ResetGlyphScratchAndAdvanceUploadCursor` |
| 247 | C4:5ECE | C4:5F7B | 173 | `exact` | yes | `misc/change_equipped_other.asm` | `CHANGE_EQUIPPED_OTHER` | `` |
| 248 | C4:5F7B | C4:5F96 | 27 | `exact` | yes | `data/item_usable_flags.asm` | `ITEM_USABLE_FLAGS` | `` |
| 249 | C4:5F96 | C4:5FA8 | 18 | `exact` | yes | `misc/check_status_group.asm` | `CHECK_STATUS_GROUP` | `` |
| 250 | C4:5FA8 | C4:6028 | 128 | `exact` | yes | `misc/inflict_status_nonbattle.asm` | `INFLICT_STATUS_NONBATTLE` | `` |
| 251 | C4:6028 | C4:645A | 1074 | `exact` | yes | `data/battle/misc_target_text.asm` | `UNKNOWN_C46028` | `FindEntitySlotByCachedPoseDescriptorId` |
| 252 | C4:645A | C4:6A5E | 1540 | `exact` | yes | `data/text/phone_call_text.asm` | `UNKNOWN_C4645A` | `ClearRegistryEntitySlotsFlag8000` |
| 253 | C4:6A5E | C4:6A6E | 16 | `exact` | yes | `misc/get_required_exp.asm` | `UNKNOWN_C46A5E` | `PlayerDirection987fTurnBiasTable` |
| 254 | C4:6A6E | C4:6A7A | 12 | `exact` | yes | `data/text/status_equip_window_text.asm` | `UNKNOWN_C46A6E` | `MapPlayerDirection987fToTurnBias` |
| 255 | C4:6A7A | C4:6A8A | 16 | `exact` | yes | `data/homesickness_probabilities.asm` | `UNKNOWN_C46A7A` | `DirectionOctantToAltFacingQuadrantTable` |
| 256 | C4:5C90 | C4:5DDD | 333 | `exact` | yes | `unknown/C4/C45C90.asm` | `UNKNOWN_C45C90` | `RenderMaskedGlyphRunToMenuScratchRows` |
| 257 | C4:5DDD | C4:5E96 | 185 | `exact` | yes | `unknown/C4/C45DDD.asm` | `UNKNOWN_C45DDD` | `FlushMenuGlyphScratchRowsToVram` |
| 258 | C4:5E96 | C4:5ECE | 56 | `exact` | yes | `unknown/C4/C45E96.asm` | `UNKNOWN_C45E96` | `ResetGlyphScratchAndAdvanceUploadCursor` |
| 259 | C4:5ECE | C4:5F7B | 173 | `exact` | yes | `misc/check_if_psi_known.asm` | `CHECK_IF_PSI_KNOWN` | `` |
| 260 | C4:5F7B | C4:5F96 | 27 | `exact` | yes | `system/math/rand_mod.asm` | `RAND_MOD` | `` |
| 261 | C4:5F96 | C4:5FA8 | 18 | `exact` | yes | `data/map/direction_matrix.asm` | `DIRECTION_MATRIX` | `` |
| 262 | C4:5FA8 | C4:6028 | 128 | `exact` | yes | `overworld/get_direction_to.asm` | `GET_DIRECTION_TO` | `` |
| 263 | C4:6028 | C4:645A | 1074 | `exact` | yes | `unknown/C4/C46028.asm` | `UNKNOWN_C46028` | `FindEntitySlotByCachedPoseDescriptorId` |
| 264 | C4:605A | C4:608C | 50 | `exact` | yes | `unknown/C4/C4605A.asm` | `UNKNOWN_C4605A` | `FindEntitySlotByVisualTypeId` |
| 265 | C4:608C | C4:60CE | 66 | `exact` | yes | `unknown/C4/C4608C.asm` | `UNKNOWN_C4608C` | `ResolveEntitySlotFromOverworldTypeRegistryCode` |
| 266 | C4:60CE | C4:6125 | 87 | `exact` | yes | `unknown/C4/C460CE.asm` | `UNKNOWN_C460CE` | `RunVisualTypeEntityScriptWithCachedPose` |
| 267 | C4:6125 | C4:617C | 87 | `exact` | yes | `unknown/C4/C46125.asm` | `UNKNOWN_C46125` | `RunPoseDescriptorEntityScriptWithCachedPose` |
| 268 | C4:617C | C4:61CC | 80 | `exact` | yes | `unknown/C4/C4617C.asm` | `UNKNOWN_C4617C` | `RunVisualTypeEntityScriptFromRecordC4c4d4` |
| 269 | C4:61CC | C4:621C | 80 | `exact` | yes | `unknown/C4/C461CC.asm` | `UNKNOWN_C461CC` | `RunPoseDescriptorEntityScriptFromRecordC4c4d4` |
| 270 | C4:621C | C4:6257 | 59 | `exact` | yes | `unknown/C4/C4621C.asm` | `` | `ResolveEntitySlotBySelectorMode` |
| 271 | C4:6257 | C4:62AE | 87 | `exact` | yes | `unknown/C4/C46257.asm` | `UNKNOWN_C46257` | `ComputeRoundedOctantBetweenResolvedEntities` |
| 272 | C4:62AE | C4:62C9 | 27 | `exact` | yes | `unknown/C4/C462AE.asm` | `UNKNOWN_C462AE` | `ComputeVisualTypeEntityFacingOctantToTarget` |
| 273 | C4:62C9 | C4:62E4 | 27 | `exact` | yes | `unknown/C4/C462C9.asm` | `UNKNOWN_C462C9` | `ComputePoseDescriptorEntityFacingOctantToTarget` |
| 274 | C4:62E4 | C4:62FF | 27 | `exact` | yes | `unknown/C4/C462E4.asm` | `UNKNOWN_C462E4` | `ComputeRegistryEntityFacingOctantToTarget` |
| 275 | C4:62FF | C4:6331 | 50 | `exact` | yes | `unknown/C4/C462FF.asm` | `UNKNOWN_C462FF` | `UpdateEntityFrameSelectorByVisualTypeId` |
| 276 | C4:6331 | C4:6363 | 50 | `exact` | yes | `unknown/C4/C46331.asm` | `UNKNOWN_C46331` | `UpdateEntityFrameSelectorByPoseDescriptorId` |
| 277 | C4:6363 | C4:6397 | 52 | `exact` | yes | `unknown/C4/C46363.asm` | `UNKNOWN_C46363` | `UpdateEntityFrameSelectorByRegistryTypeCode` |
| 278 | C4:6397 | C4:63F4 | 93 | `exact` | yes | `unknown/C4/C46397.asm` | `UNKNOWN_C46397` | `BroadcastRegistryEntityFrameSelectorUpdate` |
| 279 | C4:63F4 | C4:645A | 102 | `exact` | yes | `unknown/C4/C463F4.asm` | `UNKNOWN_C463F4` | `MarkRegistryEntitySlotsFlag8000` |
| 280 | C4:645A | C4:6A5E | 1540 | `exact` | yes | `unknown/C4/C4645A.asm` | `UNKNOWN_C4645A` | `ClearRegistryEntitySlotsFlag8000` |
| 281 | C4:6A5E | C4:6A6E | 16 | `exact` | yes | `overworld/create_prepared_entity_npc.asm` | `UNKNOWN_C46A5E` | `PlayerDirection987fTurnBiasTable` |
| 282 | C4:6A6E | C4:6A7A | 12 | `exact` | yes | `overworld/create_prepared_entity_sprite.asm` | `UNKNOWN_C46A6E` | `MapPlayerDirection987fToTurnBias` |
| 283 | C4:6534 | C4:655E | 42 | `exact` | yes | `unknown/C4/C46534.asm` | `UNKNOWN_C46534` | `SpawnEntityAtCurrentSlotAnchor` |
| 284 | C4:655E | C4:6579 | 27 | `exact` | yes | `unknown/C4/C4655E.asm` | `UNKNOWN_C4655E` | `SetVisualTypeSlotFlagsC000` |
| 285 | C4:6579 | C4:6594 | 27 | `exact` | yes | `unknown/C4/C46579.asm` | `UNKNOWN_C46579` | `SetPoseDescriptorSlotFlagsC000` |
| 286 | C4:6594 | C4:65FB | 103 | `exact` | yes | `unknown/C4/C46594.asm` | `UNKNOWN_C46594` | `SetRegistrySlotFlagsC000` |
| 287 | C4:65FB | C4:6616 | 27 | `exact` | yes | `unknown/C4/C465FB.asm` | `UNKNOWN_C465FB` | `ClearVisualTypeSlotFlagsC000` |
| 288 | C4:6616 | C4:6631 | 27 | `exact` | yes | `unknown/C4/C46616.asm` | `UNKNOWN_C46616` | `ClearPoseDescriptorSlotFlagsC000` |
| 289 | C4:6631 | C4:6698 | 103 | `exact` | yes | `unknown/C4/C46631.asm` | `UNKNOWN_C46631` | `ClearRegistrySlotFlagsC000` |
| 290 | C4:6698 | C4:66A8 | 16 | `exact` | yes | `unknown/C4/C46698.asm` | `UNKNOWN_C46698` | `SelectModeSlotByVisualTypeId` |
| 291 | C4:66A8 | C4:66B8 | 16 | `exact` | yes | `unknown/C4/C466A8.asm` | `UNKNOWN_C466A8` | `SelectModeSlotByPoseDescriptorId` |
| 292 | C4:66B8 | C4:66C1 | 9 | `exact` | yes | `unknown/C4/C466B8.asm` | `UNKNOWN_C466B8` | `ClearSelectedModeSlot` |
| 293 | C4:66C1 | C4:66F0 | 47 | `exact` | yes | `unknown/C4/C466C1.asm` | `UNKNOWN_C466C1` | `RunWanderingPhotographerScriptForPhotoIndex` |
| 294 | C4:66F0 | C4:6712 | 34 | `exact` | yes | `unknown/C4/C466F0.asm` | `UNKNOWN_C466F0` | `ExecuteNestedTextPointerFromAx` |
| 295 | C4:6712 | C4:675C | 74 | `exact` | yes | `unknown/C4/C46712.asm` | `UNKNOWN_C46712` | `SetLeadAndCompanionRegistryVisualFlags` |
| 296 | C4:675C | C4:67B4 | 88 | `exact` | yes | `unknown/C4/C4675C.asm` | `UNKNOWN_C4675C` | `ClearLeadAndCompanionRegistryVisualFlags` |
| 297 | C4:67B4 | C4:67C2 | 14 | `exact` | yes | `unknown/C4/C467B4.asm` | `UNKNOWN_C467B4` | `RandomDelay0cTo2b` |
| 298 | C4:67C2 | C4:67E6 | 36 | `exact` | yes | `unknown/C4/C467C2.asm` | `UNKNOWN_C467C2` | `RandomDelayBiasedByCurrentDrawY` |
| 299 | C4:67E6 | C4:681A | 52 | `exact` | yes | `unknown/C4/C467E6.asm` | `UNKNOWN_C467E6` | `ClearFlagsForPose016fEntities` |
| 300 | C4:681A | C4:6881 | 103 | `exact` | yes | `unknown/C4/C4681A.asm` | `UNKNOWN_C4681A` | `QueueCurrentVisualTypeMovementScript` |
| 301 | C4:6881 | C4:68A9 | 40 | `exact` | yes | `unknown/C4/C46881.asm` | `UNKNOWN_C46881` | `SetAllRegistryFlagsAndQueueCallerMovement` |
| 302 | C4:68A9 | C4:68AF | 6 | `exact` | yes | `unknown/C4/C468A9.asm` | `UNKNOWN_C468A9` | `ReadInputState006d` |
| 303 | C4:68AF | C4:68B5 | 6 | `exact` | yes | `unknown/C4/C468AF.asm` | `UNKNOWN_C468AF` | `ReadInputState0065` |
| 304 | C4:68B5 | C4:68DC | 39 | `exact` | yes | `unknown/C4/C468B5.asm` | `UNKNOWN_C468B5` | `TestValueLeftOfCurrentAnchorX` |
| 305 | C4:68DC | C4:6903 | 39 | `exact` | yes | `unknown/C4/C468DC.asm` | `UNKNOWN_C468DC` | `TestValueAboveCurrentAnchorY` |
| 306 | C4:6903 | C4:6914 | 17 | `exact` | yes | `unknown/C4/C46903.asm` | `UNKNOWN_C46903` | `TestValueBelowPlayerY` |
| 307 | C4:6914 | C4:6957 | 67 | `exact` | yes | `unknown/C4/C46914.asm` | `UNKNOWN_C46914` | `GetCurrentVisualTypeRecordByte03` |
| 308 | C4:6957 | C4:6984 | 45 | `exact` | yes | `unknown/C4/C46957.asm` | `UNKNOWN_C46957` | `UpdateCurrentSlotFrameSelector` |
| 309 | C4:6984 | C4:69F1 | 109 | `exact` | yes | `unknown/C4/C46984.asm` | `UNKNOWN_C46984` | `FaceVisualTypeSlotTowardCurrentSlot` |
| 310 | C4:69F1 | C4:6A5E | 109 | `exact` | yes | `unknown/C4/C469F1.asm` | `UNKNOWN_C469F1` | `FacePoseDescriptorSlotTowardCurrentSlot` |
| 311 | C4:6A5E | C4:6A6E | 16 | `exact` | yes | `data/unknown/C46A5E.asm` | `UNKNOWN_C46A5E` | `PlayerDirection987fTurnBiasTable` |
| 312 | C4:6A6E | C4:6A7A | 12 | `exact` | yes | `unknown/C4/C46A6E.asm` | `UNKNOWN_C46A6E` | `MapPlayerDirection987fToTurnBias` |
| 313 | C4:6A7A | C4:6A8A | 16 | `exact` | yes | `data/unknown/C46A7A.asm` | `UNKNOWN_C46A7A` | `DirectionOctantToAltFacingQuadrantTable` |
| 314 | C4:6A8A | C4:6A9A | 16 | `exact` | yes | `data/unknown/C46A8A.asm` | `` | `DirectionOctantToSpriteFacingQuadrantTable` |
| 315 | C4:6A9A | C4:6B41 | 167 | `exact` | yes | `unknown/C4/C46A9A.asm` | `UNKNOWN_C46A9A` | `MapOctantToAltFacingQuadrant` |
| 316 | C4:6AA3 | C4:6AAC | 9 | `exact` | yes | `unknown/C4/C46AA3.asm` | `UNKNOWN_C46AA3` | `MapOctantToSpriteFacingQuadrant` |
| 317 | C4:6AAC | C4:6ADB | 47 | `exact` | yes | `unknown/C4/C46AAC.asm` | `UNKNOWN_C46AAC` | `ComputeCurrentSlotSignDeltaTargetDirection` |
| 318 | C4:6ADB | C4:6B0A | 47 | `exact` | yes | `unknown/C4/C46ADB.asm` | `UNKNOWN_C46ADB` | `ComputeCurrentSlotTargetDirectionOctant` |
| 319 | C4:6B0A | C4:6B2D | 35 | `exact` | yes | `unknown/C4/C46B0A.asm` | `UNKNOWN_C46B0A` | `RoundAngleToOctantAndCacheCurrentSlot` |
| 320 | C4:6B2D | C4:6B37 | 10 | `exact` | yes | `unknown/C4/C46B2D.asm` | `UNKNOWN_C46B2D` | `FloorAngleToDirectionOctant` |
| 321 | C4:6B37 | C4:6B41 | 10 | `exact` | yes | `unknown/C4/C46B37.asm` | `UNKNOWN_C46B37` | `RotateDirectionOctantHalfTurn` |
| 322 | C4:6B41 | C4:6B51 | 16 | `exact` | yes | `data/unknown/C46B41.asm` | `UNKNOWN_C46B41` | `RoundedAngleToWalkDirectionTable` |
| 323 | C4:6B51 | C4:6C45 | 244 | `exact` | yes | `unknown/C4/C46B51.asm` | `UNKNOWN_C46B51` | `RoundAngleToWalkDirectionStep` |
| 324 | C4:6B65 | C4:6B79 | 20 | `exact` | yes | `unknown/C4/C46B65.asm` | `UNKNOWN_C46B65` | `SetCurrentSlotTargetToPlayerPosition` |
| 325 | C4:6B79 | C4:6B8D | 20 | `exact` | yes | `unknown/C4/C46B79.asm` | `UNKNOWN_C46B79` | `SetCurrentSlotTargetTo9e2dPosition` |
| 326 | C4:6B8D | C4:6BBB | 46 | `exact` | yes | `unknown/C4/C46B8D.asm` | `UNKNOWN_C46B8D` | `SetCurrentSlotTargetToVisualTypeSlotPosition` |
| 327 | C4:6BBB |  | 0 | `open` |  | `unknown/C4/C46BBB.asm` | `UNKNOWN_C46BBB` | `SetCurrentSlotTargetToPoseDescriptorSlotPosition` |
| 328 |  |  | 0 | `open` |  | `overworld/get_position_of_party_member.asm` | `GET_POSITION_OF_PARTY_MEMBER` | `` |
| 329 | C4:6C45 | C4:6D4B | 262 | `exact` | yes | `unknown/C4/C46C45.asm` | `UNKNOWN_C46C45` | `SnapshotCurrentSlotAnchorToStagedPosition` |
| 330 | C4:6C5E | C4:6C87 | 41 | `exact` | yes | `unknown/C4/C46C5E.asm` | `UNKNOWN_C46C5E` | `SetStagedPositionOffsetFromCurrentAnchor` |
| 331 | C4:6C87 | C4:6C9B | 20 | `exact` | yes | `unknown/C4/C46C87.asm` | `UNKNOWN_C46C87` | `RestoreCurrentSlotAnchorFromCachedTarget` |
| 332 | C4:6C9B | C4:6CC7 | 44 | `exact` | yes | `unknown/C4/C46C9B.asm` | `UNKNOWN_C46C9B` | `CopyRegistrySlotAnchorToCurrentSlot` |
| 333 | C4:6CC7 | C4:6CF5 | 46 | `exact` | yes | `unknown/C4/C46CC7.asm` | `UNKNOWN_C46CC7` | `CopyPoseDescriptorSlotAnchorToCurrentSlot` |
| 334 | C4:6CF5 | C4:6D23 | 46 | `exact` | yes | `unknown/C4/C46CF5.asm` | `UNKNOWN_C46CF5` | `SetCurrentSlotCameraRelativeAnchorWithFlags` |
| 335 | C4:6D23 | C4:6D4B | 40 | `exact` | yes | `unknown/C4/C46D23.asm` | `UNKNOWN_C46D23` | `PlaceCurrentSlotAtRandomCameraXPlus70Y` |
| 336 | C4:6D4B | C4:6EF8 | 429 | `exact` | yes | `unknown/C4/C46D4B.asm` | `UNKNOWN_C46D4B` | `PlaceCurrentSlotFromPhotoSceneRecord` |
| 337 | C4:6EF8 | C4:7369 | 1137 | `exact` | yes | `overworld/prepare_new_entity_at_existing_entity_location.asm` | `UNKNOWN_C46EF8` | `CheckCurrentSlotWithinPlayerProximityThreshold` |
| 338 | C4:7369 | C4:7370 | 7 | `exact` | yes | `overworld/prepare_new_entity_at_teleport_destination.asm` | `UNKNOWN_C47369` | `RefreshMapStripsAroundCameraFarWrapper` |
| 339 | C4:7370 | C4:74F6 | 390 | `exact` | yes | `overworld/prepare_new_entity.asm` | `PREPARE_NEW_ENTITY` | `` |
| 340 | C4:6E46 | C4:6E4F | 9 | `exact` | yes | `unknown/C4/C46E46.asm` | `UNKNOWN_C46E46` | `SetYieldToTextLatch9641` |
| 341 | C4:6E4F |  | 0 | `open` |  | `unknown/C4/C46E4F.asm` | `UNKNOWN_C46E4F` | `QueueEventTextPointerRecord8` |
| 342 |  |  | 0 | `open` |  | `overworld/actionscript/test_player_in_area.asm` | `TEST_PLAYER_IN_AREA` | `` |
| 343 | C4:6EF8 | C4:7369 | 1137 | `exact` | yes | `unknown/C4/C46EF8.asm` | `UNKNOWN_C46EF8` | `CheckCurrentSlotWithinPlayerProximityThreshold` |
| 344 | C4:6F7C | C4:7044 | 200 | `exact` | yes | `unknown/C4/C46F7C.asm` | `UNKNOWN_C46F7C` | `StepCurrentSlotTowardCachedTargetOrReportArrival` |
| 345 | C4:7044 | C4:7143 | 255 | `exact` | yes | `unknown/C4/C47044.asm` | `UNKNOWN_C47044` | `ProjectAngleIntoCurrentSlotVectorWords` |
| 346 | C4:7143 | C4:7225 | 226 | `exact` | yes | `unknown/C4/C47143.asm` | `UNKNOWN_C47143` | `StepCurrentSlotTargetVectorByAngleModes` |
| 347 | C4:7225 | C4:7269 | 68 | `exact` | yes | `unknown/C4/C47225.asm` | `UNKNOWN_C47225` | `SetCurrentSlotAreaBoundsFromRadii` |
| 348 | C4:7269 | C4:72A8 | 63 | `exact` | yes | `unknown/C4/C47269.asm` | `UNKNOWN_C47269` | `ClassifyCurrentSlotAgainstAreaBounds` |
| 349 | C4:72A8 | C4:730E | 102 | `exact` | yes | `unknown/C4/C472A8.asm` | `UNKNOWN_C472A8` | `ProjectSlot0e5eAngleAndRefreshFacing` |
| 350 | C4:730E | C4:7333 | 37 | `exact` | yes | `unknown/C4/C4730E.asm` | `UNKNOWN_C4730E` | `HalveCurrentSlot0d32PreserveSign` |
| 351 | C4:7333 | C4:733C | 9 | `exact` | yes | `unknown/C4/C47333.asm` | `UNKNOWN_C47333` | `ReadActiveOverworldRegistryCount` |
| 352 | C4:733C | C4:734C | 16 | `exact` | yes | `unknown/C4/C4733C.asm` | `UNKNOWN_C4733C` | `DispatchCurrentLandingProfileAction` |
| 353 | C4:734C | C4:7369 | 29 | `exact` | yes | `unknown/C4/C4734C.asm` | `UNKNOWN_C4734C` | `RefreshMapStripForIndexPreserveA` |
| 354 | C4:7369 | C4:7370 | 7 | `exact` | yes | `unknown/C4/C47369.asm` | `UNKNOWN_C47369` | `RefreshMapStripsAroundCameraFarWrapper` |
| 355 | C4:7370 | C4:74F6 | 390 | `exact` | yes | `system/load_background_animation.asm` | `LOAD_BACKGROUND_ANIMATION` | `` |
| 356 | C4:73B2 | C4:73D0 | 30 | `exact` | yes | `unknown/C4/C473B2.asm` | `` | `ClampSignedPaletteComponentTo5Bit` |
| 357 | C4:73D0 | C4:746B | 155 | `exact` | yes | `unknown/C4/C473D0.asm` | `` | `ApplySignedBrightnessOffsetToPaletteRow` |
| 358 | C4:746B | C4:7499 | 46 | `exact` | yes | `unknown/C4/C4746B.asm` | `UNKNOWN_C4746B` | `ApplySignedBrightnessOffsetToPaletteRowsAndUpload` |
| 359 | C4:7499 | C4:74A8 | 15 | `exact` | yes | `unknown/C4/C47499.asm` | `UNKNOWN_C47499` | `ApplyCurrentSlot0e5eBrightnessToPaletteRows` |
| 360 | C4:74A8 | C4:74F6 | 78 | `exact` | yes | `unknown/C4/C474A8.asm` | `UNKNOWN_C474A8` | `ApplyCurrentSlot0e5eFixedColorMath` |
| 361 | C4:74F6 | C4:7501 | 11 | `exact` | yes | `data/unknown/C474F6.asm` | `UNKNOWN_C474F6` | `WhWindowSpanRadiusRampTable` |
| 362 | C4:7501 | C4:7C3F | 1854 | `exact` | yes | `unknown/C4/C47501.asm` | `` | `WriteCurrentEntityWhWindowSpan` |
| 363 | C4:76A5 | C4:7705 | 96 | `exact` | yes | `unknown/C4/C476A5.asm` | `UNKNOWN_C476A5` | `StageCurrentEntityWh0MaskAndStartHdma` |
| 364 | C4:7705 | C4:7765 | 96 | `exact` | yes | `unknown/C4/C47705.asm` | `UNKNOWN_C47705` | `StageCurrentEntityWh2MaskAndStartHdma` |
| 365 | C4:7765 | C4:7866 | 257 | `exact` | yes | `unknown/C4/C47765.asm` | `UNKNOWN_C47765` | `StageMosaicFadeWh0MaskAndStartHdma` |
| 366 | C4:7866 | C4:789E | 56 | `exact` | yes | `unknown/C4/C47866.asm` | `` | `ClampCoordToUnsignedLimit` |
| 367 | C4:789E | C4:7930 | 146 | `exact` | yes | `unknown/C4/C4789E.asm` | `` | `AppendWhWindowRunDescriptor` |
| 368 | C4:7930 | C4:79E9 | 185 | `exact` | yes | `unknown/C4/C47930.asm` | `UNKNOWN_C47930` | `StageWh0BoxMaskAndStartHdma` |
| 369 | C4:79E9 | C4:7A27 | 62 | `exact` | yes | `unknown/C4/C479E9.asm` | `UNKNOWN_C479E9` | `StageCurrentEntityCenteredWh0BoxMask` |
| 370 | C4:7A27 | C4:7A6B | 68 | `exact` | yes | `unknown/C4/C47A27.asm` | `UNKNOWN_C47A27` | `StageBaseSlotRelativeWh0BoxMask` |
| 371 | C4:7A6B | C4:7A9E | 51 | `exact` | yes | `unknown/C4/C47A6B.asm` | `UNKNOWN_C47A6B` | `MirrorCurrentEntityYAroundTarget1002` |
| 372 | C4:7A9E | C4:7B77 | 217 | `exact` | yes | `unknown/C4/C47A9E.asm` | `UNKNOWN_C47A9E` | `LoadCurrentEntityIndexedWindowGfxToVram` |
| 373 | C4:7B77 |  | 0 | `open` |  | `unknown/C4/C47B77.asm` | `UNKNOWN_C47B77` | `LoadIndexedWindowGfxAndReadVariantByte` |
| 374 |  |  | 0 | `open` |  | `system/load_window_gfx.asm` | `LOAD_WINDOW_GFX` | `` |
| 375 | C4:7F87 |  | 0 | `open` |  | `unknown/C4/C47F87.asm` | `UNKNOWN_C47F87` | `RefreshWindowFlavourPaletteBlock` |
| 376 |  |  | 0 | `open` |  | `text/undraw_flyover_text.asm` | `UNDRAW_FLYOVER_TEXT` | `` |
| 377 |  |  | 0 | `open` |  | `data/text/lumine_hall.asm` | `` | `` |
| 378 | C4:810E | C4:827B | 365 | `exact` | yes | `unknown/C4/C4810E.asm` | `UNKNOWN_C4810E` | `ExpandEvent353TileCellTo7fRows` |
| 379 | C4:827B | C4:838A | 271 | `exact` | yes | `unknown/C4/C4827B.asm` | `UNKNOWN_C4827B` | `DrawEvent353EncodedGlyphTo3492` |
| 380 | C4:838A | C4:880C | 1154 | `exact` | yes | `unknown/C4/C4838A.asm` | `UNKNOWN_C4838A` | `BuildEvent353MessageTileBuffer` |
| 381 | C4:880C | C4:8A6D | 609 | `exact` | yes | `unknown/C4/C4880C.asm` | `UNKNOWN_C4880C` | `InitEvent353MessageTileReveal` |
| 382 | C4:8A6D | C4:8B2C | 191 | `exact` | yes | `unknown/C4/C48A6D.asm` | `UNKNOWN_C48A6D` | `StepEvent353MessageTileReveal` |
| 383 | C4:8B2C | C4:8B3B | 15 | `exact` | yes | `unknown/C4/C48B2C.asm` | `UNKNOWN_C48B2C` | `SetTeleportEvent670LandingMode` |
| 384 | C4:8B3B | C4:8BDA | 159 | `exact` | yes | `overworld/actionscript/make_party_look_at_active_entity.asm` | `MAKE_PARTY_LOOK_AT_ACTIVE_ENTITY` | `` |
| 385 | C4:8BDA | C4:8BE1 | 7 | `exact` | yes | `overworld/actionscript/animated_background_callback.asm` | `ACTIONSCRIPT_ANIMATED_BACKGROUND_CALLBACK` | `` |
| 386 | C4:8BE1 | C4:8C02 | 33 | `exact` | yes | `overworld/actionscript/simple_screen_position_callback.asm` | `ACTIONSCRIPT_SIMPLE_SCREEN_POSITION_CALLBACK` | `` |
| 387 | C4:8C02 | C4:8C2B | 41 | `exact` | yes | `overworld/actionscript/simple_screen_position_callback_offset.asm` | `ACTIONSCRIPT_SIMPLE_SCREEN_POSITION_CALLBACK_OFFSET` | `` |
| 388 | C4:8C2B | C4:8C3E | 19 | `exact` | yes | `overworld/actionscript/centre_screen_on_entity_callback.asm` | `ACTIONSCRIPT_CENTRE_SCREEN_ON_ENTITY_CALLBACK` | `` |
| 389 | C4:8C3E | C4:8C59 | 27 | `exact` | yes | `overworld/actionscript/centre_screen_on_entity_callback_offset.asm` | `ACTIONSCRIPT_CENTRE_SCREEN_ON_ENTITY_CALLBACK_OFFSET` | `` |
| 390 | C4:8C59 | C4:8C69 | 16 | `exact` | yes | `data/unknown/C48C59.asm` | `UNKNOWN_C48C59` | `MovementOctantToPulseSelectorTable` |
| 391 | C4:8C69 | C4:8C97 | 46 | `exact` | yes | `unknown/C4/C48C69.asm` | `UNKNOWN_C48C69` | `ClearMovementPulseAccumulator` |
| 392 | C4:8C97 | C4:8D38 | 161 | `exact` | yes | `unknown/C4/C48C97.asm` | `UNKNOWN_C48C97` | `AppendMovementPulseSelectorRun` |
| 393 | C4:8D38 | C4:8D58 | 32 | `exact` | yes | `data/unknown/C48D38.asm` | `UNKNOWN_C48D38` | `MovementOctantSignedUnitDeltaTable` |
| 394 | C4:8D58 | C4:8E6B | 275 | `exact` | yes | `unknown/C4/C48D58.asm` | `UNKNOWN_C48D58` | `BuildStagedMovementPulsesAndReturnDelay` |
| 395 | C4:8E6B | C4:8E95 | 42 | `exact` | yes | `unknown/C4/C48E6B.asm` | `UNKNOWN_C48E6B` | `AppendRepeatedMovementPulseSelector` |
| 396 | C4:8E95 | C4:8ECE | 57 | `exact` | yes | `unknown/C4/C48E95.asm` | `UNKNOWN_C48E95` | `InstallGeneratedMovementPulseScript` |
| 397 | C4:8ECE | C4:8EEB | 29 | `exact` | yes | `overworld/is_valid_item_transformation.asm` | `IS_VALID_ITEM_TRANSFORMATION` | `CheckTrackedItemPulseSlotActive` |
| 398 | C4:8EEB | C4:8F98 | 173 | `exact` | yes | `overworld/initialize_item_transformation.asm` | `INITIALIZE_ITEM_TRANSFORMATION` | `ArmTrackedItemPulseSlotFromD5f4bb` |
| 399 | C4:8F98 | C4:8FC4 | 44 | `exact` | yes | `unknown/C4/C48F98.asm` | `UNKNOWN_C48F98` | `ClearTrackedItemPulseSlot` |
| 400 | C4:8FC4 | C4:90EE | 298 | `exact` | yes | `overworld/process_item_transformations.asm` | `PROCESS_ITEM_TRANSFORMATIONS` | `StepTrackedItemPulseSlots` |
| 401 | C4:90EE | C4:91EE | 256 | `exact` | yes | `overworld/get_distance_to_magic_truffle.asm` | `GET_DISTANCE_TO_MAGIC_TRUFFLE` | `` |
| 402 | C4:91EE | C4:9208 | 26 | `exact` | yes | `system/get_colour_fade_slope.asm` | `` | `` |
| 403 | C4:9208 | C4:92D2 | 202 | `exact` | yes | `overworld/initialize_map_palette_fade.asm` | `INITIALIZE_MAP_PALETTE_FADE` | `BuildLandingInterpolationPlanesFrom7f7800` |
| 404 | C4:92D2 | C4:939C | 202 | `exact` | yes | `unknown/C4/C492D2.asm` | `UNKNOWN_C492D2` | `StepLandingProfile7900ColorPlanesTo0240` |
| 405 | C4:939C | C4:9496 | 250 | `exact` | yes | `unknown/C4/C4939C.asm` | `UNKNOWN_C4939C` | `RunLandingProfileDisplayBuildAndFade` |
| 406 | C4:9496 | C4:954C | 182 | `exact` | yes | `unknown/C4/C49496.asm` | `` | `ScalePackedRgb555ColorByStep` |
| 407 | C4:954C | C4:958E | 66 | `exact` | yes | `unknown/C4/C4954C.asm` | `UNKNOWN_C4954C` | `BuildScaledPaletteBlockTo7f0000` |
| 408 | C4:958E | C4:96E7 | 345 | `exact` | yes | `unknown/C4/C4958E.asm` | `` | `BuildLandingPaletteInterpolationPlanes` |
| 409 | C4:96E7 | C4:96F0 | 9 | `exact` | yes | `unknown/C4/C496E7.asm` | `UNKNOWN_C496E7` | `InitLandingPalettePlanesFrom0200` |
| 410 | C4:96F0 | C4:96F9 | 9 | `exact` | yes | `unknown/C4/C496F0.asm` | `UNKNOWN_C496F0` | `InitLandingPalettePlanesFrom4476` |
| 411 | C4:96F9 | C4:9740 | 71 | `exact` | yes | `unknown/C4/C496F9.asm` | `UNKNOWN_C496F9` | `MirrorCgramShadow0200To7f0000` |
| 412 | C4:9740 | C4:978E | 78 | `exact` | yes | `unknown/C4/C49740.asm` | `UNKNOWN_C49740` | `ExportLandingPaletteAndQueueCgramUpload` |
| 413 | C4:978E | C4:97C0 | 50 | `exact` | yes | `unknown/C4/C4978E.asm` | `UNKNOWN_C4978E` | `CopyCgramShadow0200To4476` |
| 414 | C4:97C0 | C4:981F | 95 | `exact` | yes | `unknown/C4/C497C0.asm` | `UNKNOWN_C497C0` | `RunLandingPaletteFadeToScaledBlock` |
| 415 | C4:981F | C4:9841 | 34 | `exact` | yes | `unknown/C4/C4981F.asm` | `UNKNOWN_C4981F` | `CopyStaticVisualBlock0be8To7c00` |
| 416 | C4:9841 | C4:984B | 10 | `exact` | yes | `unknown/C4/C49841.asm` | `UNKNOWN_C49841` | `BeginCoffeeTeaBattleBgVisualState` |
| 417 | C4:984B | C4:9875 | 42 | `exact` | yes | `unknown/C4/C4984B.asm` | `` | `InvertCoffeeTeaTileBufferWords` |
| 418 | C4:9875 | C4:999B | 294 | `exact` | yes | `unknown/C4/C49875.asm` | `UNKNOWN_C49875` | `ApplyCoffeeTeaTileRowMask` |
| 419 | C4:999B | C4:9A4B | 176 | `exact` | yes | `unknown/C4/C4999B.asm` | `UNKNOWN_C4999B` | `DrawCoffeeTeaTileTokenRun` |
| 420 | C4:9A4B | C4:9A56 | 11 | `exact` | yes | `unknown/C4/C49A4B.asm` | `` | `WaitFrameAndUpdateBattleBgVisualState` |
| 421 | C4:9A56 | C4:9B6E | 280 | `exact` | yes | `unknown/C4/C49A56.asm` | `UNKNOWN_C49A56` | `InitCoffeeTeaTileBufferAndTransferState` |
| 422 | C4:9B6E | C4:9C56 | 232 | `exact` | yes | `unknown/C4/C49B6E.asm` | `UNKNOWN_C49B6E` | `UploadCoffeeTeaTileBufferWindow` |
| 423 | C4:9C56 | C4:9CA8 | 82 | `exact` | yes | `unknown/C4/C49C56.asm` | `UNKNOWN_C49C56` | `AdvanceCoffeeTeaTileScrollState` |
| 424 | C4:9CA8 | C4:9CC3 | 27 | `exact` | yes | `unknown/C4/C49CA8.asm` | `UNKNOWN_C49CA8` | `AdvanceCoffeeTeaRowRevealCursor` |
| 425 | C4:9CC3 | C4:9D16 | 83 | `exact` | yes | `unknown/C4/C49CC3.asm` | `UNKNOWN_C49CC3` | `RenderCoffeeTeaTokenString` |
| 426 | C4:9D16 | C4:9D1E | 8 | `exact` | yes | `unknown/C4/C49D16.asm` | `UNKNOWN_C49D16` | `RenderSingleCoffeeTeaTileToken` |
| 427 | C4:9D1E | C4:9D6A | 76 | `exact` | yes | `unknown/C4/C49D1E.asm` | `UNKNOWN_C49D1E` | `AdvanceCoffeeTeaVramOffsetByTileRow` |
| 428 | C4:9D6A | C4:9EA4 | 314 | `exact` | yes | `text/coffee_tea_scene.asm` | `` | `` |
| 429 | C4:9EA4 | C4:9EC4 | 32 | `exact` | yes | `data/text/flyover_text_pointers.asm` | `FLYOVER_TEXT_POINTERS` | `FlyoverIntroTextPointerTable` |
| 430 | C4:9EC4 | C4:9FE1 | 285 | `exact` | yes | `unknown/C4/C49EC4.asm` | `UNKNOWN_C49EC4` | `RunFlyoverIntroTextSceneByIndex` |
| 431 | C4:9FE1 | C4:A0CF | 238 | `exact` | yes | `data/text/battle_menu_text.asm` | `BATTLE_MENU_TEXT` | `` |
| 432 | C4:A0CF | C4:A15D | 142 | `exact` | yes | `data/battle/dead_targettable_actions.asm` | `DEAD_TARGETTABLE_ACTIONS` | `` |
| 433 | C4:A15D | C4:A1F2 | 149 | `exact` | yes | `battle/autohealing.asm` | `AUTOHEALING` | `` |
| 434 | C4:A1F2 | C4:A1F5 | 3 | `exact` | yes | `battle/autolifeup.asm` | `AUTOLIFEUP` | `` |
| 435 | C4:A1F5 | C4:A228 | 51 | `exact` | yes | `data/battle/battle_window_sizes.asm` | `BATTLE_WINDOW_SIZES` | `` |
| 436 | C4:A228 | C4:A279 | 81 | `exact` | yes | `battle/check_if_valid_target.asm` | `UNKNOWN_C4A228` | `StoreRankedBattlerTargetOrdinal` |
| 437 | C4:A228 | C4:A279 | 81 | `exact` | yes | `unknown/C4/C4A228.asm` | `UNKNOWN_C4A228` | `StoreRankedBattlerTargetOrdinal` |
| 438 | C4:A279 | C4:A377 | 254 | `exact` | yes | `data/powers_of_two_32.asm` | `` | `` |
| 439 | C4:A377 | C4:A591 | 538 | `exact` | yes | `data/battle/prayer_list.asm` | `UNKNOWN_C4A377` | `LoadGasStationIntroGraphicsAndTilemap` |
| 440 | C4:A591 | C4:A5CE | 61 | `exact` | yes | `data/battle/prayer_text_pointers.asm` | `UNKNOWN_C4A591` | `BattleBgStaticTransitionWaveTable` |
| 441 | C4:A5CE | C4:A5FA | 44 | `exact` | yes | `data/battle/giygas_death_static_transition_delays.asm` | `UNKNOWN_C4A5CE` | `BattleSwirlOverlayOpenMode0Script` |
| 442 | C4:A5FA | C4:A626 | 44 | `exact` | yes | `data/battle/final_giygas_prayer_noise_table.asm` | `UNKNOWN_C4A5FA` | `BattleSwirlOverlayOpenMode1Script` |
| 443 | C4:A377 | C4:A591 | 538 | `exact` | yes | `unknown/C4/C4A377.asm` | `UNKNOWN_C4A377` | `LoadGasStationIntroGraphicsAndTilemap` |
| 444 | C4:A591 | C4:A5CE | 61 | `exact` | yes | `data/unknown/C4A591.asm` | `UNKNOWN_C4A591` | `BattleBgStaticTransitionWaveTable` |
| 445 | C4:A5CE | C4:A5FA | 44 | `exact` | yes | `data/unknown/C4A5CE.asm` | `UNKNOWN_C4A5CE` | `BattleSwirlOverlayOpenMode0Script` |
| 446 | C4:A5FA | C4:A626 | 44 | `exact` | yes | `data/unknown/C4A5FA.asm` | `UNKNOWN_C4A5FA` | `BattleSwirlOverlayOpenMode1Script` |
| 447 | C4:A626 | C4:A652 | 44 | `exact` | yes | `data/unknown/C4A626.asm` | `UNKNOWN_C4A626` | `BattleSwirlOverlayCloseMode0Script` |
| 448 | C4:A652 | C4:A67E | 44 | `exact` | yes | `data/unknown/C4A652.asm` | `UNKNOWN_C4A652` | `BattleSwirlOverlayCloseModeNonzeroScript` |
| 449 | C4:A67E | C4:A7B0 | 306 | `exact` | yes | `unknown/C4/C4A67E.asm` | `UNKNOWN_C4A67E` | `StartBattleOverlayScriptState` |
| 450 | C4:A7B0 | C4:AC57 | 1191 | `exact` | yes | `unknown/C4/C4A7B0.asm` | `UNKNOWN_C4A7B0` | `StepBattleOverlayScriptState` |
| 451 | C4:AC57 | C4:ACCE | 119 | `exact` | yes | `data/unknown/C4AC57.asm` | `UNKNOWN_C4AC57` | `SoundStonePresentationEfPayloadPointerTable` |
| 452 | C4:ACCE | C4:B1B8 | 1258 | `exact` | yes | `data/sound_stone_unknown1.asm` | `` | `RunSoundStonePresentationSequence` |
| 453 | C4:B1B8 | C4:B26B | 179 | `exact` | yes | `data/sound_stone_unknown2.asm` | `` | `TransferLandingDisplayAssetSubpiecePair` |
| 454 | C4:B26B | C4:B329 | 190 | `exact` | yes | `data/sound_stone_unknown3.asm` | `` | `InitializeLandingDisplayStreamsAndChildAnchors` |
| 455 | C4:B329 | C4:B3D0 | 167 | `exact` | yes | `data/sound_stone_unknown4.asm` | `` | `AdjustChildEntityAnchorForParentGeometry` |
| 456 | C4:B3D0 | C4:B4BE | 238 | `exact` | yes | `data/sound_stone_unknown5.asm` | `` | `SpawnAttachedChildEntityFromParentSlot` |
| 457 | C4:B4BE | C4:B4FE | 64 | `exact` | yes | `data/sound_stone_unknown6.asm` | `UNKNOWN_C4B4BE` | `ClearAttachedChildEntitiesByParentSlot` |
| 458 | C4:B4FE | C4:B519 | 27 | `exact` | yes | `data/music/sound_stone_music.asm` | `UNKNOWN_C4B4FE` | `SpawnAttachedChildForRegistryTypeCode` |
| 459 | C4:B519 | C4:B524 | 11 | `exact` | yes | `data/sound_stone_unknown7.asm` | `UNKNOWN_C4B519` | `ClearAttachedChildForRegistryTypeCode` |
| 460 | C4:B524 | C4:B53F | 27 | `exact` | yes | `data/sound_stone_unknown8.asm` | `UNKNOWN_C4B524` | `SpawnAttachedChildForVisualTypeId` |
| 461 | C4:B53F | C4:B54A | 11 | `exact` | yes | `data/sound_stone_melody_flags.asm` | `UNKNOWN_C4B53F` | `ClearAttachedChildForVisualTypeId` |
| 462 | C4:B54A | C4:B565 | 27 | `exact` | yes | `overworld/use_sound_stone.asm` | `UNKNOWN_C4B54A` | `SpawnAttachedChildForPoseDescriptorId` |
| 463 | C4:B1B8 | C4:B26B | 179 | `exact` | yes | `unknown/C4/C4B1B8.asm` | `` | `TransferLandingDisplayAssetSubpiecePair` |
| 464 | C4:B26B | C4:B329 | 190 | `exact` | yes | `overworld/load_overlay_sprites.asm` | `LOAD_OVERLAY_SPRITES` | `InitializeLandingDisplayStreamsAndChildAnchors` |
| 465 | C4:B329 | C4:B3D0 | 167 | `exact` | yes | `unknown/C4/C4B329.asm` | `` | `AdjustChildEntityAnchorForParentGeometry` |
| 466 | C4:B3D0 | C4:B4BE | 238 | `exact` | yes | `text/spawn_floating_sprite.asm` | `SPAWN_FLOATING_SPRITE` | `SpawnAttachedChildEntityFromParentSlot` |
| 467 | C4:B4BE | C4:B4FE | 64 | `exact` | yes | `unknown/C4/C4B4BE.asm` | `UNKNOWN_C4B4BE` | `ClearAttachedChildEntitiesByParentSlot` |
| 468 | C4:B4FE | C4:B519 | 27 | `exact` | yes | `unknown/C4/C4B4FE.asm` | `UNKNOWN_C4B4FE` | `SpawnAttachedChildForRegistryTypeCode` |
| 469 | C4:B519 | C4:B524 | 11 | `exact` | yes | `unknown/C4/C4B519.asm` | `UNKNOWN_C4B519` | `ClearAttachedChildForRegistryTypeCode` |
| 470 | C4:B524 | C4:B53F | 27 | `exact` | yes | `unknown/C4/C4B524.asm` | `UNKNOWN_C4B524` | `SpawnAttachedChildForVisualTypeId` |
| 471 | C4:B53F | C4:B54A | 11 | `exact` | yes | `unknown/C4/C4B53F.asm` | `UNKNOWN_C4B53F` | `ClearAttachedChildForVisualTypeId` |
| 472 | C4:B54A | C4:B565 | 27 | `exact` | yes | `unknown/C4/C4B54A.asm` | `UNKNOWN_C4B54A` | `SpawnAttachedChildForPoseDescriptorId` |
| 473 | C4:B565 | C4:B570 | 11 | `exact` | yes | `unknown/C4/C4B565.asm` | `UNKNOWN_C4B565` | `ClearAttachedChildForPoseDescriptorId` |
| 474 | C4:B570 | C4:B57D | 13 | `exact` | yes | `unknown/C4/C4B570.asm` | `UNKNOWN_C4B570` | `SpawnDefaultAttachedChildForBaseSlot18` |
| 475 | C4:B57D | C4:B587 | 10 | `exact` | yes | `unknown/C4/C4B57D.asm` | `UNKNOWN_C4B57D` | `ClearDefaultAttachedChildForBaseSlot18` |
| 476 | C4:B587 | C4:B595 | 14 | `exact` | yes | `unknown/C4/C4B587.asm` | `` | `AllocPathSolverScratchWords` |
| 477 | C4:B595 | C4:B59F | 10 | `exact` | yes | `unknown/C4/C4B595.asm` | `UNKNOWN_C4B595` | `GetPathSolverScratchUsage` |
| 478 | C4:B59F | C4:B7A5 | 518 | `exact` | yes | `unknown/C4/C4B59F.asm` | `UNKNOWN_C4B59F` | `RunPathGridCandidateSolver` |
| 479 | C4:B7A5 | C4:B859 | 180 | `exact` | yes | `unknown/C4/C4B7A5.asm` | `` | `MarkPathGridBorderBlocked` |
| 480 | C4:B859 | C4:B923 | 202 | `exact` | yes | `unknown/C4/C4B859.asm` | `` | `SortPathCandidatePointersByGridPosition` |
| 481 | C4:B923 | C4:BAF6 | 467 | `exact` | yes | `unknown/C4/C4B923.asm` | `` | `MarkPathCandidateFootprintsInGrid` |
| 482 | C4:BAF6 | C4:BD9A | 676 | `exact` | yes | `unknown/C4/C4BAF6.asm` | `` | `PropagatePathGridCandidateRoutes` |
| 483 | C4:BD9A | C4:BF7F | 485 | `exact` | yes | `unknown/C4/C4BD9A.asm` | `` | `TracePathGridRouteIntoStepList` |
| 484 | C4:BF7F | C4:C05E | 223 | `exact` | yes | `unknown/C4/C4BF7F.asm` | `` | `CompressCollinearPathStepList` |
| 485 | C4:C05E | C4:C2DE | 640 | `exact` | yes | `data/text/file_select_text.asm` | `` | `` |
| 486 | C4:C2DE | C4:C45F | 385 | `exact` | yes | `unknown/C4/C4C2DE.asm` | `` | `InitializeSavedLandingDisplayState` |
| 487 | C4:C45F | C4:C519 | 186 | `exact` | yes | `unknown/C4/C4C45F.asm` | `` | `StageLandingPalettePhaseBlock` |
| 488 | C4:C519 | C4:C567 | 78 | `exact` | yes | `unknown/C4/C4C519.asm` | `` | `RunLandingPalettePhaseFadeFrames` |
| 489 | C4:C567 | C4:C58F | 40 | `exact` | yes | `text/skippable_pause.asm` | `` | `WaitFramesAbortOnInput006d` |
| 490 | C4:C58F | C4:C60E | 127 | `exact` | yes | `unknown/C4/C4C58F.asm` | `UNKNOWN_C4C58F` | `RunSavedLandingPaletteRestoreFadeFrames` |
| 491 | C4:C60E | C4:C64D | 63 | `exact` | yes | `unknown/C4/C4C60E.asm` | `UNKNOWN_C4C60E` | `RunSavedLandingPaletteWorldRefreshFadeFrames` |
| 492 | C4:C64D | C4:C718 | 203 | `exact` | yes | `unknown/C4/C4C64D.asm` | `` | `RunSavedLandingFadeSequence` |
| 493 | C4:C718 | C4:C8A4 | 396 | `exact` | yes | `overworld/spawn.asm` | `SPAWN` | `RunSavedCoordinateLandingReload` |
| 494 | C4:C8A4 | C4:C8DB | 55 | `exact` | yes | `unknown/C4/C4C8A4.asm` | `` | `InitVisualRecordTable7f7c00` |
| 495 | C4:C8DB | C4:C8E9 | 14 | `exact` | yes | `unknown/C4/C4C8DB.asm` | `` | `AllocVisualRecordScratchBytes` |
| 496 | C4:C8E9 | C4:C91A | 49 | `exact` | yes | `unknown/C4/C4C8E9.asm` | `` | `ClearVisualRecordScratchSpan7f` |
| 497 | C4:C91A | C4:CB4F | 565 | `exact` | yes | `unknown/C4/C4C91A.asm` | `UNKNOWN_C4C91A` | `AppendDynamicVisualRecord` |
| 498 | C4:CB4F | C4:CB8F | 64 | `exact` | yes | `unknown/C4/C4CB4F.asm` | `UNKNOWN_C4CB4F` | `ClearVisualRecordSlot4000Flags` |
| 499 | C4:CB8F | C4:CBE3 | 84 | `exact` | yes | `unknown/C4/C4CB8F.asm` | `UNKNOWN_C4CB8F` | `RefreshVisualRecordsAndClearState1Latch` |
| 500 | C4:CBE3 | C4:CC2C | 73 | `exact` | yes | `unknown/C4/C4CBE3.asm` | `UNKNOWN_C4CBE3` | `SetState1VisualRecordLatchFFFF` |
| 501 | C4:CC2C | C4:CC2F | 3 | `exact` | yes | `misc/null/C4CC2C.asm` | `UNKNOWN_C4CC2C` | `` |
| 502 | C4:CC2F | C4:CD44 | 277 | `exact` | yes | `unknown/C4/C4CC2F.asm` | `UNKNOWN_C4CC2F` | `StepState2VisualRecordFrameStrips` |
| 503 | C4:CD44 | C4:CEB0 | 364 | `exact` | yes | `unknown/C4/C4CD44.asm` | `UNKNOWN_C4CD44` | `StepState3VisualRecordMaskedColumns` |
| 504 | C4:CEB0 | C4:CED8 | 40 | `exact` | yes | `unknown/C4/C4CEB0.asm` | `UNKNOWN_C4CEB0` | `ClearVisualRecordOccupancyBitmap7f7f00` |
| 505 | C4:CED8 | C4:D00F | 311 | `exact` | yes | `unknown/C4/C4CED8.asm` | `UNKNOWN_C4CED8` | `StepState4VisualRecordRandomTileMask` |
| 506 | C4:D00F | C4:D065 | 86 | `exact` | yes | `unknown/C4/C4D00F.asm` | `` | `AppendNamingVowelRemapBytes` |
| 507 | C4:D065 | C4:D274 | 527 | `exact` | yes | `unknown/C4/C4D065.asm` | `UNKNOWN_C4D065` | `NormalizeNamingBufferToCommittedSelectorText` |
| 508 | C4:D274 | C4:D2A8 | 52 | `exact` | yes | `overworld/get_town_map_id.asm` | `` | `GetTownMapIdForCurrentPosition` |
| 509 | C4:D2A8 | C4:D2F0 | 72 | `exact` | yes | `unknown/C4/C4D2A8.asm` | `` | `TickTownMapPaletteAnimation` |
| 510 | C4:D2F0 | C4:D43F | 335 | `exact` | yes | `unknown/C4/C4D2F0.asm` | `` | `DrawTownMapCurrentPositionOverlay` |
| 511 | C4:D43F | C4:D553 | 276 | `exact` | yes | `unknown/C4/C4D43F.asm` | `` | `DrawTownMapStaticIconsAndOverlay` |
| 512 | C4:D553 | C4:D681 | 302 | `exact` | yes | `overworld/load_town_map_data.asm` | `` | `LoadTownMapData` |
| 513 | C4:D681 | C4:D744 | 195 | `exact` | yes | `overworld/display_town_map.asm` | `DISPLAY_TOWN_MAP` | `DisplayCurrentPositionTownMap` |
| 514 | C4:D744 | C4:D7D9 | 149 | `exact` | yes | `unknown/C4/C4D744.asm` | `UNKNOWN_C4D744` | `RunTownMapBrowseViewer` |
| 515 | C4:D7D9 | C4:D830 | 87 | `exact` | yes | `intro/display_animated_naming_sprite.asm` | `DISPLAY_ANIMATED_NAMING_SPRITE` | `` |
| 516 | C4:D830 | C4:D8FA | 202 | `exact` | yes | `unknown/C4/C4D830.asm` | `UNKNOWN_C4D830` | `RunFileSelectPoseEntityScriptList` |
| 517 | C4:D8FA | C4:D989 | 143 | `exact` | yes | `unknown/C4/C4D8FA.asm` | `UNKNOWN_C4D8FA` | `SpawnFileSelectFixedEntityBatch` |
| 518 | C4:D989 | C4:DAD2 | 329 | `exact` | yes | `unknown/C4/C4D989.asm` | `UNKNOWN_C4D989` | `RunFileSelectSwirlTransitionMode` |
| 519 | C4:DAD2 | C4:DCF6 | 548 | `exact` | yes | `intro/init_intro.asm` | `INIT_INTRO` | `InitIntroFileSelectStateDispatcher` |
| 520 | C4:DCF6 | C4:DD28 | 50 | `exact` | yes | `unknown/C4/C4DCF6.asm` | `` | `SetPriorityBitOnFileSelectTilemap7f0000` |
| 521 | C4:DD28 | C4:DDD0 | 168 | `exact` | yes | `intro/decomp_itoi_production.asm` | `DECOMP_ITOI_PRODUCTION` | `DecompressItoiProductionIntroAssets` |
| 522 | C4:DDD0 | C4:DE78 | 168 | `exact` | yes | `intro/decomp_nintendo_presentation.asm` | `DECOMP_NINTENDO_PRESENTATION` | `DecompressNintendoPresentationIntroAssets` |
| 523 | C4:DE78 | C4:DE98 | 32 | `exact` | yes | `data/unknown/C4DE78.asm` | `UNKNOWN_C4DE78` | `YourSanctuaryLocationCoordinateTable` |
| 524 | C4:DE98 | C4:DED0 | 56 | `exact` | yes | `overworld/initialize_your_sanctuary_display.asm` | `INITIALIZE_YOUR_SANCTUARY_DISPLAY` | `InitializeYourSanctuaryDisplayState` |
| 525 | C4:DED0 | C4:DEE9 | 25 | `exact` | yes | `overworld/enable_your_sanctuary_display.asm` | `ENABLE_YOUR_SANCTUARY_DISPLAY` | `EnableYourSanctuaryDisplayBg2State` |
| 526 | C4:DEE9 | C4:DF7D | 148 | `exact` | yes | `overworld/prepare_your_sanctuary_location_palette_data.asm` | `` | `PrepareYourSanctuaryLocationPaletteData` |
| 527 | C4:DF7D | C4:E08C | 271 | `exact` | yes | `overworld/prepare_your_sanctuary_location_tile_arrangement_data.asm` | `` | `PrepareYourSanctuaryLocationTileArrangementData` |
| 528 | C4:E08C | C4:E13E | 178 | `exact` | yes | `overworld/prepare_your_sanctuary_location_tileset_data.asm` | `` | `PrepareYourSanctuaryLocationTilesetData` |
| 529 | C4:E13E | C4:E281 | 323 | `exact` | yes | `overworld/load_your_sanctuary_location_data.asm` | `` | `LoadYourSanctuaryLocationData` |
| 530 | C4:E281 | C4:E2D7 | 86 | `exact` | yes | `overworld/load_your_sanctuary_location.asm` | `LOAD_YOUR_SANCTUARY_LOCATION` | `LoadYourSanctuaryLocation` |
| 531 | C4:E2D7 | C4:E366 | 143 | `exact` | yes | `overworld/display_your_sanctuary_location.asm` | `DISPLAY_YOUR_SANCTUARY_LOCATION` | `DisplayYourSanctuaryLocation` |
| 532 | C4:E366 | C4:E369 | 3 | `exact` | yes | `overworld/test_your_sanctuary_display.asm` | `TEST_YOUR_SANCTUARY_DISPLAY` | `TestYourSanctuaryDisplayStub` |
| 533 | C4:E369 | C4:E4DA | 369 | `exact` | yes | `ending/load_cast_scene.asm` | `LOAD_CAST_SCENE` | `LoadCastScene` |
| 534 | C4:E4DA | C4:E4F9 | 31 | `exact` | yes | `ending/set_cast_scroll_threshold.asm` | `SET_CAST_SCROLL_THRESHOLD` | `SetCastScrollThreshold` |
| 535 | C4:E4F9 | C4:E51E | 37 | `exact` | yes | `ending/check_cast_scroll_threshold.asm` | `CHECK_CAST_SCROLL_THRESHOLD` | `CheckCastScrollThreshold` |
| 536 | C4:E51E | C4:E583 | 101 | `exact` | yes | `ending/handle_cast_scrolling.asm` | `HANDLE_CAST_SCROLLING` | `HandleCastScrolling` |
| 537 | C4:E583 | C4:E7AE | 555 | `exact` | yes | `ending/render_cast_name_text.asm` | `` | `RenderCastNameText` |
| 538 | C4:E7AE | C4:EA9C | 750 | `exact` | yes | `data/character_guardian_text.asm` | `CHARACTER_GUARDIAN_TEXT` | `PrepareCastNameTilemap` |
| 539 | C4:EA9C | C4:EB04 | 104 | `exact` | yes | `ending/prepare_dynamic_cast_name_text.asm` | `PREPARE_DYNAMIC_CAST_NAME_TEXT` | `CopyCastNameTilemap` |
| 540 | C4:EB04 | C4:EBAD | 169 | `exact` | yes | `ending/prepare_cast_name_tilemap.asm` | `PREPARE_CAST_NAME_TILEMAP` | `PrintCastName` |
| 541 | C4:EBAD | C4:EC05 | 88 | `exact` | yes | `ending/copy_cast_name_tilemap.asm` | `COPY_CAST_NAME_TILEMAP` | `PrintCastNameParty` |
| 542 | C4:EC05 | C4:EC52 | 77 | `exact` | yes | `ending/print_cast_name.asm` | `PRINT_CAST_NAME` | `PrintCastNameEntityVar0` |
| 543 | C4:EC52 | C4:EC6E | 28 | `exact` | yes | `ending/print_cast_name_party.asm` | `PRINT_CAST_NAME_PARTY` | `PrintCastNameCurrentThreshold` |
| 544 | C4:EC6E | C4:ECAD | 63 | `exact` | yes | `ending/print_cast_name_entity_var0.asm` | `PRINT_CAST_NAME_ENTITY_VAR0` | `UploadSpecialCastPalette` |
| 545 | C4:ECAD | C4:ECE7 | 58 | `exact` | yes | `ending/upload_special_cast_palette.asm` | `UPLOAD_SPECIAL_CAST_PALETTE` | `CreateEntityAtV01PlusBg3Y` |
| 546 | C4:ECE7 | C4:ED0E | 39 | `exact` | yes | `ending/create_entity_at_v01_plus_bg3y.asm` | `CREATE_ENTITY_AT_V01_PLUS_BG3Y` | `IsEntityStillOnCastScreen` |
| 547 | C4:ED0E | C4:EDA3 | 149 | `exact` | yes | `ending/is_entity_still_on_cast_screen.asm` | `IS_ENTITY_STILL_ON_CAST_SCREEN` | `PlayCastScene` |
| 548 | C4:EDA3 | C4:EE9D | 250 | `exact` | yes | `ending/play_cast_scene.asm` | `PLAY_CAST_SCENE` | `UnusedCastNameScratchRenderer` |
| 549 | C4:EDA3 | C4:EE9D | 250 | `exact` | yes | `unused/C4EDA3.asm` | `` | `UnusedCastNameScratchRenderer` |
| 550 | C4:EE9D | C4:EEE1 | 68 | `exact` | yes | `unused/C4EE9D.asm` | `UNUSED_C4EE9D` | `RenderUnusedCastNameScratchSet` |
| 551 | C4:EEE1 | C4:EFC4 | 227 | `exact` | yes | `ending/change_vwf_2bpp_to_3_colour.asm` | `CHANGE_VWF_2BPP_TO_3_COLOUR` | `ConvertVwf2bppToThreeColor` |
| 552 | C4:EFC4 | C4:F01D | 89 | `exact` | yes | `ending/enqueue_credits_dma.asm` | `ENQUEUE_CREDITS_DMA` | `EnqueueCreditsDma` |
| 553 | C4:F01D | C4:F07D | 96 | `exact` | yes | `ending/process_credits_dma_queue.asm` | `PROCESS_CREDITS_DMA_QUEUE` | `ProcessCreditsDmaQueue` |
| 554 | C4:F07D | C4:F264 | 487 | `exact` | yes | `ending/initialize_credits_scene.asm` | `INITIALIZE_CREDITS_SCENE` | `InitializeCreditsScene` |
| 555 | C4:F264 | C4:F433 | 463 | `exact` | yes | `ending/try_rendering_photograph.asm` | `TRY_RENDERING_PHOTOGRAPH` | `TryRenderingPhotograph` |
| 556 | C4:F433 | C4:F46F | 60 | `exact` | yes | `ending/count_photo_flags.asm` | `COUNT_PHOTO_FLAGS` | `CountPhotoFlags` |
| 557 | C4:F46F | C4:F554 | 229 | `exact` | yes | `ending/slide_credits_photograph.asm` | `SLIDE_CREDITS_PHOTOGRAPH` | `SlideCreditsPhotograph` |
| 558 | C4:F554 | C4:F70A | 438 | `exact` | yes | `ending/play_credits.asm` | `PLAY_CREDITS` | `PlayCredits` |
| 559 | C4:F70A | C4:F947 | 573 | `exact` | yes | `data/music/dataset_table.asm` | `MUSIC_DATASET_TABLE` | `MusicDatasetTable` |
| 560 | C4:F947 | C4:FB42 | 507 | `exact` | yes | `data/music/pack_pointer_table.asm` | `MUSIC_PACK_POINTER_TABLE` | `MusicPackPointerTable` |
| 561 | C4:FB42 | C4:FB58 | 22 | `exact` | yes | `audio/get_audio_bank.asm` | `GET_AUDIO_BANK` | `GetAudioBank` |
| 562 | C4:FB58 | C4:FBBD | 101 | `exact` | yes | `audio/initialize_music_subsystem.asm` | `INITIALIZE_MUSIC_SUBSYSTEM` | `InitializeMusicSubsystem` |
| 563 | C4:FBBD | C4:FD18 | 347 | `exact` | yes | `audio/change_music.asm` | `CHANGE_MUSIC` | `ChangeMusic` |
| 564 | C4:FD18 | C4:FD45 | 45 | `exact` | yes | `audio/set_num_channels.asm` | `` | `SetAudioChannels` |
| 565 | C4:FD45 | C4:FD4B | 6 | `exact` | yes | `overworld/set_auto_sector_music_changes.asm` | `SET_AUTO_SECTOR_MUSIC_CHANGES` | `SetAutoSectorMusicChanges` |
