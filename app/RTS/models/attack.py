from app.db import db

class Attack(db.Model):
    __tablename__ = "RtsAttack"

    id = db.Colum(db.Integer, primary_key = True)
    username = db.Column(db.String(120), db.ForeignKey("User.username"))

    origin = db.relationship('Town', backref='id', lazy='dynamic')
    destination = db.relationship('Town', backref='id', lazy='dynamic')


    pikemen_amount = db.Column(db.Integer)
    cavalry_amount = db.Column(db.Integer)
    knight_amount = db.Column(db.Integer)

    def __init__(self, id, username, destination, origin, knight_amount, pikemen_amount, cavalry_amount):
        self.id = id
        self.username = username
        self.destination = destination
        self.origin = origin
        self.pikemen_amount = pikemen_amount
        self.cavalry_amount = cavalry_amount
        self.knight_amount = knight_amount