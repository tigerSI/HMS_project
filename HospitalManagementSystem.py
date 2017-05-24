from PySide.QtGui import *
import ReturnValueClass
import Login
import Setting
from Employee.Admin import mainWindowAdmin as Admin
from Employee.Doctor import mainWindowDoctor as Doctor
from Employee.Nurse import mainWindowNurse as Nurse
from Employee.Roommanager import mainWindowRoomManager as RoomManager


class HMS(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        #self.position = ReturnValueClass.Choice()
        self.initCentalWidget()

    def initCentalWidget(self):
        self.login_widget = Login.LoginWindow()
        self.central_widget.addWidget(self.login_widget)
        self.centralWidget().setCurrentWidget(self.login_widget)

    def loginSucess(self):
        self.mainWindow = QMainWindow()
        choice = self.position.getChoice()
        if choice == Setting.Position.admin.value:
            self.mainWindow = Admin.MainWindowAdmin()
        elif choice == Setting.Position.doctor.value:
            self.mainWindow = Doctor.MainWindowDoctor()
        elif choice == Setting.Position.nurse.value:
            self.mainWindow = Nurse.MainWindowNurse()
        elif choice == Setting.Position.roomManager.value:
            print("in")
            self.mainWindow = RoomManager.MainWindowRoomManager()
        else:
            print("Error")
        self.central_widget.addWidget(self.mainWindow)
        self.centralWidget().setCurrentWidget(self.mainWindow)


def main():
    from PySide.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)
    window = HMS()
    window.show()
    exit(app.exec_())

main()
