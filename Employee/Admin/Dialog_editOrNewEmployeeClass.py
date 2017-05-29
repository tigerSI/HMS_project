import sys
import psycopg2
from PySide.QtCore import QRegExp, QPoint
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
from Employee.Admin.AdminClass import *
from Employee.Doctor.DoctorUI import *
from Employee.Nurse.NurseClass import *
from Base.Dialog_MsgBox import ConfirmMsgClass
from Patient import PatientClass

class EditOrNewEmployeeDialog(QDialog):
    def __init__(self, id=0, parent=None):
        super(EditOrNewEmployeeDialog, self).__init__(parent)
        self.idEmployee = id
        posX, posY, sizeW, sizeH = s.GEOMETRY_DIALOG_NEW_EMPLOYEE
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.loader = QUiLoader()
        self.ui = self.loader.load('Employee/Admin/View/create_new_employee.ui', self)
        self.initUI()
        self.initLayout()
        self.show()


    def initUI(self):
        self.ui.id.setText(str(self.idEmployee))
        #s = i.findText(str(post[count]))
        #i.setCurrentIndex(s)
        self.b_save = self.ui.findChild(QPushButton, "b_save")
        self.b_cancel = self.ui.findChild(QPushButton, "b_cancel")
        self.b_save.clicked.connect(self.save)
        self.b_cancel.clicked.connect(self.cancel)
        #self.setValidation()
        #self.setLineEdit()
    '''
    def setLineEdit(self):
        if self.idEmployee != 0:
            text = []
            #getText from database search
            for i in range(len(self.setInput)):
                self.setInput[i].setText(text[i])

        self.setInput[5].textChanged.connect(self.check_state)
        self.setInput[5].textChanged.emit(self.setInput[5].text())

    def setValidation(self):
        checkInt = QDoubleValidator()
        self.setInput[5].setValidator(checkInt)

    def check_state(self, *args, **kwargs):
        if self.setInput[3].text() == self.setInput[4].text():
            color = '#c4df9b'
            self.setInput[4].setStyleSheet('QLineEdit { background-color: %s }' % color)
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
        else:
            color = '#f6989d'
            self.setInput[4].setStyleSheet('QLineEdit { background-color: %s }' % color)

    def check_password(self, *args, **kwargs):
        pass

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
    '''

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

    def getData(self):
        text = []
        text.append(self.ui.type.currentText())
        #id
        text.append(self.ui.username.text())
        text.append(self.ui.password.text())
        text.append(self.ui.firstname.text())
        text.append(self.ui.lastname.text())
        text.append(self.ui.phonenumber.text())
        return text

    def forDev(self):
        self.ui.type.currentText()
        self.ui.username.text()
        self.ui.password.text()
        self.ui.firstname.text()
        self.ui.lastname.text()
        self.ui.phonenumber.text()


    def save(self):
        pass

    def cancel(self):
        pass

