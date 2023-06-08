from wtforms import BooleanField, StringField,FileField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegisterForm(FlaskForm):

    username=StringField('Username',validators=[DataRequired(),Length(min=3, max=30)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=StringField('password',validators=[DataRequired()])
    confirm_password=StringField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    photo=FileField('Photo')


class LoginForm(FlaskForm):

    username=StringField('Username',validators=[DataRequired(),Length(min=3, max=30)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=StringField('password',validators=[DataRequired()])
    remember_me=BooleanField('remember_me')

  
