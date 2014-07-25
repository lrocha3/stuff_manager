# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_main.ui'
#
# Created: Fri Jul 25 21:08:18 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_update = QtGui.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(250, 380, 85, 26))
        self.btn_update.setObjectName(_fromUtf8("btn_update"))
        self.line_teste = QtGui.QLineEdit(self.centralwidget)
        self.line_teste.setGeometry(QtCore.QRect(370, 130, 113, 21))
        self.line_teste.setObjectName(_fromUtf8("line_teste"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuDataBase = QtGui.QMenu(self.menubar)
        self.menuDataBase.setObjectName(_fromUtf8("menuDataBase"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_DataBase = QtGui.QAction(MainWindow)
        self.actionCreate_DataBase.setObjectName(_fromUtf8("actionCreate_DataBase"))
        self.menuDataBase.addAction(self.actionCreate_DataBase)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDataBase.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_update.setText(_translate("MainWindow", "Update", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuDataBase.setTitle(_translate("MainWindow", "DataBase", None))
        self.actionCreate_DataBase.setText(_translate("MainWindow", "Create DataBase", None))

