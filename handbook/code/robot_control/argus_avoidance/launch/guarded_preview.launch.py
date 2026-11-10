"""Isolated selected/guarded topics. No motor, lidar-driver or simulator startup."""

from pathlib import Path
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    share = Path(get_package_share_directory("argus_avoidance"))
    guard_config = "preview_guard_humble.yaml" if os.environ.get("ROS_DISTRO") == "humble" else "preview_guard.yaml"
    sim_time = ParameterValue(LaunchConfiguration("use_sim_time"), value_type=bool)
    return LaunchDescription([
        DeclareLaunchArgument("use_sim_time", default_value="false"),
        DeclareLaunchArgument("enable_output", default_value="false"),
        DeclareLaunchArgument("config", default_value=str(share / "config/avoidance.yaml")),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(str(share / "launch/avoidance.launch.py")),
            launch_arguments={
                "config": LaunchConfiguration("config"),
                "use_sim_time": LaunchConfiguration("use_sim_time"),
                "enable_output": LaunchConfiguration("enable_output"),
                "output_topic": "/avoidance/guard_input",
                "guard_service": "/avoidance_preview_guard/get_state",
            }.items(),
        ),
        Node(
            package="nav2_collision_monitor", executable="collision_monitor",
            name="avoidance_preview_guard", output="screen",
            parameters=[str(share / "config" / guard_config), {"use_sim_time": sim_time}],
        ),
        Node(
            package="nav2_lifecycle_manager", executable="lifecycle_manager",
            name="avoidance_preview_lifecycle_manager", output="screen",
            parameters=[{
                "autostart": True, "node_names": ["avoidance_preview_guard"],
                "use_sim_time": sim_time,
            }],
        ),
    ])
