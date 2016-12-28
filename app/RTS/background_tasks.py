import atexit, datetime
from app.RTS.models import *
from app import app, db
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

def update_towns():
    for town in towns:
        town.update_resources()
        town.update_upgrade()

def update_attacks():
    now = datetime.datetime.now()
    attack = Attack.query.order_by(Attack.arrival_time).first()
    while attack and attack.arrival_time < now:
        attack.resolve()
        attack = Attack.query.order_by(Attack.arrival_time).first()

if not app.debug:
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(func=update_towns,trigger=IntervalTrigger(seconds=5),id='town_update',replace_existing=True)
    scheduler.add_job(func=update_attacks,trigger=IntervalTrigger(seconds=5),id='town_update',replace_existing=True)
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())