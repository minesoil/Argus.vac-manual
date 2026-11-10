"""Calibrated floor-anomaly preview. No motor or serial interface lives here."""
import argparse
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading
import time
import urllib.request

import cv2
import numpy as np
from .line_preview import SnapshotReader, raw_clock

ROI = (.12, .76, .88, 1.0)
SAMPLE = (.04, .86, .25, .98)
PROFILE_LIFETIME = 900.0


def region_mask(rect, shape=(60, 80)):
    if len(rect) != 4 or not all(np.isfinite(v) for v in rect):
        raise ValueError('Invalid region')
    x1,y1,x2,y2 = rect
    if not (0 <= x1 < x2 <= 1 and 0 <= y1 < y2 <= 1):
        raise ValueError('Region must be normalized and ordered')
    h,w=shape; mask=np.zeros(shape,bool)
    mask[int(y1*h):max(int(y1*h)+1,int(y2*h)),int(x1*w):max(int(x1*w)+1,int(x2*w))]=True
    return mask


def features(frame):
    if not isinstance(frame,np.ndarray) or frame.dtype!=np.uint8 or frame.ndim!=3 or frame.shape[2]!=3 or min(frame.shape[:2])<120:
        raise ValueError('Missing or malformed camera image')
    small=cv2.resize(frame,(320,240),interpolation=cv2.INTER_AREA)
    colors=small.astype(np.float32);total=colors.sum(axis=2)+1
    gray=cv2.cvtColor(small,cv2.COLOR_BGR2GRAY).astype(np.float32)
    gx=cv2.Sobel(gray,cv2.CV_32F,1,0);gy=cv2.Sobel(gray,cv2.CV_32F,0,1)
    values=(255*colors[:,:,2]/total,255*colors[:,:,1]/total,cv2.magnitude(gx,gy),gray)
    return np.stack([v.reshape(60,4,80,4).mean(axis=(1,3)) for v in values],axis=2)


def calibrate(frames, sample=SAMPLE, now=None):
    if len(frames)<5: raise ValueError('At least five fresh calibration frames required')
    mask=region_mask(sample)
    if mask.sum()<12: raise ValueError('Calibration patch is too small')
    shape=frames[0].shape
    if any(f.shape!=shape for f in frames): raise ValueError('Camera geometry changed')
    values=np.concatenate([features(f)[mask] for f in frames])
    if np.percentile(values[:,3],90)-np.percentile(values[:,3],10)>75:
        raise ValueError('Calibration patch is not uniform; choose a clean floor patch')
    median=np.median(values,axis=0)
    spread=np.maximum(np.median(np.abs(values-median),axis=0),(2,2,3,5))
    if median[3]<35: raise ValueError('Calibration patch is too dark')
    return {'version':1,'median':median.tolist(),'spread':spread.tolist(),'shape':list(shape),
            'sample':list(sample),'created':time.time() if now is None else now}


@dataclass
class Observation:
    state: str
    reason: str
    boxes: list


def detect(frame, profile, now=None):
    now=time.time() if now is None else now
    try:
        if profile['version']!=1 or not 0<=now-profile['created']<PROFILE_LIFETIME:
            raise ValueError('Floor calibration expired; recalibrate while stopped')
        if list(frame.shape)!=profile['shape']: raise ValueError('Camera geometry changed')
        median=np.array(profile['median'],dtype=float);spread=np.array(profile['spread'],dtype=float)
        if median.shape!=(4,) or spread.shape!=(4,) or not np.isfinite(median).all() or not np.isfinite(spread).all() or (spread<=0).any():
            raise ValueError('Invalid floor calibration')
        f=features(frame);roi=region_mask(ROI)
        colored=(np.abs(f[:,:,:2]-median[:2])>np.maximum(16,4*spread[:2])).any(axis=2)
        textured=f[:,:,2]>median[2]+max(15,4*spread[2])
        dark=f[:,:,3]<median[3]*.55
        bright=f[:,:,3]>median[3]+max(60,5*spread[3])
        flags=((colored|textured|dark|bright)&roi).astype(np.uint8)
        flags=cv2.morphologyEx(flags,cv2.MORPH_CLOSE,np.ones((3,3),np.uint8))*roi.astype(np.uint8)
        count,_,stats,_=cv2.connectedComponentsWithStats(flags,connectivity=8)
        boxes=[];height,width=frame.shape[:2]
        for x,y,w,h,area in stats[1:]:
            if area<3: continue
            boxes.append([int(x*width/80),int(y*height/60),int(w*width/80),int(h*height/60)])
        return Observation('blocked' if boxes else 'clear',
                           'Appearance change in front region' if boxes else 'No floor anomaly detected',boxes)
    except (KeyError,TypeError,ValueError,AttributeError,cv2.error) as error:
        return Observation('fault',str(error),[])


def annotate(frame, observation, sample=None):
    image=frame.copy();height,width=image.shape[:2]
    x1,y1,x2,y2=ROI
    cv2.rectangle(image,(int(x1*width),int(y1*height)),(int(x2*width)-1,int(y2*height)-1),(0,180,255),2)
    if sample:
        a,b,c,d=sample;cv2.rectangle(image,(int(a*width),int(b*height)),(int(c*width),int(d*height)),(255,190,0),2)
    for x,y,w,h in observation.boxes:cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(image,observation.state.upper(),(12,28),cv2.FONT_HERSHEY_SIMPLEX,.7,(0,0,255) if observation.state!='clear' else (0,180,0),2)
    return image


