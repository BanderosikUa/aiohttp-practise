from app.store.database.models import db

class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    time_created = db.Column(db.DateTime, nullable=False)