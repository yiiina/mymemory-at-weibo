# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton_saveSelf = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_saveSelf.setGeometry(QtCore.QRect(290, 200, 191, 16))
        self.radioButton_saveSelf.setChecked(True)#默认选择自己的微博账户
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.radioButton_saveSelf.setFont(font)
        self.radioButton_saveSelf.setObjectName("radioButton_saveSelf")
        self.radioButton_saveElse = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_saveElse.setGeometry(QtCore.QRect(290, 230, 171, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.radioButton_saveElse.setFont(font)
        self.radioButton_saveElse.setObjectName("radioButton_saveElse")
        self.lineEdit_urlElse = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_urlElse.setGeometry(QtCore.QRect(332, 290, 321, 20))
        self.lineEdit_urlElse.setObjectName("lineEdit_urlElse")
        self.label_hint = QtWidgets.QLabel(self.centralwidget)
        self.label_hint.setGeometry(QtCore.QRect(90, 140, 271, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.label_hint.setFont(font)
        self.label_hint.setObjectName("label_hint")
        self.label_inputUrlelse = QtWidgets.QLabel(self.centralwidget)
        self.label_inputUrlelse.setGeometry(QtCore.QRect(330, 270, 151, 16))
        self.label_inputUrlelse.setObjectName("label_inputUrlelse")
        self.pushButton_beginSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_beginSave.setGeometry(QtCore.QRect(220, 400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.pushButton_beginSave.setFont(font)
        self.pushButton_beginSave.setObjectName("pushButton_beginSave")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(420, 400, 81, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        #self.pushButton_beginSave.clicked.connect(MainWindow2.save_to_doc)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.radioButton_saveSelf.setText(_translate("MainWindow2", "备份自己的微博"))
        self.radioButton_saveElse.setText(_translate("MainWindow2", "备份他人的微博"))
        self.label_hint.setText(_translate("MainWindow2", "请选择您要保存的微博账户："))
        self.label_inputUrlelse.setText(_translate("MainWindow2", "请输入此人微博主页网址："))
        self.pushButton_beginSave.setText(_translate("MainWindow2", "开始保存"))
        self.pushButton_exit.setText(_translate("MainWindow2", "退出"))

