from app import db

class Attack(db.Model):
    __tablename__ = "RtsAttack"
    id = db.Column(db.Integer, primary_key = True)
    
    player_id = db.Column(db.String(120), db.ForeignKey("RtsPlayer.id"))
    player = db.relationship('Player', foreign_keys = [player_id])

    origin_id = db.Column(db.Integer, db.ForeignKey("RtsTown.id"))
    destination_id = db.Column(db.Integer, db.ForeignKey("RtsTown.id"))

    origin = db.relationship('Town', foreign_keys = [origin_id])
    destination = db.relationship('Town', foreign_keys=[destination_id])
    
    knight_amount = db.Column(db.Integer)
    cavalry_amount = db.Column(db.Integer)
    pikemen_amount = db.Column(db.Integer)

    def __init__(self, user, destination, origin, knight_amount = 0, cavalry_amount = 0, pikemen_amount = 0):
        self.user = user
        self.destination = destination
        self.origin = origin
        self.knight_amount = knight_amount
        self.cavalry_amount = cavalry_amount
        self.pikemen_amount = pikemen_amount