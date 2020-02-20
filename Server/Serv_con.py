import Server
import time
import configparser

class controller():
    #This will be running directly on the reaspberry PI
    Server_class = Server.Server()

    def action1(self):
        print("Message for Action1 received!!")

    def decryptor(self, msg):
        decoded = msg.decode("utf-8", "ignore")
        list = msg.split(self.Server_class.protocol_key)
        if len(list) == 3:
            self.type = list[0]
            self.message = list[1]
            self.status = list[2]

    def __init__(self):
        while True:
            message = self.Server_class.listen()
            if len(message) > 0:
                self.decryptor(message)
                print(self.message)
                asw = "neet"
                self.Server_class.protocol_implementer(asw, "res", "read")
                
            time.sleep(1)

Ser_Controller = controller()
Ser_Controller()

