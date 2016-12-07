from app import app
from config import *

if __name__ == "__main__":
    app.run(HOSTNAME, PORT, debug=DEBUG)