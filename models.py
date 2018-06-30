from softstack import db
from datetime import datetime

class Software(db.Model):
    name=db.Column(db.String(40),primary_key=True)
    userid=db.Column(db.String(20),nullable=False)
    description=db.Column(db.String(150),nullable=False)
    upload_time=db.Column(db.DATETIME,default=datetime.utcnow)

class User(db.Model):
    username=db.Column(db.String(20),primary_key=True)
    password=db.Column(db.String(20),nullable=False)
