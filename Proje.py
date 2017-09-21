import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()

        file = bar.addMenu("File")
        file.addAction("New Customer")
        file.addAction("New Route")

        view = bar.addMenu("View")
        view.addAction("Cascade")
        view.addAction("Tiled")

        file.triggered[QAction].connect(self.fileMenuActions)
        view.triggered[QAction].connect(self.viewMenuActions)
        self.setWindowTitle("Transport Invoices")

    def fileMenuActions(self, q):
        print("File menu triggered")
        if q.text() == "New Customer":
            MainWindow.count = MainWindow.count + 1
            self.sub = QMdiSubWindow()
            self.sub.setWidget(QTextEdit())
            self.sub.setWindowTitle("New Customer " + str(MainWindow.count))
            self.mdi.addSubWindow(self.sub)
            self.sub.show()

        if q.text() == "New Route":
            MainWindow.count = MainWindow.count + 1

            self.sub = QMdiSubWindow()
            widget = QWidget()
            nameLabel = QLabel("Name")
            nameInput = QLineEdit()

            adressLabel = QLabel("Address")
            add1 = QLineEdit()
            fbox = QFormLayout()
            fbox.addRow(nameLabel, nameInput)
            vbox = QVBoxLayout()

            vbox.addWidget(add1)
            fbox.addRow(adressLabel, vbox)

            b1 = QPushButton(widget)
            b1.setText("Save Customer")
            b1.clicked.connect(lambda:self.save_clicked(nameInput.text(),add1.text()))

            cancelButton = QPushButton(widget)
            cancelButton.setText("Cancel Customer")
            cancelButton.clicked.connect(self.cancel_clicked)

            fbox.addRow(b1, cancelButton)

            widget.setLayout(fbox)

            self.sub.setWidget(widget)
            # sub.setWidget(QTextEdit())

            self.sub.setWindowTitle("New Route " + str(MainWindow.count))
            self.mdi.addSubWindow(self.sub)
            self.sub.show()

    def viewMenuActions(self, q):
        print("View menu triggered")
        if q.text() == "Cascade":
            self.mdi.cascadeSubWindows()

        if q.text() == "Tiled":
            self.mdi.tileSubWindows()


    def save_clicked(self,name,adress):
        print(name+adress)
        print("Save Customer clicked")

    def cancel_clicked(self):
        print("Cancel Customer clicked")
        self.sub.hide()

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
