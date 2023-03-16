from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():
    return LaunchDescription(
        [
        IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(get_package_share_directory("leo_gazebo"), "launch", "spawn_robot.launch.py",
                                )
                ),
                launch_arguments={
                    "x_pose": "-45.0",
                    "y_pose": "0.0",
                    "z_pose": "5.01",
                    "roll_pose": "0",
                    "pitch_pose": "0",
                    "yaw_pose": "0",                                      
                }.items()
            ),
        ])
