#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from subprocess import call


class RobotManager:
    def __init__(self):
        # In ROS, nodes are uniquely named. If two nodes with the same
        # name are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('robot_manager')

        rospy.loginfo("Robot manager : started.")

        rospy.Subscriber("syscommand", String, self._cmd_callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

        rospy.loginfo("Robot manager : exiting.")

    def _cmd_callback(self, data):
        if data.data == "shutdown":
            rospy.loginfo(f"Robot manager: {data.data} received")
            call("sudo shutdown -h now", shell=True)
        elif data.data == "reboot":
            rospy.loginfo(f"Robot manager: {data.data} received")
            call("sudo reboot", shell=True)
        else:
            rospy.logerr(f"Robot manager: Received invalid value ({data.data})")


if __name__ == '__main__':
    RobotManager()
