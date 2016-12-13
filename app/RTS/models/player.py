from app.db import db

class Player(db.Model):
    __tablename__ = "RtsPlayer"

    username = db.Column(db.String, primary_key = True)
    house = db.Column(db.String)
    towns = db.relationship('Town', backref='RtsPlayer', lazy='dynamic')

    def __init__(self, username, house):
        self.username = username
        self.house = house
        self.towns = []