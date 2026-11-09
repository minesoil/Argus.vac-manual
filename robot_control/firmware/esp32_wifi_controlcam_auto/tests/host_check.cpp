// Offline HTTP route checks using the actual sketch and control state.
// WiFi, serial transport and time are stand-ins; no hardware is contacted.
#include "stubs/Arduino.h"
#include "stubs/WiFi.h"
#include <cassert>
#include <iostream>
#include <regex>

uint32_t testNow = 0;
SerialMock Serial, Serial1, Serial2;
WiFiMock WiFi;
#include "../esp32_wifi_controlcam_auto.ino"

std::string jsonValue(const std::string& body, const char* key) {
  std::smatch match;
  std::regex pattern(std::string("\"") + key + "\":(?:\"([^\"]*)\"|([0-9]+))");
  assert(std::regex_search(body, match, pattern));
  return match[1].matched ? match[1].str() : match[2].str();
}

std::string epoch() {
  assert(server.dispatch("/state", HTTP_GET) == 200);
  assert(server.responseBody.find("session") == std::string::npos);
  return jsonValue(server.responseBody, "epoch");
}

std::string arm(const char* route) {
  std::string expected = epoch();
  assert(server.dispatch(route, HTTP_POST, {{"epoch", expected}}) == 200);
  return jsonValue(server.responseBody, "session");
}

int drive(const char* route, const std::string& token, const char* sequence,
          const char* left = "5", const char* right = "5") {
  return server.dispatch(route, HTTP_POST,
                        {{"session", token}, {"seq", sequence}, {"l", left}, {"r", right}});
}

void reset() {
  testNow = 1000;
  control.reset(100);
  lastMotorSend = testNow;
  Serial2.output.clear();
  Serial1.input.clear();
  Serial1.output.clear();
  gpioControl.reset();
  phoneStart = PhoneStart();
  phoneSessionActive = false;
}

