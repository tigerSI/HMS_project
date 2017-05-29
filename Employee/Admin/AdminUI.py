from PySide.QtGui import *
from Base.Widget_ManagePerson import Widget_ManagePersonClass
from Employee.Admin import Admin
import Employee.Admin.Dialog_NewEmployeeClass as d
import Setting as s

from enum import Enum
class UserPosition(Enum):
    doctor = 0
    nurse = 1
    admin = 2

class MainWindowAdmin(QMainWindow):
    def __init__(self, user):
        super(MainWindowAdmin, self).__init__()
        self.ctrlDatabase = Admin.AdminApplication()
        self.user = user
        self.all_user = []
        self.initUI()
        self.initLayout()
        self.initButton()
        # self.allRowDatabaseDoctor = []
        # self.allRowDatabaseNurse = []
        # self.allRowDatabaseAdmin = []

    def initUI(self):
        posX, posY, sizeW, sizeH = s.GEOMETRY_MAINWIDOW
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.setWindowTitle("Admin Main Window")
        self.setTab()
        self.show()

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tabWidget)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def setTab(self):
        self.updateDatabase()
        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet(s.SS_TabWidget)
        self.tab1 = Widget_ManagePersonClass.WidgetManagePerson("Doctor", self)
        self.tab1.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[UserPosition.doctor.value])
        self.tab2 = Widget_ManagePersonClass.WidgetManagePerson("Nurse", self)
        self.tab2.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[UserPosition.nurse.value])
        self.tab3 = Widget_ManagePersonClass.WidgetManagePerson("Admin", self)
        self.tab3.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[UserPosition.admin.value])
        self.tabWidget.addTab(self.tab1, "Doctor")
        self.tabWidget.addTab(self.tab2, "Nurse")
        self.tabWidget.addTab(self.tab3, "Admin")


    def initButton(self):
        self.b_newDoctor = self.tab1.b_newPerson
        self.b_newDoctor.clicked.connect(lambda: self.newEmployee(UserPosition.doctor.value))
        self.b_newNurse = self.tab2.b_newPerson
        self.b_newNurse.clicked.connect(lambda: self.newEmployee(UserPosition.nurse.value))
        self.b_newAdmin = self.tab3.b_newPerson
        self.b_newAdmin.clicked.connect(lambda: self.newEmployee(UserPosition.admin.value))

    def updateDatabase(self):
        self.ctrlDatabase.getListByPosition()
        self.all_user = []
        self.all_user.append(self.ctrlDatabase.getListDoctor())
        self.all_user.append(self.ctrlDatabase.getListNurse())
        self.all_user.append(self.ctrlDatabase.getListAdmin())

    def updateTable(self, type):
        self.updateDatabase()
        if type == UserPosition.doctor.name:
            print("Update Table: " + str(type))
            self.all_user[UserPosition.doctor.value] = self.ctrlDatabase.getListDoctor()
            self.tab1.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[UserPosition.doctor.value])
        elif type == UserPosition.nurse.name:
            print("Update Table: " + str(type))
            self.all_user[UserPosition.nurse.value] = self.ctrlDatabase.getListNurse()
            self.tab2.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[UserPosition.nurse.value])
        elif type == UserPosition.admin.name:
            print("Update Table: " + str(type))
            self.all_user[UserPosition.admin.value] = self.ctrlDatabase.getListAdmin()
            self.tab3.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[UserPosition.admin.value])
        else:
            raise TypeError

    def getListUserByType(self, type):
        if type == "D":
            return UserPosition.doctor.value
        elif type == "N":
            return UserPosition.nurse.value
        elif type == "A":
            return UserPosition.admin.value
        else:
            raise ValueError

    def editButtonPressed(self, id):
        position = self.getListUserByType(id[:1])
        for i in range(len(self.all_user[position])):
            if id == self.all_user[position][i].id:
                dialog = d.EditOrNewEmployeeDialog("edit", id, self)
                dialog.show()
                dialog.exec_()

    def editEmployee(self, id, data, type):
        if self.ctrlDatabase.editEmployee(id, data, type):
            self.updateTable(type)
            return True
        return False

    def newEmployee(self, position):
        print("in Employee")
        dialog = d.EditOrNewEmployeeDialog("new")
        dialog.show()
        dialog.exec_()
        if position == UserPosition.doctor.value:
            pass
        elif position == UserPosition.nurse.value:
            pass
        elif position == UserPosition.admin.value:
            pass
        else:
            raise TypeError



