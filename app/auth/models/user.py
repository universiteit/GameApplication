from app import db

class User(db.Model):
    __tablename__ = "AuthUser"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.LargeBinary())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    