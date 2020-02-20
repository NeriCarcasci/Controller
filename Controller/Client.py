import zmq
import sys


class Client():
        protocol_key = "-"  

        def __init__(self):
            self.port = "5556"
            self.mode = "local"
            self.Servers = {
                "Server1":"ONE",
                "port1":"5556",

                "Server2":"TWO",
                "port2":"5556",
                }

            #Connecting to servers
            context = zmq.Context()
            print ("Connecting to server...")
            self.socket = context.socket(zmq.REQ)
            self.socket.connect ("tcp://192.168.30.201:%s" % self.Servers.get("port1"))
            if self.mode == "local":
                self.socket.connect ("tcp://localhost:%s" % self.Servers.get("port2"))

        def Con_try(self):
                #  Do 10 requests, waiting each time for a response
            for request in range (1,10):
                print ("Sending request ", request,"...")
                self.socket.send_string("Hello")
                #  Get the reply.
                message = self.socket.recv()
                print ("Received reply ", request, "[", message, "]")

        def protocol_implementer(self, msg, type, status):
            message = type + self.protocol_key + msg + self.protocol_key + str(status)
            #message = message.encode('utf-8')
            self.Msg_snd_rcv(message)

        def returner(self):
            return self.type, self.message, self.status

        def decryptor(self, msg):
            decoded_message = str(msg, 'utf-8')
            list = decoded_message.split(self.protocol_key)
            if len(list) == 3:
                self.type = list[0]
                self.message = list[1]
                self.status = list[2]

        def Msg_snd_rcv(self, message):
            print("Sending request %s …" % self.Servers.get("Server1"))
            self.socket.send_string(message)
            answer = self.socket.recv()
            self.decryptor(answer)
            print("type:" + self.type + "   message:" + self.message + "   status:" + self.status)



#    if len(sys.argv) > 1:
#       port =  sys.argv[1]
#        int(port)

#    if len(sys.argv) > 2:
#        port1 =  sys.argv[2]
#        int(port1)
#                               len(sys.argv) > 2: