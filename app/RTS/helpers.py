from flask import session, redirect
from app.RTS.models import *
from app import db

houses = ["Stark", "Arryn", "Tully", "Lannister", "Greyjoy", "Targaeryan", "Baratheon", "Tyrell", "Martell"]
towns = ["Winterfell", "The Eyrie", "Riverrun", "Casterly Rock", "Pyke", "King's Landing", "Storm's End", "Highgarden", "Sunspear"]

def session_id():
    return session["user_id"]

def current_player():
    if "user_id" in session:
        return Player.query.filter_by(id=session["user_id"]).first()
    else:
        return None

# Instantiates a new player for a user with a random house and random starting town
def generate_new_player(user):
    house = houses[random.randrange(0,len(houses))]
    new_player = Player(user, house)
    starting_town = generate_random_town(new_player)
    new_player.towns.append(starting_town)
    return new_player

# Generates a new town with an initial owner
def generate_random_town(player):
    name = towns[random.randrange(0,len(towns))]
    new_town = Town(player, name)
    new_town.knights = 1
    new_town.pikemen = 5
    new_town.cavalry = 3
    return new_town

def get_player_from_user_id(user_id):
    player = Player.query.filter_by(id=user_id).first()
    if not player:
        player = generate_new_player(user)
        db.session.add(player)
        db.session.commit()
    return player
