import cv2
import zmq
import json
import numpy as np
sub_port = 5556
context = zmq.Context()
#connect to socket we subscrib
socket_sub = context.socket(zmq.SUB)
socket_sub.connect("tcp://localhost:5556")
#socket_sub.setsockopt(zmq.SUBSCRIBE, b"")
socket_sub.setsockopt(zmq.SUBSCRIBE,b'')
def recv_array(socket, flags=0, copy=True, track=False):
    """recv a numpy array"""
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)
    buf = buffer(msg)
    A = np.frombuffer(buf, dtype=md['dtype'])
    return A.reshape(md['shape'])
while True:
    print('asds')
    contents  =  recv_array(socket_sub,copy=False)
    print(contents)
    #nparr = np.asarray(bytearray(contents), dtype="uint8")

    img_decode = cv2.imdecode(contents, cv2.IMREAD_COLOR)
    cv2.imshow('URL2Image',img_decode)
    cv2.imwrite("/home/yunchu/5.png",img_decode)
    cv2.waitKey(3)


