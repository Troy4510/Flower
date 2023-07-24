from flask import Flask             #основа
from flask import request           #запросы
from flask import render_template   #шаблоны
import sql_handler as SQLH
import socket

local_name = socket.gethostname()
local_addr = socket.gethostbyname(local_name)
print(f"server: [{local_name}] on addr: [{local_addr}]")
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    dt = SQLH.struct_datetime()
    ts1 = f'Дата и время запроса: {dt}'
    svs1 = SQLH.read_hour(SQLH.base_path, dt.year, dt.month, dt.day, dt.hour)

    return render_template('index.html', time_string = ts1, single_value_string = svs1)

@app.route('/stat.html')
def stat():
    return render_template('stat.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/direct_control.html')
def direct_control():
    return render_template('direct_control.html')

@app.route('/schedule.html')
def schedule():
    return render_template('schedule.html')

def run_page():
    #if __name__ == '__main__':
    app.run(host=str(local_addr), port=5000, debug=True)