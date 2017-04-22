class Employee:
    def __init__(self, id, position, department):
        self.id = id
        self.firstName = ""
        self.lastName = ""
        self.phone = ""
        self.position = position
        self.department = department

    def setName(self, f, l):
        self.firstName, self.lastName = f, l

    def setPhone(self, num):
        self.phone = num

