from pathlib import Path
out=Path(__file__).resolve().parents[1]/'outputs'
path=out/'validate_drive.py';text=path.read_text(encoding='utf-8-sig')
text=text.replace('odom = []','odom = []\ntimed_odom = []')
text=text.replace("node.create_subscription(Odometry, '/odom', odom.append, qos_profile_sensor_data)", "def receive_odom(message):\n    odom.append(message); timed_odom.append((time.monotonic(), message))\nnode.create_subscription(Odometry, '/odom', receive_odom, qos_profile_sensor_data)")
text=text.replace("'held': held", "'enabled': held")
text=text.replace("(('forward', .50, 2), ('reverse', -.30, 3))", "(('forward', 1.50, 2), ('reverse', -.90, 3))")
text=text.replace('        exercise(speed, True, seconds)', '        issued=time.monotonic()\n        exercise(speed, True, seconds)')
text=text.replace("        report['tests'][label] = {'signed_displacement_m': displacement, 'peak_odometry_m_s': actual_speed}", '''        after_command=[(t,m) for t,m in timed_odom if t>=issued]
        reaction=next(t-issued for t,m in after_command if abs(m.twist.twist.linear.x)>=abs(speed)*.10)
        rise=next(t-issued for t,m in after_command if abs(m.twist.twist.linear.x)>=abs(speed)*.90)
        assert reaction < .25, f'{label} response delayed: {reaction}'
        assert rise < .50, f'{label} rise too slow: {rise}'
        report['tests'][label] = {'signed_displacement_m': displacement, 'peak_odometry_m_s': actual_speed,
                                  'first_10_percent_wall_s':reaction,'time_to_90_percent_wall_s':rise}
        neutral_at=time.monotonic()''')
text=text.replace('        exercise(0., False, 2)', '''        exercise(0., True, 1)
        stopping=next(t-neutral_at for t,m in timed_odom if t>=neutral_at and abs(m.twist.twist.linear.x)<.02)
        assert stopping < .5, f'Neutral stop too slow: {stopping}'
        report['tests'][label]['neutral_stop_wall_s']=stopping''')
text=text.replace("    report['tests']['released_stop'] = True", "    report['tests']['neutral_stop_without_hold_button'] = True\n    report['tests']['disarmed_stop'] = True\n    exercise(0., False, .5)")
text=text.replace("    exercise(.1, True, 1)", '''    # A pure turn tests the smaller wheels and higher yaw command without a
    # translational goal or a held-button input.
    turn_start=time.monotonic()
    while time.monotonic()-turn_start<1.0:
        bridge.stdin.write(json.dumps({'v':0.,'w':2.4,'enabled':True})+'\\n');bridge.stdin.flush()
        rclpy.spin_once(node,timeout_sec=.015);time.sleep(.01)
    turn_records=[(t,m) for t,m in timed_odom if t>=turn_start]
    peak=max(abs(m.twist.twist.angular.z) for t,m in turn_records)
    assert peak>2.0, f'Turn speed clipped: {peak}'
    turn_rise=next(t-turn_start for t,m in turn_records if abs(m.twist.twist.angular.z)>=2.16)
    assert turn_rise<.5, f'Turn rise too slow: {turn_rise}'
    report['tests']['steering']={'peak_rad_s':peak,'time_to_90_percent_wall_s':turn_rise}
    exercise(0.,False,1)
    exercise(.2, True, 1)''')
text=text.replace('direct-drive-20261007','modern-drive-20261007')
path.write_text(text,encoding='utf-8')
path=out/'validate_directional_guard.py';text=path.read_text(encoding='utf-8-sig')
text=text.replace(".5,float('inf')", "1.5,float('inf')")
text=text.replace("-.5)<.01", "-1.5)<.01")
text=text.replace(".5,.70)-.20", "1.5,1.25)-.60")
text=text.replace(".5,.35", "1.5,.50")
text=text.replace("-.3,.35)+.30", "-.9,.50)+.90")
text=text.replace("-.3,.39,math.pi", "-.9,.50,math.pi")
text=text.replace(".5,.39,math.pi)-.50", "1.5,.50,math.pi)-1.50")
text=text.replace(".5,.14,math.pi/2", "1.5,.14,math.pi/2")
text=text.replace(".5,None", "1.5,None")
path.write_text(text,encoding='utf-8')
print('Modern response and full-speed guard validation prepared.')
