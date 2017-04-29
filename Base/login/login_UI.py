import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from Base.login import User_Application

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




    def logIn(self):
        users = User_Application.User_Application(self.user_id.text(), self.password.text()).user
        print(type(users))
        self.parent.changePageLoginSection("login", users)



