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
        buttons = QDialogButtonBox()
        buttons.addButton(QDialogButtonBox.Save)
        buttons.addButton(QDialogButtonBox.Discard)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout.addWidget(buttons)

    def accept(self, *args, **kwargs):
        print("accept")

    def reject(self, *args, **kwargs):
        print("in reject")
        # reply = QMessageBox.question("Yes", "No", QMessageBox.Yes, QMessageBox.No)
        # reply.show()
        # if reply == QMessageBox.Yes:
        #     QApplication.quit()
        #     print("Yes")
        # else:
        #     print("No")


class ConfirmMsgBox(QWidget):
    def __init__(self):
        reply = QMessageBox.question("Yes", "No", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.quit()
            print("Yes")
        else:
            print("No")
        layout = QLayout()
        layout.addWidget(reply)

# QMessageBox msgBox;
# msgBox.setText("The document has been modified.");
# msgBox.setInformativeText("Do you want to save your changes?");
# msgBox.setStandardButtons(QMessageBox::Save | QMessageBox::Discard | QMessageBox::Cancel);
# msgBox.setDefaultButton(QMessageBox::Save);
# int ret = msgBox.exec();
#
# switch (ret) {
#   case QMessageBox::Save:
#       // Save was clicked
#       break;
#   case QMessageBox::Discard:
#       // Don't Save was clicked
#       break;
#   case QMessageBox::Cancel:
#       // Cancel was clicked
#       break;
#   default:
#       // should never be reached
#       break;
# }




def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    exit(app.exec_())

if __name__ == "__main__":
    main()
