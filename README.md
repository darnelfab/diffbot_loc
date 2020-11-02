# diffbot_loc

This package contains the updated launch files for visual odometry and visual inertial odometry. The lidar odometry launch file was created too, many configuration was made, however each one created the same error log:


```python

OdometryF2M.cpp:1325::computeTransform() Missing scan to initialize odometry.

```

For visual odometry use:
```sh
roslaunch diffbot visual_odometry.launch
```
The topic for visual odometry is /visual_odom


For visual inertial odometry(fusing visual odometry with imu):

```sh
roslaunch diffbot visual_inertial_odometry.launch
```
The topic for visual inertial odometry is /visual_inertial_odom
