from app.RTS import rts
from app.RTS.helpers import current_player, generate_player_for_user, current_user
from app.auth.attributes import secure
from app.RTS.models import *
from app.auth.models.user import User
from flask import Blueprint, render_template, redirect, session, request
from app import db


@rts.route('/create-player', methods=['POST'])
@secure(cookie_authorization=True)
def create_player():
    if current_player():
        return "", 500
    user = User.query.filter_by(id=session['user_id']).first()
    if user:
        generate_player_for_user(user)
        return redirect('rts')
    return redirect('auth')

#TODO: Check if the user has enough resources.
@rts.route('/purchase-unit', methods=['POST'])
def create_unit():
    cavalry_amount = int(request.form['amount_of_cavalry'])
    knight_amount = int(request.form['amount_of_knights'])
    pikemen_amount = int(request.form['amount_of_pikemen'])
    id = int(request.form['townid'])
    town = Town.query.filter_by(id = id).first()
    town.add_units(knight_amount, cavalry_amount, pikemen_amount)
    db.session.add(town)
    db.session.commit()
    return redirect('rts/town/' + str(id))

#TODO: Check if the user has enough resources.
@rts.route('/purchase-building', methods=['POST'])
def upgrade_building():
    building = request.form['building-name']
    id = int(request.form['townid'])
    town = Town.query.filter_by(id = id).first()
    if town.add_upgrade(building):
        db.session.add(town)
        db.session.commit()
    return redirect('rts/town/' + str(id))