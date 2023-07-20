import sqlite3
from sqlite3 import Error
import pathlib
from pathlib import Path

def read_from_db(path, rec_number):
    connection = None
    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        print(f"Соединение с {path} выполнено")
        sqlite_select_query = """SELECT * from flower_statistics where id = ?"""
        cursor.execute(sqlite_select_query, (rec_number,))
        #cursor.execute(sqlite_select_query, rec_number)
        print("Чтение одной строки \n")
        record = cursor.fetchone()
        print(record)
        print("ID:", record[0])
        print("Время:", record[1])
        print("Температура:", record[2])
        print("Влажность", record[3])
        print("Освещение:", record[4])
        cursor.close()
    except Error as e:
        print(f"Ошибка при подключении к sqlite '{e}'")
    finally:
        if (connection):
            connection.close()
            print("Соединение с SQLite закрыто")

dir_path = pathlib.Path.cwd()
print('переменная dir_path:', dir_path)
need_path = Path(dir_path.parent, 'sql', 'tst_db.sqlite')
print('переменная need_path: ', need_path)

read_from_db(need_path, 2)