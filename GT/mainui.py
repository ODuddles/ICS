# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = mplwidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 30, 541, 541))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 530, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(660, 170, 61, 26))
        self.spinBox_2.setMaximum(500)
        self.spinBox_2.setProperty("value", 100)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 150, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 200, 111, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 390, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(610, 280, 41, 26))
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(650, 280, 41, 26))
        self.spinBox_4.setProperty("value", 3)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(610, 310, 41, 26))
        self.spinBox_5.setProperty("value", 5)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_6.setGeometry(QtCore.QRect(650, 310, 41, 26))
        self.spinBox_6.setProperty("value", 0)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_7.setGeometry(QtCore.QRect(700, 310, 41, 26))
        self.spinBox_7.setProperty("value", 1)
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_8 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_8.setGeometry(QtCore.QRect(700, 280, 41, 26))
        self.spinBox_8.setProperty("value", 0)
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_9 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_9.setGeometry(QtCore.QRect(740, 280, 41, 26))
        self.spinBox_9.setProperty("value", 5)
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_10 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_10.setGeometry(QtCore.QRect(740, 310, 41, 26))
        self.spinBox_10.setProperty("value", 1)
        self.spinBox_10.setObjectName("spinBox_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 280, 51, 17))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 260, 51, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(710, 260, 51, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 310, 51, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(650, 50, 101, 20))
        self.label_7.setObjectName("label_7")
        self.spinBox_11 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_11.setGeometry(QtCore.QRect(660, 70, 61, 26))
        self.spinBox_11.setMaximum(500)
        self.spinBox_11.setProperty("value", 50)
        self.spinBox_11.setObjectName("spinBox_11")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 460, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.spinBox_12 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_12.setGeometry(QtCore.QRect(660, 120, 61, 26))
        self.spinBox_12.setMaximum(500)
        self.spinBox_12.setProperty("value", 50)
        self.spinBox_12.setObjectName("spinBox_12")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(630, 100, 121, 20))
        self.label_8.setObjectName("label_8")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(660, 220, 65, 26))
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(560, 400, 121, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(560, 430, 141, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulation"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "Poule size"))
        self.label_3.setText(_translate("MainWindow", "Mutatian factor"))
        self.pushButton_2.setText(_translate("MainWindow", "Save "))
        self.label.setText(_translate("MainWindow", " A coop"))
        self.label_4.setText(_translate("MainWindow", "B coop"))
        self.label_5.setText(_translate("MainWindow", "B def"))
        self.label_6.setText(_translate("MainWindow", " A def"))
        self.label_7.setText(_translate("MainWindow", "Generations"))
        self.pushButton_3.setText(_translate("MainWindow", "Reset "))
        self.label_8.setText(_translate("MainWindow", "Rounds per game"))
        self.checkBox.setText(_translate("MainWindow", "Character plot"))
        self.checkBox_2.setText(_translate("MainWindow", "Strategies result"))
from mplwidget import mplwidget
