# from flask import  flash, redirect, render_template, request, session, url_for
# from app import app
# from app import db
# from app.forms import RegisterForm
# from app.models import User

# @app.route('/')
# @app.route('/register', methods=['GET', 'POST'])
# # def register():
# #     form = RegisterForm(request.form)
# #     # if form.validate_on_submit():  # This checks if the form submission is valid     
# #     if request.method == 'POST' and form.validate():
# #             new_user = User(name = form.name.data, password_hash = form.password.data, 
# #                         email = form.email.data )
# #             db.session.add(new_user)
# #             db.session.commit()
# #             # flash('thanks for registering')
# #             return redirect(url_for('register'))
# #     return render_template('register.html', form=form) 

# def register():
#         form = RegisterForm()
#         if form.validate_on_submit():
#                  user = User(name=form.name.data, email=form.email.data)
#                  user.set_password(form.password.data)
#                  db.session.add(user)
#                  db.session.commit()
#                  flash('Congratulations, you are now a registered user!')
#                  return redirect(url_for('register'))
#         return render_template('register.html', title='Register', form=form)


from flask import flash, redirect, render_template, request, url_for
from app import app, db
from app.forms import RegisterForm
from app.models import User

@app.route('/')
@app.route('/register', methods=['GET','POST'])
def register():
    print("Route accessed!")
    form = RegisterForm()
    
    if request.method == 'POST':
        print("POST request received")

    # This checks if the form submission is valid and method is POST
    if form.validate_on_submit():
        print("Form is valid")
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)  # Ensure `set_password` is implemented correctly
        db.session.add(user)
        db.session.commit()
        
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('register'))
    else:
            print("form unvalid")
            print(form.errors) 
    return render_template('register.html', title='Register', form=form)
