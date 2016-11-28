from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

DogeCoinApplication = Blueprint('DogeCoinApplication', __name__, template_folder='templates')

@DogeCoinApplication.route('/dogecoin')
def index():
    return "Index page for dogecoin application"