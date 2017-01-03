from app.RTS import rts
from app.RTS.helpers import current_player, generate_player_for_user, current_user
from app.auth.attributes import secure
from app.RTS.models import *
from flask import Blueprint, render_template, redirect, session, request

@rts.route('/towns/')
@secure(cookie_authorization=True)
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
@secure(cookie_authorization=True)
def index():
    return render_template('views/index.html', user=current_user(), player=current_player())

@rts.route('/town/<town_id>')
@secure(cookie_authorization=True)
def townview(town_id):
    player = current_player()
    town = Town.query.filter_by(id=int(town_id)).first()
    if town.player == player:
        return render_template("views/town_view.html", current_town = town, user=current_user(), towns=Town.query.all())
    else:
        return render_template("views/town_preview.html", current_town = town, user=current_user())

@rts.route('/attacks')
@secure(cookie_authorization=True)
def attackview():
    player = current_player()
    if not player:
        return redirect("rts")
    attacks = Attack.query.filter(Attack.player_id == player.id).all()
    return render_template("views/attack_view.html",user = player.user, player = player, attacks = attacks)
