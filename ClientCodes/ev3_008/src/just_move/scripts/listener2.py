#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    # control_forward(data.data)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
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

# def control_forward(move_command):
#     mB = LargeMotor('outB')
#     mC = LargeMotor('outC')
#     us = UltrasonicSensor()
#     assert us.connected, "Connect a single US sensor to any sensor port"
#     ts = TouchSensor()
#     assert ts.connected, "Connect a touch sensor to any port"

#     # Put the US sensor into distance mode.
#     us.mode='US-DIST-CM'

#     units = us.units
#     # reports 'cm' even though the sensor measures 'mm'
#     if move_command is 'w':
#         mB.run_timed(time_sp=3000, speed_sp=100)
#         mC.run_timed(time_sp=3000, speed_sp=100)
#     elif move_command is 's':
#         mB.run_timed(time_sp=3000, speed_sp=-500)
#     elif move_command is 'a':
#         mB.run_timed(time_sp=3000, speed_sp=-100)
#         mC.run_timed(time_sp=3000, speed_sp=-100)
#     elif move_command is 'd':
#         mC.run_timed(time_sp=3000, speed_sp=-500)
#     Leds.set_color(Leds.LEFT, Leds.GREEN)  #set left led green before exiting

if __name__ == '__main__':
    listener()
