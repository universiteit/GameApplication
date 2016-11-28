#!python3

from flask import Flask
from DogeCoinApplication import DogeCoinApplication
from BitCoinApplication import BitCoinApplication
from LoginSystem import LoginSystem

app = Flask(__name__)
app.register_blueprint(DogeCoinApplication)
app.register_blueprint(BitCoinApplication)
app.register_blueprint(LoginSystem)

# Flask parameters
host = "0.0.0.0"
port = "8070"

if __name__ == '__main__':
    app.run(host = host, port=port)