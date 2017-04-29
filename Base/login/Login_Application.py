import sys
"""dsahfjdskfsjfsdkfdslfk"""
from PySide.QtGui import *

from login import signup_UI
from login import login_UI
from Roommaneger import mainWindowRoommaneger

class Login_Application(QMainWindow):
    def __init__(self):
        #Main UI set up
        QMainWindow.__init__(self, None)
        self.setMinimumSize(1280, 720)
        self.setWindowTitle("HMS version 1.0.1")

        # Init main Widget

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        login_widget = login_UI.Login_UI(self)
        self.central_widget.addWidget(login_widget)

        # Init state attributes
        self.state = 'Not Login'

        # Add widget
        self.login_widget = login_UI.Login_UI(self)
        self.register_widget = signup_UI.Signup_UI(self)
        self.roommaneger_widget = mainWindowRoommaneger.MainWindow()
        self.central_widget.addWidget(self.login_widget)
        self.central_widget.addWidget(self.register_widget)
        ##self.central_widget.addWidget(self.roommaneger_widget)


    # Change page signal (send from log in UI page)
    def changePageLoginSection(self, signal = None):
        if signal == "login":
            print('login pressed')
            self.state = "Login"
            ##self.centralWidget().setCurrentWidget(self.roommaneger_widget)


        elif signal == "register":
            self.centralWidget().setCurrentWidget(self.register_widget)


    # Change Page signal (send from register UI page)
    def changePageRegisterSection(self, signal = None):
        if signal == "submit":
            self.centralWidget().setCurrentWidget(self.register_widget)
            self.state = 'Register Already'
            print('submit')

        elif signal == "back":
            self.centralWidget().setCurrentWidget(self.login_widget)

def main():
    app = QApplication(sys.argv)
    ui = Login_Application()
    ui.show()
    app.exec_()

if __name__ == "__main__":
    main()