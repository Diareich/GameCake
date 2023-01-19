# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 479)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setObjectName("helpButton")
        self.verticalLayout.addWidget(self.helpButton)
        self.versionLabel = QtWidgets.QLabel(self.centralwidget)
        self.versionLabel.setObjectName("versionLabel")
        self.verticalLayout.addWidget(self.versionLabel)
        self.helloLabel = QtWidgets.QLabel(self.centralwidget)
        self.helloLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.helloLabel.setAutoFillBackground(False)
        self.helloLabel.setObjectName("helloLabel")
        self.verticalLayout.addWidget(self.helloLabel)
        self.twoPlayersModeButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoPlayersModeButton.setObjectName("twoPlayersModeButton")
        self.verticalLayout.addWidget(self.twoPlayersModeButton)
        self.onePlayerModeButton = QtWidgets.QPushButton(self.centralwidget)
        self.onePlayerModeButton.setObjectName("onePlayerModeButton")
        self.verticalLayout.addWidget(self.onePlayerModeButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.helpButton.setText(_translate("MainWindow", "Помощь"))
        self.versionLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">version</p></body></html>"))
        self.helloLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Добро пожаловать!</p><p align=\"center\">Выберите режим игры чтобы начать</p><p align=\"center\"><br/></p></body></html>"))
        self.twoPlayersModeButton.setText(_translate("MainWindow", "Два игрока"))
        self.onePlayerModeButton.setText(_translate("MainWindow", "Против компьютера"))
