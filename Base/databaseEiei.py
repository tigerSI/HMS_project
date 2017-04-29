import psycopg2
import sys
"""dsahfjdskfsjfsdkfdslfk"""

def main():
    # Define our connection string
    sql_insert = """INSERT INTO patient(AN, firstname, surname, age, phone_number)
                 VALUES(%s, %s, %s, %s, %s);"""

    sql_select = """SELECT AN, firstname, surname, age, phone_number from patient"""

    sql_update = """UPDATE patient
                    SET firstname = %s, surname = %s, phone_number = %s
                    WHERE AN = %s
                    """

    sql_delete = """DELETE FROM patient WHERE AN = %s """
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        print("Connecting to database\n	->%s", (conn_string))
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        # Insert
        '''
        cursor.execute(sql_insert, ('1234', 'sirapop', 'issariyodom', 20, '0971591691'))
        conn.commit()
        print('Insert!!')
        '''

        # Select
        '''
        cursor.execute(sql_select)
        print('The number of rows: ', cursor.rowcount)
        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone() ##fetchont() return next row of query in type of single tuple or None
        '''
        # update
        '''
        cursor.execute(sql_update, ('tiger', 'tg', '12345678', '1234'))
        conn.commit()
        '''

        #delete
        '''
        cursor.execute(sql_delete, ('1234',))
        conn.commit()
        '''
        cursor.close()
        print("Finished!!")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        conn.close()

if __name__ == "__main__":
    main()