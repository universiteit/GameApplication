from app.db import db

class User(db.Model):
    __tablename__ = "User"

    username = db.Column(db.String, primary_key = True)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password