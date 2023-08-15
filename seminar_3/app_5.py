# Задание №3
# Доработаем задача про студентов.
# Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.

from flask import Flask, render_template
from seminar_3.models_05 import db, Student, Mark

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/school.db'
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return 'School'


@app.route('/school/')
def get_library_list():
    school = Mark.query.all()
    context = {'school': school}
    return render_template('school.html', **context)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Ok school')


@app.cli.command("add-student")
def add_student():
    student = Student(first_name='Pavel', last_name='Sidorov', group='4', email='pavel@mail.ru')
    db.session.add(student)
    db.session.commit()
    print('Student added successfully!')


@app.cli.command("add-mark")
def add_mark():
    mark = Mark(subject_name='Maths', mark=5, student_id=1)
    db.session.add(mark)
    db.session.commit()
    print('Mark added successfully!')


if __name__ == '__main__':
    app.run(debug=True)
