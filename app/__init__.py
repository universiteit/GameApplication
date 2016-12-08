from flask import Flask
from app.db import db

from app.dogecoin import dogecoin
from app.bitcoin import bitcoin
from app.auth import auth
from app.RTS import rts

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(bitcoin)
app.register_blueprint(dogecoin)
app.register_blueprint(auth)
app.register_blueprint(rts, url_prefix='/rts')

if __name__ == "__main__":
    app.run(debug=True)