from PyQt4 import QtSql, QtGui
from PyQt4.QtSql import QSqlQuery

class SQLConnection:
    def __init__(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('transport.db')

        if not db.open():
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

        # query.exec_("insert into customers ('name') values('test customer')")
        if self.countCustomer() == 0:
            self.addNewCustomer('test musteri')
        if self.countLocations() == 0:
            self.query.exec_("insert into locations ('customer_id','name') values(1,'istanbul')")

        return

    def addNewCustomer(self,name):
        queryString ="insert into customers ('name') values('"+str(name)+"')"
        print(queryString)
        self.query.exec_(queryString)

    def addNewLocation(self,cus,loc):
        queryString ="insert into locations ('customer_id','name') values('"+str(cus)+"','"+str(loc)+"')"
        print(queryString)
        self.query.exec_(queryString)

    def getCutomerList(self):
        queryString ="select * from customers"
        self.query.exec_(queryString)
        while (self.query.next()):
            idString = self.query.value(0)

    def getLocationList(self):
        self.query.exec("select * from locations");
        while (self.query.next()):
            name = self.query.value(0).toString();
            self.cusLocWidget.addItem(name)
        print("select * from locations size "+str(self.query.size()))

    def countCustomer(self):
        queryString ="select count* from customers"
        self.query.exec_(queryString)

    def countLocations(self):
        queryString = "select count* from locations"
        self.query.exec_(queryString)

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    SQLConnection()