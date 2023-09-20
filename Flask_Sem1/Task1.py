# Задание №1
# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!"
from datetime import datetime

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# Задание №2
# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
# ○ страницу "contact"

@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'

# Задание №3
# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.
@app.route('/<int:num_1>/<int:num_2>')
def sum_nums(num_1: int, num_2: int):
    return str(num_1 + num_2)


# Задание №4
# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.

@app.route('/string/<string:name>')
def count_len_text(name: str):
    return str(len(name))

# Задание №5
# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".

@app.route('/world')
def world():
    return render_template('index.html')

# Задание №6
# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.

@app.route('/students/')
def students():
    head = {
        'name': 'Имя',
        'lastname': 'Фамилия',
        'age': 'Возраст',
        'rating': 'Средний балл'
    }

    students_list = [
        {'name': 'Иван',
        'lastname': 'Немов',
        'age': 16,
        'rating': 4.0
         },
        {'name': 'Олег',
        'lastname': 'Иванов',
        'age': 20,
        'rating': 5.0
         },
        {'name': 'Семён',
        'lastname': 'Дружков',
        'age': 25,
        'rating': 4.7
         }]

    return render_template('index.html', **head, students_list=students_list)

# Задание №7
# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

@app.route('/news/')
def news():
    news_block = [
        {'title': 'News1',
        'description': 'Описание',
        'data': datetime.now().strftime('%H:%M - %m.%d.%Y года')
        },
        {'title': 'News1',
        'description': 'Описание',
        'data': datetime.now().strftime('%H:%M - %m.%d.%Y года')
         },
        {'title': 'News1',
        'description': 'Описание',
        'data': datetime.now().strftime('%H:%M - %m.%d.%Y года')
         }]

    return render_template('news.html', news_block=news_block)


# Задание №8
# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.

if __name__ == '__main__':
    app.run(debug=True)
