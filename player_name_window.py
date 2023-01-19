# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player_name_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(210, 151)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(70, 100, 75, 23))
        self.saveButton.setObjectName("saveButton")
        self.firstPlayerNameLine = QtWidgets.QLineEdit(Dialog)
        self.firstPlayerNameLine.setGeometry(QtCore.QRect(50, 29, 121, 21))
        self.firstPlayerNameLine.setObjectName("firstPlayerNameLine")
        self.secondPlayerNameLine = QtWidgets.QLineEdit(Dialog)
        self.secondPlayerNameLine.setGeometry(QtCore.QRect(50, 60, 121, 21))
        self.secondPlayerNameLine.setObjectName("secondPlayerNameLine")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.saveButton.setText(_translate("Dialog", "Сохранить"))
        self.firstPlayerNameLine.setPlaceholderText(_translate("Dialog", "Имя первого игрока"))
        self.secondPlayerNameLine.setPlaceholderText(_translate("Dialog", "Имя второго игрока"))
