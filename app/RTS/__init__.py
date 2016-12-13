# required for db creation
from app.RTS.models.attack import Attack
from app.RTS.models.town import Town
from app.RTS.models.unit import Unit
from app.RTS.models.player import Player
from flask import Blueprint, render_template

real_time_strategy = Blueprint('Real time strategy game', __name__, static_folder='static', template_folder='templates')
rts = real_time_strategy

def static_file(file):
    return rts.send_static_file('pages/' + file)

@rts.route('/')
def index():
    return render_template('index.html', metal=100)
    #return static_file('index.html')

@rts.route('/town/<id>')
def town(id):
    return id