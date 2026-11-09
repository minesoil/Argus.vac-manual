"""Hardware bringup stays disarmed. Lidar driver is an optional external package."""

from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package = Path(get_package_share_directory("vacuum_hardware"))
    config = LaunchConfiguration("config")
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "config", default_value=str(package / "config/hardware.yaml")
            ),
            DeclareLaunchArgument("lidar", default_value="true"),
            DeclareLaunchArgument("lidar_port", default_value="/dev/robot_lidar"),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                parameters=[
                    {
                        "robot_description": (package / "urdf/robot.urdf").read_text(),
                        "use_sim_time": False,
                    }
                ],
            ),
            Node(
                package="vacuum_hardware",
                executable="motor_bridge",
                parameters=[config],
            ),
            Node(
                package="sllidar_ros2",
                executable="sllidar_node",
                name="sllidar_node",
                condition=IfCondition(LaunchConfiguration("lidar")),
                parameters=[
                    {
                        "channel_type": "serial",
                        "serial_port": LaunchConfiguration("lidar_port"),
                        "serial_baudrate": 460800,
                        "frame_id": "lidar_link",
                        "inverted": False,
                        "angle_compensate": True,
                        "scan_mode": "Standard",
                    }
                ],
            ),
            Node(
                package="nav2_collision_monitor",
                executable="collision_monitor",
                name="collision_monitor",
                parameters=[config],
            ),
            Node(
                package="nav2_lifecycle_manager",
                executable="lifecycle_manager",
                name="hardware_lifecycle_manager",
                parameters=[
                    {
                        "autostart": True,
                        "node_names": ["collision_monitor"],
                        "use_sim_time": False,
                    }
                ],
            ),
        ]
    )
