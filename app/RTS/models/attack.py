from app import db
from config import *

class Attack(db.Model):
    __tablename__ = "RtsAttack"
    id = db.Column(db.Integer, primary_key = True)
    
    player_id = db.Column(db.String(120), db.ForeignKey("RtsPlayer.id"))
    player = db.relationship('Player', foreign_keys = [player_id])

    origin_id = db.Column(db.Integer, db.ForeignKey("RtsTown.id"))
    destination_id = db.Column(db.Integer, db.ForeignKey("RtsTown.id"))

    origin = db.relationship('Town', foreign_keys = [origin_id])
    destination = db.relationship('Town', foreign_keys=[destination_id])
    
    knights = db.Column(db.Integer)
    cavalry = db.Column(db.Integer)
    pikemen = db.Column(db.Integer)

    def __init__(self, player, destination, origin, knights = 0, cavalry = 0, pikemen = 0):
        self.player = player
        self.destination = destination
        self.origin = origin
        self.knights = knights
        self.cavalry = cavalry
        self.pikemen = pikemen

    def get_defender_stats(self):
        defense = (self.origin.pikemen * pikemen_defense) + (self.origin.knights * knights_defense) + (self.origin.cavalry * cavalry_defense)
        defense *= get_wall_defense(self.origin.wall)
        
        offense = (self.origin.pikemen * pikemen_offense) + (self.origin.knights * knights_offense) + (self.origin.cavalry * cavalry_offense)
        return defense, offense

    def get_attacker_stats(self):
        defense = (self.pikemen * pikemen_defense) + (self.knights * knights_defense) + (self.cavalry * cavalry_defense)
        
        offense = (self.pikemen * pikemen_offense) + (self.knights * knights_offense) + (self.cavalry * cavalry_offense)
        return defense, offense
    
    def simulate(self):
        defender = self.get_defender_stats
        attacker = self.get_attacker_stats

        if (attacker[1] - defender[0]) > 0:
            return self.origin
        return self.destination
    
    
        
