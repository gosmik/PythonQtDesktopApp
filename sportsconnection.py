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

    query.exec_("create table sportsmen(id int primary key, "
                "firstname varchar(20), lastname varchar(20))")

    query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
    query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
    query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
    query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
    query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
    return True

def addNewRow(id,name,surname):
    query = QtSql.QSqlQuery()
    queryString ="insert into sportsmen values("+str(id)+", 'Yusuf1', 'Unlu')"
    print(queryString)
    query.exec_(queryString)

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    createDB()