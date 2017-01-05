from flask import Blueprint, request, session
from app import db
from app.auth.attributes import secure, context

from app.shiba_chef.models.highscore import Highscore

shiba_chef = Blueprint('Shiba Chef game', __name__, static_folder='static', template_folder='templates')


@shiba_chef.route('/')
@secure(cookie_authorization=True, auto_redirect=True)
def index():
    return shiba_chef.send_static_file('pages/index.html')

@shiba_chef.route('/score', methods=['POST'])
@secure(cookie_authorization=True, auto_redirect=False)
def send_highscore():
    content = request.get_json()
    user_id = session['user_id']
    score = content['score']

    highscore = Highscore.query.filter_by(id=user_id).first()
    if highscore is None:
        highscore = Highscore(user_id, score)
        db.session.add(highscore)
        db.session.commit()
    elif score > highscore.highscore:
        highscore.highscore = score
        db.session.commit()

    all = [{ 'id': x.id, 'score': x.highscore} for x in Highscore.query.all()]
    return str(all), 200

# Static file routing
@shiba_chef.route('/<path:path>')
def serve_static_directory(path):
    return shiba_chef.send_static_file(path)