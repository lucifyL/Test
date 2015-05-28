from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy import Column, DateTime
from datetime import date
import time

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))
                            
    def __init__(self, username, email, password):
        self.username = username
        self.email = email.lower()
        self.set_password(password)
        
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

class Weight(db.Model):
    __tablename__ = 'weight'
    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    record_date = db.Column(db.DateTime, default = date.today())
    weight = db.Column(db.Float)

    def __init__(self, username, weight):
        self.username = username
        self.weight = weight