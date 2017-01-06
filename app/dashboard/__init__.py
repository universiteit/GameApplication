from flask import Blueprint, request, render_template, abort, jsonify, session, redirect
from jinja2 import TemplateNotFound

from app import db
from app.shiba_chef.models.highscore import Highscore
from app.auth.models.user import User
from app.RTS.models.town import Town
from app.RTS.models.player import Player

from app.auth.attributes import secure
from collections import OrderedDict

dashboard = Blueprint('Dashboard', __name__, template_folder='templates', static_folder='static')


@dashboard.route('/', methods=['GET'])
@secure(cookie_authorization=True)
def index():
    return dashboard.send_static_file('dashboard.html')

def generate_shiba_chef_score():
    all = Highscore.query.join(User, Highscore.id == User.id)\
                .add_columns(User.username, Highscore.highscore)\
                .order_by(Highscore.highscore.desc())\
                .all()
    dic = {}
    for element in all:
        dic[element.username] = element.highscore
    return dic

def generate_ogot_score():

    score = db.func.count(User.username).label('score')
    all = Town.query\
                .join(User, Town.player_id == User.id)\
                .add_columns(User.username, score)\
                .group_by(User.username)\
                .order_by(score.desc())\
                .all()
    #return [{'username': x.username, 'score_ogot': x[2]} for x in all]
    dic = {}
    for element in all:
        dic[element.username] = element[2]
    return dic



@dashboard.route('scoreboard/', methods=['GET'])
def scoreboard():
    default = 'shiba_chef'
    order_by = request.args.get('order_by', default)
    
    ogot_scores = generate_ogot_score()
    shiba_scores = generate_shiba_chef_score()

    scores = {}
    for key in ogot_scores:
        scores[key] = { 'ogot' : ogot_scores[key], 'shiba_chef' : 0 }
    for key in shiba_scores:
        if key in scores:
            scores[key]['shiba_chef'] = shiba_scores[key]
        else:
            scores[key] = { 'ogot' : 0, 'shiba_chef': shiba_scores[key] }

    scores = sorted(scores.items(), key=lambda x: x[1][order_by], reverse=True)
    scores = OrderedDict(scores)
    return render_template('scoreboard.html', aids_list=scores)