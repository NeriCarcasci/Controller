
import zmq
import time
import sys

class Server():

    def __init__(self):
        # Provide port as command line argument to run server at two different ports.
        port = "5556"
        if len(sys.argv) > 1:
            port =  sys.argv[1]
            int(port)
        #Server is created with a socket type “zmq.REP” and is bound to well known port.
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:%s" % port)
        #It will block on recv() to get a request before it can send a reply.
        while True:
            #  Wait for next request from client
            message = socket.recv()
            print("Received request: ", message)
            time.sleep(1)  
            socket.send_string("World from %s" % port)

server = Server()
server()