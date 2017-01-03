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

    # Removes given units from town, if the town has enough of each unit.
    def remove_units(self, knights = 0, cavalry = 0, pikemen = 0):
        if self.knights >= knights and self.cavalry >= cavalry and self.pikemen >= pikemen:
            self.knights -= knights
            self.cavalry -= cavalry
            self.pikemen -= pikemen
            return True
        return False
    
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
        return datetime.timedelta(hours = h, minutes = m)

    # Get the amount of resources per minute based on given level.
    def get_production(self, level):
        return int(math.ceil((level * 50) ** 1.2))

    # Returns dictionary of the cost of resources for a given unit
    def get_unit_cost(self, unit):
        return {
            'knight' : { 'gold' : 25, 'wood' : 60, 'food' : 30, 'iron' : 70},
            'cavalry' : { 'gold' : 50, 'wood' : 125, 'food' : 100, 'iron' : 250},
            'pikemen' : { 'gold' : 15, 'wood' : 50, 'food' : 30, 'iron' : 10},
        }[unit.lower()]
        
    # Adds given units if the town has enough resources
    def add_units(self, knight = 0, cavalry = 0, pikemen = 0):
        knight_cost = self.get_unit_cost("knight")
        cavalry_cost = self.get_unit_cost("cavalry")
        pikemen_cost = self.get_unit_cost("pikemen")

        def sum_costs(key):
            return knight_cost[key] * knight + cavalry_cost[key] * cavalry + pikemen_cost[key] * pikemen

        gold = sum_costs("gold")
        wood = sum_costs("wood")
        food = sum_costs("food")
        iron = sum_costs("iron")
        if self.remove_resources(gold, food, wood, iron):
            self.knights += knight
            self.cavalry += cavalry
            self.pikemen += pikemen

    # Converts building name in string format to the level of the current town's building
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

    # Predicate that checks whether the town has at least the given resource amounts
    def check_resources(self, gold = 0, food = 0, wood = 0, iron = 0):
        return (self.food - food) >= 0 and (self.gold - gold) >= 0 and (self.iron - iron) >= 0 and (self.wood - wood) >= 0

    # Removes resources from the town if town has enough resources.
    def remove_resources(self, gold = 0, food = 0, wood = 0, iron = 0):
        if self.check_resources(gold, food, wood, iron) and gold <= 0 and food <= and wood <= 0 and iron <=0:
            self.gold -= gold
            self.food -= food
            self.wood -= wood
            self.iron -= iron
            return True
        return False

    # Sets an upgrade if not already in progress and enough money is in the town to purchase it.
    def add_upgrade(self, building):
        building_level = self.get_building_level(building)
        if not self.upgrade:
            upgrade_cost = self.get_upgrade_cost(building_level)
            if not self.remove_resources(upgrade_cost, upgrade_cost, upgrade_cost, upgrade_cost):
                return 
            self.upgrade = building
            self.upgrade_time_done = datetime.datetime.now() + self.get_upgrade_time(building_level)
        else:
            raise RuntimeError("Town already has an upgrade queued up")

    # Increments resources according to production levels.
    def update_resources(self):
        self.gold += int(self.get_production(self.gold_mine) / 12.0)
        self.wood += int(self.get_production(self.lumber_mill) / 12.0)
        self.food += int(self.get_production(self.farm) / 12.0)
        self.iron += int(self.get_production(self.quarry) / 12.0)
    
    # Checks whether the upgrade time has passed
    # If so, remove the upgrade and upgrade timer and upgrade the building.
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
            self.upgrade = None
            self.upgrade_time_done = None