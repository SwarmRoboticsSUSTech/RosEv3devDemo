## Control Lego EV3 Robots with [ROS](http://wiki.ros.org/) and [EV3DEV](https://github.com/ev3dev)
## Ideas
 - random walk # TODO
 - Preemptive

## Tips:
<https://superpershing.github.io/2017/10/01/%E5%9C%A8EV3DEV%E4%B8%8A%E8%BF%90%E8%A1%8CROS%E8%8A%82%E7%82%B9%E7%A8%8B%E5%BA%8F/>

## 设置环境变量：
```
source /opt/ros/indigo/setup.bash
```

## 多机器人：
```
# change address to your laptop ipv4 address
export ROS_MASTER_URI=http://192.168.1.101:11311
export ROS_IP=`hostname -I`
```

## 观察状态
```
rosrun rqt_graph rqt_graph
rqt_console
```

## 注意：
等所有机器程序全部开始运行后，再放入场内，防止出现消息发送过早导致没有接收到的后果。
