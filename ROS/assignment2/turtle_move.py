#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
import m


def move_t(distance, angle):
    info_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    msg_value = Twist()

    msg_value.linear.z = 0
    msg_value.angular.z = 0
    
    temp_distance_x = 0
    temp_distance_y = 0
    vx = float(distance*math.cos(angle))
    vy = float(distance*math.sin(angle))

    msg_value.linear.x = vx
    msg_value.linear.y = vy

    msg_value.angular.x = 0
    msg_value.angular.y = 0

    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec()
        while temp_distance_y < vy**2:
            info_publisher.publish(msg_value)
            t1 = rospy.Time.now().to_sec()
            temp_distance_x = ((t1 - t0)*vx)**2
            temp_distance_y = ((t1 - t0)*vy)**2
        break




def draw():
    m.draw_m()
if __name__ =='__main__':
    rospy.init_node('my_initials')
    try:
        draw()
    except rospy.ROSInterruptException: pass