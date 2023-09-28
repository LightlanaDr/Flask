from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_task3.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    id_grade = db.Column(db.Integer, db.ForeignKey('grade.id'))


    def __repr__(self):
        return f'{self.firstname} {self.lastname}'


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_subject = db.Column(db.String(80), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    students = db.relationship('Student', backref='grade', lazy=True)

    def __repr__(self):
        return f'{self.name}'
