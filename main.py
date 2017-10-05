from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
import sys
from PyQt4 import QtCore, QtGui, QtSql

import arayuz  # This file holds our MainWindow and all design related things

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

        self.btnRefreshLocations.clicked.connect(self.initComboBox)
        self.btnSaveLocation.clicked.connect(self.saveNewLocation)

        self.btnSave.clicked.connect(self.saveNewCustomer)
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('transport.db')

        if not self.db.open():
            QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                       QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                     "This example needs SQLite support. Please read "
                                                     "the Qt SQL driver documentation for information "
                                                     "how to build it.\n\n" "Click Cancel to exit."),
                                       QtGui.QMessageBox.Cancel)

            return

        self.query = QtSql.QSqlQuery()
        self.query.exec_("CREATE TABLE customers (customer_id integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,  name  varchar(50)) ")
        self.query.exec_("CREATE TABLE locations (location_id  integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE , customer_id INT, name  varchar(50), "
                    "FOREIGN KEY (customer_id) REFERENCES customers(customer_id)) ")

        ok = self.db.open()
        if (ok):
            self.initComboBox()
            self.initCusLocWidget()

    def saveNewCustomer(self):
        self.query.clear()
        queryString ="insert into customers ('name') values('"+str(self.customerNameLineEdit.text())+"')"
        print("saveNewCustomer"+queryString)
        self.query.exec(queryString)
        print(self.query.lastError())
        self.initComboBox()

    def saveNewLocation(self):
        self.query.clear()
        queryString ="insert into locations ('customer_id','name') values('"+str(self.customerComboBox.currentText())+"','"+str(self.newLocationLineEdit.text())+"')"
        print("saveNewLocation"+queryString)
        self.query.exec(queryString)


    def initComboBox(self):
        self.customersModel = QtSql.QSqlTableModel()
        self.customersModel.setTable('customers')
        self.customersModel.select()

        self.customerComboBox.setModel(self.customersModel)
        self.customerComboBox.setModelColumn(1)

    def initCusLocWidget(self):
        self.query.clear()
        isOk = self.query.exec("select * from locations")
        if isOk:
            while (self.query.next()):
                name = self.query.value(0).toString();
                self.cusLocWidget.addItem(name)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function