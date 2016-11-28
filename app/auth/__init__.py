from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

auth = Blueprint('auth', __name__, template_folder='templates/')

@auth.route('/login')
def index():
    return "Login page"