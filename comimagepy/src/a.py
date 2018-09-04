#!/usr/bin/env python
#!coding=utf-8
 
#right code !
#write by leo at 2018.04.26
#function: 
#display the frame from another node.
 
import rospy
import numpy as np
from sensor_msgs.msg import Image,CompressedImage
from cv_bridge import CvBridge, CvBridgeError
import cv2
 
def callback(data):
    # define picture to_down' coefficient of ratio
    scaling_factor = 0.5
    global count,bridge
    count = count + 1
    if count == 1:
        count = 0
        np_arr = np.fromstring(data.data, np.uint8)
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
	print('get')
        cv2.imshow("frame" , image_np)
        cv2.imwrite("/home/yunchu/3.png",image_np)
        cv2.waitKey(5)
    else:
        pass
 
def displayWebcam():
    rospy.init_node('webcam_display', anonymous=True)
 
    # make a video_object and init the video object
    global count,bridge

    count = 0
    bridge = CvBridge()
    rospy.Subscriber('camera/rgb/image_raw/compressed', CompressedImage, callback)
    rospy.spin()
 
if __name__ == '__main__':
    displayWebcam()
