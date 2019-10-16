# Import requests package
import requests
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.ffdb
data = ''
players = db['players']
# Enter week number
week = input()
# API Key in a environment variable
api_key = ENV.Api_key

def update_ppr_points():
    positions = ["QB","RB","WR","TE","K","DEF"]
    for position in positions:
        url = f"https://www.fantasyfootballnerd.com/service/weekly-rankings/json/{api_key}/{position}/{week}/1/"
        r = requests.get(url)
        json_data = r.json()
        for player in json_data['Rankings']:
            players.update_one({"playerId": player["playerId"]},{"$push": {"ppr_points": player["ppr"]}})
