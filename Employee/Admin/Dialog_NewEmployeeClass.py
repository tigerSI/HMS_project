from PySide.QtGui import QDialog, QPushButton, QGridLayout, QErrorMessage
from PySide.QtUiTools import QUiLoader
import Setting as s

class EditOrNewEmployeeDialog(QDialog):
    def __init__(self, editOrNew, id="", parent=None):
        QDialog.__init__(self, None)
        self.editOrNew = editOrNew
        self.parent = parent
        self.idEmployee = id
        self.returnVal = False
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
        elif self.editOrNew == "new":
            self.initUI_NEW()
        else:
            raise TypeError

    def initUI_EDIT(self):
        self.ui.id.setText(str(self.idEmployee))
        self.setDefaultType(self.idEmployee[:1])
        self.ui.type.setEnabled(False)

    def initUI_NEW(self):
        position = self.idEmployee
        index = self.ui.type.findText(position)
        self.ui.type.setCurrentIndex(index)
        self.ui.type.setEnabled(False)
        print("----init UI new Employee:" + str(position) + str("-----"))
        new_id = self.parent.getNewIDByUserType(position)
        self.ui.id.setText(new_id)
        self.setWindowTitle("new Employee " + str(position))

    def setDefaultType(self, type):
        text = ""
        if type == 'D':
            text = s.Position.doctor.name
        elif type == 'N':
            text = s.Position.nurse.name
        elif type == 'A':
            text = s.Position.admin.name
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
            if not self.parent.editEmployee(self.idEmployee, data, data[3]):
                error = QErrorMessage()
                error.showMessage("Invalid username: " + str(data[1]) + " already exist")
                error.setWindowTitle("Error!!!")
                error.exec_()
            else:
                self.returnVal = True

        elif self.editOrNew == 'new':
            if not self.parent.addNewEmployee(data, data[3]):
                error = QErrorMessage()
                error.showMessage("ID or/and Username is/are invalid")
                error.setWindowTitle("Error!!!")
                error.exec_()
            else:
                self.returnVal = True
        else:
            raise TypeError

    def cancel(self):
        pass

