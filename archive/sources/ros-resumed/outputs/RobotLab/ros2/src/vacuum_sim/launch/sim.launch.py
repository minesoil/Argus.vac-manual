from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    RegisterEventHandler,
    SetEnvironmentVariable,
    ExecuteProcess,
)
from launch.conditions import IfCondition
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    package = Path(get_package_share_directory("vacuum_sim"))
    description = ParameterValue(
        Command(
            [
                "xacro ",
                LaunchConfiguration("description_file"),
                " camera_width:=",
                LaunchConfiguration("camera_width"),
                " camera_height:=",
                LaunchConfiguration("camera_height"),
                " camera_rate:=",
                LaunchConfiguration("camera_rate"),
            ]
        ),
        value_type=str,
    )
    spawn = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-world",
            "vacuum_room",
            "-name",
            "vacuum",
            "-topic",
            "/robot_description",
            "-z",
            "0.015",
        ],
        output="screen",
    )
    controllers = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "diff_drive_controller",
            "--controller-manager-timeout",
            "120",
        ],
        output="screen",
    )
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "description_file",
                default_value=str(
                    package
                    / (
                        "urdf/designed.urdf"
                        if (package / "urdf/designed.urdf").exists()
                        else "urdf/vacuum.urdf.xacro"
                    )
                ),
            ),
            DeclareLaunchArgument("camera_width", default_value="320"),
            DeclareLaunchArgument("camera_height", default_value="240"),
            DeclareLaunchArgument("camera_rate", default_value="60"),
            DeclareLaunchArgument("gui", default_value="true"),
            DeclareLaunchArgument("rviz", default_value="true"),
            DeclareLaunchArgument(
                "rviz_config", default_value=str(package / "config/view.rviz")
            ),
            SetEnvironmentVariable("ROS_AUTOMATIC_DISCOVERY_RANGE", "LOCALHOST"),
            SetEnvironmentVariable("ROS_DOMAIN_ID", "42"),
            SetEnvironmentVariable("GZ_PARTITION", "vacuum_sim_42"),
            SetEnvironmentVariable("GZ_IP", "127.0.0.1"),
            # Direct argv keeps Gazebo under launch's signal handling; a shell wrapper
            # previously exited first and left its Gazebo child running.
            ExecuteProcess(
                cmd=[
                    "gz",
                    "sim",
                    "-r",
                    "-s",
                    "-v",
                    "2",
                    str(package / "worlds/room.sdf"),
                ],
                output="screen",
            ),
            ExecuteProcess(
                cmd=["gz", "sim", "-g", "-v", "2"],
                output="screen",
                condition=IfCondition(LaunchConfiguration("gui")),
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                parameters=[{"robot_description": description, "use_sim_time": True}],
                output="screen",
            ),
            Node(
                package="ros_gz_bridge",
                executable="parameter_bridge",
                parameters=[
                    {
                        "config_file": str(package / "config/bridge.yaml"),
                        "use_sim_time": True,
                    }
                ],
                output="screen",
            ),
            RegisterEventHandler(
                OnProcessExit(target_action=spawn, on_exit=[controllers])
            ),
            spawn,
            Node(
                package="vacuum_sim",
                executable="twist_adapter.py",
                parameters=[{"use_sim_time": True}],
                output="screen",
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                arguments=["-d", LaunchConfiguration("rviz_config")],
                parameters=[{"use_sim_time": True}],
                condition=IfCondition(LaunchConfiguration("rviz")),
                output="screen",
            ),
        ]
    )
