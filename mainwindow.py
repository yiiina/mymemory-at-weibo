# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\weibomaiwindow\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_userName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_userName.setGeometry(QtCore.QRect(360, 130, 171, 31))
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.lineEdit_userName.setText("****")#待删除
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(360, 180, 171, 31))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setText("****")#待删除

        self.label_userName = QtWidgets.QLabel(self.centralwidget)
        self.label_userName.setGeometry(QtCore.QRect(270, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        font.setUnderline(False)
        self.label_userName.setFont(font)
        self.label_userName.setObjectName("label_userName")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(290, 190, 71, 21))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 270, 101, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_warning = QtWidgets.QLabel(self.centralwidget)
        self.label_warning.setGeometry(QtCore.QRect(120, 450, 591, 16))
        self.label_warning.setObjectName("label_warning")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_userName.setText(_translate("MainWindow", "账户名"))
        self.label_password.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label_warning.setText(_translate("MainWindow", "为备份完整微博，新浪需要您登录才能访问微博信息，程序不会记录您的包括用户名和密码在内的任何账户信息"))

