from flask import Blueprint

docs = Blueprint('docs', __name__, static_folder='static', template_folder='templates')


@docs.route('/')
def get_docs():
    return docs.send_static_file('docs.html')