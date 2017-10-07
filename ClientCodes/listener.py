#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ev3dev.ev3 import *
from time import sleep

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    control_forward(data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def control_forward(move_command):
    mB = LargeMotor('outB')
    mC = LargeMotor('outC')
    us = UltrasonicSensor()
    assert us.connected, "Connect a single US sensor to any sensor port"
    ts = TouchSensor()
    assert ts.connected, "Connect a touch sensor to any port"

    # Put the US sensor into distance mode.
    us.mode='US-DIST-CM'

    units = us.units
    # reports 'cm' even though the sensor measures 'mm'
    if move_command is 'w':
        mB.run_timed(time_sp=1000, speed_sp=100, stop_action="hold")
        # mB.run_forever(time_sp=1000, speed_sp=100)
        mC.run_timed(time_sp=1000, speed_sp=100, stop_action="hold")
        # mC.run_forever(time_sp=1000, speed_sp=100)
	while any(mB.state or mC.state):
	    sleep(0.1)
    elif move_command is 'a':
        mB.run_timed(position_sp=45, speed_sp=-100, stop_action="hold")
	while any(mB.state or mC.state):
            sleep(0.1)
    elif move_command is 's':
        mB.run_timed(time_sp=1000, speed_sp=-100, stop_action="hold")
        mC.run_timed(time_sp=1000, speed_sp=-100, stop_action="hold")
	while any(mB.state or mC.state):
            sleep(0.1)
    elif move_command is 'd':
        mC.run_timed(position_sp=45, speed_sp=-100, stop_action="hold")
	while any(mB.state or mC.state):
            sleep(0.1)
    Leds.set_color(Leds.LEFT, Leds.GREEN)  #set left led green before exiting

if __name__ == '__main__':
    listener()

