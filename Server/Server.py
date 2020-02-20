
import zmq
import time
import sys
from datetime import datetime

class Server():
    protocol_key = "-"   
    now = datetime.now()


    def __init__(self):
        port = "5556"
        if len(sys.argv) > 1:
            port =  sys.argv[1]
            int(port)
        context = zmq.Context()
        self.socket = context.socket(zmq.REP)
        self.socket.bind("tcp://*:%s" % port)

    def listen(self):
            message = self.socket.recv()
            print("Received request: ", message)
            current_time = self.now.strftime("%H:%M")
            return message

    def protocol_implementer(self, msg, type, status):
        message = type + self.protocol_key + msg + self.protocol_key + str(status)
        self.answer(message)
            
    def answer(self, answer):
       try:
            self.socket.send_string(answer)
       except:
            return "Error has accurred"
       

