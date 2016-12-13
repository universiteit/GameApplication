from app import db

class Player(db.Model):
    __tablename__ = "RtsPlayer"

    id = db.Column(db.Integer, db.ForeignKey("AuthUser.id"), primary_key = True)
    user = db.relationship('User', foreign_keys = [id])

    house = db.Column(db.String)
    towns = db.relationship('Town', backref='RtsPlayer', lazy='dynamic')

    def __init__(self, user, house):
        self.user = user
        self.house = house
        self.towns = []