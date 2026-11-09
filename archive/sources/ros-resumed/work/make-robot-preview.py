from pathlib import Path
out=Path(__file__).resolve().parents[1]/'outputs'
text=(out/'capture_room_preview.py').read_text()
text=text.replace('room_preview','robot_preview')
text=text.replace('-12.0 -10.0 20.0 0 0.91 0.695','.4 -.42 .19 0 .17 2.332')
text=text.replace('<horizontal_fov>1.6</horizontal_fov>','<horizontal_fov>1.0</horizontal_fov>')
text=text.replace('<width>1200</width><height>900</height>','<width>1400</width><height>850</height>')
text=text.replace('room-overview.png','robot-hardware.png')
text=text.replace('try:\n    result=', '''try:
    reset=subprocess.run(['gz','service','-s','/world/vacuum_room/set_pose',
                         '--reqtype','gz.msgs.Pose','--reptype','gz.msgs.Boolean','--timeout','5000',
                         '--req','name: "vacuum", position: {x: 0 y: 0 z: 0.015}, orientation: {w: 1}'],
                         capture_output=True,text=True,timeout=8)
    assert reset.returncode==0 and 'true' in reset.stdout,reset.stdout+reset.stderr
    time.sleep(1)
    result=''')
(out/'capture_robot_preview.py').write_text(text)
print('Robot close-up capture prepared.')
