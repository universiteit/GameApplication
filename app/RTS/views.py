from app.RTS import rts
from app.RTS.helpers import current_player, generate_player_for_user
from app.auth.attributes import secure
from app.RTS.models import *
from flask import Blueprint, render_template, redirect, session

@rts.route('/towns/')
def all_towns():
    return render_template('views/all_towns_view.html', towns = Town.query.all(), player=current_player())

@rts.route('/house')
@secure(cookie_authorization=True)
def house():
    player = current_player()
    if not player:
        return redirect(url_for('rts'))
    return render_template('views/house_view.html', player=player)

@rts.route('/')
def index():
    return render_template('views/index.html', player=current_player())

@rts.route('/join', methods=['GET'])
@secure(cookie_authorization=True)
def join():
    player = current_player()
    if player:
        return redirect(url_for('rts'))
    else:
        return render_template('views/join.html')

@rts.route('/join', methods=['POST'])
@secure(cookie_authorization=True)
def create_player():
    if current_player():
        return "", 500
    user = User.query.filter_by(id=session['user_id']).first()
    if user:
        generate_player_for_user(user)
        return redirect(url_for('rts'))