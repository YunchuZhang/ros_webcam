import cv2
import zmq

sub_port = 5511
context = zmq.Context()
#connect to socket we subscrib
socket_sub = context.socket(zmq.SUB)
socket_sub.connect("tcp://192.168.3.71:%d" %sub_port)
socket_sub.setsockopt(zmq.SUBSCRIBE, b"")


while True:
	print('sd')
	contents  =  socket_sub.recv_string()
	print('sdsds')
	nparr = np.asarray(bytearray(contents), dtype="uint8")
	img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	cv2.imshow('URL2Image',img_decode)
	cv2.waitKey(0)