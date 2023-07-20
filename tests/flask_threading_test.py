import threading
import time
from flask import Flask

app = Flask(__name__)

def run_flask():
    print("Запуск FLASK")
    app.run()

# Запуск Flask в отдельном потоке
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Продолжение выполнения программы в основном потоке
time.sleep(10)
print("FLASK Запущен")

# Остановка Flask
flask_thread.join()
print("FLASK остановлен")