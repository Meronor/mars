from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def deviz():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def add():
    return '''Человечество вырастает из детства. <br>

Человечеству мала одна планета.<br>

Мы сделаем обитаемыми безжизненные пока планеты.<br>

И начнем с Марса!<br>

Присоединяйся!'''


@app.route('/image_mars')
def image():
    return '''<h1>Привет, Марс!</h1><br>
    <img src="https://narisyu.cdnbro.com/posts/4780903-risunok-planety-mars-29.jpg" alt="mars"
    height="400", width="700"><br>
    Вот она какая, красная планета.'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
