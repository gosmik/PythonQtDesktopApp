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

        self.btnRefreshLocations.clicked.connect(self.initComboBox)

        self.btnSave.clicked.connect(self.saveNewCustomer)
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('transport.db')

        self.initComboBox()


    def saveNewCustomer(self):
        dbLayer.SQLConnection.addNewCustomer(dbLayer.SQLConnection(),self.customerNameLineEdit.text())
    def saveNewLocation(self):
        dbLayer.SQLConnection.addNewCustomer(dbLayer.SQLConnection(),self.newLocationLineEdit.text(),self.customerComboBox.currentText())

    def initComboBox(self):
        self.locationsModel = QtSql.QSqlTableModel()
        self.locationsModel.setTable('locations')
        self.locationsModel.select()

        self.customerComboBox.setModel(self.locationsModel)
        self.customerComboBox.setModelColumn(2)

    def fillCustomerQombo(self):
        self.query.exec("select * from customers");
        while (self.query.next()):
            id = self.query.value(0).toString()
            self.customerComboBox.addItem(id)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function