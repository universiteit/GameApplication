# Flask
from flask import Flask
from celery import Celery
app = Flask(__name__, static_folder='static')
app.config.from_object('config')

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

# Flask extensions
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

flask_app.config.update(
    CELERY_BROKER_URL='pyamqp://guest@localhost//',
)
celery_app = make_celery(flask_app)

# Blueprints
from app.auth import auth
from app.RTS import rts
from app.docs import docs
from app.shiba_chef import shiba_chef

# Initialize database
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(rts, url_prefix='/rts')
app.register_blueprint(docs, url_prefix='/docs')
app.register_blueprint(shiba_chef, url_prefix='/shiba_chef')

app.secret_key = "secret test key"



if __name__ == "__main__":
    app.run(debug=True)