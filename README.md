# Comparative analysis of different techniques of robot localisation

 This project when instantiated will launch different methods for robot localisation. From the rqt-graph below 3 main methods based on imu, visual odometry and lidar-slam will be used. The system was developed further by fusing the different methods of localisation.


To launch the demo use;

```sh
roslaunch diffbot diffbot_world.launch
```

Launching this will launch the various nodes for imu, visual odometry and icp.  

To generate maps use:

```sh
roslaunch diffbot diffbot_gmapping.launch
```

And then :

```sh
roslaunch diffbot diffbot_amcl.launch
```

To launch the amcl node.

## Rqt graph

![alt text](https://github.com/darnelfab/diffbot_loc/blob/v5-dev/pictures/rqt.png?raw=true)

## Rqt graph for amcl

![alt text](https://github.com/darnelfab/diffbot_loc/blob/v5-dev/pictures/rosgraph_amcl.png?raw=true)

## Rtabmap viewer

![alt text](https://github.com/darnelfab/diffbot_loc/blob/v5-dev/pictures/rtabmap-viewer.png?raw=true)



