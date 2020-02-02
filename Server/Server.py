
import zmq
import time
import sys
from datetime import datetime

class Server():
    protocol_key = "-"   
    now = datetime.now()


    def __init__(self):
        # Provide port as command line argument to run server at two different ports.
        port = "5556"
        if len(sys.argv) > 1:
            port =  sys.argv[1]
            int(port)
        #Server is created with a socket type “zmq.REP” and is bound to well known port.
        context = zmq.Context()
        self.socket = context.socket(zmq.REP)
        self.socket.bind("tcp://*:%s" % port)

    def listen(self):
        #It will block on recv() to get a request before it can send a reply.
        #while True:
            #  Wait for next request from client
            message = self.socket.recv()
            print("Received request: ", message)
            current_time = self.now.strftime("%H:%M")
            return message

    def protocol_implementer(self, msg, type, status):
        message = type + self.protocol_key + msg + self.protocol_key + str(status)
        #message = message.encode('utf-8')
        self.answer(message)
            
    def answer(self, answer):
       try:
            self.socket.send_string(answer)
       except:
            return "Error has accurred"
       

