from PySide.QtCore import QEvent, Qt
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader

from Base.Dialog_MsgBox import ConfirmMsgClass
from Patient import PatientClass
from Appointment import AppointmentClass
import Setting as s


class NewPatientDialog(QDialog):
    def __init__(self, user, parent=None):
        super(NewPatientDialog, self).__init__(parent)
        posX, posY, sizeW, sizeH = s.GEOMETRY_DIALOG_NEW_PATIENT
        self.setGeometry(posX + 400, posY, sizeW, sizeH + 400)
        self.user = user
        self.initUI()
        self.initLayout()
        self.initButton()
        self.initConnect()
        self.setDateEdit()
        self.part_basic_info = []
        self.part_appointment = []
        self.part_extra_info = []
        self.forDev()

    def initUI(self):
        path = s.PATH_DOCTOR_DIALOG_NEWPATIENT
        #path = '../View/Widget_NewPatientUI.ui'
        self.ui = QUiLoader().load(path, self)
        self.dateEdit = self.ui.findChild(QDateEdit, "Date")
        self.b_save = self.ui.findChild(QPushButton, "button_save")
        self.b_cancel = self.ui.findChild(QPushButton, "button_cancel")


    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

    def initButton(self):
        self.b_save.clicked.connect(self.save)
        self.b_cancel.clicked.connect(self.cancel)

    def initConnect(self):
        pass

    def setDateEdit(self):
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarWidget().installEventFilter(self)
        self.dateEdit.calendarWidget().setFirstDayOfWeek(Qt.Monday)

    def eventFilter(self, obj, event):
        if obj == self.dateEdit.calendarWidget() and event.type() == QEvent.Show:
            pos = self.dateEdit.mapToGlobal(self.dateEdit.geometry().bottomRight())
            self.dateEdit.calendarWidget().window().move(pos.x(), pos.y())
        return False

    def forDev(self):
        count = "1"
        ui = self.ui
        ui.AN.setText("000 " + count)
        ui.PIC.setText("PIC " + count)
        ui.Name.setText("Atichat " + count)
        ui.Age.setText("20 " + count)
        ui.Phone.setText("0971249197 " + count)
        ui.Pre_OD.document().setPlainText("Pre_OD " + count)
        ui.Plan.document().setPlainText("Plan " + count)
        ui.Underlying.document().setPlainText("Underlying " + count)
        ui.Treatment.document().setPlainText("Treatment " + count)
        ui.Note.document().setPlainText("Note " + count)

    def getData(self):
        ui = self.ui
        #["OPD", "AN", "Pic", "Name", "Age", "Phone"]
        self.part_basic_info.append(ui.OPD.currentText())
        self.part_basic_info.append(ui.AN.text())
        self.part_basic_info.append(ui.PIC.text())
        self.part_basic_info.append(ui.Name.text())
        self.part_basic_info.append(ui.Age.text())
        self.part_basic_info.append(ui.Phone.text())
        #"Type", "Date", "Time"
        self.part_appointment.append(ui.Type.currentText())
        self.part_appointment.append(ui.Date.text())
        self.part_appointment.append(ui.Time.currentText())
        #"Pre_OD", "Plan", "Underlying", "Treatment", "Note"
        self.part_extra_info.append(ui.Pre_OD.toPlainText())
        self.part_extra_info.append(ui.Plan.toPlainText())
        self.part_extra_info.append(ui.Underlying.toPlainText())
        self.part_extra_info.append(ui.Treatment.toPlainText())
        self.part_extra_info.append(ui.Note.toPlainText())

    def save(self):
        self.getData()
        pre_pre_report = [self.part_basic_info, self.part_extra_info]
        newPatient = PatientClass.Patient(pre_pre_report)
        newAppointment = AppointmentClass.Appointment(self.part_appointment, self.user, newPatient)
        print(newPatient)
        print(newAppointment)
        self.close()

    def cancel(self):
        dialog = ConfirmMsgClass.ConfirmYesNo()
        if dialog.ans == True:
            print("Discard")
            self.close()
        else:
            print("Cancel")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = NewPatientDialog()
    win.show()
    win.exec_()
