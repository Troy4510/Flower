import sqlite3
from sqlite3 import Error
import pathlib
from pathlib import Path



def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print(f"Connection to SQLite DB {path} successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

dir_path = pathlib.Path.cwd()
need_path = Path(dir_path.parent, 'sql', 'tst_db2.sqlite')

#как выяснилось - если бд не существует, она будет создана
conn1 = create_connection(need_path)