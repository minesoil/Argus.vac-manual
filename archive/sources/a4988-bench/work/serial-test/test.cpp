// Controller simulation using the installed, unmodified AccelStepper source.
// Arduino time, pins and serial are simulated; this is not a physical motor test.
#include <cassert>
#include <iostream>
#include "Arduino.h"
static_assert(sizeof(unsigned long) == 4, "Tests need AVR-style 32-bit micros rollover");
unsigned long testTimeUs = 0;
unsigned long stepEdges = 0;
int pins[70] = {};
TestSerial Serial;
unsigned long micros() { return testTimeUs; }
void pinMode(uint8_t, uint8_t) {}
void digitalWrite(uint8_t pin, uint8_t value) {
  if (pin == 4 && value == HIGH && pins[pin] == LOW) ++stepEdges;
  pins[pin] = value;
}
void delayMicroseconds(unsigned int us) { testTimeUs += us; }
#include "../../outputs/left_wheel_diagnostic/left_wheel_diagnostic.ino"
void tick(unsigned long us = 100) { testTimeUs += us; loop(); }
void spin(unsigned long durationUs) {
  unsigned long start = micros();
  while ((unsigned long)(micros() - start) < durationUs) tick();
}
void send(const std::string &text) {
  for (char c : text) Serial.input.push_back(c);
  while (Serial.available()) tick();
}
bool near(float a, float b, float tolerance = 0.01f) { return fabs(a - b) < tolerance; }
int main() {
  setup();
  assert(motorState == DISABLED && pins[ENABLE_PIN] == HIGH && near(wheel.speed(), 0));
  spin(100000);
  assert(stepEdges == 0);
  assert(near(accelerationCmPerS2, 2));
  assert(Serial.output.find("a2=accel/decel") != std::string::npos);
  // Verify the new default ramp and changing acceleration without a speed jump.
  send("2\nr\n");
  spin(500000);
  assert(near(currentSpeedCmPerS, 1, 0.02f));
  float speedBeforeAccelerationChange = currentSpeedCmPerS;
  send("a1\n");
  assert(near(accelerationCmPerS2, 1));
  assert(near(currentSpeedCmPerS, speedBeforeAccelerationChange, 0.02f));
  spin(500000);
  assert(near(currentSpeedCmPerS, 1.5f, 0.02f));
  spin(600000);
  assert(near(currentSpeedCmPerS, 2));
  send("0\n");
  spin(1000000);
  assert(near(currentSpeedCmPerS, 1, 0.02f));
  spin(1100000);
  assert(near(currentSpeedCmPerS, 0) && pins[ENABLE_PIN] == LOW);
  send("s\nA 2\n");
  assert(motorState == DISABLED && near(accelerationCmPerS2, 2));
  send("a0.1\n");
  assert(near(accelerationCmPerS2, 0.1f));
  send("a50\n");
  assert(near(accelerationCmPerS2, 50));
  send("a0\na-1\na50.1\na\nanan\nainf\na1junk\n");
  assert(near(accelerationCmPerS2, 50) && motorState == DISABLED);
  send("a10\n"); // Run legacy speed/serial regression cases at their original ramp.
  stepEdges = 0;
  send(" 2.5 \r\n");
  assert(near(targetSpeedCmPerS, 2.5f) && motorState == DISABLED);
  send("r\n");
  assert(pins[ENABLE_PIN] == LOW && motorState == RUNNING);
  spin(100000);
  assert(currentSpeedCmPerS > 0 && currentSpeedCmPerS < 2.5f);
  spin(200000);
  assert(near(currentSpeedCmPerS, 2.5f) && stepEdges > 0);
  send("+\r\n");
  assert(near(targetSpeedCmPerS, 3.5f));
  assert(currentSpeedCmPerS < targetSpeedCmPerS);
  spin(50000);
  assert(currentSpeedCmPerS > 2.5f && currentSpeedCmPerS < 3.5f);
  spin(60000);
  assert(near(currentSpeedCmPerS, 3.5f));
  send("-\n");
  assert(near(targetSpeedCmPerS, 2.5f) && currentSpeedCmPerS > 3.4f);
  spin(50000);
  assert(currentSpeedCmPerS > 2.5f && currentSpeedCmPerS < 3.5f);
  spin(60000);
  assert(near(currentSpeedCmPerS, 2.5f));
  send("30\n");
  spin(2800000);
  assert(near(currentSpeedCmPerS, 30) && near(wheel.speed(), 30 * STEPS_PER_CM, 0.1f));
  // Serial backpressure and a full feedback queue must not stop stepping.
  Serial.writable = 0;
  for (int i = 0; i < 100; ++i) send("p\n");
  unsigned long before = stepEdges;
  spin(250000);
  assert(stepEdges - before > 290 && stepEdges - before < 340);
  Serial.writable = 64;
  send("0\n");
  spin(1500000);
  assert(currentSpeedCmPerS > 14 && currentSpeedCmPerS < 16);
  spin(1600000);
  assert(near(currentSpeedCmPerS, 0) && pins[ENABLE_PIN] == LOW);
  before = stepEdges;
  spin(100000);
  assert(stepEdges == before);
  send("-\n");
  assert(near(targetSpeedCmPerS, 0));
  send("60\n+\n");
  assert(near(targetSpeedCmPerS, 60));
  send("-2\n61\nnan\ninf\n1e99\n12junk\n123456789012345678901234567890\n");
  assert(near(targetSpeedCmPerS, 60));
  send("10\n");
  spin(300000);
  float speedBeforeRepeat = currentSpeedCmPerS;
  send("R\n");
  assert(currentSpeedCmPerS >= speedBeforeRepeat);
  send("H\n");
  assert(motorState == HOLDING && pins[ENABLE_PIN] == LOW && near(wheel.speed(), 0));
  before = stepEdges;
  spin(100000);
  assert(stepEdges == before);
  send("S\n");
  assert(motorState == DISABLED && pins[ENABLE_PIN] == HIGH);
  send("2\n");
  spin(100000);
  assert(stepEdges == before && motorState == DISABLED);
  // Crossing micros() rollover must continue ramping and stepping.
  testTimeUs = 0xFFFFF000UL;
  send("r\n");
  spin(300000);
  assert(near(currentSpeedCmPerS, 2) && stepEdges > before);
  send("s\n");
  assert(pins[ENABLE_PIN] == HIGH && near(wheel.speed(), 0));
  std::cout << "PASS: default gentler ramp, live acceleration tuning and bounds;\n"
               "startup, numeric/+/-, smooth ramps both ways, stop/hold, bounds, CRLF,\n"
               "invalid/overlong input, repeated run, serial backpressure, micros rollover.\n";
}
