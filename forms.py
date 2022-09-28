from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    company = StringField('company', validators=[DataRequired()])
    message = TextAreaField('message', validators=[DataRequired()])
    is_subscribe = BooleanField()


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired()])
    confirm_password = StringField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    
