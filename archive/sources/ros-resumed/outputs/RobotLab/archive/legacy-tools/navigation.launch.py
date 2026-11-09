"""Local destination navigation, with only the servers used by this robot's BT."""
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, TimerAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package = Path(get_package_share_directory('vacuum_sim'))
    params = LaunchConfiguration('params_file')
    servers = [
        ('nav2_controller', 'controller_server', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_planner', 'planner_server', []),
        ('nav2_behaviors', 'behavior_server', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_velocity_smoother', 'velocity_smoother', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_collision_monitor', 'collision_monitor', []),
        ('nav2_bt_navigator', 'bt_navigator', []),
    ]
    actions = [DeclareLaunchArgument('params_file', default_value=str(package / 'config/vacuum_nav2.yaml'))]
    for pkg, name, remap in servers:
        actions.append(Node(package=pkg, executable=name, name=name,
                            parameters=[params, {'use_sim_time': True}],
                            remappings=[('/tf','tf'),('/tf_static','tf_static')] + remap,
                            output='screen'))
    # Allow process/plugin startup and local discovery before lifecycle requests.
    # All commands still pass through the gate and Collision Monitor.
    actions.append(TimerAction(period=4., actions=[Node(
        package='nav2_lifecycle_manager', executable='lifecycle_manager',
        name='lifecycle_manager_navigation', output='screen',
        parameters=[{'use_sim_time': True, 'autostart': True,
                     'node_names': [name for _, name, _ in servers],
                     'bond_timeout': 4.0}])]))
    return LaunchDescription(actions)
