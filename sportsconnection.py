from PyQt4 import QtSql, QtGui


def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sports.db')

    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                   QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n" "Click Cancel to exit."),
                                   QtGui.QMessageBox.Cancel)

        return False

    query = QtSql.QSqlQuery()

    query.exec_("CREATE TABLE GroupNames (  ID    integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,  Name  varchar(50)) ")

    query.exec_("insert into groupnames (name) values ("'testName'")")
    # query.exec_("insert into sportsmen values(101,'Christiano', 'Ronaldo')")
    # query.exec_("insert into sportsmen values(102,'Ussain', 'Bolt')")
    # query.exec_("insert into sportsmen values(103, 'Sachin', 'Tendulkar')")
    # query.exec_("insert into sportsmen values(104,'Saina', 'Nehwal')")
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