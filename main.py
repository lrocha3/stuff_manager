import sys

from PyQt4.QtGui import QMainWindow, QApplication, QIcon
from form_main import Ui_MainWindow  # Load the form | Class in form_main.py


class Main(QMainWindow): # First Menu

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_update.clicked.connect(self.btn_update_cliked)

    def btn_update_cliked(self):
        self.ui.line_teste.setText("Hello")
        

def main():
    app = QApplication(sys.argv)
    window=Main()
    window.show()
    window.setWindowIcon(QIcon('web.png'))      
    app.exec_()
   

if __name__ == '__main__':
    main()
