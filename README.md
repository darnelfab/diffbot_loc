# diffbot_loc

This package contains the updated launch files for visual odometry and visual inertial odometry. The lidar odometry launch file was refactored and now you can access the lidar odometry node, through which you can echo its topic which is **/lidar_odom**. Also the sensor fusion for visual and inertial odometry was corected so as not to overwrite for the original one using imu., its node will be **/visual_inertial_fuse**. Furthermore you can see **/lidar_inertial_fuse** being published , this is the fusion of lidar using icp method and imu.

## Errors to be rectified

```sh
[ WARN] (2020-11-03 04:33:38.887) RegistrationIcp.cpp:983::computeTransformationImpl() ICP PointToPlane ignored for 2d scans with PCL registration (some crash issues). Use libpointmatcher (Icp/PM) or disable Icp/PointToPlane to avoid this warning.
```
```sh
[ WARN] [1604363617.205343903, 254.720000000]: Failed to meet update rate! 
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

