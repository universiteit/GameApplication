from time import sleep
from daemonize import Daemonize
from app import app
from config import *
import sys
import logging

pid = "/tmp/server.pid"

def main():
    app.debug == True
    handler = logging.FileHandler("/tmp/coinapplication.log", "w+")
    log = logging.getLogger('werkzeug')
    log.addHandler(handler)
    app.run(HOSTNAME, PORT)

daemon = Daemonize(app="coinapplication_server", pid=pid, action=main)
daemon.start()