# from db_repository.db_connection import cred
from flask import Flask, render_template, redirect, request, url_for, flash, make_response, session
from forms import *
from db_repository.db import db_auth, database
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hacktaxi_secret_key'
ADMIN_FLAG = False
USER_FLAG = False
username = ''
SESSION = {}
data_for_reg = {}


@app.route('/')
@app.route('/main')
def main():
    print(username)
    return render_template('index.html', user=USER_FLAG, login=username)


@app.route('/admin_page')
def admin_page():
    if ADMIN_FLAG:
        return "Admin Page"
    else:
        return redirect('/admin_auth')


@app.route('/admin_auth', methods=['GET', 'POST'])
def admin_auth():
    form = AdminLoginForm()
    if form.validate_on_submit():
        global ADMIN_FLAG
        ADMIN_FLAG = True
        return redirect('/admin_page')
    return render_template('admin_auth.html', title='Авторизация админа', form=form)


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    form = UserLoginForm()
    if form.validate_on_submit():
        login = form.username.data
        passwd = form.password.data
        try:
            session_auth = db_auth.sign_in_with_email_and_password(login + "@gmail.com", passwd)
            print(session_auth)
            # session['user_id'] = session_auth['localId']
            # data = {'b_day': data_for_reg['db'], 'name': data_for_reg['name'], 'number': data_for_reg['phone_number'],
            #         'patronymic': data_for_reg['patronymic'], 'secondName': data_for_reg['lastname'],
            #         'userId': session_auth['localId'], 'username': login}
            # print(data)
            # database.child('Users').set(data)
            global username
            username = login
            global USER_FLAG
            USER_FLAG = True
        except Exception as _ex:
            print(type(_ex))
            return render_template('auth.html', title='Авторизация', form=form, error='Вы ввели неверные данные')
        return redirect('/')

    return render_template('auth.html', title='Авторизация', form=form)


@app.route('/user_reg', methods=['GET', 'POST'])
def user_reg():
    form = UserRegForm()
    if form.validate_on_submit():
        login = form.username.data
        passwd = form.password.data
        try:
            db_auth.create_user_with_email_and_password(login + "@gmail.com", passwd)
            data_for_reg['name'] = form.name.data
            data_for_reg['lastname'] = form.name.data
            data_for_reg['patronymic'] = form.patronymic.data
            data_for_reg['db'] = form.date_of_birth.data
            data_for_reg['phone_number'] = form.phone_number.data
        except Exception as _ex:
            print(_ex)
            return render_template('user_reg.html', title='Регистрация пользователя', form=form)
        return redirect('/auth')
    return render_template('user_reg.html', title='Регистрация пользователя', form=form)


@app.route('/account/<string:username>')
def account(username):
    return username


@app.route('/add_trip', methods=['GET', 'POST'])
def add_trip():
    if USER_FLAG:
        form = TripDriverAddForm()
        if form.validate_on_submit():
            data = {'active': 'true',
                    'car': form.car_name.data,
                    'date': form.deadline_date.data,
                    'driver': SESSION['name'],
                    'from': form.from_place.data,
                    'more': form.more.data,
                    'number': SESSION['number'],
                    'places': 5,
                    'time': form.deadline_time.data,
                    'to': form.to_place.data
                    }
            try:
                database.child('Roads').push(data)
            except Exception as _ex:
                print(_ex)
                return render_template('trip_add_driver.html', form=form)
            return redirect('/')
        return render_template('trip_add_driver.html', form=form)
    else:
        pass


@app.route('/about')
def about():
    return 'Страница о нас'


if __name__ == "__main__":
    app.run(debug=True)
