import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class Login_UI(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.parent = parent

        loader = QUiLoader()
        form = loader.load('./login_widget.ui', self)

        self.user_id = form.findChild(QLineEdit, "lineEdit_username")
        self.password = form.findChild(QLineEdit, "lineEdit_password")

        self.login_button = form.findChild(QPushButton, "button_login")
        self.login_button.clicked.connect(self.logIn)

        self.signin_button = form.findChild(QPushButton, "button_signup")
        self.signin_button.clicked.connect(self.signUp)



    def logIn(self):
        self.parent.changePageLoginSection("login")

    def signUp(self):
        self.parent.changePageLoginSection("register")


