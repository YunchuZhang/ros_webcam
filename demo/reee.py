import time
import zmq
import numpy
import sys
def recv_array(socket, flags=0, copy=True, track=False):
    """recv a numpy array"""
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)
    buf = buffer(msg)
    A = numpy.frombuffer(buf, dtype=md['dtype'])
    return A.reshape(md['shape'])
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")

socket.setsockopt(zmq.SUBSCRIBE,b'')
while True:
    #  Wait for next request from client
    message = recv_array(socket,copy=False)
    print("Received request: %s" % message)

