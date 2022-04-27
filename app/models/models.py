from app.models.orm import db

class Users(db.Model):
    __tablename__ = 'users'
    email_address = db.Column(db.String(80), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(12), nullable=False, unique=True)