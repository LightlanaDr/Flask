# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from models import db, Student, Faculty
#
# app = Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# db.init_app(app)
from flask import render_template

import random

from flask import Flask
from Flask_Sem3.Task2.models import db, Books, Author, BooksAuthor

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_books.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-books")
def add_data():
    for i in range(1, 10):
        book = Books(
            name=f'name_{i}',
            year=i + 2000,
            count=i
        )
        db.session.add(book)

    for i in range(0, 10):
        author = Author(
            firstname=f'firstname{i}',
            lastname=f'lastname{i}',
        )
        db.session.add(author)
    db.session.commit()

    for i in range(1, 10):
        books_author = BooksAuthor(
            book_id=random.randint(1, 9),
            author_id=random.randint(1, 9),
        )
        db.session.add(books_author)
    db.session.commit()

    print('Данные добавлены')


@app.route('/book/')
def get_books():
    books = Books.query.all()
    context = {
        "books": books
    }
    return render_template('books.html', **context)
