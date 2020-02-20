
from PyQt5 import QtWidgets, uic
import sys
import Controller

class Ui(QtWidgets.QMainWindow):
    Commands = {}
    num = 1
    controller_class = Controller.ControllerCl()

    def getAction(self, text):
        self.ChosenAction = text
    def getDistance(self):
        self.ChosenDistance = self.spinBoxDist.value()
    def getPower(self):
        self.ChosenPower = self.spinBoxPwr.value()

    def commandAppender(self):
        i = self.num

        if self.ChosenDistance <= 0 or self.ChosenPower <= 0 or self.ChosenAction == "Choose Action":
            print("invalid Input")
        else:
            self.Commands['Cmd_%s' % i] = [self.ChosenAction + "-" + str(self.ChosenDistance) + "-" + str(self.ChosenPower)]
            self.num += 1
        
        

    def initializer(self):
        self.controller_class.pathMaker(self.Commands)


    def dataClearer(self):
        i = 1
        self.ChosenAction = None
        self.ChosenDistance = 0
        self.ChosenPower = 0
        self.Commands = {}


    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('PathCreator.ui', self)
        self.dataClearer()

        self.comboBox = self.findChild(QtWidgets.QComboBox, 'Act_decider')
        self.comboBox.currentTextChanged.connect(self.getAction)

        self.spinBoxDist = self.findChild(QtWidgets.QSpinBox, 'Dist_decider')
        self.spinBoxDist.valueChanged.connect(self.getDistance)

        self.spinBoxPwr = self.findChild(QtWidgets.QSpinBox, 'Pwr_decider')
        self.spinBoxPwr.valueChanged.connect(self.getPower)

        self.button = self.findChild(QtWidgets.QPushButton, 'AddLine') # Find the button
        self.button.clicked.connect(self.commandAppender)

        self.button = self.findChild(QtWidgets.QPushButton, 'Run') # Find the button
        self.button.clicked.connect(self.initializer)

        self.show()

def startUi():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()

startUi()