PAGE='''<!doctype html><meta name="viewport" content="width=device-width, initial-scale=1"><title>Argus camera preview</title>
<style>body{font:15px system-ui;background:#f8f8f5;color:#222;max-width:900px;margin:30px auto;padding:0 20px}img{width:100%;max-width:640px}pre{white-space:pre-wrap}small{color:#666}</style>
<h1>Camera obstacle preview</h1><p>Amber: watched front region · Red: appearance changes</p><img id="frame"><h2 id="state">Loading…</h2><pre id="details"></pre>
<small>Calibration-based preview. No motor commands. Objects outside the marked view are not covered.</small>
<script>async function update(){try{let r=await fetch('/status',{cache:'no-store'});let s=await r.json();document.getElementById('state').textContent=s.state+' — '+s.reason;document.getElementById('details').textContent=JSON.stringify(s,null,2);document.getElementById('frame').src='/frame.jpg?t='+Date.now()}catch{document.getElementById('state').textContent='Preview connection lost'}}setInterval(update,350);update()</script>'''


class Preview:
    def __init__(self,profile,profile_path=None):
        self.profile=profile;self.profile_path=profile_path;self.revision=None
        self.lock=threading.Lock();self.latest={'state':'fault','reason':'Waiting for camera','captured_at':None};self.jpeg=None;self.ended=threading.Event()
    def refresh_profile(self):
        if self.profile_path is None:return
        if self.profile_path.with_suffix('.calibrating').exists():raise ValueError('Floor calibration in progress')
        revision=self.profile_path.stat().st_mtime_ns
        if revision!=self.revision:
            self.profile=json.loads(self.profile_path.read_text(encoding='utf-8'));self.revision=revision
    def status(self):
        with self.lock: result=dict(self.latest)
        at=result.get('captured_at');age=None if at is None else raw_clock()-at
        result['age_ms']=None if age is None else round(age*1000,1)
        if age is None or not 0<=age<=.25:result.update(state='fault',reason='Camera frame unavailable or stale')
        return result
    def run(self):
        camera=SnapshotReader();clear=0
        while not self.ended.is_set():
            started=time.monotonic()
            try:
                self.refresh_profile()
                frame=camera.read(timeout=.20);observation=detect(frame,self.profile)
                if not camera.is_fresh():raise ValueError('Frame expired during analysis')
                clear=clear+1 if observation.state=='clear' else 0
                if observation.state=='clear' and clear<3:observation=Observation('fault','Checking consecutive clear frames',[])
                ok,jpeg=cv2.imencode('.jpg',annotate(frame,observation,self.profile.get('sample')),[cv2.IMWRITE_JPEG_QUALITY,70])
                if not ok:raise ValueError('Preview encoding failed')
                with self.lock:
                    self.jpeg=jpeg.tobytes();self.latest={'state':observation.state,'reason':observation.reason,'boxes':observation.boxes,'captured_at':camera.last_grab,'processing_ms':round((time.monotonic()-started)*1000,1)}
            except (OSError,ValueError,RuntimeError,cv2.error) as error:
                clear=0
                with self.lock:self.latest={'state':'fault','reason':str(error),'captured_at':None}
            self.ended.wait(max(0,.1-(time.monotonic()-started)))


def serve(profile,port,profile_path=None):
    preview=Preview(profile,profile_path)
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*_):pass
        def do_GET(self):
            route=self.path.split('?')[0]
            if route=='/status':body=json.dumps(preview.status()).encode();kind='application/json'
            elif route=='/':body=PAGE.encode();kind='text/html; charset=utf-8'
            elif route=='/frame.jpg':
                with preview.lock:body=preview.jpeg
                if body is None:self.send_error(503);return
                kind='image/jpeg'
            else:self.send_error(404);return
            self.send_response(200);self.send_header('Content-Type',kind);self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
    server=ThreadingHTTPServer(('127.0.0.1',port),Handler)
    thread=threading.Thread(target=preview.run,daemon=True);thread.start()
    print(f'Stationary obstacle preview on 127.0.0.1:{port}; no motor interface.',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:preview.ended.set();server.server_close();thread.join(timeout=1)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--profile',type=Path,required=True);p.add_argument('--calibrate',action='store_true');p.add_argument('--sample',type=float,nargs=4,default=SAMPLE);p.add_argument('--port',type=int,default=8767);a=p.parse_args()
    if a.calibrate:
        with urllib.request.urlopen('http://127.0.0.1:8766/state',timeout=1) as reply: state=json.load(reply)
        if state.get('mode')!='stopped' or state.get('left')!=0 or state.get('right')!=0:
            p.error('Press STOP before calibrating the floor')
        a.profile.parent.mkdir(parents=True,exist_ok=True);marker=a.profile.with_suffix('.calibrating');marker.write_text('Calibration in progress')
        try:
            frames=[];camera=SnapshotReader()
            for _ in range(10):frames.append(camera.read());time.sleep(.1)
            profile=calibrate(frames,a.sample);pending=a.profile.with_suffix('.pending');pending.write_text(json.dumps(profile),encoding='utf-8');pending.replace(a.profile)
        finally:marker.unlink(missing_ok=True)
        print('Floor patch calibrated. This does not certify the watched region clear.');return
    serve({},a.port,a.profile)


if __name__=='__main__':main()
