import time
import random

def simulate_edge_processing():
    """
    Simulates the ARM Assembly logic for Edge-based Data Sorting.
    This mimics the bit-shifting and LED-per-row feedback described in edge_sort_firmware.s
    """
    print("==================================================")
    print("INDUSTRIAL MATERIAL TRACKING FIRMWARE SIMULATOR")
    print("==================================================")
    print("[INFO] Initializing Peripheral Interfaces...")
    time.sleep(1)
    
    # Simulate a raw data array from RFID scanners (Material Priorities)
    raw_data = [random.randint(1, 100) for _ in range(10)]
    print(f"[INPUT] Raw RFID Signal Array: {raw_data}")
    
    print("\n[EXEC] Running Assembly Edge-Sort Protocol...")
    time.sleep(1)
    
    # Bubble sort simulation matching the assembly logic
    n = len(raw_data)
    for i in range(n):
        for j in range(0, n-i-1):
            if raw_data[j] > raw_data[j+1]:
                raw_data[j], raw_data[j+1] = raw_data[j+1], raw_data[j]
                
                # Simulate the LED / Bit-shift updates
                binary_val = bin(raw_data[j])[2:].zfill(8)
                print(f"  SORTING | Register R4 Shift: {binary_val} | [LED ON] Syncing Row {j//4}")
                time.sleep(0.1)

    print("\n[RESULT] Sorted Material Priorities (Local Storage):")
    print(f"  {raw_data}")
    print("\n[SUCCESS] Commissioning Phase Complete. Data Ready for SiteSense Sync.")

if __name__ == "__main__":
    simulate_edge_processing()
