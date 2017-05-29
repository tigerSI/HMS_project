from Database import ControllerDatabase
from Employee.EmployeeClass import Employee
import Setting as s


class AdminApplication(object):
    def __init__(self):
        self.ctrlDatabase = ControllerDatabase.ControllerDatabase(s.DB_USER)
        self.lst_admin = []
        self.lst_roommanager = []
        self.lst_doctor = []
        self.lst_nurse = []

    def getUserFromDatabase(self):
        obj_users = self.ctrlDatabase.loadObj()
        return obj_users

    def getListByPosition(self):
        print("in")
        self.lst_doctor.clear()
        self.lst_roommanager.clear()
        self.lst_nurse.clear()
        self.lst_admin.clear()
        users = self.getUserFromDatabase()
        for user in users:
            print(user)
            if user.getType() == s.Position.admin:
                self.lst_admin.append(user)
            elif user.getType() == s.Position.doctor:
                self.lst_doctor.append(user)
            elif user.getType() == s.Position.nurse:
                self.lst_nurse.append(user)
            elif user.getType() == s.Position.roommanager:
                self.lst_roommanager.append(user)
            else:
                print("Error")

    def getListAdmin(self):
        return self.lst_admin

    def getListDoctor(self):
        return self.lst_doctor

    def getListNurse(self):
        return self.lst_nurse

    def getListRoomManager(self):
        return self.lst_roommanager

    def editEmployee(self, id, data):
        users = self.getUserFromDatabase()
        for i in range(len(users)):
            if users[i].id == id:
                print("Edit")
                if not self.userNameValid(data[1]):
                    users[i] = Employee(data[0], data[1], data[2], data[3],
                                        data[4], data[5], data[6])
                    print(users)
                    self.ctrlDatabase.updateObject(users)
                    print("Update")
                return True
        return False

    def newEmployee(self, data):
        pass

    def userNameValid(self, userName):
        users = self.getUserFromDatabase()
        for user in users:
            if user.username == userName:
                return False
        return True


if __name__ == "__main__":
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    win = AdminApplication()
    win.checkRegisteredUser(1, 1)
    exit(app.exec_())
