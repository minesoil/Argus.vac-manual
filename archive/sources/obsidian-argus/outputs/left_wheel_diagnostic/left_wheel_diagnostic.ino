// Left-wheel diagnostic, revision 1.5; requires AccelStepper.
// Mega: D4 -> STEP, D3 -> DIR, D8 -> EN (active LOW).
// Quarter stepping: MS1 disconnected, MS2 -> 5 V/VDD, MS3 disconnected.
// MS1 has a measured low-resistance ground path: keep it off 5 V.
// VDD = 5 V, VMOT = separate 12 V supply, Arduino/A4988 grounds shared.
// Disconnect all power before changing wiring.
//
// Serial Monitor: 115200 baud, Newline or Both NL & CR; send one command.
// r = run, s = disable immediately, h = stop immediately and hold
// + / - = raise / lower the target by 1 cm/s
// A number, e.g. 2 or 30, sets the target in cm/s; 0 ramps to a holding stop.
// a2 = set acceleration/deceleration to 2 cm/s squared (range 0.1..50).
// p = status, ? = help. Changing the target alone does not enable the motor.

#include <AccelStepper.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const byte STEP_PIN = 4;
const byte DIR_PIN = 3;
const byte ENABLE_PIN = 8;
const bool REVERSE_DIRECTION = false;

// Geometry assumes direct drive and a 1.8-degree motor.
// MICROSTEPS describes physical MS wiring; the sketch does not set MS pins.
const unsigned int FULL_STEPS_PER_REV = 200;
const unsigned int MICROSTEPS = 4;
const float WHEEL_DIAMETER_CM = 6.0f;
const float STEPS_PER_CM =
  (float)FULL_STEPS_PER_REV * MICROSTEPS / (3.14159265f * WHEEL_DIAMETER_CM);

const float INITIAL_SPEED_CM_PER_S = 30.0f;
const float MAX_SPEED_CM_PER_S = 60.0f; // Software limit, not a verified motor maximum.
const float SPEED_INCREMENT_CM_PER_S = 1.0f;
const float INITIAL_ACCELERATION_CM_PER_S2 = 2.0f; // 0 -> 10 cm/s takes about 5 seconds.
const float MIN_ACCELERATION_CM_PER_S2 = 0.1f;
const float MAX_ACCELERATION_CM_PER_S2 = 50.0f;
const unsigned int PULSE_WIDTH_US = 5;
const unsigned long RAMP_UPDATE_US = 2000UL;

// false avoids configuring outputs during global construction.
AccelStepper wheel(AccelStepper::DRIVER, STEP_PIN, DIR_PIN, 0, 0, false);

enum MotorState { DISABLED, HOLDING, RUNNING };
MotorState motorState = DISABLED;
float targetSpeedCmPerS = INITIAL_SPEED_CM_PER_S;
float currentSpeedCmPerS = 0.0f;
float accelerationCmPerS2 = INITIAL_ACCELERATION_CM_PER_S2;
unsigned long lastRampUs = 0;

char commandBuffer[24];
byte commandLength = 0;
bool commandOverflow = false;

// Queue feedback so Serial output does not wait for the USB serial transmitter.
// If commands flood the queue, feedback can be dropped; commands still execute.
const unsigned int TX_CAPACITY = 512;
char txBuffer[TX_CAPACITY];
unsigned int txHead = 0;
unsigned int txTail = 0;

void queueText(const char *text) {
  while (*text) {
    const unsigned int next = (txHead + 1) % TX_CAPACITY;
    if (next == txTail) return;
    txBuffer[txHead] = *text++;
    txHead = next;
  }
}

void queueStatus() {
  char targetText[16];
  char currentText[16];
  char accelerationText[16];
  char message[128];
  dtostrf(targetSpeedCmPerS, 1, 2, targetText);
  dtostrf(currentSpeedCmPerS, 1, 2, currentText);
  dtostrf(accelerationCmPerS2, 1, 2, accelerationText);
  const char *stateText = motorState == DISABLED ? "disabled" :
    motorState == HOLDING ? "holding" : "running";
  snprintf(message, sizeof(message), "%s; target=%s, commanded=%s cm/s; accel=%s cm/s^2\r\n",
    stateText, targetText, currentText, accelerationText);
  queueText(message);
}

void queueHelp() {
  queueText("r=run, s=disable now, h=stop/hold now\r\n");
  queueText("+=+1 cm/s, -=-1 cm/s, number=target (0..60 cm/s)\r\n");
  queueText("0=ramps to hold while running; p=status, ?=help\r\n");
  queueText("a2=accel/decel 2 cm/s^2 (range 0.1..50)\r\n");
  queueText("Send with Newline. A target change alone does not start the motor.\r\n");
}

void stopMotion() {
  currentSpeedCmPerS = 0.0f;
  wheel.setSpeed(0.0f);
  digitalWrite(STEP_PIN, LOW);
}

void disableMotor() {
  motorState = DISABLED;
  stopMotion();
  digitalWrite(ENABLE_PIN, HIGH);
  wheel.disableOutputs();
  queueStatus();
}

void holdMotor() {
  motorState = HOLDING;
  stopMotion();
  wheel.enableOutputs();
  digitalWrite(ENABLE_PIN, LOW);
  queueStatus();
}

