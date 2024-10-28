from flask import redirect, render_template, request, url_for
from app import app
from app.forms import RegisterForm

@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():  # This checks if the form submission is valid
        # Handle successful form submission here, e.g., save data
        print("User Added yew!")
        return redirect(url_for('/'))
    return render_template('register.html', form=form) 

