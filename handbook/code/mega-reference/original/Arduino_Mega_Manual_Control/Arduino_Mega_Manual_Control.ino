
#include <AccelStepper.h>
#include <stdio.h>

// =======================================
// ARGUS VAC V2 - DUAL MOTOR CONTROLLER
// Arduino Mega + 2 HW-090B Drivers
// ESP32 Wireless Joystick
// =======================================

// ORIGINAL MOTOR PINS
#define LEFT_STEP   24
#define LEFT_DIR    25
#define RIGHT_STEP  22
#define RIGHT_DIR   23

// Change these if forward direction is wrong
const int LEFT_SIGN  =  1;
const int RIGHT_SIGN = -1;

// =======================================
// MOTOR SETTINGS
// =======================================

// At joystick 100%, request this speed
const float MAX_STEP_RATE = 3500.0;

// Acceleration in microsteps/second^2
const float ACCEL_RATE = 4500.0;

// Update speeds every 10 milliseconds
const unsigned long RAMP_INTERVAL_MS = 10;

// Stop on lost communication
const unsigned long TIMEOUT_MS = 900;

// =======================================
// STEPPER OBJECTS
// =======================================

AccelStepper leftMotor(
  AccelStepper::DRIVER,
  LEFT_STEP,
  LEFT_DIR
);

AccelStepper rightMotor(
  AccelStepper::DRIVER,
  RIGHT_STEP,
  RIGHT_DIR
);

// Current target speeds
float leftTarget = 0;
float rightTarget = 0;

unsigned long lastCommand = 0;
unsigned long lastRamp = 0;
bool linkActive = false;

// Separate parsers for USB and ESP32
struct CommandParser {
  char buffer[24];
  byte length = 0;
  bool collecting = false;
};

CommandParser usbParser;
CommandParser espParser;

// =======================================
// DRIVE CONTROL
// =======================================

void drive(int leftPercent, int rightPercent) {
  leftPercent = constrain(leftPercent, -100, 100);
  rightPercent = constrain(rightPercent, -100, 100);

  leftTarget =
    LEFT_SIGN * MAX_STEP_RATE *
    leftPercent / 100.0;

  rightTarget =
    RIGHT_SIGN * MAX_STEP_RATE *
    rightPercent / 100.0;

  lastCommand = millis();
  linkActive = true;
}

// Immediate stop for emergency / timeout
void stopNow() {
  leftTarget = 0;
  rightTarget = 0;

  leftMotor.setSpeed(0);
  rightMotor.setSpeed(0);

  linkActive = false;
}

// =======================================
// SMOOTH ACCELERATION
// =======================================

float approach(float current,
               float target,
               float maxChange) {

  if (target > current + maxChange) {
    return current + maxChange;
  }

  if (target < current - maxChange) {
    return current - maxChange;
  }

  return target;
}

void updateMotorSpeeds() {
  unsigned long now = millis();
  unsigned long elapsed = now - lastRamp;

  if (elapsed < RAMP_INTERVAL_MS) return;

  lastRamp = now;

  // Prevent a huge jump after a delay
  if (elapsed > 40) elapsed = 40;

  float change =
    ACCEL_RATE * elapsed / 1000.0;

  float nextLeft = approach(
    leftMotor.speed(),
    leftTarget,
    change
  );

  float nextRight = approach(
    rightMotor.speed(),
    rightTarget,
    change
  );

  leftMotor.setSpeed(nextLeft);
  rightMotor.setSpeed(nextRight);
}

// =======================================
// COMMAND HANDLING
// =======================================

void handleSingleCommand(char c) {
  switch (c) {
    case 'F': drive(60, 60); break;
    case 'B': drive(-60, -60); break;
    case 'L': drive(-50, 50); break;
    case 'R': drive(50, -50); break;

    case '1': drive(50, 0); break;
    case '2': drive(0, 50); break;

    case 'S':
    case 'X':
      stopNow();
      break;
  }
}

void handleInput(CommandParser &p, char c) {
  if (p.collecting) {

    if (c == '\n' || c == '\r' || c == ';') {

      p.buffer[p.length] = '\0';

      int leftValue;
      int rightValue;

      // ESP32 sends M:left,right
      if (sscanf(
            p.buffer,
            ":%d,%d",
            &leftValue,
            &rightValue
          ) == 2) {

        if (leftValue >= -100 &&
            leftValue <= 100 &&
            rightValue >= -100 &&
            rightValue <= 100) {

          drive(leftValue, rightValue);
        }
      }

      p.length = 0;
      p.collecting = false;

    } else if (p.length < sizeof(p.buffer) - 1) {
      p.buffer[p.length++] = c;

    } else {
      p.length = 0;
      p.collecting = false;
      stopNow();
    }

  } else if (c == 'M') {
    p.collecting = true;
    p.length = 0;

  } else {
    handleSingleCommand(c);
  }
}

void readCommands(Stream &port,
                  CommandParser &parser) {

  while (port.available()) {
    handleInput(parser, (char)port.read());
  }
}

// =======================================
// SETUP
// =======================================

void setup() {
  Serial.begin(115200);
  Serial1.begin(9600);

  leftMotor.setMaxSpeed(MAX_STEP_RATE);
  rightMotor.setMaxSpeed(MAX_STEP_RATE);

  // Common-cathode = normal STEP pulses
  // DIR inverted to preserve old
  // common-anode direction logic
  leftMotor.setPinsInverted(true, false, false);
  rightMotor.setPinsInverted(true, false, false);

  leftMotor.setMinPulseWidth(20);
  rightMotor.setMinPulseWidth(20);

  stopNow();
  lastRamp = millis();

  Serial.println("ARGUS VAC V2 READY");
  Serial.println("Dual HW-090B drivers");
  Serial.println("Max step rate: 3000 steps/s");
  Serial.println("Commands: F B L R S 1 2");
  Serial.println("ESP32 format: M:left,right");
}

// =======================================
// MAIN LOOP
// =======================================

void loop() {

  readCommands(Serial, usbParser);
  readCommands(Serial1, espParser);

  // Lost communication safety
  if (linkActive &&
      millis() - lastCommand > TIMEOUT_MS) {
    stopNow();
  }

  // Update acceleration
  updateMotorSpeeds();

  // Generate step pulses continuously
  leftMotor.runSpeed();
  rightMotor.runSpeed();
}
