#pragma once
#include <stddef.h>
#include <stdint.h>

// Independent receiver for the Pi GPIO UART. USB camera parsing stays separate.
class ControlPacketParser {
 public:
  static constexpr size_t MaxPayload = 160;
  char payload[MaxPayload + 1] = {};

  void reset() { stage = magicPosition = lengthPosition = received = expected = 0; }

  void expire(uint32_t now) {
    if ((stage || magicPosition) && uint32_t(now - lastByte) > 250) reset();
  }

  bool feed(uint8_t value, uint32_t now) {
    expire(now);
    lastByte = now;
    static const uint8_t magic[] = {0xA5, 0xDA, 0xC3, 0xBC};
    if (stage == 0) {
      magicPosition = value == magic[magicPosition] ? magicPosition + 1
                                                  : (value == magic[0] ? 1 : 0);
      if (magicPosition == 4) { stage = 1; magicPosition = 0; }
      return false;
    }
    if (value < 0x80) { reset(); return false; }
    if (stage == 1) {
      expected |= uint16_t(value & 0x7f) << (7 * lengthPosition++);
      if (lengthPosition == 2) {
        if (!expected || expected > MaxPayload) reset();
        else stage = 2;
      }
      return false;
    }
    value &= 0x7f;
    if (!value) { reset(); return false; }
    payload[received++] = char(value);
    if (received == expected) {
      payload[received] = '\0';
      reset();
      return true;
    }
    return false;
  }

 private:
  uint8_t stage = 0, magicPosition = 0, lengthPosition = 0;
  uint16_t expected = 0, received = 0;
  uint32_t lastByte = 0;
};
