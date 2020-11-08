# wallfollower

Problem Statement:
Build a left-wall following robot capable of completing the provided course in a Gazebo world and reading AR Tags. The challenge consists of the following four parts:

Development of URDF/XACRO model of the robot with appropriate sensors. This includes all the plugins and sensors required for the robot to be able to follow a wall.

Execution of left-wall following behaviour in the provided Gazebo world. This includes creating all the required nodes to be able to execute this behaviour.

Reading AR Tags placed on the wall, publishing their Tag ID on the topic /AR_Tag_ID_Topic and saving the Tag ID for each Tag in a .txt file.

