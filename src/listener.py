#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from subprocess import call

def callback(data):
    if data.data == "shutdown":
        rospy.loginfo(f"Robot manager : {data.data} received")
        call("sudo shutdown -h now", shell=True)
    elif data.data == "reboot":
        rospy.loginfo(f"Robot manager : {data.data} received")
        call("sudo reboot", shell=True)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.loginfo("Robot manager : started.")

    rospy.Subscriber("syscommand", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    rospy.loginfo("Robot manager : exiting.")

if __name__ == '__main__':
    
    listener()

