#!/usr/bin/env python
import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
rospy.init_node('path_planner_omni')
pub=rospy.Publisher('path',Path,queue_size=1)
rate=rospy.Rate(10)
#decrales a path object
path=Path()
path.header.frame_id="path"
#Takes the path as input from the user
while True:
    x=float(raw_input("Enter the x coordinate of the point:"))
    y=float(raw_input("Enter the y coordinate of the point:"))
    pose=PoseStamped()
    pose.pose.position.x=x
    pose.pose.position.y=y
    pose.pose.position.z=0
    path.poses.append(pose)
    chk=raw_input("Do you want to enter another point?(y/n):")
    if chk=="y" or chk=="Y":
        pass
    else:
        break
while not rospy.is_shutdown():
    pub.publish(path)
    rate.sleep()
