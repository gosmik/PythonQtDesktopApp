from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
import sys
from PyQt4.QtCore import Qt, QVariant
from PyQt4.QtGui import *
from PyQt4.QtSql import QSqlQuery
from PyQt4 import QtCore, QtGui, QtSql

import arayuz  # This file holds our MainWindow and all design related things
import dbLayer

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods


class ExampleApp(QtGui.QMainWindow, arayuz.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        self.query = QSqlQuery()

        self.btnCustomerList.clicked.connect(self.fillCustomerQombo)

        self.btnSave.clicked.connect(self.saveNewCustomer)
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('transport.db')
        model = QtSql.QSqlTableModel()
        self.initializeModel(model)

        view1 = self.createView("Table Model (View 1)", model)

        self.formLayout_2.addWidget(view1)

    def saveNewCustomer(self):
        dbLayer.SQLConnection.addNewCustomer(dbLayer.SQLConnection(),self.customerNameLineEdit.text())

    def fillCustomerQombo(self):
        self.query.exec("select * from customers");
        while (self.query.next()):
            id = self.query.value(0).toString()
            self.customerComboBox.addItem(id)


    def createView(self,title, model):
        view = QtGui.QTableView()
        view.setModel(model)
        view.setWindowTitle(title)
        return view

    def initializeModel(self,model):
        model.setTable('customers')
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function