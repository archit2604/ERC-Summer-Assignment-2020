# ERC-Summer-Assignment-2020
I have attempted 2 question from the "4.3 Automation and Control" section of the assignment
##These are

##4.3.1.2
##Omnibase
Omnibase is an omni-wheel based ground robot platform for simulation
built by ERC members. Your task is to use it to make a simple waypoint
controller with PID to traverse a given path in Gazebo. Given a list of
points, make a ROS node which subscribes to /odom topic (for current
position) and publishes to /cmd_vel topic the required velocity to get to
the next point. The robot should stop at each point in the path before
continuing. It will receive the path by subscribing to /path topic with
/nav_msgs/Path​ message type. For the purpose of demonstration you can
set up a simple node for publishing /path.
Since the robot uses omni-wheels it can move in any direction without
needing to rotate. Your controller should use this fact to publish velocity in
x and y direction [Hint: you might need to implement PID separately for x
and y]. Submit your code and a rosbag recording of the functioning robot.

##4.3.4.1
##Computer Vision + ROS
Create a line following bot which follows a line using computer vision.
You may use the available turtlebot platform in ROS. The line following bot
must follow the line in the world file provided to you (in the repo
mentioned in section 1). You will have to use OpenCV to detect the line,
its centre and thereby alter the velocities of the bot to minimize the error
between the bot’s centre and the line’s centre. Submit your code and a
rosbag recording of the functioning robot.

##Please follow these instructions to reproduce the results:
##4.3.1.2
