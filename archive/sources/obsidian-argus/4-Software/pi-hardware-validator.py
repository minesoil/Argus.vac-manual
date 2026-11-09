#!/usr/bin/env python3
"""
pi-hardware-validator.py
Argus Vac - End-to-End Serial Actuator Diagnostic Suite
Developed for Orange Pi 5

This script provides an interactive terminal diagnostic environment to systematically 
test all physical actuators on the Argus Vac via USB Serial commands sent to the Arduino Mega 2560.
This serves as a diagnostic scaffold to test physical components, verify cable handshakes, 
and establish the absolute communication patterns that Claude or ROS2 nodes must adhere to 
for final assembly.
"""

import serial
import time
import sys

# --- HARDWARE CONFIGURATION ---
SERIAL_PORT = '/dev/ttyACM0'  # Default for Arduino Mega on Linux/Orange Pi 5 USB ports
BAUD_RATE = 115200
TIMEOUT = 2.0

def print_header():
    print("\n" + "="*60)
    print("      ARGUS VAC - SYSTEM HARDWARE VALIDATION SCROLL      ")
    print("="*60)
    print(f"Target Port: {SERIAL_PORT} | Baud Rate: {BAUD_RATE}")
    print("Ensure the Arduino Mega is connected to your Orange Pi via USB.\n")

def establish_connection():
    try:
        print(f"[SERIAL] Opening port {SERIAL_PORT}...")
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT)
        time.sleep(2.0)  # Wait for Arduino auto-reset on connection
        
        # Clear buffers
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        
        # Ping test
        print("[SERIAL] Sending Handshake Ping (P)...")
        ser.write(b"P\n")
        response = ser.readline().decode('utf-8').strip()
        
        if "ACK" in response:
            print(f"[SUCCESS] Connected! Arduino Response: {response}")
            return ser
        else:
            print(f"[WARNING] Sent ping, got unexpected response: '{response}'")
            return ser
            
    except serial.SerialException as e:
        print(f"\n[ERROR] Could not open serial port {SERIAL_PORT}.")
        print("1. Run 'ls /dev/ttyACM*' or 'ls /dev/ttyUSB*' on the Orange Pi to find the port.")
        print("2. Ensure your user has dialout permissions: 'sudo usermod -a -G dialout $USER'.")
        print(f"Details: {e}")
        sys.exit(1)

def send_command(ser, cmd_string):
    """Sends a formatted command string to the Arduino and returns its response."""
    full_cmd = f"{cmd_string}\n"
    print(f"\n[TX] Sending: '{cmd_string}'")
    ser.write(full_cmd.encode('utf-8'))
    
    # Read response
    time.sleep(0.1) # Give Arduino a moment to process and respond
    while ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        print(f"[RX] {line}")

def interactive_menu(ser):
    while True:
        print("\n" + "-"*40)
        print("          ACTUATOR DIAGNOSTIC MENU        ")
        print("-"*40)
        print(" [1] Connection Ping Test")
        print(" [2] Stepper Traction Motors Test (Move Forward slowly)")
        print(" [3] Dual N20 Brush Sweeper Motors (L298N) ON")
        print(" [4] Dual N20 Brush Sweeper Motors (L298N) OFF")
        print(" [5] San Ace 40 Vacuum Fan (drv-1012) ON")
        print(" [6] San Ace 40 Vacuum Fan (drv-1012) OFF")
        print(" [7] Trigger Emergency Stop/Halt (H)")
        print(" [8] Reset/Clear Halt state (G)")
        print(" [9] Run Interactive Mock Obstacle Loop (Test CV Evasion)")
        print(" [0] Exit Diagnostics")
        print("-"*40)
        
        choice = input("Select physical component to test (0-9): ").strip()
        
        if choice == '1':
            send_command(ser, "P")
        elif choice == '2':
            send_command(ser, "S 1")
        elif choice == '3':
            send_command(ser, "B 1")
        elif choice == '4':
            send_command(ser, "B 0")
        elif choice == '5':
            send_command(ser, "V 1")
        elif choice == '6':
            send_command(ser, "V 0")
        elif choice == '7':
            send_command(ser, "H")
        elif choice == '8':
            send_command(ser, "G")
        elif choice == '9':
            test_evasion_reaction(ser)
        elif choice == '0':
            print("\nShutting down diagnostics and stopping all actuators...")
            send_command(ser, "H")
            break
        else:
            print("[INVALID] Please select a number from 0 to 9.")

def test_evasion_reaction(ser):
    """
    Simulates a running vacuum cycle. At any point, the user can press 'Space' 
    to mock a Camera/OpenCV Obstacle Detection warning event to see the exact 
    latency and behavior of the Arduino Mega mechanical halt mechanism.
    """
    print("\n" + "*"*55)
    print("      MOCK CYCLING RUN (TESTING CAMERA HALT INTERRUPT)    ")
    print("*"*55)
    print("Press ENTER to start simulating a running cycle...")
    input()
    
    # 1. Turn on sweeping brushes and vacuum fan
    print("[MOCK] Spinning up sweepers and vacuum...")
    send_command(ser, "B 1")
    time.sleep(1.0)
    send_command(ser, "V 1")
    time.sleep(1.0)
    
    # 2. Start stepper movement loop
    print("[MOCK] Commencing forward movement...")
    send_command(ser, "S 1")
    
    print("\n!!! ROBOT IS RUNNING !!!")
    print(">>> Press [ENTER] at any moment to simulate CAMERA DETECTED AN OBSTACLE! <<<")
    
    input() # Wait for user reaction
    
    print("\n[MOCK CAMERA DETECTED OBJECT] !!! EMITTING IMMEDIATE HALT COMMAND !!!")
    # Immediate write bypassing standard queue delays
    ser.write(b"H\n")
    
    # Capture response
    time.sleep(0.1)
    while ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        print(f"[RX] {line}")
        
    print("\n[SUCCESS] Halt verified. Actuators isolated and safe.")
    print("Press ENTER to return to main menu...")
    input()
    send_command(ser, "G") # Reset state before returning

def main():
    print_header()
    ser = establish_connection()
    try:
        interactive_menu(ser)
    except KeyboardInterrupt:
        print("\n\nForced Quit. Safely halting all physical hardware...")
        try:
            ser.write(b"H\n")
            ser.close()
        except:
            pass
        print("Hardware isolated. Done.")

if __name__ == "__main__":
    main()
