#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from cv_bridge import CvBridge
import cv2 


def showImage(img):
    cv2.imshow('image', img)
    cv2.waitKey(1)

def process_image(msg):
    try:
       bridge = CvBridge()
       orig = bridge.imgmsg_to_cv2(msg, "32FC1")
       drawImg = orig
    except Exception as err:
        print err

	#Load the dictionary that was used to generate the markers.

	dictionary = cv2.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)
	# Initialize the detector parameters using default values
	
	parameters =  cv2.aruco.DetectorParameters_create()
	# Detect the markers in the image

	markerCorners, markerIds, rejectedCandidates = cv.aruco.detectMarkers(frame, dictionary,parameters=parameters)
	
	pub.publish(markerIds)
	
	

    	showImage(drawImg)

def start_node():
    rospy.init_node('depth_camera_kinect')
    rospy.loginfo('detect_pub node started')
    rospy.Subscriber("/camera/image_raw", Image, process_image)
    pub = rospy.Publisher("/AR_Tag_ID_Topic", Int32, queue_size = 10)
    rospy.spin()


if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
