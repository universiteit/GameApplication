#!/usr/bin/python3
import daemonize
import time

def process_server():
    while True:
        print("Server is still running...")
        time.sleep(1)

def run():
    pid = "tmp/test.pid"
    daemon = deamonize.Daemonize(app="run", pid=pid, action=process_server)
    daemon.start()

run()