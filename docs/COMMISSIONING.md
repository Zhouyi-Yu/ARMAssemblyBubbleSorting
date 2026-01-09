# Commissioning Guide: Industrial RFID Edge Processor

This document provides technical instructions for commissioning the **SiteSense® Edge Sorting Firmware** on local project-site hardware.

## 📋 System Prerequisites
- **Target OS**: POSIX / ARMv7-A Architecture
- **Peripherals**: 8x8 LED Matrix (for status signaling), GPIO Controllers
- **Toolchain**: GNU Arm Embedded Toolchain (arm-none-eabi)

## 🛠️ Installation Steps

### 1. Hardware Interface Setup
Ensure the LED peripheral is mapped to the correct memory bank. The firmware expects:
- **Column Register**: `r1` mapping
- **Row Register**: `r2` mapping

### 2. Firmware Deployment
Compile and link the `edge_sort_firmware.s`:
```bash
arm-none-eabi-as -o edge_sort.o firmware/edge_sort_firmware.s
arm-none-eabi-ld -o edge_sort.elf edge_sort.o
```

### 3. Commissioning Test
Run the emulator to verify logic without physical hardware:
```bash
python3 emulator/edge_sort_emulator.py
```

## 🔍 Troubleshooting
- **Issue**: LED signaling is inverted or delayed.
- **Root Cause**: `HAL_Delay` constant in `r3` is too high for current clock speed.
- **Fix**: Adjust `mov r3, #0` value in line 30 of `edge_sort_firmware.s` to match site requirements.

---
*Note: For further support, contact the Senior Implementation Strategy team via JIRA.*
