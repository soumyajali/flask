from extension import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String(150), nullable=False, unique=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    credits = db.Column(db.Integer, nullable=False, default=0)
    password = db.Column(db.String(150), nullable=False)
