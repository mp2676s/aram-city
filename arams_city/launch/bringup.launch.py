from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
import os

def generate_launch_description():

    arams_city_path = get_package_share_directory("arams_city")


    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([arams_city_path, "/launch/arams_city.launch.py",]),
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([arams_city_path, "/launch/spawn_leo.launch.py",]),
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([arams_city_path, "/launch/controller_spawner.launch.py",]),
            ),
        ]
    )