from app.RTS import rts
from app.RTS.helpers import current_player, generate_player_for_user
from app.auth.attributes import secure
from app.RTS.models import *
from flask import Blueprint, render_template, redirect, session, request

shit = Town("shit", "name", 0, 0, 0, 1, 3, 1, 1, 0, 1, 0, 0, 0, 0,None, None)

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

@rts.route('/jeffsmoeder', methods=['POST'])
def create_unit():
    cavalry_amount = int(request.form['amount_of_cavalry'])
    knight_amount = int(request.form['amount_of_knights'])
    pikemen_amount = int(request.form['amount_of_pikemen'])
    id = int(request.form['townid'])
    town = Town.query.filter_by(id = id).first()
    town.add_units(knight_amount, cavalry_amount, pikemen_amount)
    return redirect('rts/townview/' + id)


@rts.route('/join', methods=['POST'])
@secure(cookie_authorization=True)
def create_player():
    if current_player():
        return "", 500
    user = User.query.filter_by(id=session['user_id']).first()
    if user:
        generate_player_for_user(user)
        return redirect(url_for('rts'))

@rts.route('/townview/<town>')
def townview(town):
    return render_template("views/town_view.html", current_town = shit)
