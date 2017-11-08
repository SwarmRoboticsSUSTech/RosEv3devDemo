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

ir_select_list = [1, 2, 3, 4]
node_name = 'ev3_008'
pub = rospy.Publisher(node_name + '_chatter', String, queue_size=1)
speed = 200

'''
Kinds of messages:
 - number: 1,2,3,4
 - str: stop for wait
'''

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    if int(data.data) in [1, 2, 3, 4]:
        ir_select_list.remove(int(data.data))
    print('My ir_select_list is: ' + ir_select_list)
    # publisher(pub, 'ev3_00#', speed)
    
def main():
    # pub = rospy.Publisher('ev3_009_chatter', String, queue_size=1)

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node(node_name, anonymous=True)

    rospy.Subscriber("chatter", String, callback, queue_size=1)   # laptop node
    rospy.Subscriber("ev3_001_chatter", String, callback, queue_size=1) # other robot node
    rospy.Subscriber("ev3_002_chatter", String, callback, queue_size=1) # other robot node
    rospy.Subscriber("ev3_009_chatter", String, callback, queue_size=1) # other robot node
    seeker(node_name)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


def publisher(pub, node_name, speed):
    '''
    publish its status informations, speed
    '''
    status_str = 'speed: ' + str(speed)
    rospy.loginfo(status_str)
    pub.publish(node_name + "'status: " + status_str)

def publisher_ir_info(pub, node_name, ir_id):
    '''
    publish its found ir id
    '''
    rospy.loginfo('I have find: ' + str(ir_id))
    pub.publish(str(ir_id))

def seeker(node_name):
    '''
    node_name: node name of itself
    '''
    flag = None
    
    while not ts.value():
        if flag is None:
            # Lock only once
            degree_ir_channel1 = ir.value(0)
            degree_ir_channel2 = ir.value(2)
            degree_ir_channel3 = ir.value(4)
            degree_ir_channel4 = ir.value(6)
            if degree_ir_channel1 != 0 and (1 in ir_select_list):
                flag = 1
                publisher_ir_info(pub, node_name + '_chatter', flag)
            elif degree_ir_channel2 != 0 and (2 in ir_select_list):
                flag = 2
                publisher_ir_info(pub, node_name + '_chatter', flag)
            elif degree_ir_channel3 != 0 and (3 in ir_select_list):
                flag = 3
                publisher_ir_info(pub, node_name + '_chatter', flag)
            elif degree_ir_channel4 != 0 and (4 in ir_select_list):
                flag = 4
                publisher_ir_info(pub, node_name + '_chatter', flag)


        if flag == 1:
            degree_ir = ir.value(0)
            distance_ir = ir.value(1)
        elif flag == 2:
            degree_ir = ir.value(2)
            distance_ir = ir.value(3)
        elif flag == 3:
            degree_ir = ir.value(4)
            distance_ir = ir.value(5)
        elif flag == 4:
            degree_ir = ir.value(6)
            distance_ir = ir.value(7)
        else:
            # No found
            degree_ir = 999
            distance_ir = 999
        
        distance = us.value()/10
        print('degree:' + str(degree_ir))
        print('distcane_ir:' + str(distance_ir))
        print('distance:' + str(distance))

        if distance <= 20:
            if degree_ir == 999 and distance_ir == 999:
                # No found
                mB.run_to_rel_pos(position_sp=15, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-15, speed_sp=100)
                
            elif degree_ir < 0:
                # Found
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
            elif degree_ir > 0:
                # Found
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
        elif distance > 20:
            if degree_ir == 999 and distance_ir == 999:
                # NO found
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
                # Found
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
            elif degree_ir > 0:
                # Found
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
            # run_time_length = distance_ir / 100
            mB.run_forever(speed_sp=100)
            mC.run_forever(speed_sp=100)
    mB.stop()
    mC.stop()

def random_walk():
    '''
    random walk
    TODO: random stop to wait
    '''
    mB.run_to_rel_pos(position_sp=15, speed_sp=100)
    mC.run_to_rel_pos(position_sp=-15, speed_sp=100)

if __name__ == '__main__':
    main()
