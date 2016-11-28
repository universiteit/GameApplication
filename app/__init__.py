from flask import Flask
from dogecoin import dogecoin
from bitcoin import bitcoin
from auth import auth

app = Flask(__name__)
app.register_blueprint(bitcoin)
app.register_blueprint(dogecoin)
app.register_blueprint(auth)