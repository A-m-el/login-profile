from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash




class User(db.Model, UserMixin):   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=True)
    password_hash =  db.Column(db.String(128), index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
  
    def __repr__(self):
         return f'<User {self.username}>'





    