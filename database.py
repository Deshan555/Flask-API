import sqlite3


# function for create database connection
def connection():
    conn = sqlite3.connect('database.db')
    return conn


# function for create new sqlite database
def create_Table():
    try:
        conn = connection()
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (Task_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Task_INFO TEXT NOT NULL,
        Task_Date TEXT NOT NULL,
        Status TEXT NOT NULL);''')
        conn.commit()
        print('----------------------------------------------------------------')
    except:
        print("Error in creating table")
    finally:
        conn.close()


create_Table()

