import json
import re
import subprocess
from pathlib import Path

def stats(text):
    samples = []
    for match in re.finditer(r'sim_time\s*\{(.*?)\}\s*real_time\s*\{(.*?)\}', text, re.S):
        values = []
        for block in match.groups():
            seconds = re.search(r'\bsec:\s*(\d+)', block)
            nanos = re.search(r'\bnsec:\s*(\d+)', block)
            values.append((int(seconds[1]) if seconds else 0)+(int(nanos[1]) if nanos else 0)*1e-9)
        samples.append(values)
    if len(samples) < 2:
        raise RuntimeError('No usable Gazebo stats samples')
    return (samples[-1][0]-samples[0][0])/(samples[-1][1]-samples[0][1])

capture = subprocess.run(['timeout', '12', 'gz', 'topic', '-e', '-t', '/world/vacuum_room/stats'],
                         stdout=subprocess.PIPE, text=True)
Path('/tmp/vacuum-tuned-stats.txt').write_text(capture.stdout)
result = dict(baseline_real_time_factor=stats(Path('/tmp/vacuum-baseline-stats.txt').read_text()),
              tuned_real_time_factor=stats(capture.stdout))
Path('/home/robot/vacuum_ws/performance-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
