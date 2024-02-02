#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

#introducing global variable dist with the initial value of 0

dist = 0


def scan_callback(data):
    global dist
    # data will contain the message information of type LaserScan, we can access and print that data as follows.
    dist = data.ranges[0]
    rospy.loginfo('Received ctr:{}'.format(data.ranges[0]))

def controller_node():
    global dist
    # Create a publisher object with Twist
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    # Declare the node, and register it with a unique name
    rospy.init_node('my_control_node', anonymous=True)
    # Define the execution rate object (10Hz)
    rate = rospy.Rate(10)

    '''According to the question, we are supposed to make the bot approach the wall and then stop, but according to
    the formula of linear motion, the bot is just going from coordinate (0,0) to (1,0). 
     
    When we are not calling the global variable inside the function, the bot is moving all the way towards the wall
    and taking an arbitrary trajectory and swirling back after getting reverse hit from the wall, or sometimes its 
    taking random direction and stopping near the wall but not as per our requirement.'''


    '''
        This is the main node loop
    '''
    while not rospy.is_shutdown():
        # Define a subscriber that will catch the messages published by scan
        # Observe how the subscription has to match use some of the parameters defined for the publisher.
        rospy.Subscriber("/scan", LaserScan, scan_callback)
        # Create message object with a specific type

        vel_msg = Twist()

        # Populate custom message object
        vel_msg.linear.x = 0.5 * (dist - 1)
        vel_msg.angular.z = 0
        # Log/trace information on console
        rospy.loginfo('[my_control_node] Running')
        # Publish the data
        pub.publish(vel_msg)
        # Sleep the necessary amount of time to keep a 10Hz execution rate
        rate.sleep()


if __name__ == '__main__':
    try:
        controller_node()
    except rospy.ROSInterruptException:
        pass