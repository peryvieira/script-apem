import requests
import re
import json
from bs4 import BeautifulSoup
from model.Ship import Ship

def  __get_table():
    url = "http://www.apem-ma.com.br/?module=shipmaneuvering"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find_all("tr")
    table_size = len(table)
    return table[3:table_size-1]

def format_data_ships(ships_target):
    all_ships = __get_table()
    response_ships = []

    for ship in all_ships:
        ship_formated = re.findall("(?<=>)(.*)(?=<)",str(ship))
        if ship_formated[0] in ships_target:
            ship_data = Ship(ship_formated)
            response_ships.append(json.dumps(ship_data.__dict__))
    return response_ships
