import psycopg2
import sys

def main():
    # Define our connection string
    conn_string = "host='161.246.94.219' dbname='postgres' user='postgres' password='4141'"

    # print the connection string we will use to connect
    print("Connecting to database\n	->%s", (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("INSERT into Patient(AN, firstname, surname, age, phone_number) values(%s, %s, %s, %i, %s)", ['tg', 'sirapop', 'tiger', 20,'123465789'])

    print("Connected!\n")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()