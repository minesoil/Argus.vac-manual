from pathlib import Path
path = Path('/home/robot/vacuum_ws/src/vacuum_sim/launch/sim.launch.py')
text = path.read_text()
text = text.replace('RegisterEventHandler, SetEnvironmentVariable', 'RegisterEventHandler, SetEnvironmentVariable, ExecuteProcess')
old = """        IncludeLaunchDescription(PythonLaunchDescriptionSource(gz_launch), launch_arguments={
            'gz_args': '-r -s -v 3 ' + str(package / 'worlds/room.sdf')}.items()),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(gz_launch), launch_arguments={
            'gz_args': '-g -v 3'}.items(), condition=IfCondition(LaunchConfiguration('gui'))),"""
new = """        # Direct argv keeps Gazebo under launch's signal handling; a shell wrapper
        # previously exited first and left its Gazebo child running.
        ExecuteProcess(cmd=['gz', 'sim', '-r', '-s', '-v', '2', str(package / 'worlds/room.sdf')], output='screen'),
        ExecuteProcess(cmd=['gz', 'sim', '-g', '-v', '2'], output='screen', condition=IfCondition(LaunchConfiguration('gui'))),"""
assert text.count(old) == 1
path.write_text(text.replace(old, new))
