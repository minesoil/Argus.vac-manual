#pragma once
#define ATOMIC_RESTORESTATE 0
#define ATOMIC_BLOCK(value) for(bool atomicOnce=true;atomicOnce;atomicOnce=false)
