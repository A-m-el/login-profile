from flask import  flash, redirect, render_template, request, session, url_for
from app import app
from app.forms import RegisterForm
from app.models import User

@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():  # This checks if the form submission is valid
    # Handle successful form submission here, e.g., save data
        # print("User Added yew!")
        # if (request.method == 'POST'):
        #     user = User(form.name.data, form.email.data,
        #                 form.password.data )
        #     session.add(user)
        #     # flash('thanks for registering')
        return redirect(url_for('register'))
    return render_template('register.html', form=form) 

