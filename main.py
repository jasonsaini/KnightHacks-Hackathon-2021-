from DadBot import * 
from SpeechHandler import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from playsound import playsound
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #set window title
        MainWindow.setWindowTitle("DadBot 2.0")

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFixedSize(QtCore.QSize(800, 1000))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pfpLabel = QtWidgets.QLabel(self.centralwidget)
        self.pfpLabel.setGeometry(QtCore.QRect(140, 10, 531, 441))
        self.pfpLabel.setText("")
        self.pfpLabel.setPixmap(QtGui.QPixmap("resources/dadFrames/Mr. Turner_2.png"))
        self.pfpLabel.setScaledContents(True)
        self.pfpLabel.setObjectName("pfpLabel")
        self.talkButton = QtWidgets.QPushButton(self.centralwidget)
        self.talkButton.setGeometry(QtCore.QRect(180, 450, 442, 88))
        self.talkButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/talkButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.talkButton.setIcon(icon)
        self.talkButton.setIconSize(QtCore.QSize(442, 88))
        self.talkButton.setObjectName("talkButton")
                
        # linked event handler function to talk button
        self.talkButton.clicked.connect(self.onTalkButtonClicked)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 580, 801, 401))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("resources/icons/lol2Final.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("resources/icons/lightbulbFinal.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/icons/weatherFinal.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSelect = QtWidgets.QMenu(self.menubar)
        self.menuSelect.setMouseTracking(True)
        self.menuSelect.setObjectName("menuSelect")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMr_Turner = QtWidgets.QAction(MainWindow)
        self.actionMr_Turner.setObjectName("actionMr_Turner")
        
        self.actionMr_Turner_Bonus = QtWidgets.QAction(MainWindow)
        self.actionMr_Turner_Bonus.setObjectName("actionMr_Turner_Bonus")
        
        self.actionMr_Neutron = QtWidgets.QAction(MainWindow)
        self.actionMr_Neutron.setObjectName("actionMr_Neutron")
        
        self.actionMr_Incredible = QtWidgets.QAction(MainWindow)
        self.actionMr_Incredible.setObjectName("actionMr_Incredible")
        
        self.actionHomer_Simpson = QtWidgets.QAction(MainWindow)
        self.actionHomer_Simpson.setObjectName("actionHomer_Simpson")
        
        self.actionHomer_Simpson_Bonus = QtWidgets.QAction(MainWindow)
        self.actionHomer_Simpson_Bonus.setObjectName("actionHomer_Simpson_Bonus")
        
        self.actionKratos = QtWidgets.QAction(MainWindow)
        self.actionKratos.setObjectName("actionKratos")
        
        self.actionBob_Belcher = QtWidgets.QAction(MainWindow)
        self.actionBob_Belcher.setObjectName("actionBob_Belcher")
        
        self.actionDarth_Vader = QtWidgets.QAction(MainWindow)
        self.actionDarth_Vader.setObjectName("actionDarth_Vader")
        
        self.menuSelect.addAction(self.actionMr_Turner)
        
        self.menuSelect.addAction(self.actionMr_Turner_Bonus)
        
        self.menuSelect.addAction(self.actionMr_Neutron)
        
        self.menuSelect.addAction(self.actionMr_Incredible)
        
        self.menuSelect.addAction(self.actionHomer_Simpson)
        
        self.menuSelect.addAction(self.actionHomer_Simpson_Bonus)
        
        self.menuSelect.addAction(self.actionKratos)
        
        self.menuSelect.addAction(self.actionBob_Belcher)
        
        self.menuSelect.addAction(self.actionDarth_Vader)
        
        self.menubar.addAction(self.menuSelect.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Link event handlers to buttons
        self.actionMr_Turner.triggered.connect(self.Mr_Turner_selected)
        self.actionMr_Turner_Bonus.triggered.connect(self.Mr_Turner_Bonus_selected)
        self.actionMr_Neutron.triggered.connect(self.Mr_Neutron_selected)
        self.actionMr_Incredible.triggered.connect(self.Mr_Incredible_selected)
        self.actionHomer_Simpson.triggered.connect(self.Homer_selected)
        self.actionHomer_Simpson_Bonus.triggered.connect(self.Homer_Bonus_selected)
        self.actionKratos.triggered.connect(self.Kratos_selected)
        self.actionBob_Belcher.triggered.connect(self.Bob_Belcher_selected)
        self.actionDarth_Vader.triggered.connect(self.Darth_Vader_selected)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dadbot 2.0"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources\icons\lol2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.menuSelect.setTitle(_translate("MainWindow", "Choose Dad..."))
        self.actionMr_Turner.setText(_translate("MainWindow", "Mr. Turner"))
        self.actionMr_Turner_Bonus.setText(_translate("MainWindow", "Mr. Turner (Bonus!)"))
        self.actionMr_Neutron.setText(_translate("MainWindow", "Mr. Neutron"))
        self.actionMr_Incredible.setText(_translate("MainWindow", "Mr. Incredible"))
        self.actionHomer_Simpson.setText(_translate("MainWindow", "Homer Simpson"))
        self.actionHomer_Simpson_Bonus.setText(_translate("MainWindow", "Homer Simpson (Bonus!)"))
        self.actionKratos.setText(_translate("MainWindow", "Kratos"))
        self.actionBob_Belcher.setText(_translate("MainWindow", "Bob Belcher"))
        self.actionDarth_Vader.setText(_translate("MainWindow", "Darth Vader"))


    def onTalkButtonClicked(self):
        #play startup sound for user to start speaking
        playsound('resources/audio/startup.wav')

        # call respond to user function
        respondToUser()
        return
    
    def Mr_Turner_selected(self):
         self.pfpLabel.setPixmap(QtGui.QPixmap("resources/dadFrames/Mr. Turner_2.png"))
         return
    
    def Mr_Turner_Bonus_selected(self):
         self.pfpLabel.setPixmap(QtGui.QPixmap("resources/dadFrames/Mr. Turner_1.png"))
         return
    def Mr_Neutron_selected(self):
         self.pfpLabel.setPixmap(QtGui.QPixmap("resources/dadFrames/Hugh_Neutron1.png"))
         return
        
    def Mr_Incredible_selected(self):
         self.pfpLabel.setPixmap(QtGui.QPixmap("resources/dadFrames/Mr. Incredible.png"))
         return
    
    def Homer_selected(self):
         self.pfpLabel.setPixmap(QtGui.QPixmap("resources/dadFrames/Homer_1.png"))
         return

    def Homer_Bonus_selected(self):
         self.pfpLabel.setPixmap(QtGui.QPixmap("resources/dadFrames/Homer_2.png"))
         return
    
    def Kratos_selected(self):
         self.pfpLabel.setPixmap(QtGui.QPixmap("resources/dadFrames/Kratos.png"))
         return
    
    def Bob_Belcher_selected(self):
         self.pfpLabel.setPixmap(QtGui.QPixmap("resources/dadFrames/Bob_Belcher.png"))
         return
    
    def Darth_Vader_selected(self):
         self.pfpLabel.setPixmap(QtGui.QPixmap("resources/dadFrames/Vader.png"))
         return

def respondToUser():
    # convert user's speech to string
    userInput = SpeechHandler.listen()

    # init output string
    output = ""

    # Greet user
    if not userInput:
        output = "Sorry, I didn't understand that."
        
    elif userInput.startswith('Hello') or userInput.startswith('hi') or userInput.startswith('hey'):
        output = ("Hello say help for a list of commands!")

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
    elif("quote" in userInput or "advice" in userInput):
        output = DadBot.getQuote()

    # provide user with help message
    elif("help" in userInput):
        output = DadBot.getHelpMsg()

    else:
        output = "Sorry, I didn't understand that."

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
