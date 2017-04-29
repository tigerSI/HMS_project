import sys

from PySide.QtCore import QRegExp, QPoint
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader

from Base.Dialog_MsgBox import ConfirmMsgClass
from Patient import PatientClass

class newDoctorDialog(QDialog):
    def __init__(self, parent = None):
        super(newDoctorDialog, self).__init__(parent)
        self.setGeometry(300,200,400,400)
        self.loader = QUiLoader()
        self.ui = self.loader.load('./view/Dialog_newDoctorUI.ui', self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.ui)
        self.initUI()



        #Line Edit with QDoubleValidator must be int
        # self.l = QLineEdit()
        # validator = QDoubleValidator()
        # self.l.setValidator(validator)
        # self.l.textChanged.connect(self.check_state)
        # self.l.textChanged.emit(self.l.text())
        # self.layout.addWidget(self.l)
        # self.show()


    def initUI(self):
        self.setInput = []
        self.setInput.append(self.ui.findChild(QLineEdit, "lineEdit_1"))
        self.setInput.append(self.ui.findChild(QLineEdit, "lineEdit_2"))
        self.setInput.append(self.ui.findChild(QLineEdit, "lineEdit_3"))
        self.setInput.append(self.ui.findChild(QLineEdit, "lineEdit_4"))
        self.setInput.append(self.ui.findChild(QLineEdit, "lineEdit_5"))
        self.setInput.append(self.ui.findChild(QLineEdit, "lineEdit_6"))
        self.b_save = self.ui.findChild(QPushButton, "b_save")
        self.b_cancel = self.ui.findChild(QPushButton, "b_cancel")
        self.b_save.clicked.connect(self.save)
        self.b_discard.clicked.connect(self.discard)

    def setLineEdit(self):
        self.setInput[6].textchanged.connect(self.check_state)

    def setValidation(self):
        checkInt = QIntValidator()
        self.setInput[6].setValidator(checkInt)

    def check_state(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if state == QValidator.Acceptable:
            color = '#c4df9b'  # green
        elif state == QValidator.Intermediate:
            color = '#fff79a'  # yellow
        else:
            color = '#f6989d'  # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def onTextChange(self, text):
        regExp = QRegExp()
        regExp.setPattern("[^0-9]*")
        m_correctText = ""
        if regExp.exactMatch(text):
            m_correctText = text
            QToolTip.hideText()

        else:
            point = QPoint(self.l.geometry().left(), self.l.geometry().bottom())
            self.l.setText(m_correctText)
            QToolTip.showText(point, "Cannot enter number..")

    def save(self):
        self.ans = []
        for i in range(len(self.setInput1)):
            self.ans.append(self.setInput1[i].text())
        print(self.ans)
        return True

    def cancel(self):
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