/** Two TB6600 velocity controller for the Arduino Mega 2560.
 * Timer1 generates pulses independently of serial parsing. Start/reset, NC stop,
 * invalid frames and heartbeat timeout all stop pulses and require fresh zero
 * commands before motion can resume. Telemetry counts issued pulses, not encoders.
 */
#include <Arduino.h>
#include <util/atomic.h>
#include <avr/wdt.h>
#include "drive_config.h"
#include "protocol.h"

constexpr uint8_t STEP_L = _BV(PA0), STEP_R = _BV(PA1);
constexpr uint8_t DIR_L = _BV(PA2), DIR_R = _BV(PA3), ENABLE = _BV(PA4), STOP = _BV(PA5);
volatile int16_t rates[2] = {0, 0};
volatile uint32_t steps[2] = {0, 0}; // Modular counts avoid signed overflow.
volatile uint16_t ageTicks = 65535;
volatile uint8_t fault = 1; // 1=start/timeout; 2=stop loop; 3=protocol.
volatile bool armed = false;
uint16_t phase[2] = {0, 0};
uint8_t highMask = 0;
int16_t target[2] = {0, 0}, current[2] = {0, 0};
uint16_t lastSequence = 0;
bool haveSequence = false, zeroSeen = false;
char input[80]; uint8_t inputLength = 0; bool overflowing = false;
uint32_t lastRamp = 0, lastReport = 0;

ISR(TIMER1_COMPA_vect) {
  const uint8_t previous = highMask;
  PORTA |= STEP_L | STEP_R; // Release any asserted pulse (common-anode).
  highMask = 0;
  if (ageTicks < 65535) ++ageTicks;
  if (PINA & STOP) { fault = 2; armed = false; }
  if (ageTicks > uint32_t(TIMER_HZ) * COMMAND_TIMEOUT_MS / 1000) { fault = 1; armed = false; }
  if (!armed) { rates[0] = rates[1] = 0; phase[0] = phase[1] = 0; return; }
  for (uint8_t i = 0; i < 2; ++i) {
    const uint8_t pin = i == 0 ? STEP_L : STEP_R;
    const int16_t rate = rates[i];
    phase[i] += uint16_t(rate < 0 ? -rate : rate);
    // A previous high pulse always gets a full low tick before the next edge.
    if (phase[i] >= TIMER_HZ && !(previous & pin)) {
      phase[i] -= TIMER_HZ; highMask |= pin;
      if (rate >= 0) ++steps[i]; else --steps[i];
    }
  }
  PORTA &= ~highMask;
}

void disable(uint8_t reason) {
  ATOMIC_BLOCK(ATOMIC_RESTORESTATE) { armed = false; fault = reason; rates[0] = rates[1] = 0; }
  target[0] = target[1] = current[0] = current[1] = 0; zeroSeen = false;
}

void receive(char* line) {
  DriveCommand command;
  if (!parseCommand(line, command, MAX_STEP_RATE)) { disable(3); return; }
  if (haveSequence && (command.enabled || command.left || command.right)) {
    const uint16_t difference = command.sequence - lastSequence;
    if (difference == 0 || difference >= 32768) { disable(3); return; }
  }
  haveSequence = true; lastSequence = command.sequence;
  ATOMIC_BLOCK(ATOMIC_RESTORESTATE) { ageTicks = 0; }
  if (PINA & STOP) { disable(2); return; }
  if (!command.enabled) {
    disable(0);
    // A disabled zero packet is the explicit reconnect/disarm handshake.
    zeroSeen = command.left == 0 && command.right == 0;
    return;
  }
  bool isArmed;
  ATOMIC_BLOCK(ATOMIC_RESTORESTATE) { isArmed = armed; }
  if (!isArmed) {
    if (!zeroSeen || command.left != 0 || command.right != 0) { disable(1); return; }
    ATOMIC_BLOCK(ATOMIC_RESTORESTATE) { fault = 0; armed = true; }
  }
  target[0] = command.left; target[1] = command.right;
}

