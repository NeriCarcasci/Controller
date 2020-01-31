import zmq
import sys


class Client():
    
        def __init__(self):
            self.port = "5556"
            self.mode = "single"
            self.Servers = {
                "Server1":"ONE",
                "port1":"5556",

                "Server2":"TWO",
                "port2":"5555",
                }

            #Connecting to servers
            context = zmq.Context()
            print ("Connecting to server...")
            self.socket = context.socket(zmq.REQ)
            self.socket.connect ("tcp://localhost:%s" % self.Servers.get("port1"))
            if self.mode == "multi":
                self.socket.connect ("tcp://localhost:%s" % self.Servers.get("port2"))

        def Con_try(self):
                #  Do 10 requests, waiting each time for a response
            for request in range (1,10):
                print ("Sending request ", request,"...")
                self.socket.send_string("Hello")
                #  Get the reply.
                message = self.socket.recv()
                print ("Received reply ", request, "[", message, "]")

        def Msg_snd_rcv(self, message):
            message = message.encode('utf-8')
            print("Sending request %s …" % self.Servers.get("Server1"))
            self.socket.send(message)
            answer = self.socket.recv()
            print("Received reply %s [ %s ]" % (self.Servers.get("Server1"), answer))
            return answer



#    if len(sys.argv) > 1:
#       port =  sys.argv[1]
#        int(port)

#    if len(sys.argv) > 2:
#        port1 =  sys.argv[2]
#        int(port1)
#                               len(sys.argv) > 2: