from flask import Blueprint
from app import db

shiba_chef = Blueprint('Shiba Chef game', __name__, static_folder='static', template_folder='templates')

# Static file routing
@shiba_chef.route('/<path:path>')
def serve_static_directory(path):
    return shiba_chef.send_static_file(path)

@shiba_chef.route('/')
def index():
    return shiba_chef.send_static_file('pages/index.html')