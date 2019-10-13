from . import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(30), nullable=False)
    done = db.Column(db.Boolean, default=False)
