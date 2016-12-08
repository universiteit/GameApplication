from app.db import db

class Attack(db.Model):
    __tablename__ = "RtsAttack"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), db.ForeignKey("RtsUser.username"))

    origin = db.relationship('Town', backref='id', lazy='dynamic')
    destination = db.relationship('Town', backref='id', lazy='dynamic')
    
    knight_amount = db.Column(db.Integer)
    cavalry_amount = db.Column(db.Integer)
    pikemen_amount = db.Column(db.Integer)
    
    

    def __init__(self, username, destination, origin, knight_amount = 0, cavalry_amount = 0, pikemen_amount = 0):
        self.username = username
        self.destination = destination
        self.origin = origin
        self.knight_amount = knight_amount
        self.cavalry_amount = cavalry_amount
        self.pikemen_amount = pikemen_amount