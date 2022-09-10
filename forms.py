from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, DateField, TimeField, Field
from wtforms.validators import DataRequired, InputRequired, Optional


class AdminLoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], id='username')
    password = PasswordField('Пароль', validators=[DataRequired()], id='password')
    submit = SubmitField('Войти')


class UserLoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], id='username')
    password = PasswordField('Пароль', validators=[DataRequired()], id='password')
    submit = SubmitField('Войти')


class UserRegForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], id='username')
    password = StringField('Пароль', validators=[DataRequired()], id='password')
    name = StringField('Имя', validators=[DataRequired()], id='name')
    lastname = StringField('Фамилия', validators=[DataRequired()], id='lastname')
    # date_of_birth = DateField('Дата рождения в формате ДД.ММ.ГГГГ', validators=[DataRequired()], id='date_of_birth',
    #                           format='%m/%d/%Y')
    phone_number = StringField('Номер телефона', validators=[DataRequired()], id='phone_number')
    account_type = RadioField('Label', choices=[(1, 'Водитель'), (2, 'Пользователь')], default=1,
                              validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class TripDriverAddForm(FlaskForm):
    deadline_date = DateField('Дедлайн число', validators=[DataRequired()], id='deadline_date')
    deadline_time = TimeField('Дедлайн время', validators=[DataRequired()], id='deadline_time')
    from_place = StringField('Откуда', validators=[DataRequired()], id='from_place')
    to_place = StringField('Куда', validators=[DataRequired()], id='to_place')
    car_name = StringField('Машина', validators=[DataRequired()], id='car_name')
    more = StringField('Дополнительно', validators=[Optional()], id='more')

    submit = SubmitField('Создать')


class TripUserAddForm(FlaskForm):
    deadline_date = DateField('Дедлайн число', validators=[DataRequired()], id='deadline_date')
    deadline_time = TimeField('Дедлайн время', validators=[DataRequired()], id='deadline_time')
    from_place = StringField('Откуда', validators=[DataRequired()], id='from_place')
    to_place = StringField('Куда', validators=[DataRequired()], id='to_place')
    requirements = Field('Требования', validators=[Optional()], id='requirements')
    submit = SubmitField('Запросить')