int main() {
  setup();
  assert(control.mode == DriveMode::Stopped);
  assert(Serial2.output == "\nS\n");
  assert(server.dispatch("/drive", HTTP_GET, {{"l", "100"}, {"r", "100"}}) == 400);

  reset();
  std::string automatic = arm("/auto/arm");
  assert(drive("/auto/drive", automatic, "1", "35", "-35") == 204);
  testNow += 100; updateMotors();
  assert(Serial2.output.find("M:35,-35\r\n") != std::string::npos);
  assert(drive("/auto/drive", automatic, "2", "36", "0") == 400);
  assert(control.left == 35 && control.right == -35);
  assert(drive("/auto/drive", automatic, "1") == 409);
  assert(drive("/auto/drive", automatic, "0") == 409);
  assert(drive("/drive", automatic, "2", "0", "0") == 409);

  // The stop response invalidates both a pending drive and a pending arm.
  std::string oldEpoch = epoch();
  assert(server.dispatch("/stop", HTTP_POST) == 200);
  assert(control.mode == DriveMode::Stopped);
  assert(Serial2.output.size() >= 3 && Serial2.output.substr(Serial2.output.size() - 3) == "\nS\n");
  assert(drive("/auto/drive", automatic, "2") == 409);
  assert(server.dispatch("/auto/arm", HTTP_POST, {{"epoch", oldEpoch}}) == 409);

  // Explicit manual selection takes ownership; old Pi cleanup cannot stop it.
  automatic = arm("/auto/arm");
  std::string pendingAutomaticArmEpoch = epoch();
  std::string manual = arm("/manual/arm");
  assert(server.dispatch("/auto/arm", HTTP_POST, {{"epoch", pendingAutomaticArmEpoch}}) == 409);
  assert(drive("/auto/drive", automatic, "1") == 409);
  assert(server.dispatch("/auto/stop", HTTP_POST, {{"session", automatic}}) == 409);
  assert(control.mode == DriveMode::Manual);
  assert(drive("/drive", manual, "1", "100", "-100") == 204);
  assert(drive("/drive", manual, "2", "0", "0") == 204);
  assert(control.left == 0 && control.right == 0);

  // Both modes expire at the lease boundary and cannot restart with old packets.
  for (const char* route : {"/manual/arm", "/auto/arm"}) {
    reset();
    std::string lease = arm(route);
    const char* commands = control.mode == DriveMode::Manual ? "/drive" : "/auto/drive";
    assert(drive(commands, lease, "1") == 204);
    testNow += 349; updateMotors();
    assert(control.mode != DriveMode::Stopped);
    testNow += 1; updateMotors();
    assert(control.mode == DriveMode::Stopped);
    assert(Serial2.output.substr(Serial2.output.size() - 3) == "\nS\n");
    assert(drive(commands, lease, "2") == 409);
    testNow += 100; updateMotors();
    assert(control.mode == DriveMode::Stopped);
  }

  reset();
  automatic = arm("/auto/arm");
  for (const char* bad : {"", "+1", "-1", "1x", "4294967296"}) {
    assert(drive("/auto/drive", automatic, bad) == 400);
  }
  for (const char* bad : {"", "+1", "1.0", "1x", " 1", "-36"}) {
    assert(drive("/auto/drive", automatic, "1", bad, "0") == 400);
  }
  assert(drive("/auto/drive", "0000000000000000", "1") == 400);
  assert(drive("/auto/drive", "0000000000000001", "1") == 409);
  assert(server.dispatch("/auto/stop", HTTP_POST, {{"session", automatic}}) == 200);
  assert(control.mode == DriveMode::Stopped);

  // A stopped manual session also rejects its delayed browser drive packet.
  manual = arm("/manual/arm");
  assert(server.dispatch("/stop", HTTP_POST) == 200);
  assert(drive("/drive", manual, "1", "100", "100") == 409);

  // Unsigned time subtraction preserves expiry across millis() rollover.
  testNow = UINT32_MAX - 100;
  control.reset(500);
  automatic = arm("/auto/arm");
  assert(drive("/auto/drive", automatic, "1") == 204);
  testNow += 350;
  updateMotors();
  assert(control.mode == DriveMode::Stopped);

  reset();
  assert(server.dispatch("/", HTTP_GET) == 200);
  assert(server.responseBody.find("/stop") != std::string::npos);
  assert(server.responseBody.find("ENABLE MANUAL") != std::string::npos);
  assert(server.dispatch("/frame", HTTP_GET) == 503);
  const uint8_t frame[] = {'A','V','F','1',4,0,0,0,0xff,0xd8,0xff,0xd9};
  for (uint8_t value : frame) processCameraByte(value);
  assert(frameReady && activeLength == 4);
  assert(server.dispatch("/frame", HTTP_GET) == 200);
  assert(server.responseType == "image/jpeg");

  std::cout << "PASS actual HTTP routes: ownership, stop races, expiry, bounds, malformed input, rollover, camera relay\n";

  auto usb = [](const std::string& payload) {
    Serial.output.clear();
    const uint8_t magic[] = {0xA5,0xDA,0xC3,0xBC};
    for (uint8_t value : magic) processCameraByte(value);
    for (int i = 0; i < 2; ++i) processCameraByte(0x80 | ((payload.size() >> (7*i)) & 0x7f));
    for (uint8_t value : payload) processCameraByte(value | 0x80);
    assert(Serial.output.substr(0,4) == "AVR1");
    uint32_t length = 0;
    for (int i = 0; i < 4; ++i) length |= (uint32_t)(uint8_t)Serial.output[4+i] << (8*i);
    assert(Serial.output.size() == length + 8);
    return Serial.output.substr(8);
  };
  reset();
  assert(jsonValue(usb("1,state"), "status") == "200");
  std::string serialState = usb("2,arm," + epoch());
  automatic = jsonValue(serialState, "session");
  assert(jsonValue(serialState, "request_id") == "2");
  assert(jsonValue(usb("3,drive," + automatic + ",1,5,5"), "status") == "204");
  assert(control.left == 5 && control.right == 5);
  assert(server.dispatch("/stop", HTTP_POST) == 200);
  assert(jsonValue(usb("4,drive," + automatic + ",2,5,5"), "status") == "409");
  manual = arm("/manual/arm");
  assert(jsonValue(usb("5,stop," + automatic), "status") == "409");
  assert(control.mode == DriveMode::Manual);
  reset();
  automatic = jsonValue(usb("6,arm," + epoch()), "session");
  assert(jsonValue(usb("7,drive," + automatic + ",1,36,0"), "status") == "400");
  testNow += 350;
  assert(jsonValue(usb("8,drive," + automatic + ",1,5,5"), "status") == "409");
  assert(control.mode == DriveMode::Stopped);
  assert(jsonValue(usb("9,state"), "status") == "200");
  assert(jsonValue(usb("10,state"), "max_auto_percent") == "35");
  std::cout << "PASS USB packets: framing, HTTP/USB ownership, stop, expiry, malformed input\n";

  auto packet = [](const std::string& payload) {
    std::string data("\xa5\xda\xc3\xbc", 4);
    data += char(0x80 | (payload.size() & 0x7f));
    data += char(0x80 | (payload.size() >> 7));
    for (uint8_t value : payload) data += char(value | 0x80);
    return data;
  };
  auto gpio = [&](const std::string& payload) {
    Serial1.output.clear();
    std::string usbBefore = Serial.output;
    Serial1.input += packet(payload);
    receiveGpioControl();
    assert(Serial.output == usbBefore);
    assert(Serial1.output.substr(0,4) == "AVR1");
    uint32_t length = 0;
    for (int i = 0; i < 4; ++i) length |= (uint32_t)(uint8_t)Serial1.output[4+i] << (8*i);
    assert(Serial1.output.size() == length + 8);
    return Serial1.output.substr(8);
  };
  reset();
  assert(jsonValue(gpio("1,state"), "status") == "200");
  automatic = jsonValue(gpio("2,arm," + epoch()), "session");
  assert(jsonValue(gpio("3,drive," + automatic + ",1,25,35"), "status") == "204");
  testNow += 100; updateMotors();
  assert(Serial2.output.find("M:25,35\r\n") != std::string::npos);
  assert(server.dispatch("/stop", HTTP_POST) == 200);
  assert(jsonValue(gpio("4,drive," + automatic + ",2,5,7"), "status") == "409");
  manual = arm("/manual/arm");
  assert(jsonValue(gpio("5,stop," + automatic), "status") == "409");
  assert(control.mode == DriveMode::Manual);
  reset();
  automatic = jsonValue(gpio("6,arm," + epoch()), "session");
  assert(jsonValue(gpio("7,drive," + automatic + ",1,36,0"), "status") == "400");
  testNow += 350;
  assert(jsonValue(gpio("8,drive," + automatic + ",1,5,7"), "status") == "409");
  assert(control.mode == DriveMode::Stopped);

  // A broken/expired UART packet cannot arm; the next complete packet recovers.
  reset();
  std::string partial = packet("9,arm," + epoch());
  Serial1.input = partial.substr(0, 7);
  receiveGpioControl();
  testNow += 251;
  Serial1.input = partial.substr(7);
  receiveGpioControl();
  assert(Serial1.output.empty() && control.mode == DriveMode::Stopped);
  Serial1.input = packet(std::string(161, 'x'));
  receiveGpioControl();
  assert(Serial1.output.empty());
  Serial1.input = packet(std::string("1,state\0junk", 12));
  receiveGpioControl();
  assert(Serial1.output.empty());
  assert(jsonValue(gpio("10,state"), "status") == "200");
  std::cout << "PASS GPIO UART: framing, reply routing, phone Stop, manual takeover, expiry and malformed-packet recovery\n";

  reset();
  std::string startEpoch = epoch();
  assert(server.dispatch("/follow/start", HTTP_POST, {{"epoch", startEpoch}}) == 200);
  std::string startToken = jsonValue(server.responseBody, "follow_token");
  assert(server.dispatch("/follow/start", HTTP_POST, {{"epoch", startEpoch}}) == 409);
  assert(server.dispatch("/stop", HTTP_POST) == 200);
  assert(jsonValue(gpio("10,claim," + startEpoch + "," + startToken), "status") == "409");
  assert(control.mode == DriveMode::Stopped);

  reset();
  startEpoch = epoch();
  assert(server.dispatch("/follow/start", HTTP_POST, {{"epoch", startEpoch}}) == 200);
  startToken = jsonValue(server.responseBody, "follow_token");
  manual = arm("/manual/arm");
  assert(jsonValue(gpio("10,claim," + startEpoch + "," + startToken), "status") == "409");
  assert(control.mode == DriveMode::Manual);

  reset();
  startEpoch = epoch();
  assert(server.dispatch("/follow/start", HTTP_POST, {{"epoch", startEpoch}}) == 200);
  startToken = jsonValue(server.responseBody, "follow_token");
  assert(jsonValue(gpio("11,claim," + startEpoch + "," + startToken), "status") == "200");
  assert(jsonValue(gpio("12,claim," + startEpoch + "," + startToken), "status") == "409");
  assert(server.dispatch("/stop", HTTP_POST) == 200);
  assert(server.dispatch("/auto/arm", HTTP_POST, {{"epoch", startEpoch}}) == 409);

  reset();
  startEpoch = epoch();
  assert(server.dispatch("/follow/start", HTTP_POST, {{"epoch", startEpoch}}) == 200);
  startToken = jsonValue(server.responseBody, "follow_token");
  assert(jsonValue(gpio("13,claim," + startEpoch + "," + startToken), "status") == "200");
  automatic = jsonValue(gpio("14,arm," + startEpoch), "session");
  assert(server.dispatch("/follow/heartbeat", HTTP_POST, {{"session", startToken}}) == 204);
  for (int i = 1; i <= 10; ++i) {
    testNow += 100;
    std::string reply = gpio(std::to_string(14+i) + ",drive," + automatic + "," + std::to_string(i) + ",25,25");
    assert(jsonValue(reply, "status") == (i < 10 ? "204" : "409"));
  }
  assert(control.mode == DriveMode::Stopped);
  assert(std::string(control.reason).find("Phone connection lost") != std::string::npos);
  assert(Serial2.output.substr(Serial2.output.size() - 3) == "\nS\n");

  reset();
  startEpoch = epoch();
  assert(server.dispatch("/follow/start", HTTP_POST, {{"epoch", startEpoch}}) == 200);
  startToken = jsonValue(server.responseBody, "follow_token");
  assert(jsonValue(gpio("30,claim," + startEpoch + "," + startToken), "status") == "200");
  automatic = jsonValue(gpio("31,arm," + startEpoch), "session");
  for (int i = 1; i <= 12; ++i) {
    testNow += 100;
    if (i % 4 == 0) {
      assert(server.dispatch("/follow/heartbeat", HTTP_POST, {{"session", startToken}}) == 204);
    }
    assert(jsonValue(gpio(std::to_string(31+i) + ",drive," + automatic + "," +
                          std::to_string(i) + ",25,25"), "status") == "204");
  }
  assert(control.mode == DriveMode::Automatic);
  assert(server.dispatch("/stop", HTTP_POST) == 200);
  assert(control.mode == DriveMode::Stopped);
  assert(jsonValue(gpio("50,drive," + automatic + ",13,25,25"), "status") == "409");
  assert(server.dispatch("/follow/heartbeat", HTTP_POST, {{"session", startToken}}) == 409);
  std::cout << "PASS phone start: one-shot, stop-before-arm, heartbeat watchdog, and operator Stop\n";
}
