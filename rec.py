import cv2
import zmq
import json
sub_port = 5511
context = zmq.Context()
#connect to socket we subscrib
socket_sub = context.socket(zmq.SUB)
socket_sub.connect("tcp://127.0.0.1:%d" %sub_port)
socket_sub.setsockopt(zmq.SUBSCRIBE, b"")

def recv_array(socket, flags=0, copy=True, track=False):
    """recv a numpy array"""
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)
    buf = buffer(msg)
    A = numpy.frombuffer(buf, dtype=md['dtype'])
    return A.reshape(md['shape'])
while True:
    print('sd')
    contents  =  recv_array(socket_sub)
    print('sdsds')
    nparr = np.asarray(bytearray(contents), dtype="uint8")
    img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow('URL2Image',img_decode)
    cv2.waitKey(0)


