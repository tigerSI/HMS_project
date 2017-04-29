import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class Signup_UI(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self)
        self.parent = parent

        loader = QUiLoader()
        form = loader.load('./signup_widget.ui', self)

        self.firstname = form.findChild(QLineEdit, "lineEdit_firstname")
        self.surname = form.findChild(QLineEdit, "lineEdit_surname")
        self.birthday = form.findChild(QLineEdit, "lineEdit_birthday")
        self.job = form.findChild(QLineEdit, "lineEdit_job")


        self.submit_button = form.findChild(QPushButton, "submit_button")
        self.submit_button.clicked.connect(self.submit)

        self.back_button = form.findChild(QPushButton, "back_button")
        self.back_button.clicked.connect(self.back)

    def submit(self):
        self.parent.changePageRegisterSection("submit")

    def back(self):
        self.parent.changePageRegisterSection("back")

