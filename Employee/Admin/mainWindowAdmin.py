import sys
from PySide.QtGui import *
from Employee.Admin import Tab_ManageEmployeeClass


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tabWidget = QTabWidget()
        self.centralWidget = QWidget()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("ADMIN main window")
        self.setTab()
        grid = QGridLayout()
        grid.addWidget(self.tabWidget)
        self.centralWidget.setLayout(grid)
        self.setCentralWidget(self.centralWidget)
        self.show()

    def setTab(self):
        lstHeadDoctor = ["NAME", "ID", "Position", "Phone"]
        lstHeadNurse = ["NAME", "ID", "Phone"]
        allRowDatabaseDoctor = [("Atichat","001", "Brain", "0971249197"), ("Tiger","002","Chest", "0971249194")]
        allRowDatabaseNurse = [("Nuttera", "0001", "0978488151"), ("Aafsdfn", "05184", "518454")]
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 35px; width: 100px; }")
        self.tab1 = Tab_ManageEmployeeClass.TabManageEmployee()
        self.tab1.setSourceModel(lstHeadDoctor, allRowDatabaseDoctor)
        self.tab2 = Tab_ManageEmployeeClass.TabManageEmployee()
        self.tab2.setSourceModel(lstHeadNurse, allRowDatabaseNurse)
        self.tabWidget.addTab(self.tab1, "Doctor")
        self.tabWidget.addTab(self.tab2, "Nurse")




def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    exit(app.exec_())

if __name__ == "__main__":
    main()
