from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bitcoin = Blueprint('bitcoin', __name__, template_folder='templates')

@bitcoin.route('/bitcoin')
def index():
    return "Index page for bitcoin application"