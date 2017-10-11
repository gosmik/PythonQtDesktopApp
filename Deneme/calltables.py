from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
import sys
from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import tables  # This file holds our MainWindow and all design related things

class MyForm(QtGui.QDialog):
 def __init__(self, data):
  QtGui.QWidget.__init__(self)
  self.ui = Ui_Dialog()
  self.ui.setupUi(self)
  self.data=data
  self.addcontent()

  def addcontent(self):
   row=0
   for tup in self.data:
    col=0
    for item in tup:
     anitem=QTableWidgetItem(item)
     self.ui.tableWidget.setItem(row,col, anitem)
     col+=1
    row+=1

data=[]
data.append(('John', 'johny@gmail.com'))
data.append(('Caroline', 'caroline@hotmail.com'))
data.append(('Bintu', 'bintu@yahoo.com'))

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm(data)
  myapp.show()
  sys.exit(app.exec_())