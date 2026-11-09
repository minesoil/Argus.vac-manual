"""Code-native app icon: vacuum outline in the launcher's dark/cyan palette."""
from pathlib import Path
import math
import struct
import zlib

def chunk(name,data):
    return struct.pack('>I',len(data))+name+data+struct.pack('>I',zlib.crc32(name+data))

size=256
raw=bytearray()
for y in range(size):
    raw.append(0)
    for x in range(size):
        values=[]
        for ox,oy in ((.25,.25),(.75,.25),(.25,.75),(.75,.75)):
            px,py=x+ox,y+oy;r=math.hypot(px-128,py-131)
            if 70<r<88:color=(53,222,196,255)
            elif 112<px<144 and 55<py<105:color=(234,241,250,255)
            elif 80<px<176 and 190<py<196:color=(53,222,196,255)
            else:color=(11,18,32,255)
            values.append(color)
        raw.extend(round(sum(v[c] for v in values)/4) for c in range(4))
png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',size,size,8,6,0,0,0))+chunk(b'IDAT',zlib.compress(bytes(raw)))+chunk(b'IEND',b'')
header=struct.pack('<HHH',0,1,1)+struct.pack('<BBBBHHII',0,0,0,0,1,32,len(png),22)
(Path(__file__).resolve().parents[1]/'Vacuum-Lab.ico').write_bytes(header+png)
