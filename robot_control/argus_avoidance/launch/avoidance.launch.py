"""Controller only. Does not start or arm physical hardware."""

from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    share = Path(get_package_share_directory("argus_avoidance"))
    return LaunchDescription([
        DeclareLaunchArgument("config", default_value=str(share / "config/avoidance.yaml")),
        DeclareLaunchArgument("use_sim_time", default_value="false"),
        DeclareLaunchArgument("enable_output", default_value="false"),
        DeclareLaunchArgument("output_topic", default_value="/avoidance/preview_cmd_vel"),
        DeclareLaunchArgument("scan_topic", default_value="/scan"),
        DeclareLaunchArgument("base_frame", default_value="base_link"),
        DeclareLaunchArgument("guard_service", default_value="/collision_monitor/get_state"),
        Node(
            package="argus_avoidance", executable="avoidance_controller",
            name="argus_avoidance", output="screen",
            parameters=[LaunchConfiguration("config"), {
                "use_sim_time": ParameterValue(LaunchConfiguration("use_sim_time"), value_type=bool),
                "enable_output": ParameterValue(LaunchConfiguration("enable_output"), value_type=bool),
                "output_topic": LaunchConfiguration("output_topic"),
                "scan_topic": LaunchConfiguration("scan_topic"),
                "base_frame": LaunchConfiguration("base_frame"),
                "guard_service": LaunchConfiguration("guard_service"),
            }],
        ),
    ])
