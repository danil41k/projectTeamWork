from flask import Flask, render_template

app = Flask(__name__)

# Маршрут для Головної сторінки (Рівень 1)
@app.route('/')
def index():
    return render_template('index.html', title='Головна')

# Маршрут для сторінки "Про нас" (Рівень 1)
@app.route('/about')
def about():
    return render_template('about.html', title='Про нас')

# Маршрут для сторінки "Каталог" (Рівень 2)
@app.route('/catalog')
def catalog():
    return render_template('catalog.html', title='Каталог')

# Маршрут для сторінки "Доставка" (Рівень 2)
@app.route('/delivery')
def delivery():
    return render_template('delivery.html', title='Доставка')

if __name__ == '__main__':
    app.run(debug=True)
