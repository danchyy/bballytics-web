from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.players import Players
from resources.seasons import Seasons
from resources.shotchart import Shotchart


def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    api.add_resource(Seasons, '/api/seasons')
    api.add_resource(Players, '/api/players')
    api.add_resource(Shotchart, '/api/shotchart')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port='4000', host='localhost')