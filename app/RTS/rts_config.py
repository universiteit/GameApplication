pikemen_defense = 35
pikemen_offense = 10

knight_defense = 10
knight_offense = 40

cavalry_defense = 30
cavalry_offense = 130

def get_wall_defense(level):
    if level <= 20:
        return 1 + ((level * 5) / 100) 
    return None

buildings = ["Wall", "Lumber Camp", "Iron Quarry", "Goldmine", "Barracks", "Farm"]