from flask import session, redirect
from app.RTS.models import *
from app.auth.models.user import User
import random
from app import db

houses = ["Arryn", "Baelish", "Baratheon", "Blackwood", "Bolton", "Bracken", "Brax", "Crakehall", "Cerwyn", "Clegane", "Connington", "Dondarrion", "Estermont" ,"Glover", "Greyjoy", "Hornwood", "Karstark", "Lannister", "Mallister", "Manderly", "Marbrand", "Martell", "Mormont", "Redwyne", "Seaworth", "Stark", "Swann", "Swyft", "Targaryen", "Tarth", "Tully", "Tyrell", "Whent"]
towns = ["Winterfell", "The Eyrie", "Riverrun", "Casterly Rock", "Pyke", "King's Landing", "Storm's End", "Highgarden", "Sunspear", "Harrenhall"]
towns = ["Harrenhall", "The Eyrie", "Storm's End", "Raventree Hall", "Dreadfort", "Stone Hedge", "Crakehall", "Griffin's Roost", "Castle Cerwyn", "Clegane's Keep", "Blackhaven", "Greenstone", "Deepwood Motte", "Pyke", "Hornwood", "Karhold", "Casterly Rock", "Seagard", "The New Castle", "Ashemark", "Sunspear", "Bear Island", "The Arbor", "Cape Wrath", "Winterfell", "Stonehelm", "Cornfield", "King's Landing", "Evenfall Hall", "Riverrun", "Highgarden", "Hornvale"]

def session_id():
    return session["user_id"]

def current_player():
    if "user_id" in session:
        return Player.query.filter_by(id=session["user_id"]).first()
    else:
        return None

def current_user():
    if "user_id" in session:
        return User.query.filter_by(id=session["user_id"]).first()
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
    new_town.doges = 1
    return new_town

# Assigns a new player to an existing user in the database
def generate_player_for_user(user):
    new_player = generate_new_player(user)
    db.session.add(new_player)
    db.session.commit()

# Gets the player from a user id, if it has no player, generate one.
def get_player_from_user_id(user_id):
    player = Player.query.filter_by(id=user_id).first()
    if not player:
        player = generate_new_player(user)
        db.session.add(player)
        db.session.commit()
    return player


# Runs an attack
def run_attack(attack):
    return True