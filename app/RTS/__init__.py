# required for db creation
from flask import session
from app.RTS.models.attack import Attack
from app.RTS.models.town import Town
from app.RTS.models.unit import Unit
from app.RTS.models.player import Player
from flask import Blueprint, render_template, redirect


real_time_strategy = Blueprint('Real time strategy game', __name__, static_folder='static', template_folder='templates')
rts = real_time_strategy


def static_file(file):
    return rts.send_static_file('pages/' + file)

@rts.route('/towns/all')
def all_towns():
    if not ('user_id' in session):
            return redirect('auth/login')
    player = Player.query.filter_by(id=session['user_id']).first()
    if not player:
        return redirect('rts')

    return render_template('towns_view.html', towns = Town.query.all(), player = player)

@rts.route('/towns')
def player_towns():
    if not ('user_id' in session):
        return redirect(url_for('auth/login'))

    player = Player.query.filter_by(id=session['user_id']).first()
    if not player:
        return redirect(url_for('rts'))

    if (player):
        return render_template('towns_view.html', towns = player.towns, player=player)
    return render_template('404.html'), 404

import app.RTS.controllers.index_controller