import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        loader = QUiLoader()
        ui = loader.load('searchWidget.ui', self)
        self.setCentralWidget(ui)
        self.ip_name = ui.findChild(QLineEdit, "ip_name")
        self.list_patient = ui.findChild(QListWidget, "list_patient")
        self.b_search = ui.findChild(QPushButton, "b_search")
        self.b_search.clicked.connect(self.search)

        self.addPatient("Boss")
        self.addPatient("Boss")
        self.addPatient("Nut")
        self.addPatient("Fuck")
        self.addPatient("Eiei")

    def search(self):
        input_text = self.ip_name.text()
        out = self.list_patient.findItems(input_text, Qt.MatchExactly)
        self.updateListPatient(out)

    def updateListPatient(self, lst):
        temp = list()
        for i in lst:
            temp.append(i.text())
        self.list_patient.clear()
        for i in temp:
            self.addPatient(i)
        self.list_patient.update()

    def addPatient(self, name):
        self.list_patient.addItem(name)

    def delPatient(self):
        pass

global w
def main():
    app = QApplication(sys.argv)
    w = Login()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())