from flask import Blueprint, render_template
from app.db import db
from app.real_time_strategy.models.unit import Unit
from app.real_time_strategy.models.town import Town
from app.real_time_strategy.models.user import User

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
    admin = User('admin', 'shiba inu')
    guest = User('guest', 'akita inu')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

    return "dix"