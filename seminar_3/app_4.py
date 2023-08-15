# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.

from flask import Flask, render_template
from seminar_3.models_04 import db, Book, Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/library.db'
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return 'Hiii'


@app.route('/library/')
def get_library_list():
    library = Book.query.all()
    context = {'library': library}
    return render_template('library.html', **context)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Okk')


@app.cli.command("add-author")
def add_author():
    author = Author(first_name='Lev', last_name='Tolstoy')
    db.session.add(author)
    db.session.commit()
    print('Author added successfully!')


@app.cli.command("add-book")
def add_book():
    book = Book(name='War and Peace', publ_year=1869, count=100, author_id=1)
    db.session.add(book)
    db.session.commit()
    print('Book added successfully!')


if __name__ == '__main__':
    app.run(debug=True)
