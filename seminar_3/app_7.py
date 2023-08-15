# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import CSRFProtect
import secrets
from werkzeug.security import generate_password_hash

from seminar_3.forms_07 import RegistrationForm
from seminar_3.models_07 import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/new_credentials.db'
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return 'New Hello'


@app.route('/new_register/', methods=['GET', 'POST'])
def new_register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        hashed_password = generate_password_hash(password)
        user = User(username=name, usersurname=surname, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success', name=name))
    return render_template('new_register.html', form=form)


@app.route('/success/<name>')
def success(name):
    return render_template('success.html', name=name)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Ok new_credentials')


if __name__ == '__main__':
    app.run(debug=True)
