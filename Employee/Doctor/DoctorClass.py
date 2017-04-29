from Employee.Roommaneger import EmployeeClass


class Doctor(EmployeeClass.Employee):
    def __init__(self, id, firstname, lastname, phone_number, department):
        EmployeeClass.Employee.__init__(self,  id, firstname, lastname, phone_number)
        self.department = department

    def setDepartment(self, new_department):
        self.department = new_department

    def getDepartment(self):
        return self.department
    
