#pragma once
#include <stdint.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <deque>
#include <string>
typedef uint8_t byte;
typedef bool boolean;
#define HIGH 1
#define LOW 0
#define OUTPUT 1
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define constrain(a,l,h) ((a)<(l)?(l):((a)>(h)?(h):(a)))
unsigned long micros();
void pinMode(uint8_t pin, uint8_t mode);
void digitalWrite(uint8_t pin, uint8_t value);
void delayMicroseconds(unsigned int us);
inline char *dtostrf(double v, signed char w, unsigned char p, char *out) {
  sprintf(out, "%*.*f", (int)w, (int)p, v);
  return out;
}
struct TestSerial {
  std::deque<char> input;
  std::string output;
  int writable = 64;
  void begin(unsigned long baud) { if (baud != 115200) abort(); }
  int available() { return (int)input.size(); }
  int read() { char c = input.front(); input.pop_front(); return c; }
  int availableForWrite() { return writable; }
  size_t write(uint8_t c) { output += (char)c; return 1; }
};
extern TestSerial Serial;
