# ERC-Summer-Assignment-2020
I have attempted 2 question from the "4.3 Automation and Control" section of the assignment.These are:

## 4.3.1.2- Omnibase
Omnibase is an omni-wheel based ground robot platform for simulation
built by ERC members. Your task is to use it to make a simple waypoint
controller with PID to traverse a given path in Gazebo. Given a list of
points, make a ROS node which subscribes to /odom topic (for current
position) and publishes to /cmd_vel topic the required velocity to get to
the next point. The robot should stop at each point in the path before
continuing. It will receive the path by subscribing to /path topic with
/nav_msgs/Path message type. For the purpose of demonstration you can
set up a simple node for publishing /path.
Since the robot uses omni-wheels it can move in any direction without
needing to rotate. Your controller should use this fact to publish velocity in
x and y direction [Hint: you might need to implement PID separately for x
and y]. Submit your code and a rosbag recording of the functioning robot.

## 4.3.4.1- Computer Vision + ROS
Create a line following bot which follows a line using computer vision.
You may use the available turtlebot platform in ROS. The line following bot
must follow the line in the world file provided to you (in the repo
mentioned in section 1). You will have to use OpenCV to detect the line,
its centre and thereby alter the velocities of the bot to minimize the error
between the bot’s centre and the line’s centre. Submit your code and a
rosbag recording of the functioning robot.

## Please follow these instructions to reproduce the results:
### 4.3.1.2
To clone and run omnibase follow [Omnibase Github repository](https://github.com/ERC-BPGC/omnibase).

Clone ERC-Summer-Assignment-2020:
*Download the repository as a ZIP file
*Unpack it
*Copy all the contents and paste them in your /catkin_ws/src
*Now run:
```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```
Start omnibase in gazebo:
```bash
cd ~/catkin_ws
source devel/setup.bash
rosrun omnibase_gazebo omnibase.launch
```
Run the path planning node:
```bash
cd ~/catkin_ws
source devel/setup.bash
rosrun omnibase_controller path_planner.py
#Enter the path before proceeding further
```
Run the path planner:
```bash
cd ~/catkin_ws
source devel/setup.bash
rosrun omnibase_controller controller.py
```
Use Ctrl+C to stop the nodes.

### 4.3.4.1
Clone ERC-Summer-Assignment-2020:
```bash
cd ~/catkin_ws/src
git clone https://github.com/archit2604/ERC-Summer-Assignment-2020.git
```
Start the simulation:
```bash
cd ~/catkin_ws
source devel/setup.bash
roslaunch follower tb3_lfm1.launch
```
Use Ctrl+C to stop the nodes.

## Rosbag Recordings
Rosbag recordings for both the question is inside the folder rosbag.
