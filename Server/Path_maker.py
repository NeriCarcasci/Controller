
import settings
import motor
import time

class path_maker():

    motorFL = None
    motorFR = None
    motorBL = None
    motorBR = None

    def __init__(self):
        self.motorFL = motor.Motor(settings.Motor4B, settings.Motor4A, settings.Motor4Enable)
        self.motorFR = motor.Motor(settings.Motor3B, settings.Motor3A, settings.Motor3Enable)
        self.motorBL = motor.Motor(settings.Motor1B, settings.Motor1A, settings.Motor1Enable)
        self.motorBR = motor.Motor(settings.Motor2B, settings.Motor2A, settings.Motor2Enable)

    def __del__(self):
        del self.motorFL
        del self.motorFR
        del self.motorBL
        del self.motorBR

    def forward(self, sec):
        try:
            t_end = time.time() + int(sec)
        except:
            print("Time input error for forward")
        while time.time() < t_end:
            self.motorFL.moveForward()
            self.motorFR.moveForward()
            self.motorBL.moveForward()
            self.motorBR.moveForward()

    def backward(self, sec):
        try:
            t_end = time.time() + int(sec)
        except:
            print("Time input error for backward")
        while time.time() < t_end:
            self.motorFL.moveBackward()
            self.motorFR.moveBackward()
            self.motorBL.moveBackward()
            self.motorBR.moveBackward()

    def left(self, sec):
        try:
            t_end = time.time() + int(sec)
        except:
            print("Time input error for left")
        while time.time() < t_end:
            self.motorFL.moveBackward()
            self.motorFR.moveForward()
            self.motorBL.moveBackward()
            self.motorBR.moveForward()

    def right(self, sec):
        try:
            t_end = time.time() + int(sec)
        except:
            print("Time input error for right")
        while time.time() < t_end:
            self.motorFL.moveForward()
            self.motorFR.moveBackward()
            self.motorBL.moveForward()
            self.motorBR.moveBackward()

    def stop(self):
        self.motorFL.stop()
        self.motorFR.stop()
        self.motorBL.stop()
        self.motorBR.stop()

