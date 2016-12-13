import random
from app import db
from app.RTS.models.player import Player
from app.RTS.models.town import Town
from app.auth.models.user import User
from app.RTS import rts
from flask import session, render_template

houses = ["Stark", "Arryn", "Tully", "Lannister", "Greyjoy", "Targaeryan", "Baratheon", "Tyrell", "Martell"]
towns = ["Winterfell", "The Eyrie", "Riverrun", "Casterly Rock", "Pyke", "King's Landing", "Storm's End", "Highgarden", "Sunspear"]

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


@rts.route('/')
def index():
    if not ('user_id' in session):
        return redirect(url_for('auth/login'))
    user = User.query.filter_by(id=session['user_id']).first()
    if not user:
        return "Credentials are not found!", 401
    player = Player.query.filter_by(id=session['user_id']).first()
    if not player:
        player = generate_new_player(user)
        db.session.add(player)
        db.session.commit()

    return render_template('index.html', player=player)
    #return static_file('index.html')