#pragma once
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

// CRC-16/CCITT-FALSE over the ASCII bytes before the last comma.
inline uint16_t crc16(const char* data, size_t length) {
  uint16_t crc = 0xffff;
  for (size_t i = 0; i < length; ++i) {
    crc ^= uint16_t(uint8_t(data[i])) << 8;
    for (uint8_t bit = 0; bit < 8; ++bit)
      crc = crc & 0x8000 ? uint16_t((crc << 1) ^ 0x1021) : uint16_t(crc << 1);
  }
  return crc;
}

struct DriveCommand { uint16_t sequence; bool enabled; int16_t left; int16_t right; };

inline bool number(char* value, long lower, long upper, long& result) {
  if (!value || !*value || *value == '+' || *value == ' ') return false;
  char* end = nullptr;
  result = strtol(value, &end, 10);
  return *end == '\0' && result >= lower && result <= upper;
}

inline bool parseCommand(char* line, DriveCommand& command, int16_t maxRate) {
  char* checksum = strrchr(line, ',');
  if (!checksum || strlen(checksum + 1) != 4) return false;
  for (const char* p = checksum + 1; *p; ++p)
    if (!((*p >= '0' && *p <= '9') || (*p >= 'A' && *p <= 'F') || (*p >= 'a' && *p <= 'f'))) return false;
  char* end = nullptr;
  unsigned long expected = strtoul(checksum + 1, &end, 16);
  if (*end || crc16(line, size_t(checksum - line)) != expected) return false;
  *checksum = '\0';
  // strtok collapses empty fields, so reject them before tokenizing.
  if (strstr(line, ",,") || line[strlen(line)-1] == ',') return false;
  char* context = nullptr;
  char* fields[6] = {};
  uint8_t count = 0;
  for (char* p = strtok_r(line, ",", &context); p && count < 6; p = strtok_r(nullptr, ",", &context)) fields[count++] = p;
  if (count != 5 || strcmp(fields[0], "V1")) return false;
  long sequence, enabled, left, right;
  if (!number(fields[1], 0, 65535, sequence) || !number(fields[2], 0, 1, enabled) ||
      !number(fields[3], -maxRate, maxRate, left) || !number(fields[4], -maxRate, maxRate, right)) return false;
  command = {uint16_t(sequence), enabled == 1, int16_t(left), int16_t(right)};
  return true;
}
