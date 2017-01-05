from flask import Blueprint, request, render_template, abort, jsonify, session, redirect
from jinja2 import TemplateNotFound

from app import db
from app.shiba_chef.models.highscore import Highscore
from app.auth.models.user import User
from app.RTS.models.town import Town
from app.RTS.models.player import Player

dashboard = Blueprint('Dashboard', __name__, template_folder='templates', static_folder='static')


@dashboard.route('/', methods=['GET'])
def index():
    return dashboard.send_static_file('dashboard.html')

def generate_shiba_chef_score():
    all = Highscore.query.join(User, Highscore.id == User.id)\
                .add_columns(User.username, Highscore.highscore)\
                .all()
    return [{'name': x.username, 'score': x.highscore} for x in all]

def generate_ogot_score():
    all = Town.query\
                .join(User, Town.player_id == User.id)\
                .add_columns(User.username, db.func.count(User.username))\
                .group_by(User.username)\
                .all()
    return [{'name': x.username, 'score': x[2]} for x in all]


@dashboard.route('scoreboard/', methods=['GET'])
def scoreboard():
    default = 'shiba_chef'
    selected_list = request.args.get('game', default)

    func = None
    if selected_list == 'ogot':
        func = generate_ogot_score
    else:
        func = generate_shiba_chef_score
    
    scores = func()
    return render_template('scoreboard.html', aids_list=scores)