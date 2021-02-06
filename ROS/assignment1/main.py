#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import f as function

def sub():
    rospy.Subscriber('topic1', String, converter)
    rospy.spin()

def Publisher(converted_message):
    pub = rospy.Publisher('topic2', String, queue_size=10)
    msg_to_publish = String()
    msg_to_publish.data = converted_message
    pub.publish(msg_to_publish)


def converter(message):
    result = function.data_collector(message.data)
    Publisher(result)

if __name__ == "__main__":
    rospy.init_node("my_convertor")
    sub()
