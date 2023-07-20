#процессы - грубо говоря это копия программы, запущенная отдельно (повышает скорость выполнения)
#потоки - это "очередь" в одном процессе, условно-последовательное выполнение (жрёт меньше ресурсов, проще взаимодействие)
#тот поток, который захватил управление, будет выполняться, остальные - ждать. Зависнет один - зависнут все (win98)

import threading #из коробки!
import time

def first_thr():
    while True:
        print(f"{thr1.name}")
        time.sleep(1)

def second_thr():
    while True:
        print(f"{thr2.name}")
        time.sleep(5)

def get_data(data):
    while True:
        print(f"[{threading.currentThread().name}] - {data}")
        time.sleep(5)

thr1 = threading.Thread(target=first_thr, daemon=True)
thr2 = threading.Thread(target=second_thr, daemon=True)
#если daemon = False, то потоки будут выполняться даже после завершения программы
thr3 = threading.Thread(target=get_data, args=(str(time.time()),), name = "third_thr")
#запятая в конце args делает из str кортеж, без запятой это просто переменная

#система запускает основной поток (Main Thread) для выполнения основного кода
print(f"{threading.currentThread().name}")

#а потом мы можем запускать свои
#thr1.start()
#thr2.start()
thr3.start()

#из конструктора класса потока:
#def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):