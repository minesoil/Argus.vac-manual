/*
  Argus Vac - Drive Motor Control
  ---------------------------------------------------------------------------
  Hardware (from the Fritzing wiring audit):

    Arduino Mega 2560          Left A4988 driver      Left stepper (M2)
      D2  ---------------------> STEP
      D3  ---------------------> DIR
      5V  ---------------------> VDD (logic power)
      GND ---------------------> GND (logic ground)
                                 1A/1B/2A/2B  --------> A / C / B / D

    Arduino Mega 2560          Right A4988 driver     Right stepper (M4)
      D4  ---------------------> STEP
      D5  ---------------------> DIR
      5V  ---------------------> VDD (logic power)
      GND ---------------------> GND (logic ground)
                                 1A/1B/2A/2B  --------> A / C / B / D

    LiPo (11.1V) -> LM2596 buck converter -> Arduino VIN
    LiPo (+)     -> VMOT on both A4988 drivers (motor power)
    LiPo (-)     -> GND(motor) on both A4988 drivers, and driver GND(logic)
                    is tied to Arduino GND (common ground - required!)

  Both drivers have RESET tied to SLEEP (required for the A4988 to run).
  ENABLE, MS1, MS2, MS3 are left unconnected on purpose -> the Pololu A4988
  carrier pulls ENABLE low (driver enabled) and MS1-3 low (full-step mode)
  by default, so this is a valid, simple configuration.

  IMPORTANT - fix these 3 wiring bugs found in the .fzz before you power this up:
    1. C2's "-" leg is floating -> connect it to the battery/GND rail.
    2. C3's "+" leg is floating -> connect it to the battery/VMOT (+) rail.
    3. The RIGHT driver's motor-side GND pin (next to VMOT) isn't wired to
       anything -> connect it to the battery negative rail, same as the
       left driver. Running it without this is unreliable/unsafe for the
       driver.

  Library required: AccelStepper (Arduino Library Manager -> "AccelStepper" by Mike McCauley)
*/

#include <AccelStepper.h>

// ---- Pin assignments (matches the wiring above) ----------------------------
const uint8_t LEFT_STEP_PIN  = 2;
const uint8_t LEFT_DIR_PIN   = 3;
const uint8_t RIGHT_STEP_PIN = 4;
const uint8_t RIGHT_DIR_PIN  = 5;

// ---- Tuning ------------------------------------------------------------
const float MAX_SPEED_SPS     = 800.0;  // steps/sec ceiling
const float ACCEL_SPS2        = 600.0;  // steps/sec^2
const float CRUISE_SPEED_SPS  = 500.0;  // normal driving speed
const float TURN_SPEED_SPS    = 350.0;  // speed used while turning in place

// AccelStepper::DRIVER mode = 2 pins (STEP, DIR), which is exactly what an
// A4988 needs.
AccelStepper leftMotor(AccelStepper::DRIVER, LEFT_STEP_PIN, LEFT_DIR_PIN);
AccelStepper rightMotor(AccelStepper::DRIVER, RIGHT_STEP_PIN, RIGHT_DIR_PIN);

void setup() {
  leftMotor.setMaxSpeed(MAX_SPEED_SPS);
  leftMotor.setAcceleration(ACCEL_SPS2);

  rightMotor.setMaxSpeed(MAX_SPEED_SPS);
  rightMotor.setAcceleration(ACCEL_SPS2);

  stopMotors();
}

void loop() {
  // Simple demo pattern - replace with your own navigation/vacuum logic.
  driveForward(CRUISE_SPEED_SPS);
  runFor(2000);   // 2 seconds forward

  stopMotors();
  runFor(300);

  turnRight(TURN_SPEED_SPS);
  runFor(650);    // roughly a 90 degree pivot - tune this for your gearing

  stopMotors();
  runFor(300);
}

// ---- Motion primitives ---------------------------------------------------
// NOTE: if the robot drives backward when you ask for forward (or turns the
// wrong way), swap the sign on that motor's speed below rather than
// re-wiring anything - it's just a matter of which coil pair got called A/C.

void driveForward(float speed) {
  leftMotor.setSpeed(speed);
  rightMotor.setSpeed(speed);
}

void driveBackward(float speed) {
  leftMotor.setSpeed(-speed);
  rightMotor.setSpeed(-speed);
}

void turnLeft(float speed) {
  // Left wheel back, right wheel forward = pivot left in place.
  leftMotor.setSpeed(-speed);
  rightMotor.setSpeed(speed);
}

void turnRight(float speed) {
  leftMotor.setSpeed(speed);
  rightMotor.setSpeed(-speed);
}

void stopMotors() {
  leftMotor.setSpeed(0);
  rightMotor.setSpeed(0);
}

// Runs the motors at whatever speed was last set, for the given duration.
void runFor(unsigned long ms) {
  unsigned long start = millis();
  while (millis() - start < ms) {
    leftMotor.runSpeed();
    rightMotor.runSpeed();
  }
}
