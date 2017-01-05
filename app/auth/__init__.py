from flask import Blueprint, request, render_template, abort, jsonify, session, redirect, send_from_directory
from jinja2 import TemplateNotFound

from datetime import datetime, timedelta
import jwt
from app.auth.attributes import secure, context
from app import db
from app import bcrypt

from app.auth.models.user import User
from random import randint

auth = Blueprint('auth', __name__, static_folder='static', template_folder='templates/')

#Waarom ziet ie mijn css file nou niet, potverdomme
#Ik doe het wel zo, don't judge
@auth.route('/static/<path:filename>')
def waarIsMijnCss(filename):
    return send_from_directory('.auth/static', filename)

@auth.route('/login', methods=['GET'])
def login():
    if 'user_id' in session:
        return render_template('library.html')
    return render_template('login.html')

@auth.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('auth/login')

@auth.route('/login', methods=['POST'])
def index():
    if (request.form):
        login_info = request.form
    else:
        login_info = request.get_json()

    user = User.query.filter_by(username=login_info['username']).first()

    if user is None:
        return "<meta http-equiv='refresh' content='2;URL=login' />Login failed. Try again.", 401

    valid_password = bcrypt.check_password_hash(user.password, login_info['password'])
    if not valid_password:
        return "<meta http-equiv='refresh' content='2;URL=login' />Login failed. Try again", 401

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

    if (request.form):
        session['user_id'] = user.id
        return "<meta http-equiv='refresh' content='3;URL=login' />Login successful. Continue in 3 seconds"
    else:
        return jsonify(ret)

@auth.route('', methods=['GET'])
def register():
    return render_template('login.html')

@auth.route('', methods=['POST'])
def create_account():
    if (request.form):
        account_details = request.form
    else:
        account_details = request.get_json()
    username = account_details['username']
    password = bcrypt.generate_password_hash(account_details['password'])
    user = User(username, password)
    db.session.add(user)
    try:
        db.session.commit()
        return "<meta http-equiv='refresh' content='3;URL=auth/login' />Account created successfully. Login in 3 seconds.", 200
    except:
        return"<meta http-equiv='refresh' content='3;URL=auth/login' />Oops! Something went wrong. Try again in 3 seconds."
@auth.route('/verify')
@secure()
def verify():
    print('\n', context())
    message = 'User with id: `' + str(context().user_id) + '` is logged in.'
    return message

@auth.route('/verify-cookie')
def verify_cookie():
    if 'user_id' in session:
        message = "User with id: '" + str(session["user_id"]) + "' is logged in."
    else:
        message = "No user is logged in."
    return message