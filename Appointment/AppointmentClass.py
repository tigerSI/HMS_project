class Date:
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0

    def setDate(self, date):
        self.day = date[0]
        self.month = date[1]
        self.year = date[2]


class Appointment:
    # "Type", "Date", "Time"
    #self.part_appointment, self.user, newPatient
    def __init__(self, appointment, doctor, patient):
        self.type = ""
        self.date = Date()
        self.time = ""
        self.doctor = doctor
        self.patient = patient
        self.number_room = 0
        self.setInfo(appointment[0], appointment[1], appointment[2])

    def setInfo(self, type, date, time):
        self.type = type
        self.date.setDate(date.split('/'))
        self.time = time

    def setRoom(self, number):
        self.number_room = number


