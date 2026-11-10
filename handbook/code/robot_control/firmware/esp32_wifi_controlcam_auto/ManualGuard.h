#pragma once
#include "DriveControl.h"

// Camera assistance is opt-in. A clear report never resumes a stopped drive.
class ManualGuard {
 public:
  static const uint32_t TimeoutMs = 800;
  uint64_t token = 0;
  uint32_t sequence = 0, updatedAt = 0;
  int code = 2; // 0: no anomaly, 1: blocked, 2: unavailable/uncalibrated.
  bool received = false, selected = false, latched = false;

  void connect(uint64_t newToken) {
    token = newToken; sequence = 0; received = false; code = 2;
    if (selected) latched = true;
  }
  bool report(uint64_t requestToken, uint32_t seq, int state, uint32_t now) {
    if (!requestToken || requestToken != token || seq <= sequence || state < 0 || state > 2) return false;
    sequence = seq; code = state; updatedAt = now; received = true;
    if (selected && state != 0) latched = true;
    return true;
  }
  bool clear(uint32_t now) const {
    return received && code == 0 && uint32_t(now - updatedAt) < TimeoutMs;
  }
  const char* state(uint32_t now) const {
    if (!received || uint32_t(now - updatedAt) >= TimeoutMs || code == 2) return "unavailable";
    return code == 1 ? "blocked" : "clear";
  }
  bool tick(DriveControl& control, uint32_t now) {
    if (!selected) return false;
    if (!clear(now)) latched = true;
    if (latched && control.mode == DriveMode::Manual) {
      control.stop(code == 1 && received && uint32_t(now - updatedAt) < TimeoutMs
                     ? "Camera obstacle; assisted drive stopped"
                     : "Camera unavailable; assisted drive stopped");
      return true;
    }
    return false;
  }
  bool permits(int left, int right, uint32_t now) const {
    return !selected || (!latched && clear(now) && left >= 0 && right >= 0 && left <= 35 && right <= 35);
  }
};
