from PySide.QtGui import QMainWindow, QGridLayout, QWidget, QPalette, QBrush, QPixmap, QLineEdit, QPushButton, \
    QErrorMessage
from PySide.QtUiTools import QUiLoader
from Base.Dialog_MsgBox import ConfirmMsgClass
import Setting as s
import Login_System


class LoginWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.system = Login_System.LoginSystem()
        self.initUI()
        self.show()

    def initUI(self):
        posX, posY, sizeW, sizeH = s.GEOMETRY_MAINWIDOW
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.setWindowTitle("Hospital Management System")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(s.PATH_IMG_BG_LOGIN)))
        self.setPalette(palette)
        self.initButton()
        self.forDev()

    def initButton(self):
        loader = QUiLoader()
        form = loader.load('RSC/loginUI/Widget_LoginUI.ui', self)
        self.user_id = form.findChild(QLineEdit, "lineEdit_username")
        self.password = form.findChild(QLineEdit, "lineEdit_password")
        self.login_button = form.findChild(QPushButton, "button_login")
        self.login_button.clicked.connect(self.logIn)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(s.PATH_IMG_BG_LOGIN)))
        self.setPalette(palette)

    def forDev(self):
        id = "Nur1"
        psw = "1234"
        self.user_id.setText(id)
        self.password.setText(psw)

    def initLayout(self):
        layout = QGridLayout()
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def logIn(self):
        user_name, psw = self.user_id.text(), self.password.text()
        found, user, position = self.system.checkRegisteredUser(user_name, psw)
        if not found:
            error = QErrorMessage()
            error.showMessage("wrong input")
            error.setWindowTitle("Error!!!")
            error.exec_()
        else:
            self.parent.loginSucess(user, position)
            self.close()

    def clear(self):
        self.user_id.clear()
        self.password.clear()


