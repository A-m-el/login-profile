from dataclasses import field
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField


class RegisterForm(FlaskForm):
    name = StringField('Name') #, validators=[DataRequired()]
    email = EmailField('Email Address')
    
    # def validate_password(self, field):
    #     if len(field.data < 8):
    #         raise ValidationError('Passwors must be at least 8 characters')
    password = PasswordField('Password') #, validate_password(password)
    register = SubmitField('Register')    
     
    