void startMotor() {
  if (motorState != RUNNING) {
    stopMotion();
    wheel.enableOutputs();
    digitalWrite(ENABLE_PIN, LOW);
    lastRampUs = micros();
    motorState = RUNNING;
  }
  queueStatus();
}

bool isSpace(char c) {
  return c == ' ' || c == '\t';
}

void processCommand(char *command) {
  while (isSpace(*command)) ++command;
  size_t length = strlen(command);
  while (length > 0 && isSpace(command[length - 1])) command[--length] = '\0';
  if (length == 0) return;

  if (length == 1) {
    switch (command[0]) {
      case 'r': case 'R': startMotor(); return;
      case 's': case 'S': disableMotor(); return;
      case 'h': case 'H': holdMotor(); return;
      case 'p': case 'P': queueStatus(); return;
      case '?': queueHelp(); return;
      case '+':
        targetSpeedCmPerS += SPEED_INCREMENT_CM_PER_S;
        if (targetSpeedCmPerS > MAX_SPEED_CM_PER_S) targetSpeedCmPerS = MAX_SPEED_CM_PER_S;
        queueStatus(); return;
      case '-':
        targetSpeedCmPerS -= SPEED_INCREMENT_CM_PER_S;
        if (targetSpeedCmPerS < 0.0f) targetSpeedCmPerS = 0.0f;
        queueStatus(); return;
    }
  }

  const bool accelerationCommand = command[0] == 'a' || command[0] == 'A';
  char *number = accelerationCommand ? command + 1 : command;
  char *end = number;
  const float requested = strtod(number, &end);
  const bool validNumber = end != number && *end == '\0' && isfinite(requested);
  if (accelerationCommand) {
    if (validNumber && requested >= MIN_ACCELERATION_CM_PER_S2 &&
        requested <= MAX_ACCELERATION_CM_PER_S2) {
      accelerationCmPerS2 = requested;
      queueStatus();
    } else {
      queueText("Invalid acceleration. Use a0.1 through a50, e.g. a2.\r\n");
    }
  } else if (validNumber &&
      requested >= 0.0f && requested <= MAX_SPEED_CM_PER_S) {
    targetSpeedCmPerS = requested;
    queueStatus();
  } else {
    queueText("Invalid command. Use r/s/h/+/-/p/?, a2 or a speed from 0 to 60.\r\n");
  }
}

void readSerial() {
  // Read one character per pass so motor servicing stays frequent.
  if (Serial.available() <= 0) return;
  const char c = (char)Serial.read();
  if (c == '\n' || c == '\r') {
    if (commandOverflow) {
      queueText("Command too long; ignored.\r\n");
    } else {
      commandBuffer[commandLength] = '\0';
      processCommand(commandBuffer);
    }
    commandLength = 0;
    commandOverflow = false;
  } else if (!commandOverflow) {
    if (commandLength < sizeof(commandBuffer) - 1) {
      commandBuffer[commandLength++] = c;
    } else {
      commandOverflow = true;
    }
  }
}

void updateRamp() {
  if (motorState != RUNNING) return;
  const unsigned long nowUs = micros();
  const unsigned long elapsedUs = nowUs - lastRampUs;
  if (elapsedUs < RAMP_UPDATE_US) return;
  lastRampUs = nowUs;
  if (currentSpeedCmPerS == targetSpeedCmPerS) return;
  // Limit a speed jump if loop servicing was interrupted for an unusually long time.
  const unsigned long boundedElapsedUs = elapsedUs > 20000UL ? 20000UL : elapsedUs;
  const float change = accelerationCmPerS2 * boundedElapsedUs / 1000000.0f;
  if (currentSpeedCmPerS < targetSpeedCmPerS) {
    currentSpeedCmPerS += change;
    if (currentSpeedCmPerS > targetSpeedCmPerS) currentSpeedCmPerS = targetSpeedCmPerS;
  } else {
    currentSpeedCmPerS -= change;
    if (currentSpeedCmPerS < targetSpeedCmPerS) currentSpeedCmPerS = targetSpeedCmPerS;
  }
  wheel.setSpeed(currentSpeedCmPerS * STEPS_PER_CM);
}

void setup() {
  digitalWrite(ENABLE_PIN, HIGH);
  pinMode(ENABLE_PIN, OUTPUT);
  wheel.enableOutputs();
  wheel.setPinsInverted(REVERSE_DIRECTION, false, false);
  wheel.setMinPulseWidth(PULSE_WIDTH_US);
  wheel.setMaxSpeed(MAX_SPEED_CM_PER_S * STEPS_PER_CM);
  wheel.setSpeed(0.0f);
  wheel.disableOutputs();

  Serial.begin(115200);
  queueText("Left-wheel diagnostic 1.5: AccelStepper, quarter stepping\r\n");
  queueStatus();
  queueHelp();
}

void loop() {
  // runSpeed() supplies continuous motion without an arbitrary position target.
  // It does not apply AccelStepper's setAcceleration(); updateRamp() handles
  // gradual acceleration AND deceleration of the commanded wheel speed.
  wheel.runSpeed();
  updateRamp();
  wheel.runSpeed();
  readSerial();
  wheel.runSpeed();
  if (txTail != txHead && Serial.availableForWrite() > 0) {
    Serial.write((uint8_t)txBuffer[txTail]);
    txTail = (txTail + 1) % TX_CAPACITY;
  }
}
