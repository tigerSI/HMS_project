import sys
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader

from Base.Dialog_MsgBox import ConfirmMsgClass
from Patient import PatientClass

class ExampleDialog(QDialog):
    def __init__(self, parent = None):
        super(ExampleDialog, self).__init__(parent)
        self.setGeometry(300,200,400,400)
        self.loader = QUiLoader()
        self.ui = self.loader.load('./widgetTestDialog.ui', self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.ui)
        self.initUI()
        self.show()

    def initUI(self):
        self.setInput1 = []
        self.setInput1.append(self.ui.findChild(QLineEdit, "lineEdit_1"))
        self.setInput1.append(self.ui.findChild(QLineEdit, "lineEdit_2"))
        self.setInput1.append(self.ui.findChild(QLineEdit, "lineEdit_3"))

        self.b_save = self.ui.findChild(QPushButton, "b_save")
        self.b_discard = self.ui.findChild(QPushButton, "b_discard")
        self.b_save.clicked.connect(self.save)
        self.b_discard.clicked.connect(self.discard)

    def save(self):
        self.ans = []
        for i in range (len(self.setInput1)):
            self.ans += self.setInput1[i].text() + "\n"
        return True

    def discard(self):
        dialog = ConfirmMsgClass.ConfirmYesNo()
        if dialog.ans == True:
            print("Discard")
            self.close()
        else:
            print("Cancel")

def main():
    app = QApplication(sys.argv)
    win = ExampleDialog()
    exit(app.exec_())

if __name__ == "__main__":
    main()