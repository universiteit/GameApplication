from flask import Blueprint, request, render_template, abort, jsonify
from jinja2 import TemplateNotFound

from datetime import datetime, timedelta
import jwt
from app.auth.attributes import secure, context
from app import db
from app import bcrypt

from app.auth.models.user import User

from random import randint

auth = Blueprint('auth', __name__, template_folder='templates/')

@auth.route('/login', methods=['POST'])
def index():
    login_info = request.get_json()

    user = User.query.filter_by(username=login_info['username']).first()

    if user is None:
        return 'Username or password was incorrect.', 401

    valid_password = bcrypt.check_password_hash(user.password, login_info['password'])
    if not valid_password:
        return 'Username or password was incorrect.', 401

    claims = {
        # Subject
        'sub' : user.id,
        # Issued at
        'iat' : datetime.utcnow(),
        # Expiry
        'exp' : datetime.utcnow() + timedelta(hours=1)
    }
    secret = 'secret'
    algorithm = 'HS256'
    token = jwt.encode(claims, secret, algorithm)

    ret = {
        'access_token' : token.decode('unicode_escape'),
        'token_type' : 'Bearer'
    }

    return jsonify(ret)

@auth.route('', methods=['POST'])
def create_account():
    account_details = request.get_json()
    username = account_details['username']
    password = bcrypt.generate_password_hash(account_details['password'])
    user = User(username, password)
    db.session.add(user)
    db.session.commit()
    return '', 200

@auth.route('/verify')
@secure()
def verify():
    print('\n', context())
    message = 'User with id: `' + str(context().user_id) + '` is logged in.'
    return message