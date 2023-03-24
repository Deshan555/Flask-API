import sqlite3


# function for create database connection
def connection():
    conn = sqlite3.connect('database.db')
    return conn
