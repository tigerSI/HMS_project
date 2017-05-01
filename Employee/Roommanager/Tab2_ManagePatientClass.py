from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader


class Tab2ManagePatient(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()
        self.initLayout()
        self.initButton()
        self.initConnect()

    def initUI(self):
        self.tab2 = QUiLoader().load('./View/Tab2_ManagePatientUI.ui', self)

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tab1)

    def initButton(self):
        pass

    def initConnect(self):
        pass


if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication

    app = QApplication(sys.argv)
    tab2_widget = Tab2ManagePatient()
    tab2_widget.show()
    sys.exit(app.exec_())
