import os

from flask_restful import Resource
from utils.constants import SHOTS_PATH


class Seasons(Resource):

    def get(self):
        paths = os.listdir(SHOTS_PATH)
        return [path.split(".")[0] for path in paths if ".csv" in path]