void setup() {
  MCUSR = 0; wdt_disable();
  DDRA |= STEP_L | STEP_R | DIR_L | DIR_R | ENABLE;
  DDRA &= ~STOP; PORTA |= STEP_L | STEP_R | STOP;
  if (USE_ENABLE_OUTPUT) {
    if (ENABLE_OUTPUT_LOW_WHEN_ARMED) PORTA |= ENABLE; else PORTA &= ~ENABLE;
  }
  Serial.begin(SERIAL_BAUD);
  TCCR1A = 0; TCCR1B = _BV(WGM12) | _BV(CS11); // CTC, clock /8.
  OCR1A = F_CPU / 8 / TIMER_HZ - 1;
  TIMSK1 = _BV(OCIE1A);
  wdt_enable(WDTO_1S); // Main-loop deadlock resets into a disarmed boot.
}

void loop() {
  wdt_reset();
  // Bound serial work so continuous garbage cannot starve ramp/watchdog handling.
  for (uint8_t n = 0; n < 64 && Serial.available(); ++n) {
    char c = Serial.read();
    if (c == '\n') {
      if (overflowing) disable(3);
      else { input[inputLength] = '\0'; receive(input); }
      inputLength = 0; overflowing = false;
    } else if (c != '\r') {
      if (inputLength < sizeof(input)-1) input[inputLength++] = c;
      else { overflowing = true; disable(3); }
    }
  }
  const uint32_t now = millis();
  if (now - lastRamp >= 5) {
    const uint32_t dt = min(uint32_t(20), now - lastRamp); lastRamp = now;
    bool isArmed; uint8_t reason;
    ATOMIC_BLOCK(ATOMIC_RESTORESTATE) { isArmed = armed; reason = fault; }
    if (!isArmed) {
      target[0] = target[1] = current[0] = current[1] = 0;
      if (reason != 0) zeroSeen = false;
    }
    const int16_t increment = max(uint32_t(1), uint32_t(ACCEL_STEPS_PER_S2) * dt / 1000);
    for (uint8_t i = 0; i < 2; ++i) {
      // Reverse by ramping to zero, then set direction before the next pulse.
      const int16_t wanted = int32_t(target[i]) * current[i] < 0 ? 0 : target[i];
      int16_t next = current[i];
      if (next < wanted) next = min(int32_t(wanted), int32_t(next) + increment);
      else if (next > wanted) next = max(int32_t(wanted), int32_t(next) - increment);
      const bool positive = next >= 0;
      const bool inverted = i == 0 ? LEFT_DIRECTION_INVERTED : RIGHT_DIRECTION_INVERTED;
      const uint8_t dir = i == 0 ? DIR_L : DIR_R;
      ATOMIC_BLOCK(ATOMIC_RESTORESTATE) {
        if (current[i] == 0) {
          if (positive ^ inverted) PORTA |= dir; else PORTA &= ~dir;
          // Hold one ramp period at zero after a direction change (5 ms setup).
          if (next != 0) { current[i] = next; rates[i] = 0; continue; }
        }
        current[i] = next; rates[i] = next;
      }
    }
    if (USE_ENABLE_OUTPUT) {
      ATOMIC_BLOCK(ATOMIC_RESTORESTATE) {
        if (isArmed == ENABLE_OUTPUT_LOW_WHEN_ARMED) PORTA &= ~ENABLE; else PORTA |= ENABLE;
      }
    }
  }
  if (now - lastReport >= 50) {
    lastReport = now;
    int32_t left, right; bool active; uint8_t reason;
    ATOMIC_BLOCK(ATOMIC_RESTORESTATE) { left = steps[0]; right = steps[1]; active = armed; reason = fault; }
    char report[70];
    snprintf(report, sizeof(report), "S1,%u,%u,%u,%ld,%ld", lastSequence, active ? 1 : 0, reason, long(left), long(right));
    const uint16_t checksum = crc16(report, strlen(report));
    char ending[8]; snprintf(ending, sizeof(ending), ",%04X\n", checksum);
    if (Serial.availableForWrite() >= int(strlen(report) + strlen(ending))) { Serial.print(report); Serial.print(ending); }
  }
}
