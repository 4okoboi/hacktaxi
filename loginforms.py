from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class AdminLoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], id='username')
    password = PasswordField('Пароль', validators=[DataRequired()], id='password')
    submit = SubmitField('Войти')


class UserLoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], id='username')
    password = PasswordField('Пароль', validators=[DataRequired()], id='password')
    submit = SubmitField('Войти')

