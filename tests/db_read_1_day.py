import sqlite3
from sqlite3 import Error
import pathlib
from pathlib import Path

def read_from_db(path, month, day):
    connection = None
    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        print(f"Соединение с {path} выполнено \n")
        sqlite_select_query = f"""SELECT * from flower_statistics WHERE day = {day}"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print(f'Данные за {day}:{month}')
        print('c:\tt:\th:\tr:')

        for record in records:
            print(f'{record[4]}\t{record[5]}\t{record[6]}\t{record[7]}')
        cursor.close()
    except Error as e:
        print(f"Ошибка при подключении к sqlite '{e}'")
    finally:
        if (connection):
            connection.close()
            print("\nСоединение с SQLite закрыто")

dir_path = pathlib.Path.cwd()
need_path = Path(dir_path.parent, 'sql', 'tst_db.sqlite')
month = 3
day = 29

read_from_db(need_path, month, day)