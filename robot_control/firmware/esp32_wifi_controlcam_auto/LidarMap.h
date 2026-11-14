#pragma once

#include <stddef.h>
#include <stdint.h>
#include <string.h>

// Display-only scan cache. The Pi owns ranging and drive safety decisions.
// Pi rotates raw C1 ranges into robot heading. Ranges remain from C1;
// bin 0 is forward and bins increase clockwise in 5-degree steps.
class LidarMap {
 public:
  static constexpr size_t BinCount = 72;
  static constexpr uint32_t FreshMs = 1000;
  uint8_t bins[BinCount] = {};
  uint32_t receivedAt = 0;
  bool hasScan = false;

  bool updateBins(const uint8_t* values, size_t count, uint32_t now) {
    if (!values || count != BinCount) return false;
    for (size_t i = 0; i < BinCount; ++i) {
      if (values[i] > 240) return false;
    }
    memcpy(bins, values, BinCount);
    receivedAt = now;
    hasScan = true;
    return true;
  }

  uint32_t age(uint32_t now) const {
    return hasScan ? uint32_t(now - receivedAt) : 0;
  }

  bool fresh(uint32_t now) const {
    return hasScan && age(now) <= FreshMs;
  }

  void encodeHex(char* out) const {
    static const char digits[] = "0123456789ABCDEF";
    for (size_t i = 0; i < BinCount; ++i) {
      out[2 * i] = digits[bins[i] >> 4];
      out[2 * i + 1] = digits[bins[i] & 0x0f];
    }
    out[BinCount * 2] = '\0';
  }
};
