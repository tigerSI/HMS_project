import psycopg2
from Employee import EmployeeClass
from Employee.Admin import AdminClass
from Employee.Doctor import DoctorClass
from Employee.Nurse import NurseClass
from Employee.Roommanager import RoommanagerClass

class User_Application():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.employee = ''
        self.id = ''
        self.check_login = False
        self.user = object

        self.check_Input()

    def check_Input(self):
        sql_select = """SELECT users_username, users_password, admin_id, doctor_id, nurse_id, roommanager_id   from users"""
        try:
            conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            cursor.execute(sql_select, )
            row = cursor.fetchone()

            while row is not None:
                if(self.username == row[0] and self.password == row[1]):
                    self.check_login = True
                    type_employee = ['admin', 'doctor', 'nurse', 'roommanager']
                    for i in range(4):
                        if(row[i + 2] != None):
                            self.id = row[i + 2]
                            self.employee = type_employee[i]
                            break
                row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
            cursor.close()

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()
        self.create_users()

    def create_users(self):
        if (self.check_login != True):
            self.user = None
            return 0

        if (self.employee == 'admin'):
            sql_select = """SELECT admin_id, admin_firstname, admin_lastname, admin_phone_number from admin
                            WHERE admin_id = %s"""

        elif(self.employee == 'doctor'):
            sql_select = """SELECT doctor_id, doctor_firstname, doctor_lastname, doctor_phone_number, doctor_department from doctor
                            WHERE doctor_id = %s"""

        elif(self.employee == 'nurse'):
            sql_select = """SELECT nurse_id, nurse_firstname, nurse_lastname, nurse_phone_number from nurse
                            WHERE nurse_id = %s"""

        elif(self.employee == 'roommanager'):
            sql_select = """SELECT Roommanager_id, Roommanager_firstname, Roommanager_lastname, Roommanager_phone_number from roommanager
                            WHERE Roommanager_id = %s"""
        else:
            sql_select = """"""

        try:
            conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            cursor.execute(sql_select, (self.id,))
            row = cursor.fetchone()
            cursor.close()

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()

        if (self.employee == 'admin'):
            self.user = AdminClass.Admin(row[0], row[1], row[2], row[3])

        elif(self.employee == 'doctor'):
            self.user = DoctorClass.Doctor(row[0], row[1], row[2], row[3], row[4])

        elif(self.employee == 'nurse'):
            self.user = NurseClass.Nurse(row[0], row[1], row[2], row[3])

        elif (self.employee == 'roommanager'):
            self.user = RoommanagerClass.RoomManager(row[0], row[1], row[2], row[3])


