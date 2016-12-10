# Flask
from flask import Flask
app = Flask(__name__, static_folder='static')
app.config.from_object('config')

# Flask extensions
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


# Blueprints
from app.dogecoin import dogecoin
from app.bitcoin import bitcoin
from app.auth import auth
from app.real_time_strategy import real_time_strategy
from app.shiba_chef import shiba_chef

# Initialize database
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(bitcoin)
app.register_blueprint(dogecoin)
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(real_time_strategy, url_prefix='/rts')
app.register_blueprint(shiba_chef, url_prefix='/shiba_chef')

if __name__ == "__main__":
    app.run(debug=True)