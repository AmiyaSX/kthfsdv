#!/usr/bin/env python


import rospy
from std_msgs.msg import Int32, Float32

def callback(data):
    q = 0.15
    result = data.data / q
    rospy.loginfo('Result: %f', result)
    publisher.publish(result)

def nodeB():

    rospy.init_node('nodeB', anonymous=True)
    

    rospy.Subscriber('/sun', Int32, callback)
    global publisher
    publisher = rospy.Publisher('/kthfs/result', Float32, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try():
        nodeB()
    except rospy.ROSInterruptException:
        pass
