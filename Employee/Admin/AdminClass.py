from Employee import EmployeeClass


class Admin(EmployeeClass.Employee):
    def __init__(self, id, firstname, lastname, phone_number):
        EmployeeClass.Employee.__init__(self, id, firstname, lastname, phone_number)
