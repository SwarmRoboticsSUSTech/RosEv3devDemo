import rospy
from std_msgs.msg import String
from ev3dev.ev3 import *
from time import sleep
mB = LargeMotor('outB')
mC = LargeMotor('outC')
us = UltrasonicSensor()
assert us.connected, "Connect a single US sensor to any sensor port"
ts = TouchSensor()
assert ts.connected, "Connect a touch sensor to any port"
us.mode='US-DIST-CM'

units = us.units

speed = 100

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    control_forward(data.data)
    
def main():
    pub = rospy.Publisher('ev3_008_chater', String, queue_size=1)

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('ev3_008', anonymous=True)

    rospy.Subscriber("chatter", String, callback, queue_size=1)
    respect()
    publisher(pub, node_name, speed)
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

if __name__ == '__main__':
    main()

