# Comparative analysis of different techniques of robot localisation

 This project when instantiated will launch different methods for robot localisation. From the rqt-graph below 3 main methods based on imu, visual odometry and lidar-slam will be used. The system was developed further by fusing the different methods of localisation.



## Rqt graph

![alt text](https://github.com/darnelfab/diffbot_loc/blob/v5-dev/pictures/rqt.png?raw=true)

## Rqt graph for amcl

![alt text](https://github.com/darnelfab/diffbot_loc/blob/v5-dev/pictures/rosgraph_amcl.png?raw=true)

## Rtabmap viewer

![alt text](https://github.com/darnelfab/diffbot_loc/blob/v5-dev/pictures/rtabmap-viewer.png?raw=true)

## Work in progress

 Two new worlds were created, store.world and curvedMaze.world. However even though the worlds can be uploaded successfuly when using;

```sh
gazebo worldname.world

```

When loading using;

```sh
roslaunch diffbot diffbot_world.launch
```
the meshes does not instantiate and the robot fall into oblivion.

