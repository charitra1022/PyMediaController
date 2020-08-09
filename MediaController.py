# Created and Completed on - 13-06-2020 in 5hrs

#       COPYRIGHT® 2020
#       ——————————————
#       PyMediaController
#       Made by "Charitra Agarwal"
#       "www.youtube.com/c/EverythingComputerized"
#       "www.linkedin.com/in/chiku1022/"




      ############               ###
     #############              #####
    ###                        ### ###
   ###                        ###   ###
  ###                        ###     ###
  ###                       ###       ###
  ###                      ###############
  ###                     #################
   ###                    ###           ###
    ###                   ###           ###
     #############        ###           ###
      ############        ###           ###



# Instructions:- 
# 1. Install libraries:- pyqt5, pyqt5-tools, pynput
# 2. Icons folder should be correctly placed



from PyQt5 import QtCore, QtGui, QtWidgets
from pynput.keyboard import Key, Controller, Listener,  GlobalHotKeys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(185, 126)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(2, 2, 181, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MuteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MuteButton.sizePolicy().hasHeightForWidth())
        self.MuteButton.setSizePolicy(sizePolicy)
        self.MuteButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 50px; \n"
"height: 50px;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.MuteButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/mute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MuteButton.setIcon(icon1)
        self.MuteButton.setIconSize(QtCore.QSize(30, 30))
        self.MuteButton.setObjectName("MuteButton")
        self.horizontalLayout.addWidget(self.MuteButton)
        self.VolumeDownButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolumeDownButton.sizePolicy().hasHeightForWidth())
        self.VolumeDownButton.setSizePolicy(sizePolicy)
        self.VolumeDownButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 50px; \n"
"height: 50px;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.VolumeDownButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/vol-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VolumeDownButton.setIcon(icon2)
        self.VolumeDownButton.setIconSize(QtCore.QSize(30, 30))
        self.VolumeDownButton.setObjectName("VolumeDownButton")
        self.horizontalLayout.addWidget(self.VolumeDownButton)
        self.VolumeUpButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolumeUpButton.sizePolicy().hasHeightForWidth())
        self.VolumeUpButton.setSizePolicy(sizePolicy)
        self.VolumeUpButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 50px; \n"
"height: 50px;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.VolumeUpButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/vol-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VolumeUpButton.setIcon(icon3)
        self.VolumeUpButton.setIconSize(QtCore.QSize(30, 30))
        self.VolumeUpButton.setObjectName("VolumeUpButton")
        self.horizontalLayout.addWidget(self.VolumeUpButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(2, 62, 181, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PlayPauseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayPauseButton.sizePolicy().hasHeightForWidth())
        self.PlayPauseButton.setSizePolicy(sizePolicy)
        self.PlayPauseButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 50px; \n"
"height: 50px;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.PlayPauseButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/play-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPauseButton.setIcon(icon4)
        self.PlayPauseButton.setIconSize(QtCore.QSize(40, 40))
        self.PlayPauseButton.setObjectName("PlayPauseButton")
        self.horizontalLayout_2.addWidget(self.PlayPauseButton)
        self.PrevButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PrevButton.sizePolicy().hasHeightForWidth())
        self.PrevButton.setSizePolicy(sizePolicy)
        self.PrevButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 50px; \n"
"height: 50px;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.PrevButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PrevButton.setIcon(icon5)
        self.PrevButton.setIconSize(QtCore.QSize(40, 40))
        self.PrevButton.setObjectName("PrevButton")
        self.horizontalLayout_2.addWidget(self.PrevButton)
        self.NextButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NextButton.sizePolicy().hasHeightForWidth())
        self.NextButton.setSizePolicy(sizePolicy)
        self.NextButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 50px; \n"
"height: 50px;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.NextButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextButton.setIcon(icon6)
        self.NextButton.setIconSize(QtCore.QSize(40, 40))
        self.NextButton.setObjectName("NextButton")
        self.horizontalLayout_2.addWidget(self.NextButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.VolumeUpButton.setAutoRepeat(True)
        self.VolumeUpButton.setAutoRepeatDelay(500)
        self.VolumeUpButton.clicked.connect(self.volUp_button)

        self.VolumeDownButton.setAutoRepeat(True)
        self.VolumeDownButton.setAutoRepeatDelay(500)
        self.VolumeDownButton.clicked.connect(self.volDown_button)


        self.MuteButton.clicked.connect(self.mute_button)
        self.PlayPauseButton.clicked.connect(self.play_button)
        self.PrevButton.clicked.connect(self.prev_button)
        self.NextButton.clicked.connect(self.next_button)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Media Controller"))
        self.MuteButton.setToolTip(_translate("MainWindow", "Volume Mute\n"
"\'Ctrl + Alt + F1\'"))
        self.MuteButton.setShortcut(_translate("MainWindow", "Ctrl+Alt+F1"))
        self.VolumeDownButton.setToolTip(_translate("MainWindow", "Volume Down\n"
"\'Ctrl + Alt + F2\'"))
        self.VolumeDownButton.setShortcut(_translate("MainWindow", "Ctrl+Alt+F2"))
        self.VolumeUpButton.setToolTip(_translate("MainWindow", "Volume Up\n"
"\'Ctrl + Alt + F3\'"))
        self.VolumeUpButton.setShortcut(_translate("MainWindow", "Ctrl+Alt+F3"))
        self.PlayPauseButton.setToolTip(_translate("MainWindow", "Play/Pause\n"
"\'Ctrl + Alt + F4\'"))
        self.PlayPauseButton.setShortcut(_translate("MainWindow", "Ctrl+Alt+F4"))
        self.PrevButton.setToolTip(_translate("MainWindow", "Previous Track\n"
"\'Ctrl + Alt + F5\'"))
        self.PrevButton.setShortcut(_translate("MainWindow", "Ctrl+Alt+F5"))
        self.NextButton.setToolTip(_translate("MainWindow", "Next Track\n"
"\'Ctrl + Alt + F6\'"))
        self.NextButton.setShortcut(_translate("MainWindow", "Ctrl+Alt+F6"))


    def mute_button(self):
        keyboard = Controller()
        keyboard.touch(Key.media_volume_mute, True)

    def volUp_button(self):
        keyboard = Controller()
        keyboard.touch(Key.media_volume_up, True)

    def volDown_button(self):
        keyboard = Controller()
        keyboard.touch(Key.media_volume_down, True)

    def prev_button(self):
        keyboard = Controller()
        keyboard.touch(Key.media_previous, True)

    def play_button(self):
        keyboard = Controller()
        keyboard.touch(Key.media_play_pause, True)

    def next_button(self):
        keyboard = Controller()
        keyboard.touch(Key.media_next, True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())