import Client

class ControllerCl:
    def __init__(self):
        self.Client_class = Client.Client()

    def Option1(self):
        # this is option one
        print("option1")
        self.Client_class.Msg_snd_rcv("Hello, it is neri")

    def Option2(self):
        # this is option2
        print("option2")

    def Forward(self):
        # this is move forward
        print("forward")