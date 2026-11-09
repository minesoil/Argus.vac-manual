from pathlib import Path

out=Path(__file__).resolve().parents[1]/'outputs'
for name in ('controller_bridge.py','command_gate.py'):
    path=out/name;text=path.read_text(encoding='utf-8-sig')
    text=text.replace("from pathlib import Path", "from pathlib import Path\nimport json" if name=='command_gate.py' else "from pathlib import Path")
    text=text.replace("MODE = Path('/home/robot/vacuum_ws/.lab/manual-mode')", "MODE = Path('/home/robot/vacuum_ws/.lab/manual-mode')\nPROFILE = json.loads((Path(__file__).parent / 'robot-profile.json').read_text())['drive']")
    text=text.replace("data.get('held') is not True", "data.get('enabled', data.get('held', False)) is not True")
    text=text.replace('max(-.30, min(.50, v)), max(-1.2, min(1.2, w))', "max(-PROFILE['reverse_m_s'], min(PROFILE['forward_m_s'], v)), max(-PROFILE['turn_rad_s'], min(PROFILE['turn_rad_s'], w))")
    text=text.replace('self.create_timer(.05, self.tick)', "self.create_timer(PROFILE['input_period_s'], self.tick)")
    path.write_text(text,encoding='utf-8')
path=out/'prepare_lab.py';text=path.read_text(encoding='utf-8-sig')
text=text.replace('    prepare_driving_views()\n', '    prepare_driving_views()\n    from apply_robot_profile import apply_profile\n    apply_profile()\n')
text=text.replace('At the 0.5 m/s limit a physics step covers less than 3 mm.', 'At the 1.5 m/s limit a physics step covers about 8.3 mm.')
path.write_text(text,encoding='utf-8')
path=out/'check_lab.py';text=path.read_text(encoding='utf-8-sig')
text=text.replace('(.50, 1.2)', '(1.50, 2.4)').replace('(-.30, -1.2)', '(-.90, -2.4)')
text=text.replace('    def test_manual_watchdog_and_interlock', '''    def test_armed_input_without_hold_button(self):
        self.assertEqual(controller_bridge.decode('{"v":1.5,"w":2.4,"enabled":true}'), (1.5, 2.4))
        self.assertEqual(controller_bridge.decode('{"v":1.5,"w":0,"enabled":false}'), (0., 0.))
        self.assertEqual(controller_bridge.decode('{"v":1.5,"w":0}'), (0., 0.))

    def test_manual_watchdog_and_interlock''')
path.write_text(text,encoding='utf-8')
print('Drive profile, 50 Hz bridge/gate, no-hold protocol and checks updated.')
