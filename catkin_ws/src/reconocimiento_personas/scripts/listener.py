#!/usr/bin/env python
import rospy
from reconocimiento_personas.msg import coordenadas

def callback(data):
    rospy.loginfo("Tus coordenas son: y: %d, h: %d, x: %d, w: %d",data.y,data.h,data.x,data.w)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", coordenadas, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    y = data.y

if __name__ == '__main__':
    listener()
