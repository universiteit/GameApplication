#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/CoinApplication/")

from app import app as application
application.secret_key = '52441650bc72a8d1bd8ebd5605af4275b2178109y'