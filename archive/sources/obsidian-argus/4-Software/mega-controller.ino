/*
  Argus Vac - Mega Controller (reconstruction v1.0)
  ============================================================
  Written 2026-08-25 from the vault's own documents because the original
  mega-diagnostic.ino lives only in the Gemini Notebook workspace and was
  never ported over. This sketch implements the SAME command contract that
  pi-hardware-validator.py already speaks:

      P        -> ping, replies with a line containing ACK
      S 1 / S 0 -> drive steppers forward / stop
      B 1 / B 0 -> brush sweepers on / off   (L298N)
      V 1 / V 0 -> vacuum fan on / off       (drv-1012)
      H        -> immediate halt of everything (latches until G)
      G        -> release halt latch (actuators stay OFF until re-commanded)
      R <name> <risk%> <cx> <cy> -> camera threat report; auto-halt at >=85%

  Pin map is the authoritative one from the Electrical Wiring & Power Reference:
      Left  stepper A4988: STEP 5,  DIR 6
      Right stepper A4988: STEP 3,  DIR 4
      L298N inputs     :   7, 8 (Frontish), 9, 10 (Backish)
      drv-1012 fan     :   PWM 11, DIR 12, BRAKE 2

  SAFETY RULES BAKED IN:
    * Boots HALTED. Nothing moves until H latch is released with G AND an
      explicit actuator command arrives.
    * H always wins instantly, from anywhere in the loop.
    * A camera R packet with risk >= AUTO_HALT_RISK triggers H by itself
      (the validator's menu option 9 behavior, automated).
    * WATCHDOG_MS: while driving, if no serial traffic for this long the robot
      stops. Default 0 = disabled for bench testing via the interactive menu.
      Set to 500 for autonomous runs (matches the Calibration Guide's rule).

  Bench-test with pi-hardware-validator.py menu options 1-9 BEFORE trusting it.
*/

#define STEP_LEFT   5
#define DIR_LEFT    6
#define STEP_RIGHT  3
#define DIR_RIGHT   4
#define BRUSH_A_IN1 7
#define BRUSH_A_IN2 8
#define BRUSH_B_IN3 9
#define BRUSH_B_IN4 10
#define FAN_PWM     11
#define FAN_DIR     12
#define FAN_BRAKE   2

#define BAUD          115200
#define STEP_INTERVAL_US 4000UL   // 250 steps/sec - slow and safe for bench
#define AUTO_HALT_RISK   85       // percent; matches THREAT_HALT_RISK on the Pi side
#define WATCHDOG_MS      0        // 0 = off for bench tests; 500 for autonomous

bool halted          = true;   // boot safe
bool driving         = false;
bool brushes_on      = false;
bool fan_on          = false;
unsigned long last_step_us = 0;
unsigned long last_serial_ms = 0;
char   threat_name[24] = "-";

void allStop() {
  driving = false;
  brushes_on = false;
  fan_on = false;
  digitalWrite(BRUSH_A_IN1, LOW); digitalWrite(BRUSH_A_IN2, LOW);
  digitalWrite(BRUSH_B_IN3, LOW); digitalWrite(BRUSH_B_IN4, LOW);
  analogWrite(FAN_PWM, 0);
}

void setup() {
  pinMode(STEP_LEFT, OUTPUT);   pinMode(DIR_LEFT, OUTPUT);
  pinMode(STEP_RIGHT, OUTPUT);  pinMode(DIR_RIGHT, OUTPUT);
  pinMode(BRUSH_A_IN1, OUTPUT); pinMode(BRUSH_A_IN2, OUTPUT);
  pinMode(BRUSH_B_IN3, OUTPUT); pinMode(BRUSH_B_IN4, OUTPUT);
  pinMode(FAN_PWM, OUTPUT);     pinMode(FAN_DIR, OUTPUT); pinMode(FAN_BRAKE, OUTPUT);

  digitalWrite(DIR_LEFT, HIGH);   // both wheels same side = forward
  digitalWrite(DIR_RIGHT, HIGH);
  digitalWrite(FAN_DIR, HIGH);
  digitalWrite(FAN_BRAKE, LOW);

  allStop();
  Serial.begin(BAUD);
  Serial.println(F("ARGUS-MEGA up. HALTED. Send P to ping."));
}

