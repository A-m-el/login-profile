


from dataclasses import field
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, ValidationError


class RegisterFrom(FlaskForm):
    name = StringField('Name') #, validators=[DataRequired()]
    email = EmailField('Email Address')
    
    def validate_password(FlaskForm):
        if len(field.data < 8):
            raise ValidationError('Passwors must be at least 8 characters')
    password = PasswordField('Password', validate_password)
    register = SubmitField('Register')    
     
    