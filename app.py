# from db_repository.db_connection import cred
from flask import Flask, render_template, redirect, request, url_for, flash, make_response
from loginforms import *
from db_repository.db import db_auth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hacktaxi_secret_key'
ADMIN_FLAG = False
USER_FLAG = False
LOGIN = 0


@app.route('/cookie/')
def cookie():
    res = make_response("Setting a cookie")
    res.set_cookie('foo', 'bar', max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.route('/')
@app.route('/main')
def main():
    if USER_FLAG:
        return 'privet' + LOGIN
    else:
        return 'main'


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
            db_auth.sign_in_with_email_and_password(login + "@gmail.com", passwd)
            global LOGIN
            LOGIN = login
            global USER_FLAG
            USER_FLAG = True
        except Exception as _ex:
            render_template('auth.html', title='Авторизация', form=form)
        return redirect('/')
    return render_template('auth.html', title='Авторизация', form=form)


@app.route('/account/<int:id>')
def account(id):
    return str(id)


@app.route('/about')
def about():
    return 'Страница о нас'


if __name__ == "__main__":
    app.run(debug=True)
