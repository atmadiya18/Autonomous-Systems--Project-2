 For the practical implementation you will have to create a node capable of moving the car and reading the
 ultrasonic sensor. To do this you will need to implement a ROS architecture as shown in the diagram below.
 You will find that the the image in the RPi already contains a workspace ( aut_sys_ws ) and a package with
 some of the drivers interact with the sensors and actuators of the car. The ROS architecture below contains
 the actual names of the topics and nodes that you will need for this section. The orange node is the one that
 you will have to create. In this same diagram, the orange node has to publish data to the /motors topic,
 and catch data from the /distance topic. This implementation will be the basis of future labs involving the
 car.
 1. Under the package aut_sys create a file called uctronics.py This file must contain a publisher
 and a subscriber similar to the ones created in Sec.I-A, but in this case, the message type, and the topic
 names are different. Remember that message types have to be imported from the package owning the
 message. In this case, the package has already been created ( aut_sys ), explore the files in the msg
 folder and identify the message types that have to be used.
 2. The /distance topic retrieves a distance measured from the ultrasonic sensor as a floating point
 value in meters, you will have to implement the logic to print this value and move the car in a straight line
 for 2 seconds.
 3. Once the logic is ready, you will need to execute the application to verify it is working. To do that, you
 need to include the newly created node into the existing run_car.launch file.
 4. Verify the correctness of your system architecture by using the visualization command rqt_graph .
