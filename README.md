## Control Lego EV3 Robots with [ROS](http://wiki.ros.org/) and [EV3DEV](https://github.com/ev3dev)
## Ideas
 - random walk # TODO
 - Preemptive

## System requirements
 - Ubuntu14.04 LTS with ROS indigo installed(Run roscore on your laptop)
 - ev3dev with Ros_comm installed (Run ros nodes in Lego EV3 Robotics)

It may cost you much time to write ros_comm to ev3dev, you can contact me to get the *.img file.

## set environment variables in both your laptop and your lego robotics：
```
$ source /opt/ros/indigo/setup.bash
```

## connect your robotics to your machine who run roscore：
Run those command in the terminal of your lego ev3dev system:
```
# change address to your laptop ipv4 address
$ export ROS_MASTER_URI=http://192.168.1.101:11311
$ export ROS_IP=`hostname -I`
```

## run roscore on your laptop
```
$ roscore
```

## run robotics programs on lego robotics
```
$ python src/swarm_robotics/scripts/listener.py
```

## view the relationship map of ros nodes and the massages they talked on your machine who run roscore
```
$ rosrun rqt_graph rqt_graph
$ rqt_console
```

## Attention!：
Do not open your IR Beacon before your robotics bagin to run, prevent robotics send message too early that some robotics who start lately cannot receive messages others send before.  
You should compile your program before your first running.  
Your laptop and your robotics should connect to the same wireless network, if not they cannot find each other.

## Some Tips may help you:
<https://superpershing.github.io>

## Reference
 - <http://www.ev3dev.org/>
 - <http://wiki.ros.org>
 - <https://github.com/ev3dev/ev3dev-lang-python>
 - <https://github.com/moriarty/ros-ev3>
 - OPAL, SUSTech