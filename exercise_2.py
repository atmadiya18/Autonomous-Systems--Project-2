#!/usr/bin/env python3
import rospy
from gazebo_msgs.srv import SpawnModel, DeleteModel, SetModelState
from gazebo_msgs.msg import ModelState


def position_node():
    # Create a publisher object with Twist
    pub_model = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=1)
    # Declare the node, and register it with a unique name
    rospy.init_node('model_service_node', anonymous=True)
    # Define the execution rate object (10Hz)
    rate = rospy.Rate(10)

    '''
        This is the main node loop
    '''

    # Create message object with a specific type
    state_msg = ModelState()
    state_msg.model_name = 'turtlebot3_burger'
    rospy.wait_for_service('/gazebo/set_model_state')

    #Initial position of the robot (0,0)
    state_msg.pose.position.x = 0
    state_msg.pose.position.y = 0

    while state_msg.pose.position.x < 1:
        try:
            #Step size increment in initial position to move the robot till the desired position (1,0)
            state_msg.pose.position.x += 0.05
            set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
            resp = set_state(state_msg)
            #Printing position for debugging purposes
            print(str(state_msg.pose.position.x))

        except rospy.ServiceException:
            print("Service call failed: ")
        # Sleep the necessary amount of time to keep a 10Hz execution rate
        rate.sleep()

if __name__ == '__main__':
    try:
        #Create a position node that contains publisher information
        position_node()
    except rospy.ROSInterruptException:
        pass