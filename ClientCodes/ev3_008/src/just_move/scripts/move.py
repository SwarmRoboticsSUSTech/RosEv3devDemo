from ev3dev.ev3 import *
from time import sleep
import sys
import datetime
print(datetime.datetime.now())
mB = LargeMotor('outB')
mC = LargeMotor('outC')
print(datetime.datetime.now())

if sys.argv[1] is 'w':
    
    mB.run_forever(speed_sp=100)
    mC.run_forever(speed_sp=100)
    print(datetime.datetime.now())
elif sys.argv[1] is 's':
    mB.run_forever(speed_sp=-100)
    mC.run_forever(speed_sp=-100)
elif sys.argv[1] is 'a':
    mB.run_timed(position_sp=45, speed_sp=-100, stop_action="hold")
    while any(mB.state or mC.state):
        sleep(0.1)
elif sys.argv[1] is 'd':    
    mC.run_timed(position_sp=45, speed_sp=-100, stop_action="hold")
    while any(mB.state or mC.state):
        sleep(0.1)
elif sys.argv[1] is 'x':
    mB.stop()
    mC.stop()

