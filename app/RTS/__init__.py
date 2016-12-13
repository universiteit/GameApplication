# required for db creation
from flask import session
from app.RTS.models.attack import Attack
from app.RTS.models.town import Town
from app.RTS.models.unit import Unit
from app.RTS.models.player import Player
from flask import Blueprint, render_template, redirect
from app.auth.attributes import secure 
from app.RTS.helpers import session_id, current_player

real_time_strategy = Blueprint('Real time strategy game', __name__, static_folder='static', template_folder='templates')
rts = real_time_strategy

def static_file(file):
    return rts.send_static_file('pages/' + file)

@rts.route('/towns/')
def all_towns():
    return render_template('all_towns_view.html', towns = Town.query.all(), player=current_player())

@rts.route('/player-towns')
@secure()
def player_towns():
    player = current_player()
    if not player:
        return redirect(url_for('rts'))
    return render_template('player_towns_view.html', towns = player.towns, player=player)

import app.RTS.controllers.index_controller