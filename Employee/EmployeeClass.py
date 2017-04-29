
class Employee(object):
    def __init__(self, id, firstname, lastname, phone_number):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number

    def setId(self, new_id):
        self.id = new_id

    def getId(self):
        return self.id

    def setFirstname(self, new_firstname):
        self.firstName = new_firstname

    def getFirstname(self):
        return self.firstname

    def setLastname(self, new_lastname):
        self.lastname = new_lastname

    def getLastname(self):
        return self.lastname

    def setPhone(self, new_phone_number):
        self.phone_number = new_phone_number

    def getPhone(self):
        return self.phone_number

