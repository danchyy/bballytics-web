from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from utils.constants import SHOTS_PATH
from pathlib import  Path
import pandas as pd

class Players(Resource):

    def get(self):

        parser = RequestParser()
        parser.add_argument('season', type=str, required=False, default="2019-20")
        args = parser.parse_args()
        season = args['season']

        data_path = (Path(SHOTS_PATH) / season).with_suffix('.csv')

        players_df = pd.read_csv(data_path)
        unique_df: pd.DataFrame = players_df.drop_duplicates(subset="PLAYER_ID")
        unique_df = unique_df.loc[:, ["PLAYER_ID", "PLAYER_NAME"]].sort_values(by='PLAYER_NAME', ascending=True)
        return unique_df.to_dict(orient="records")