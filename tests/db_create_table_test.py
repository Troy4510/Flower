import sqlite3
from sqlite3 import Error
import pathlib
from pathlib import Path

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print(f"Соединение с {path} выполнено")
    except Error as e:
        print(f"Ошибка при подключении к sqlite '{e}'")

    return connection

def create_table(db_conn):
    try:
        sqlite_create_table_query = '''CREATE TABLE flower_statistics (
                                    id INTEGER PRIMARY KEY,
                                    year INTEGER,
                                    month INTEGER,
                                    day INTEGER,
                                    hour INTEGER,
                                    temp_sens INTEGER,
                                    hyd_sens INTEGER,
                                    light_relay TEXT, 
                                    other TEXT);'''

        cursor = db_conn.cursor()
        cursor.execute(sqlite_create_table_query)
        #Метод commit() используется для обеспечения согласованности изменений, внесенных в базу данных.
        #Поскольку по умолчанию Connector/Python не выполняет автоматическую фиксацию,
        #важно вызывать этот метод после каждой транзакции, которая изменяет данные для таблиц, использующих механизмы хранения транзакций.
        db_conn.commit()
        cursor.close()
        print("Таблица flower_statistics создана")
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (db_conn):
            db_conn.close()
            print("Соединение с SQLite закрыто")



dir_path = pathlib.Path.cwd()
need_path = Path(dir_path.parent, 'sql', 'tst_db.sqlite')

#как выяснилось - если бд не существует, она будет создана
conn1 = create_connection(need_path)
create_table(conn1)

