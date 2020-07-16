from flask import Blueprint, jsonify, request
from .App import scrape

main = Blueprint('main', __name__)

@main.route('/give_id', methods=['POST'])

def give_id():
    id_data = request.get_json()

    name, picture, level, badge, xp, nxp, private  = scrape(id_data['SteamId'])

    obj = {
        "name" : name,
        "picture" : picture,
        "level" : level,
        "badge" : badge,
        "xp" : xp,
        "nxp" : nxp,
        "private" : private
    }

    return obj, 201

