## Install Ubuntu 22.04
https://releases.ubuntu.com/jammy/
## Install ROS2 Humble
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
Follow all installations steps including ros dev tools

### Install the following packages
```
sudo apt install ros-humble-gazebo-ros ros-humble-xacro ros-humble-controller-manager ros-humble-gazebo-ros-pkgs ros-humble-joint-state-publisher ros-humble-gazebo-ros2-control ros-humble-diff-drive-controller ros-humble-joint-state-broadcaster ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-rqt-robot-steering
```

### Create a ROS2 workspace
```
mkdir -p ~/ros2_ws/src
```

### Get all necessary packages
```
cd ~/ros2_ws/src
git clone https://git.fh-aachen.de/mascor-public/arams-city
git clone https://git.fh-aachen.de/mascor-public/leo_simulator
git clone https://git.fh-aachen.de/mascor-public/robotik2/projekt_wise22_23/leo_common
```

### Build your workspace
```
cd ~/ros2_ws
colcon build
# Ignore warnings

```

### Source the workspace packages
```
source ~/ros2_ws/install/local_setup.bash
```

### Launch the simulation
```
ros2 launch arams_city arams_city.launch.py
# wait until the commandline shows "[INFO] [traffic_light_controller]: All traffig lights are now available!"

ros2 launch arams_city spawn_leo.launch.py
# wait until the  commandline shows "[INFO] [spawn_entity.py]: process has finished cleanly"

ros2 launch arams_city controller_spawner.launch.py
# wait until the commandline did finish all commands
# simulation is running now! have fun!
```
