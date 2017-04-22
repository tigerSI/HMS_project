from Employee import EmployeeClass


class Roommanager(EmployeeClass):
    def __init__(self, department):
        super.__init__(self, id, "Roommanager", department)