#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition

def generate_launch_description():

    use_sim_time = LaunchConfiguration("use_sim_time", default="false")
    urdf_file_name = "prius.urdf"
    world_file_name = 'arams_city.world'


    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    os.environ["GAZEBO_MODEL_PATH"] = os.path.join(
        get_package_share_directory('car_demo'), "models")
    world = os.path.join(get_package_share_directory(
        "arams_city"), 'worlds', world_file_name)
    urdf = os.path.join(
        get_package_share_directory("prius_description"),
        "urdf", urdf_file_name
    )
    with open(urdf, "r") as infp:
        robot_desc = infp.read()

    rviz_path = os.path.join(
        get_package_share_directory("car_demo"),
        "rviz", "ros2.rviz"
    )
    print(f"{rviz_path=}")

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            namespace="prius",
            output="screen",
            parameters=[{"use_sim_time": use_sim_time, "robot_description": robot_desc}],
            arguments=[urdf]
        ),

        Node(
                name="joint_state_broadcaster_spawner",
                package="controller_manager",
                executable="spawner",
                arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
        ),


        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
            ),
            launch_arguments={'world': world, 'verbose': "false",
                              'extra_gazebo_args': 'verbose'}.items()
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
            ),
            launch_arguments={'verbose': "false"}.items()
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory("car_demo"), "launch", "spawn_prius.launch.py",
                             )
            ),
            launch_arguments={
                        "x_pose": "1",
                        "y_pose": "1",
                        "z_pose": "1",
                        "roll_pose": "0",
                        "pitch_posw": "0",
                        "yaw_pose": "0",                                      
            }.items()
        )
    ])
