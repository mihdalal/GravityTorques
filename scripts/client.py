#!/usr/bin/env python

import sys
import rospy
from gravity_torques.srv import *

def gravity_torques_client(name):
    rospy.wait_for_service('gravity_torques')
    try:
        gravity_torques = rospy.ServiceProxy('gravity_torques', GravityTorques)
        resp1 = gravity_torques(name)
        return resp1.torques
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    print(gravity_torques_client('right'))