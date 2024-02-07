from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    surname = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f'{self.name}'