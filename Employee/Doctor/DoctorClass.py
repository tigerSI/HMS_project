from Employee import EmployeeClass


class Doctor(EmployeeClass):
    def __init__(self, id, department):
        EmployeeClass.__init__(self, id, "Doctor", department)

    
