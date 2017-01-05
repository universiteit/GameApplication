from app import db
from app.RTS.rts_config import *
import random, datetime

class Attack(db.Model):
    __tablename__ = "RtsAttack"
    id = db.Column(db.Integer, primary_key = True)
    
    player_id = db.Column(db.String(120), db.ForeignKey("RtsPlayer.id"))
    player = db.relationship('Player', foreign_keys = [player_id])

    origin_id = db.Column(db.Integer, db.ForeignKey("RtsTown.id"))
    destination_id = db.Column(db.Integer, db.ForeignKey("RtsTown.id"))

    origin = db.relationship('Town', foreign_keys = [origin_id])
    destination = db.relationship('Town', foreign_keys=[destination_id])

    arrival_time = db.Column(db.DateTime)
    
    knights = db.Column(db.Integer)
    cavalry = db.Column(db.Integer)
    pikemen = db.Column(db.Integer)
    doges = db.Column(db.Integer)

    def __init__(self, player, destination, origin, knights = 0, cavalry = 0, pikemen = 0, doges = 0):
        self.player = player
        self.destination = destination
        self.origin = origin
        self.knights = knights
        self.cavalry = cavalry
        self.pikemen = pikemen
        self.doges = doges
        self.arrival_time = datetime.datetime.now() + datetime.timedelta(minutes = 10)

    def get_defender_stats(self):
        defense = (self.destination.pikemen * pikemen_defense) + (self.destination.knights * knight_defense) + (self.destination.cavalry * cavalry_defense) + (self.destination.doges * doge_defense)
        defense *= self.get_wall_defense(self.destination.wall)
        
        offense = (self.destination.pikemen * pikemen_offense) + (self.destination.knights * knight_offense) + (self.destination.cavalry * cavalry_offense) + (self.destination.doges * doge_offense)
        return defense, offense

    def get_attacker_stats(self):
        defense = (self.pikemen * pikemen_defense) + (self.knights * knight_defense) + (self.cavalry * cavalry_defense) + (self.doges * doge_defense)
        
        offense = (self.pikemen * pikemen_offense) + (self.knights * knight_offense) + (self.cavalry * cavalry_offense) + (self.doges * doge_offense)
        return defense, offense
    
    def take_damage(self, pikemen = 0, cavalry = 0, knights = 0, doges = 0, damage = 0, defense_modifier = 1):
        while damage > 0:
            if pikemen > 0 and damage > pikemen_defense * defense_modifier:
                damage -= pikemen_defense
                pikemen -= 1
            elif cavalry > 0 and damage > cavalry_defense * defense_modifier:
                damage -= cavalry_defense
                cavalry -= 1
            elif knights > 0 and damage > knight_defense * defense_modifier:
                damage -= knight_defense
                knights -= 1
            elif doges > 0 and damage > doge_defense * defense_modifier:
                damage -= doge_defense
                doges -= 1
            else:
                return pikemen, cavalry, knights, doges
        return pikemen, cavalry, knights, doges

    def simulate_battle(self):
        defender_defense = self.get_defender_stats()[0]
        attacker_offense = self.get_attacker_stats()[1]
        if defender_defense > attacker_offense:
            attacker_army = 0, 0, 0
            defender_army = self.take_damage(self.destination.pikemen, self.destination.cavalry, self.destination.knights, self.destination.doges, attacker_offense - defender_defense, self.get_wall_defense(self.destination.wall))
            return { "success" : False, "attacking army" : attacker_army, "defending army" : defender_army }
        else:
            defender_army = 0, 0, 0
            attacker_army = self.take_damage(self.pikemen, self.cavalry, self.knights, self.doges, attacker_offense - defender_defense)
            return { "success" : True, "attacking army" : attacker_army, "defending army" : defender_army }
    
    def get_wall_defense(self, level):
        if level <= 20:
            return 1 + ((level * 5) / 100) 
        return None
        
    # Resolves the attack, returning the new state of the destination (with perhaps a new owner and army size)
    def resolve(self):
        battle_result = self.simulate_battle()
        if battle_result["success"]:
            self.destination.player = self.player
            self.destination.pikemen = battle_result["attacking army"][0]
            self.destination.cavalry = battle_result["attacking army"][1]
            self.destination.knights = battle_result["attacking army"][2]
            self.destination.doges = battle_result["attacking army"][3]
        else:
            self.destination.pikemen = battle_result["defending army"][0]
            self.destination.cavalry = battle_result["defending army"][1]
            self.destination.knights = battle_result["defending army"][2]
            self.destination.doges = battle_result["defending army"][3]
        db.session.add(self.destination)
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        v = "ATTACK\n"
        v += self.player.user.username + "\n"
        v += str(self.destination) + "\n"
        v += str(self.origin) + "\n"
        v += str(self.knights) + "\n"
        v += str(self.cavalry) + "\n"
        v += str(self.pikemen) + "\n"
        v += str(self.doges) + "\n"
        v += "END ATTACK\n"
        return v