void doStepPulse() {
  digitalWrite(STEP_LEFT, HIGH);  digitalWrite(STEP_RIGHT, HIGH);
  delayMicroseconds(20);
  digitalWrite(STEP_LEFT, LOW);   digitalWrite(STEP_RIGHT, LOW);
}

void handleCommand(char* line) {
  // tokenize on spaces
  char* cmd = strtok(line, " ");
  if (cmd == NULL) return;

  if (strcmp(cmd, "P") == 0) {
    Serial.println(F("ACK ARGUS-MEGA ready"));
  }
  else if (strcmp(cmd, "H") == 0) {
    halted = true;
    allStop();
    Serial.println(F("HALT latched"));
  }
  else if (strcmp(cmd, "G") == 0) {
    halted = false;
    Serial.println(F("Halt released (actuators still OFF until commanded)"));
  }
  else if (strcmp(cmd, "S") == 0) {
    char* arg = strtok(NULL, " ");
    if (!halted && arg && arg[0] == '1') {
      driving = true;
      last_serial_ms = millis();
      Serial.println(F("Drive ON"));
    } else {
      driving = false;
      Serial.println(F("Drive OFF"));
    }
  }
  else if (strcmp(cmd, "B") == 0) {
    char* arg = strtok(NULL, " ");
    brushes_on = (!halted && arg && arg[0] == '1');
    digitalWrite(BRUSH_A_IN1, brushes_on ? HIGH : LOW);
    digitalWrite(BRUSH_A_IN2, LOW);
    digitalWrite(BRUSH_B_IN3, brushes_on ? HIGH : LOW);
    digitalWrite(BRUSH_B_IN4, LOW);
    Serial.println(brushes_on ? F("Brushes ON") : F("Brushes OFF"));
  }
  else if (strcmp(cmd, "V") == 0) {
    char* arg = strtok(NULL, " ");
    fan_on = (!halted && arg && arg[0] == '1');
    analogWrite(FAN_PWM, fan_on ? 255 : 0);
    Serial.println(fan_on ? F("Vacuum ON") : F("Vacuum OFF"));
  }
  else if (strcmp(cmd, "R") == 0) {
    char* name = strtok(NULL, " ");
    char* risk = strtok(NULL, " ");
    strncpy(threat_name, name ? name : "-", sizeof(threat_name) - 1);
    int r = risk ? atoi(risk) : 0;
    if (r >= AUTO_HALT_RISK && !halted) {
      halted = true;
      allStop();
      Serial.print(F("AUTO-HALT: camera threat "));
      Serial.print(threat_name);
      Serial.print(F(" risk "));
      Serial.println(r);
    } else {
      Serial.print(F("Threat noted: "));
      Serial.print(threat_name);
      Serial.print(F(" "));
      Serial.println(r);
    }
  }
  else {
    Serial.println(F("ERR unknown command"));
  }
}

void loop() {
  // read one full line if available
  static char buf[64];
  static byte idx = 0;
  while (Serial.available()) {
    char c = (char)Serial.read();
    if (c == '\n' || c == '\r') {
      if (idx > 0) { buf[idx] = 0; handleCommand(buf); idx = 0; }
    } else if (idx < sizeof(buf) - 1) {
      buf[idx++] = c;
    }
    last_serial_ms = millis();
  }

  unsigned long now_us = micros();
  if (driving && !halted) {
#if WATCHDOG_MS > 0
    if (millis() - last_serial_ms > WATCHDOG_MS) {
      driving = false;
      Serial.println(F("WATCHDOG: serial silence, drive stopped"));
    }
#endif
    if (driving && now_us - last_step_us >= STEP_INTERVAL_US) {
      last_step_us = now_us;
      doStepPulse();
    }
  }
}
