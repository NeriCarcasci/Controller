import Client

class ControllerCl:
    def __init__(self):
        self.Client_class = Client.Client()

    def checkStatus(self, wantedStatus):
        print(self.Received_info)
        if self.Received_info[2] == wantedStatus:
            return "go"


    def pathMaker(self, cmd_dict):
        self.Client_class.protocol_implementer("PathCreator", "req", "sent")
        self.Received_info = self.Client_class.returner()
        if self.checkStatus("ready") == "go":
            for i in cmd_dict:
                self.Client_class.Msg_snd_rcv(cmd_dict[i])
                if not self.Received_info[1] == "next":
                    break
            self.Client_class.protocol_implementer("stop", "request", "finished")
        return


    def forward(self):
        self.Client_class.protocol_implementer("forward", "act", "request")

    def backward(self):
        self.Client_class.protocol_implementer("backward", "act", "request")

    def left(self):
        self.Client_class.protocol_implementer("Hello", "act", "request")

    def right(self):
        self.Client_class.protocol_implementer("Hello", "act", "request")

    def stop(self):
        self.Client_class.protocol_implementer("Hello", "act", "request")

