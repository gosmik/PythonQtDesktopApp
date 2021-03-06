import sys
from PyQt5 import QtCore, QtGui, QtSql,QtWidgets

import arayuz  # This file holds our MainWindow and all design related things

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods


class ExampleApp(QtWidgets.QMainWindow, arayuz.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined

        self.btnRefreshLocations.clicked.connect(self.initCustomerComboBox)
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
        self.query.exec_("CREATE TABLE customers (customer_name integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,  name  varchar(50)) ")
        self.query.exec_("CREATE TABLE locations (location_id  integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE , customer_name INT, name  varchar(50), "
                    "FOREIGN KEY (customer_name) REFERENCES customers(customer_name)) ")
        self.query.exec_("CREATE TABLE items (item_id integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE , item_name varchar(50), item_price  integer)")
        self.query.exec_(
            "CREATE TABLE item_customer (item_customer_id  integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE , item_customer_discounted  integer)")
        self.query.exec_(
            "CREATE TABLE quotes (quote_id  integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE , start_loc_id INT, end_loc_id INT,customer_name  varchar(50) "
            "FOREIGN KEY (customer_name) REFERENCES customers(customer_name)) ")
        ok = self.db.open()
        if (ok):
            self.initCustomerComboBox()
            self.initCusLocWidget()
            self.initItemPriceCustomerTable()
            self.initQuoteCustomerCombo()
            self.initQuoteStartLoc()

        self.menuShow_Tables.triggered.connect(self.initItemPriceCustomerTable)
        self.newItemSaveBtn.clicked.connect(self.saveNewItem)

    def saveNewCustomer(self):
        self.query.clear()
        queryString ="insert into customers ('name') values('"+str(self.customerNameLineEdit.text())+"')"
        print("saveNewCustomer"+queryString)
        self.query.exec(queryString)
        print(self.query.lastError())
        self.initCustomerComboBox()

    def saveNewLocation(self):
        self.query.clear()
        queryString ="insert into locations ('customer_name','name') values('"+str(self.customerComboBox.currentText())+"','"+str(self.newLocationLineEdit.text())+"')"
        print("saveNewLocation"+queryString)
        self.query.exec(queryString)
        print(self.query.lastError())
        self.initCusLocWidget()

    def saveNewItem(self):
        self.query.clear()
        queryString ="insert into items ('item_name','item_price')  values('"+self.itemNameLineEdit.text()+"','"+self.tonPriceLineEdit.text()+"')"
        self.query.exec(queryString)
        print("saveNewItem: "+queryString)
        print("query error: "+self.query.lastError().text())
        self.initItemPriceCustomerTable()

    def initCustomerComboBox(self):
        self.customersModel = QtSql.QSqlTableModel()
        self.customersModel.setTable('customers')
        self.customersModel.select()

        self.customerComboBox.setModel(self.customersModel)
        self.customerComboBox.setModelColumn(1)
        # self.connect(self.customerComboBox,QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.initCusLocWidget)
        # self.customerComboBox.currentIndexChanged(self.initQuoteCustomerCombo())

    def initItemPriceCustomerTable(self):
        self.itemsModel = QtSql.QSqlTableModel()
        self.itemsModel.setTable('items')
        self.itemsModel.select()
        self.itemsModel.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.tableView.setModel(self.itemsModel)

    def initItemDiscountTable(self):
        self.itemDiscountModel = QtSql.QSqlTableModel()
        self.itemDiscountModel.setTable('item_customer')
        self.itemDiscountModel.select()
        self.itemDiscountModel.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.itemDiscountsTable.setModel(self.itemDiscountModel)

    def initCusLocWidget(self):
        self.query.clear()
        self.cusLocWidget.clear()
        queryString = "select customer_name,name from locations where customer_name='"+self.customerComboBox.currentText()+"'"
        print("initCusLocWidget: "+queryString)
        isOk = self.query.exec(queryString)
        if isOk:
            while (self.query.next()):
                name = self.query.value(1);
                self.cusLocWidget.addItem(name)

    def initQuoteCustomerCombo(self):
        self.customersModel = QtSql.QSqlTableModel()
        self.customersModel.setTable('customers')
        self.customersModel.select()
        self.chooseQuoteCustomerCombo.activated.connect(self.initQuoteStartLoc)

        self.chooseQuoteCustomerCombo.setModel(self.customersModel)
        self.chooseQuoteCustomerCombo.setModelColumn(1)
        self.chooseQuoteCustomerCombo.activated.connect(self.initQuoteStartLoc)
        # self.connect(self.chooseQuoteCustomerCombo,QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.initQuoteStartLoc)

    def initQuoteStartLoc(self):
        self.query.clear()
        self.chooseStartLocationComboBox.clear()
        queryString = "select customer_name,name from locations where customer_name='"+self.chooseQuoteCustomerCombo.currentText()+"'"
        print("initQuoteStartLoc: "+queryString)
        isOk = self.query.exec(queryString)
        if isOk:
            while (self.query.next()):
                name = self.query.value(1);
                self.chooseStartLocationComboBox.addItem(name)
        # self.connect(self.chooseStartLocationComboBox, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.initQuoteEndLoc)
        self.chooseStartLocationComboBox.activated.connect(self.initQuoteEndLoc)

    def initQuoteEndLoc(self):
        self.query.clear()
        self.chooseEndLocationComboBox.clear()
        queryString = "select customer_name,name from locations where customer_name='"+self.chooseQuoteCustomerCombo.currentText()+"' and name <> '" + self.chooseStartLocationComboBox.currentText()+"'"
        print("initQuoteEndLoc: "+queryString)
        isOk = self.query.exec(queryString)
        if isOk:
            while (self.query.next()):
                name = self.query.value(1);
                self.chooseEndLocationComboBox.addItem(name)


def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function