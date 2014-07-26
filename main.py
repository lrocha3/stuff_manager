from PyQt4.QtGui import QMainWindow, QApplication, QIcon
from PyQt4.QtCore import QString
from PyQt4 import QtSql
import sys
import os.path
from form_main import Ui_MainWindow  # Load the form | Class in form_main.py


class Main(QMainWindow): # First Menu
    

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.groupBox_insert.hide()
        self.ui.pushButton_update.clicked.connect(self.pushButton_update_clicked)
        self.ui.actionCreate_DataBase.triggered.connect(self.actionCreate_DataBase_open)
        self.ui.pushButton_new_insert.clicked.connect(self.pushButton_new_insert_clicked)  
        self.ui.pushButton_new.clicked.connect(self.pushButton_new_clicked)   
        self.ui.pushButton_new_cancel.clicked.connect(self.pushButton_new_cancel_clicked)
        
    def pushButton_update_clicked(self):
        self.ui.line_teste.setText("Update")
        
        
    def actionCreate_DataBase_open(self):
        self.ui.line_teste.setText("Update")
    
    def pushButton_new_clicked(self):
        self.ui.groupBox_insert.show()
     
                
    def pushButton_new_insert_clicked(self):
        query = QtSql.QSqlQuery()
        comando = QString("INSERT INTO person (id, componente, quantidade) VALUES (" + self.ui.lineEdit_id.text()+ ", '" + self.ui.lineEdit_componente.text() + "', " + self.ui.lineEdit_quantidade.text()  + ")")
        self.ui.line_teste.setText(comando)
        query.exec_(comando)
        self.ui.groupBox_insert.setHidden(1)
        self.clear_new_fields()

    def clear_new_fields(self):
        self.ui.lineEdit_id.setText("")
        self.ui.lineEdit_componente.setText("")
        self.ui.lineEdit_quantidade.setText("")
        
    def pushButton_new_cancel_clicked(self):
        self.ui.groupBox_insert.setHidden(1)
        self.clear_new_fields()

        
    
        
        
                
def DataBase():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('stuff.db')
    
    if not os.path.isfile('stuff.db'):   # Se nao existir cria e poem um item!
        db.open()

        if db:  # Se consegue abrir a base de dados, cria a tabela
            query = QtSql.QSqlQuery()
            query.exec_("create table person(id int primary key, componente varchar(20), quantidade int)")
    
    else:
        db.open()
        
        

def main():
    
    app = QApplication(sys.argv)
    DataBase()
    window=Main()
    window.show()
    window.setWindowIcon(QIcon('web.png'))      
    app.exec_()
   

if __name__ == '__main__':
    main()