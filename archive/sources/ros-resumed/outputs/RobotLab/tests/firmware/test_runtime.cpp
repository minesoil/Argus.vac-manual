// Run the actual sketch against fake registers/serial; no hardware is opened.
#include <cassert>
#include <iostream>
#include "../../firmware/mega_drive/mega_drive.ino"

void advance(unsigned ms) {
  for(unsigned n=0;n<ms;++n){for(unsigned t=0;t<TIMER_HZ/1000;++t) TIMER1_COMPA_vect();++clockMs;loop();}
}
void send(uint16_t sequence,bool enabled,int left,int right) {
  char payload[70],packet[80];
  snprintf(payload,sizeof(payload),"V1,%u,%u,%d,%d",sequence,enabled?1:0,left,right);
  snprintf(packet,sizeof(packet),"%s,%04X\n",payload,crc16(payload,strlen(payload)));
  Serial.input+=packet;loop();
}
int main() {
  setup(); assert(!armed);
  send(1,true,1000,1000); assert(!armed); // Moving boot command cannot arm.
  send(2,false,0,0);advance(10);assert(zeroSeen);
  send(3,true,0,0);assert(armed);advance(5);
  send(4,true,1000,1000);advance(100);send(5,true,1000,1000);advance(100);
  assert(armed&&steps[0]>50&&steps[1]>50);
  send(6,true,-1000,-1000);advance(150);send(7,true,-1000,-1000);advance(250);
  assert(rates[0]<0&&rates[1]<0); // Reversal ramps through zero.
  advance(400);assert(!armed&&rates[0]==0&&rates[1]==0); // Independent timer timeout.
  send(8,true,0,0);assert(!armed); // Timeout requires a new disabled zero handshake.
  send(9,false,0,0);send(10,true,0,0);assert(armed);
  PINA|=STOP;advance(1);assert(!armed&&fault==2);
  PINA&=~STOP;send(11,false,0,0);send(12,true,0,0);assert(armed);
  Serial.input="V1,13,1,200,200,0000\n";loop();assert(!armed&&fault==3);
  send(14,false,0,0);send(15,true,0,0);assert(armed);
  send(15,true,200,200);assert(!armed&&fault==3); // Replayed enabled sequence.
  send(0,false,0,0);advance(5);send(1,true,0,0);assert(armed); // USB caller restart.
  assert(crc16("123456789",9)==0x29b1);
  std::cout<<"Firmware boot, pulses, reversal, timeout, stop loop, checksum, replay and reconnect passed.\n";
}
