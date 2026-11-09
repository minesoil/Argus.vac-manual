#pragma once
#include <cstdint>
#include <string>
#include <sstream>
#include <cstring>

#define PROGMEM
#define SERIAL_8N1 0
using byte = uint8_t;
extern uint32_t testNow;
inline unsigned long millis() { return testNow; }
inline void delay(unsigned long) {}
inline uint32_t esp_random() { static uint32_t value = 500; return ++value; }

class String {
 public:
  std::string text;
  String() {}
  String(const char* value) : text(value) {}
  String(const std::string& value) : text(value) {}
  size_t length() const { return text.length(); }
  char operator[](size_t i) const { return text[i]; }
  const char* c_str() const { return text.c_str(); }
};

class SerialMock {
 public:
  std::string output;
  std::string input;
  template <typename... Args> void begin(Args...) {}
  void setRxBufferSize(size_t) {}
  int available() { return input.size(); }
  int read() {
    if (input.empty()) return -1;
    uint8_t value = input.front();
    input.erase(0, 1);
    return value;
  }
  size_t write(const uint8_t* bytes, size_t count) {
    output.append(reinterpret_cast<const char*>(bytes), count);
    return count;
  }
  template <typename T> void print(T value) {
    std::ostringstream stream; stream << value; output += stream.str();
  }
  template <typename T> void println(T value) { print(value); output += "\r\n"; }
};
extern SerialMock Serial, Serial1, Serial2;
