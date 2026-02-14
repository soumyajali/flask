from extension import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    admin_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(150), nullable=False)
    small_description = db.Column(db.String(50), nullable=False, default="admin")
