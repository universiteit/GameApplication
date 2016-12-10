#!/usr/bin/python3

app_name = 'GameApplication'
# Initialize virtualenv

activate_this = '/var/www/' + GameApplication + '/.venv/bin/activate_this.py'
with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

# wsgi config
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/var/www/' + app_name)

from app import app as application
application.secret_key = '52441650bc72a8d1bd8ebd5605af4275b2178109y'