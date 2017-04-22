import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        loader = QUiLoader()
        ui = loader.load('./login.ui', self)
        self.setCentralWidget(ui)
        self.ip_username = ui.findChild(QLineEdit, "ip_username")
        self.ip_password = ui.findChild(QLineEdit, "ip_password")
        self.b_login = ui.findChild(QPushButton, "b_login")


def main():
    app = QApplication(sys.argv)
    w = Login()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())