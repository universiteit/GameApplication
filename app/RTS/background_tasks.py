import atexit, datetime
from app.RTS.models import *
from app import app, db
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

def update_towns():
    towns = Town.query.all()
    for town in towns:
        town.update_resources()
        town.update_upgrade()
        db.session.add(town)
    db.session.commit()

def update_attacks():
    now = datetime.datetime.now()
    attack = Attack.query.order_by(Attack.arrival_time).first()
    while attack and now <= attack.arrival_time:
        attack.resolve()
        attack = Attack.query.order_by(Attack.arrival_time).first()

def setup_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(func=update_towns,trigger=IntervalTrigger(seconds=5),id='town_update',replace_existing=True)
    scheduler.add_job(func=update_attacks,trigger=IntervalTrigger(seconds=5),id='attack_update',replace_existing=True)
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

if not app.debug:
    setup_scheduler()