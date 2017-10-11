from PyQt4 import QtCore, QtGui
try:
    fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
 _fromUtf8 = lambda s: s

class Ui_Dialog(object):
 def setupUi(self, Dialog):
   Dialog.setObjectName(_fromUtf8("Dialog"))
   Dialog.resize(296, 236)
   self.tableWidget = QtGui.QTableWidget(Dialog)
   self.tableWidget.setGeometry(QtCore.QRect(20, 20, 256, 192))
   self.tableWidget.setRowCount(3)
   self.tableWidget.setColumnCount(2)
   self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
   self.tableWidget.setColumnCount(2)
   self.tableWidget.setRowCount(3)
   self.tableWidget.verticalHeader().setVisible(True)
   self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
   self.tableWidget.verticalHeader().setHighlightSections(True)
   self.retranslateUi(Dialog)
   QtCore.QMetaObject.connectSlotsByName(Dialog)

 def retranslateUi(self, Dialog):
      Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None,
QtGui.QApplication.UnicodeUTF8))