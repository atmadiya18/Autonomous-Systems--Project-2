#!/usr/bin/env python3
import rospy
import time
from aut_sys.msg import motors
from aut_sys.msg import distance

#store initial starting time
starttime = time.time()

def scan_callback(data):
    global dist_data
    #data will contain message info from distance
    print(data)              #display current distance seen

def uctronics():
    
    # Create a publisher object with motors 
    pub = rospy.Publisher('motors', motors, queue_size=10)
    # Declare the node and register it with a name
    rospy.init_node('uctronics', anonymous=True)
    # Execution Rate
    rate = rospy.Rate(10)
    # Define a publisher to catch distance messages
    rospy.Subscriber("distance", distance, scan_callback)


    '''
        Main Loop beginning
    '''

    while not rospy.is_shutdown():
        #create message object with motor type
        vel_msg = motors()

        #populate motor message object with correct speed
        #if less than 2 seconds have passed, write full speed, else 0.
        if (time.time() - starttime) < 2:
            vel_msg.leftSpeed = 1
            vel_msg.rightSpeed = 1
        else:         
            vel_msg.leftSpeed = 0
            vel_msg.rightSpeed = 0
        
        #log/trance information on console
        rospy.loginfo('[utronics_node] Running')


        #Publish the speed 
        #print(vel_msg)         #printing velocity for debugging purposes
        pub.publish(vel_msg)
        #sleep to maintain 10hz rate
        rate.sleep()


if __name__ == '__main__':
    try:
            uctronics()
    except rospy.ROSInterruptException:
        pass