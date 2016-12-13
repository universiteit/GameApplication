from flask import session, redirect
from app.RTS.models.player import Player

def session_id():
    return session["user_id"]

def current_player():
    if "user_id" in session
        return Player.query.filter_by(id=session["user_id"]).first()
    else:
        return None