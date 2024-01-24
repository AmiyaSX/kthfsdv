#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def nodeA():
    pub = rospy.Publisher('/sun', Int32, queue_size=10)
    rospy.init_node('nodeA', anonymous=True)
    rate = rospy.Rate(20) # 20hz
    n = 4
    k = 0
    while not rospy.is_shutdown():
        k = k + n
        rospy.loginfo("Publishing: %d", k)
        pub.publish(k)
        rate.sleep()

if __name__ == '__main__':
    try:
        nodeA()
    except rospy.ROSInterruptException:
        pass
