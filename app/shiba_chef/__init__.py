from flask import Blueprint, request
from app import db

from app.shiba_chef.models.highscore import Highscore

shiba_chef = Blueprint('Shiba Chef game', __name__, static_folder='static', template_folder='templates')


@shiba_chef.route('/')
def index():
    return shiba_chef.send_static_file('pages/index.html')

@shiba_chef.route('/score', methods=['POST'])
def send_highscore():
    content = request.get_json()
    user_id = request.session.id

    highscore = Highscore.filter_by(id=user_id).first()
    if highscore is None:
        highscore = Highscore(user_id, content.score)
        db.session.add(highscore)
        db.session.commit()
    elif content.score > highscore:
        highscore.highscore = content.score
        db.session.commit()


    return str(content), 200

# Static file routing
@shiba_chef.route('/<path:path>')
def serve_static_directory(path):
    return shiba_chef.send_static_file(path)