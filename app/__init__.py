from flask import Flask


app = Flask(__name__, static_folder='static')


from app.dogecoin import dogecoin
from app.bitcoin import bitcoin
from app.auth import auth
from app.real_time_strategy import real_time_strategy

app.register_blueprint(bitcoin)
app.register_blueprint(dogecoin)
app.register_blueprint(auth)

app.register_blueprint(real_time_strategy, url_prefix='/rts')

if __name__ == "__main__":
    app.run(debug=True)