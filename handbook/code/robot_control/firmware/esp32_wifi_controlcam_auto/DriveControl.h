#pragma once

#include <stdint.h>

enum class DriveMode { Stopped, Manual, Automatic };

class DriveControl {
 public:
  static const uint32_t TimeoutMs = 350;
  static const int AutoLimit = 35;

  DriveMode mode = DriveMode::Stopped;
  uint32_t epoch = 1;
  uint64_t session = 0;
  uint32_t lastSequence = 0;
  uint32_t lastCommandAt = 0;
  int left = 0;
  int right = 0;
  const char* reason = "Start stopped; select manual or automatic control";

  void reset(uint32_t initialEpoch) {
    epoch = initialEpoch ? initialEpoch : 1;
    mode = DriveMode::Stopped;
    session = 0;
    left = right = 0;
    lastSequence = 0;
    reason = "Start stopped; select manual or automatic control";
  }

  void stop(const char* message) {
    mode = DriveMode::Stopped;
    session = 0;
    left = right = 0;
    lastSequence = 0;
    ++epoch;
    reason = message;
  }

  bool expire(uint32_t now) {
    if (mode != DriveMode::Stopped && now - lastCommandAt >= TimeoutMs) {
      stop("Command expired; select control again");
      return true;
    }
    return false;
  }

  bool arm(DriveMode requestedMode, uint32_t expectedEpoch,
           uint64_t newSession, uint32_t now) {
    expire(now);
    if (expectedEpoch != epoch || requestedMode == DriveMode::Stopped || !newSession) {
      return false;
    }
    ++epoch;
    mode = requestedMode;
    session = newSession;
    left = right = 0;
    lastSequence = 0;
    lastCommandAt = now;
    reason = requestedMode == DriveMode::Manual ? "Manual selected" : "Automatic selected";
    return true;
  }

  bool command(DriveMode requestedMode, uint64_t requestSession,
               uint32_t sequence, int requestedLeft, int requestedRight,
               uint32_t now) {
    expire(now);
    int limit = requestedMode == DriveMode::Automatic ? AutoLimit : 100;
    if (mode != requestedMode || mode == DriveMode::Stopped ||
        !requestSession || requestSession != session || sequence <= lastSequence ||
        requestedLeft < -limit || requestedLeft > limit ||
        requestedRight < -limit || requestedRight > limit) {
      return false;
    }
    left = requestedLeft;
    right = requestedRight;
    lastSequence = sequence;
    lastCommandAt = now;
    reason = requestedMode == DriveMode::Manual ? "Manual command" : "Automatic command";
    return true;
  }

  bool stopAutomatic(uint64_t requestSession, uint32_t now) {
    expire(now);
    if (mode != DriveMode::Automatic || !requestSession || requestSession != session) {
      return false;
    }
    stop("Automatic controller stopped; select control again");
    return true;
  }
};
