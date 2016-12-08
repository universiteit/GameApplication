from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from app.auth.attributes import secure, context

auth = Blueprint('auth', __name__, template_folder='templates/')

@auth.route('/login')
@secure()
def index():
    print('in index')
    return "Login page test" + str(context.user)