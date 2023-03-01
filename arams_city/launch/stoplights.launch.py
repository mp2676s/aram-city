from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    gazebo_ros_share= get_package_share_directory("gazebo_ros")
    pkg_share = get_package_share_directory("arams_city")

    return LaunchDescription(
            [
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        [
                            gazebo_ros_share,
                            "/launch/gazebo.launch.py",
                        ]
                    ),
                    launch_arguments={
                        "world" : os.path.join(pkg_share, "worlds", "stoplights.world"),
                        "pause" : "False",
                        "gui" : "True",
                        "gdb" : "False",
                        "verbose" : "True",
                    }.items(),
                ),
            ])

