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