from Patient import PreReportPatient, IntraReportPatient, PostReportPatient

class Patient:
    def __init__(self, AN):
        """Pre-Pre Anesthesia"""
        self.AN = AN
        self.firstName = ""
        self.lastName = ""
        self.age = 0
        self.phoneNumber = ""
        self.pic = object
        self.preReportDoctor = Patient.PreReportByDoctor
        self.preReportNurse = Patient.PreReportByNurse
        self.intraReport = Patient.InraReportPatient
        self.postReport = []

    def setName(self, f, l):
        self.firstName, self.lastName = f, l

    def getName(self):
        return self.firstName, self.lastName

    def setAgePhone(self, a, num):
        self.age, self.phoneNumber = a, num

    def getAge(self):
        return self.age

    def getPhoneNumber(self):
        return self.phoneNumber

    def editPreReportDoctor(self, preDoc):
        self.preReportDoctor = preDoc

    def editPreReportNurse(self, preNurse):
        self.preReportNurse = preNurse

    def editIntraReport(self, intra):
        self.intraReport = intra

    def addPostReport(self, post):
        self.postReport.append(post)
