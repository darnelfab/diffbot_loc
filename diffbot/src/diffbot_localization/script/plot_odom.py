#!/usr/bin/env python

import math
from math import sin, cos, pi
# importing the required module 
import matplotlib.pyplot as plt 

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

rospy.init_node('diffbot_odom')

odom_pub = rospy.Publisher("diffbot_odom", Odometry, queue_size=50)
odom_broadcaster = tf.TransformBroadcaster()

x = 0.0
y = 0.0
th = 0.0

vx = 0.1
vy = -0.1
vth = 0.1

current_time = rospy.Time.now()
last_time = rospy.Time.now()

r = rospy.Rate(1.0)
while not rospy.is_shutdown():
    current_time = rospy.Time.now()

    # compute odometry in a typical way given the velocities of the robot
    dt = (current_time - last_time).to_sec()
    delta_x = (vx * cos(th) - vy * sin(th)) * dt
    delta_y = (vx * sin(th) + vy * cos(th)) * dt
    delta_th = vth * dt

    x += delta_x
    y += delta_y
    th += delta_th

		# plotting the points  
    plt.plot(x, y) 
  
	# naming the x axis 
    plt.xlabel('x - axis') 
	# naming the y axis 
    plt.ylabel('y - axis') 
  
	# giving a title to my graph 
    plt.title('My first graph!') 
  
	# function to show the plot 

    # since all odometry is 6DOF we'll need a quaternion created from yaw
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)

    # first, we'll publish the transform over tf
    odom_broadcaster.sendTransform(
        (x, y, 0.),
        odom_quat,
        current_time,
        "chassis",
        "diffbot_odom"
    )
		
    
    # next, we'll publish the odometry message over ROS
    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "odom"

    # set the position
    odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

    # set the velocity
    odom.child_frame_id = "chassis"
    odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))

    # publish the message
    odom_pub.publish(odom)

    last_time = current_time
    r.sleep()

		# plotting the points  
    plt.plot(x, y) 
  
	# naming the x axis 
    plt.xlabel('x - axis') 
	# naming the y axis 
    plt.ylabel('y - axis') 
  
	# giving a title to my graph 
    plt.title('My first graph!') 
  
	# function to show the plot 
    plt.show() 
