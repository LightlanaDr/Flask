# Задание №3
# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.

from flask import render_template

import random

from flask import Flask
from Flask_Sem3.Task1.models import db, Student, Grade

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_task3.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-student")
def add_data():
    # lst_subject=['Математика', 'История', 'Психология']
    for i in range(1, 6):
        grade_1 = Grade(
            name_subject=random.choice(['Математика', 'История', 'Психология']),
            grade=random.randint(1,5),
        )
        db.session.add(grade_1)

    for i in range(0, 10):
        student = Student(
            firstname=f'firstname{i}',
            lastname=f'lastname{i}',
            email=f'{i}@mail.com',
            group=random.randint(1, 15),
            id_grade=random.randint(1,5)
        )
        db.session.add(student)
    db.session.commit()
    print('Данные добавлены')


@app.route('/student/')
def get_student():
    students = Student.query.all()
    context={
        "students": students
    }
    return render_template('students.html', **context)