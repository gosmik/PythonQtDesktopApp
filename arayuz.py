# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(560, 0, 231, 211))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.customerNameLabel = QtGui.QLabel(self.formLayoutWidget)
        self.customerNameLabel.setObjectName(_fromUtf8("customerNameLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.customerNameLabel)
        self.customerNameLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.customerNameLineEdit.setObjectName(_fromUtf8("customerNameLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.customerNameLineEdit)
        self.customerLocationLabel = QtGui.QLabel(self.formLayoutWidget)
        self.customerLocationLabel.setObjectName(_fromUtf8("customerLocationLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.customerLocationLabel)
        self.customerLocationLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.customerLocationLineEdit.setObjectName(_fromUtf8("customerLocationLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.customerLocationLineEdit)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label)
        self.btnSave = QtGui.QPushButton(self.formLayoutWidget)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.btnSave)
        self.formLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(509, 219, 291, 361))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_2)
        self.customerComboBox = QtGui.QComboBox(self.formLayoutWidget_2)
        self.customerComboBox.setObjectName(_fromUtf8("customerComboBox"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.customerComboBox)
        self.btnCustomerList = QtGui.QPushButton(self.formLayoutWidget_2)
        self.btnCustomerList.setObjectName(_fromUtf8("btnCustomerList"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.btnCustomerList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.customerNameLabel.setText(_translate("MainWindow", "Customer Name", None))
        self.customerLocationLabel.setText(_translate("MainWindow", "Customer Location", None))
        self.label.setText(_translate("MainWindow", "New Customer", None))
        self.btnSave.setText(_translate("MainWindow", "Save", None))
        self.label_2.setText(_translate("MainWindow", "Customer List", None))
        self.btnCustomerList.setText(_translate("MainWindow", "Customer List", None))
