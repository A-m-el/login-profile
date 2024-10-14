from app import app

@app.route('/')
@app.route('/Register')
def first_try():
    return 'hello world'

