#pragma once
#include "Arduino.h"
#define WIFI_AP 0
struct WiFiMock {
  void mode(int) {}
  void softAP(const char*, const char*) {}
};
extern WiFiMock WiFi;
class WiFiClient {
 public:
  size_t write(const uint8_t*, size_t count) { return count; }
};
