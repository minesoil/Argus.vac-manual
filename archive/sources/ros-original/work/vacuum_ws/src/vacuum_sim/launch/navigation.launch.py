"""Start navigation against the map published by the separate mapping launch."""
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    package = Path(get_package_share_directory('vacuum_sim'))
    config = package / 'config/nav2.yaml'
    if not config.exists():
        raise RuntimeError('Generate config with tools/prepare_nav2.py in Ubuntu and rebuild first.')
    nav2 = Path(get_package_share_directory('nav2_bringup'))
    return LaunchDescription([IncludeLaunchDescription(
        PythonLaunchDescriptionSource(str(nav2 / 'launch/navigation_launch.py')),
        launch_arguments={'use_sim_time': 'true', 'params_file': str(config),
                          'autostart': 'true', 'use_composition': 'False'}.items())])
