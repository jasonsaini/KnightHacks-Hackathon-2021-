from DadBot import * 
from SpeechHandler import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# Code generated from .ui file
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 800)
        MainWindow.setMaximumSize(QtCore.QSize(750, 1000))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pfpLabel = QtWidgets.QLabel(self.centralwidget)
        self.pfpLabel.setGeometry(QtCore.QRect(110, 10, 531, 441))
        self.pfpLabel.setText("")
        self.pfpLabel.setPixmap(QtGui.QPixmap("resources/dadFrames/Mr. Turner_2.png"))
        self.pfpLabel.setScaledContents(True)
        self.pfpLabel.setObjectName("pfpLabel")
        self.talkButton = QtWidgets.QPushButton(self.centralwidget)
        self.talkButton.setGeometry(QtCore.QRect(100, 460, 551, 31))
        self.talkButton.setObjectName("talkButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 510, 701, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(2, 2, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.jokeLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.jokeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.jokeLabel.setWordWrap(True)
        self.jokeLabel.setObjectName("jokeLabel")
        self.gridLayout_2.addWidget(self.jokeLabel, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(2, 2, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.bulbIconLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bulbIconLabel.sizePolicy().hasHeightForWidth())
        self.bulbIconLabel.setSizePolicy(sizePolicy)
        self.bulbIconLabel.setText("")
        self.bulbIconLabel.setPixmap(QtGui.QPixmap("resources/icons/lightbulb.png"))
        self.bulbIconLabel.setScaledContents(True)
        self.bulbIconLabel.setObjectName("bulbIconLabel")
        self.gridLayout_2.addWidget(self.bulbIconLabel, 0, 0, 1, 1)
        self.adviceLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.adviceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.adviceLabel.setObjectName("adviceLabel")
        self.gridLayout_2.addWidget(self.adviceLabel, 1, 0, 1, 1)
        self.weatherLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.weatherLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherLabel.setWordWrap(True)
        self.weatherLabel.setObjectName("weatherLabel")
        self.gridLayout_2.addWidget(self.weatherLabel, 1, 4, 1, 1)
        self.laughIconLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.laughIconLabel.sizePolicy().hasHeightForWidth())
        self.laughIconLabel.setSizePolicy(sizePolicy)
        self.laughIconLabel.setText("")
        self.laughIconLabel.setPixmap(QtGui.QPixmap("resources/icons/lol2.png"))
        self.laughIconLabel.setScaledContents(True)
        self.laughIconLabel.setObjectName("laughIconLabel")
        self.gridLayout_2.addWidget(self.laughIconLabel, 0, 2, 1, 1)
        self.weatherIconLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weatherIconLabel.sizePolicy().hasHeightForWidth())
        self.weatherIconLabel.setSizePolicy(sizePolicy)
        self.weatherIconLabel.setText("")
        self.weatherIconLabel.setPixmap(QtGui.QPixmap("resources/icons/weather.png"))
        self.weatherIconLabel.setScaledContents(True)
        self.weatherIconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherIconLabel.setObjectName("weatherIconLabel")
        self.gridLayout_2.addWidget(self.weatherIconLabel, 0, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        self.menuSelect = QtWidgets.QMenu(self.menubar)
        self.menuSelect.setMouseTracking(False)
        self.menuSelect.setObjectName("menuSelect")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChoose_Dad = QtWidgets.QAction(MainWindow)
        self.actionChoose_Dad.setObjectName("actionChoose_Dad")
        self.menuSelect.addAction(self.actionChoose_Dad)
        self.menubar.addAction(self.menuSelect.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.talkButton.setText(_translate("MainWindow", "Talk to DadBot!"))
        self.jokeLabel.setText(_translate("MainWindow", "Ask DadBot to tell you one of his famous dad jokes! (Or a programming joke)"))
        self.adviceLabel.setText(_translate("MainWindow", "Ask DadBot for life advice!"))
        self.weatherLabel.setText(_translate("MainWindow", "Ask DadBot to tell you the weather in any city!"))
        self.menuSelect.setTitle(_translate("MainWindow", "Select..."))
        self.actionChoose_Dad.setText(_translate("MainWindow", "Choose Dad..."))

def respondToUser():
    # convert user's speech to string
    userInput = SpeechHandler.listen()

    # init output string
    output = ""

    # Greet user
    if userInput.startswith('Hello') or userInput.startswith('hi') or userInput.startswith('hey'):
        output = ("Hello! Say help for a list of commands!")

    # tell user joke accordingly
    elif 'joke' in userInput:
        # if user specifies a geek joke, set output to geek joke
        if 'geeky' in userInput or 'coding' in userInput or 'programming' in userInput or 'computer' in userInput:
            output = DadBot.getGeekyJoke()
        # use a dad joke by default
        else:
            output = DadBot.getJoke()
    # Classic "Hi ___, I'm Dad!" joke
    elif userInput.startswith('I am'):
        output = DadBot.getHiJoke(userInput)

    # provide user w/ detailed weather description
    elif 'weather' in userInput:
        location = DadBot.parseLocation(userInput)
        output = DadBot.getWeather(location)

    # provide user with quote specifying its author
    elif("quote" or "advice" in userInput):
        output = DadBot.getQuote()

    # provide user with help message
    elif("help" in userInput):
        output = DadBot.getHelpMsg()

    # produce speech to text output!
    SpeechHandler.speak(output)
    return



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


