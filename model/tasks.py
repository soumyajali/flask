from extension import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    category = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(150), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
