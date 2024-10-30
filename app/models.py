from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, unique=True)
    password_hash =  db.Column(db.String, index=True, unique=True)
    email = db.Column(d.String, unique=True)
    def __repr__(self):
         return f'<User {self.username}>'

    
    