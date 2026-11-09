#pragma once
// Match MICROSTEPS to both TB6600 DIP-switch settings. One pulse is one microstep.
constexpr uint16_t FULL_STEPS_PER_REV = 200;
constexpr uint8_t MICROSTEPS = 8;
constexpr uint32_t SERIAL_BAUD = 115200;
constexpr uint16_t TIMER_HZ = 40000;
constexpr int16_t MAX_STEP_RATE = 16000;
constexpr uint16_t ACCEL_STEPS_PER_S2 = 4000;
constexpr uint16_t COMMAND_TIMEOUT_MS = 350;
constexpr bool LEFT_DIRECTION_INVERTED = false;
constexpr bool RIGHT_DIRECTION_INVERTED = true;

// Mega PORTA: D22 step left, D23 step right, D24 dir left, D25 dir right.
// Common-anode wiring: PUL+/DIR+ -> Mega 5 V; PUL-/DIR- -> these output pins.
// D27 is an NC stop loop to GND: closed = healthy, open = stop/fault.
// ENA terminal behavior varies between modules. Leave ENA disconnected until
// checked against your driver's manual. Pulses always stop when disarmed.
constexpr bool USE_ENABLE_OUTPUT = false; // D26, only after checking ENA polarity.
constexpr bool ENABLE_OUTPUT_LOW_WHEN_ARMED = true;
