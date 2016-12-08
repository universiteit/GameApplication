from app.db import db

class User(db.Model):
    __tablename__ = "RtsUser"

    username = db.Column(db.String, primary_key = True)
    house = db.Column(db.String)

    def __init__(self, username, house):
        self.username = username
        self.house = house