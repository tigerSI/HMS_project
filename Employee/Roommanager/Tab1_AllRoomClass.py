from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader


class Tab1AllRoom(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()
        self.initLayout()
        self.initButton()
        self.initConnect()

    def initUI(self):
        self.tab1 = QUiLoader().load('./View/Tab1_AllRoomUI.ui', self)

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
    tab1_widget = Tab1AllRoom()
    tab1_widget.show()
    sys.exit(app.exec_())
