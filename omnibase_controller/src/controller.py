#!/usr/bin/env python
import rospy
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
#callback called by sub_path
def callback_path(msg):
    global x_g
    global y_g
    global flag
    global l
    l=len(msg.poses)
    #defines goal coordinates
    x_g=msg.poses[flag].pose.position.x
    y_g=msg.poses[flag].pose.position.y
#callback called by sub_odom
def callback_odom(msg):
    global l
    global x_g
    global y_g
    global e_x_sum
    global e_x_prev
    global e_y_sum
    global e_y_prev
    global count1
    global count2
    global flag
    #creates twist message to control the omnibase
    twist=Twist()
    x=msg.pose.pose.position.x
    y=msg.pose.pose.position.y
    #PID controller for x coordinate
    if count1==0:
        e_x=x_g-x
        e_x_sum+=e_x
        dedt_x=e_x-e_x_prev
        u_x=0.50*e_x+0.0008*e_x_sum+0.17*dedt_x
        twist.linear.x=u_x
        pub.publish(twist)
        e_x_prev=e_x
        #code snippet to stop the movement in x direction when omnibase reaches the goal within some error
        if e_x<=0.01 and e_x>=-0.01:
            print(e_x)
            twist.linear.x=0
            pub.publish(twist)
            count1=1
    #PID controller for y coordinate
    if count2==0:   
        e_y=y_g-y
        e_y_sum+=e_y
        dedt_y=e_y-e_y_prev
        u_y=0.50*e_y+0.0008*e_y_sum+0.17*dedt_y
        twist.linear.y=u_y
        pub.publish(twist)
        e_y_prev=e_y 
        #code snippet to stop the movement in y direction when omnibase reaches the goal within some error
        if e_y<=0.01 and e_y>=-0.01:
            print(e_y)
            twist.linear.y=0
            pub.publish(twist)
            count2=1
    #code snippet to change goal coordinaes to next point on path after reaching one point
    if count1==1 and count2==1:
        if flag+1<l:
            count1=0
            count2=0
            flag+=1
            rospy.sleep(1)
global count1
count1=0
global count2
count2=0
global e_x_sum
e_x_sum=0
global e_x_prev
e_x_prev=0
global e_y_sum
e_y_sum=0
global e_y_prev
e_y_prev=0
global flag
flag=0
rospy.init_node('controller_omni')
rospy.sleep(1)
sub_path=rospy.Subscriber('path',Path,callback_path)
sub_odom=rospy.Subscriber('odom',Odometry,callback_odom)
pub=rospy.Publisher('cmd_vel',Twist,queue_size=2)
rospy.spin()
