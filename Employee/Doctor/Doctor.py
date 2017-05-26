from Database import ControllerDatabase
from Appointment import AppointmentClass
import Setting as s


class DoctorApplication(object):
    def __init__(self):
        self.ctrlDatabase_patient = ControllerDatabase.ControllerDatabase(s.DB_PATIENT)
        self.ctrlDatabase_appointment = ControllerDatabase.ControllerDatabase(s.DB_APPOINTMENT)

    def getPatientFromDatabase(self):
        obj_patients = self.ctrlDatabase_patient.loadObj()
        return obj_patients

    def getAppointmentFromDatabase(self):
        obj_appointments = self.ctrlDatabase_appointment.loadObj()
        return obj_appointments

    def addNewPatient(self, newPatient):
        patients = self.getPatientFromDatabase()
        patients.append(newPatient)
        self.ctrlDatabase_patient.updateObject(patients)

    def editPatient(self, newPatient):
        patients = self.getPatientFromDatabase()
        for i in range(len(patients)):
            if patients[i].AN == newPatient.AN:
                patients[i] = newPatient
                break
        self.ctrlDatabase_patient.updateObject(patients)





if __name__ == "__main__":
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    win = DoctorApplication()
    exit(app.exec_())
