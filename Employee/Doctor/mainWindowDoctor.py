import sys

from PySide.QtCore import QDateTime, Qt

import ControllerClass
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
from Patient.view import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.loader = QUiLoader()
        self.tabWidget = QTabWidget()
        self.centralWidget = QWidget()
        self.initUI()
        #self.initButtonTab1()
        self.initButtonTab2()

    def initUI(self):
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("Doctor window")
        self.setTab()
        grid = QGridLayout()
        grid.addWidget(self.tabWidget)
        self.centralWidget.setLayout(grid)
        self.setCentralWidget(self.centralWidget)
        self.show()

    def setTab(self):
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 35px; width: 100px; }")
        self.tab1 = self.loader.load('./view/tab1_Calendar.ui', self)
        self.tab2 = self.loader.load('./view/tab2_Patient.ui', self)
        self.tabWidget.addTab(self.tab1, "Dashboard")
        self.tabWidget.addTab(self.tab2, "Patient")

    def initButtonTab2(self):
        b_newPatient = self.tab2.findChild(QPushButton, "b_newPatient")
        b_newPatient.clicked.connect(self.addNewPatient)

    def addNewPatient(self):
        q = QDialog()
        # allTab = self.loader.load('./view/dialog_newPatient.ui', self)
        # allTab.setModal(True)
        # allTab.setGeometry(600,600,600,1000)
        # allTab.show()
        dialog = TestDialog()
        dialog.show()
        dialog.exec_()


class TestDialog(QDialog):
    def __init__(self, parent = None):
        super(TestDialog, self).__init__(parent)
        self.setGeometry(300,200,400,400)
        self.loader = QUiLoader()
        ui = self.loader.load('./view/widgetTestDialog.ui', self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(ui)
        self.initButtons()

    def initButtons(self):
        save = QPushButton("Save")
        buttons = QDialogButtonBox()
        buttons.addButton(save, QDialogButtonBox.AcceptRole)
        buttons.addButton(QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout.addWidget(buttons)



    def accept(self):
        print("accept")
    def reject(self):
        print("reject")


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    exit(app.exec_())

if __name__ == "__main__":
    main()
