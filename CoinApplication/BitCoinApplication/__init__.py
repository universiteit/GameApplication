from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

BitCoinApplication = Blueprint('BitCoinApplication', __name__, template_folder='templates')

@BitCoinApplication.route('/bitcoin')
def index():
    return "Index page for bitcoin application"