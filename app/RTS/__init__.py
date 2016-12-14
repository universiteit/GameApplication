# required for db creation
from flask import session
from app.RTS.models import *
from flask import Blueprint, render_template, redirect
from app.auth.attributes import secure

real_time_strategy = Blueprint('Real time strategy game', __name__, static_folder='static', template_folder='templates')
rts = real_time_strategy

def static_file(file):
    return rts.send_static_file('pages/' + file)


import app.RTS.views
import app.RTS.posts