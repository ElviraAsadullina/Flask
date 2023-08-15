# Задание №1
# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.

from flask import Flask, render_template
from seminar_3.models_03 import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/university.db'
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/university/')
def get_list():
    university = Student.query.all()
    context = {'university': university}
    return render_template('university.html', **context)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Ok university')


@app.cli.command("add-student")
def add_student():
    student = Student(first_name='Ivan', last_name='Ivanov', age=20, gender='male', group=11, faculty_id=1)
    db.session.add(student)
    db.session.commit()
    print('Student added successfully!')


if __name__ == '__main__':
    app.run(debug=True)

