import mysql.connector

import Config


def waterLvl(date):
    sql_connection = mysql.connector.connect(host=Config.HOST_NAME, user=Config.USER_NAME, password=Config.PASSWORD,
                                             database=Config.DATABASE_NAME)

    connection = sql_connection.cursor()

    SQL = "SELECT Record_Time, Water_Level FROM sensor_box_02 WHERE Record_Date = '" + date + "' LIMIT 10;"

    connection.execute(SQL)

    result = connection.fetchall()

    data_dict: dict = {}

    for x in result:
        data_dict[x[0]] = x[1]

    sql_connection.close()

    return data_dict



