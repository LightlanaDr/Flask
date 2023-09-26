# Задание №1
# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.

from markupsafe import escape

from pathlib import PurePath, Path
from typing import Dict

from flask import Flask, abort, redirect, url_for, flash,  session
from flask import render_template, request
from werkzeug.utils import secure_filename
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/next')
def next_page():
    return "Привет, Вася"


@app.route('/load_img', methods=['GET', 'POST'])
def load_img():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads',
                                    file_name))
        return f"Файл  {escape(file)} загружен на сервер"

    context: dict[str, str] = {
        "task": "Zadanie 2"
    }
    return render_template('page_1.html', **context)


@app.route('/authorization', methods=['GET', 'POST'])
def authorization():
    login = {
        'auth_email': '1@mail.ru',
        'auth_pass': '123'
    }
    if request.method == 'POST':
        auth_email = request.form.get('auth_email')
        auth_pass = request.form.get('auth_pass')
        if auth_email == login['auth_email'] and auth_pass == login['auth_pass']:
            return f"Вход с почты  {escape(auth_email)} выполнен успешно"
        else:
            return 'Ошибка'

    context: dict[str, str] = {
        "task": "Zadanie 3"
    }

    return render_template('authorization.html', **context)


@app.route('/counter', methods=['GET', 'POST'])
def counter():
    if request.method == 'POST':
        text = request.form.get('text')
        return f"Количество слов  {len(text.split())} "

    context: dict[str, str] = {
        "task": "Zadanie 4"
    }
    return render_template('counter.html', **context)


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        number_1 = request.form.get('number_1')
        number_2 = request.form.get('number_2')

        operation = request.form.get('operation')

        if operation == 'add':
            return f'{int(number_1) + int(number_2)}'
        elif operation == 'subtract':
            return f'{int(number_1) - int(number_2)}'
        elif operation == 'multiply':
            return f'{int(number_1) * int(number_2)}'
        else:
            return f'{int(number_1) / int(number_2)}'

    context: dict[str, str] = {
        "task": "Zadanie 5"
    }
    return render_template('calc.html', **context)


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Доступ запрещен по возрасту',
        'url': request.base_url,
    }
    return render_template('403.html', **context), 403


@app.route('/user', methods=['GET', 'POST'])
def user():
    MIN_AGE = 18

    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if MIN_AGE < int(age):
            return f"вы вошли"
        else:
            abort(403)

    context: dict[str, str] = {
        "task": "Zadanie 6"
    }

    return render_template('user.html', **context)


@app.route('/number_quad', methods=['GET', 'POST'])
def number_quad():
    NUMBER = 5
    return redirect(url_for('base', number=int(NUMBER ** 2)))


@app.route('/number_quad/<int:number>')
def numb_res(number: int):
    return str(number)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')

# Урок 2. Погружение во Flask
# Задание

# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
    
@app.get('/login_user')
def login_user():
    context = {
        'username': 'Авторизация'
    }
    return render_template('login.html', **context)


@app.post('/login_user')
def submit_post():
    session['username'] = request.form.get('username')
    session['auth_email'] = request.form.get('auth_email')
    return redirect(url_for('success'))


@app.route('/success/', methods=['GET', 'POST'])
def success():
    if 'username' in session:
        context = {
            'username': session['username'],
            'auth_email': session['auth_email'],
            'title': 'Добро пожаловать'
        }
        if request.method == 'POST':
            session.pop('username', None)
            session.pop('auth_email', None)
            return redirect(url_for('login_user'))
        return render_template('success.html', **context)
    else:
        return redirect(url_for('username'))





if __name__ == '__main__':
    app.run()
