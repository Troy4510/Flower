#from datetime import datetime
#from datetime import date
#from datetime import time
import datetime
import sqlite3
from sqlite3 import Error
import pathlib
from pathlib import Path

current_data = datetime.datetime.today()
print('current launch data: ', current_data)
base_name = 'tst_db.sqlite'

dir_path = pathlib.Path.cwd()
print('dir_path: ', dir_path)
base_path = Path(dir_path.parent, 'sql', base_name)
print('base_path: ', base_path)

def struct_datetime():
    dt = datetime.datetime.today()
    return dt

def read_day(path, year, month, day):
    connection = None
    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        print(f"Connection with {path} successable")
        sqlite_select_query = f"""select * from flower_statistics where 
                                year = {year} month = {month} and day = {day}"""
        cursor.execute(sqlite_select_query)
        print("read multiple data \n")
        records = cursor.fetchall()
        for record in records:
            print(record)
        cursor.close()
    except Error as e:
        print(f"Error connect to sqlite '{e}'")
    finally:
        if (connection):
            connection.close()
            print("Connection with SQLite closed")
    return records

def read_hour(path, year, month, day, hour):
    connection = None
    record = None
    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        print(f"Connection with {path} successable")
        sqlite_select_query = f"""select * from flower_statistics where 
                                    year = {year} and month = {month} and day = {day} and hour = {hour}"""
        cursor.execute(sqlite_select_query)
        print("read hour data \n")
        record = cursor.fetchone()
        cursor.close()
    except Error as e:
        print(f"Error connect to sqlite '{e}'")
    finally:
        if (connection):
            connection.close()
            print("Connection with SQLite closed")
    return record

#if __name__ == "__main__":
    #read_from_db(base_path, 4, 21)