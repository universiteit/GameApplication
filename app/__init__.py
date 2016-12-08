from flask import Flask
from app.db import db

from app.dogecoin import dogecoin
from app.bitcoin import bitcoin
from app.auth import auth
from app.real_time_strategy import real_time_strategy

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(bitcoin)
app.register_blueprint(dogecoin)
app.register_blueprint(auth)
app.register_blueprint(real_time_strategy, url_prefix='/rts')

if __name__ == "__main__":
    app.run(debug=True)