from app import db
import datetime, math

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

    # Gets the cost of upgrading a building from given level to the next.
    def get_upgrade_cost(self, level):
        exponent = 1.06
        val = 40
        for i in range(int(level)):
            val = val ** exponent
        return int(math.ceil(val))

    # Get the time in timespan required to upgrade a building frm given level to the next.
    def get_upgrade_time(self, level):
        minutes = level ** 2
        h, m = divmod(minutes, 60)
        return datetime.time(hour = h, minute = m)

    # Get the amount of resources per minute based on given level.
    def get_production(self, level):
        return int(math.ceil((level * 50) ** 1.2))

    def get_unit_cost(self, unit):
        return {
            'knight' : { 'gold' : 25, 'wood' : 60, 'food' : 30, 'iron' : 70},
            'cavalry' : { 'gold' : 50, 'wood' : 125, 'food' : 100, 'iron' : 250},
            'pikemen' : { 'gold' : 15, 'wood' : 50, 'food' : 30, 'iron' : 10},
        }[unit.lower()]
        
    def add_units(self, knight = 0, cavalry = 0, pikemen = 0):
        self.knights += knight
        self.cavalry += cavalry
        self.pikemen += pikemen

    def get_building_level(self, building):
        building = building.lower()
        if(building == 'barrack'):
            return self.barracks
        elif(building == 'lumber'):
            return self.lumber_mill
        elif(building == 'quarry'):
            return self.quarry
        elif(building == 'mine'):
            return self.gold_mine
        elif(building == 'farm'):
            return self.farm
        elif(building == 'wall'):
            return self.wall      
        else:
            raise ValueError("Invalid value")

    def add_upgrade(self, building):
        if not self.upgrade:
            self.food -= self.get_upgrade_cost(self.get_building_level(building))
            self.wood -= self.get_upgrade_cost(self.get_building_level(building))
            self.iron -= self.get_upgrade_cost(self.get_building_level(building))
            self.gold -= self.get_upgrade_cost(self.get_building_level(building))
            if self.food or self.wood or self.iron or self.gold < 0:
                return False
            self.upgrade = building
            self.upgrade_time_done = self.get_upgrade_time(1)
            return True
        else:
            raise RuntimeError("Town already has an upgrade queued up")
            return False

    def update_resources(self):
        self.gold += int(self.get_production(self.gold_mine) / 12.0)
        self.wood += int(self.get_production(self.lumber_mill) / 12.0)
        self.food += int(self.get_production(self.farm) / 12.0)
        self.iron += int(self.get_production(self.quarry) / 12.0)
    
    def update_upgrade(self):
        if self.upgrade_time_done and datetime.datetime.now() >= self.upgrade_time_done:
            building = self.upgrade.lower()
            if(building == 'barrack'):
                self.barracks += 1
            elif(building == 'lumber'):
                self.lumber_mill += 1
            elif(building == 'quarry'):
                self.quarry += 1
            elif(building == 'mine'):
                self.gold_mine += 1
            elif(building == 'farm'):
                self.farm += 1
            elif(building == 'wall'):
                self.wall += 1        
            else:
                raise ValueError("Invalid value")
            upgrade = None
            upgrade_time_done = None