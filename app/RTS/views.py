from app.RTS import rts
from app.RTS.helpers import current_player, generate_player_for_user, current_user
from app.auth.attributes import secure
from app.RTS.models import *
from flask import Blueprint, render_template, redirect, session

shit = Town("shit", "name", 0, 0, 0, 1, 3, 1, 1, 0, 1, 0, 0, 0, 0,None, None)

@rts.route('/towns/')
def all_towns():
    return render_template('views/all_towns_view.html', towns = Town.query.all(), user=current_user())

@rts.route('/house')
@secure(cookie_authorization=True)
def house():
    player = current_player()
    if not player:
        return redirect('rts')
    return render_template('views/house_view.html', player=player, user=player.user)

@rts.route('/')
def index():
    return render_template('views/index.html', user=current_user(), player=current_player())

@rts.route('/join')
@secure(cookie_authorization=True)
def join():
    player = current_player()
    if player:
        return redirect('rts')
    else:
        return render_template('views/join.html', user=current_user())

@rts.route('/townview/<town>')
def townview(town):
    return render_template("views/town_view.html", current_town = shit)