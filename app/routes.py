from flask import  flash, redirect, render_template, request, session, url_for
from app import app
from app import db
from app.forms import RegisterForm
from app.models import User

@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    # if form.validate_on_submit():  # This checks if the form submission is valid     
    if request.method == 'POST' and form.validate():
            new_user = User(name = form.name.data, password_hash = form.password.data, 
                        email = form.email.data )
            db.session.add(new_user)
            db.session.commit()
            # flash('thanks for registering')
            return redirect(url_for('register'))
    return render_template('register.html', form=form) 

