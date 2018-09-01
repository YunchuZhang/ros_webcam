#!/usr/bin/env python
#!coding=utf-8
 
#right code !
#write by leo at 2018.04.26
#function: 
#display the frame from another node.
 
import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
 
def callback(data):
    # define picture to_down' coefficient of ratio
    scaling_factor = 0.5
    global count,bridge
    count = count + 1
    if count == 10:
        count = 0
        cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
	print('get')
        #cv2.imshow("frame" , cv_img)
        cv2.imwrite("/home/yunchu/3.png",cv_img)
        #cv2.waitKey(3)
    else:
        pass
 
def displayWebcam():
    rospy.init_node('webcam_display', anonymous=True)
 
    # make a video_object and init the video object
    global count,bridge

    count = 0
    bridge = CvBridge()
    rospy.Subscriber('camera/rgb/image_raw', Image, callback)
    rospy.spin()
 
if __name__ == '__main__':
    displayWebcam()
