from app.RTS import rts
from app.RTS.helpers import current_player, generate_player_for_user, current_user
from app.auth.attributes import secure
from app.RTS.models import *
from flask import Blueprint, render_template, redirect, session

@rts.route('/create-player')
@secure(cookie_authorization=True)
def create_player():
    if current_player():
        return "", 500
    user = User.query.filter_by(id=session['user_id']).first()
    if user:
        generate_player_for_user(user)
        return redirect('rts')
    return redirect('auth')