from pathlib import Path
import  io
from flask import make_response
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from matplotlib.backends.backend_agg import FigureCanvasAgg
import  pandas as pd
from utils.constants import SHOTS_PATH, LEAGUE_AVG_PATH
from utils.shotchart_tools import plot_shotchart, create_bins
from nba_api.stats.static.players import find_player_by_id


class Shotchart(Resource):

    def get(self):
        parser = RequestParser()
        parser.add_argument('season', type=str, required=True)
        parser.add_argument('playerId', type=int, required=True)

        args = parser.parse_args()
        season = args['season']
        player_id = args['playerId']
        player_name = find_player_by_id(player_id=player_id)["full_name"]

        data_path = (Path(SHOTS_PATH) / season).with_suffix('.csv')

        players_df = pd.read_csv(data_path)
        target_player_df = players_df.loc[players_df.PLAYER_ID == player_id]

        league_avg = (Path(LEAGUE_AVG_PATH) / season).with_suffix('.csv')
        league_avg_df = pd.read_csv(league_avg)
        binned_df = create_bins(data_frame=target_player_df, league_average=league_avg_df)

        figure = plot_shotchart(original_df=target_player_df, data_frame=binned_df, title=f"Shotchart for {player_name} in {season} season")
        canvas = FigureCanvasAgg(figure)
        output = io.BytesIO()
        canvas.print_png(output)
        response = make_response(output.getvalue())
        response.headers["Content-Type"] = "image/png"
        return response