# Industrial Material Tracking Firmware (Edge Sort) 📟

This repository contains the **Edge Processing Firmware** for industrial material tracking systems (SiteSense® compatible). It is designed to run on ARM-based edge hardware at construction sites to prioritize material detection and sort RFID signal arrays with low-power consumption.

## 🚀 Key Features
- **Edge-Based Data Sorting**: High-performance bubble sort implemented in **ARMv7-A Assembly** for sub-millisecond edge processing.
- **Peripheral Interface Logic**: direct bit-manipulation of LED matrix registers for real-time site status signaling.
- **System Commissioning**: Includes a technical commissioning guide for on-site engineering and installation.
- **Digital Twin Emulator**: Python-based functional emulator to verify sorting logic and peripheral state transitions without physical hardware.

## 📂 Repository Structure
- `firmware/`: Core assembly firmware (`edge_sort_firmware.s`).
- `emulator/`: Visualizer and logic verification script (`edge_sort_emulator.py`).
- `docs/`: Professional technical documentation (`COMMISSIONING.md`).

## 🛠️ Getting Started

### 1. Functional Verification (Emulator)
Run the Python emulator to visualize how the edge processor handles raw RFID signals:
```bash
python3 emulator/edge_sort_emulator.py
```

### 2. Physical Commissioning
Refer to the [Commissioning Guide](./docs/COMMISSIONING.md) for instructions on hardware mapping and toolchain setup.

## 🔍 Implementation Details
The firmware utilizes `LDR/STR` operations for memory access and `BCS` (Branch if Carry Set) for bit-level peripheral signaling. It is optimized for low-latency operational environments where cloud connectivity may be intermittent.

---
*Developed for Procore Solutions Engineering Strategy — Leveraging edge computing to improve construction site operations.*
