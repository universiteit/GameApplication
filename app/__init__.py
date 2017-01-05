# Flask
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

# Flask extensions
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

# Blueprints
from app.auth import auth
from app.RTS import rts

# Initialize database
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(rts, url_prefix='/rts')
app.secret_key = "secret test key"

if __name__ == "__main__":
    app.run(debug=True)