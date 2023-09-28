# Задание №8
# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе
# данных, а пароль должен быть зашифрован

from flask import render_template, request
from flask_wtf import FlaskForm, CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash

from flask import Flask

from Flask_Sem3.Task4.form import RegisterForm
from Flask_Sem3.Task4.models import db, Users


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_user_task8.db'

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        lastname = form.lastname.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        user = Users(username=username, email=email, lastname=lastname, password=password)
        db.session.add(user)
        db.session.commit()
        return f'Вы успешно зарегистрированы'
    return render_template('register.html', form=form)


@app.route('/users/')
def get_user():
    users = Users.query.all()
    context = {
        "users": users
    }
    return render_template('users.html', **context)
