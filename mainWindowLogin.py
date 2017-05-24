from PySide.QtGui import QMainWindow, QGridLayout, QWidget, QPalette, QBrush, QPixmap, QLineEdit, QPushButton
from PySide.QtUiTools import QUiLoader
from Base.Dialog_MsgBox import ConfirmMsgClass
import LoginSystem
import setting as s


class mainWindowLogin(QMainWindow):
    def __init__(self, position):
        super(mainWindowLogin, self).__init__()
        self.system = LoginSystem.LoginSystem()
        self.initUI()
        self.initLayout()
        self.show()
        self.position = position
        self.position.setChoice(3)

    def initUI(self):
        posX, posY, sizeW, sizeH = s.GEOMETRY_MAINWIDOW
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.setWindowTitle("Hospital Management System")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(s.PATH_IMG_BG_LOGIN)))
        self.setPalette(palette)
        self.initButton()

    def initButton(self):
        loader = QUiLoader()
        form = loader.load('RSC/loginUI/Widget_LoginUI.ui', self)
        self.user_id = form.findChild(QLineEdit, "lineEdit_username")
        self.password = form.findChild(QLineEdit, "lineEdit_password")
        self.login_button = form.findChild(QPushButton, "button_login")
        self.login_button.clicked.connect(self.logIn)

    def initLayout(self):
        layout = QGridLayout()
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def logIn(self):
        # user_name, psw = self.user_id.text(), self.password.text()
        # found, user, position = self.system.checkRegisteredUser(user_name, psw)
        # if not found:
        #     dialog = ConfirmMsgClass.ConfirmYesNo()
        #     dialog.show()
        #     dialog.exec_()
        #     self.clear()
        position = 3
        self.position.setChoice(position)
        self.close()

    def clear(self):
        self.user_id.clear()
        self.password.clear()

    def main(self):
        pass


if __name__ == "__main__":
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    win = mainWindowLogin()
    exit(app.exec_())
