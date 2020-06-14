#!/usr/bin/env python
import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
#Defines PI
PI = 3.1415926535897
count=0
class Follower:
    #Constructor for the class
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('camera/rgb/image_raw',Image, self.image_callback)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel',Twist, queue_size=1)
        self.twist = Twist()
        self.e_prev=0
        self.e_sum=0
        self.e=0
    #function to process image and control the turtlebot accordingly
    def image_callback(self, msg):
        #image conversion from ROS to OpenCV format
        image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
        #image conversion from RGB to HSv format
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        #describes the range of yellow color in HSV format
        lower_yellow = numpy.array([ 10, 10, 10])
        upper_yellow = numpy.array([255, 255, 250])
        #masks image to detect yellow color
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        h, w, d = image.shape
        search_top = 3*h/4-10
        search_bot = 3*h/4+10
        #makes all pixels except the required region to 0
        #required region is the are just in front of the tb3
        mask[0:search_top, 0:w] = 0
        mask[search_bot:h, 0:w] = 0
        if mask.any():
            #Defines the centre of the required region
            M = cv2.moments(mask)
            if M['m00'] > 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                #Implementing a PID controller
                self.e = cx - w/2
                self.e_sum+=self.e
                dedt=self.e-self.e_prev
                self.twist.linear.x = 0.2
                self.twist.angular.z =-float(0.01*self.e+0.000005*self.e_sum+0.005*dedt)/15
                self.cmd_vel_pub.publish(self.twist)
        else:
            self.twist.linear.x = 0
            self.twist.angular.z = 0
            self.cmd_vel_pub.publish(self.twist)
        cv2.imshow("window", image)
        cv2.waitKey(3)
rospy.init_node('follower')
#Makes a object named follower of the class Follower
follower = Follower()
rospy.spin()
