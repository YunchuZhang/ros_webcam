#!/usr/bin/env python
#!coding=utf-8
 
#right code !
#write by leo at 2018.04.26
#function: 
#display the frame from another node.
import base64
import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import zmq
b=[0,1,2]
aaa=np.array(b)
ctx = zmq.Context()
sckt = ctx.socket(zmq.PUB)
#sckt.connect("tcp://127.0.0.1:5511")
sckt.bind("tcp://*:5556")
def send_array(socket, A, flags=0, copy=True, track=False):
    """send a numpy array with metadata"""
    md = dict(
        dtype = str(A.dtype),
        shape = A.shape,
    )
    socket.send_json(md, flags|zmq.SNDMORE)
    return socket.send(A, flags, copy=copy, track=track)


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
        #cv2.imwrite("/home/yunchu/3.png",cv_img)
        #cv2.waitKey(3)
        #print(aaa)
        img_encode = cv2.imencode('.jpg',cv_img)[1]
        data_encode = np.array(img_encode)
        #print(data_encode[0][0])
        send_array(sckt,data_encode,copy=False)
        #str_encode = data_encode.tostring()
        #str_encode = base64.b64encode(str_encode)
        #sckt.send_string(str_encode)
    else:
        pass
 
def displayWebcam():


    rospy.init_node('webcam_display', anonymous=True)
 
    # make a video_object and init the video object
    global count,bridge

    count = 0
    bridge = CvBridge()
    rospy.Subscriber('usb_cam/image_raw', Image, callback)
    rospy.spin()
 
if __name__ == '__main__':
    displayWebcam()