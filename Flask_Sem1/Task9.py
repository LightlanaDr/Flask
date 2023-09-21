# Задание №9
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/catalog/')
def about():
    return render_template('catalog.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
