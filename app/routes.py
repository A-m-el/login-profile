from flask import flash, redirect, render_template, request, url_for
from app import app, db
from app.forms import RegisterForm
from app.models import User

@app.route('/' , methods=['GET', 'POST'])
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    # This checks if the form submission is valid and method is POST
    if form.validate_on_submit():
        print("Form is valid")
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)  # Ensure `set_password` is implemented correctly
        db.session.add(user)
        db.session.commit()
        
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)
