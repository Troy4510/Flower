from flask import Flask             #основа
from flask import request           #запросы
from flask import render_template   #шаблоны

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/stat')
def hello2():
    return render_template('stat.html')

'''
#http://.../request?month=3&day=20 означает, что после "?" идет запрос с параметрами month=3&day=20
По умолчанию, свойство request.args, представляет собой объект словаря, доступ к значениям параметров осуществляется по ключу request.args['day']
Для безопасного извлечения ключей из словаря, что бы избежать исключений (при отсутствии ключа), можно воспользоваться методом dict.get().
'''

@app.route('/req', methods=['GET'])
def req():
    error = None
    month1 = request.args.get('month', type=int)
    #проверяем, передается ли 'month' в запросе
    if month1 and month1 !=None: #если month1 cуществует и это не пустая строка
        day1 = request.args.get('day', default=29, type=int)
        return f"month={month1}, day={day1}"
    else:
        #если month не существует или это пустая строка, отображаем страницу stat с ошибкой
        error = 'не введен запрос, например ".../req?month=3&day=20"'
        return error

@app.route('/test1')
def test1():
    return render_template('test1.html', somedata = 'ТЕКСТ ИЗ PYTHON-ОБРАБОТЧИКА')

#app.run(host='192.168.0.13', port=5000, debug=True)
app.run(host='127.0.0.1', port=5000, debug=True)