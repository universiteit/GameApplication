import atexit, datetime
from app.RTS.models import *
from app import app
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

def update_towns():
    for town in towns:
        town.update_resources()
        town.update_upgrade()

if not app.debug:
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(func=print_date_time,trigger=IntervalTrigger(seconds=5),id='town_update',replace_existing=True)

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())