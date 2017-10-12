# python3
import rospy
from std_msgs.msg import String
import getch


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    while not rospy.is_shutdown():
        key = getch.getch()
        hello_str = key + str(rospy.get_time())
        rospy.loginfo(hello_str)
        pub.publish(key)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass