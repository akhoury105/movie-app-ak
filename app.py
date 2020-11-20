from flask import Flask
from models import setup_db

def create_app():

    app = Flask(__name__)
    setup_db(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()