SWD Robot Manager
===

This package contains a set of helper nodes for the SWD Starter Kit.

The package contains this nodes:
- `robot_manager`: A node which manages the robot, currently it can be use to send commands such as *shutdown* or *restart*.
- `path_publisher`: A node which publishes a `nav_msgs::Path` message from a stream of `geometry_msgs::PoseStamped` messages.
- `pose_from_tf`: A node which publishes a `PoseStamped` message from a TF tree lookup, useful to recover information about the robot's pose in a multi-frame setup.


ez-Wheel® 2021

