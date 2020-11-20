#!/usr/bin/env python

"""

Script to move Turtlesim in a circle

"""

import rospy
import time
import board
from adafruit_motorkit import MotorKit
from geometry_msgs.msg import Twist

kit = MotorKit(i2c=board.I2C())

def move_circle():



    # Create a publisher which can "talk" to Turtlesim and tell it to move

    pub = rospy.Publisher('/cmd', Twist, queue_size=1)


    # Create a Twist message and add linear x and angular z values

    move_cmd = Twist()

    kit.motor1.throttle = 0 #Steering Control

    kit.motor2.throttle = 0 #Speed control

    move_cmd.linear.x = kit.motor1.throttle

    move_cmd.angular.z = kit.motor3.throttle



    # Save current time and set publish rate at 10 Hz

    now = rospy.Time.now()

    rate = rospy.Rate(10)



    # For the next 6 seconds publish cmd_vel move commands to Turtlesim

    while rospy.Time.now() < now + rospy.Duration.from_sec(6):

        pub.publish(move_cmd)

        rate.sleep()



if __name__ == '__main__':

    try:
	move_circle()

    except rospy.ROSInterruptException:

       pass
