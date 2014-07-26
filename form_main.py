# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_main.ui'
#
# Created: Sun Jul 27 00:25:23 2014
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
        self.pushButton_update = QtGui.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(610, 410, 85, 26))
        self.pushButton_update.setObjectName(_fromUtf8("pushButton_update"))
        self.line_teste = QtGui.QLineEdit(self.centralwidget)
        self.line_teste.setGeometry(QtCore.QRect(212, 370, 491, 21))
        self.line_teste.setObjectName(_fromUtf8("line_teste"))
        self.groupBox_insert = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_insert.setGeometry(QtCore.QRect(140, 40, 211, 191))
        self.groupBox_insert.setObjectName(_fromUtf8("groupBox_insert"))
        self.pushButton_new_insert = QtGui.QPushButton(self.groupBox_insert)
        self.pushButton_new_insert.setGeometry(QtCore.QRect(10, 130, 85, 26))
        self.pushButton_new_insert.setObjectName(_fromUtf8("pushButton_new_insert"))
        self.lineEdit_quantidade = QtGui.QLineEdit(self.groupBox_insert)
        self.lineEdit_quantidade.setGeometry(QtCore.QRect(90, 90, 113, 21))
        self.lineEdit_quantidade.setObjectName(_fromUtf8("lineEdit_quantidade"))
        self.lineEdit_componente = QtGui.QLineEdit(self.groupBox_insert)
        self.lineEdit_componente.setGeometry(QtCore.QRect(90, 60, 113, 21))
        self.lineEdit_componente.setObjectName(_fromUtf8("lineEdit_componente"))
        self.label_5 = QtGui.QLabel(self.groupBox_insert)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_3 = QtGui.QLabel(self.groupBox_insert)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 16, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_insert)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_id = QtGui.QLineEdit(self.groupBox_insert)
        self.lineEdit_id.setGeometry(QtCore.QRect(90, 30, 113, 21))
        self.lineEdit_id.setObjectName(_fromUtf8("lineEdit_id"))
        self.pushButton_new_cancel = QtGui.QPushButton(self.groupBox_insert)
        self.pushButton_new_cancel.setGeometry(QtCore.QRect(110, 130, 85, 26))
        self.pushButton_new_cancel.setObjectName(_fromUtf8("pushButton_new_cancel"))
        self.pushButton_new = QtGui.QPushButton(self.centralwidget)
        self.pushButton_new.setGeometry(QtCore.QRect(20, 40, 85, 26))
        self.pushButton_new.setObjectName(_fromUtf8("pushButton_new"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 370, 101, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
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
        self.pushButton_update.setText(_translate("MainWindow", "Update", None))
        self.groupBox_insert.setTitle(_translate("MainWindow", "New Item", None))
        self.pushButton_new_insert.setText(_translate("MainWindow", "Insert", None))
        self.label_5.setText(_translate("MainWindow", "Quantidade", None))
        self.label_3.setText(_translate("MainWindow", "ID", None))
        self.label_4.setText(_translate("MainWindow", "Componente", None))
        self.pushButton_new_cancel.setText(_translate("MainWindow", "Cancel", None))
        self.pushButton_new.setText(_translate("MainWindow", "New", None))
        self.label_6.setText(_translate("MainWindow", "Comando SQLite", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuDataBase.setTitle(_translate("MainWindow", "DataBase", None))
        self.actionCreate_DataBase.setText(_translate("MainWindow", "Create DataBase", None))

