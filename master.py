from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def deviz():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Привет, Яндекс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1><br>
                        <img src="{url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка,
                         но не нашлась" height="400", width="700"><br>
                        <div class="alert alert-light" role="alert">
                          Человечество вырастает из детства. <br>
                        </div>
                        <div class="alert alert-success" role="alert">
                          Человечеству мала одна планета.<br>
                        </div>
                        <div class="alert alert-dark" role="alert">
                          Мы сделаем обитаемыми безжизненные пока планеты.<br>
                        </div>
                        <div class="alert alert-warning" role="alert">
                          И начнем с Марса!<br>
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Присоединяйся!
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
