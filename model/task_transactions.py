from extension import db
from datetime import datetime

class TaskTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, nullable=False)
    from_status = db.Column(db.String(150), nullable=False)
    to_status = db.Column(db.String(150), nullable=False)
    reason = db.Column(db.String(150), nullable=True)
    time = db.Column(db.String(50), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    transaction_type = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)