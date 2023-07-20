from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<big><big><big><big><big><big><big>ТЕСТОВАЯ<big><big><big><big><big><big><big>'

@app.route('/xomka')
def hello2():
    return 'ХОМЯКИ НАПАЛИ!!! РАЗБЕГАЙСЯ!!! <p>Моя кошка <strong>очень</strong> раздражена.</p>'

@app.route('/stat')


app.run(host='192.168.0.13', port=5000, debug=True)
#app.run(host='127.0.0.1', port=5000, debug=True)