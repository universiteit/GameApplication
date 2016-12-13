# required for db creation
from app.RTS.models.attack import Attack
from app.RTS.models.town import Town
from app.RTS.models.unit import Unit
from app.RTS.models.player import Player
from flask import Blueprint, render_template
import app.RTS.rts_config

real_time_strategy = Blueprint('Real time strategy game', __name__, static_folder='static', template_folder='templates')
rts = real_time_strategy

shit = Town("shit", "name", 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,None, None)

def static_file(file):
    return rts.send_static_file('pages/' + file)

@rts.route('/')
def index():
    return render_template('index.html', metal=100)
    #return static_file('index.html')

@rts.route('/townview/<town>')
def townview(town):
    return render_template("town_view.html", current_town = shit)

@rts.route('/town/<id>')
def town(id):
    return id