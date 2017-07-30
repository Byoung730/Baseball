from app import db
from main import db

class Stats(db.Model):
    Name = db.Column(db.String(80), unique=True)
    ID = db.Column(db.Integer, primary_key = True)
    CFIP = db.Column(db.Integer)
    xFIP = db.Column(db.double)
    FIP = db.Column(db.float)
    KperBB = db.Column(db.float)
