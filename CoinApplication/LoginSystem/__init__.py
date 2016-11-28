from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

LoginSystem = Blueprint('LoginSystem', __name__, template_folder='templates')

@LoginSystem.route('/login')
def index():
    return "Login page"