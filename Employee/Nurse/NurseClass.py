from Employee.Roommaneger import EmployeeClass


class Nurse(EmployeeClass):
    def __init__(self, id,department):
        EmployeeClass.__init__(self, id, "Nurse", department)