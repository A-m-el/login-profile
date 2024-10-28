from flask import render_template, request
from app import app

@app.route('/')
@app.route('/Register')
def register():
    if request.method == 'POST':
        # Process form data (e.g., validate, save to database)
        pass
    return render_template('register.html', message="Register here!")

