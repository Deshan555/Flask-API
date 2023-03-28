import mysql.connector

import Config


def sensor_Box2():
    sql_connection = mysql.connector.connect(host=Config.HOST_NAME, user=Config.USER_NAME, password=Config.PASSWORD,
                                             database=Config.DATABASE_NAME)

    connection = sql_connection.cursor()

    SQL = "SELECT Record_Date, Record_Time, Water_Level, Soil_Moisture from real_time_box_2;"

    connection.execute(SQL)

    result = connection.fetchall()

    for x in result:
        values = {
            'Record Date': x[0],
            'Record Time': x[1],
            'Water Leval': x[2],
            'Soil Moisture': x[3]
        }

    sql_connection.close()

    return values;

