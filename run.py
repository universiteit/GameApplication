from time import sleep
from daemonize import Daemonize
from app import app
from config import *
pid = "/tmp/server.pid"

def main():
    app.run(HOSTNAME, PORT)

daemon = Daemonize(app="coinapplication_server", pid=pid, action=main)
daemon.start()