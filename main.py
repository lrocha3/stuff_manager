import sys
from PyQt4 import QtCore, QtGui
from PyQt4 import QtCore
from form_main import *  # Load the form

class Main(QtGui.QMainWindow): # First Menu

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

 	self.ui.btn_update.clicked.connect(self.btn_update_cliked)

    def btn_update_cliked(self):
        self.ui.line_teste.setText("Helo")

def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    window.setWindowIcon(QtGui.QIcon('web.png'))      
    app.exec_()
   

if __name__ == '__main__':
    main()
