from PyQt4 import QtSql, QtGui


def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('transport.db')

    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                   QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n" "Click Cancel to exit."),
                                   QtGui.QMessageBox.Cancel)

        return False

    query = QtSql.QSqlQuery()

    query.exec_("CREATE TABLE customers (customer_id integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,  name  varchar(50)) ")
    query.exec_("CREATE TABLE locations (location_id  integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE , customer_id INT, name  varchar(50), "
                "FOREIGN KEY (customer_id) REFERENCES customers(customer_id)) ")

    query.exec_("insert into customers values(null,'test customer')")
    query.exec_("insert into locations values(null,1,'istanbul')")

    return True

def addNewRow(id,name,surname):
    query = QtSql.QSqlQuery()
    queryString ="insert into sportsmen values("+str(id)+", '"+name+"', '"+surname+"')"
    print(queryString)
    query.exec_(queryString)

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    createDB()