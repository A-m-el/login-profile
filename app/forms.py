from dataclasses import field
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import  EqualTo, DataRequired, EqualTo



class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()]) #, validators=[DataRequired()]
    email = EmailField('Email Address', validators=[DataRequired()])
    
    # def validate_password(self, field):
    #     if len(field.data < 8):
    #         raise ValidationError('Passwors must be at least 8 characters')
    password = PasswordField('Password', validators=[DataRequired()]) #, validate_password(password)
    password2 = PasswordField( 'Repeat Password', 
                              validators=[EqualTo('password', message='Passwords must match')])
    register = SubmitField('Register')    
     
    