from app.db import db

class Unit(db.Model):
    __tablename__ = "RtsUnit"

    type = db.Column(db.String, primary_key = True)
    offense = db.Column(db.Integer)
    defense = db.Column(db.Integer)

    def __init__(self, type, offense, defense):
        self.type = type
        self.offense = offense
        self.defense = defense