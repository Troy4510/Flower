import pathlib
from pathlib import Path

'''
cwd() — возвращает путь к рабочей директории
home() — возвращает путь к домашней директории
'''

# Получаем строку, содержащую путь к рабочей директории:
dir_path = pathlib.Path.cwd()

#это может быть полезно для linux
home_path = pathlib.Path.home()

# Объединяем полученную строку с недостающими частями пути
full_path = Path(dir_path, 'files', 'info', 'docs.txt')

#можно в одну строку
#path = Path(pathlib.Path.cwd(), 'files', 'info', 'docs.txt')

#если папка "выше"
#tst_path = (str(dir_path) - 'tests')
tst_path = dir_path.parent

#пробуем "вверх" и переход в другую директорию
need_path = Path(dir_path.parent, 'sql')

# выведем значение переменной path:
print('текущая директория: ' + str(dir_path))
print('домашняя директория: ' + str(home_path))
print('возможная конструкция: ' + str(full_path))
print('тестовая конструкция вверх: ' + str(tst_path))
print('вверх и в другую: ' + str(need_path))

