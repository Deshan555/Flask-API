import mysql.connector

import Config


def sensor_Box1():
    sql_connection = mysql.connector.connect(host=Config.HOST_NAME, user=Config.USER_NAME, password=Config.PASSWORD,
                                             database=Config.DATABASE_NAME)

    connection = sql_connection.cursor()

    SQL = "SELECT Record_Date, Record_Time, Temperature, Humidity, Heat_Index, Gas_Value from real_time_box_1;"

    connection.execute(SQL)

    result = connection.fetchall()

    for x in result:
        Temp = x[0]
        values = {
            'Record Date': x[0],
            'Record Time': x[1],
            'Temperature': x[2],
            'Humidity': x[3],
            'Heat Index': x[4],
            'Gas Value': x[5]
        }

    sql_connection.close()

    return values;


