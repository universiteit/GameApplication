<<<<<<< HEAD
from app.db import db
from config import *
=======
from app import db
>>>>>>> 22a44f66e946b7887806bf46cfe8de2e7310e08d

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

    def __init__(self, player, destination, origin, knight_amount = 0, cavalry_amount = 0, pikemen_amount = 0):
        self.player = player
        self.destination = destination
        self.origin = origin
        self.knight_amount = knight_amount
        self.cavalry_amount = cavalry_amount
        self.pikemen_amount = pikemen_amount

    def get_defender_stats(self):
        defense = (self.origin.pikemen * pikemen_defense) + 
                    (self.origin.knights * knights_defense) +
                    (self.origin.cavalry * cavalry_defense)
        defense *= get_wall_defense(self.origin.wall)
        
        offense = (self.origin.pikemen * pikemen_offense) + 
                    (self.origin.knights * knights_offense) +
                    (self.origin.cavalry * cavalry_offense)
        return defense, offense

    def get_attacker_stats(self):
        defense = (self.pikemen_amount * pikemen_defense) + 
                    (self.knight_amount * knights_defense) +
                    (self.cavalry_amount * cavalry_defense)
        
        offense = (self.pikemen_amount * pikemen_offense) + 
                    (self.knight_amount * knights_offense) +
                    (self.cavalry_amount * cavalry_offense)
        return defense, offense
    
    def simulate(self):
        defender = self.get_defender_stats
        attacker = self.get_attacker_stats

        if (attacker[1] - defender[0]) > 0:
            return self.origin
        return self.destination
    
    
        
