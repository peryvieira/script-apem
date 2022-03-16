from flask import Flask, request
from scrapping import format_data_ships
import json

app = Flask(__name__)

@app.route("/")
def get_ship():
    request_ships = request.get_json()['ships']
    response = format_data_ships(request_ships)
    return json.dumps(response).replace("\\","")
      