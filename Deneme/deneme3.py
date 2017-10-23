import sys
import site
from subprocess import Popen
from PyQt5.QtCore import(Qt)
from PyQt5 import QtCore, QtGui, QtSql,QtWidgets
from PyQt5.QtSql import(QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel)


class Window(QtWidgets):

    def __init__(self):

        super(Window, self).__init__()

        # Open and connect to database - this needs to be changed for the particular db you are using
        self.__database = QSqlDatabase.addDatabase('QPSQL')
        self.__database.setHostName('localhost')
        self.__database.setDatabaseName('~/Desktop/H2 testing/TESTING/db/db')
        self.__database.setPort(5435)
        self.__database.setUserName('grav')
        self.__database.setPassword('XXXXXXXXXX')
        self.__database.open()

        ok = self.__database.open()
        if ok == False:
            print ('Could not open database')
            print ('Text: ', self.__database.lastError().text())
            print ('Type: ', str(self.__database.lastError().type()))
            print ('Number: ', str(self.__database.lastError().number()))
            print ('Loaded drivers:', str(QSqlDatabase.drivers()))

        # Create the QSqlTableModel using the database
        self.modelDirections = QSqlTableModel(None, self.__database)
        self.modelDirections.setTable('PUBLIC.DIRECTIONS')
        self.modelDirections.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.modelDirections.select()

        # Create the QTableView and connect to the QSqlTableModel
        self.tableDirections = QTableView()
        self.tableDirections.setModel(self.modelDirections)

        # Create a QPushButton to add a row to the table
        self.buttonAddDir = QPushButton('Add direction')
        self.buttonAddDir.clicked.connect(self.createDirection)

        # Set up the rest of the window with the QTableView and the QPushButton
        vbox = QVBoxLayout()
        vbox.addWidget(self.tableDirections)
        vbox.addWidget(self.buttonAddDir)
        stretchBox = QWidget()
        stretchBox.setLayout(vbox)
        self.setCentralWidget(stretchBox)
        self.show()


    def createDirection(self):

        # Define and execute query to determine current max direction serial
        model = QSqlQueryModel()
        query = 'SELECT * FROM directions WHERE id=(SELECT MAX(id) FROM directions)'
        model.setQuery(query)
        if model.record(0).value('id').toString() == '':
            newDirectionSerial = 0
        else:
            newDirectionSerial = int(model.record(0).value('id').toString()) + 1

        # Define queries to insert new direction record
        queryText = 'INSERT INTO public.directions (id, text, olddir, opposite) \
        VALUES (%s, NULL, 1, NULL)' % (newDirectionSerial)
        query = QSqlQuery()
        query.exec_(queryText)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    newWindow = Window()
    sys.exit(app.exec_())