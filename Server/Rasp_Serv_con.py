
import Server
import time
import configparser
from time import sleep
#from car import car


class controller():
    Server_class = Server.Server()
    #car = car()

    def action(self, msg):
        msg = msg.lower()
        if msg == "forward":
            print("forward")
            #self.car.forward()
        elif msg == "backward":
            #self.car.backward()
            print("Backward")
        elif msg == "left":
            #self.car.left()
            print("left")
        elif msg == "right":
            #self.car.right()
            print("right")
        elif msg == "stop":
            self.stop()
        else:
            self.e ="Error: Action not recognised"

    def path_handler(self):
        print("Entering Path enviroment")
        self.Server_class.protocol_implementer("start", "accapted", "ready")
        while message[1] != "stopSession":
            message = self.Server_class.listen()
            if len(message) > 0:
                message = message.split("-")
                msg = message[0].lower()
                dist = int(message[1])
                pwr = int(message[2])
                if msg == "forward":
                    #self.path.forward(dist, pwr)
                    print("forward for %s" % str(dis))
                elif msg == "backward":
                    #self.path.backward(dist, pwr)
                    print("backward for %s" % str(dis))
                elif msg == "left":
                    #self.path.left(dist, pwr)
                    print("left for %s" % str(dis))
                elif msg == "right":
                    #self.path.right(dist, pwr)
                    print("right for %s" % str(dis))
                elif msg == "stop":
                    #self.path.stop()
                    print("stopping")
                else:
                    self.e ="Error: Action not recognised"
                    self.Server_class.protocol_implementer("A001", "error", "waiting")
                self.Server_class.protocol_implementer("next", "accapted", "waiting")


    def request_handler(self, msg):
        if msg == "PathCreator":
            path_handler()
    
    def executer(self, type):
        if type == "act":
            self.action(self.message)
        if type == "inf":
            self.answer = "info"
        if type == "req":
            self.request_handler(self.message)



    def decryptor(self, msg):
        decoded = msg.decode("utf-8", "ignore")
        list = msg.split(self.Server_class.protocol_key)
        if len(list) == 3:
            self.type = list[0]
            self.message = list[1]
            self.status = list[2]

    def __init__(self):
        while True:
            self.e = ""
            message = self.Server_class.listen()
            if len(message) > 0:
                self.decryptor(message)
                print(self.message)
                self.executer(self.type)
                if self.e > 0:
                    self.answer = self.e
                self.Server_class.protocol_implementer("res", self.answer, "read")
            time.sleep(1)

Ser_Controller = controller()
Ser_Controller()

