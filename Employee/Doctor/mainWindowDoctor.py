from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
from Employee.Doctor import Tab1_CalendarClass, Tab2_PatientClass


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.loader = QUiLoader()
        self.tabWidget = QTabWidget()
        self.centralWidget = QWidget()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("Doctor window")
        self.setTab()
        grid = QGridLayout()
        grid.addWidget(self.tabWidget)
        self.centralWidget.setLayout(grid)
        self.setCentralWidget(self.centralWidget)
        self.show()

    def setTab(self):
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 35px; width: 100px; }")
        self.tab1 = Tab1_CalendarClass.Tab1Calendar()
        self.tab2 = Tab2_PatientClass.Tab2Patient()
        self.tabWidget.addTab(self.tab1, "Dashboard")
        self.tabWidget.addTab(self.tab2, "Patient")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    exit(app.exec_())
