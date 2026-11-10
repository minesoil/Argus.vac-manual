"""Publish camera observations to the ESP32's assisted-manual stop gate."""
import json
import math
import re
import urllib.request
from .follow import ControlError
from .line_preview import raw_clock


def observation_code(status, now):
    """A stale, future, malformed or expensive observation is never clear."""
    if not isinstance(status,dict):return 2
    at=status.get('captured_at');elapsed=status.get('processing_ms')
    if type(at) not in (int,float) or type(elapsed) not in (int,float):return 2
    if not all(math.isfinite(v) for v in (at,elapsed,now)) or not 0<=now-at<=.25 or not 0<=elapsed<=200:return 2
    return {'clear':0,'blocked':1}.get(status.get('state'),2)


def read_observation(url):
    with urllib.request.urlopen(url,timeout=.08) as reply:
        data=reply.read(8193)
    if len(data)>8192:raise ValueError('Guard response too large')
    return json.loads(data)


class GuardPublisher:
    def __init__(self,controller,url,fetch=read_observation,clock=raw_clock):
        self.controller=controller;self.url=url;self.fetch=fetch;self.clock=clock
        self.token=None;self.sequence=0
    def tick(self,state):
        try:
            if not self.token:
                reply=self.controller.request('/guard/arm',{'epoch':state['epoch']})
                token=reply.get('guard_token')
                if not isinstance(token,str) or not re.fullmatch('[0-9a-fA-F]{16}',token) or not int(token,16):
                    raise ControlError('ESP32 does not provide the camera-guard protocol')
                self.token=token;self.sequence=0
            try:code=observation_code(self.fetch(self.url),self.clock())
            except (OSError,ValueError,TypeError):code=2
            self.sequence+=1
            self.controller.request('/guard/update',{'session':self.token,'seq':self.sequence,'code':code})
            return code
        except ControlError as error:
            self.token=None
            if error.status!=409:raise
            return 2
