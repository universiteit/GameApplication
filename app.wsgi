#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/CoinApplication")

activate_this = '.pyenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import app as application
application.secret_key = '52441650bc72a8d1bd8ebd5605af4275b2178109y'