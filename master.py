from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def deviz():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Яндекс!</title>
                      </head>
                      <body>
                        <div class="alert alert-primary" role="alert">
                          <h1>Привет, Марс!</h1><br>
                        </div>
                        <img src="https://narisyu.cdnbro.com/posts/4780903-risunok-planety-mars-29.jpg" alt="mars"
                        height="400", width="700"><br>
                        <div class="alert alert-primary" role="alert">
                          Человечество вырастает из детства. <br>
                        
                          Человечеству мала одна планета.<br>
                        
                          Мы сделаем обитаемыми безжизненные пока планеты.<br>
                        
                          И начнем с Марса!<br>
                        
                          Присоединяйся!
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
