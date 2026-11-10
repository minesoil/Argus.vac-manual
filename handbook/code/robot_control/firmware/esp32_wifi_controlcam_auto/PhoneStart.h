#pragma once
#include <stdint.h>

// A Start is a short-lived, one-shot request bound to the stopped epoch.
class PhoneStart {
 public:
  bool pending = false;
  uint32_t epoch = 0;
  uint32_t requestedAt = 0;
  uint64_t requestToken = 0;
  bool consumed = false;
  uint32_t consumedEpoch = 0;

  void expire(uint32_t now, uint32_t currentEpoch, bool stopped) {
    if (pending && (!stopped || currentEpoch != epoch || now - requestedAt >= 2000))
      pending = false;
  }

  bool request(uint32_t expectedEpoch, uint32_t currentEpoch, bool stopped, uint32_t now,
               uint64_t token) {
    expire(now, currentEpoch, stopped);
    if (!token || !stopped || expectedEpoch != currentEpoch || pending ||
        (consumed && consumedEpoch == currentEpoch)) return false;
    epoch = currentEpoch;
    requestedAt = now;
    requestToken = token;
    pending = true;
    return true;
  }

  bool claim(uint32_t expectedEpoch, uint64_t token, uint32_t currentEpoch, bool stopped, uint32_t now) {
    expire(now, currentEpoch, stopped);
    if (!pending || expectedEpoch != epoch || !token || token != requestToken) return false;
    pending = false;
    consumed = true;
    consumedEpoch = epoch;
    return true;
  }
};
