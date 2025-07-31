from flask import flash, redirect, render_template, url_for
from app import db
from app.auth.forms import  RegisterForm
from app.models import User
from app.auth import auth_bp

@auth_bp.route('/')
@auth_bp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit(): 
        user = User(name=form.name.data, email=form.email.data, username=form.username.data)
        user.set_password(form.password.data)  
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('auth.register'))
    return render_template('register.html', title='Register', form=form)


    