from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
import os

def generate_launch_description():
    gazebo_ros_share= get_package_share_directory("gazebo_ros")
    pkg_share = get_package_share_directory("arams_city")

    #urdf_file_name = "prius.urdf"
    # use_sim_time = LaunchConfiguration("use_sim_time", default="false")

    # os.environ["GAZEBO_MODEL_PATH"] = os.path.join(
    #     get_package_share_directory('car_demo'), "models")

    # urdf = os.path.join(
    #     get_package_share_directory("prius_description"),
    #     "urdf", urdf_file_name
    # )
    # with open(urdf, "r") as infp:
    #     robot_desc = infp.read()

    rviz_path = os.path.join(
    get_package_share_directory("arams_city"),
    "rviz", "leo.rviz"
    )


    return LaunchDescription(
        [
                # DeclareLaunchArgument(
                # 'use_sim_time',
                # default_value='false',
                # description='Use simulation (Gazebo) clock if true'),

            # DeclareLaunchArgument(
            #     name="model",
            #     default_value=[urdf],
            #     description="Absolute path to robot urdf.xacro file",
            # ),
            # DeclareLaunchArgument(
            #     name="fixed",
            #     default_value="false",
            #     description='Set to "true" to spawn the robot fixed to the world',
            # ),
            DeclareLaunchArgument(
                'frame',
                default_value='base_link',
                description='The fixed frame to be used in RViz'
            ),

            # Node(
            #     name="robot_state_publisher",
            #     package="robot_state_publisher",
            #     executable="robot_state_publisher",
            #     parameters=[
            #         {
            #             "robot_description": Command(
            #                 [
            #                     "xacro ",
            #                     LaunchConfiguration("model"),
            #                     " fixed:=",
            #                     LaunchConfiguration("fixed"),
            #                 ]
            #             )
            #         }
            #     ],
            # ),

                
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [
                        gazebo_ros_share,
                        "/launch/gazebo.launch.py",
                    ]
                ),
                launch_arguments={
                    "world" : os.path.join(pkg_share, "worlds", "arams_city.world"),
                    "pause" : "False",
                    "gui" : "True",
                    "gdb" : "False",
                    "verbose" : "True",
                }.items(),
            ),


            Node(
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                arguments=[
                    "-d", rviz_path,
                    "--fixed-frame", LaunchConfiguration(variable_name="frame")
                ],
                output="screen",
            ),

            Node(
                package="rqt_robot_steering",
                executable="rqt_robot_steering",
                name="rqt_robot_steering",
                output="screen",
            ),

            Node(
                package="arams_city",
                executable="traffic_light_node.py",
                name="traffic_light_controller",
                output="screen",
            ),

            # IncludeLaunchDescription(
            #     PythonLaunchDescriptionSource(
            #         os.path.join(get_package_share_directory("car_demo"), "launch", "spawn_prius.launch.py",
            #                     )
            #     ),
            #     launch_arguments={
            #         "x_pose": "1",
            #         "y_pose": "1",
            #         "z_pose": "5.01",
            #         "roll_pose": "0",
            #         "pitch_pose": "0",
            #         "yaw_pose": "0",                                      
            #     }.items()
            # ),
        ])

