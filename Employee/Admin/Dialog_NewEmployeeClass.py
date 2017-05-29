from PySide.QtGui import QDialog, QPushButton, QGridLayout
from PySide.QtUiTools import QUiLoader
import Setting as s

class EditOrNewEmployeeDialog(QDialog):
    def __init__(self, editOrNew, id=0, parent=None):
        QDialog.__init__(self, None)
        self.editOrNew = editOrNew
        self.parent = parent
        self.idEmployee = id
        self.initUI()
        self.initLayout()
        self.forDev()
        self.show()

    def initUI(self):
        posX, posY, sizeW, sizeH = s.GEOMETRY_DIALOG_NEW_EMPLOYEE
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.ui = QUiLoader().load('Employee/Admin/View/create_new_employee.ui', self)
        self.setWindowTitle("New Employee")
        self.b_save = self.ui.findChild(QPushButton, "b_save")
        self.b_cancel = self.ui.findChild(QPushButton, "b_cancel")
        self.b_save.clicked.connect(self.save)
        self.b_cancel.clicked.connect(self.cancel)
        if self.editOrNew == "edit":
            self.initUI_EDIT()

    def initUI_EDIT(self):
        self.ui.id.setText(str(self.idEmployee))
        self.setDefaultType(self.idEmployee[:1])
        self.ui.type.setEnabled(False)

    def setDefaultType(self, type):
        text = ""
        if type == 'D':
            text = 'Doctor'
        elif type == 'N':
            text = 'Nurse'
        elif type == 'A':
            text = 'Admin'
        else:
            raise TypeError
        index = self.ui.type.findText(text)
        self.ui.type.setCurrentIndex(index)
        self.setWindowTitle("Edit Employee " + str(text))

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

    def getData(self):
        return [self.ui.id.text(),
                self.ui.username.text(),
                self.ui.password.text(),
                self.ui.type.currentText(),
                self.ui.firstname.text(),
                self.ui.lastname.text(),
                self.ui.phonenumber.text()]

    def forDev(self):
        self.ui.password.setText('1234')
        self.ui.firstname.setText('Atichat')
        self.ui.lastname.setText('Lappanopakon')
        self.ui.phonenumber.setText('0971249197')

    def save(self):
        data = self.getData()
        if self.editOrNew == 'edit':
            self.parent.editEmployee(self.idEmployee, data)
        elif self.editOrNew == 'new':
            self.parent.newEmployee(data)
        else:
            raise TypeError

    def cancel(self):
        pass

