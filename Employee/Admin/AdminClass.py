from Employee import EmployeeClass
import Setting as s

class Admin(EmployeeClass.Employee):
    def __init__(self, id, username, password, firstname, lastname, phone_number):
        EmployeeClass.Employee.__init__(self, id, username, password, s.Position.admin , firstname, lastname, phone_number)
