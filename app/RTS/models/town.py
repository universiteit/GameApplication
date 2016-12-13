from app import db

class Town(db.Model):
    __tablename__ = "RtsTown"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), db.ForeignKey("RtsUser.username"))
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

    def __init__(self, username, name, knights = 0, cavalry = 0, pikemen = 0, lumber_mill = 1, gold_mine = 1, farm = 1, barracks = 1, wall = 0, quarry = 1, gold = 0, wood = 0, food = 0, iron = 0, upgrade=None, upgrade_time_done = None):
        self.username = username
        self.name = name
        self.knights = knights
        self.cavalry = cavaly
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