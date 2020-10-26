#!/usr/bin/env python

import rosbag
from odom.msg import Pose, Color
bag = rosbag.Bag('../home/darnel/catkin_darnel_ws/odom.bag')
# Initialize some empty lists for storing the data
tt = []
x = []
y = []
th = []
v = []
# Note - there seems to be issues with the recorded log file, so
# the following will cause an error
#for topic,msg,t in bag.read_messages():
# Need to only read the pose messages, like this
for topic,msg,t in bag.read_messages(topics=['/diffbot/pose']):
    tt.append(t.to_sec())
    x.append(msg.x)
    y.append(msg.y)
    th.append(msg.theta)
    v.append(msg.linear_velocity)
bag.close()

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
