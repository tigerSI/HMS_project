from Employee.Admin import mainWindowAdmin as Admin
from Employee.Doctor import mainWindowDoctor as Doctor
from Employee.Roommanager import mainWindowRoomManager as RoomManager
from Employee.Nurse import mainWindowNurse as Nurse
import mainWindowLogin, setting, sys, ReturnValueClass

def main():
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    position = ReturnValueClass.Choice()
    windowLogin = mainWindowLogin.mainWindowLogin(position).main()
    choice = position.getChoice()
    if choice == setting.Position.admin.value:
       mainWindow = Admin.MainWindowAdmin()
    elif choice == setting.Position.doctor.value:
        mainWindow = Doctor.MainWindowDoctor()
    elif choice == setting.Position.nurse.value:
        mainWindow = Nurse.MainWindowNurse()
    elif choice == setting.Position.roomManager.value:
        print("in")
        mainWindow = mainWindowLogin.mainWindowLogin(position)
    else:
        print("Error")
    exit(app.exec_())

main()
