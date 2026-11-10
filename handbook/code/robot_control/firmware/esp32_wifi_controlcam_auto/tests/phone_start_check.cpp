#include "../PhoneStart.h"
#include <cassert>
#include <stdint.h>

int main() {
  PhoneStart p;
  assert(!p.request(1, 1, false, 100, 11));
  assert(!p.request(2, 1, true, 100, 11));
  assert(!p.request(1, 1, true, 100, 0));
  assert(p.request(1, 1, true, 100, 11));
  assert(!p.request(1, 1, true, 101, 12));
  assert(!p.claim(1, 12, 1, true, 102));
  assert(p.claim(1, 11, 1, true, 103));
  assert(!p.claim(1, 11, 1, true, 104));
  assert(!p.request(1, 1, true, 105, 13));
  assert(p.request(2, 2, true, 106, 14));
  assert(!p.claim(2, 14, 3, true, 107)); // Stop changed epoch
  assert(p.request(3, 3, true, 108, 15));
  assert(!p.claim(3, 15, 3, false, 109)); // manual takeover
  assert(p.request(4, 4, true, 110, 16));
  assert(!p.claim(4, 16, 4, true, 2110)); // expired
  assert(p.request(4, 4, true, 2111, 17));
  assert(!p.claim(4, 16, 4, true, 2112)); // delayed old claim
  assert(p.claim(4, 17, 4, true, 2113));
  PhoneStart rollover;
  assert(rollover.request(9, 9, true, UINT32_MAX - 1000, 22));
  assert(!rollover.claim(9, 22, 9, true, 1100));
}
