from PySide.QtGui import *
from Base.Widget_ManagePerson import Widget_ManagePersonClass
from Employee.Doctor.GuiClass import Dialog_3ReportPatientClass, Dialog_NewPatientClass

class Tab2Patient(QWidget):
    def __init__(self, user):
        QWidget.__init__(self)
        self.user = user
        self.initUI()
        self.initLayout()
        self.initButton()
        self.initConnect()

    def initUI(self):
        self.tab2 = Widget_ManagePersonClass.WidgetManagePerson("Patient")
        allRow = [("Atichat", "001", "Brain", "0971249197"), ("Tiger", "002", "Chest", "0971249194")]
        #self.tab2.setSourceModel(Setting.HEAD_BAR_PATIENT, allRow)

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tab2)
        self.setLayout(layout)

    def initButton(self):
        self.b_view = self.tab2.b_edit
        self.b_newPatient = self.tab2.b_newPerson

    def initConnect(self):
        self.b_view.clicked.connect(self.viewPatient)
        self.b_newPatient.clicked.connect(self.newPatient)

    def viewPatient(self):
        dialog = Dialog_3ReportPatientClass.ReportPatient()
        dialog.show()
        dialog.exec_()

    def newPatient(self):
        dialog = Dialog_NewPatientClass.NewPatientDialog(self.user)
        dialog.show()
        dialog.exec_()



if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    tab2_widget = Tab2Patient()
    sys.exit(app.exec_())
