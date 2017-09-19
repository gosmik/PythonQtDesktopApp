import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    nameLabel = QLabel("Name")
    nameInput = QLineEdit()

    adressLabel = QLabel("Address")
    add1 = QLineEdit()
    add2 = QLineEdit()
    fbox = QFormLayout()
    fbox.addRow(nameLabel, nameInput)
    vbox = QVBoxLayout()

    vbox.addWidget(add1)
    vbox.addWidget(add2)
    fbox.addRow(adressLabel, vbox)
    hbox = QHBoxLayout()

    r1 = QRadioButton("Male")
    r2 = QRadioButton("Female")
    hbox.addWidget(r1)
    hbox.addWidget(r2)
    hbox.addStretch()
    fbox.addRow(QLabel("sex"), hbox)
    b1 = QPushButton(win)
    b1.setText("Button1")
    b1.clicked.connect(b1_clicked)
    fbox.addRow(b1, QPushButton("Cancel"))

    win.setLayout(fbox)

    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())

def b1_clicked():
   print ("Button 1 clicked")

if __name__ == '__main__':
    window()