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

        global query
        query = QtSql.QSqlQuery()

        query.exec_("CREATE TABLE customers (customer_id integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,  name  varchar(50)) ")
        query.exec_("CREATE TABLE locations (location_id  integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE , customer_id INT, name  varchar(50), "
                    "FOREIGN KEY (customer_id) REFERENCES customers(customer_id)) ")

        # query.exec_("insert into customers ('name') values('test customer')")
        self.addNewCustomer('test musteri')
        query.exec_("insert into locations ('customer_id','name') values(1,'istanbul')")

        return

    def addNewLocationOfCustomer(id,name):
        query.prepare("INSERT INTO locations (customer_id, name) "
                      "VALUES (:customer_id, :name)");
        query.bindValue(":customer_id", id);
        query.bindValue(":name", name);
        query.exec();

    def addNewCustomer(self,name):
        queryString ="insert into customers ('name') values('"+str(name)+"')"
        print(queryString)
        query.exec_(queryString)

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    SQLConnection()