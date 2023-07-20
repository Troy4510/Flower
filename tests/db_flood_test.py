import random
from datetime import datetime
from datetime import date
from datetime import time
import sqlite3
from sqlite3 import Error
import pathlib
from pathlib import Path


def write_to_db(path, insertData):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print(f"Соединение с {path} выполнено")
        cursor = connection.cursor()
        cursor.execute(insertData)
        connection.commit()
        #Метод connect.commit() фиксирует (подтверждает?) текущую транзакцию.
        #Если не вызывать этот метод, то все, что сделано после последнего вызова connect.commit(),
        #не будет видно из других соединений с базой данных.
        print(insertData)
        print("Запись успешно вставлена в таблицу flower_statistics ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Не удалось вставить данные в таблицу sqlite")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (connection):
            connection.close()
            print("Соединение с SQLite закрыто")


#sqlite_insert_query = '''INSERT INTO flower_statistics
#                                (id, year, month, day, hour, temp_sens, hyd_sens, light_relay)
#                                VALUES (1, '2023', 01, 15, 5, 25, 50, 'off')'''

dir_path = pathlib.Path.cwd()
need_path = Path(dir_path.parent, 'sql', 'tst_db.sqlite')
#write_to_db(need_path)
dt = datetime(2023,3,1,0)
print(dt)

for day1 in range (1, 30):
    for hour1 in range (0, 24):
        tmp1 = random.randrange(30)
        hyd1 = random.randrange(100)
        light1 = random.choice(['on', 'off'])

        ins_query = f'''INSERT INTO flower_statistics
                        (year, month, day, hour, temp_sens, hyd_sens, light_relay, other)
                        VALUES (2023, 5, {day1}, {hour1}, {tmp1}, {hyd1}, '{light1}', 'tst')'''
        write_to_db(need_path, ins_query)
