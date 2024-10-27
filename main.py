from app import app

print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])
