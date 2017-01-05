import atexit, datetime
from app.RTS.models import *
from app import app, db
from celery import Celery

celery_app = Celery('tasks', broker='pyamqp://guest@localhost//')

@celery_app.task
def update_towns():
    towns = Town.query.all()
    for town in towns:
        town.update_resources()
        town.update_upgrade()
        db.session.add(town)
    db.session.commit()

@celery_app.task
def update_attacks():
    now = datetime.datetime.now()
    attack = Attack.query.order_by(Attack.arrival_time).first()
    while attack and now >= attack.arrival_time:
        attack.resolve()
        attack = Attack.query.order_by(Attack.arrival_time).first()

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    if not os.environ["TEST"]:
        sender.add_periodic_task(2.0, update_towns.s())
        sender.add_periodic_task(2.0, update_attacks.s())