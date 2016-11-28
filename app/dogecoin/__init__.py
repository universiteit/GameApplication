from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

dogecoin = Blueprint('dogecoin', __name__, template_folder='templates')

@dogecoin.route('/dogecoin')
def index():
    return "Index page for dogecoin application"