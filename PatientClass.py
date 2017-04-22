import AppointmentClass


class Patient:
    def __init__(self, AN):
        """Pre-Pre Anesthesia"""
        self.AN = AN
        self.firstName = ""
        self.lastName = ""
        self.age = 0
        self.phoneNumber = ""
        self.pic = object
        self.preInfo = PreInformationPatient

    def setName(self, f, l):
        self.firstName = f
        self.lastName = l

    def getName(self):
        return self.firstName, self.lastName

    def setAgePhone(self, a, num):
        self.age = a
        self.phoneNumber = num

    def getAge(self):
        return self.age

    def getPhoneNumber(self):
        return self.phoneNumber


class PreInformationPatient:
    def __init__(self, type):
        self.opd = 0
        self.type = type
        self.appointment = AppointmentClass
        self.preDiagonsis = ""

    def setPreDiagonsis(self, text):
        self.preDiagonsis = text

    def getPreDiagonsis(self):
        return self.preDiagonsis



