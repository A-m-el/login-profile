from dataclasses import field
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import  EqualTo, DataRequired, EqualTo, Email
from wtforms import validators



class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired() ])
    
    email = EmailField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', [
                validators.data_required(message='password is required'),
                validators.Length(message='password should be at least 8 char', min=8)
                ])
    password2 = PasswordField( 'Repeat Password', [
                validators.data_required(message='Confirm password'),
                validators.EqualTo('password', message='Passwords must match')
                
                                          ])
    register = SubmitField('Register')    
     
    