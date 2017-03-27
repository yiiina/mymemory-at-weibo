#!/usr/bin/python3
#coding:utf-8

#from PyQt5.QtWidgets.__init__ import QMessageBox
import sys
from docx import Document
from login import *
from text_parser import *
from mainwindow import Ui_MainWindow
from mainwindow2 import Ui_MainWindow2
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)
global cookie
global password
global UserName




class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.another =MyApp2()
        self.pushButton.clicked.connect(self.get_login_cookie)

        self.pushButton.clicked.connect(self.another.show)

    def get_login_cookie(self):
        global cookie
        global password
        global UserName
        UserName=self.lineEdit_userName.text()
        password=self.lineEdit_password.text()

        cookie=cn_get_login_cookie(UserName,password)[0]
        islogin=cn_get_login_cookie(UserName,password)[1]
        if islogin==0:
            self.label_login_error = QtWidgets.QLabel(self.centralwidget)
            self.label_login_error.setGeometry(QtCore.QRect(310, 240, 191, 16))
            self.label_login_error.setObjectName("label_login_error")
            self.label_login_error.setText(QtCore.QCoreApplication.translate("MainWindow", "账户名或者密码错误，请重新输入"))
            self.label_login_error.show()
        if islogin==1:
            self.close()
            #self.anotherWindow()

class MyApp2(QtWidgets.QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super(MyApp2,self).__init__()
        Ui_MainWindow2.__init__(self)
        self.setupUi(self)
        #another = Ui_MainWindow2()
        #self.pushButton.clicked.connect(self.get_login_cookie)
        self.pushButton_beginSave.clicked.connect(self.save_to_doc)
        self.pushButton_exit.clicked.connect(self.close)
    def save_to_doc(self):

        user_id=0
        #print(cookie)
        if self.radioButton_saveSelf.isChecked():
            user_id=cn_get_SelfId(cookie)
            else_or_self='self'
        if self.radioButton_saveElse.isChecked():
            url=self.lineEdit_urlElse.text()
            user_id=com_get_ELseId(url,cookie)
            else_or_self='else'
        #print(user_id)
        pagenum=get_page(cookie,int(user_id))

        #pagenum=128
        a_while=pagenum
        #pagenum=12
        #print(os.listdir('/Users/Yina/Desktop/mymemory-at-weibo/weibo_to_doc'))
        document =Document()
        document.add_paragraph('测试ing')
        document.save('/Users/Yina/Desktop/mymemory-at-weibo/weibo_to_doc/demo.docx')
        i=1
        weibo_order=1

        while(a_while):
            fp = open('/Users/Yina/Desktop/mymemory-at-weibo/weibo_to_doc/weibo_to_doc/%d.txt'%i , 'r' , encoding = 'utf-8')
            hlxml=fp.read()
            fp.close()


            text,weibo_order=parse_text(hlxml,cookie,weibo_order,else_or_self)
            del text

            a_while=a_while-1
            #print(i,'页做完')
            i=i+1
            del fp, hlxml







app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
