from flask import  render_template
from app import app
from app.forms import RegisterForm

@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
        # if form.validate_on_submit():  # This checks if the form submission is valid
        #     # Handle successful form submission here, e.g., save data
        #     print("User Added yew!")
        #     return redirect(url_for('register'))
    return render_template('register.html', form=form) 

