import zmq
import numpy as np

def send_array(socket, A, flags=0, copy=True, track=False):
    """send a numpy array with metadata"""
    md = dict(
        dtype = str(A.dtype),
        shape = A.shape,
    )
    socket.send_json(md, flags|zmq.SNDMORE)
    return socket.send(A, flags, copy=copy, track=track)


context = zmq.Context()
#  Socket to talk to server
print('Connecting to hello world serve')
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")
b=[0,1,2]
aaa=np.array(b)
#  Do 10 requests, waiting each time for a response
while True:
    print('Sending request ')
    send_array(socket,aaa,copy= False)

    