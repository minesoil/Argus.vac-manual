#pragma once
#include <stdint.h>
#include <stddef.h>
#include <algorithm>
#include <string>
using std::min;
using std::max;
constexpr unsigned long F_CPU=16000000;
#define _BV(x) (1u<<(x))
enum {PA0=0,PA1=1,PA2=2,PA3=3,PA4=4,PA5=5,WGM12=3,CS11=1,OCIE1A=1};
inline uint8_t PORTA=0,DDRA=0,PINA=0,MCUSR=0,TCCR1A=0,TCCR1B=0,TIMSK1=0;
inline uint16_t OCR1A=0;
inline uint32_t clockMs=0;
inline uint32_t millis(){return clockMs;}
#define ISR(name) void name()
struct FakeSerial {
  std::string input, output;
  void begin(unsigned long){}
  int available(){return input.size();}
  int read(){char c=input[0];input.erase(0,1);return c;}
  int availableForWrite(){return 128;}
  void print(const char* value){output+=value;}
};
inline FakeSerial Serial;
