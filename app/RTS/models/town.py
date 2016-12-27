from app import db

class Town(db.Model):
    __tablename__ = "RtsTown"

    id = db.Column(db.Integer, primary_key = True)
    player_id = db.Column(db.Integer, db.ForeignKey("RtsPlayer.id"))
    player = db.relationship('Player', foreign_keys = [player_id])

    name = db.Column(db.String(120))
    knights = db.Column(db.Integer)
    cavalry = db.Column(db.Integer)
    pikemen = db.Column(db.Integer)
    lumber_mill = db.Column(db.Integer)
    gold_mine = db.Column(db.Integer)
    farm = db.Column(db.Integer)
    barracks = db.Column(db.Integer)
    wall = db.Column(db.Integer)
    quarry = db.Column(db.Integer)
    gold = db.Column(db.Integer)
    wood = db.Column(db.Integer)
    food = db.Column(db.Integer)
    iron = db.Column(db.Integer)
    upgrade = db.Column(db.String)
    upgrade_time_done = db.Column(db.DateTime)

    def __init__(self, player, name, knights = 0, cavalry = 0, pikemen = 0, lumber_mill = 1, gold_mine = 1, farm = 1, barracks = 1, wall = 0, quarry = 1, gold = 0, wood = 0, food = 0, iron = 0, upgrade=None, upgrade_time_done = None):
        self.player = player
        self.name = name
        self.knights = knights
        self.cavalry = cavalry
        self.pikemen = pikemen
        self.lumber_mill = lumber_mill
        self.gold_mine = gold_mine
        self.farm = farm
        self.barracks = barracks
        self.wall = wall
        self.quarry = quarry
        self.gold = gold
        self.wood = wood
        self.food = food
        self.iron = iron

    def get_costs(self, level):
        exponent = 1.1
        val = 40
        for i in range(level):
            val = val ** exponent
        return int(val)

    def get_time(self, level):
        minutes = level ** 2
        h, m = divmod(minutes, 60)
        return "%d:%02d:%02d" % (h, m, 00)

    def get_production(self, level):
        return int((level * 50) ** 1.2)

    def get_unit_costs(self, unit):
        return {
            'knight' : { 'gold' : 25, 'wood' : 60, 'food' : 30, 'iron' : 70},
            'cavalry' : { 'gold' : 50, 'wood' : 125, 'food' : 100, 'iron' : 250},
            'pikemen' : { 'gold' : 15, 'wood' : 50, 'food' : 30, 'iron' : 10},
        }[unit.lower()]
        
    def add_units(self, knight, cavalry, pikemen):
        self.knights += knight
        self.cavalry += cavalry
        self.pikemen += pikemen