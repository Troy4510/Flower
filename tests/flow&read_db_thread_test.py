import threading
import time
from datetime import datetime
import sqlite3
from sqlite3 import Error
import pathlib
from pathlib import Path

dir_path = pathlib.Path.cwd()
conn_path = Path(dir_path.parent, 'sql', 'thr_tst_db.sqlite')

def write_cycle(path):
    while True:
        connection = None
        data = input("enter some data: ")
        try:
            c_dt = datetime.now()
            dt = c_dt.minute
            print(dt)
            insertData = f'''INSERT INTO timer_and_data (time,data)
                        VALUES ({dt}, {data})'''
            connection = sqlite3.connect(path)
            cursor = connection.cursor()
            cursor.execute(insertData)
            connection.commit()
            cursor.close()
            connection.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            pass
        time.sleep(1)

def read_cycle(path):
    connection = None
    while True:
        try:
            connection = sqlite3.connect(path)
            select_query = """SELECT * from timer_and_data ORDER BY id DESC LIMIT 1"""
            cursor = connection.cursor()
            cursor.execute(select_query)
            record = cursor.fetchone()
            print(f'\n{record}')
            cursor.close()
            connection.close()
        except sqlite3.Error as error:
            print(f'[error:] f{error}')
        finally:
            pass
        time.sleep(5)

def connection_to_db(path):
    try:
        connection = sqlite3.connect(path)
        print(f"[connection to SQLite DB] {path} [OK]")
    except Error as e:
        print(f'[connection error:] {e}')

#write_cycle(conn_path)
#read_cycle(conn_path)

thr1 = threading.Thread(target=write_cycle, args=(conn_path,), daemon=False)
thr2 = threading.Thread(target=read_cycle, args=(conn_path,), daemon=False)

thr1.start()
thr2.start()