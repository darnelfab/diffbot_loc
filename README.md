# diffbot_loc
updated repositiory

to launch diffbot in gazebo world --> roslaunch diffbot diffbot_world.launch
to launch teleop twist --> roslaunch diffbot diffbot_control.launch
to see the topics being published: rostopic list 
to view odometry topic: rostopic echo /diffbot_odom
to view imu topic: rostopic echo /diffbot_imu
to view ground_truth topic: rostopic echo /ground_truth
to view ekf filtered odometry: rostopic echo /odometry/filtered
