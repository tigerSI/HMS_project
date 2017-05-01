import sys
import psycopg2
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
        lstHeadDoctor = ["Username", "Password", "ID", "Firstname", "Lastname", "Phone", "Position"]
        lstHeadNurse = ["Username", "Password", "ID", "Firstname", "Lastname", "Phone"]
        lstHeadRoom = ["Username", "Password", "ID", "Firstname", "Lastname", "Phone"]
        # allRowDatabaseDoctor = getDoctorDB()
        # allRowDatabaseNurse = getNurseDB()
        # allRowDatabaseRoom = getRoomDB()
        allRowDatabaseDoctor = []
        allRowDatabaseNurse = []
        allRowDatabaseRoom = []
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 35px; width: 100px; }")
        self.tab1 = Tab_ManageEmployeeClass.TabManageEmployee("Doctor")
        self.tab1.setSourceModel(lstHeadDoctor, allRowDatabaseDoctor)
        self.tab2 = Tab_ManageEmployeeClass.TabManageEmployee("Nurse")
        self.tab2.setSourceModel(lstHeadNurse, allRowDatabaseNurse)
        self.tab3 = Tab_ManageEmployeeClass.TabManageEmployee("Room manager")
        self.tab3.setSourceModel(lstHeadNurse, allRowDatabaseRoom)
        self.tabWidget.addTab(self.tab1, "Doctor")
        self.tabWidget.addTab(self.tab2, "Nurse")
        self.tabWidget.addTab(self.tab3, "RoomManager")


def getDoctorDB():
    lst = []
    sql_select = """SELECT users_username, users_password, doctor_id from users"""
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()
        while row is not None:
            if(row[2] != None):
                lst.append(row)
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

    sql_select = """SELECT * from doctor"""
    new_lst = []
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()
        count = 0
        while row is not None:
            for tup in lst:
                if(tup[2] == row[0]):
                    new_lst.append((lst[count][0], lst[count][1], row[0], row[1], row[2], row[3], row[4]))
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
    return new_lst

def getNurseDB():
    lst = []
    sql_select = """SELECT users_username, users_password, nurse_id from users"""
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()

        while row is not None:
            if (row[2] != None):
                lst.append(row)
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

    sql_select = """SELECT * from nurse"""
    new_lst = []
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()
        count = 0
        while row is not None:
            for tup in lst:
                if(tup[2] == row[0]):
                    new_lst.append((lst[count][0], lst[count][1], row[0], row[1], row[2], row[3]))
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
    return new_lst

def getRoomDB():
    lst = []
    sql_select = """SELECT users_username, users_password, roommanager_id from users"""
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()

        while row is not None:
            if (row[2] != None):
                lst.append(row)
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

    sql_select = """SELECT * from roommanager"""
    new_lst = []
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()
        count = 0
        while row is not None:
            for tup in lst:
                if(tup[2] == row[0]):
                    new_lst.append((lst[count][0], lst[count][1], row[0], row[1], row[2], row[3]))
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
    return new_lst


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    exit(app.exec_())


if __name__ == "__main__":
    main()
