'''
 - use ROS to communicate
 - preemptive
 - use EV3DEV api
 - Random Walk
'''

import rospy
from std_msgs.msg import String
from ev3dev.ev3 import *
import random
from time import sleep
#import threading

mB = LargeMotor('outB')
mC = LargeMotor('outC')
us = UltrasonicSensor()
assert us.connected, "Connect a single US sensor to any sensor port"
ts = TouchSensor()
assert ts.connected, "Connect a touch sensor to any port"
us.mode='US-DIST-CM'

ir = InfraredSensor()
assert ir.connected, "Connect a single infrared sensor to any sensor port"
ir.mode = 'IR-SEEK'

units = us.units
pub = rospy.Publisher('ev3_00#_chatter', String, queue_size=1)
speed = 200

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    publisher(pub, 'ev3_00#', speed)
    
def main():
    # pub = rospy.Publisher('ev3_009_chatter', String, queue_size=1)

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('ev3_00#', anonymous=True)

    rospy.Subscriber("chatter", String, callback, queue_size=1)
    rospy.Subscriber("ev3_008_chatter", String, callback, queue_size=1)
    seeker()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


def publisher(pub, node_name, speed):
    '''
    publish its status informations
    '''
    status_str = 'speed: ' + str(speed)
    rospy.loginfo(status_str)
    pub.publish(node_name + "'status: " + status_str)

'''
def control_forward(move_command):
    global speed
    # mB = LargeMotor('outB')
    # mC = LargeMotor('outC')
    # us = UltrasonicSensor()
    # assert us.connected, "Connect a single US sensor to any sensor port"
    # ts = TouchSensor()
    # assert ts.connected, "Connect a touch sensor to any port"

    # Put the US sensor into distance mode.
    # us.mode='US-DIST-CM'

    # units = us.units
    # reports 'cm' even though the sensor measures 'mm'
    if move_command is 'w':  
        mB.run_forever(speed_sp=speed)
        mC.run_forever(speed_sp=speed)
    elif move_command is 'a':
        mB.run_timed(position_sp=45, speed_sp=-100, stop_action="hold")
    elif move_command is 's':
        mB.run_forever(speed_sp=-speed)
        mC.run_forever(speed_sp=-speed)
    elif move_command is 'd':
        mC.run_timed(position_sp=45, speed_sp=-100, stop_action="hold")
    elif move_command is 'x':
        speed = 100
        mB.stop()
        mC.stop()
    elif move_command is 'r':
        speed += 50
        mB.run_forever(speed_sp=speed)
        mC.run_forever(speed_sp=speed)
    elif move_command is 'f':
        speed -= 50
        mB.run_forever(speed_sp=speed)
        mC.run_forever(speed_sp=speed)
    # Leds.set_color(Leds.LEFT, Leds.GREEN)  #set left led green before exiting
'''

def seeker():
    while not ts.value():
        degree_ir_channel1 = ir.value(0)
        degree_ir_channel2 = ir.value(2)
        degree_ir_channel3 = ir.value(4)
        degree_ir_channel4 = ir.value(6)
        
                        
        degree_ir = ir.value(6)
        distance_ir = ir.value(7)
        distance = us.value()/10
        print('degreeA:' + str(degree_ir))
        print('distcaneA:' + str(distance_ir))
        print('distance:' + str(distance))

        if distance <= 20:
            if degree_ir == 0 and (distance_ir == 100 or distance_ir == -128):
                
                mB.run_to_rel_pos(position_sp=15, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-15, speed_sp=100)
                
            elif degree_ir < 0:
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
            elif degree_ir > 0:
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
        elif distance > 20:
            if degree_ir == 0 and (distance_ir == 100 or distance_ir == -128):
                # direction = random.randint(0, 1)
                # if direction == 0:
                random_walk()
                # elif direction == 1:
                #     mB.run_to_rel_pos(position_sp=-15, speed_sp=100)
                #     mC.run_to_rel_pos(position_sp=15, speed_sp=100)
                # run_time_random = random.randint(0, 3)
                # mB.run_forever(speed_sp=100)
                # mC.run_forever(speed_sp=100)
                # sleep(run_time_random)
            elif degree_ir < 0:
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
            elif degree_ir > 0:
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
            # run_time_length = distance_ir / 100
            mB.run_forever(speed_sp=100)
            mC.run_forever(speed_sp=100)
    mB.stop()
    mC.stop()

def random_walk(): # TODO
    '''
    random walk
    '''
    mB.run_to_rel_pos(position_sp=15, speed_sp=100)
    mC.run_to_rel_pos(position_sp=-15, speed_sp=100)

if __name__ == '__main__':
    main()
