#import rospy
#from std_msgs.msg import String
from ev3dev.ev3 import *
#from time import sleep
#import threading

mB = LargeMotor('outB')
mC = LargeMotor('outC')
us = UltrasonicSensor()
assert us.connected, "Connect a single US sensor to any sensor port"
ts = TouchSensor()
assert ts.connected, "Connect a touch sensor to any port"
us.mode='US-DIST-CM'

ir = InfraredSensor()
#assert ir.connected, "Connect a single infrared sensor to any sensor port"
ir.mode = 'IR-SEEK'

units = us.units
#pub = rospy.Publisher('ev3_009_chatter', String, queue_size=1)
speed = 200

def f():
    # do something here ...
    # call f() again in 1 seconds
    publisher(pub, 'ev3_009', speed)
    threading.Timer(1, f).start()

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    publisher(pub, 'ev3_009', speed)
    control_forward(data.data)
    
def main():
    # pub = rospy.Publisher('ev3_009_chatter', String, queue_size=1)

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('ev3_009', anonymous=True)

    rospy.Subscriber("chatter", String, callback, queue_size=1)
    rospy.Subscriber("ev3_008_chatter", String, callback, queue_size=1)
    respect()
    # publisher(pub, 'ev3_009', speed)
    #f()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def respect():
    while not ts.value():    # Stop program by pressing touch sensor button
        # US sensor will measure distance to the closest
        # object in front of it.
        
        distance = us.value()/10  # convert mm to cm
        if distance < 60 and distance > 30:  #This is an inconveniently large distance
            Leds.set_color(Leds.LEFT, Leds.RED)
        elif distance <= 15:
            mB.stop()
            mC.stop()
        else:
            Leds.set_color(Leds.LEFT, Leds.GREEN)

def publisher(pub, node_name, speed):
    '''
    publish its status informations
    '''
    status_str = 'speed: ' + str(speed)
    rospy.loginfo(status_str)
    pub.publish(node_name + "'status: " + status_str)


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


def seeker_temp():
    while not ts.value():
        degree_A = ir.value(2)
        degree_B = ir.value(4)
        distance_A = ir.value(3)
        distance_B = ir.value(5)
        print('degreeA:' + str(degree_A))
        print('degreeB:' + str(degree_B))
        print('distcaneA:' + str(distance_A))
        print('distcaneB:' + str(distance_B))
        if degree_A < 0 and degree_B < 0:
            mB.run_to_rel_pos(position_sp=(degree_A+degree_B)/2, speed_sp=100)
        elif degree_A > 0 and degree_B > 0:
            mC.run_to_rel_pos(position_sp=-(degree_A+degree_B)/2, speed_sp=100)
        elif distance_A > 35 and distance_B > 35:
            run_time_length = (distance_A + distance_B) / 200
            mB.run_timed(time_sp=1000 * run_time_length, speed_sp=100)
            mC.run_timed(time_sp=1000 * run_time_length, speed_sp=100)
            mB.wait_while('running')
            mC.wait_while('running')
        elif distance_A <= 35 or distance_B <= 35:
            mB.stop()
            mC.stop()

def seeker():
    while not ts.value():
        target = None
        degree_A = ir.value(2)
        distance = us.value()/10
        print('degreeA:' + str(degree_A))
        print('distance:' + str(distance))
        if distance < 20:
            print('test1')
            if degree_A < 0 and degree_B < 0:
                mB.run_to_rel_pos(position_sp=(degree_A+degree_B)/2, speed_sp=200)
                mB.wait_while('running')
            elif degree_A > 0 and degree_B > 0:
                mC.run_to_rel_pos(position_sp=-(degree_A+degree_B)/2, speed_sp=200)
                mC.wait_while('running')
            #mB.stop()
            #mC.stop()
        elif distance > 20:
            if degree_A < 0 and degree_B < 0:
                mB.run_to_rel_pos(position_sp=(degree_A+degree_B)/2, speed_sp=200)
                mB.wait_while('running')
            elif degree_A > 0 and degree_B > 0:
                mC.run_to_rel_pos(position_sp=-(degree_A+degree_B)/2, speed_sp=200)
                mC.wait_while('running')
            run_time_length = distance / 50
            mB.run_timed(time_sp=1000 * run_time_length, speed_sp=50)
            mC.run_timed(time_sp=1000 * run_time_length, speed_sp=50)
            mB.wait_while('running')
            mC.wait_while('running') 

def seeker_single():
    while not ts.value():
        degree_ir = ir.value(4)
        distance_ir = ir.value(5)
        distance = us.value()/10
        print('degreeA:' + str(degree_ir))
        print('distcaneA:' + str(distance_ir))
        print('distance:' + str(distance))
        if distance <= 20:
            if degree_ir == 0 and distance_ir == 100:
                mB.run_to_rel_pos(position_sp=15, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-15, speed_sp=100)
            elif degree_ir < 0:
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
            elif degree_ir > 0:
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
        elif distance > 20:
            if degree_ir == 0 and distance_ir == 100:
                mB.run_to_rel_pos(position_sp=15, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-15, speed_sp=100)
                print('???')
            elif degree_ir < 0:
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
            elif degree_ir > 0:
                mB.run_to_rel_pos(position_sp=degree_ir, speed_sp=100)
                mC.run_to_rel_pos(position_sp=-degree_ir, speed_sp=100)
            run_time_length = distance_ir / 100
            mB.run_forever(speed_sp=100)
            mC.run_forever(speed_sp=100)


if __name__ == '__main__':
    # main()
    seeker_single()
